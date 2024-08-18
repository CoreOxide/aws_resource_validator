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
from aws_resource_validator.pydantic_models.route53_recovery_readiness_constants import *

class CellOutputTypeDef(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Optional[Dict[str, str]] = None

class CreateCellRequestRequestTypeDef(BaseValidatorModel):
    CellName: str
    Cells: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateCrossAccountAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    CrossAccountAuthorization: str

class CreateReadinessCheckRequestRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str
    Tags: Optional[Mapping[str, str]] = None

class CreateRecoveryGroupRequestRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    Cells: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class DeleteCellRequestRequestTypeDef(BaseValidatorModel):
    CellName: str

class DeleteCrossAccountAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    CrossAccountAuthorization: str

class DeleteReadinessCheckRequestRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str

class DeleteRecoveryGroupRequestRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str

class DeleteResourceSetRequestRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str

class GetArchitectureRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RecommendationTypeDef(BaseValidatorModel):
    RecommendationText: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetCellReadinessSummaryRequestRequestTypeDef(BaseValidatorModel):
    CellName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ReadinessCheckSummaryTypeDef(BaseValidatorModel):
    Readiness: Optional[ReadinessType] = None
    ReadinessCheckName: Optional[str] = None

class GetCellRequestRequestTypeDef(BaseValidatorModel):
    CellName: str

class GetReadinessCheckRequestRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str

class GetReadinessCheckResourceStatusRequestRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetReadinessCheckStatusRequestRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MessageTypeDef(BaseValidatorModel):
    MessageText: Optional[str] = None

class ResourceResultTypeDef(BaseValidatorModel):
    LastCheckedTimestamp: datetime
    Readiness: ReadinessType
    ComponentId: Optional[str] = None
    ResourceArn: Optional[str] = None

class GetRecoveryGroupReadinessSummaryRequestRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetRecoveryGroupRequestRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str

class GetResourceSetRequestRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str

class ListCellsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCrossAccountAuthorizationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListReadinessChecksRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ReadinessCheckOutputTypeDef(BaseValidatorModel):
    ReadinessCheckArn: str
    ResourceSet: str
    ReadinessCheckName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListRecoveryGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RecoveryGroupOutputTypeDef(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Optional[Dict[str, str]] = None

class ListResourceSetsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRulesOutputTypeDef(BaseValidatorModel):
    ResourceType: str
    RuleDescription: str
    RuleId: str

class ListRulesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None

class ListTagsForResourcesRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class NLBResourceTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class R53ResourceRecordTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    RecordSetId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateCellRequestRequestTypeDef(BaseValidatorModel):
    CellName: str
    Cells: Sequence[str]

class UpdateReadinessCheckRequestRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str

class UpdateRecoveryGroupRequestRequestTypeDef(BaseValidatorModel):
    Cells: Sequence[str]
    RecoveryGroupName: str

class CreateCellResponseTypeDef(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCrossAccountAuthorizationResponseTypeDef(BaseValidatorModel):
    CrossAccountAuthorization: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReadinessCheckResponseTypeDef(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecoveryGroupResponseTypeDef(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCellResponseTypeDef(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetReadinessCheckResponseTypeDef(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryGroupResponseTypeDef(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCellsResponseTypeDef(BaseValidatorModel):
    Cells: List[CellOutputTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrossAccountAuthorizationsResponseTypeDef(BaseValidatorModel):
    CrossAccountAuthorizations: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourcesResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCellResponseTypeDef(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReadinessCheckResponseTypeDef(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecoveryGroupResponseTypeDef(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetArchitectureRecommendationsResponseTypeDef(BaseValidatorModel):
    LastAuditTimestamp: datetime
    NextToken: str
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCellReadinessSummaryRequestGetCellReadinessSummaryPaginateTypeDef(BaseValidatorModel):
    CellName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReadinessCheckResourceStatusRequestGetReadinessCheckResourceStatusPaginateTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReadinessCheckStatusRequestGetReadinessCheckStatusPaginateTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRecoveryGroupReadinessSummaryRequestGetRecoveryGroupReadinessSummaryPaginateTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCellsRequestListCellsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCrossAccountAuthorizationsRequestListCrossAccountAuthorizationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReadinessChecksRequestListReadinessChecksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecoveryGroupsRequestListRecoveryGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceSetsRequestListResourceSetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCellReadinessSummaryResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecoveryGroupReadinessSummaryResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleResultTypeDef(BaseValidatorModel):
    LastCheckedTimestamp: datetime
    Messages: List[MessageTypeDef]
    Readiness: ReadinessType
    RuleId: str

class GetReadinessCheckStatusResponseTypeDef(BaseValidatorModel):
    Messages: List[MessageTypeDef]
    NextToken: str
    Readiness: ReadinessType
    Resources: List[ResourceResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReadinessChecksResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ReadinessChecks: List[ReadinessCheckOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecoveryGroupsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    RecoveryGroups: List[RecoveryGroupOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Rules: List[ListRulesOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetResourceTypeDef(BaseValidatorModel):
    NLBResource: Optional[NLBResourceTypeDef] = None
    R53Resource: Optional[R53ResourceRecordTypeDef] = None

class GetReadinessCheckResourceStatusResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Readiness: ReadinessType
    Rules: List[RuleResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DNSTargetResourceTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    HostedZoneArn: Optional[str] = None
    RecordSetId: Optional[str] = None
    RecordType: Optional[str] = None
    TargetResource: Optional[TargetResourceTypeDef] = None

class ResourcePaginatorTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResourceTypeDef] = None
    ReadinessScopes: Optional[List[str]] = None
    ResourceArn: Optional[str] = None

class ResourceTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResourceTypeDef] = None
    ReadinessScopes: Optional[Sequence[str]] = None
    ResourceArn: Optional[str] = None

class ResourceSetOutputPaginatorTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourcePaginatorTypeDef]
    Tags: Optional[Dict[str, str]] = None

class CreateResourceSetRequestRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: Sequence[ResourceTypeDef]
    Tags: Optional[Mapping[str, str]] = None

class CreateResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceSetOutputTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Optional[Dict[str, str]] = None

class UpdateResourceSetRequestRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: Sequence[ResourceTypeDef]

class UpdateResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceSetsResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    ResourceSets: List[ResourceSetOutputPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceSetsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ResourceSets: List[ResourceSetOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

