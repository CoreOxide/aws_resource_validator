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
from aws_resource_validator.pydantic_models.amp_constants import *

class AlertManagerDefinitionStatusTypeDef(BaseModel):
    statusCode: AlertManagerDefinitionStatusCodeType
    statusReason: Optional[str] = None

class AmpConfigurationTypeDef(BaseModel):
    workspaceArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateLoggingConfigurationRequestRequestTypeDef(BaseModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None

class LoggingConfigurationStatusTypeDef(BaseModel):
    statusCode: LoggingConfigurationStatusCodeType
    statusReason: Optional[str] = None

class RuleGroupsNamespaceStatusTypeDef(BaseModel):
    statusCode: RuleGroupsNamespaceStatusCodeType
    statusReason: Optional[str] = None

class ScraperStatusTypeDef(BaseModel):
    statusCode: ScraperStatusCodeType

class CreateWorkspaceRequestRequestTypeDef(BaseModel):
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class WorkspaceStatusTypeDef(BaseModel):
    statusCode: WorkspaceStatusCodeType

class DeleteAlertManagerDefinitionRequestRequestTypeDef(BaseModel):
    workspaceId: str
    clientToken: Optional[str] = None

class DeleteLoggingConfigurationRequestRequestTypeDef(BaseModel):
    workspaceId: str
    clientToken: Optional[str] = None

class DeleteRuleGroupsNamespaceRequestRequestTypeDef(BaseModel):
    name: str
    workspaceId: str
    clientToken: Optional[str] = None

class DeleteScraperRequestRequestTypeDef(BaseModel):
    scraperId: str
    clientToken: Optional[str] = None

class DeleteWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str
    clientToken: Optional[str] = None

class DescribeAlertManagerDefinitionRequestRequestTypeDef(BaseModel):
    workspaceId: str

class DescribeLoggingConfigurationRequestRequestTypeDef(BaseModel):
    workspaceId: str

class DescribeRuleGroupsNamespaceRequestRequestTypeDef(BaseModel):
    name: str
    workspaceId: str

class DescribeScraperRequestRequestTypeDef(BaseModel):
    scraperId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeWorkspaceRequestRequestTypeDef(BaseModel):
    workspaceId: str

class EksConfigurationPaginatorTypeDef(BaseModel):
    clusterArn: str
    subnetIds: List[str]
    securityGroupIds: Optional[List[str]] = None

class EksConfigurationTypeDef(BaseModel):
    clusterArn: str
    subnetIds: Sequence[str]
    securityGroupIds: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRuleGroupsNamespacesRequestRequestTypeDef(BaseModel):
    workspaceId: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListScrapersRequestRequestTypeDef(BaseModel):
    filters: Optional[Mapping[str, Sequence[str]]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListWorkspacesRequestRequestTypeDef(BaseModel):
    alias: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLoggingConfigurationRequestRequestTypeDef(BaseModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None

class UpdateWorkspaceAliasRequestRequestTypeDef(BaseModel):
    workspaceId: str
    alias: Optional[str] = None
    clientToken: Optional[str] = None

class AlertManagerDefinitionDescriptionTypeDef(BaseModel):
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    status: AlertManagerDefinitionStatusTypeDef

class DestinationTypeDef(BaseModel):
    ampConfiguration: Optional[AmpConfigurationTypeDef] = None

class CreateAlertManagerDefinitionRequestRequestTypeDef(BaseModel):
    data: BlobTypeDef
    workspaceId: str
    clientToken: Optional[str] = None

class CreateRuleGroupsNamespaceRequestRequestTypeDef(BaseModel):
    data: BlobTypeDef
    name: str
    workspaceId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class PutAlertManagerDefinitionRequestRequestTypeDef(BaseModel):
    data: BlobTypeDef
    workspaceId: str
    clientToken: Optional[str] = None

class PutRuleGroupsNamespaceRequestRequestTypeDef(BaseModel):
    data: BlobTypeDef
    name: str
    workspaceId: str
    clientToken: Optional[str] = None

class ScrapeConfigurationTypeDef(BaseModel):
    configurationBlob: Optional[BlobTypeDef] = None

class CreateAlertManagerDefinitionResponseTypeDef(BaseModel):
    status: AlertManagerDefinitionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultScraperConfigurationResponseTypeDef(BaseModel):
    configuration: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAlertManagerDefinitionResponseTypeDef(BaseModel):
    status: AlertManagerDefinitionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoggingConfigurationResponseTypeDef(BaseModel):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationMetadataTypeDef(BaseModel):
    createdAt: datetime
    logGroupArn: str
    modifiedAt: datetime
    status: LoggingConfigurationStatusTypeDef
    workspace: str

class UpdateLoggingConfigurationResponseTypeDef(BaseModel):
    status: LoggingConfigurationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupsNamespaceResponseTypeDef(BaseModel):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuleGroupsNamespaceResponseTypeDef(BaseModel):
    arn: str
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleGroupsNamespaceDescriptionTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    data: bytes
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Optional[Dict[str, str]] = None

class RuleGroupsNamespaceSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    modifiedAt: datetime
    name: str
    status: RuleGroupsNamespaceStatusTypeDef
    tags: Optional[Dict[str, str]] = None

class CreateScraperResponseTypeDef(BaseModel):
    arn: str
    scraperId: str
    status: ScraperStatusTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteScraperResponseTypeDef(BaseModel):
    scraperId: str
    status: ScraperStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceResponseTypeDef(BaseModel):
    arn: str
    kmsKeyArn: str
    status: WorkspaceStatusTypeDef
    tags: Dict[str, str]
    workspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkspaceDescriptionTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    status: WorkspaceStatusTypeDef
    workspaceId: str
    alias: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    prometheusEndpoint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class WorkspaceSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    status: WorkspaceStatusTypeDef
    workspaceId: str
    alias: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class DescribeScraperRequestScraperActiveWaitTypeDef(BaseModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeScraperRequestScraperDeletedWaitTypeDef(BaseModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeWorkspaceRequestWorkspaceActiveWaitTypeDef(BaseModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeWorkspaceRequestWorkspaceDeletedWaitTypeDef(BaseModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class SourcePaginatorTypeDef(BaseModel):
    eksConfiguration: Optional[EksConfigurationPaginatorTypeDef] = None

class SourceTypeDef(BaseModel):
    eksConfiguration: Optional[EksConfigurationTypeDef] = None

class ListRuleGroupsNamespacesRequestListRuleGroupsNamespacesPaginateTypeDef(BaseModel):
    workspaceId: str
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScrapersRequestListScrapersPaginateTypeDef(BaseModel):
    filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspacesRequestListWorkspacesPaginateTypeDef(BaseModel):
    alias: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAlertManagerDefinitionResponseTypeDef(BaseModel):
    alertManagerDefinition: AlertManagerDefinitionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoggingConfigurationResponseTypeDef(BaseModel):
    loggingConfiguration: LoggingConfigurationMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRuleGroupsNamespaceResponseTypeDef(BaseModel):
    ruleGroupsNamespace: RuleGroupsNamespaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleGroupsNamespacesResponseTypeDef(BaseModel):
    nextToken: str
    ruleGroupsNamespaces: List[RuleGroupsNamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceResponseTypeDef(BaseModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkspacesResponseTypeDef(BaseModel):
    nextToken: str
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScraperSummaryPaginatorTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    destination: DestinationTypeDef
    lastModifiedAt: datetime
    roleArn: str
    scraperId: str
    source: SourcePaginatorTypeDef
    status: ScraperStatusTypeDef
    alias: Optional[str] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class CreateScraperRequestRequestTypeDef(BaseModel):
    destination: DestinationTypeDef
    scrapeConfiguration: ScrapeConfigurationTypeDef
    source: SourceTypeDef
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ScraperDescriptionTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    destination: DestinationTypeDef
    lastModifiedAt: datetime
    roleArn: str
    scrapeConfiguration: ScrapeConfigurationTypeDef
    scraperId: str
    source: SourceTypeDef
    status: ScraperStatusTypeDef
    alias: Optional[str] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ScraperSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    destination: DestinationTypeDef
    lastModifiedAt: datetime
    roleArn: str
    scraperId: str
    source: SourceTypeDef
    status: ScraperStatusTypeDef
    alias: Optional[str] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListScrapersResponsePaginatorTypeDef(BaseModel):
    nextToken: str
    scrapers: List[ScraperSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScraperResponseTypeDef(BaseModel):
    scraper: ScraperDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListScrapersResponseTypeDef(BaseModel):
    nextToken: str
    scrapers: List[ScraperSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

