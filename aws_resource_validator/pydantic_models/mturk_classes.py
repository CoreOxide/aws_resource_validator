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
from aws_resource_validator.pydantic_models.mturk_constants import *

class AcceptQualificationRequestRequestRequestTypeDef(BaseValidatorModel):
    QualificationRequestId: str
    IntegerValue: Optional[int] = None

class ApproveAssignmentRequestRequestTypeDef(BaseValidatorModel):
    AssignmentId: str
    RequesterFeedback: Optional[str] = None
    OverrideRejection: Optional[bool] = None

class AssignmentTypeDef(BaseValidatorModel):
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

class AssociateQualificationWithWorkerRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    WorkerId: str
    IntegerValue: Optional[int] = None
    SendNotification: Optional[bool] = None

class BonusPaymentTypeDef(BaseValidatorModel):
    WorkerId: Optional[str] = None
    BonusAmount: Optional[str] = None
    AssignmentId: Optional[str] = None
    Reason: Optional[str] = None
    GrantTime: Optional[datetime] = None

class CreateAdditionalAssignmentsForHITRequestRequestTypeDef(BaseValidatorModel):
    HITId: str
    NumberOfAdditionalAssignments: int
    UniqueRequestToken: Optional[str] = None

class HITLayoutParameterTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateQualificationTypeRequestRequestTypeDef(BaseValidatorModel):
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

class QualificationTypeTypeDef(BaseValidatorModel):
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

class CreateWorkerBlockRequestRequestTypeDef(BaseValidatorModel):
    WorkerId: str
    Reason: str

class DeleteHITRequestRequestTypeDef(BaseValidatorModel):
    HITId: str

class DeleteQualificationTypeRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: str

class DeleteWorkerBlockRequestRequestTypeDef(BaseValidatorModel):
    WorkerId: str
    Reason: Optional[str] = None

class DisassociateQualificationFromWorkerRequestRequestTypeDef(BaseValidatorModel):
    WorkerId: str
    QualificationTypeId: str
    Reason: Optional[str] = None

class GetAssignmentRequestRequestTypeDef(BaseValidatorModel):
    AssignmentId: str

class GetFileUploadURLRequestRequestTypeDef(BaseValidatorModel):
    AssignmentId: str
    QuestionIdentifier: str

class GetHITRequestRequestTypeDef(BaseValidatorModel):
    HITId: str

class GetQualificationScoreRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    WorkerId: str

class GetQualificationTypeRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssignmentsForHITRequestRequestTypeDef(BaseValidatorModel):
    HITId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AssignmentStatuses: Optional[Sequence[AssignmentStatusType]] = None

class ListBonusPaymentsRequestRequestTypeDef(BaseValidatorModel):
    HITId: Optional[str] = None
    AssignmentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHITsForQualificationTypeRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHITsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListQualificationRequestsRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QualificationRequestTypeDef(BaseValidatorModel):
    QualificationRequestId: Optional[str] = None
    QualificationTypeId: Optional[str] = None
    WorkerId: Optional[str] = None
    Test: Optional[str] = None
    Answer: Optional[str] = None
    SubmitTime: Optional[datetime] = None

class ListQualificationTypesRequestRequestTypeDef(BaseValidatorModel):
    MustBeRequestable: bool
    Query: Optional[str] = None
    MustBeOwnedByCaller: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReviewPolicyResultsForHITRequestRequestTypeDef(BaseValidatorModel):
    HITId: str
    PolicyLevels: Optional[Sequence[ReviewPolicyLevelType]] = None
    RetrieveActions: Optional[bool] = None
    RetrieveResults: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListReviewableHITsRequestRequestTypeDef(BaseValidatorModel):
    HITTypeId: Optional[str] = None
    Status: Optional[ReviewableHITStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListWorkerBlocksRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class WorkerBlockTypeDef(BaseValidatorModel):
    WorkerId: Optional[str] = None
    Reason: Optional[str] = None

class ListWorkersWithQualificationTypeRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    Status: Optional[QualificationStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LocaleTypeDef(BaseValidatorModel):
    Country: str
    Subdivision: Optional[str] = None

class NotificationSpecificationTypeDef(BaseValidatorModel):
    Destination: str
    Transport: NotificationTransportType
    Version: str
    EventTypes: Sequence[EventTypeType]

class NotifyWorkersFailureStatusTypeDef(BaseValidatorModel):
    NotifyWorkersFailureCode: Optional[NotifyWorkersFailureCodeType] = None
    NotifyWorkersFailureMessage: Optional[str] = None
    WorkerId: Optional[str] = None

class NotifyWorkersRequestRequestTypeDef(BaseValidatorModel):
    Subject: str
    MessageText: str
    WorkerIds: Sequence[str]

class ParameterMapEntryTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class RejectAssignmentRequestRequestTypeDef(BaseValidatorModel):
    AssignmentId: str
    RequesterFeedback: str

class RejectQualificationRequestRequestRequestTypeDef(BaseValidatorModel):
    QualificationRequestId: str
    Reason: Optional[str] = None

class ReviewActionDetailTypeDef(BaseValidatorModel):
    ActionId: Optional[str] = None
    ActionName: Optional[str] = None
    TargetId: Optional[str] = None
    TargetType: Optional[str] = None
    Status: Optional[ReviewActionStatusType] = None
    CompleteTime: Optional[datetime] = None
    Result: Optional[str] = None
    ErrorCode: Optional[str] = None

class ReviewResultDetailTypeDef(BaseValidatorModel):
    ActionId: Optional[str] = None
    SubjectId: Optional[str] = None
    SubjectType: Optional[str] = None
    QuestionId: Optional[str] = None
    Key: Optional[str] = None
    Value: Optional[str] = None

class SendBonusRequestRequestTypeDef(BaseValidatorModel):
    WorkerId: str
    BonusAmount: str
    AssignmentId: str
    Reason: str
    UniqueRequestToken: Optional[str] = None

class UpdateHITReviewStatusRequestRequestTypeDef(BaseValidatorModel):
    HITId: str
    Revert: Optional[bool] = None

class UpdateHITTypeOfHITRequestRequestTypeDef(BaseValidatorModel):
    HITId: str
    HITTypeId: str

class UpdateQualificationTypeRequestRequestTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    Description: Optional[str] = None
    QualificationTypeStatus: Optional[QualificationTypeStatusType] = None
    Test: Optional[str] = None
    AnswerKey: Optional[str] = None
    TestDurationInSeconds: Optional[int] = None
    RetryDelayInSeconds: Optional[int] = None
    AutoGranted: Optional[bool] = None
    AutoGrantedValue: Optional[int] = None

class CreateHITTypeResponseTypeDef(BaseValidatorModel):
    HITTypeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountBalanceResponseTypeDef(BaseValidatorModel):
    AvailableBalance: str
    OnHoldBalance: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFileUploadURLResponseTypeDef(BaseValidatorModel):
    FileUploadURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssignmentsForHITResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    Assignments: List[AssignmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBonusPaymentsResponseTypeDef(BaseValidatorModel):
    NumResults: int
    NextToken: str
    BonusPayments: List[BonusPaymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQualificationTypeResponseTypeDef(BaseValidatorModel):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetQualificationTypeResponseTypeDef(BaseValidatorModel):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListQualificationTypesResponseTypeDef(BaseValidatorModel):
    NumResults: int
    NextToken: str
    QualificationTypes: List[QualificationTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQualificationTypeResponseTypeDef(BaseValidatorModel):
    QualificationType: QualificationTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssignmentsForHITRequestListAssignmentsForHITPaginateTypeDef(BaseValidatorModel):
    HITId: str
    AssignmentStatuses: Optional[Sequence[AssignmentStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBonusPaymentsRequestListBonusPaymentsPaginateTypeDef(BaseValidatorModel):
    HITId: Optional[str] = None
    AssignmentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHITsForQualificationTypeRequestListHITsForQualificationTypePaginateTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHITsRequestListHITsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQualificationRequestsRequestListQualificationRequestsPaginateTypeDef(BaseValidatorModel):
    QualificationTypeId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQualificationTypesRequestListQualificationTypesPaginateTypeDef(BaseValidatorModel):
    MustBeRequestable: bool
    Query: Optional[str] = None
    MustBeOwnedByCaller: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReviewableHITsRequestListReviewableHITsPaginateTypeDef(BaseValidatorModel):
    HITTypeId: Optional[str] = None
    Status: Optional[ReviewableHITStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkerBlocksRequestListWorkerBlocksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkersWithQualificationTypeRequestListWorkersWithQualificationTypePaginateTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    Status: Optional[QualificationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQualificationRequestsResponseTypeDef(BaseValidatorModel):
    NumResults: int
    NextToken: str
    QualificationRequests: List[QualificationRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkerBlocksResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    WorkerBlocks: List[WorkerBlockTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QualificationRequirementPaginatorTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: Optional[List[int]] = None
    LocaleValues: Optional[List[LocaleTypeDef]] = None
    RequiredToPreview: Optional[bool] = None
    ActionsGuarded: Optional[HITAccessActionsType] = None

class QualificationRequirementTypeDef(BaseValidatorModel):
    QualificationTypeId: str
    Comparator: ComparatorType
    IntegerValues: Optional[Sequence[int]] = None
    LocaleValues: Optional[Sequence[LocaleTypeDef]] = None
    RequiredToPreview: Optional[bool] = None
    ActionsGuarded: Optional[HITAccessActionsType] = None

class QualificationTypeDef(BaseValidatorModel):
    QualificationTypeId: Optional[str] = None
    WorkerId: Optional[str] = None
    GrantTime: Optional[datetime] = None
    IntegerValue: Optional[int] = None
    LocaleValue: Optional[LocaleTypeDef] = None
    Status: Optional[QualificationStatusType] = None

class SendTestEventNotificationRequestRequestTypeDef(BaseValidatorModel):
    Notification: NotificationSpecificationTypeDef
    TestEventType: EventTypeType

class UpdateNotificationSettingsRequestRequestTypeDef(BaseValidatorModel):
    HITTypeId: str
    Notification: Optional[NotificationSpecificationTypeDef] = None
    Active: Optional[bool] = None

class NotifyWorkersResponseTypeDef(BaseValidatorModel):
    NotifyWorkersFailureStatuses: List[NotifyWorkersFailureStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyParameterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None
    MapEntries: Optional[Sequence[ParameterMapEntryTypeDef]] = None

class ReviewReportTypeDef(BaseValidatorModel):
    ReviewResults: Optional[List[ReviewResultDetailTypeDef]] = None
    ReviewActions: Optional[List[ReviewActionDetailTypeDef]] = None

class UpdateExpirationForHITRequestRequestTypeDef(BaseValidatorModel):
    HITId: str
    ExpireAt: TimestampTypeDef

class HITPaginatorTypeDef(BaseValidatorModel):
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

class CreateHITTypeRequestRequestTypeDef(BaseValidatorModel):
    AssignmentDurationInSeconds: int
    Reward: str
    Title: str
    Description: str
    AutoApprovalDelayInSeconds: Optional[int] = None
    Keywords: Optional[str] = None
    QualificationRequirements: Optional[Sequence[QualificationRequirementTypeDef]] = None

class HITTypeDef(BaseValidatorModel):
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

class GetQualificationScoreResponseTypeDef(BaseValidatorModel):
    Qualification: QualificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkersWithQualificationTypeResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    Qualifications: List[QualificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReviewPolicyTypeDef(BaseValidatorModel):
    PolicyName: str
    Parameters: Optional[Sequence[PolicyParameterTypeDef]] = None

class ListHITsForQualificationTypeResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    HITs: List[HITPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHITsResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    HITs: List[HITPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewableHITsResponsePaginatorTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    HITs: List[HITPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHITResponseTypeDef(BaseValidatorModel):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHITWithHITTypeResponseTypeDef(BaseValidatorModel):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssignmentResponseTypeDef(BaseValidatorModel):
    Assignment: AssignmentTypeDef
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHITResponseTypeDef(BaseValidatorModel):
    HIT: HITTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHITsForQualificationTypeResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHITsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReviewableHITsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    NumResults: int
    HITs: List[HITTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHITRequestRequestTypeDef(BaseValidatorModel):
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

class CreateHITWithHITTypeRequestRequestTypeDef(BaseValidatorModel):
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

class ListReviewPolicyResultsForHITResponseTypeDef(BaseValidatorModel):
    HITId: str
    AssignmentReviewPolicy: ReviewPolicyTypeDef
    HITReviewPolicy: ReviewPolicyTypeDef
    AssignmentReviewReport: ReviewReportTypeDef
    HITReviewReport: ReviewReportTypeDef
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

