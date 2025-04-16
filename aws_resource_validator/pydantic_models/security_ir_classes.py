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
from aws_resource_validator.pydantic_models.security_ir_constants import *

class BatchGetMemberAccountDetailsRequest(BaseValidatorModel):
    membershipId: str
    accountIds: Sequence[str]


class GetMembershipAccountDetailError(BaseValidatorModel):
    accountId: str
    error: str
    message: str


class GetMembershipAccountDetailItem(BaseValidatorModel):
    accountId: Optional[str] = None
    relationshipStatus: Optional[MembershipAccountRelationshipStatusType] = None
    relationshipType: Optional[Literal["Organization"]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class CloseCaseRequest(BaseValidatorModel):
    caseId: str


class CreateCaseCommentRequest(BaseValidatorModel):
    caseId: str
    body: str
    clientToken: Optional[str] = None


class ImpactedAwsRegion(BaseValidatorModel):
    region: AwsRegionType


class ThreatActorIp(BaseValidatorModel):
    ipAddress: str
    userAgent: Optional[str] = None


class Watcher(BaseValidatorModel):
    email: str
    name: Optional[str] = None
    jobTitle: Optional[str] = None


class IncidentResponder(BaseValidatorModel):
    name: str
    jobTitle: str
    email: str


class OptInFeature(BaseValidatorModel):
    featureName: Literal["Triage"]
    isEnabled: bool


class GetCaseAttachmentDownloadUrlRequest(BaseValidatorModel):
    caseId: str
    attachmentId: str


class GetCaseAttachmentUploadUrlRequest(BaseValidatorModel):
    caseId: str
    fileName: str
    contentLength: int
    clientToken: Optional[str] = None


class GetCaseRequest(BaseValidatorModel):
    caseId: str


class GetMembershipRequest(BaseValidatorModel):
    membershipId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


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


class ListMembershipsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateCaseCommentRequest(BaseValidatorModel):
    caseId: str
    commentId: str
    body: str


class UpdateCaseStatusRequest(BaseValidatorModel):
    caseId: str
    caseStatus: SelfManagedCaseStatusType


class UpdateResolverTypeRequest(BaseValidatorModel):
    caseId: str
    resolverType: ResolverTypeType


class BatchGetMemberAccountDetailsResponse(BaseValidatorModel):
    items: List[GetMembershipAccountDetailItem]
    errors: List[GetMembershipAccountDetailError]
    ResponseMetadata: ResponseMetadata


class CancelMembershipResponse(BaseValidatorModel):
    membershipId: str
    ResponseMetadata: ResponseMetadata


class CloseCaseResponse(BaseValidatorModel):
    caseStatus: CaseStatusType
    closedDate: datetime
    ResponseMetadata: ResponseMetadata


class CreateCaseCommentResponse(BaseValidatorModel):
    commentId: str
    ResponseMetadata: ResponseMetadata


class CreateCaseResponse(BaseValidatorModel):
    caseId: str
    ResponseMetadata: ResponseMetadata


class CreateMembershipResponse(BaseValidatorModel):
    membershipId: str
    ResponseMetadata: ResponseMetadata


class GetCaseAttachmentDownloadUrlResponse(BaseValidatorModel):
    attachmentPresignedUrl: str
    ResponseMetadata: ResponseMetadata


class GetCaseAttachmentUploadUrlResponse(BaseValidatorModel):
    attachmentPresignedUrl: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateCaseCommentResponse(BaseValidatorModel):
    commentId: str
    body: str
    ResponseMetadata: ResponseMetadata


class UpdateCaseStatusResponse(BaseValidatorModel):
    caseStatus: SelfManagedCaseStatusType
    ResponseMetadata: ResponseMetadata


class UpdateResolverTypeResponse(BaseValidatorModel):
    caseId: str
    caseStatus: CaseStatusType
    resolverType: ResolverTypeType
    ResponseMetadata: ResponseMetadata


class ListCaseEditsResponse(BaseValidatorModel):
    items: List[CaseEditItem]
    total: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class CreateCaseRequest(BaseValidatorModel):
    resolverType: ResolverTypeType
    title: str
    description: str
    engagementType: EngagementTypeType
    reportedIncidentStartDate: Timestamp
    impactedAccounts: Sequence[str]
    watchers: Sequence[Watcher]
    clientToken: Optional[str] = None
    threatActorIpAddresses: Optional[Sequence[ThreatActorIp]] = None
    impactedServices: Optional[Sequence[str]] = None
    impactedAwsRegions: Optional[Sequence[ImpactedAwsRegion]] = None
    tags: Optional[Mapping[str, str]] = None


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
    watchersToAdd: Optional[Sequence[Watcher]] = None
    watchersToDelete: Optional[Sequence[Watcher]] = None
    threatActorIpAddressesToAdd: Optional[Sequence[ThreatActorIp]] = None
    threatActorIpAddressesToDelete: Optional[Sequence[ThreatActorIp]] = None
    impactedServicesToAdd: Optional[Sequence[str]] = None
    impactedServicesToDelete: Optional[Sequence[str]] = None
    impactedAwsRegionsToAdd: Optional[Sequence[ImpactedAwsRegion]] = None
    impactedAwsRegionsToDelete: Optional[Sequence[ImpactedAwsRegion]] = None
    impactedAccountsToAdd: Optional[Sequence[str]] = None
    impactedAccountsToDelete: Optional[Sequence[str]] = None


class CreateMembershipRequest(BaseValidatorModel):
    membershipName: str
    incidentResponseTeam: Sequence[IncidentResponder]
    clientToken: Optional[str] = None
    optInFeatures: Optional[Sequence[OptInFeature]] = None
    tags: Optional[Mapping[str, str]] = None


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
    incidentResponseTeam: Optional[Sequence[IncidentResponder]] = None
    optInFeatures: Optional[Sequence[OptInFeature]] = None


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


class ListCasesResponse(BaseValidatorModel):
    items: List[ListCasesItem]
    total: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCommentsResponse(BaseValidatorModel):
    items: List[ListCommentsItem]
    total: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMembershipsResponse(BaseValidatorModel):
    items: List[ListMembershipItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


