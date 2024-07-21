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
from aws_resource_validator.pydantic_models.route53_recovery_readiness_constants import *

class CellOutputTypeDef(BaseModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Optional[Dict[str, str]] = None

class CreateCellRequestRequestTypeDef(BaseModel):
    CellName: str
    Cells: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateCrossAccountAuthorizationRequestRequestTypeDef(BaseModel):
    CrossAccountAuthorization: str

class CreateReadinessCheckRequestRequestTypeDef(BaseModel):
    ReadinessCheckName: str
    ResourceSetName: str
    Tags: Optional[Mapping[str, str]] = None

class CreateRecoveryGroupRequestRequestTypeDef(BaseModel):
    RecoveryGroupName: str
    Cells: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteCellRequestRequestTypeDef(BaseModel):
    CellName: str

class DeleteCrossAccountAuthorizationRequestRequestTypeDef(BaseModel):
    CrossAccountAuthorization: str

class DeleteReadinessCheckRequestRequestTypeDef(BaseModel):
    ReadinessCheckName: str

class DeleteRecoveryGroupRequestRequestTypeDef(BaseModel):
    RecoveryGroupName: str

class DeleteResourceSetRequestRequestTypeDef(BaseModel):
    ResourceSetName: str

class GetArchitectureRecommendationsRequestRequestTypeDef(BaseModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RecommendationTypeDef(BaseModel):
    RecommendationText: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetCellReadinessSummaryRequestRequestTypeDef(BaseModel):
    CellName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ReadinessCheckSummaryTypeDef(BaseModel):
    Readiness: Optional[ReadinessType] = None
    ReadinessCheckName: Optional[str] = None

class GetCellRequestRequestTypeDef(BaseModel):
    CellName: str

class GetReadinessCheckRequestRequestTypeDef(BaseModel):
    ReadinessCheckName: str

class GetReadinessCheckResourceStatusRequestRequestTypeDef(BaseModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetReadinessCheckStatusRequestRequestTypeDef(BaseModel):
    ReadinessCheckName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MessageTypeDef(BaseModel):
    MessageText: Optional[str] = None

class ResourceResultTypeDef(BaseModel):
    LastCheckedTimestamp: datetime
    Readiness: ReadinessType
    ComponentId: Optional[str] = None
    ResourceArn: Optional[str] = None

class GetRecoveryGroupReadinessSummaryRequestRequestTypeDef(BaseModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetRecoveryGroupRequestRequestTypeDef(BaseModel):
    RecoveryGroupName: str

class GetResourceSetRequestRequestTypeDef(BaseModel):
    ResourceSetName: str

class ListCellsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCrossAccountAuthorizationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListReadinessChecksRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ReadinessCheckOutputTypeDef(BaseModel):
    ReadinessCheckArn: str
    ResourceSet: str
    ReadinessCheckName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListRecoveryGroupsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RecoveryGroupOutputTypeDef(BaseModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Optional[Dict[str, str]] = None

class ListResourceSetsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRulesOutputTypeDef(BaseModel):
    ResourceType: str
    RuleDescription: str
    RuleId: str

class ListRulesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None

class ListTagsForResourcesRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class NLBResourceTypeDef(BaseModel):
    Arn: Optional[str] = None

class R53ResourceRecordTypeDef(BaseModel):
    DomainName: Optional[str] = None
    RecordSetId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateCellRequestRequestTypeDef(BaseModel):
    CellName: str
    Cells: Sequence[str]

class UpdateReadinessCheckRequestRequestTypeDef(BaseModel):
    ReadinessCheckName: str
    ResourceSetName: str

class UpdateRecoveryGroupRequestRequestTypeDef(BaseModel):
    Cells: Sequence[str]
    RecoveryGroupName: str

class CreateCellResponseTypeDef(BaseModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCrossAccountAuthorizationResponseTypeDef(BaseModel):
    CrossAccountAuthorization: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReadinessCheckResponseTypeDef(BaseModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecoveryGroupResponseTypeDef(BaseModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCellResponseTypeDef(BaseModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadinessCheckResponseTypeDef(BaseModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryGroupResponseTypeDef(BaseModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCellsResponseTypeDef(BaseModel):
    Cells: List[CellOutputTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrossAccountAuthorizationsResponseTypeDef(BaseModel):
    CrossAccountAuthorizations: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourcesResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCellResponseTypeDef(BaseModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReadinessCheckResponseTypeDef(BaseModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecoveryGroupResponseTypeDef(BaseModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchitectureRecommendationsResponseTypeDef(BaseModel):
    LastAuditTimestamp: datetime
    NextToken: str
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCellReadinessSummaryRequestGetCellReadinessSummaryPaginateTypeDef(BaseModel):
    CellName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReadinessCheckResourceStatusRequestGetReadinessCheckResourceStatusPaginateTypeDef(BaseModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReadinessCheckStatusRequestGetReadinessCheckStatusPaginateTypeDef(BaseModel):
    ReadinessCheckName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRecoveryGroupReadinessSummaryRequestGetRecoveryGroupReadinessSummaryPaginateTypeDef(BaseModel):
    RecoveryGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCellsRequestListCellsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCrossAccountAuthorizationsRequestListCrossAccountAuthorizationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadinessChecksRequestListReadinessChecksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryGroupsRequestListRecoveryGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceSetsRequestListResourceSetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCellReadinessSummaryResponseTypeDef(BaseModel):
    NextToken: str
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryGroupReadinessSummaryResponseTypeDef(BaseModel):
    NextToken: str
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleResultTypeDef(BaseModel):
    LastCheckedTimestamp: datetime
    Messages: List[MessageTypeDef]
    Readiness: ReadinessType
    RuleId: str

class GetReadinessCheckStatusResponseTypeDef(BaseModel):
    Messages: List[MessageTypeDef]
    NextToken: str
    Readiness: ReadinessType
    Resources: List[ResourceResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReadinessChecksResponseTypeDef(BaseModel):
    NextToken: str
    ReadinessChecks: List[ReadinessCheckOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryGroupsResponseTypeDef(BaseModel):
    NextToken: str
    RecoveryGroups: List[RecoveryGroupOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesResponseTypeDef(BaseModel):
    NextToken: str
    Rules: List[ListRulesOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetResourceTypeDef(BaseModel):
    NLBResource: Optional[NLBResourceTypeDef] = None
    R53Resource: Optional[R53ResourceRecordTypeDef] = None

class GetReadinessCheckResourceStatusResponseTypeDef(BaseModel):
    NextToken: str
    Readiness: ReadinessType
    Rules: List[RuleResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DNSTargetResourceTypeDef(BaseModel):
    DomainName: Optional[str] = None
    HostedZoneArn: Optional[str] = None
    RecordSetId: Optional[str] = None
    RecordType: Optional[str] = None
    TargetResource: Optional[TargetResourceTypeDef] = None

class ResourcePaginatorTypeDef(BaseModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResourceTypeDef] = None
    ReadinessScopes: Optional[List[str]] = None
    ResourceArn: Optional[str] = None

class ResourceTypeDef(BaseModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResourceTypeDef] = None
    ReadinessScopes: Optional[Sequence[str]] = None
    ResourceArn: Optional[str] = None

class ResourceSetOutputPaginatorTypeDef(BaseModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourcePaginatorTypeDef]
    Tags: Optional[Dict[str, str]] = None

class CreateResourceSetRequestRequestTypeDef(BaseModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: Sequence[ResourceTypeDef]
    Tags: Optional[Mapping[str, str]] = None

class CreateResourceSetResponseTypeDef(BaseModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSetResponseTypeDef(BaseModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceSetOutputTypeDef(BaseModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Optional[Dict[str, str]] = None

class UpdateResourceSetRequestRequestTypeDef(BaseModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: Sequence[ResourceTypeDef]

class UpdateResourceSetResponseTypeDef(BaseModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceSetsResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    ResourceSets: List[ResourceSetOutputPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceSetsResponseTypeDef(BaseModel):
    NextToken: str
    ResourceSets: List[ResourceSetOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

