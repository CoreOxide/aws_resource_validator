from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ssm_contacts.ssm_contacts_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


class Contact(BaseValidatorModel):
    ContactArn: str
    Alias: str
    Type: ContactTypeType
    DisplayName: Optional[str] = None


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

Timestamp = Union[datetime, str]


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


# This class is the input for the 'describe_engagement' function.
class DescribeEngagementRequest(BaseValidatorModel):
    EngagementId: str


# This class is the input for the 'describe_page' function.
class DescribePageRequest(BaseValidatorModel):
    PageId: str


class Engagement(BaseValidatorModel):
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None


# This class is the input for the 'get_contact_channel' function.
class GetContactChannelRequest(BaseValidatorModel):
    ContactChannelId: str


# This class is the input for the 'get_contact_policy' function.
class GetContactPolicyRequest(BaseValidatorModel):
    ContactArn: str


# This class is the input for the 'get_contact' function.
class GetContactRequest(BaseValidatorModel):
    ContactId: str


# This class is the input for the 'get_rotation_override' function.
class GetRotationOverrideRequest(BaseValidatorModel):
    RotationId: str
    RotationOverrideId: str


# This class is the input for the 'get_rotation' function.
class GetRotationRequest(BaseValidatorModel):
    RotationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_contact_channels' function.
class ListContactChannelsRequest(BaseValidatorModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_contacts' function.
class ListContactsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AliasPrefix: Optional[str] = None
    Type: Optional[ContactTypeType] = None


# This class is the input for the 'list_page_receipts' function.
class ListPageReceiptsRequest(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Receipt(BaseValidatorModel):
    ReceiptType: ReceiptTypeType
    ReceiptTime: datetime
    ContactChannelArn: Optional[str] = None
    ReceiptInfo: Optional[str] = None


# This class is the input for the 'list_page_resolutions' function.
class ListPageResolutionsRequest(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None


class ResolutionContact(BaseValidatorModel):
    ContactArn: str
    Type: ContactTypeType
    StageIndex: Optional[int] = None


# This class is the input for the 'list_pages_by_contact' function.
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


# This class is the input for the 'list_pages_by_engagement' function.
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


# This class is the input for the 'list_rotations' function.
class ListRotationsRequest(BaseValidatorModel):
    RotationNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class PutContactPolicyRequest(BaseValidatorModel):
    ContactArn: str
    Policy: str


class ShiftDetails(BaseValidatorModel):
    OverriddenContactIds: List[str]


class SendActivationCodeRequest(BaseValidatorModel):
    ContactChannelId: str


# This class is the input for the 'start_engagement' function.
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
    TagKeys: List[str]


class ContactChannel(BaseValidatorModel):
    ContactChannelArn: str
    ContactArn: str
    Name: str
    DeliveryAddress: ContactChannelAddress
    ActivationStatus: ActivationStatusType
    Type: Optional[ChannelTypeType] = None


# This class is the input for the 'create_contact_channel' function.
class CreateContactChannelRequest(BaseValidatorModel):
    ContactId: str
    Name: str
    Type: ChannelTypeType
    DeliveryAddress: ContactChannelAddress
    DeferActivation: Optional[bool] = None
    IdempotencyToken: Optional[str] = None


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


# This class is the output for the 'create_contact_channel' function.
class CreateContactChannelResult(BaseValidatorModel):
    ContactChannelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_contact' function.
class CreateContactResult(BaseValidatorModel):
    ContactArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_rotation_override' function.
class CreateRotationOverrideResult(BaseValidatorModel):
    RotationOverrideId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_rotation' function.
class CreateRotationResult(BaseValidatorModel):
    RotationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_engagement' function.
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


# This class is the output for the 'describe_page' function.
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


# This class is the output for the 'get_contact_channel' function.
class GetContactChannelResult(BaseValidatorModel):
    ContactArn: str
    ContactChannelArn: str
    Name: str
    Type: ChannelTypeType
    DeliveryAddress: ContactChannelAddress
    ActivationStatus: ActivationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_contact_policy' function.
class GetContactPolicyResult(BaseValidatorModel):
    ContactArn: str
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rotation_override' function.
class GetRotationOverrideResult(BaseValidatorModel):
    RotationOverrideId: str
    RotationArn: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_contacts' function.
class ListContactsResult(BaseValidatorModel):
    Contacts: List[Contact]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_engagement' function.
class StartEngagementResult(BaseValidatorModel):
    EngagementArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResult(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the input for the 'create_rotation_override' function.
class CreateRotationOverrideRequest(BaseValidatorModel):
    RotationId: str
    NewContactIds: List[str]
    StartTime: Timestamp
    EndTime: Timestamp
    IdempotencyToken: Optional[str] = None


# This class is the input for the 'list_rotation_overrides' function.
class ListRotationOverridesRequest(BaseValidatorModel):
    RotationId: str
    StartTime: Timestamp
    EndTime: Timestamp
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_rotation_shifts' function.
class ListRotationShiftsRequest(BaseValidatorModel):
    RotationId: str
    EndTime: Timestamp
    StartTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PreviewOverride(BaseValidatorModel):
    NewMembers: Optional[List[str]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class TimeRange(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


# This class is the output for the 'list_engagements' function.
class ListEngagementsResult(BaseValidatorModel):
    Engagements: List[Engagement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListContactChannelsRequestPaginate(BaseValidatorModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactsRequestPaginate(BaseValidatorModel):
    AliasPrefix: Optional[str] = None
    Type: Optional[ContactTypeType] = None
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


# This class is the output for the 'list_page_receipts' function.
class ListPageReceiptsResult(BaseValidatorModel):
    Receipts: List[Receipt]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_page_resolutions' function.
class ListPageResolutionsResult(BaseValidatorModel):
    PageResolutions: List[ResolutionContact]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_pages_by_contact' function.
class ListPagesByContactResult(BaseValidatorModel):
    Pages: List[Page]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_pages_by_engagement' function.
class ListPagesByEngagementResult(BaseValidatorModel):
    Pages: List[Page]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_rotation_overrides' function.
class ListRotationOverridesResult(BaseValidatorModel):
    RotationOverrides: List[RotationOverride]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RotationShift(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ContactIds: Optional[List[str]] = None
    Type: Optional[ShiftTypeType] = None
    ShiftDetails: Optional[ShiftDetails] = None


# This class is the output for the 'list_contact_channels' function.
class ListContactChannelsResult(BaseValidatorModel):
    ContactChannels: List[ContactChannel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StageOutput(BaseValidatorModel):
    DurationInMinutes: int
    Targets: List[Target]


class Stage(BaseValidatorModel):
    DurationInMinutes: int
    Targets: List[Target]


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
    MonthlySettings: Optional[List[MonthlySetting]] = None
    WeeklySettings: Optional[List[WeeklySetting]] = None
    DailySettings: Optional[List[HandOffTime]] = None
    ShiftCoverages: Optional[Dict[DayOfWeekType, List[CoverageTime]]] = None


class ListEngagementsRequestPaginate(BaseValidatorModel):
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRange] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_engagements' function.
class ListEngagementsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRange] = None


# This class is the output for the 'list_preview_rotation_shifts' function.
class ListPreviewRotationShiftsResult(BaseValidatorModel):
    RotationShifts: List[RotationShift]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_rotation_shifts' function.
class ListRotationShiftsResult(BaseValidatorModel):
    RotationShifts: List[RotationShift]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PlanOutput(BaseValidatorModel):
    Stages: Optional[List[StageOutput]] = None
    RotationIds: Optional[List[str]] = None


class Plan(BaseValidatorModel):
    Stages: Optional[List[Stage]] = None
    RotationIds: Optional[List[str]] = None


# This class is the output for the 'get_rotation' function.
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

RecurrenceSettingsUnion = Union[RecurrenceSettings, RecurrenceSettingsOutput]


# This class is the output for the 'get_contact' function.
class GetContactResult(BaseValidatorModel):
    ContactArn: str
    Alias: str
    DisplayName: str
    Type: ContactTypeType
    Plan: PlanOutput
    ResponseMetadata: ResponseMetadata

PlanUnion = Union[Plan, PlanOutput]


# This class is the output for the 'list_rotations' function.
class ListRotationsResult(BaseValidatorModel):
    Rotations: List[Rotation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_rotation' function.
class CreateRotationRequest(BaseValidatorModel):
    Name: str
    ContactIds: List[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnion
    StartTime: Optional[Timestamp] = None
    Tags: Optional[List[Tag]] = None
    IdempotencyToken: Optional[str] = None


class ListPreviewRotationShiftsRequestPaginate(BaseValidatorModel):
    EndTime: Timestamp
    Members: List[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnion
    RotationStartTime: Optional[Timestamp] = None
    StartTime: Optional[Timestamp] = None
    Overrides: Optional[List[PreviewOverride]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_preview_rotation_shifts' function.
class ListPreviewRotationShiftsRequest(BaseValidatorModel):
    EndTime: Timestamp
    Members: List[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnion
    RotationStartTime: Optional[Timestamp] = None
    StartTime: Optional[Timestamp] = None
    Overrides: Optional[List[PreviewOverride]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UpdateRotationRequest(BaseValidatorModel):
    RotationId: str
    Recurrence: RecurrenceSettingsUnion
    ContactIds: Optional[List[str]] = None
    StartTime: Optional[Timestamp] = None
    TimeZoneId: Optional[str] = None


# This class is the input for the 'create_contact' function.
class CreateContactRequest(BaseValidatorModel):
    Alias: str
    Type: ContactTypeType
    Plan: PlanUnion
    DisplayName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    IdempotencyToken: Optional[str] = None


class UpdateContactRequest(BaseValidatorModel):
    ContactId: str
    DisplayName: Optional[str] = None
    Plan: Optional[PlanUnion] = None