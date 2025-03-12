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

class AcceptPageRequestTypeDef(BaseValidatorModel):
    PageId: str
    AcceptType: AcceptTypeType
    AcceptCode: str
    ContactChannelId: Optional[str] = None
    Note: Optional[str] = None
    AcceptCodeValidation: Optional[AcceptCodeValidationType] = None


class ActivateContactChannelRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str
    ActivationCode: str


class ChannelTargetInfoTypeDef(BaseValidatorModel):
    ContactChannelId: str
    RetryIntervalInMinutes: Optional[int] = None


class ContactChannelAddressTypeDef(BaseValidatorModel):
    SimpleAddress: Optional[str] = None


class ContactTargetInfoTypeDef(BaseValidatorModel):
    IsEssential: bool
    ContactId: Optional[str] = None


class HandOffTimeTypeDef(BaseValidatorModel):
    HourOfDay: int
    MinuteOfHour: int


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class DeactivateContactChannelRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str


class DeleteContactChannelRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str


class DeleteContactRequestTypeDef(BaseValidatorModel):
    ContactId: str


class DeleteRotationOverrideRequestTypeDef(BaseValidatorModel):
    RotationId: str
    RotationOverrideId: str


class DeleteRotationRequestTypeDef(BaseValidatorModel):
    RotationId: str


class DescribeEngagementRequestTypeDef(BaseValidatorModel):
    EngagementId: str


class DescribePageRequestTypeDef(BaseValidatorModel):
    PageId: str


class EngagementTypeDef(BaseValidatorModel):
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None


class GetContactChannelRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str


class GetContactPolicyRequestTypeDef(BaseValidatorModel):
    ContactArn: str


class GetContactRequestTypeDef(BaseValidatorModel):
    ContactId: str


class GetRotationOverrideRequestTypeDef(BaseValidatorModel):
    RotationId: str
    RotationOverrideId: str


class GetRotationRequestTypeDef(BaseValidatorModel):
    RotationId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListContactChannelsRequestTypeDef(BaseValidatorModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPageReceiptsRequestTypeDef(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ReceiptTypeDef(BaseValidatorModel):
    ReceiptType: ReceiptTypeType
    ReceiptTime: datetime
    ContactChannelArn: Optional[str] = None
    ReceiptInfo: Optional[str] = None


class ListPageResolutionsRequestTypeDef(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None


class ListPagesByContactRequestTypeDef(BaseValidatorModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PageTypeDef(BaseValidatorModel):
    PageArn: str
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    SentTime: Optional[datetime] = None
    DeliveryTime: Optional[datetime] = None
    ReadTime: Optional[datetime] = None


class ListPagesByEngagementRequestTypeDef(BaseValidatorModel):
    EngagementId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RotationOverrideTypeDef(BaseValidatorModel):
    RotationOverrideId: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime


class ListRotationsRequestTypeDef(BaseValidatorModel):
    RotationNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class PutContactPolicyRequestTypeDef(BaseValidatorModel):
    ContactArn: str
    Policy: str


class ShiftDetailsTypeDef(BaseValidatorModel):
    OverriddenContactIds: List[str]


class SendActivationCodeRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str


class StartEngagementRequestTypeDef(BaseValidatorModel):
    ContactId: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: Optional[str] = None
    PublicContent: Optional[str] = None
    IncidentId: Optional[str] = None
    IdempotencyToken: Optional[str] = None


class StopEngagementRequestTypeDef(BaseValidatorModel):
    EngagementId: str
    Reason: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateContactChannelRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str
    Name: Optional[str] = None
    DeliveryAddress: Optional[ContactChannelAddressTypeDef] = None


class TargetTypeDef(BaseValidatorModel):
    ChannelTargetInfo: Optional[ChannelTargetInfoTypeDef] = None
    ContactTargetInfo: Optional[ContactTargetInfoTypeDef] = None


class CoverageTimeTypeDef(BaseValidatorModel):
    Start: Optional[HandOffTimeTypeDef] = None
    End: Optional[HandOffTimeTypeDef] = None


class MonthlySettingTypeDef(BaseValidatorModel):
    DayOfMonth: int
    HandOffTime: HandOffTimeTypeDef


class WeeklySettingTypeDef(BaseValidatorModel):
    DayOfWeek: DayOfWeekType
    HandOffTime: HandOffTimeTypeDef


class CreateContactChannelResultTypeDef(BaseValidatorModel):
    ContactChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContactResultTypeDef(BaseValidatorModel):
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRotationOverrideResultTypeDef(BaseValidatorModel):
    RotationOverrideId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRotationResultTypeDef(BaseValidatorModel):
    RotationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEngagementResultTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePageResultTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetContactPolicyResultTypeDef(BaseValidatorModel):
    ContactArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRotationOverrideResultTypeDef(BaseValidatorModel):
    RotationOverrideId: str
    RotationArn: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ContactTypeDef(BaseValidatorModel):
    pass


class ListContactsResultTypeDef(BaseValidatorModel):
    Contacts: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StartEngagementResultTypeDef(BaseValidatorModel):
    EngagementArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateRotationOverrideRequestTypeDef(BaseValidatorModel):
    RotationId: str
    NewContactIds: Sequence[str]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    IdempotencyToken: Optional[str] = None


class ListRotationOverridesRequestTypeDef(BaseValidatorModel):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListRotationShiftsRequestTypeDef(BaseValidatorModel):
    RotationId: str
    EndTime: TimestampTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PreviewOverrideTypeDef(BaseValidatorModel):
    NewMembers: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None


class TimeRangeTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None


class ListEngagementsResultTypeDef(BaseValidatorModel):
    Engagements: List[EngagementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListContactChannelsRequestPaginateTypeDef(BaseValidatorModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPageReceiptsRequestPaginateTypeDef(BaseValidatorModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPageResolutionsRequestPaginateTypeDef(BaseValidatorModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPagesByContactRequestPaginateTypeDef(BaseValidatorModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPagesByEngagementRequestPaginateTypeDef(BaseValidatorModel):
    EngagementId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRotationOverridesRequestPaginateTypeDef(BaseValidatorModel):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRotationShiftsRequestPaginateTypeDef(BaseValidatorModel):
    RotationId: str
    EndTime: TimestampTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRotationsRequestPaginateTypeDef(BaseValidatorModel):
    RotationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPageReceiptsResultTypeDef(BaseValidatorModel):
    Receipts: List[ReceiptTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResolutionContactTypeDef(BaseValidatorModel):
    pass


class ListPageResolutionsResultTypeDef(BaseValidatorModel):
    PageResolutions: List[ResolutionContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPagesByContactResultTypeDef(BaseValidatorModel):
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPagesByEngagementResultTypeDef(BaseValidatorModel):
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRotationOverridesResultTypeDef(BaseValidatorModel):
    RotationOverrides: List[RotationOverrideTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ContactChannelTypeDef(BaseValidatorModel):
    pass


class ListContactChannelsResultTypeDef(BaseValidatorModel):
    ContactChannels: List[ContactChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StageOutputTypeDef(BaseValidatorModel):
    DurationInMinutes: int
    Targets: List[TargetTypeDef]


class StageTypeDef(BaseValidatorModel):
    DurationInMinutes: int
    Targets: Sequence[TargetTypeDef]


class RecurrenceSettingsOutputTypeDef(BaseValidatorModel):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: Optional[List[MonthlySettingTypeDef]] = None
    WeeklySettings: Optional[List[WeeklySettingTypeDef]] = None
    DailySettings: Optional[List[HandOffTimeTypeDef]] = None
    ShiftCoverages: Optional[Dict[DayOfWeekType, List[CoverageTimeTypeDef]]] = None


class RecurrenceSettingsTypeDef(BaseValidatorModel):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: Optional[Sequence[MonthlySettingTypeDef]] = None
    WeeklySettings: Optional[Sequence[WeeklySettingTypeDef]] = None
    DailySettings: Optional[Sequence[HandOffTimeTypeDef]] = None
    ShiftCoverages: Optional[Mapping[DayOfWeekType, Sequence[CoverageTimeTypeDef]]] = None


class ListEngagementsRequestPaginateTypeDef(BaseValidatorModel):
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRangeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEngagementsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRangeTypeDef] = None


class RotationShiftTypeDef(BaseValidatorModel):
    pass


class ListPreviewRotationShiftsResultTypeDef(BaseValidatorModel):
    RotationShifts: List[RotationShiftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRotationShiftsResultTypeDef(BaseValidatorModel):
    RotationShifts: List[RotationShiftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PlanOutputTypeDef(BaseValidatorModel):
    Stages: Optional[List[StageOutputTypeDef]] = None
    RotationIds: Optional[List[str]] = None


class PlanTypeDef(BaseValidatorModel):
    Stages: Optional[Sequence[StageTypeDef]] = None
    RotationIds: Optional[Sequence[str]] = None


class GetRotationResultTypeDef(BaseValidatorModel):
    RotationArn: str
    Name: str
    ContactIds: List[str]
    StartTime: datetime
    TimeZoneId: str
    Recurrence: RecurrenceSettingsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RotationTypeDef(BaseValidatorModel):
    RotationArn: str
    Name: str
    ContactIds: Optional[List[str]] = None
    StartTime: Optional[datetime] = None
    TimeZoneId: Optional[str] = None
    Recurrence: Optional[RecurrenceSettingsOutputTypeDef] = None


class ListRotationsResultTypeDef(BaseValidatorModel):
    Rotations: List[RotationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RecurrenceSettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreateRotationRequestTypeDef(BaseValidatorModel):
    Name: str
    ContactIds: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IdempotencyToken: Optional[str] = None


class ListPreviewRotationShiftsRequestPaginateTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    RotationStartTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Overrides: Optional[Sequence[PreviewOverrideTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPreviewRotationShiftsRequestTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    RotationStartTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Overrides: Optional[Sequence[PreviewOverrideTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UpdateRotationRequestTypeDef(BaseValidatorModel):
    RotationId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    ContactIds: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    TimeZoneId: Optional[str] = None


class PlanUnionTypeDef(BaseValidatorModel):
    pass


class UpdateContactRequestTypeDef(BaseValidatorModel):
    ContactId: str
    DisplayName: Optional[str] = None
    Plan: Optional[PlanUnionTypeDef] = None


