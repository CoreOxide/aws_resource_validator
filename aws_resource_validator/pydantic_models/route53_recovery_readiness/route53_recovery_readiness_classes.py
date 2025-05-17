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


# This class is the input for the 'create_cell' function.
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


# This class is the input for the 'create_cross_account_authorization' function.
class CreateCrossAccountAuthorizationRequest(BaseValidatorModel):
    CrossAccountAuthorization: str


# This class is the input for the 'create_readiness_check' function.
class CreateReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_recovery_group' function.
class CreateRecoveryGroupRequest(BaseValidatorModel):
    RecoveryGroupName: str
    Cells: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_cell' function.
class DeleteCellRequest(BaseValidatorModel):
    CellName: str


class DeleteCrossAccountAuthorizationRequest(BaseValidatorModel):
    CrossAccountAuthorization: str


# This class is the input for the 'delete_readiness_check' function.
class DeleteReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str


# This class is the input for the 'delete_recovery_group' function.
class DeleteRecoveryGroupRequest(BaseValidatorModel):
    RecoveryGroupName: str


# This class is the input for the 'delete_resource_set' function.
class DeleteResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str


# This class is the input for the 'get_architecture_recommendations' function.
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


# This class is the input for the 'get_cell_readiness_summary' function.
class GetCellReadinessSummaryRequest(BaseValidatorModel):
    CellName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReadinessCheckSummary(BaseValidatorModel):
    Readiness: Optional[ReadinessType] = None
    ReadinessCheckName: Optional[str] = None


# This class is the input for the 'get_cell' function.
class GetCellRequest(BaseValidatorModel):
    CellName: str


# This class is the input for the 'get_readiness_check' function.
class GetReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str


# This class is the input for the 'get_readiness_check_resource_status' function.
class GetReadinessCheckResourceStatusRequest(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceIdentifier: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_readiness_check_status' function.
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


# This class is the input for the 'get_recovery_group_readiness_summary' function.
class GetRecoveryGroupReadinessSummaryRequest(BaseValidatorModel):
    RecoveryGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_recovery_group' function.
class GetRecoveryGroupRequest(BaseValidatorModel):
    RecoveryGroupName: str


# This class is the input for the 'get_resource_set' function.
class GetResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str


# This class is the input for the 'list_cells' function.
class ListCellsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_cross_account_authorizations' function.
class ListCrossAccountAuthorizationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_readiness_checks' function.
class ListReadinessChecksRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ReadinessCheckOutput(BaseValidatorModel):
    ReadinessCheckArn: str
    ResourceSet: str
    ReadinessCheckName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_recovery_groups' function.
class ListRecoveryGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RecoveryGroupOutput(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_resource_sets' function.
class ListResourceSetsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRulesOutput(BaseValidatorModel):
    ResourceType: str
    RuleDescription: str
    RuleId: str


# This class is the input for the 'list_rules' function.
class ListRulesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceType: Optional[str] = None


# This class is the input for the 'list_tags_for_resources' function.
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


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_cell' function.
class UpdateCellRequest(BaseValidatorModel):
    CellName: str
    Cells: List[str]


# This class is the input for the 'update_readiness_check' function.
class UpdateReadinessCheckRequest(BaseValidatorModel):
    ReadinessCheckName: str
    ResourceSetName: str


# This class is the input for the 'update_recovery_group' function.
class UpdateRecoveryGroupRequest(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupName: str


# This class is the output for the 'create_cell' function.
class CreateCellResponse(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cross_account_authorization' function.
class CreateCrossAccountAuthorizationResponse(BaseValidatorModel):
    CrossAccountAuthorization: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_readiness_check' function.
class CreateReadinessCheckResponse(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_recovery_group' function.
class CreateRecoveryGroupResponse(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cell' function.
class GetCellResponse(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_readiness_check' function.
class GetReadinessCheckResponse(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_recovery_group' function.
class GetRecoveryGroupResponse(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_cells' function.
class ListCellsResponse(BaseValidatorModel):
    Cells: List[CellOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_cross_account_authorizations' function.
class ListCrossAccountAuthorizationsResponse(BaseValidatorModel):
    CrossAccountAuthorizations: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resources' function.
class ListTagsForResourcesResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cell' function.
class UpdateCellResponse(BaseValidatorModel):
    CellArn: str
    CellName: str
    Cells: List[str]
    ParentReadinessScopes: List[str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_readiness_check' function.
class UpdateReadinessCheckResponse(BaseValidatorModel):
    ReadinessCheckArn: str
    ReadinessCheckName: str
    ResourceSet: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_recovery_group' function.
class UpdateRecoveryGroupResponse(BaseValidatorModel):
    Cells: List[str]
    RecoveryGroupArn: str
    RecoveryGroupName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_architecture_recommendations' function.
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


# This class is the output for the 'get_cell_readiness_summary' function.
class GetCellReadinessSummaryResponse(BaseValidatorModel):
    Readiness: ReadinessType
    ReadinessChecks: List[ReadinessCheckSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_recovery_group_readiness_summary' function.
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


# This class is the output for the 'get_readiness_check_status' function.
class GetReadinessCheckStatusResponse(BaseValidatorModel):
    Messages: List[Message]
    Readiness: ReadinessType
    Resources: List[ResourceResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_readiness_checks' function.
class ListReadinessChecksResponse(BaseValidatorModel):
    ReadinessChecks: List[ReadinessCheckOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_recovery_groups' function.
class ListRecoveryGroupsResponse(BaseValidatorModel):
    RecoveryGroups: List[RecoveryGroupOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_rules' function.
class ListRulesResponse(BaseValidatorModel):
    Rules: List[ListRulesOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TargetResource(BaseValidatorModel):
    NLBResource: Optional[NLBResource] = None
    R53Resource: Optional[R53ResourceRecord] = None


# This class is the output for the 'get_readiness_check_resource_status' function.
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


# This class is the output for the 'create_resource_set' function.
class CreateResourceSetResponse(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutput]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_set' function.
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


# This class is the output for the 'update_resource_set' function.
class UpdateResourceSetResponse(BaseValidatorModel):
    ResourceSetArn: str
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceOutput]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

ResourceUnion = Union[Resource, ResourceOutput]


# This class is the output for the 'list_resource_sets' function.
class ListResourceSetsResponse(BaseValidatorModel):
    ResourceSets: List[ResourceSetOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_resource_set' function.
class CreateResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceUnion]
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_resource_set' function.
class UpdateResourceSetRequest(BaseValidatorModel):
    ResourceSetName: str
    ResourceSetType: str
    Resources: List[ResourceUnion]