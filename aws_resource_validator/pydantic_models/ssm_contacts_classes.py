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
from aws_resource_validator.pydantic_models.ssm_contacts_constants import *

class AcceptPageRequestRequestTypeDef(BaseValidatorModel):
    PageId: str
    AcceptType: AcceptTypeType
    AcceptCode: str
    ContactChannelId: Optional[str] = None
    Note: Optional[str] = None
    AcceptCodeValidation: Optional[AcceptCodeValidationType] = None

class ActivateContactChannelRequestRequestTypeDef(BaseValidatorModel):
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

class ContactTypeDef(BaseValidatorModel):
    ContactArn: str
    Alias: str
    Type: ContactTypeType
    DisplayName: Optional[str] = None

class HandOffTimeTypeDef(BaseValidatorModel):
    HourOfDay: int
    MinuteOfHour: int

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class DeactivateContactChannelRequestRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str

class DeleteContactChannelRequestRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str

class DeleteContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str

class DeleteRotationOverrideRequestRequestTypeDef(BaseValidatorModel):
    RotationId: str
    RotationOverrideId: str

class DeleteRotationRequestRequestTypeDef(BaseValidatorModel):
    RotationId: str

class DescribeEngagementRequestRequestTypeDef(BaseValidatorModel):
    EngagementId: str

class DescribePageRequestRequestTypeDef(BaseValidatorModel):
    PageId: str

class EngagementTypeDef(BaseValidatorModel):
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None

class GetContactChannelRequestRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str

class GetContactPolicyRequestRequestTypeDef(BaseValidatorModel):
    ContactArn: str

class GetContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str

class GetRotationOverrideRequestRequestTypeDef(BaseValidatorModel):
    RotationId: str
    RotationOverrideId: str

class GetRotationRequestRequestTypeDef(BaseValidatorModel):
    RotationId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListContactChannelsRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListContactsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AliasPrefix: Optional[str] = None
    Type: Optional[ContactTypeType] = None

class ListPageReceiptsRequestRequestTypeDef(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ReceiptTypeDef(BaseValidatorModel):
    ReceiptType: ReceiptTypeType
    ReceiptTime: datetime
    ContactChannelArn: Optional[str] = None
    ReceiptInfo: Optional[str] = None

class ListPageResolutionsRequestRequestTypeDef(BaseValidatorModel):
    PageId: str
    NextToken: Optional[str] = None

class ResolutionContactTypeDef(BaseValidatorModel):
    ContactArn: str
    Type: ContactTypeType
    StageIndex: Optional[int] = None

class ListPagesByContactRequestRequestTypeDef(BaseValidatorModel):
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

class ListPagesByEngagementRequestRequestTypeDef(BaseValidatorModel):
    EngagementId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RotationOverrideTypeDef(BaseValidatorModel):
    RotationOverrideId: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime

class ListRotationsRequestRequestTypeDef(BaseValidatorModel):
    RotationNamePrefix: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class PutContactPolicyRequestRequestTypeDef(BaseValidatorModel):
    ContactArn: str
    Policy: str

class ShiftDetailsTypeDef(BaseValidatorModel):
    OverriddenContactIds: List[str]

class SendActivationCodeRequestRequestTypeDef(BaseValidatorModel):
    ContactChannelId: str

class StartEngagementRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: Optional[str] = None
    PublicContent: Optional[str] = None
    IncidentId: Optional[str] = None
    IdempotencyToken: Optional[str] = None

class StopEngagementRequestRequestTypeDef(BaseValidatorModel):
    EngagementId: str
    Reason: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class ContactChannelTypeDef(BaseValidatorModel):
    ContactChannelArn: str
    ContactArn: str
    Name: str
    DeliveryAddress: ContactChannelAddressTypeDef
    ActivationStatus: ActivationStatusType
    Type: Optional[ChannelTypeType] = None

class CreateContactChannelRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    Name: str
    Type: ChannelTypeType
    DeliveryAddress: ContactChannelAddressTypeDef
    DeferActivation: Optional[bool] = None
    IdempotencyToken: Optional[str] = None

class UpdateContactChannelRequestRequestTypeDef(BaseValidatorModel):
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

class GetContactChannelResultTypeDef(BaseValidatorModel):
    ContactArn: str
    ContactChannelArn: str
    Name: str
    Type: ChannelTypeType
    DeliveryAddress: ContactChannelAddressTypeDef
    ActivationStatus: ActivationStatusType
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

class ListContactsResultTypeDef(BaseValidatorModel):
    NextToken: str
    Contacts: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartEngagementResultTypeDef(BaseValidatorModel):
    EngagementArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRotationOverrideRequestRequestTypeDef(BaseValidatorModel):
    RotationId: str
    NewContactIds: Sequence[str]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    IdempotencyToken: Optional[str] = None

class ListRotationOverridesRequestRequestTypeDef(BaseValidatorModel):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRotationShiftsRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    Engagements: List[EngagementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListContactChannelsRequestListContactChannelsPaginateTypeDef(BaseValidatorModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactsRequestListContactsPaginateTypeDef(BaseValidatorModel):
    AliasPrefix: Optional[str] = None
    Type: Optional[ContactTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPageReceiptsRequestListPageReceiptsPaginateTypeDef(BaseValidatorModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPageResolutionsRequestListPageResolutionsPaginateTypeDef(BaseValidatorModel):
    PageId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPagesByContactRequestListPagesByContactPaginateTypeDef(BaseValidatorModel):
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPagesByEngagementRequestListPagesByEngagementPaginateTypeDef(BaseValidatorModel):
    EngagementId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRotationOverridesRequestListRotationOverridesPaginateTypeDef(BaseValidatorModel):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRotationShiftsRequestListRotationShiftsPaginateTypeDef(BaseValidatorModel):
    RotationId: str
    EndTime: TimestampTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRotationsRequestListRotationsPaginateTypeDef(BaseValidatorModel):
    RotationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPageReceiptsResultTypeDef(BaseValidatorModel):
    NextToken: str
    Receipts: List[ReceiptTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPageResolutionsResultTypeDef(BaseValidatorModel):
    NextToken: str
    PageResolutions: List[ResolutionContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPagesByContactResultTypeDef(BaseValidatorModel):
    NextToken: str
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPagesByEngagementResultTypeDef(BaseValidatorModel):
    NextToken: str
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRotationOverridesResultTypeDef(BaseValidatorModel):
    RotationOverrides: List[RotationOverrideTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotationShiftTypeDef(BaseValidatorModel):
    StartTime: datetime
    EndTime: datetime
    ContactIds: Optional[List[str]] = None
    Type: Optional[ShiftTypeType] = None
    ShiftDetails: Optional[ShiftDetailsTypeDef] = None

class ListContactChannelsResultTypeDef(BaseValidatorModel):
    NextToken: str
    ContactChannels: List[ContactChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StageTypeDef(BaseValidatorModel):
    DurationInMinutes: int
    Targets: Sequence[TargetTypeDef]

class RecurrenceSettingsTypeDef(BaseValidatorModel):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: Optional[Sequence[MonthlySettingTypeDef]] = None
    WeeklySettings: Optional[Sequence[WeeklySettingTypeDef]] = None
    DailySettings: Optional[Sequence[HandOffTimeTypeDef]] = None
    ShiftCoverages: Optional[Mapping[DayOfWeekType, Sequence[CoverageTimeTypeDef]]] = None

class ListEngagementsRequestListEngagementsPaginateTypeDef(BaseValidatorModel):
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRangeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEngagementsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncidentId: Optional[str] = None
    TimeRangeValue: Optional[TimeRangeTypeDef] = None

class ListPreviewRotationShiftsResultTypeDef(BaseValidatorModel):
    RotationShifts: List[RotationShiftTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRotationShiftsResultTypeDef(BaseValidatorModel):
    RotationShifts: List[RotationShiftTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PlanTypeDef(BaseValidatorModel):
    Stages: Optional[Sequence[StageTypeDef]] = None
    RotationIds: Optional[Sequence[str]] = None

class CreateRotationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ContactIds: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IdempotencyToken: Optional[str] = None

class GetRotationResultTypeDef(BaseValidatorModel):
    RotationArn: str
    Name: str
    ContactIds: List[str]
    StartTime: datetime
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPreviewRotationShiftsRequestListPreviewRotationShiftsPaginateTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    RotationStartTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Overrides: Optional[Sequence[PreviewOverrideTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPreviewRotationShiftsRequestRequestTypeDef(BaseValidatorModel):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsTypeDef
    RotationStartTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None
    Overrides: Optional[Sequence[PreviewOverrideTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RotationTypeDef(BaseValidatorModel):
    RotationArn: str
    Name: str
    ContactIds: Optional[List[str]] = None
    StartTime: Optional[datetime] = None
    TimeZoneId: Optional[str] = None
    Recurrence: Optional[RecurrenceSettingsTypeDef] = None

class UpdateRotationRequestRequestTypeDef(BaseValidatorModel):
    RotationId: str
    Recurrence: RecurrenceSettingsTypeDef
    ContactIds: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    TimeZoneId: Optional[str] = None

class CreateContactRequestRequestTypeDef(BaseValidatorModel):
    Alias: str
    Type: ContactTypeType
    Plan: PlanTypeDef
    DisplayName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    IdempotencyToken: Optional[str] = None

class GetContactResultTypeDef(BaseValidatorModel):
    ContactArn: str
    Alias: str
    DisplayName: str
    Type: ContactTypeType
    Plan: PlanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    DisplayName: Optional[str] = None
    Plan: Optional[PlanTypeDef] = None

class ListRotationsResultTypeDef(BaseValidatorModel):
    NextToken: str
    Rotations: List[RotationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

