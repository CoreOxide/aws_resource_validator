from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CellOutput(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Optional[Dict[str, str]] = None


class CreateCellRequest(BaseValidatorModel):
    CellName: str
    Cells: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateCrossAccountAuthorizationRequest(BaseValidatorModel):
    CrossAccountAuthorization: str


class CreateReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str
    Tags: Optional[Dict[str, str]] = None


class CreateRecoveryGroupRequest(BaseValidatorModel):
    RecoveryGroupName: str
    Cells: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


class DeleteCellRequest(BaseValidatorModel):
    CellName: str


class DeleteCrossAccountAuthorizationRequest(BaseValidatorModel):
    CrossAccountAuthorization: str


class DeleteReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str


class DeleteRecoveryGroupRequest(BaseValidatorModel):
    RecoveryGroupName: str


class DeleteResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str


class GetArchitectureRecommendationsRequest(BaseValidatorModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Recommendation(BaseValidatorModel):
    RecommendationText: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetCellReadinessSummaryRequest(BaseValidatorModel):
    CellName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReadinessCheckSummary(BaseValidatorModel):
    Readiness: Optional[ReadinessType] = None
    ReadinessCheckName: Optional[str] = None


class GetCellRequest(BaseValidatorModel):
    CellName: str


class GetReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str


class GetReadinessCheckResourceStatusRequest(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetReadinessCheckStatusRequest(BaseValidatorModel):
    ReadinessCheckName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Message(BaseValidatorModel):
    MessageText: Optional[str] = None


class ResourceResult(BaseValidatorModel):
    LastCheckedTimestamp: datetime
    Readiness: ReadinessType
    ComponentId: Optional[str] = None
    ResourceArn: Optional[str] = None


class GetRecoveryGroupReadinessSummaryRequest(BaseValidatorModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetRecoveryGroupRequest(BaseValidatorModel):
    RecoveryGroupName: str


class GetResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str


class ListCellsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrossAccountAuthorizationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListReadinessChecksRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReadinessCheckOutput(BaseValidatorModel):
    ReadinessCheckArn: str
    ResourceSet: str
    ReadinessCheckName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListRecoveryGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RecoveryGroupOutput(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Optional[Dict[str, str]] = None


class ListResourceSetsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRulesOutput(BaseValidatorModel):
    ResourceType: str
    RuleDescription: str
    RuleId: str


class ListRulesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None


class ListTagsForResourcesRequest(BaseValidatorModel):
    ResourceArn: str


class NLBResource(BaseValidatorModel):
    Arn: Optional[str] = None


class R53ResourceRecord(BaseValidatorModel):
    DomainName: Optional[str] = None
    RecordSetId: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateCellRequest(BaseValidatorModel):
    CellName: str
    Cells: List[str]


class UpdateReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str


class UpdateRecoveryGroupRequest(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupName: str


class CreateCellResponse(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateCrossAccountAuthorizationResponse(BaseValidatorModel):
    CrossAccountAuthorization: str
    ResponseMetadata: ResponseMetadata


class CreateReadinessCheckResponse(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateRecoveryGroupResponse(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCellResponse(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetReadinessCheckResponse(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetRecoveryGroupResponse(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListCellsResponse(BaseValidatorModel):
    Cells: List[CellOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCrossAccountAuthorizationsResponse(BaseValidatorModel):
    CrossAccountAuthorizations: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourcesResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateCellResponse(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateReadinessCheckResponse(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateRecoveryGroupResponse(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetArchitectureRecommendationsResponse(BaseValidatorModel):
    LastAuditTimestamp: datetime
    Recommendations: List[Recommendation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCellReadinessSummaryRequestPaginate(BaseValidatorModel):
    CellName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReadinessCheckResourceStatusRequestPaginate(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReadinessCheckStatusRequestPaginate(BaseValidatorModel):
    ReadinessCheckName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRecoveryGroupReadinessSummaryRequestPaginate(BaseValidatorModel):
    RecoveryGroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCellsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCrossAccountAuthorizationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReadinessChecksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecoveryGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceSetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesRequestPaginate(BaseValidatorModel):
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCellReadinessSummaryResponse(BaseValidatorModel):
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetRecoveryGroupReadinessSummaryResponse(BaseValidatorModel):
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RuleResult(BaseValidatorModel):
    LastCheckedTimestamp: datetime
    Messages: List[Message]
    Readiness: ReadinessType
    RuleId: str


class GetReadinessCheckStatusResponse(BaseValidatorModel):
    Messages: List[Message]
    Readiness: ReadinessType
    Resources: List[ResourceResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListReadinessChecksResponse(BaseValidatorModel):
    ReadinessChecks: List[ReadinessCheckOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRecoveryGroupsResponse(BaseValidatorModel):
    RecoveryGroups: List[RecoveryGroupOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRulesResponse(BaseValidatorModel):
    Rules: List[ListRulesOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TargetResource(BaseValidatorModel):
    NLBResource: Optional[NLBResource] = None
    R53Resource: Optional[R53ResourceRecord] = None


class GetReadinessCheckResourceStatusResponse(BaseValidatorModel):
    Readiness: ReadinessType
    Rules: List[RuleResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DNSTargetResource(BaseValidatorModel):
    DomainName: Optional[str] = None
    HostedZoneArn: Optional[str] = None
    RecordSetId: Optional[str] = None
    RecordType: Optional[str] = None
    TargetResource: Optional[TargetResource] = None


class ResourceOutput(BaseValidatorModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResource] = None
    ReadinessScopes: Optional[List[str]] = None
    ResourceArn: Optional[str] = None


class Resource(BaseValidatorModel):
    ComponentId: Optional[str] = None
    DnsTargetResource: Optional[DNSTargetResource] = None
    ReadinessScopes: Optional[List[str]] = None
    ResourceArn: Optional[str] = None


class CreateResourceSetResponse(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutput]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetResourceSetResponse(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutput]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ResourceSetOutput(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutput]
    Tags: Optional[Dict[str, str]] = None


class UpdateResourceSetResponse(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutput]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

ResourceUnion = Union[Resource, ResourceOutput]


class ListResourceSetsResponse(BaseValidatorModel):
    ResourceSets: List[ResourceSetOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceUnion]
    Tags: Optional[Dict[str, str]] = None


class UpdateResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceUnion]