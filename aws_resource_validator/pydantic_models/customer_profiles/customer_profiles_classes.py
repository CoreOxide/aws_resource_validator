from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddProfileKeyRequest(BaseValidatorModel):
    ProfileId: str
    KeyName: str
    Values: List[str]
    DomainName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AdditionalSearchKey(BaseValidatorModel):
    KeyName: str
    Values: List[str]


class ProfileDimensionOutput(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: List[str]


class Address(BaseValidatorModel):
    Address1: Optional[str] = None
    Address2: Optional[str] = None
    Address3: Optional[str] = None
    Address4: Optional[str] = None
    City: Optional[str] = None
    County: Optional[str] = None
    State: Optional[str] = None
    Province: Optional[str] = None
    Country: Optional[str] = None
    PostalCode: Optional[str] = None


class AppflowIntegrationWorkflowAttributes(BaseValidatorModel):
    SourceConnectorType: SourceConnectorTypeType
    ConnectorProfileName: str
    RoleArn: Optional[str] = None


class AppflowIntegrationWorkflowMetrics(BaseValidatorModel):
    RecordsProcessed: int
    StepsCompleted: int
    TotalSteps: int


class AppflowIntegrationWorkflowStep(BaseValidatorModel):
    FlowName: str
    Status: StatusType
    ExecutionMessage: str
    RecordsProcessed: int
    BatchRecordsStartTime: str
    BatchRecordsEndTime: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class AttributeItem(BaseValidatorModel):
    Name: str


class AttributeDimensionOutput(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]


class AttributeDimension(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]


class AttributeTypesSelectorOutput(BaseValidatorModel):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: Optional[List[str]] = None
    PhoneNumber: Optional[List[str]] = None
    EmailAddress: Optional[List[str]] = None


class AttributeTypesSelector(BaseValidatorModel):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: Optional[List[str]] = None
    PhoneNumber: Optional[List[str]] = None
    EmailAddress: Optional[List[str]] = None


class AttributeValueItem(BaseValidatorModel):
    Value: Optional[str] = None


class ConflictResolution(BaseValidatorModel):
    ConflictResolvingModel: ConflictResolvingModelType
    SourceName: Optional[str] = None


class ConsolidationOutput(BaseValidatorModel):
    MatchingAttributesList: List[List[str]]


class BatchGetCalculatedAttributeForProfileError(BaseValidatorModel):
    Code: str
    Message: str
    ProfileId: str


class CalculatedAttributeValue(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    IsDataPartial: Optional[str] = None
    ProfileId: Optional[str] = None
    Value: Optional[str] = None


class BatchGetProfileError(BaseValidatorModel):
    Code: str
    Message: str
    ProfileId: str


class BatchGetProfileRequest(BaseValidatorModel):
    DomainName: str
    ProfileIds: List[str]

Timestamp = Union[datetime, str]


class RangeOverride(BaseValidatorModel):
    Start: int
    Unit: Literal['DAYS']
    End: Optional[int] = None


class Range(BaseValidatorModel):
    Value: int
    Unit: Literal['DAYS']


class Threshold(BaseValidatorModel):
    Value: str
    Operator: OperatorType


class ConnectorOperator(BaseValidatorModel):
    Marketo: Optional[MarketoConnectorOperatorType] = None
    S3: Optional[S3ConnectorOperatorType] = None
    Salesforce: Optional[SalesforceConnectorOperatorType] = None
    ServiceNow: Optional[ServiceNowConnectorOperatorType] = None
    Zendesk: Optional[ZendeskConnectorOperatorType] = None


class Consolidation(BaseValidatorModel):
    MatchingAttributesList: List[List[str]]


class CreateEventStreamRequest(BaseValidatorModel):
    DomainName: str
    Uri: str
    EventStreamName: str
    Tags: Optional[Dict[str, str]] = None


class CreateSegmentSnapshotRequest(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    DataFormat: DataFormatType
    EncryptionKey: Optional[str] = None
    RoleArn: Optional[str] = None
    DestinationUri: Optional[str] = None


class DateDimensionOutput(BaseValidatorModel):
    DimensionType: DateDimensionTypeType
    Values: List[str]


class DateDimension(BaseValidatorModel):
    DimensionType: DateDimensionTypeType
    Values: List[str]


class DeleteCalculatedAttributeDefinitionRequest(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str


class DeleteDomainRequest(BaseValidatorModel):
    DomainName: str


class DeleteEventStreamRequest(BaseValidatorModel):
    DomainName: str
    EventStreamName: str


class DeleteEventTriggerRequest(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str


class DeleteIntegrationRequest(BaseValidatorModel):
    DomainName: str
    Uri: str


class DeleteProfileKeyRequest(BaseValidatorModel):
    ProfileId: str
    KeyName: str
    Values: List[str]
    DomainName: str


class DeleteProfileObjectRequest(BaseValidatorModel):
    ProfileId: str
    ProfileObjectUniqueKey: str
    ObjectTypeName: str
    DomainName: str


class DeleteProfileObjectTypeRequest(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str


class DeleteProfileRequest(BaseValidatorModel):
    ProfileId: str
    DomainName: str


class DeleteSegmentDefinitionRequest(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str


class DeleteWorkflowRequest(BaseValidatorModel):
    DomainName: str
    WorkflowId: str


class DestinationSummary(BaseValidatorModel):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: Optional[datetime] = None


class DetectProfileObjectTypeRequest(BaseValidatorModel):
    Objects: List[str]
    DomainName: str


class ObjectTypeField(BaseValidatorModel):
    Source: Optional[str] = None
    Target: Optional[str] = None
    ContentType: Optional[FieldContentTypeType] = None


class ObjectTypeKeyOutput(BaseValidatorModel):
    StandardIdentifiers: Optional[List[StandardIdentifierType]] = None
    FieldNames: Optional[List[str]] = None


class DomainStats(BaseValidatorModel):
    ProfileCount: Optional[int] = None
    MeteringProfileCount: Optional[int] = None
    ObjectCount: Optional[int] = None
    TotalSize: Optional[int] = None


class EventStreamDestinationDetails(BaseValidatorModel):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: Optional[datetime] = None
    Message: Optional[str] = None


class ObjectAttributeOutput(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    Values: List[str]
    Source: Optional[str] = None
    FieldName: Optional[str] = None


class Period(BaseValidatorModel):
    Unit: PeriodUnitType
    Value: int
    MaxInvocationsPerProfile: Optional[int] = None
    Unlimited: Optional[bool] = None


class EventTriggerSummaryItem(BaseValidatorModel):
    ObjectTypeName: Optional[str] = None
    EventTriggerName: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class S3ExportingConfig(BaseValidatorModel):
    S3BucketName: str
    S3KeyName: Optional[str] = None


class S3ExportingLocation(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3KeyName: Optional[str] = None


class ExtraLengthValueProfileDimensionOutput(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: List[str]


class ExtraLengthValueProfileDimension(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: List[str]


class FieldSourceProfileIds(BaseValidatorModel):
    AccountNumber: Optional[str] = None
    AdditionalInformation: Optional[str] = None
    PartyType: Optional[str] = None
    BusinessName: Optional[str] = None
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    LastName: Optional[str] = None
    BirthDate: Optional[str] = None
    Gender: Optional[str] = None
    PhoneNumber: Optional[str] = None
    MobilePhoneNumber: Optional[str] = None
    HomePhoneNumber: Optional[str] = None
    BusinessPhoneNumber: Optional[str] = None
    EmailAddress: Optional[str] = None
    PersonalEmailAddress: Optional[str] = None
    BusinessEmailAddress: Optional[str] = None
    Address: Optional[str] = None
    ShippingAddress: Optional[str] = None
    MailingAddress: Optional[str] = None
    BillingAddress: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None


class FilterAttributeDimensionOutput(BaseValidatorModel):
    DimensionType: FilterDimensionTypeType
    Values: List[str]


class FilterAttributeDimension(BaseValidatorModel):
    DimensionType: FilterDimensionTypeType
    Values: List[str]


class FoundByKeyValue(BaseValidatorModel):
    KeyName: Optional[str] = None
    Values: Optional[List[str]] = None


class GetCalculatedAttributeDefinitionRequest(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str


class GetCalculatedAttributeForProfileRequest(BaseValidatorModel):
    DomainName: str
    ProfileId: str
    CalculatedAttributeName: str


class GetDomainRequest(BaseValidatorModel):
    DomainName: str


class GetEventStreamRequest(BaseValidatorModel):
    DomainName: str
    EventStreamName: str


class GetEventTriggerRequest(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str


class GetIdentityResolutionJobRequest(BaseValidatorModel):
    DomainName: str
    JobId: str


class JobStats(BaseValidatorModel):
    NumberOfProfilesReviewed: Optional[int] = None
    NumberOfMatchesFound: Optional[int] = None
    NumberOfMergesDone: Optional[int] = None


class GetIntegrationRequest(BaseValidatorModel):
    DomainName: str
    Uri: str


class GetMatchesRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MatchItem(BaseValidatorModel):
    MatchId: Optional[str] = None
    ProfileIds: Optional[List[str]] = None
    ConfidenceScore: Optional[float] = None


class GetProfileObjectTypeRequest(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str


class GetProfileObjectTypeTemplateRequest(BaseValidatorModel):
    TemplateId: str


class GetSegmentDefinitionRequest(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str


class GetSegmentEstimateRequest(BaseValidatorModel):
    DomainName: str
    EstimateId: str


class GetSegmentMembershipRequest(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    ProfileIds: List[str]


class ProfileQueryFailures(BaseValidatorModel):
    ProfileId: str
    Message: str
    Status: Optional[int] = None


class GetSegmentSnapshotRequest(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    SnapshotId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetSimilarProfilesRequest(BaseValidatorModel):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetWorkflowRequest(BaseValidatorModel):
    DomainName: str
    WorkflowId: str


class GetWorkflowStepsRequest(BaseValidatorModel):
    DomainName: str
    WorkflowId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SourceSegment(BaseValidatorModel):
    SegmentDefinitionName: Optional[str] = None


class IncrementalPullConfig(BaseValidatorModel):
    DatetimeTypeFieldName: Optional[str] = None


class JobSchedule(BaseValidatorModel):
    DayOfTheWeek: JobScheduleDayOfTheWeekType
    Time: str


class ListAccountIntegrationsRequest(BaseValidatorModel):
    Uri: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeHidden: Optional[bool] = None


class ListIntegrationItem(BaseValidatorModel):
    DomainName: str
    Uri: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ObjectTypeName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    ObjectTypeNames: Optional[Dict[str, str]] = None
    WorkflowId: Optional[str] = None
    IsUnstructured: Optional[bool] = None
    RoleArn: Optional[str] = None
    EventTriggerNames: Optional[List[str]] = None


class ListCalculatedAttributeDefinitionItem(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class ListCalculatedAttributeDefinitionsRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCalculatedAttributeForProfileItem(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    IsDataPartial: Optional[str] = None
    Value: Optional[str] = None


class ListCalculatedAttributesForProfileRequest(BaseValidatorModel):
    DomainName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDomainItem(BaseValidatorModel):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Optional[Dict[str, str]] = None


class ListDomainsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventStreamsRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventTriggersRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIdentityResolutionJobsRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIntegrationsRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeHidden: Optional[bool] = None


class ListObjectTypeAttributeItem(BaseValidatorModel):
    AttributeName: str
    LastUpdatedAt: datetime


class ListObjectTypeAttributesRequest(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileObjectTypeItem(BaseValidatorModel):
    ObjectTypeName: str
    Description: str
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    MaxProfileObjectCount: Optional[int] = None
    MaxAvailableProfileObjectCount: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None


class ListProfileObjectTypeTemplateItem(BaseValidatorModel):
    TemplateId: Optional[str] = None
    SourceName: Optional[str] = None
    SourceObject: Optional[str] = None


class ListProfileObjectTypeTemplatesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileObjectTypesRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileObjectsItem(BaseValidatorModel):
    ObjectTypeName: Optional[str] = None
    ProfileObjectUniqueKey: Optional[str] = None
    Object: Optional[str] = None


class ObjectFilter(BaseValidatorModel):
    KeyName: str
    Values: List[str]


class ListRuleBasedMatchesRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSegmentDefinitionsRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SegmentDefinitionItem(BaseValidatorModel):
    SegmentDefinitionName: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    SegmentDefinitionArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListWorkflowsItem(BaseValidatorModel):
    WorkflowType: Literal['APPFLOW_INTEGRATION']
    WorkflowId: str
    Status: StatusType
    StatusDescription: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class MarketoSourceProperties(BaseValidatorModel):
    Object: str


class MatchingRuleOutput(BaseValidatorModel):
    Rule: List[str]


class MatchingRule(BaseValidatorModel):
    Rule: List[str]


class ObjectAttribute(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    Values: List[str]
    Source: Optional[str] = None
    FieldName: Optional[str] = None


class ObjectTypeKey(BaseValidatorModel):
    StandardIdentifiers: Optional[List[StandardIdentifierType]] = None
    FieldNames: Optional[List[str]] = None


class ProfileAttributeValuesRequest(BaseValidatorModel):
    DomainName: str
    AttributeName: str


class ProfileDimension(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: List[str]


class PutProfileObjectRequest(BaseValidatorModel):
    ObjectTypeName: str
    Object: str
    DomainName: str


class S3SourceProperties(BaseValidatorModel):
    BucketName: str
    BucketPrefix: Optional[str] = None


class SalesforceSourceProperties(BaseValidatorModel):
    Object: str
    EnableDynamicFieldUpdate: Optional[bool] = None
    IncludeDeletedRecords: Optional[bool] = None


class ServiceNowSourceProperties(BaseValidatorModel):
    Object: str


class ZendeskSourceProperties(BaseValidatorModel):
    Object: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateAddress(BaseValidatorModel):
    Address1: Optional[str] = None
    Address2: Optional[str] = None
    Address3: Optional[str] = None
    Address4: Optional[str] = None
    City: Optional[str] = None
    County: Optional[str] = None
    State: Optional[str] = None
    Province: Optional[str] = None
    Country: Optional[str] = None
    PostalCode: Optional[str] = None


class AddProfileKeyResponse(BaseValidatorModel):
    KeyName: str
    Values: List[str]
    ResponseMetadata: ResponseMetadata


class CreateEventStreamResponse(BaseValidatorModel):
    EventStreamArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateIntegrationWorkflowResponse(BaseValidatorModel):
    WorkflowId: str
    Message: str
    ResponseMetadata: ResponseMetadata


class CreateProfileResponse(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadata


class CreateSegmentDefinitionResponse(BaseValidatorModel):
    SegmentDefinitionName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    SegmentDefinitionArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateSegmentEstimateResponse(BaseValidatorModel):
    DomainName: str
    EstimateId: str
    StatusCode: int
    ResponseMetadata: ResponseMetadata


class CreateSegmentSnapshotResponse(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


class DeleteDomainResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class DeleteEventTriggerResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class DeleteIntegrationResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class DeleteProfileKeyResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class DeleteProfileObjectResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class DeleteProfileObjectTypeResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class DeleteProfileResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class DeleteSegmentDefinitionResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class GetAutoMergingPreviewResponse(BaseValidatorModel):
    DomainName: str
    NumberOfMatchesInSample: int
    NumberOfProfilesInSample: int
    NumberOfProfilesWillBeMerged: int
    ResponseMetadata: ResponseMetadata


class GetCalculatedAttributeForProfileResponse(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    IsDataPartial: str
    Value: str
    ResponseMetadata: ResponseMetadata


class GetIntegrationResponse(BaseValidatorModel):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ObjectTypeNames: Dict[str, str]
    WorkflowId: str
    IsUnstructured: bool
    RoleArn: str
    EventTriggerNames: List[str]
    ResponseMetadata: ResponseMetadata


class GetSegmentEstimateResponse(BaseValidatorModel):
    DomainName: str
    EstimateId: str
    Status: EstimateStatusType
    Estimate: str
    Message: str
    StatusCode: int
    ResponseMetadata: ResponseMetadata


class GetSegmentSnapshotResponse(BaseValidatorModel):
    SnapshotId: str
    Status: SegmentSnapshotStatusType
    StatusMessage: str
    DataFormat: DataFormatType
    EncryptionKey: str
    RoleArn: str
    DestinationUri: str
    ResponseMetadata: ResponseMetadata


class GetSimilarProfilesResponse(BaseValidatorModel):
    ProfileIds: List[str]
    MatchId: str
    MatchType: MatchTypeType
    RuleLevel: int
    ConfidenceScore: float
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRuleBasedMatchesResponse(BaseValidatorModel):
    MatchIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class MergeProfilesResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class PutIntegrationResponse(BaseValidatorModel):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ObjectTypeNames: Dict[str, str]
    WorkflowId: str
    IsUnstructured: bool
    RoleArn: str
    EventTriggerNames: List[str]
    ResponseMetadata: ResponseMetadata


class PutProfileObjectResponse(BaseValidatorModel):
    ProfileObjectUniqueKey: str
    ResponseMetadata: ResponseMetadata


class UpdateProfileResponse(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadata


class SearchProfilesRequest(BaseValidatorModel):
    DomainName: str
    KeyName: str
    Values: List[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AdditionalSearchKeys: Optional[List[AdditionalSearchKey]] = None
    LogicalOperator: Optional[LogicalOperatorType] = None


class AddressDimensionOutput(BaseValidatorModel):
    City: Optional[ProfileDimensionOutput] = None
    Country: Optional[ProfileDimensionOutput] = None
    County: Optional[ProfileDimensionOutput] = None
    PostalCode: Optional[ProfileDimensionOutput] = None
    Province: Optional[ProfileDimensionOutput] = None
    State: Optional[ProfileDimensionOutput] = None


class CreateProfileRequest(BaseValidatorModel):
    DomainName: str
    AccountNumber: Optional[str] = None
    AdditionalInformation: Optional[str] = None
    PartyType: Optional[PartyTypeType] = None
    BusinessName: Optional[str] = None
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    LastName: Optional[str] = None
    BirthDate: Optional[str] = None
    Gender: Optional[GenderType] = None
    PhoneNumber: Optional[str] = None
    MobilePhoneNumber: Optional[str] = None
    HomePhoneNumber: Optional[str] = None
    BusinessPhoneNumber: Optional[str] = None
    EmailAddress: Optional[str] = None
    PersonalEmailAddress: Optional[str] = None
    BusinessEmailAddress: Optional[str] = None
    Address: Optional[Address] = None
    ShippingAddress: Optional[Address] = None
    MailingAddress: Optional[Address] = None
    BillingAddress: Optional[Address] = None
    Attributes: Optional[Dict[str, str]] = None
    PartyTypeString: Optional[str] = None
    GenderString: Optional[str] = None


class WorkflowAttributes(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowAttributes] = None


class WorkflowMetrics(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowMetrics] = None


class WorkflowStepItem(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowStep] = None


class AttributeDetailsOutput(BaseValidatorModel):
    Attributes: List[AttributeItem]
    Expression: str


class AttributeDetails(BaseValidatorModel):
    Attributes: List[AttributeItem]
    Expression: str

AttributeDimensionUnion = Union[AttributeDimension, AttributeDimensionOutput]

AttributeTypesSelectorUnion = Union[AttributeTypesSelector, AttributeTypesSelectorOutput]


class ProfileAttributeValuesResponse(BaseValidatorModel):
    DomainName: str
    AttributeName: str
    Items: List[AttributeValueItem]
    StatusCode: int
    ResponseMetadata: ResponseMetadata


class AutoMergingOutput(BaseValidatorModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationOutput] = None
    ConflictResolution: Optional[ConflictResolution] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None


class Batch(BaseValidatorModel):
    StartTime: Timestamp
    EndTime: Timestamp


class ListWorkflowsRequest(BaseValidatorModel):
    DomainName: str
    WorkflowType: Optional[Literal['APPFLOW_INTEGRATION']] = None
    Status: Optional[StatusType] = None
    QueryStartDate: Optional[Timestamp] = None
    QueryEndDate: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ScheduledTriggerProperties(BaseValidatorModel):
    ScheduleExpression: str
    DataPullMode: Optional[DataPullModeType] = None
    ScheduleStartTime: Optional[Timestamp] = None
    ScheduleEndTime: Optional[Timestamp] = None
    Timezone: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    FirstExecutionFrom: Optional[Timestamp] = None


class ConditionOverrides(BaseValidatorModel):
    Range: Optional[RangeOverride] = None


class Conditions(BaseValidatorModel):
    Range: Optional[Range] = None
    ObjectCount: Optional[int] = None
    Threshold: Optional[Threshold] = None


class Task(BaseValidatorModel):
    SourceFields: List[str]
    TaskType: TaskTypeType
    ConnectorOperator: Optional[ConnectorOperator] = None
    DestinationField: Optional[str] = None
    TaskProperties: Optional[Dict[OperatorPropertiesKeysType, str]] = None

ConsolidationUnion = Union[Consolidation, ConsolidationOutput]

DateDimensionUnion = Union[DateDimension, DateDimensionOutput]


class EventStreamSummary(BaseValidatorModel):
    DomainName: str
    EventStreamName: str
    EventStreamArn: str
    State: EventStreamStateType
    StoppedSince: Optional[datetime] = None
    DestinationSummary: Optional[DestinationSummary] = None
    Tags: Optional[Dict[str, str]] = None


class DetectedProfileObjectType(BaseValidatorModel):
    SourceLastUpdatedTimestampFormat: Optional[str] = None
    Fields: Optional[Dict[str, ObjectTypeField]] = None
    Keys: Optional[Dict[str, List[ObjectTypeKeyOutput]]] = None


class GetProfileObjectTypeResponse(BaseValidatorModel):
    ObjectTypeName: str
    Description: str
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    MaxAvailableProfileObjectCount: int
    MaxProfileObjectCount: int
    Fields: Dict[str, ObjectTypeField]
    Keys: Dict[str, List[ObjectTypeKeyOutput]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetProfileObjectTypeTemplateResponse(BaseValidatorModel):
    TemplateId: str
    SourceName: str
    SourceObject: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    Fields: Dict[str, ObjectTypeField]
    Keys: Dict[str, List[ObjectTypeKeyOutput]]
    ResponseMetadata: ResponseMetadata


class PutProfileObjectTypeResponse(BaseValidatorModel):
    ObjectTypeName: str
    Description: str
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    MaxProfileObjectCount: int
    MaxAvailableProfileObjectCount: int
    Fields: Dict[str, ObjectTypeField]
    Keys: Dict[str, List[ObjectTypeKeyOutput]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetEventStreamResponse(BaseValidatorModel):
    DomainName: str
    EventStreamArn: str
    CreatedAt: datetime
    State: EventStreamStateType
    StoppedSince: datetime
    DestinationDetails: EventStreamDestinationDetails
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EventTriggerDimensionOutput(BaseValidatorModel):
    ObjectAttributes: List[ObjectAttributeOutput]


class EventTriggerLimitsOutput(BaseValidatorModel):
    EventExpiration: Optional[int] = None
    Periods: Optional[List[Period]] = None


class EventTriggerLimits(BaseValidatorModel):
    EventExpiration: Optional[int] = None
    Periods: Optional[List[Period]] = None


class ListEventTriggersResponse(BaseValidatorModel):
    Items: List[EventTriggerSummaryItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExportingConfig(BaseValidatorModel):
    S3Exporting: Optional[S3ExportingConfig] = None


class ExportingLocation(BaseValidatorModel):
    S3Exporting: Optional[S3ExportingLocation] = None

ExtraLengthValueProfileDimensionUnion = Union[ExtraLengthValueProfileDimension, ExtraLengthValueProfileDimensionOutput]


class MergeProfilesRequest(BaseValidatorModel):
    DomainName: str
    MainProfileId: str
    ProfileIdsToBeMerged: List[str]
    FieldSourceProfileIds: Optional[FieldSourceProfileIds] = None


class FilterDimensionOutput(BaseValidatorModel):
    Attributes: Dict[str, FilterAttributeDimensionOutput]


class FilterDimension(BaseValidatorModel):
    Attributes: Dict[str, FilterAttributeDimension]


class Profile(BaseValidatorModel):
    ProfileId: Optional[str] = None
    AccountNumber: Optional[str] = None
    AdditionalInformation: Optional[str] = None
    PartyType: Optional[PartyTypeType] = None
    BusinessName: Optional[str] = None
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    LastName: Optional[str] = None
    BirthDate: Optional[str] = None
    Gender: Optional[GenderType] = None
    PhoneNumber: Optional[str] = None
    MobilePhoneNumber: Optional[str] = None
    HomePhoneNumber: Optional[str] = None
    BusinessPhoneNumber: Optional[str] = None
    EmailAddress: Optional[str] = None
    PersonalEmailAddress: Optional[str] = None
    BusinessEmailAddress: Optional[str] = None
    Address: Optional[Address] = None
    ShippingAddress: Optional[Address] = None
    MailingAddress: Optional[Address] = None
    BillingAddress: Optional[Address] = None
    Attributes: Optional[Dict[str, str]] = None
    FoundByItems: Optional[List[FoundByKeyValue]] = None
    PartyTypeString: Optional[str] = None
    GenderString: Optional[str] = None


class GetMatchesResponse(BaseValidatorModel):
    MatchGenerationDate: datetime
    PotentialMatches: int
    Matches: List[MatchItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetSimilarProfilesRequestPaginate(BaseValidatorModel):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventStreamsRequestPaginate(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventTriggersRequestPaginate(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListObjectTypeAttributesRequestPaginate(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRuleBasedMatchesRequestPaginate(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSegmentDefinitionsRequestPaginate(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountIntegrationsResponse(BaseValidatorModel):
    Items: List[ListIntegrationItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIntegrationsResponse(BaseValidatorModel):
    Items: List[ListIntegrationItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCalculatedAttributeDefinitionsResponse(BaseValidatorModel):
    Items: List[ListCalculatedAttributeDefinitionItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCalculatedAttributesForProfileResponse(BaseValidatorModel):
    Items: List[ListCalculatedAttributeForProfileItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDomainsResponse(BaseValidatorModel):
    Items: List[ListDomainItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListObjectTypeAttributesResponse(BaseValidatorModel):
    Items: List[ListObjectTypeAttributeItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProfileObjectTypesResponse(BaseValidatorModel):
    Items: List[ListProfileObjectTypeItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProfileObjectTypeTemplatesResponse(BaseValidatorModel):
    Items: List[ListProfileObjectTypeTemplateItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProfileObjectsResponse(BaseValidatorModel):
    Items: List[ListProfileObjectsItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProfileObjectsRequest(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ObjectFilter: Optional[ObjectFilter] = None


class ListSegmentDefinitionsResponse(BaseValidatorModel):
    Items: List[SegmentDefinitionItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWorkflowsResponse(BaseValidatorModel):
    Items: List[ListWorkflowsItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

MatchingRuleUnion = Union[MatchingRule, MatchingRuleOutput]

ObjectAttributeUnion = Union[ObjectAttribute, ObjectAttributeOutput]

ObjectTypeKeyUnion = Union[ObjectTypeKey, ObjectTypeKeyOutput]

ProfileDimensionUnion = Union[ProfileDimension, ProfileDimensionOutput]


class SourceConnectorProperties(BaseValidatorModel):
    Marketo: Optional[MarketoSourceProperties] = None
    S3: Optional[S3SourceProperties] = None
    Salesforce: Optional[SalesforceSourceProperties] = None
    ServiceNow: Optional[ServiceNowSourceProperties] = None
    Zendesk: Optional[ZendeskSourceProperties] = None


class UpdateProfileRequest(BaseValidatorModel):
    DomainName: str
    ProfileId: str
    AdditionalInformation: Optional[str] = None
    AccountNumber: Optional[str] = None
    PartyType: Optional[PartyTypeType] = None
    BusinessName: Optional[str] = None
    FirstName: Optional[str] = None
    MiddleName: Optional[str] = None
    LastName: Optional[str] = None
    BirthDate: Optional[str] = None
    Gender: Optional[GenderType] = None
    PhoneNumber: Optional[str] = None
    MobilePhoneNumber: Optional[str] = None
    HomePhoneNumber: Optional[str] = None
    BusinessPhoneNumber: Optional[str] = None
    EmailAddress: Optional[str] = None
    PersonalEmailAddress: Optional[str] = None
    BusinessEmailAddress: Optional[str] = None
    Address: Optional[UpdateAddress] = None
    ShippingAddress: Optional[UpdateAddress] = None
    MailingAddress: Optional[UpdateAddress] = None
    BillingAddress: Optional[UpdateAddress] = None
    Attributes: Optional[Dict[str, str]] = None
    PartyTypeString: Optional[str] = None
    GenderString: Optional[str] = None


class ProfileAttributesOutput(BaseValidatorModel):
    AccountNumber: Optional[ProfileDimensionOutput] = None
    AdditionalInformation: Optional[ExtraLengthValueProfileDimensionOutput] = None
    FirstName: Optional[ProfileDimensionOutput] = None
    LastName: Optional[ProfileDimensionOutput] = None
    MiddleName: Optional[ProfileDimensionOutput] = None
    GenderString: Optional[ProfileDimensionOutput] = None
    PartyTypeString: Optional[ProfileDimensionOutput] = None
    BirthDate: Optional[DateDimensionOutput] = None
    PhoneNumber: Optional[ProfileDimensionOutput] = None
    BusinessName: Optional[ProfileDimensionOutput] = None
    BusinessPhoneNumber: Optional[ProfileDimensionOutput] = None
    HomePhoneNumber: Optional[ProfileDimensionOutput] = None
    MobilePhoneNumber: Optional[ProfileDimensionOutput] = None
    EmailAddress: Optional[ProfileDimensionOutput] = None
    PersonalEmailAddress: Optional[ProfileDimensionOutput] = None
    BusinessEmailAddress: Optional[ProfileDimensionOutput] = None
    Address: Optional[AddressDimensionOutput] = None
    ShippingAddress: Optional[AddressDimensionOutput] = None
    MailingAddress: Optional[AddressDimensionOutput] = None
    BillingAddress: Optional[AddressDimensionOutput] = None
    Attributes: Optional[Dict[str, AttributeDimensionOutput]] = None


class GetWorkflowResponse(BaseValidatorModel):
    WorkflowId: str
    WorkflowType: Literal['APPFLOW_INTEGRATION']
    Status: StatusType
    ErrorDescription: str
    StartDate: datetime
    LastUpdatedAt: datetime
    Attributes: WorkflowAttributes
    Metrics: WorkflowMetrics
    ResponseMetadata: ResponseMetadata


class GetWorkflowStepsResponse(BaseValidatorModel):
    WorkflowId: str
    WorkflowType: Literal['APPFLOW_INTEGRATION']
    Items: List[WorkflowStepItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

AttributeDetailsUnion = Union[AttributeDetails, AttributeDetailsOutput]


class TriggerProperties(BaseValidatorModel):
    Scheduled: Optional[ScheduledTriggerProperties] = None


class BatchGetCalculatedAttributeForProfileRequest(BaseValidatorModel):
    CalculatedAttributeName: str
    DomainName: str
    ProfileIds: List[str]
    ConditionOverrides: Optional[ConditionOverrides] = None


class BatchGetCalculatedAttributeForProfileResponse(BaseValidatorModel):
    Errors: List[BatchGetCalculatedAttributeForProfileError]
    CalculatedAttributeValues: List[CalculatedAttributeValue]
    ConditionOverrides: ConditionOverrides
    ResponseMetadata: ResponseMetadata


class CalculatedAttributeDimensionOutput(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]
    ConditionOverrides: Optional[ConditionOverrides] = None


class CalculatedAttributeDimension(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]
    ConditionOverrides: Optional[ConditionOverrides] = None


class UpdateCalculatedAttributeDefinitionRequest(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Conditions: Optional[Conditions] = None


class UpdateCalculatedAttributeDefinitionResponse(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Statistic: StatisticType
    Conditions: Conditions
    AttributeDetails: AttributeDetailsOutput
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class AutoMerging(BaseValidatorModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationUnion] = None
    ConflictResolution: Optional[ConflictResolution] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None


class GetAutoMergingPreviewRequest(BaseValidatorModel):
    DomainName: str
    Consolidation: ConsolidationUnion
    ConflictResolution: ConflictResolution
    MinAllowedConfidenceScoreForMerging: Optional[float] = None


class ListEventStreamsResponse(BaseValidatorModel):
    Items: List[EventStreamSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DetectProfileObjectTypeResponse(BaseValidatorModel):
    DetectedProfileObjectTypes: List[DetectedProfileObjectType]
    ResponseMetadata: ResponseMetadata


class EventTriggerConditionOutput(BaseValidatorModel):
    EventTriggerDimensions: List[EventTriggerDimensionOutput]
    LogicalOperator: EventTriggerLogicalOperatorType

EventTriggerLimitsUnion = Union[EventTriggerLimits, EventTriggerLimitsOutput]


class MatchingResponse(BaseValidatorModel):
    Enabled: Optional[bool] = None
    JobSchedule: Optional[JobSchedule] = None
    AutoMerging: Optional[AutoMergingOutput] = None
    ExportingConfig: Optional[ExportingConfig] = None


class RuleBasedMatchingResponse(BaseValidatorModel):
    Enabled: Optional[bool] = None
    MatchingRules: Optional[List[MatchingRuleOutput]] = None
    Status: Optional[RuleBasedMatchingStatusType] = None
    MaxAllowedRuleLevelForMerging: Optional[int] = None
    MaxAllowedRuleLevelForMatching: Optional[int] = None
    AttributeTypesSelector: Optional[AttributeTypesSelectorOutput] = None
    ConflictResolution: Optional[ConflictResolution] = None
    ExportingConfig: Optional[ExportingConfig] = None


class GetIdentityResolutionJobResponse(BaseValidatorModel):
    DomainName: str
    JobId: str
    Status: IdentityResolutionJobStatusType
    Message: str
    JobStartTime: datetime
    JobEndTime: datetime
    LastUpdatedAt: datetime
    JobExpirationTime: datetime
    AutoMerging: AutoMergingOutput
    ExportingLocation: ExportingLocation
    JobStats: JobStats
    ResponseMetadata: ResponseMetadata


class IdentityResolutionJob(BaseValidatorModel):
    DomainName: Optional[str] = None
    JobId: Optional[str] = None
    Status: Optional[IdentityResolutionJobStatusType] = None
    JobStartTime: Optional[datetime] = None
    JobEndTime: Optional[datetime] = None
    JobStats: Optional[JobStats] = None
    ExportingLocation: Optional[ExportingLocation] = None
    Message: Optional[str] = None


class FilterGroupOutput(BaseValidatorModel):
    Type: TypeType
    Dimensions: List[FilterDimensionOutput]


class FilterGroup(BaseValidatorModel):
    Type: TypeType
    Dimensions: List[FilterDimension]


class BatchGetProfileResponse(BaseValidatorModel):
    Errors: List[BatchGetProfileError]
    Profiles: List[Profile]
    ResponseMetadata: ResponseMetadata


class ProfileQueryResult(BaseValidatorModel):
    ProfileId: str
    QueryResult: QueryResultType
    Profile: Optional[Profile] = None


class SearchProfilesResponse(BaseValidatorModel):
    Items: List[Profile]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RuleBasedMatchingRequest(BaseValidatorModel):
    Enabled: bool
    MatchingRules: Optional[List[MatchingRuleUnion]] = None
    MaxAllowedRuleLevelForMerging: Optional[int] = None
    MaxAllowedRuleLevelForMatching: Optional[int] = None
    AttributeTypesSelector: Optional[AttributeTypesSelectorUnion] = None
    ConflictResolution: Optional[ConflictResolution] = None
    ExportingConfig: Optional[ExportingConfig] = None


class EventTriggerDimension(BaseValidatorModel):
    ObjectAttributes: List[ObjectAttributeUnion]


class PutProfileObjectTypeRequest(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    Description: str
    TemplateId: Optional[str] = None
    ExpirationDays: Optional[int] = None
    EncryptionKey: Optional[str] = None
    AllowProfileCreation: Optional[bool] = None
    SourceLastUpdatedTimestampFormat: Optional[str] = None
    MaxProfileObjectCount: Optional[int] = None
    Fields: Optional[Dict[str, ObjectTypeField]] = None
    Keys: Optional[Dict[str, List[ObjectTypeKeyUnion]]] = None
    Tags: Optional[Dict[str, str]] = None


class AddressDimension(BaseValidatorModel):
    City: Optional[ProfileDimensionUnion] = None
    Country: Optional[ProfileDimensionUnion] = None
    County: Optional[ProfileDimensionUnion] = None
    PostalCode: Optional[ProfileDimensionUnion] = None
    Province: Optional[ProfileDimensionUnion] = None
    State: Optional[ProfileDimensionUnion] = None


class SourceFlowConfig(BaseValidatorModel):
    ConnectorType: SourceConnectorTypeType
    SourceConnectorProperties: SourceConnectorProperties
    ConnectorProfileName: Optional[str] = None
    IncrementalPullConfig: Optional[IncrementalPullConfig] = None


class TriggerConfig(BaseValidatorModel):
    TriggerType: TriggerTypeType
    TriggerProperties: Optional[TriggerProperties] = None


class DimensionOutput(BaseValidatorModel):
    ProfileAttributes: Optional[ProfileAttributesOutput] = None
    CalculatedAttributes: Optional[Dict[str, CalculatedAttributeDimensionOutput]] = None

CalculatedAttributeDimensionUnion = Union[CalculatedAttributeDimension, CalculatedAttributeDimensionOutput]

AutoMergingUnion = Union[AutoMerging, AutoMergingOutput]


class CreateEventTriggerResponse(BaseValidatorModel):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutput]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutput
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetEventTriggerResponse(BaseValidatorModel):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutput]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutput
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateEventTriggerResponse(BaseValidatorModel):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutput]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutput
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateDomainResponse(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: MatchingResponse
    RuleBasedMatching: RuleBasedMatchingResponse
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetDomainResponse(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Stats: DomainStats
    Matching: MatchingResponse
    RuleBasedMatching: RuleBasedMatchingResponse
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateDomainResponse(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: MatchingResponse
    RuleBasedMatching: RuleBasedMatchingResponse
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListIdentityResolutionJobsResponse(BaseValidatorModel):
    IdentityResolutionJobsList: List[IdentityResolutionJob]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FilterOutput(BaseValidatorModel):
    Include: IncludeType
    Groups: List[FilterGroupOutput]


class Filter(BaseValidatorModel):
    Include: IncludeType
    Groups: List[FilterGroup]


class GetSegmentMembershipResponse(BaseValidatorModel):
    SegmentDefinitionName: str
    Profiles: List[ProfileQueryResult]
    Failures: List[ProfileQueryFailures]
    ResponseMetadata: ResponseMetadata

EventTriggerDimensionUnion = Union[EventTriggerDimension, EventTriggerDimensionOutput]

AddressDimensionUnion = Union[AddressDimension, AddressDimensionOutput]


class FlowDefinition(BaseValidatorModel):
    FlowName: str
    KmsArn: str
    SourceFlowConfig: SourceFlowConfig
    Tasks: List[Task]
    TriggerConfig: TriggerConfig
    Description: Optional[str] = None


class GroupOutput(BaseValidatorModel):
    Dimensions: Optional[List[DimensionOutput]] = None
    SourceSegments: Optional[List[SourceSegment]] = None
    SourceType: Optional[IncludeOptionsType] = None
    Type: Optional[IncludeOptionsType] = None


class MatchingRequest(BaseValidatorModel):
    Enabled: bool
    JobSchedule: Optional[JobSchedule] = None
    AutoMerging: Optional[AutoMergingUnion] = None
    ExportingConfig: Optional[ExportingConfig] = None


class CreateCalculatedAttributeDefinitionResponse(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    AttributeDetails: AttributeDetailsOutput
    Conditions: Conditions
    Filter: FilterOutput
    Statistic: StatisticType
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetCalculatedAttributeDefinitionResponse(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Statistic: StatisticType
    Filter: FilterOutput
    Conditions: Conditions
    AttributeDetails: AttributeDetailsOutput
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

FilterUnion = Union[Filter, FilterOutput]


class EventTriggerCondition(BaseValidatorModel):
    EventTriggerDimensions: List[EventTriggerDimensionUnion]
    LogicalOperator: EventTriggerLogicalOperatorType


class ProfileAttributes(BaseValidatorModel):
    AccountNumber: Optional[ProfileDimensionUnion] = None
    AdditionalInformation: Optional[ExtraLengthValueProfileDimensionUnion] = None
    FirstName: Optional[ProfileDimensionUnion] = None
    LastName: Optional[ProfileDimensionUnion] = None
    MiddleName: Optional[ProfileDimensionUnion] = None
    GenderString: Optional[ProfileDimensionUnion] = None
    PartyTypeString: Optional[ProfileDimensionUnion] = None
    BirthDate: Optional[DateDimensionUnion] = None
    PhoneNumber: Optional[ProfileDimensionUnion] = None
    BusinessName: Optional[ProfileDimensionUnion] = None
    BusinessPhoneNumber: Optional[ProfileDimensionUnion] = None
    HomePhoneNumber: Optional[ProfileDimensionUnion] = None
    MobilePhoneNumber: Optional[ProfileDimensionUnion] = None
    EmailAddress: Optional[ProfileDimensionUnion] = None
    PersonalEmailAddress: Optional[ProfileDimensionUnion] = None
    BusinessEmailAddress: Optional[ProfileDimensionUnion] = None
    Address: Optional[AddressDimensionUnion] = None
    ShippingAddress: Optional[AddressDimensionUnion] = None
    MailingAddress: Optional[AddressDimensionUnion] = None
    BillingAddress: Optional[AddressDimensionUnion] = None
    Attributes: Optional[Dict[str, AttributeDimensionUnion]] = None


class AppflowIntegration(BaseValidatorModel):
    FlowDefinition: FlowDefinition
    Batches: Optional[List[Batch]] = None


class PutIntegrationRequest(BaseValidatorModel):
    DomainName: str
    Uri: Optional[str] = None
    ObjectTypeName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    FlowDefinition: Optional[FlowDefinition] = None
    ObjectTypeNames: Optional[Dict[str, str]] = None
    RoleArn: Optional[str] = None
    EventTriggerNames: Optional[List[str]] = None


class SegmentGroupOutput(BaseValidatorModel):
    Groups: Optional[List[GroupOutput]] = None
    Include: Optional[IncludeOptionsType] = None


class CreateDomainRequest(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequest] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequest] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateDomainRequest(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: Optional[int] = None
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequest] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequest] = None
    Tags: Optional[Dict[str, str]] = None


class CreateCalculatedAttributeDefinitionRequest(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str
    AttributeDetails: AttributeDetailsUnion
    Statistic: StatisticType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Conditions: Optional[Conditions] = None
    Filter: Optional[FilterUnion] = None
    Tags: Optional[Dict[str, str]] = None

EventTriggerConditionUnion = Union[EventTriggerCondition, EventTriggerConditionOutput]

ProfileAttributesUnion = Union[ProfileAttributes, ProfileAttributesOutput]


class IntegrationConfig(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegration] = None


class GetSegmentDefinitionResponse(BaseValidatorModel):
    SegmentDefinitionName: str
    DisplayName: str
    Description: str
    SegmentGroups: SegmentGroupOutput
    SegmentDefinitionArn: str
    CreatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateEventTriggerRequest(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str
    ObjectTypeName: str
    EventTriggerConditions: List[EventTriggerConditionUnion]
    Description: Optional[str] = None
    SegmentFilter: Optional[str] = None
    EventTriggerLimits: Optional[EventTriggerLimitsUnion] = None
    Tags: Optional[Dict[str, str]] = None


class UpdateEventTriggerRequest(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str
    ObjectTypeName: Optional[str] = None
    Description: Optional[str] = None
    EventTriggerConditions: Optional[List[EventTriggerConditionUnion]] = None
    SegmentFilter: Optional[str] = None
    EventTriggerLimits: Optional[EventTriggerLimitsUnion] = None


class Dimension(BaseValidatorModel):
    ProfileAttributes: Optional[ProfileAttributesUnion] = None
    CalculatedAttributes: Optional[Dict[str, CalculatedAttributeDimensionUnion]] = None


class CreateIntegrationWorkflowRequest(BaseValidatorModel):
    DomainName: str
    WorkflowType: Literal['APPFLOW_INTEGRATION']
    IntegrationConfig: IntegrationConfig
    ObjectTypeName: str
    RoleArn: str
    Tags: Optional[Dict[str, str]] = None

DimensionUnion = Union[Dimension, DimensionOutput]


class Group(BaseValidatorModel):
    Dimensions: Optional[List[DimensionUnion]] = None
    SourceSegments: Optional[List[SourceSegment]] = None
    SourceType: Optional[IncludeOptionsType] = None
    Type: Optional[IncludeOptionsType] = None

GroupUnion = Union[Group, GroupOutput]


class SegmentGroup(BaseValidatorModel):
    Groups: Optional[List[Group]] = None
    Include: Optional[IncludeOptionsType] = None


class SegmentGroupStructure(BaseValidatorModel):
    Groups: Optional[List[GroupUnion]] = None
    Include: Optional[IncludeOptionsType] = None

SegmentGroupUnion = Union[SegmentGroup, SegmentGroupOutput]


class CreateSegmentEstimateRequest(BaseValidatorModel):
    DomainName: str
    SegmentQuery: SegmentGroupStructure


class CreateSegmentDefinitionRequest(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    DisplayName: str
    SegmentGroups: SegmentGroupUnion
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None