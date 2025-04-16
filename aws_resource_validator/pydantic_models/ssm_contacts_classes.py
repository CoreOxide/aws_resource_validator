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
from aws_resource_validator.pydantic_models.ssm_contacts_constants import *

class AcceptPageRequest(BaseValidatorModel):
    PageId: str
    AcceptType: AcceptTypeType
    AcceptCode: str
    ContactChannelId: Optional[str] = None
    Note: Optional[str] = None
    AcceptCodeValidation: Optional[AcceptCodeValidationType] = None


class ActivateContactChannelRequest(BaseValidatorModel):
    ContactChannelId: str
    ActivationCode: str


class ChannelTargetInfo(BaseValidatorModel):
    ContactChannelId: str
    RetryIntervalInMinutes: Optional[int] = None


class ContactChannelAddress(BaseValidatorModel):
    SimpleAddress: Optional[str] = None


class ContactTargetInfo(BaseValidatorModel):
    IsEssential: bool
    ContactId: Optional[str] = None


class HandOffTime(BaseValidatorModel):
    HourOfDay: int
    MinuteOfHour: int


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DeactivateContactChannelRequest(BaseValidatorModel):
    ContactChannelId: str


class DeleteContactChannelRequest(BaseValidatorModel):
    ContactChannelId: str


class DeleteContactRequest(BaseValidatorModel):
    ContactId: str


class DeleteRotationOverrideRequest(BaseValidatorModel):
    RotationId: str
    RotationOverrideId: str


class DeleteRotationRequest(BaseValidatorModel):
    RotationId: str


class DescribeEngagementRequest(BaseValidatorModel):
    EngagementId: str


class DescribePageRequest(BaseValidatorModel):
    PageId: str


class Engagement(BaseValidatorModel):
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None


class GetContactChannelRequest(BaseValidatorModel):
    ContactChannelId: str


class GetContactPolicyRequest(BaseValidatorModel):
    ContactArn: str


class GetContactRequest(BaseValidatorModel):
    ContactId: str


class GetRotationOverrideRequest(BaseValidatorModel):
    RotationId: str
    RotationOverrideId: str


class GetRotationRequest(BaseValidatorModel):
    RotationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListContactChannelsRequest(BaseValidatorModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPageReceiptsRequest(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Receipt(BaseValidatorModel):
    ReceiptType: ReceiptTypeType
    ReceiptTime: datetime
    ContactChannelArn: Optional[str] = None
    ReceiptInfo: Optional[str] = None


class ListPageResolutionsRequest(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None


class ListPagesByContactRequest(BaseValidatorModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Page(BaseValidatorModel):
    PageArn: str
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    SentTime: Optional[datetime] = None
    DeliveryTime: Optional[datetime] = None
    ReadTime: Optional[datetime] = None


class ListPagesByEngagementRequest(BaseValidatorModel):
    EngagementId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RotationOverride(BaseValidatorModel):
    RotationOverrideId: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime


class ListRotationsRequest(BaseValidatorModel):
    RotationNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class PutContactPolicyRequest(BaseValidatorModel):
    ContactArn: str
    Policy: str


class ShiftDetails(BaseValidatorModel):
    OverriddenContactIds: List[str]


class SendActivationCodeRequest(BaseValidatorModel):
    ContactChannelId: str


class StartEngagementRequest(BaseValidatorModel):
    ContactId: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: Optional[str] = None
    PublicContent: Optional[str] = None
    IncidentId: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class StopEngagementRequest(BaseValidatorModel):
    EngagementId: str
    Reason: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateContactChannelRequest(BaseValidatorModel):
    ContactChannelId: str
    Name: Optional[str] = None
    DeliveryAddress: Optional[ContactChannelAddress] = None


class Target(BaseValidatorModel):
    ChannelTargetInfo: Optional[ChannelTargetInfo] = None
    ContactTargetInfo: Optional[ContactTargetInfo] = None


class CoverageTime(BaseValidatorModel):
    Start: Optional[HandOffTime] = None
    End: Optional[HandOffTime] = None


class MonthlySetting(BaseValidatorModel):
    DayOfMonth: int
    HandOffTime: HandOffTime


class WeeklySetting(BaseValidatorModel):
    DayOfWeek: DayOfWeekType
    HandOffTime: HandOffTime


class CreateContactChannelResult(BaseValidatorModel):
    ContactChannelArn: str
    ResponseMetadata: ResponseMetadata


class CreateContactResult(BaseValidatorModel):
    ContactArn: str
    ResponseMetadata: ResponseMetadata


class CreateRotationOverrideResult(BaseValidatorModel):
    RotationOverrideId: str
    ResponseMetadata: ResponseMetadata


class CreateRotationResult(BaseValidatorModel):
    RotationArn: str
    ResponseMetadata: ResponseMetadata


class DescribeEngagementResult(BaseValidatorModel):
    ContactArn: str
    EngagementArn: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: str
    PublicContent: str
    IncidentId: str
    StartTime: datetime
    StopTime: datetime
    ResponseMetadata: ResponseMetadata


class DescribePageResult(BaseValidatorModel):
    PageArn: str
    EngagementArn: str
    ContactArn: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: str
    PublicContent: str
    IncidentId: str
    SentTime: datetime
    ReadTime: datetime
    DeliveryTime: datetime
    ResponseMetadata: ResponseMetadata


class GetContactPolicyResult(BaseValidatorModel):
    ContactArn: str
    Policy: str
    ResponseMetadata: ResponseMetadata


class GetRotationOverrideResult(BaseValidatorModel):
    RotationOverrideId: str
    RotationArn: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


class Contact(BaseValidatorModel):
    pass


class ListContactsResult(BaseValidatorModel):
    Contacts: List[Contact]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartEngagementResult(BaseValidatorModel):
    EngagementArn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResult(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class Timestamp(BaseValidatorModel):
    pass


class CreateRotationOverrideRequest(BaseValidatorModel):
    RotationId: str
    NewContactIds: Sequence[str]
    StartTime: Timestamp
    EndTime: Timestamp
    IdempotencyToken: Optional[str] = None


class ListRotationOverridesRequest(BaseValidatorModel):
    RotationId: str
    StartTime: Timestamp
    EndTime: Timestamp
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRotationShiftsRequest(BaseValidatorModel):
    RotationId: str
    EndTime: Timestamp
    StartTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PreviewOverride(BaseValidatorModel):
    NewMembers: Optional[Sequence[str]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class TimeRange(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class ListEngagementsResult(BaseValidatorModel):
    Engagements: List[Engagement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListContactChannelsRequestPaginate(BaseValidatorModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPageReceiptsRequestPaginate(BaseValidatorModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPageResolutionsRequestPaginate(BaseValidatorModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPagesByContactRequestPaginate(BaseValidatorModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPagesByEngagementRequestPaginate(BaseValidatorModel):
    EngagementId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRotationOverridesRequestPaginate(BaseValidatorModel):
    RotationId: str
    StartTime: Timestamp
    EndTime: Timestamp
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRotationShiftsRequestPaginate(BaseValidatorModel):
    RotationId: str
    EndTime: Timestamp
    StartTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRotationsRequestPaginate(BaseValidatorModel):
    RotationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPageReceiptsResult(BaseValidatorModel):
    Receipts: List[Receipt]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResolutionContact(BaseValidatorModel):
    pass


class ListPageResolutionsResult(BaseValidatorModel):
    PageResolutions: List[ResolutionContact]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPagesByContactResult(BaseValidatorModel):
    Pages: List[Page]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPagesByEngagementResult(BaseValidatorModel):
    Pages: List[Page]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRotationOverridesResult(BaseValidatorModel):
    RotationOverrides: List[RotationOverride]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ContactChannel(BaseValidatorModel):
    pass


class ListContactChannelsResult(BaseValidatorModel):
    ContactChannels: List[ContactChannel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StageOutput(BaseValidatorModel):
    DurationInMinutes: int
    Targets: List[Target]


class Stage(BaseValidatorModel):
    DurationInMinutes: int
    Targets: Sequence[Target]


class RecurrenceSettingsOutput(BaseValidatorModel):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: Optional[List[MonthlySetting]] = None
    WeeklySettings: Optional[List[WeeklySetting]] = None
    DailySettings: Optional[List[HandOffTime]] = None
    ShiftCoverages: Optional[Dict[DayOfWeekType, List[CoverageTime]]] = None


class RecurrenceSettings(BaseValidatorModel):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: Optional[Sequence[MonthlySetting]] = None
    WeeklySettings: Optional[Sequence[WeeklySetting]] = None
    DailySettings: Optional[Sequence[HandOffTime]] = None
    ShiftCoverages: Optional[Mapping[DayOfWeekType, Sequence[CoverageTime]]] = None


class ListEngagementsRequestPaginate(BaseValidatorModel):
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRange] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEngagementsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRange] = None


class RotationShift(BaseValidatorModel):
    pass


class ListPreviewRotationShiftsResult(BaseValidatorModel):
    RotationShifts: List[RotationShift]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRotationShiftsResult(BaseValidatorModel):
    RotationShifts: List[RotationShift]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PlanOutput(BaseValidatorModel):
    Stages: Optional[List[StageOutput]] = None
    RotationIds: Optional[List[str]] = None


class Plan(BaseValidatorModel):
    Stages: Optional[Sequence[Stage]] = None
    RotationIds: Optional[Sequence[str]] = None


class GetRotationResult(BaseValidatorModel):
    RotationArn: str
    Name: str
    ContactIds: List[str]
    StartTime: datetime
    TimeZoneId: str
    Recurrence: RecurrenceSettingsOutput
    ResponseMetadata: ResponseMetadata


class Rotation(BaseValidatorModel):
    RotationArn: str
    Name: str
    ContactIds: Optional[List[str]] = None
    StartTime: Optional[datetime] = None
    TimeZoneId: Optional[str] = None
    Recurrence: Optional[RecurrenceSettingsOutput] = None


class ListRotationsResult(BaseValidatorModel):
    Rotations: List[Rotation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RecurrenceSettingsUnion(BaseValidatorModel):
    pass


class CreateRotationRequest(BaseValidatorModel):
    Name: str
    ContactIds: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnion
    StartTime: Optional[Timestamp] = None
    Tags: Optional[Sequence[Tag]] = None
    IdempotencyToken: Optional[str] = None


class ListPreviewRotationShiftsRequestPaginate(BaseValidatorModel):
    EndTime: Timestamp
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnion
    RotationStartTime: Optional[Timestamp] = None
    StartTime: Optional[Timestamp] = None
    Overrides: Optional[Sequence[PreviewOverride]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPreviewRotationShiftsRequest(BaseValidatorModel):
    EndTime: Timestamp
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnion
    RotationStartTime: Optional[Timestamp] = None
    StartTime: Optional[Timestamp] = None
    Overrides: Optional[Sequence[PreviewOverride]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UpdateRotationRequest(BaseValidatorModel):
    RotationId: str
    Recurrence: RecurrenceSettingsUnion
    ContactIds: Optional[Sequence[str]] = None
    StartTime: Optional[Timestamp] = None
    TimeZoneId: Optional[str] = None


class PlanUnion(BaseValidatorModel):
    pass


class UpdateContactRequest(BaseValidatorModel):
    ContactId: str
    DisplayName: Optional[str] = None
    Plan: Optional[PlanUnion] = None


