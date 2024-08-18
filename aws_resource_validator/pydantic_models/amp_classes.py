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
from aws_resource_validator.pydantic_models.amp_constants import *

class AlertManagerDefinitionStatusTypeDef(BaseValidatorModel):
    statusCode: AlertManagerDefinitionStatusCodeType
    statusReason: Optional[str] = None

class AmpConfigurationTypeDef(BaseValidatorModel):
    workspaceArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None

class LoggingConfigurationStatusTypeDef(BaseValidatorModel):
    statusCode: LoggingConfigurationStatusCodeType
    statusReason: Optional[str] = None

class RuleGroupsNamespaceStatusTypeDef(BaseValidatorModel):
    statusCode: RuleGroupsNamespaceStatusCodeType
    statusReason: Optional[str] = None

class ScraperStatusTypeDef(BaseValidatorModel):
    statusCode: ScraperStatusCodeType

class CreateWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class WorkspaceStatusTypeDef(BaseValidatorModel):
    statusCode: WorkspaceStatusCodeType

class DeleteAlertManagerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None

class DeleteLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None

class DeleteRuleGroupsNamespaceRequestRequestTypeDef(BaseValidatorModel):
    name: str
    workspaceId: str
    clientToken: Optional[str] = None

class DeleteScraperRequestRequestTypeDef(BaseValidatorModel):
    scraperId: str
    clientToken: Optional[str] = None

class DeleteWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    clientToken: Optional[str] = None

class DescribeAlertManagerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class DescribeLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class DescribeRuleGroupsNamespaceRequestRequestTypeDef(BaseValidatorModel):
    name: str
    workspaceId: str

class DescribeScraperRequestRequestTypeDef(BaseValidatorModel):
    scraperId: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeWorkspaceRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str

class EksConfigurationPaginatorTypeDef(BaseValidatorModel):
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

class ListRuleGroupsNamespacesRequestRequestTypeDef(BaseValidatorModel):
    workspaceId: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListScrapersRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[str, Sequence[str]]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListWorkspacesRequestRequestTypeDef(BaseValidatorModel):
    alias: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    logGroupArn: str
    workspaceId: str
    clientToken: Optional[str] = None

class UpdateWorkspaceAliasRequestRequestTypeDef(BaseValidatorModel):
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

class CreateAlertManagerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    workspaceId: str
    clientToken: Optional[str] = None

class CreateRuleGroupsNamespaceRequestRequestTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    name: str
    workspaceId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class PutAlertManagerDefinitionRequestRequestTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    workspaceId: str
    clientToken: Optional[str] = None

class PutRuleGroupsNamespaceRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeScraperRequestScraperActiveWaitTypeDef(BaseValidatorModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeScraperRequestScraperDeletedWaitTypeDef(BaseValidatorModel):
    scraperId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeWorkspaceRequestWorkspaceActiveWaitTypeDef(BaseValidatorModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeWorkspaceRequestWorkspaceDeletedWaitTypeDef(BaseValidatorModel):
    workspaceId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class SourcePaginatorTypeDef(BaseValidatorModel):
    eksConfiguration: Optional[EksConfigurationPaginatorTypeDef] = None

class SourceTypeDef(BaseValidatorModel):
    eksConfiguration: Optional[EksConfigurationTypeDef] = None

class ListRuleGroupsNamespacesRequestListRuleGroupsNamespacesPaginateTypeDef(BaseValidatorModel):
    workspaceId: str
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScrapersRequestListScrapersPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Mapping[str, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkspacesRequestListWorkspacesPaginateTypeDef(BaseValidatorModel):
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
    nextToken: str
    ruleGroupsNamespaces: List[RuleGroupsNamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceResponseTypeDef(BaseValidatorModel):
    workspace: WorkspaceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkspacesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    workspaces: List[WorkspaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScraperSummaryPaginatorTypeDef(BaseValidatorModel):
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

class CreateScraperRequestRequestTypeDef(BaseValidatorModel):
    destination: DestinationTypeDef
    scrapeConfiguration: ScrapeConfigurationTypeDef
    source: SourceTypeDef
    alias: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ScraperDescriptionTypeDef(BaseValidatorModel):
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

class ScraperSummaryTypeDef(BaseValidatorModel):
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

class ListScrapersResponsePaginatorTypeDef(BaseValidatorModel):
    nextToken: str
    scrapers: List[ScraperSummaryPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScraperResponseTypeDef(BaseValidatorModel):
    scraper: ScraperDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListScrapersResponseTypeDef(BaseValidatorModel):
    nextToken: str
    scrapers: List[ScraperSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

