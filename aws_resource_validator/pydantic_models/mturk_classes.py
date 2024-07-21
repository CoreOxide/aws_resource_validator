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
from aws_resource_validator.pydantic_models.mturk_constants import *

class AcceptQualificationRequestRequestRequestTypeDef(BaseModel):
    QualificationRequestId: str
    IntegerValue: Optional[int] = None

class ApproveAssignmentRequestRequestTypeDef(BaseModel):
    AssignmentId: str
    RequesterFeedback: Optional[str] = None
    OverrideRejection: Optional[bool] = None

class AssignmentTypeDef(BaseModel):
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

class AssociateQualificationWithWorkerRequestRequestTypeDef(BaseModel):
    QualificationTypeId: str
    WorkerId: str
    IntegerValue: Optional[int] = None
    SendNotification: Optional[bool] = None

class BonusPaymentTypeDef(BaseModel):
    WorkerId: Optional[str] = None
    BonusAmount: Optional[str] = None
    AssignmentId: Optional[str] = None
    Reason: Optional[str] = None
    GrantTime: Optional[datetime] = None

class CreateAdditionalAssignmentsForHITRequestRequestTypeDef(BaseModel):
    HITId: str
    NumberOfAdditionalAssignments: int
    UniqueRequestToken: Optional[str] = None

class HITLayoutParameterTypeDef(BaseModel):
    Name: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateQualificationTypeRequestRequestTypeDef(BaseModel):
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

class QualificationTypeTypeDef(BaseModel):
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

class CreateWorkerBlockRequestRequestTypeDef(BaseModel):
    WorkerId: str
    Reason: str

class DeleteHITRequestRequestTypeDef(BaseModel):
    HITId: str

class DeleteQualificationTypeRequestRequestTypeDef(BaseModel):
    QualificationTypeId: str

class DeleteWorkerBlockRequestRequestTypeDef(BaseModel):
    WorkerId: str
    Reason: Optional[str] = None

class DisassociateQualificationFromWorkerRequestRequestTypeDef(BaseModel):
    WorkerId: str
    QualificationTypeId: str
    Reason: Optional[str] = None

class GetAssignmentRequestRequestTypeDef(BaseModel):
    AssignmentId: str

class GetFileUploadURLRequestRequestTypeDef(BaseModel):
    AssignmentId: str
    QuestionIdentifier: str

class GetHITRequestRequestTypeDef(BaseModel):
    HITId: str

class GetQualificationScoreRequestRequestTypeDef(BaseModel):
    QualificationTypeId: str
    WorkerId: str

class GetQualificationTypeRequestRequestTypeDef(BaseModel):
    QualificationTypeId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssignmentsForHITRequestRequestTypeDef(BaseModel):
    HITId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AssignmentStatuses: Optional[Sequence[AssignmentStatusType]] = None

class ListBonusPaymentsRequestRequestTypeDef(BaseModel):
    HITId: Optional[str] = None
    AssignmentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHITsForQualificationTypeRequestRequestTypeDef(BaseModel):
    QualificationTypeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHITsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListQualificationRequestsRequestRequestTypeDef(BaseModel):
    QualificationTypeId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QualificationRequestTypeDef(BaseModel):
    QualificationRequestId: Optional[str] = None
    QualificationTypeId: Optional[str] = None
    WorkerId: Optional[str] = None
    Test: Optional[str] = None
    Answer: Optional[str] = None
    SubmitTime: Optional[datetime] = None

class ListQualificationTypesRequestRequestTypeDef(BaseModel):
    MustBeRequestable: bool
    Query: Optional[str] = None
    MustBeOwnedByCaller: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReviewPolicyResultsForHITRequestRequestTypeDef(BaseModel):
    HITId: str
    PolicyLevels: Optional[Sequence[ReviewPolicyLevelType]] = None
    RetrieveActions: Optional[bool] = None
    RetrieveResults: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReviewableHITsRequestRequestTypeDef(BaseModel):
    HITTypeId: Optional[str] = None
    Status: Optional[ReviewableHITStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListWorkerBlocksRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class WorkerBlockTypeDef(BaseModel):
    WorkerId: Optional[str] = None
    Reason: Optional[str] = None

class ListWorkersWithQualificationTypeRequestRequestTypeDef(BaseModel):
    QualificationTypeId: str
    Status: Optional[QualificationStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LocaleTypeDef(BaseModel):
    Country: str
    Subdivision: Optional[str] = None

class NotificationSpecificationTypeDef(BaseModel):
    Destination: str
    Transport: NotificationTransportType
    Version: str
    EventTypes: Sequence[EventTypeType]

class NotifyWorkersFailureStatusTypeDef(BaseModel):
    NotifyWorkersFailureCode: Optional[NotifyWorkersFailureCodeType] = None
    NotifyWorkersFailureMessage: Optional[str] = None
    WorkerId: Optional[str] = None

class NotifyWorkersRequestRequestTypeDef(BaseModel):
    Subject: str
    MessageText: str
    WorkerIds: Sequence[str]

class ParameterMapEntryTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class RejectAssignmentRequestRequestTypeDef(BaseModel):
    AssignmentId: str
    RequesterFeedback: str

class RejectQualificationRequestRequestRequestTypeDef(BaseModel):
    QualificationRequestId: str
    Reason: Optional[str] = None

class ReviewActionDetailTypeDef(BaseModel):
    ActionId: Optional[str] = None
    ActionName: Optional[str] = None
    TargetId: Optional[str] = None
    TargetType: Optional[str] = None
    Status: Optional[ReviewActionStatusType] = None
    CompleteTime: Optional[datetime] = None
    Result: Optional[str] = None
    ErrorCode: Optional[str] = None

class ReviewResultDetailTypeDef(BaseModel):
    ActionId: Optional[str] = None
    SubjectId: Optional[str] = None
    SubjectType: Optional[str] = None
    QuestionId: Optional[str] = None
    Key: Optional[str] = None
    Value: Optional[str] = None

class SendBonusRequestRequestTypeDef(BaseModel):
    WorkerId: str
    BonusAmount: str
    AssignmentId: str
    Reason: str
    UniqueRequestToken: Optional[str] = None

class UpdateHITReviewStatusRequestRequestTypeDef(BaseModel):
    HITId: str
    Revert: Optional[bool] = None

class UpdateHITTypeOfHITRequestRequestTypeDef(BaseModel):
    HITId: str
    HITTypeId: str

class UpdateQualificationTypeRequestRequestTypeDef(BaseModel):
    QualificationTypeId: str
    Description: Optional[str] = None
    QualificationTypeStatus: Optional[QualificationTypeStatusType] = None
    Test: Optional[str] = None
    AnswerKey: Optional[str] = None
    TestDurationInSeconds: Optional[int] = None
    RetryDelayInSeconds: Optional[int] = None
    AutoGranted: Optional[bool] = None
    AutoGrantedValue: Optional[int] = None

class CreateHITTypeResponseTypeDef(BaseModel):
    HITTypeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountBalanceResponseTypeDef(BaseModel):
    AvailableBalance: str
    OnHoldBalance: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFileUploadURLResponseTypeDef(BaseModel):
    FileUploadURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssignmentsForHITResponseTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    Assignments: List[AssignmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBonusPaymentsResponseTypeDef(BaseModel):
    NumResults: int
    NextToken: str
    BonusPayments: List[BonusPaymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQualificationTypeResponseTypeDef(BaseModel):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetQualificationTypeResponseTypeDef(BaseModel):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListQualificationTypesResponseTypeDef(BaseModel):
    NumResults: int
    NextToken: str
    QualificationTypes: List[QualificationTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQualificationTypeResponseTypeDef(BaseModel):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef(BaseModel):
    HITId: str
    AssignmentStatuses: Optional[Sequence[AssignmentStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef(BaseModel):
    HITId: Optional[str] = None
    AssignmentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef(BaseModel):
    QualificationTypeId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHITsRequestListHITsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef(BaseModel):
    QualificationTypeId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQualificationTypesRequestListQualificationTypesPaginateTypeDef(BaseModel):
    MustBeRequestable: bool
    Query: Optional[str] = None
    MustBeOwnedByCaller: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReviewableHITsRequestListReviewableHITsPaginateTypeDef(BaseModel):
    HITTypeId: Optional[str] = None
    Status: Optional[ReviewableHITStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef(BaseModel):
    QualificationTypeId: str
    Status: Optional[QualificationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQualificationRequestsResponseTypeDef(BaseModel):
    NumResults: int
    NextToken: str
    QualificationRequests: List[QualificationRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkerBlocksResponseTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    WorkerBlocks: List[WorkerBlockTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QualificationRequirementPaginatorTypeDef(BaseModel):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: Optional[List[int]] = None
    LocaleValues: Optional[List[LocaleTypeDef]] = None
    RequiredToPreview: Optional[bool] = None
    ActionsGuarded: Optional[HITAccessActionsType] = None

class QualificationRequirementTypeDef(BaseModel):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: Optional[Sequence[int]] = None
    LocaleValues: Optional[Sequence[LocaleTypeDef]] = None
    RequiredToPreview: Optional[bool] = None
    ActionsGuarded: Optional[HITAccessActionsType] = None

class QualificationTypeDef(BaseModel):
    QualificationTypeId: Optional[str] = None
    WorkerId: Optional[str] = None
    GrantTime: Optional[datetime] = None
    IntegerValue: Optional[int] = None
    LocaleValue: Optional[LocaleTypeDef] = None
    Status: Optional[QualificationStatusType] = None

class SendTestEventNotificationRequestRequestTypeDef(BaseModel):
    Notification: NotificationSpecificationTypeDef
    TestEventType: EventTypeType

class UpdateNotificationSettingsRequestRequestTypeDef(BaseModel):
    HITTypeId: str
    Notification: Optional[NotificationSpecificationTypeDef] = None
    Active: Optional[bool] = None

class NotifyWorkersResponseTypeDef(BaseModel):
    NotifyWorkersFailureStatuses: List[NotifyWorkersFailureStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyParameterTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    MapEntries: Optional[Sequence[ParameterMapEntryTypeDef]] = None

class ReviewReportTypeDef(BaseModel):
    ReviewResults: Optional[List[ReviewResultDetailTypeDef]] = None
    ReviewActions: Optional[List[ReviewActionDetailTypeDef]] = None

class UpdateExpirationForHITRequestRequestTypeDef(BaseModel):
    HITId: str
    ExpireAt: TimestampTypeDef

class HITPaginatorTypeDef(BaseModel):
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
    QualificationRequirements: Optional[List[QualificationRequirementPaginatorTypeDef]] = None
    HITReviewStatus: Optional[HITReviewStatusType] = None
    NumberOfAssignmentsPending: Optional[int] = None
    NumberOfAssignmentsAvailable: Optional[int] = None
    NumberOfAssignmentsCompleted: Optional[int] = None

class CreateHITTypeRequestRequestTypeDef(BaseModel):
    AssignmentDurationInSeconds: int
    Reward: str
    Title: str
    Description: str
    AutoApprovalDelayInSeconds: Optional[int] = None
    Keywords: Optional[str] = None
    QualificationRequirements: Optional[Sequence[QualificationRequirementTypeDef]] = None

class HITTypeDef(BaseModel):
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
    QualificationRequirements: Optional[List[QualificationRequirementTypeDef]] = None
    HITReviewStatus: Optional[HITReviewStatusType] = None
    NumberOfAssignmentsPending: Optional[int] = None
    NumberOfAssignmentsAvailable: Optional[int] = None
    NumberOfAssignmentsCompleted: Optional[int] = None

class GetQualificationScoreResponseTypeDef(BaseModel):
    Qualification: QualificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersWithQualificationTypeResponseTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    Qualifications: List[QualificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReviewPolicyTypeDef(BaseModel):
    PolicyName: str
    Parameters: Optional[Sequence[PolicyParameterTypeDef]] = None

class ListHITsForQualificationTypeResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    HITs: List[HITPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHITsResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    HITs: List[HITPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewableHITsResponsePaginatorTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    HITs: List[HITPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHITResponseTypeDef(BaseModel):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHITWithHITTypeResponseTypeDef(BaseModel):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssignmentResponseTypeDef(BaseModel):
    Assignment: AssignmentTypeDef
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHITResponseTypeDef(BaseModel):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHITsForQualificationTypeResponseTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHITsResponseTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewableHITsResponseTypeDef(BaseModel):
    NextToken: str
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHITRequestRequestTypeDef(BaseModel):
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
    QualificationRequirements: Optional[Sequence[QualificationRequirementTypeDef]] = None
    UniqueRequestToken: Optional[str] = None
    AssignmentReviewPolicy: Optional[ReviewPolicyTypeDef] = None
    HITReviewPolicy: Optional[ReviewPolicyTypeDef] = None
    HITLayoutId: Optional[str] = None
    HITLayoutParameters: Optional[Sequence[HITLayoutParameterTypeDef]] = None

class CreateHITWithHITTypeRequestRequestTypeDef(BaseModel):
    HITTypeId: str
    LifetimeInSeconds: int
    MaxAssignments: Optional[int] = None
    Question: Optional[str] = None
    RequesterAnnotation: Optional[str] = None
    UniqueRequestToken: Optional[str] = None
    AssignmentReviewPolicy: Optional[ReviewPolicyTypeDef] = None
    HITReviewPolicy: Optional[ReviewPolicyTypeDef] = None
    HITLayoutId: Optional[str] = None
    HITLayoutParameters: Optional[Sequence[HITLayoutParameterTypeDef]] = None

class ListReviewPolicyResultsForHITResponseTypeDef(BaseModel):
    HITId: str
    AssignmentReviewPolicy: ReviewPolicyTypeDef
    HITReviewPolicy: ReviewPolicyTypeDef
    AssignmentReviewReport: ReviewReportTypeDef
    HITReviewReport: ReviewReportTypeDef
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

