from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.security_ir.security_ir_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'batch_get_member_account_details' function.
class BatchGetMemberAccountDetailsRequest(BaseValidatorModel):
    membershipId: str
    accountIds: List[str]


class GetMembershipAccountDetailError(BaseValidatorModel):
    accountId: str
    error: str
    message: str


class GetMembershipAccountDetailItem(BaseValidatorModel):
    accountId: Optional[str] = None
    relationshipStatus: Optional[MembershipAccountRelationshipStatusType] = None
    relationshipType: Optional[Literal['Organization']] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'cancel_membership' function.
class CancelMembershipRequest(BaseValidatorModel):
    membershipId: str


class CaseAttachmentAttributes(BaseValidatorModel):
    attachmentId: str
    fileName: str
    attachmentStatus: CaseAttachmentStatusType
    creator: str
    createdDate: datetime


class CaseEditItem(BaseValidatorModel):
    eventTimestamp: Optional[datetime] = None
    principal: Optional[str] = None
    action: Optional[str] = None
    message: Optional[str] = None


# This class is the input for the 'close_case' function.
class CloseCaseRequest(BaseValidatorModel):
    caseId: str


# This class is the input for the 'create_case_comment' function.
class CreateCaseCommentRequest(BaseValidatorModel):
    caseId: str
    body: str
    clientToken: Optional[str] = None


class ImpactedAwsRegion(BaseValidatorModel):
    region: AwsRegionType


class ThreatActorIp(BaseValidatorModel):
    ipAddress: str
    userAgent: Optional[str] = None

Timestamp = Union[datetime, str]


class Watcher(BaseValidatorModel):
    email: str
    name: Optional[str] = None
    jobTitle: Optional[str] = None


class IncidentResponder(BaseValidatorModel):
    name: str
    jobTitle: str
    email: str


class OptInFeature(BaseValidatorModel):
    featureName: Literal['Triage']
    isEnabled: bool


# This class is the input for the 'get_case_attachment_download_url' function.
class GetCaseAttachmentDownloadUrlRequest(BaseValidatorModel):
    caseId: str
    attachmentId: str


# This class is the input for the 'get_case_attachment_upload_url' function.
class GetCaseAttachmentUploadUrlRequest(BaseValidatorModel):
    caseId: str
    fileName: str
    contentLength: int
    clientToken: Optional[str] = None


# This class is the input for the 'get_case' function.
class GetCaseRequest(BaseValidatorModel):
    caseId: str


# This class is the input for the 'get_membership' function.
class GetMembershipRequest(BaseValidatorModel):
    membershipId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_case_edits' function.
class ListCaseEditsRequest(BaseValidatorModel):
    caseId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCasesItem(BaseValidatorModel):
    caseId: str
    lastUpdatedDate: Optional[datetime] = None
    title: Optional[str] = None
    caseArn: Optional[str] = None
    engagementType: Optional[EngagementTypeType] = None
    caseStatus: Optional[CaseStatusType] = None
    createdDate: Optional[datetime] = None
    closedDate: Optional[datetime] = None
    resolverType: Optional[ResolverTypeType] = None
    pendingAction: Optional[PendingActionType] = None


# This class is the input for the 'list_cases' function.
class ListCasesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCommentsItem(BaseValidatorModel):
    commentId: str
    createdDate: Optional[datetime] = None
    lastUpdatedDate: Optional[datetime] = None
    creator: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    body: Optional[str] = None


# This class is the input for the 'list_comments' function.
class ListCommentsRequest(BaseValidatorModel):
    caseId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMembershipItem(BaseValidatorModel):
    membershipId: str
    accountId: Optional[str] = None
    region: Optional[AwsRegionType] = None
    membershipArn: Optional[str] = None
    membershipStatus: Optional[MembershipStatusType] = None


# This class is the input for the 'list_memberships' function.
class ListMembershipsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_case_comment' function.
class UpdateCaseCommentRequest(BaseValidatorModel):
    caseId: str
    commentId: str
    body: str


# This class is the input for the 'update_case_status' function.
class UpdateCaseStatusRequest(BaseValidatorModel):
    caseId: str
    caseStatus: SelfManagedCaseStatusType


# This class is the input for the 'update_resolver_type' function.
class UpdateResolverTypeRequest(BaseValidatorModel):
    caseId: str
    resolverType: ResolverTypeType


# This class is the output for the 'batch_get_member_account_details' function.
class BatchGetMemberAccountDetailsResponse(BaseValidatorModel):
    items: List[GetMembershipAccountDetailItem]
    errors: List[GetMembershipAccountDetailError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_membership' function.
class CancelMembershipResponse(BaseValidatorModel):
    membershipId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'close_case' function.
class CloseCaseResponse(BaseValidatorModel):
    caseStatus: CaseStatusType
    closedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_case_comment' function.
class CreateCaseCommentResponse(BaseValidatorModel):
    commentId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_case' function.
class CreateCaseResponse(BaseValidatorModel):
    caseId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_membership' function.
class CreateMembershipResponse(BaseValidatorModel):
    membershipId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_case_attachment_download_url' function.
class GetCaseAttachmentDownloadUrlResponse(BaseValidatorModel):
    attachmentPresignedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_case_attachment_upload_url' function.
class GetCaseAttachmentUploadUrlResponse(BaseValidatorModel):
    attachmentPresignedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_case_comment' function.
class UpdateCaseCommentResponse(BaseValidatorModel):
    commentId: str
    body: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_case_status' function.
class UpdateCaseStatusResponse(BaseValidatorModel):
    caseStatus: SelfManagedCaseStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_resolver_type' function.
class UpdateResolverTypeResponse(BaseValidatorModel):
    caseId: str
    caseStatus: CaseStatusType
    resolverType: ResolverTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_case_edits' function.
class ListCaseEditsResponse(BaseValidatorModel):
    items: List[CaseEditItem]
    total: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_case' function.
class CreateCaseRequest(BaseValidatorModel):
    resolverType: ResolverTypeType
    title: str
    description: str
    engagementType: EngagementTypeType
    reportedIncidentStartDate: Timestamp
    impactedAccounts: List[str]
    watchers: List[Watcher]
    clientToken: Optional[str] = None
    threatActorIpAddresses: Optional[List[ThreatActorIp]] = None
    impactedServices: Optional[List[str]] = None
    impactedAwsRegions: Optional[List[ImpactedAwsRegion]] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_case' function.
class GetCaseResponse(BaseValidatorModel):
    title: str
    caseArn: str
    description: str
    caseStatus: CaseStatusType
    engagementType: EngagementTypeType
    reportedIncidentStartDate: datetime
    actualIncidentStartDate: datetime
    impactedAwsRegions: List[ImpactedAwsRegion]
    threatActorIpAddresses: List[ThreatActorIp]
    pendingAction: PendingActionType
    impactedAccounts: List[str]
    watchers: List[Watcher]
    createdDate: datetime
    lastUpdatedDate: datetime
    closureCode: ClosureCodeType
    resolverType: ResolverTypeType
    impactedServices: List[str]
    caseAttachments: List[CaseAttachmentAttributes]
    closedDate: datetime
    ResponseMetadata: ResponseMetadata


class UpdateCaseRequest(BaseValidatorModel):
    caseId: str
    title: Optional[str] = None
    description: Optional[str] = None
    reportedIncidentStartDate: Optional[Timestamp] = None
    actualIncidentStartDate: Optional[Timestamp] = None
    engagementType: Optional[EngagementTypeType] = None
    watchersToAdd: Optional[List[Watcher]] = None
    watchersToDelete: Optional[List[Watcher]] = None
    threatActorIpAddressesToAdd: Optional[List[ThreatActorIp]] = None
    threatActorIpAddressesToDelete: Optional[List[ThreatActorIp]] = None
    impactedServicesToAdd: Optional[List[str]] = None
    impactedServicesToDelete: Optional[List[str]] = None
    impactedAwsRegionsToAdd: Optional[List[ImpactedAwsRegion]] = None
    impactedAwsRegionsToDelete: Optional[List[ImpactedAwsRegion]] = None
    impactedAccountsToAdd: Optional[List[str]] = None
    impactedAccountsToDelete: Optional[List[str]] = None


# This class is the input for the 'create_membership' function.
class CreateMembershipRequest(BaseValidatorModel):
    membershipName: str
    incidentResponseTeam: List[IncidentResponder]
    clientToken: Optional[str] = None
    optInFeatures: Optional[List[OptInFeature]] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_membership' function.
class GetMembershipResponse(BaseValidatorModel):
    membershipId: str
    accountId: str
    region: AwsRegionType
    membershipName: str
    membershipArn: str
    membershipStatus: MembershipStatusType
    membershipActivationTimestamp: datetime
    membershipDeactivationTimestamp: datetime
    customerType: CustomerTypeType
    numberOfAccountsCovered: int
    incidentResponseTeam: List[IncidentResponder]
    optInFeatures: List[OptInFeature]
    ResponseMetadata: ResponseMetadata


class UpdateMembershipRequest(BaseValidatorModel):
    membershipId: str
    membershipName: Optional[str] = None
    incidentResponseTeam: Optional[List[IncidentResponder]] = None
    optInFeatures: Optional[List[OptInFeature]] = None


class ListCaseEditsRequestPaginate(BaseValidatorModel):
    caseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCasesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCommentsRequestPaginate(BaseValidatorModel):
    caseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembershipsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_cases' function.
class ListCasesResponse(BaseValidatorModel):
    items: List[ListCasesItem]
    total: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_comments' function.
class ListCommentsResponse(BaseValidatorModel):
    items: List[ListCommentsItem]
    total: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_memberships' function.
class ListMembershipsResponse(BaseValidatorModel):
    items: List[ListMembershipItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None