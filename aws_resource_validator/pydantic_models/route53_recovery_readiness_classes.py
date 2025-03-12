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
from aws_resource_validator.pydantic_models.route53_recovery_readiness_constants import *

class CellOutputTypeDef(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Optional[Dict[str, str]] = None


class CreateCellRequestTypeDef(BaseValidatorModel):
    CellName: str
    Cells: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateCrossAccountAuthorizationRequestTypeDef(BaseValidatorModel):
    CrossAccountAuthorization: str


class CreateReadinessCheckRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str
    Tags: Optional[Mapping[str, str]] = None


class CreateRecoveryGroupRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    Cells: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class DeleteCellRequestTypeDef(BaseValidatorModel):
    CellName: str


class DeleteCrossAccountAuthorizationRequestTypeDef(BaseValidatorModel):
    CrossAccountAuthorization: str


class DeleteReadinessCheckRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str


class DeleteRecoveryGroupRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str


class DeleteResourceSetRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str


class GetArchitectureRecommendationsRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RecommendationTypeDef(BaseValidatorModel):
    RecommendationText: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetCellReadinessSummaryRequestTypeDef(BaseValidatorModel):
    CellName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReadinessCheckSummaryTypeDef(BaseValidatorModel):
    Readiness: Optional[ReadinessType] = None
    ReadinessCheckName: Optional[str] = None


class GetCellRequestTypeDef(BaseValidatorModel):
    CellName: str


class GetReadinessCheckRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str


class GetReadinessCheckResourceStatusRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetReadinessCheckStatusRequestTypeDef(BaseValidatorModel):
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


class GetRecoveryGroupReadinessSummaryRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetRecoveryGroupRequestTypeDef(BaseValidatorModel):
    RecoveryGroupName: str


class GetResourceSetRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str


class ListCellsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrossAccountAuthorizationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListReadinessChecksRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReadinessCheckOutputTypeDef(BaseValidatorModel):
    ReadinessCheckArn: str
    ResourceSet: str
    ReadinessCheckName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListRecoveryGroupsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RecoveryGroupOutputTypeDef(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Optional[Dict[str, str]] = None


class ListResourceSetsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRulesOutputTypeDef(BaseValidatorModel):
    ResourceType: str
    RuleDescription: str
    RuleId: str


class ListRulesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None


class ListTagsForResourcesRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class NLBResourceTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None


class R53ResourceRecordTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    RecordSetId: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateCellRequestTypeDef(BaseValidatorModel):
    CellName: str
    Cells: Sequence[str]


class UpdateReadinessCheckRequestTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str


class UpdateRecoveryGroupRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCrossAccountAuthorizationsResponseTypeDef(BaseValidatorModel):
    CrossAccountAuthorizations: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetCellReadinessSummaryRequestPaginateTypeDef(BaseValidatorModel):
    CellName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetReadinessCheckResourceStatusRequestPaginateTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetReadinessCheckStatusRequestPaginateTypeDef(BaseValidatorModel):
    ReadinessCheckName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRecoveryGroupReadinessSummaryRequestPaginateTypeDef(BaseValidatorModel):
    RecoveryGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCellsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCrossAccountAuthorizationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListReadinessChecksRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecoveryGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceSetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesRequestPaginateTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCellReadinessSummaryResponseTypeDef(BaseValidatorModel):
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetRecoveryGroupReadinessSummaryResponseTypeDef(BaseValidatorModel):
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RuleResultTypeDef(BaseValidatorModel):
    LastCheckedTimestamp: datetime
    Messages: List[MessageTypeDef]
    Readiness: ReadinessType
    RuleId: str


class GetReadinessCheckStatusResponseTypeDef(BaseValidatorModel):
    Messages: List[MessageTypeDef]
    Readiness: ReadinessType
    Resources: List[ResourceResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListReadinessChecksResponseTypeDef(BaseValidatorModel):
    ReadinessChecks: List[ReadinessCheckOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRecoveryGroupsResponseTypeDef(BaseValidatorModel):
    RecoveryGroups: List[RecoveryGroupOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[ListRulesOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TargetResourceTypeDef(BaseValidatorModel):
    NLBResource: Optional[NLBResourceTypeDef] = None
    R53Resource: Optional[R53ResourceRecordTypeDef] = None


class GetReadinessCheckResourceStatusResponseTypeDef(BaseValidatorModel):
    Readiness: ReadinessType
    Rules: List[RuleResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DNSTargetResourceTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    HostedZoneArn: Optional[str] = None
    RecordSetId: Optional[str] = None
    RecordType: Optional[str] = None
    TargetResource: Optional[TargetResourceTypeDef] = None


class ResourceOutputTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResourceTypeDef] = None
    ReadinessScopes: Optional[List[str]] = None
    ResourceArn: Optional[str] = None


class ResourceTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResourceTypeDef] = None
    ReadinessScopes: Optional[Sequence[str]] = None
    ResourceArn: Optional[str] = None


class CreateResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutputTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutputTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceSetOutputTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutputTypeDef]
    Tags: Optional[Dict[str, str]] = None


class UpdateResourceSetResponseTypeDef(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutputTypeDef]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourceSetsResponseTypeDef(BaseValidatorModel):
    ResourceSets: List[ResourceSetOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateResourceSetRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: Sequence[ResourceUnionTypeDef]
    Tags: Optional[Mapping[str, str]] = None


class UpdateResourceSetRequestTypeDef(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: Sequence[ResourceUnionTypeDef]


