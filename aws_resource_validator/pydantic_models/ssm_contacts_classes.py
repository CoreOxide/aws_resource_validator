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
from aws_resource_validator.pydantic_models.ssm_contacts_constants import *

class AcceptPageRequestRequestTypeDef(BaseModel):
    PageId: str
    AcceptType: AcceptTypeType
    AcceptCode: str
    ContactChannelId: Optional[str] = None
    Note: Optional[str] = None
    AcceptCodeValidation: Optional[AcceptCodeValidationType] = None

class ActivateContactChannelRequestRequestTypeDef(BaseModel):
    ContactChannelId: str
    ActivationCode: str

class ChannelTargetInfoTypeDef(BaseModel):
    ContactChannelId: str
    RetryIntervalInMinutes: Optional[int] = None

class ContactChannelAddressTypeDef(BaseModel):
    SimpleAddress: Optional[str] = None

class ContactTargetInfoTypeDef(BaseModel):
    IsEssential: bool
    ContactId: Optional[str] = None

class ContactTypeDef(BaseModel):
    ContactArn: str
    Alias: str
    Type: ContactTypeType
    DisplayName: Optional[str] = None

class HandOffTimeTypeDef(BaseModel):
    HourOfDay: int
    MinuteOfHour: int

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DeactivateContactChannelRequestRequestTypeDef(BaseModel):
    ContactChannelId: str

class DeleteContactChannelRequestRequestTypeDef(BaseModel):
    ContactChannelId: str

class DeleteContactRequestRequestTypeDef(BaseModel):
    ContactId: str

class DeleteRotationOverrideRequestRequestTypeDef(BaseModel):
    RotationId: str
    RotationOverrideId: str

class DeleteRotationRequestRequestTypeDef(BaseModel):
    RotationId: str

class DescribeEngagementRequestRequestTypeDef(BaseModel):
    EngagementId: str

class DescribePageRequestRequestTypeDef(BaseModel):
    PageId: str

class EngagementTypeDef(BaseModel):
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None

class GetContactChannelRequestRequestTypeDef(BaseModel):
    ContactChannelId: str

class GetContactPolicyRequestRequestTypeDef(BaseModel):
    ContactArn: str

class GetContactRequestRequestTypeDef(BaseModel):
    ContactId: str

class GetRotationOverrideRequestRequestTypeDef(BaseModel):
    RotationId: str
    RotationOverrideId: str

class GetRotationRequestRequestTypeDef(BaseModel):
    RotationId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListContactChannelsRequestRequestTypeDef(BaseModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListContactsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AliasPrefix: Optional[str] = None
    Type: Optional[ContactTypeType] = None

class ListPageReceiptsRequestRequestTypeDef(BaseModel):
    PageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ReceiptTypeDef(BaseModel):
    ReceiptType: ReceiptTypeType
    ReceiptTime: datetime
    ContactChannelArn: Optional[str] = None
    ReceiptInfo: Optional[str] = None

class ListPageResolutionsRequestRequestTypeDef(BaseModel):
    PageId: str
    NextToken: Optional[str] = None

class ResolutionContactTypeDef(BaseModel):
    ContactArn: str
    Type: ContactTypeType
    StageIndex: Optional[int] = None

class ListPagesByContactRequestRequestTypeDef(BaseModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PageTypeDef(BaseModel):
    PageArn: str
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    SentTime: Optional[datetime] = None
    DeliveryTime: Optional[datetime] = None
    ReadTime: Optional[datetime] = None

class ListPagesByEngagementRequestRequestTypeDef(BaseModel):
    EngagementId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RotationOverrideTypeDef(BaseModel):
    RotationOverrideId: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime

class ListRotationsRequestRequestTypeDef(BaseModel):
    RotationNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class PutContactPolicyRequestRequestTypeDef(BaseModel):
    ContactArn: str
    Policy: str

class ShiftDetailsTypeDef(BaseModel):
    OverriddenContactIds: List[str]

class SendActivationCodeRequestRequestTypeDef(BaseModel):
    ContactChannelId: str

class StartEngagementRequestRequestTypeDef(BaseModel):
    ContactId: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: Optional[str] = None
    PublicContent: Optional[str] = None
    IncidentId: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class StopEngagementRequestRequestTypeDef(BaseModel):
    EngagementId: str
    Reason: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ContactChannelTypeDef(BaseModel):
    ContactChannelArn: str
    ContactArn: str
    Name: str
    DeliveryAddress: ContactChannelAddressTypeDef
    ActivationStatus: ActivationStatusType
    Type: Optional[ChannelTypeType] = None

class CreateContactChannelRequestRequestTypeDef(BaseModel):
    ContactId: str
    Name: str
    Type: ChannelTypeType
    DeliveryAddress: ContactChannelAddressTypeDef
    DeferActivation: Optional[bool] = None
    IdempotencyToken: Optional[str] = None

class UpdateContactChannelRequestRequestTypeDef(BaseModel):
    ContactChannelId: str
    Name: Optional[str] = None
    DeliveryAddress: Optional[ContactChannelAddressTypeDef] = None

class TargetTypeDef(BaseModel):
    ChannelTargetInfo: Optional[ChannelTargetInfoTypeDef] = None
    ContactTargetInfo: Optional[ContactTargetInfoTypeDef] = None

class CoverageTimeTypeDef(BaseModel):
    Start: Optional[HandOffTimeTypeDef] = None
    End: Optional[HandOffTimeTypeDef] = None

class MonthlySettingTypeDef(BaseModel):
    DayOfMonth: int
    HandOffTime: HandOffTimeTypeDef

class WeeklySettingTypeDef(BaseModel):
    DayOfWeek: DayOfWeekType
    HandOffTime: HandOffTimeTypeDef

class CreateContactChannelResultTypeDef(BaseModel):
    ContactChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactResultTypeDef(BaseModel):
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRotationOverrideResultTypeDef(BaseModel):
    RotationOverrideId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRotationResultTypeDef(BaseModel):
    RotationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngagementResultTypeDef(BaseModel):
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

class DescribePageResultTypeDef(BaseModel):
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

class GetContactChannelResultTypeDef(BaseModel):
    ContactArn: str
    ContactChannelArn: str
    Name: str
    Type: ChannelTypeType
    DeliveryAddress: ContactChannelAddressTypeDef
    ActivationStatus: ActivationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactPolicyResultTypeDef(BaseModel):
    ContactArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRotationOverrideResultTypeDef(BaseModel):
    RotationOverrideId: str
    RotationArn: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListContactsResultTypeDef(BaseModel):
    NextToken: str
    Contacts: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartEngagementResultTypeDef(BaseModel):
    EngagementArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRotationOverrideRequestRequestTypeDef(BaseModel):
    RotationId: str
    NewContactIds: Sequence[str]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    IdempotencyToken: Optional[str] = None

class ListRotationOverridesRequestRequestTypeDef(BaseModel):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRotationShiftsRequestRequestTypeDef(BaseModel):
    RotationId: str
    EndTime: TimestampTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PreviewOverrideTypeDef(BaseModel):
    NewMembers: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None

class TimeRangeTypeDef(BaseModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None

class ListEngagementsResultTypeDef(BaseModel):
    NextToken: str
    Engagements: List[EngagementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListContactChannelsRequestListContactChannelsPaginateTypeDef(BaseModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactsRequestListContactsPaginateTypeDef(BaseModel):
    AliasPrefix: Optional[str] = None
    Type: Optional[ContactTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPageReceiptsRequestListPageReceiptsPaginateTypeDef(BaseModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPageResolutionsRequestListPageResolutionsPaginateTypeDef(BaseModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPagesByContactRequestListPagesByContactPaginateTypeDef(BaseModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPagesByEngagementRequestListPagesByEngagementPaginateTypeDef(BaseModel):
    EngagementId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRotationOverridesRequestListRotationOverridesPaginateTypeDef(BaseModel):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRotationShiftsRequestListRotationShiftsPaginateTypeDef(BaseModel):
    RotationId: str
    EndTime: TimestampTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRotationsRequestListRotationsPaginateTypeDef(BaseModel):
    RotationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPageReceiptsResultTypeDef(BaseModel):
    NextToken: str
    Receipts: List[ReceiptTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPageResolutionsResultTypeDef(BaseModel):
    NextToken: str
    PageResolutions: List[ResolutionContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPagesByContactResultTypeDef(BaseModel):
    NextToken: str
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPagesByEngagementResultTypeDef(BaseModel):
    NextToken: str
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRotationOverridesResultTypeDef(BaseModel):
    RotationOverrides: List[RotationOverrideTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotationShiftTypeDef(BaseModel):
    StartTime: datetime
    EndTime: datetime
    ContactIds: Optional[List[str]] = None
    Type: Optional[ShiftTypeType] = None
    ShiftDetails: Optional[ShiftDetailsTypeDef] = None

class ListContactChannelsResultTypeDef(BaseModel):
    NextToken: str
    ContactChannels: List[ContactChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StageTypeDef(BaseModel):
    DurationInMinutes: int
    Targets: Sequence[TargetTypeDef]

class RecurrenceSettingsTypeDef(BaseModel):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: Optional[Sequence[MonthlySettingTypeDef]] = None
    WeeklySettings: Optional[Sequence[WeeklySettingTypeDef]] = None
    DailySettings: Optional[Sequence[HandOffTimeTypeDef]] = None
    ShiftCoverages: Optional[Mapping[DayOfWeekType, Sequence[CoverageTimeTypeDef]]] = None

class ListEngagementsRequestListEngagementsPaginateTypeDef(BaseModel):
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRangeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEngagementsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRangeTypeDef] = None

class ListPreviewRotationShiftsResultTypeDef(BaseModel):
    RotationShifts: List[RotationShiftTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRotationShiftsResultTypeDef(BaseModel):
    RotationShifts: List[RotationShiftTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PlanTypeDef(BaseModel):
    Stages: Optional[Sequence[StageTypeDef]] = None
    RotationIds: Optional[Sequence[str]] = None

class CreateRotationRequestRequestTypeDef(BaseModel):
    Name: str
    ContactIds: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IdempotencyToken: Optional[str] = None

class GetRotationResultTypeDef(BaseModel):
    RotationArn: str
    Name: str
    ContactIds: List[str]
    StartTime: datetime
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPreviewRotationShiftsRequestListPreviewRotationShiftsPaginateTypeDef(BaseModel):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    RotationStartTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Overrides: Optional[Sequence[PreviewOverrideTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPreviewRotationShiftsRequestRequestTypeDef(BaseModel):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    RotationStartTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Overrides: Optional[Sequence[PreviewOverrideTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RotationTypeDef(BaseModel):
    RotationArn: str
    Name: str
    ContactIds: Optional[List[str]] = None
    StartTime: Optional[datetime] = None
    TimeZoneId: Optional[str] = None
    Recurrence: Optional[RecurrenceSettingsTypeDef] = None

class UpdateRotationRequestRequestTypeDef(BaseModel):
    RotationId: str
    Recurrence: RecurrenceSettingsTypeDef
    ContactIds: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    TimeZoneId: Optional[str] = None

class CreateContactRequestRequestTypeDef(BaseModel):
    Alias: str
    Type: ContactTypeType
    Plan: PlanTypeDef
    DisplayName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IdempotencyToken: Optional[str] = None

class GetContactResultTypeDef(BaseModel):
    ContactArn: str
    Alias: str
    DisplayName: str
    Type: ContactTypeType
    Plan: PlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContactRequestRequestTypeDef(BaseModel):
    ContactId: str
    DisplayName: Optional[str] = None
    Plan: Optional[PlanTypeDef] = None

class ListRotationsResultTypeDef(BaseModel):
    NextToken: str
    Rotations: List[RotationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

