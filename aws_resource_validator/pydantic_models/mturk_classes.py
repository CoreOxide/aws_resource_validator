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
from aws_resource_validator.pydantic_models.mturk_constants import *

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


class GetAssignmentRequest(BaseValidatorModel):
    AssignmentId: str


class GetFileUploadURLRequest(BaseValidatorModel):
    AssignmentId: str
    QuestionIdentifier: str


class GetHITRequest(BaseValidatorModel):
    HITId: str


class GetQualificationScoreRequest(BaseValidatorModel):
    QualificationTypeId: str
    WorkerId: str


class GetQualificationTypeRequest(BaseValidatorModel):
    QualificationTypeId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssignmentsForHITRequest(BaseValidatorModel):
    HITId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AssignmentStatuses: Optional[Sequence[AssignmentStatusType]] = None


class ListBonusPaymentsRequest(BaseValidatorModel):
    HITId: Optional[str] = None
    AssignmentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHITsForQualificationTypeRequest(BaseValidatorModel):
    QualificationTypeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHITsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


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


class ListQualificationTypesRequest(BaseValidatorModel):
    MustBeRequestable: bool
    Query: Optional[str] = None
    MustBeOwnedByCaller: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReviewPolicyResultsForHITRequest(BaseValidatorModel):
    HITId: str
    PolicyLevels: Optional[Sequence[ReviewPolicyLevelType]] = None
    RetrieveActions: Optional[bool] = None
    RetrieveResults: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListReviewableHITsRequest(BaseValidatorModel):
    HITTypeId: Optional[str] = None
    Status: Optional[ReviewableHITStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListWorkerBlocksRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class WorkerBlock(BaseValidatorModel):
    WorkerId: Optional[str] = None
    Reason: Optional[str] = None


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
    EventTypes: Sequence[EventTypeType]


class NotifyWorkersFailureStatus(BaseValidatorModel):
    NotifyWorkersFailureCode: Optional[NotifyWorkersFailureCodeType] = None
    NotifyWorkersFailureMessage: Optional[str] = None
    WorkerId: Optional[str] = None


class NotifyWorkersRequest(BaseValidatorModel):
    Subject: str
    MessageText: str
    WorkerIds: Sequence[str]


class ParameterMapEntryOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class ParameterMapEntry(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


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


class UpdateHITReviewStatusRequest(BaseValidatorModel):
    HITId: str
    Revert: Optional[bool] = None


class UpdateHITTypeOfHITRequest(BaseValidatorModel):
    HITId: str
    HITTypeId: str


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


class CreateHITTypeResponse(BaseValidatorModel):
    HITTypeId: str
    ResponseMetadata: ResponseMetadata


class GetAccountBalanceResponse(BaseValidatorModel):
    AvailableBalance: str
    OnHoldBalance: str
    ResponseMetadata: ResponseMetadata


class GetFileUploadURLResponse(BaseValidatorModel):
    FileUploadURL: str
    ResponseMetadata: ResponseMetadata


class ListAssignmentsForHITResponse(BaseValidatorModel):
    NumResults: int
    Assignments: List[Assignment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListBonusPaymentsResponse(BaseValidatorModel):
    NumResults: int
    BonusPayments: List[BonusPayment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateQualificationTypeResponse(BaseValidatorModel):
    QualificationType: QualificationType
    ResponseMetadata: ResponseMetadata


class GetQualificationTypeResponse(BaseValidatorModel):
    QualificationType: QualificationType
    ResponseMetadata: ResponseMetadata


class ListQualificationTypesResponse(BaseValidatorModel):
    NumResults: int
    QualificationTypes: List[QualificationType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateQualificationTypeResponse(BaseValidatorModel):
    QualificationType: QualificationType
    ResponseMetadata: ResponseMetadata


class ListAssignmentsForHITRequestPaginate(BaseValidatorModel):
    HITId: str
    AssignmentStatuses: Optional[Sequence[AssignmentStatusType]] = None
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


class ListQualificationRequestsResponse(BaseValidatorModel):
    NumResults: int
    QualificationRequests: List[QualificationRequest]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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
    IntegerValues: Optional[Sequence[int]] = None
    LocaleValues: Optional[Sequence[Locale]] = None
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


class NotifyWorkersResponse(BaseValidatorModel):
    NotifyWorkersFailureStatuses: List[NotifyWorkersFailureStatus]
    ResponseMetadata: ResponseMetadata


class PolicyParameterOutput(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None
    MapEntries: Optional[List[ParameterMapEntryOutput]] = None


class PolicyParameter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    MapEntries: Optional[Sequence[ParameterMapEntry]] = None


class ReviewReport(BaseValidatorModel):
    ReviewResults: Optional[List[ReviewResultDetail]] = None
    ReviewActions: Optional[List[ReviewActionDetail]] = None


class Timestamp(BaseValidatorModel):
    pass


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


class GetQualificationScoreResponse(BaseValidatorModel):
    Qualification: Qualification
    ResponseMetadata: ResponseMetadata


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
    Parameters: Optional[Sequence[PolicyParameter]] = None


class CreateHITResponse(BaseValidatorModel):
    HIT: HIT
    ResponseMetadata: ResponseMetadata


class CreateHITWithHITTypeResponse(BaseValidatorModel):
    HIT: HIT
    ResponseMetadata: ResponseMetadata


class GetAssignmentResponse(BaseValidatorModel):
    Assignment: Assignment
    HIT: HIT
    ResponseMetadata: ResponseMetadata


class GetHITResponse(BaseValidatorModel):
    HIT: HIT
    ResponseMetadata: ResponseMetadata


class ListHITsForQualificationTypeResponse(BaseValidatorModel):
    NumResults: int
    HITs: List[HIT]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHITsResponse(BaseValidatorModel):
    NumResults: int
    HITs: List[HIT]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListReviewableHITsResponse(BaseValidatorModel):
    NumResults: int
    HITs: List[HIT]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class QualificationRequirementUnion(BaseValidatorModel):
    pass


class CreateHITTypeRequest(BaseValidatorModel):
    AssignmentDurationInSeconds: int
    Reward: str
    Title: str
    Description: str
    AutoApprovalDelayInSeconds: Optional[int] = None
    Keywords: Optional[str] = None
    QualificationRequirements: Optional[Sequence[QualificationRequirementUnion]] = None


class ListReviewPolicyResultsForHITResponse(BaseValidatorModel):
    HITId: str
    AssignmentReviewPolicy: ReviewPolicyOutput
    HITReviewPolicy: ReviewPolicyOutput
    AssignmentReviewReport: ReviewReport
    HITReviewReport: ReviewReport
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ReviewPolicyUnion(BaseValidatorModel):
    pass


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
    QualificationRequirements: Optional[Sequence[QualificationRequirementUnion]] = None
    UniqueRequestToken: Optional[str] = None
    AssignmentReviewPolicy: Optional[ReviewPolicyUnion] = None
    HITReviewPolicy: Optional[ReviewPolicyUnion] = None
    HITLayoutId: Optional[str] = None
    HITLayoutParameters: Optional[Sequence[HITLayoutParameter]] = None


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
    HITLayoutParameters: Optional[Sequence[HITLayoutParameter]] = None


