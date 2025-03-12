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

class BatchGetMemberAccountDetailsRequestTypeDef(BaseValidatorModel):
    membershipId: str
    accountIds: Sequence[str]


class GetMembershipAccountDetailErrorTypeDef(BaseValidatorModel):
    accountId: str
    error: str
    message: str


class GetMembershipAccountDetailItemTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    relationshipStatus: Optional[MembershipAccountRelationshipStatusType] = None
    relationshipType: Optional[Literal["Organization"]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelMembershipRequestTypeDef(BaseValidatorModel):
    membershipId: str


class CaseAttachmentAttributesTypeDef(BaseValidatorModel):
    attachmentId: str
    fileName: str
    attachmentStatus: CaseAttachmentStatusType
    creator: str
    createdDate: datetime


class CaseEditItemTypeDef(BaseValidatorModel):
    eventTimestamp: Optional[datetime] = None
    principal: Optional[str] = None
    action: Optional[str] = None
    message: Optional[str] = None


class CloseCaseRequestTypeDef(BaseValidatorModel):
    caseId: str


class CreateCaseCommentRequestTypeDef(BaseValidatorModel):
    caseId: str
    body: str
    clientToken: Optional[str] = None


class ImpactedAwsRegionTypeDef(BaseValidatorModel):
    region: AwsRegionType


class ThreatActorIpTypeDef(BaseValidatorModel):
    ipAddress: str
    userAgent: Optional[str] = None


class WatcherTypeDef(BaseValidatorModel):
    email: str
    name: Optional[str] = None
    jobTitle: Optional[str] = None


class IncidentResponderTypeDef(BaseValidatorModel):
    name: str
    jobTitle: str
    email: str


class OptInFeatureTypeDef(BaseValidatorModel):
    featureName: Literal["Triage"]
    isEnabled: bool


class GetCaseAttachmentDownloadUrlRequestTypeDef(BaseValidatorModel):
    caseId: str
    attachmentId: str


class GetCaseAttachmentUploadUrlRequestTypeDef(BaseValidatorModel):
    caseId: str
    fileName: str
    contentLength: int
    clientToken: Optional[str] = None


class GetCaseRequestTypeDef(BaseValidatorModel):
    caseId: str


class GetMembershipRequestTypeDef(BaseValidatorModel):
    membershipId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCaseEditsRequestTypeDef(BaseValidatorModel):
    caseId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCasesItemTypeDef(BaseValidatorModel):
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


class ListCasesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCommentsItemTypeDef(BaseValidatorModel):
    commentId: str
    createdDate: Optional[datetime] = None
    lastUpdatedDate: Optional[datetime] = None
    creator: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    body: Optional[str] = None


class ListCommentsRequestTypeDef(BaseValidatorModel):
    caseId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMembershipItemTypeDef(BaseValidatorModel):
    membershipId: str
    accountId: Optional[str] = None
    region: Optional[AwsRegionType] = None
    membershipArn: Optional[str] = None
    membershipStatus: Optional[MembershipStatusType] = None


class ListMembershipsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateCaseCommentRequestTypeDef(BaseValidatorModel):
    caseId: str
    commentId: str
    body: str


class UpdateCaseStatusRequestTypeDef(BaseValidatorModel):
    caseId: str
    caseStatus: SelfManagedCaseStatusType


class UpdateResolverTypeRequestTypeDef(BaseValidatorModel):
    caseId: str
    resolverType: ResolverTypeType


class BatchGetMemberAccountDetailsResponseTypeDef(BaseValidatorModel):
    items: List[GetMembershipAccountDetailItemTypeDef]
    errors: List[GetMembershipAccountDetailErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CancelMembershipResponseTypeDef(BaseValidatorModel):
    membershipId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CloseCaseResponseTypeDef(BaseValidatorModel):
    caseStatus: CaseStatusType
    closedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCaseCommentResponseTypeDef(BaseValidatorModel):
    commentId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCaseResponseTypeDef(BaseValidatorModel):
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMembershipResponseTypeDef(BaseValidatorModel):
    membershipId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCaseAttachmentDownloadUrlResponseTypeDef(BaseValidatorModel):
    attachmentPresignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCaseAttachmentUploadUrlResponseTypeDef(BaseValidatorModel):
    attachmentPresignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCaseCommentResponseTypeDef(BaseValidatorModel):
    commentId: str
    body: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCaseStatusResponseTypeDef(BaseValidatorModel):
    caseStatus: SelfManagedCaseStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateResolverTypeResponseTypeDef(BaseValidatorModel):
    caseId: str
    caseStatus: CaseStatusType
    resolverType: ResolverTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class ListCaseEditsResponseTypeDef(BaseValidatorModel):
    items: List[CaseEditItemTypeDef]
    total: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateCaseRequestTypeDef(BaseValidatorModel):
    resolverType: ResolverTypeType
    title: str
    description: str
    engagementType: EngagementTypeType
    reportedIncidentStartDate: TimestampTypeDef
    impactedAccounts: Sequence[str]
    watchers: Sequence[WatcherTypeDef]
    clientToken: Optional[str] = None
    threatActorIpAddresses: Optional[Sequence[ThreatActorIpTypeDef]] = None
    impactedServices: Optional[Sequence[str]] = None
    impactedAwsRegions: Optional[Sequence[ImpactedAwsRegionTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class GetCaseResponseTypeDef(BaseValidatorModel):
    title: str
    caseArn: str
    description: str
    caseStatus: CaseStatusType
    engagementType: EngagementTypeType
    reportedIncidentStartDate: datetime
    actualIncidentStartDate: datetime
    impactedAwsRegions: List[ImpactedAwsRegionTypeDef]
    threatActorIpAddresses: List[ThreatActorIpTypeDef]
    pendingAction: PendingActionType
    impactedAccounts: List[str]
    watchers: List[WatcherTypeDef]
    createdDate: datetime
    lastUpdatedDate: datetime
    closureCode: ClosureCodeType
    resolverType: ResolverTypeType
    impactedServices: List[str]
    caseAttachments: List[CaseAttachmentAttributesTypeDef]
    closedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCaseRequestTypeDef(BaseValidatorModel):
    caseId: str
    title: Optional[str] = None
    description: Optional[str] = None
    reportedIncidentStartDate: Optional[TimestampTypeDef] = None
    actualIncidentStartDate: Optional[TimestampTypeDef] = None
    engagementType: Optional[EngagementTypeType] = None
    watchersToAdd: Optional[Sequence[WatcherTypeDef]] = None
    watchersToDelete: Optional[Sequence[WatcherTypeDef]] = None
    threatActorIpAddressesToAdd: Optional[Sequence[ThreatActorIpTypeDef]] = None
    threatActorIpAddressesToDelete: Optional[Sequence[ThreatActorIpTypeDef]] = None
    impactedServicesToAdd: Optional[Sequence[str]] = None
    impactedServicesToDelete: Optional[Sequence[str]] = None
    impactedAwsRegionsToAdd: Optional[Sequence[ImpactedAwsRegionTypeDef]] = None
    impactedAwsRegionsToDelete: Optional[Sequence[ImpactedAwsRegionTypeDef]] = None
    impactedAccountsToAdd: Optional[Sequence[str]] = None
    impactedAccountsToDelete: Optional[Sequence[str]] = None


class CreateMembershipRequestTypeDef(BaseValidatorModel):
    membershipName: str
    incidentResponseTeam: Sequence[IncidentResponderTypeDef]
    clientToken: Optional[str] = None
    optInFeatures: Optional[Sequence[OptInFeatureTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class GetMembershipResponseTypeDef(BaseValidatorModel):
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
    incidentResponseTeam: List[IncidentResponderTypeDef]
    optInFeatures: List[OptInFeatureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMembershipRequestTypeDef(BaseValidatorModel):
    membershipId: str
    membershipName: Optional[str] = None
    incidentResponseTeam: Optional[Sequence[IncidentResponderTypeDef]] = None
    optInFeatures: Optional[Sequence[OptInFeatureTypeDef]] = None


class ListCaseEditsRequestPaginateTypeDef(BaseValidatorModel):
    caseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCasesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCommentsRequestPaginateTypeDef(BaseValidatorModel):
    caseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembershipsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCasesResponseTypeDef(BaseValidatorModel):
    items: List[ListCasesItemTypeDef]
    total: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCommentsResponseTypeDef(BaseValidatorModel):
    items: List[ListCommentsItemTypeDef]
    total: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMembershipsResponseTypeDef(BaseValidatorModel):
    items: List[ListMembershipItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


