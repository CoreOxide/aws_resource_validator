from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mturk.mturk_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptQualificationRequestRequest(BaseValidatorModel):
    QualificationRequestId: str
    IntegerValue: Optional[int] = None


class ApproveAssignmentRequest(BaseValidatorModel):
    AssignmentId: str
    RequesterFeedback: Optional[str] = None
    OverrideRejection: Optional[bool] = None


class Assignment(BaseValidatorModel):
    AssignmentId: Optional[str] = None
    WorkerId: Optional[str] = None
    HITId: Optional[str] = None
    AssignmentStatus: Optional[AssignmentStatusType] = None
    AutoApprovalTime: Optional[datetime] = None
    AcceptTime: Optional[datetime] = None
    SubmitTime: Optional[datetime] = None
    ApprovalTime: Optional[datetime] = None
    RejectionTime: Optional[datetime] = None
    Deadline: Optional[datetime] = None
    Answer: Optional[str] = None
    RequesterFeedback: Optional[str] = None


class AssociateQualificationWithWorkerRequest(BaseValidatorModel):
    QualificationTypeId: str
    WorkerId: str
    IntegerValue: Optional[int] = None
    SendNotification: Optional[bool] = None


class BonusPayment(BaseValidatorModel):
    WorkerId: Optional[str] = None
    BonusAmount: Optional[str] = None
    AssignmentId: Optional[str] = None
    Reason: Optional[str] = None
    GrantTime: Optional[datetime] = None


class CreateAdditionalAssignmentsForHITRequest(BaseValidatorModel):
    HITId: str
    NumberOfAdditionalAssignments: int
    UniqueRequestToken: Optional[str] = None


class HITLayoutParameter(BaseValidatorModel):
    Name: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_qualification_type' function.
class CreateQualificationTypeRequest(BaseValidatorModel):
    Name: str
    Description: str
    QualificationTypeStatus: QualificationTypeStatusType
    Keywords: Optional[str] = None
    RetryDelayInSeconds: Optional[int] = None
    Test: Optional[str] = None
    AnswerKey: Optional[str] = None
    TestDurationInSeconds: Optional[int] = None
    AutoGranted: Optional[bool] = None
    AutoGrantedValue: Optional[int] = None


class QualificationType(BaseValidatorModel):
    QualificationTypeId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Keywords: Optional[str] = None
    QualificationTypeStatus: Optional[QualificationTypeStatusType] = None
    Test: Optional[str] = None
    TestDurationInSeconds: Optional[int] = None
    AnswerKey: Optional[str] = None
    RetryDelayInSeconds: Optional[int] = None
    IsRequestable: Optional[bool] = None
    AutoGranted: Optional[bool] = None
    AutoGrantedValue: Optional[int] = None


class CreateWorkerBlockRequest(BaseValidatorModel):
    WorkerId: str
    Reason: str


class DeleteHITRequest(BaseValidatorModel):
    HITId: str


class DeleteQualificationTypeRequest(BaseValidatorModel):
    QualificationTypeId: str


class DeleteWorkerBlockRequest(BaseValidatorModel):
    WorkerId: str
    Reason: Optional[str] = None


class DisassociateQualificationFromWorkerRequest(BaseValidatorModel):
    WorkerId: str
    QualificationTypeId: str
    Reason: Optional[str] = None


# This class is the input for the 'get_assignment' function.
class GetAssignmentRequest(BaseValidatorModel):
    AssignmentId: str


# This class is the input for the 'get_file_upload_url' function.
class GetFileUploadURLRequest(BaseValidatorModel):
    AssignmentId: str
    QuestionIdentifier: str


# This class is the input for the 'get_hit' function.
class GetHITRequest(BaseValidatorModel):
    HITId: str


# This class is the input for the 'get_qualification_score' function.
class GetQualificationScoreRequest(BaseValidatorModel):
    QualificationTypeId: str
    WorkerId: str


# This class is the input for the 'get_qualification_type' function.
class GetQualificationTypeRequest(BaseValidatorModel):
    QualificationTypeId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_assignments_for_hit' function.
class ListAssignmentsForHITRequest(BaseValidatorModel):
    HITId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AssignmentStatuses: Optional[List[AssignmentStatusType]] = None


# This class is the input for the 'list_bonus_payments' function.
class ListBonusPaymentsRequest(BaseValidatorModel):
    HITId: Optional[str] = None
    AssignmentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_hits_for_qualification_type' function.
class ListHITsForQualificationTypeRequest(BaseValidatorModel):
    QualificationTypeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_hits' function.
class ListHITsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_qualification_requests' function.
class ListQualificationRequestsRequest(BaseValidatorModel):
    QualificationTypeId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QualificationRequest(BaseValidatorModel):
    QualificationRequestId: Optional[str] = None
    QualificationTypeId: Optional[str] = None
    WorkerId: Optional[str] = None
    Test: Optional[str] = None
    Answer: Optional[str] = None
    SubmitTime: Optional[datetime] = None


# This class is the input for the 'list_qualification_types' function.
class ListQualificationTypesRequest(BaseValidatorModel):
    MustBeRequestable: bool
    Query: Optional[str] = None
    MustBeOwnedByCaller: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_review_policy_results_for_hit' function.
class ListReviewPolicyResultsForHITRequest(BaseValidatorModel):
    HITId: str
    PolicyLevels: Optional[List[ReviewPolicyLevelType]] = None
    RetrieveActions: Optional[bool] = None
    RetrieveResults: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_reviewable_hits' function.
class ListReviewableHITsRequest(BaseValidatorModel):
    HITTypeId: Optional[str] = None
    Status: Optional[ReviewableHITStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_worker_blocks' function.
class ListWorkerBlocksRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class WorkerBlock(BaseValidatorModel):
    WorkerId: Optional[str] = None
    Reason: Optional[str] = None


# This class is the input for the 'list_workers_with_qualification_type' function.
class ListWorkersWithQualificationTypeRequest(BaseValidatorModel):
    QualificationTypeId: str
    Status: Optional[QualificationStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Locale(BaseValidatorModel):
    Country: str
    Subdivision: Optional[str] = None


class NotificationSpecification(BaseValidatorModel):
    Destination: str
    Transport: NotificationTransportType
    Version: str
    EventTypes: List[EventTypeType]


class NotifyWorkersFailureStatus(BaseValidatorModel):
    NotifyWorkersFailureCode: Optional[NotifyWorkersFailureCodeType] = None
    NotifyWorkersFailureMessage: Optional[str] = None
    WorkerId: Optional[str] = None


# This class is the input for the 'notify_workers' function.
class NotifyWorkersRequest(BaseValidatorModel):
    Subject: str
    MessageText: str
    WorkerIds: List[str]


class ParameterMapEntryOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class ParameterMapEntry(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class RejectAssignmentRequest(BaseValidatorModel):
    AssignmentId: str
    RequesterFeedback: str


class RejectQualificationRequestRequest(BaseValidatorModel):
    QualificationRequestId: str
    Reason: Optional[str] = None


class ReviewActionDetail(BaseValidatorModel):
    ActionId: Optional[str] = None
    ActionName: Optional[str] = None
    TargetId: Optional[str] = None
    TargetType: Optional[str] = None
    Status: Optional[ReviewActionStatusType] = None
    CompleteTime: Optional[datetime] = None
    Result: Optional[str] = None
    ErrorCode: Optional[str] = None


class ReviewResultDetail(BaseValidatorModel):
    ActionId: Optional[str] = None
    SubjectId: Optional[str] = None
    SubjectType: Optional[str] = None
    QuestionId: Optional[str] = None
    Key: Optional[str] = None
    Value: Optional[str] = None


class SendBonusRequest(BaseValidatorModel):
    WorkerId: str
    BonusAmount: str
    AssignmentId: str
    Reason: str
    UniqueRequestToken: Optional[str] = None

Timestamp = Union[datetime, str]


class UpdateHITReviewStatusRequest(BaseValidatorModel):
    HITId: str
    Revert: Optional[bool] = None


class UpdateHITTypeOfHITRequest(BaseValidatorModel):
    HITId: str
    HITTypeId: str


# This class is the input for the 'update_qualification_type' function.
class UpdateQualificationTypeRequest(BaseValidatorModel):
    QualificationTypeId: str
    Description: Optional[str] = None
    QualificationTypeStatus: Optional[QualificationTypeStatusType] = None
    Test: Optional[str] = None
    AnswerKey: Optional[str] = None
    TestDurationInSeconds: Optional[int] = None
    RetryDelayInSeconds: Optional[int] = None
    AutoGranted: Optional[bool] = None
    AutoGrantedValue: Optional[int] = None


# This class is the output for the 'create_hit_type' function.
class CreateHITTypeResponse(BaseValidatorModel):
    HITTypeId: str
    ResponseMetadata: ResponseMetadata


class GetAccountBalanceResponse(BaseValidatorModel):
    AvailableBalance: str
    OnHoldBalance: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_file_upload_url' function.
class GetFileUploadURLResponse(BaseValidatorModel):
    FileUploadURL: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_assignments_for_hit' function.
class ListAssignmentsForHITResponse(BaseValidatorModel):
    NumResults: int
    Assignments: List[Assignment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_bonus_payments' function.
class ListBonusPaymentsResponse(BaseValidatorModel):
    NumResults: int
    BonusPayments: List[BonusPayment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_qualification_type' function.
class CreateQualificationTypeResponse(BaseValidatorModel):
    QualificationType: QualificationType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_qualification_type' function.
class GetQualificationTypeResponse(BaseValidatorModel):
    QualificationType: QualificationType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_qualification_types' function.
class ListQualificationTypesResponse(BaseValidatorModel):
    NumResults: int
    QualificationTypes: List[QualificationType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_qualification_type' function.
class UpdateQualificationTypeResponse(BaseValidatorModel):
    QualificationType: QualificationType
    ResponseMetadata: ResponseMetadata


class ListAssignmentsForHITRequestPaginate(BaseValidatorModel):
    HITId: str
    AssignmentStatuses: Optional[List[AssignmentStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBonusPaymentsRequestPaginate(BaseValidatorModel):
    HITId: Optional[str] = None
    AssignmentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHITsForQualificationTypeRequestPaginate(BaseValidatorModel):
    QualificationTypeId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHITsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQualificationRequestsRequestPaginate(BaseValidatorModel):
    QualificationTypeId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQualificationTypesRequestPaginate(BaseValidatorModel):
    MustBeRequestable: bool
    Query: Optional[str] = None
    MustBeOwnedByCaller: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReviewableHITsRequestPaginate(BaseValidatorModel):
    HITTypeId: Optional[str] = None
    Status: Optional[ReviewableHITStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkerBlocksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkersWithQualificationTypeRequestPaginate(BaseValidatorModel):
    QualificationTypeId: str
    Status: Optional[QualificationStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_qualification_requests' function.
class ListQualificationRequestsResponse(BaseValidatorModel):
    NumResults: int
    QualificationRequests: List[QualificationRequest]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_worker_blocks' function.
class ListWorkerBlocksResponse(BaseValidatorModel):
    NumResults: int
    WorkerBlocks: List[WorkerBlock]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class QualificationRequirementOutput(BaseValidatorModel):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: Optional[List[int]] = None
    LocaleValues: Optional[List[Locale]] = None
    RequiredToPreview: Optional[bool] = None
    ActionsGuarded: Optional[HITAccessActionsType] = None


class QualificationRequirement(BaseValidatorModel):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: Optional[List[int]] = None
    LocaleValues: Optional[List[Locale]] = None
    RequiredToPreview: Optional[bool] = None
    ActionsGuarded: Optional[HITAccessActionsType] = None


class Qualification(BaseValidatorModel):
    QualificationTypeId: Optional[str] = None
    WorkerId: Optional[str] = None
    GrantTime: Optional[datetime] = None
    IntegerValue: Optional[int] = None
    LocaleValue: Optional[Locale] = None
    Status: Optional[QualificationStatusType] = None


class SendTestEventNotificationRequest(BaseValidatorModel):
    Notification: NotificationSpecification
    TestEventType: EventTypeType


class UpdateNotificationSettingsRequest(BaseValidatorModel):
    HITTypeId: str
    Notification: Optional[NotificationSpecification] = None
    Active: Optional[bool] = None


# This class is the output for the 'notify_workers' function.
class NotifyWorkersResponse(BaseValidatorModel):
    NotifyWorkersFailureStatuses: List[NotifyWorkersFailureStatus]
    ResponseMetadata: ResponseMetadata


class PolicyParameterOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MapEntries: Optional[List[ParameterMapEntryOutput]] = None


class PolicyParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MapEntries: Optional[List[ParameterMapEntry]] = None


class ReviewReport(BaseValidatorModel):
    ReviewResults: Optional[List[ReviewResultDetail]] = None
    ReviewActions: Optional[List[ReviewActionDetail]] = None


class UpdateExpirationForHITRequest(BaseValidatorModel):
    HITId: str
    ExpireAt: Timestamp


class HIT(BaseValidatorModel):
    HITId: Optional[str] = None
    HITTypeId: Optional[str] = None
    HITGroupId: Optional[str] = None
    HITLayoutId: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    Question: Optional[str] = None
    Keywords: Optional[str] = None
    HITStatus: Optional[HITStatusType] = None
    MaxAssignments: Optional[int] = None
    Reward: Optional[str] = None
    AutoApprovalDelayInSeconds: Optional[int] = None
    Expiration: Optional[datetime] = None
    AssignmentDurationInSeconds: Optional[int] = None
    RequesterAnnotation: Optional[str] = None
    QualificationRequirements: Optional[List[QualificationRequirementOutput]] = None
    HITReviewStatus: Optional[HITReviewStatusType] = None
    NumberOfAssignmentsPending: Optional[int] = None
    NumberOfAssignmentsAvailable: Optional[int] = None
    NumberOfAssignmentsCompleted: Optional[int] = None

QualificationRequirementUnion = Union[QualificationRequirement, QualificationRequirementOutput]


# This class is the output for the 'get_qualification_score' function.
class GetQualificationScoreResponse(BaseValidatorModel):
    Qualification: Qualification
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_workers_with_qualification_type' function.
class ListWorkersWithQualificationTypeResponse(BaseValidatorModel):
    NumResults: int
    Qualifications: List[Qualification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ReviewPolicyOutput(BaseValidatorModel):
    PolicyName: str
    Parameters: Optional[List[PolicyParameterOutput]] = None


class ReviewPolicy(BaseValidatorModel):
    PolicyName: str
    Parameters: Optional[List[PolicyParameter]] = None


# This class is the output for the 'create_hit' function.
class CreateHITResponse(BaseValidatorModel):
    HIT: HIT
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hit_with_hit_type' function.
class CreateHITWithHITTypeResponse(BaseValidatorModel):
    HIT: HIT
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_assignment' function.
class GetAssignmentResponse(BaseValidatorModel):
    Assignment: Assignment
    HIT: HIT
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_hit' function.
class GetHITResponse(BaseValidatorModel):
    HIT: HIT
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_hits_for_qualification_type' function.
class ListHITsForQualificationTypeResponse(BaseValidatorModel):
    NumResults: int
    HITs: List[HIT]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_hits' function.
class ListHITsResponse(BaseValidatorModel):
    NumResults: int
    HITs: List[HIT]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_reviewable_hits' function.
class ListReviewableHITsResponse(BaseValidatorModel):
    NumResults: int
    HITs: List[HIT]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_hit_type' function.
class CreateHITTypeRequest(BaseValidatorModel):
    AssignmentDurationInSeconds: int
    Reward: str
    Title: str
    Description: str
    AutoApprovalDelayInSeconds: Optional[int] = None
    Keywords: Optional[str] = None
    QualificationRequirements: Optional[List[QualificationRequirementUnion]] = None


# This class is the output for the 'list_review_policy_results_for_hit' function.
class ListReviewPolicyResultsForHITResponse(BaseValidatorModel):
    HITId: str
    AssignmentReviewPolicy: ReviewPolicyOutput
    HITReviewPolicy: ReviewPolicyOutput
    AssignmentReviewReport: ReviewReport
    HITReviewReport: ReviewReport
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ReviewPolicyUnion = Union[ReviewPolicy, ReviewPolicyOutput]


# This class is the input for the 'create_hit' function.
class CreateHITRequest(BaseValidatorModel):
    LifetimeInSeconds: int
    AssignmentDurationInSeconds: int
    Reward: str
    Title: str
    Description: str
    MaxAssignments: Optional[int] = None
    AutoApprovalDelayInSeconds: Optional[int] = None
    Keywords: Optional[str] = None
    Question: Optional[str] = None
    RequesterAnnotation: Optional[str] = None
    QualificationRequirements: Optional[List[QualificationRequirementUnion]] = None
    UniqueRequestToken: Optional[str] = None
    AssignmentReviewPolicy: Optional[ReviewPolicyUnion] = None
    HITReviewPolicy: Optional[ReviewPolicyUnion] = None
    HITLayoutId: Optional[str] = None
    HITLayoutParameters: Optional[List[HITLayoutParameter]] = None


# This class is the input for the 'create_hit_with_hit_type' function.
class CreateHITWithHITTypeRequest(BaseValidatorModel):
    HITTypeId: str
    LifetimeInSeconds: int
    MaxAssignments: Optional[int] = None
    Question: Optional[str] = None
    RequesterAnnotation: Optional[str] = None
    UniqueRequestToken: Optional[str] = None
    AssignmentReviewPolicy: Optional[ReviewPolicyUnion] = None
    HITReviewPolicy: Optional[ReviewPolicyUnion] = None
    HITLayoutId: Optional[str] = None
    HITLayoutParameters: Optional[List[HITLayoutParameter]] = None