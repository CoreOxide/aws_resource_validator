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
from aws_resource_validator.pydantic_models.customer_profiles_constants import *

class AddProfileKeyRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    KeyName: str
    Values: Sequence[str]
    DomainName: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AdditionalSearchKeyTypeDef(BaseValidatorModel):
    KeyName: str
    Values: Sequence[str]


class ProfileDimensionOutputTypeDef(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: List[str]


class AddressTypeDef(BaseValidatorModel):
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


class AppflowIntegrationWorkflowAttributesTypeDef(BaseValidatorModel):
    SourceConnectorType: SourceConnectorTypeType
    ConnectorProfileName: str
    RoleArn: Optional[str] = None


class AppflowIntegrationWorkflowMetricsTypeDef(BaseValidatorModel):
    RecordsProcessed: int
    StepsCompleted: int
    TotalSteps: int


class AppflowIntegrationWorkflowStepTypeDef(BaseValidatorModel):
    FlowName: str
    Status: StatusType
    ExecutionMessage: str
    RecordsProcessed: int
    BatchRecordsStartTime: str
    BatchRecordsEndTime: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class AttributeItemTypeDef(BaseValidatorModel):
    Name: str


class AttributeDimensionOutputTypeDef(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]


class AttributeDimensionTypeDef(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: Sequence[str]


class AttributeTypesSelectorOutputTypeDef(BaseValidatorModel):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: Optional[List[str]] = None
    PhoneNumber: Optional[List[str]] = None
    EmailAddress: Optional[List[str]] = None


class AttributeTypesSelectorTypeDef(BaseValidatorModel):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: Optional[Sequence[str]] = None
    PhoneNumber: Optional[Sequence[str]] = None
    EmailAddress: Optional[Sequence[str]] = None


class AttributeValueItemTypeDef(BaseValidatorModel):
    Value: Optional[str] = None


class ConflictResolutionTypeDef(BaseValidatorModel):
    ConflictResolvingModel: ConflictResolvingModelType
    SourceName: Optional[str] = None


class ConsolidationOutputTypeDef(BaseValidatorModel):
    MatchingAttributesList: List[List[str]]


class BatchGetCalculatedAttributeForProfileErrorTypeDef(BaseValidatorModel):
    Code: str
    Message: str
    ProfileId: str


class CalculatedAttributeValueTypeDef(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    IsDataPartial: Optional[str] = None
    ProfileId: Optional[str] = None
    Value: Optional[str] = None


class BatchGetProfileErrorTypeDef(BaseValidatorModel):
    Code: str
    Message: str
    ProfileId: str


class BatchGetProfileRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ProfileIds: Sequence[str]


class RangeOverrideTypeDef(BaseValidatorModel):
    Start: int
    Unit: Literal["DAYS"]
    End: Optional[int] = None


class RangeTypeDef(BaseValidatorModel):
    Value: int
    Unit: Literal["DAYS"]


class ThresholdTypeDef(BaseValidatorModel):
    Value: str
    Operator: OperatorType


class ConnectorOperatorTypeDef(BaseValidatorModel):
    Marketo: Optional[MarketoConnectorOperatorType] = None
    S3: Optional[S3ConnectorOperatorType] = None
    Salesforce: Optional[SalesforceConnectorOperatorType] = None
    ServiceNow: Optional[ServiceNowConnectorOperatorType] = None
    Zendesk: Optional[ZendeskConnectorOperatorType] = None


class ConsolidationTypeDef(BaseValidatorModel):
    MatchingAttributesList: Sequence[Sequence[str]]


class CreateEventStreamRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: str
    EventStreamName: str
    Tags: Optional[Mapping[str, str]] = None


class CreateSegmentSnapshotRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    DataFormat: DataFormatType
    EncryptionKey: Optional[str] = None
    RoleArn: Optional[str] = None
    DestinationUri: Optional[str] = None


class DateDimensionOutputTypeDef(BaseValidatorModel):
    DimensionType: DateDimensionTypeType
    Values: List[str]


class DateDimensionTypeDef(BaseValidatorModel):
    DimensionType: DateDimensionTypeType
    Values: Sequence[str]


class DeleteCalculatedAttributeDefinitionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str


class DeleteDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DeleteEventStreamRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventStreamName: str


class DeleteEventTriggerRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str


class DeleteIntegrationRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: str


class DeleteProfileKeyRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    KeyName: str
    Values: Sequence[str]
    DomainName: str


class DeleteProfileObjectRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    ProfileObjectUniqueKey: str
    ObjectTypeName: str
    DomainName: str


class DeleteProfileObjectTypeRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str


class DeleteProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    DomainName: str


class DeleteSegmentDefinitionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str


class DeleteWorkflowRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowId: str


class DestinationSummaryTypeDef(BaseValidatorModel):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: Optional[datetime] = None


class DetectProfileObjectTypeRequestTypeDef(BaseValidatorModel):
    Objects: Sequence[str]
    DomainName: str


class ObjectTypeFieldTypeDef(BaseValidatorModel):
    Source: Optional[str] = None
    Target: Optional[str] = None
    ContentType: Optional[FieldContentTypeType] = None


class ObjectTypeKeyOutputTypeDef(BaseValidatorModel):
    StandardIdentifiers: Optional[List[StandardIdentifierType]] = None
    FieldNames: Optional[List[str]] = None


class DomainStatsTypeDef(BaseValidatorModel):
    ProfileCount: Optional[int] = None
    MeteringProfileCount: Optional[int] = None
    ObjectCount: Optional[int] = None
    TotalSize: Optional[int] = None


class EventStreamDestinationDetailsTypeDef(BaseValidatorModel):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: Optional[datetime] = None
    Message: Optional[str] = None


class ObjectAttributeOutputTypeDef(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    Values: List[str]
    Source: Optional[str] = None
    FieldName: Optional[str] = None


class PeriodTypeDef(BaseValidatorModel):
    Unit: PeriodUnitType
    Value: int
    MaxInvocationsPerProfile: Optional[int] = None
    Unlimited: Optional[bool] = None


class EventTriggerSummaryItemTypeDef(BaseValidatorModel):
    ObjectTypeName: Optional[str] = None
    EventTriggerName: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class S3ExportingConfigTypeDef(BaseValidatorModel):
    S3BucketName: str
    S3KeyName: Optional[str] = None


class S3ExportingLocationTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3KeyName: Optional[str] = None


class ExtraLengthValueProfileDimensionOutputTypeDef(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: List[str]


class ExtraLengthValueProfileDimensionTypeDef(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: Sequence[str]


class FieldSourceProfileIdsTypeDef(BaseValidatorModel):
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
    Attributes: Optional[Mapping[str, str]] = None


class FilterAttributeDimensionOutputTypeDef(BaseValidatorModel):
    DimensionType: FilterDimensionTypeType
    Values: List[str]


class FilterAttributeDimensionTypeDef(BaseValidatorModel):
    DimensionType: FilterDimensionTypeType
    Values: Sequence[str]


class FoundByKeyValueTypeDef(BaseValidatorModel):
    KeyName: Optional[str] = None
    Values: Optional[List[str]] = None


class GetCalculatedAttributeDefinitionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str


class GetCalculatedAttributeForProfileRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ProfileId: str
    CalculatedAttributeName: str


class GetDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str


class GetEventStreamRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventStreamName: str


class GetEventTriggerRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str


class GetIdentityResolutionJobRequestTypeDef(BaseValidatorModel):
    DomainName: str
    JobId: str


class JobStatsTypeDef(BaseValidatorModel):
    NumberOfProfilesReviewed: Optional[int] = None
    NumberOfMatchesFound: Optional[int] = None
    NumberOfMergesDone: Optional[int] = None


class GetIntegrationRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: str


class GetMatchesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MatchItemTypeDef(BaseValidatorModel):
    MatchId: Optional[str] = None
    ProfileIds: Optional[List[str]] = None
    ConfidenceScore: Optional[float] = None


class GetProfileObjectTypeRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str


class GetProfileObjectTypeTemplateRequestTypeDef(BaseValidatorModel):
    TemplateId: str


class GetSegmentDefinitionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str


class GetSegmentEstimateRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EstimateId: str


class GetSegmentMembershipRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    ProfileIds: Sequence[str]


class ProfileQueryFailuresTypeDef(BaseValidatorModel):
    ProfileId: str
    Message: str
    Status: Optional[int] = None


class GetSegmentSnapshotRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    SnapshotId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetSimilarProfilesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetWorkflowRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowId: str


class GetWorkflowStepsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SourceSegmentTypeDef(BaseValidatorModel):
    SegmentDefinitionName: Optional[str] = None


class IncrementalPullConfigTypeDef(BaseValidatorModel):
    DatetimeTypeFieldName: Optional[str] = None


class JobScheduleTypeDef(BaseValidatorModel):
    DayOfTheWeek: JobScheduleDayOfTheWeekType
    Time: str


class ListAccountIntegrationsRequestTypeDef(BaseValidatorModel):
    Uri: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeHidden: Optional[bool] = None


class ListIntegrationItemTypeDef(BaseValidatorModel):
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


class ListCalculatedAttributeDefinitionItemTypeDef(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class ListCalculatedAttributeDefinitionsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCalculatedAttributeForProfileItemTypeDef(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    IsDataPartial: Optional[str] = None
    Value: Optional[str] = None


class ListCalculatedAttributesForProfileRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDomainItemTypeDef(BaseValidatorModel):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Optional[Dict[str, str]] = None


class ListDomainsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventStreamsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventTriggersRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIdentityResolutionJobsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIntegrationsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeHidden: Optional[bool] = None


class ListObjectTypeAttributeItemTypeDef(BaseValidatorModel):
    AttributeName: str
    LastUpdatedAt: datetime


class ListObjectTypeAttributesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileObjectTypeItemTypeDef(BaseValidatorModel):
    ObjectTypeName: str
    Description: str
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    MaxProfileObjectCount: Optional[int] = None
    MaxAvailableProfileObjectCount: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None


class ListProfileObjectTypeTemplateItemTypeDef(BaseValidatorModel):
    TemplateId: Optional[str] = None
    SourceName: Optional[str] = None
    SourceObject: Optional[str] = None


class ListProfileObjectTypeTemplatesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileObjectTypesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListProfileObjectsItemTypeDef(BaseValidatorModel):
    ObjectTypeName: Optional[str] = None
    ProfileObjectUniqueKey: Optional[str] = None
    Object: Optional[str] = None


class ObjectFilterTypeDef(BaseValidatorModel):
    KeyName: str
    Values: Sequence[str]


class ListRuleBasedMatchesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSegmentDefinitionsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SegmentDefinitionItemTypeDef(BaseValidatorModel):
    SegmentDefinitionName: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    SegmentDefinitionArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListWorkflowsItemTypeDef(BaseValidatorModel):
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    WorkflowId: str
    Status: StatusType
    StatusDescription: str
    CreatedAt: datetime
    LastUpdatedAt: datetime


class MarketoSourcePropertiesTypeDef(BaseValidatorModel):
    Object: str


class MatchingRuleOutputTypeDef(BaseValidatorModel):
    Rule: List[str]


class MatchingRuleTypeDef(BaseValidatorModel):
    Rule: Sequence[str]


class ObjectAttributeTypeDef(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    Values: Sequence[str]
    Source: Optional[str] = None
    FieldName: Optional[str] = None


class ObjectTypeKeyTypeDef(BaseValidatorModel):
    StandardIdentifiers: Optional[Sequence[StandardIdentifierType]] = None
    FieldNames: Optional[Sequence[str]] = None


class ProfileAttributeValuesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    AttributeName: str


class ProfileDimensionTypeDef(BaseValidatorModel):
    DimensionType: StringDimensionTypeType
    Values: Sequence[str]


class PutProfileObjectRequestTypeDef(BaseValidatorModel):
    ObjectTypeName: str
    Object: str
    DomainName: str


class S3SourcePropertiesTypeDef(BaseValidatorModel):
    BucketName: str
    BucketPrefix: Optional[str] = None


class SalesforceSourcePropertiesTypeDef(BaseValidatorModel):
    Object: str
    EnableDynamicFieldUpdate: Optional[bool] = None
    IncludeDeletedRecords: Optional[bool] = None


class ServiceNowSourcePropertiesTypeDef(BaseValidatorModel):
    Object: str


class ZendeskSourcePropertiesTypeDef(BaseValidatorModel):
    Object: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAddressTypeDef(BaseValidatorModel):
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


class AddProfileKeyResponseTypeDef(BaseValidatorModel):
    KeyName: str
    Values: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEventStreamResponseTypeDef(BaseValidatorModel):
    EventStreamArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIntegrationWorkflowResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProfileResponseTypeDef(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSegmentDefinitionResponseTypeDef(BaseValidatorModel):
    SegmentDefinitionName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    SegmentDefinitionArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSegmentEstimateResponseTypeDef(BaseValidatorModel):
    DomainName: str
    EstimateId: str
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSegmentSnapshotResponseTypeDef(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDomainResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEventTriggerResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteIntegrationResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProfileKeyResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProfileObjectResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProfileObjectTypeResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteProfileResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSegmentDefinitionResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAutoMergingPreviewResponseTypeDef(BaseValidatorModel):
    DomainName: str
    NumberOfMatchesInSample: int
    NumberOfProfilesInSample: int
    NumberOfProfilesWillBeMerged: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetCalculatedAttributeForProfileResponseTypeDef(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    IsDataPartial: str
    Value: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetIntegrationResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentEstimateResponseTypeDef(BaseValidatorModel):
    DomainName: str
    EstimateId: str
    Status: EstimateStatusType
    Estimate: str
    Message: str
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentSnapshotResponseTypeDef(BaseValidatorModel):
    SnapshotId: str
    Status: SegmentSnapshotStatusType
    StatusMessage: str
    DataFormat: DataFormatType
    EncryptionKey: str
    RoleArn: str
    DestinationUri: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSimilarProfilesResponseTypeDef(BaseValidatorModel):
    ProfileIds: List[str]
    MatchId: str
    MatchType: MatchTypeType
    RuleLevel: int
    ConfidenceScore: float
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListRuleBasedMatchesResponseTypeDef(BaseValidatorModel):
    MatchIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class MergeProfilesResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutIntegrationResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class PutProfileObjectResponseTypeDef(BaseValidatorModel):
    ProfileObjectUniqueKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProfileResponseTypeDef(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchProfilesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    KeyName: str
    Values: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AdditionalSearchKeys: Optional[Sequence[AdditionalSearchKeyTypeDef]] = None
    LogicalOperator: Optional[LogicalOperatorType] = None


class AddressDimensionOutputTypeDef(BaseValidatorModel):
    City: Optional[ProfileDimensionOutputTypeDef] = None
    Country: Optional[ProfileDimensionOutputTypeDef] = None
    County: Optional[ProfileDimensionOutputTypeDef] = None
    PostalCode: Optional[ProfileDimensionOutputTypeDef] = None
    Province: Optional[ProfileDimensionOutputTypeDef] = None
    State: Optional[ProfileDimensionOutputTypeDef] = None


class CreateProfileRequestTypeDef(BaseValidatorModel):
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
    Address: Optional[AddressTypeDef] = None
    ShippingAddress: Optional[AddressTypeDef] = None
    MailingAddress: Optional[AddressTypeDef] = None
    BillingAddress: Optional[AddressTypeDef] = None
    Attributes: Optional[Mapping[str, str]] = None
    PartyTypeString: Optional[str] = None
    GenderString: Optional[str] = None


class WorkflowAttributesTypeDef(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowAttributesTypeDef] = None


class WorkflowMetricsTypeDef(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowMetricsTypeDef] = None


class WorkflowStepItemTypeDef(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowStepTypeDef] = None


class AttributeDetailsOutputTypeDef(BaseValidatorModel):
    Attributes: List[AttributeItemTypeDef]
    Expression: str


class AttributeDetailsTypeDef(BaseValidatorModel):
    Attributes: Sequence[AttributeItemTypeDef]
    Expression: str


class ProfileAttributeValuesResponseTypeDef(BaseValidatorModel):
    DomainName: str
    AttributeName: str
    Items: List[AttributeValueItemTypeDef]
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class AutoMergingOutputTypeDef(BaseValidatorModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationOutputTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class BatchTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef


class ListWorkflowsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowType: Optional[Literal["APPFLOW_INTEGRATION"]] = None
    Status: Optional[StatusType] = None
    QueryStartDate: Optional[TimestampTypeDef] = None
    QueryEndDate: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ScheduledTriggerPropertiesTypeDef(BaseValidatorModel):
    ScheduleExpression: str
    DataPullMode: Optional[DataPullModeType] = None
    ScheduleStartTime: Optional[TimestampTypeDef] = None
    ScheduleEndTime: Optional[TimestampTypeDef] = None
    Timezone: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    FirstExecutionFrom: Optional[TimestampTypeDef] = None


class ConditionOverridesTypeDef(BaseValidatorModel):
    Range: Optional[RangeOverrideTypeDef] = None


class ConditionsTypeDef(BaseValidatorModel):
    Range: Optional[RangeTypeDef] = None
    ObjectCount: Optional[int] = None
    Threshold: Optional[ThresholdTypeDef] = None


class TaskTypeDef(BaseValidatorModel):
    SourceFields: Sequence[str]
    TaskType: TaskTypeType
    ConnectorOperator: Optional[ConnectorOperatorTypeDef] = None
    DestinationField: Optional[str] = None
    TaskProperties: Optional[Mapping[OperatorPropertiesKeysType, str]] = None


class EventStreamSummaryTypeDef(BaseValidatorModel):
    DomainName: str
    EventStreamName: str
    EventStreamArn: str
    State: EventStreamStateType
    StoppedSince: Optional[datetime] = None
    DestinationSummary: Optional[DestinationSummaryTypeDef] = None
    Tags: Optional[Dict[str, str]] = None


class DetectedProfileObjectTypeTypeDef(BaseValidatorModel):
    SourceLastUpdatedTimestampFormat: Optional[str] = None
    Fields: Optional[Dict[str, ObjectTypeFieldTypeDef]] = None
    Keys: Optional[Dict[str, List[ObjectTypeKeyOutputTypeDef]]] = None


class GetProfileObjectTypeResponseTypeDef(BaseValidatorModel):
    ObjectTypeName: str
    Description: str
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    MaxAvailableProfileObjectCount: int
    MaxProfileObjectCount: int
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    Keys: Dict[str, List[ObjectTypeKeyOutputTypeDef]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetProfileObjectTypeTemplateResponseTypeDef(BaseValidatorModel):
    TemplateId: str
    SourceName: str
    SourceObject: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    Keys: Dict[str, List[ObjectTypeKeyOutputTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef


class PutProfileObjectTypeResponseTypeDef(BaseValidatorModel):
    ObjectTypeName: str
    Description: str
    TemplateId: str
    ExpirationDays: int
    EncryptionKey: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    MaxProfileObjectCount: int
    MaxAvailableProfileObjectCount: int
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    Keys: Dict[str, List[ObjectTypeKeyOutputTypeDef]]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetEventStreamResponseTypeDef(BaseValidatorModel):
    DomainName: str
    EventStreamArn: str
    CreatedAt: datetime
    State: EventStreamStateType
    StoppedSince: datetime
    DestinationDetails: EventStreamDestinationDetailsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EventTriggerDimensionOutputTypeDef(BaseValidatorModel):
    ObjectAttributes: List[ObjectAttributeOutputTypeDef]


class EventTriggerLimitsOutputTypeDef(BaseValidatorModel):
    EventExpiration: Optional[int] = None
    Periods: Optional[List[PeriodTypeDef]] = None


class EventTriggerLimitsTypeDef(BaseValidatorModel):
    EventExpiration: Optional[int] = None
    Periods: Optional[Sequence[PeriodTypeDef]] = None


class ListEventTriggersResponseTypeDef(BaseValidatorModel):
    Items: List[EventTriggerSummaryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExportingConfigTypeDef(BaseValidatorModel):
    S3Exporting: Optional[S3ExportingConfigTypeDef] = None


class ExportingLocationTypeDef(BaseValidatorModel):
    S3Exporting: Optional[S3ExportingLocationTypeDef] = None


class MergeProfilesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MainProfileId: str
    ProfileIdsToBeMerged: Sequence[str]
    FieldSourceProfileIds: Optional[FieldSourceProfileIdsTypeDef] = None


class FilterDimensionOutputTypeDef(BaseValidatorModel):
    Attributes: Dict[str, FilterAttributeDimensionOutputTypeDef]


class FilterDimensionTypeDef(BaseValidatorModel):
    Attributes: Mapping[str, FilterAttributeDimensionTypeDef]


class ProfileTypeDef(BaseValidatorModel):
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
    Address: Optional[AddressTypeDef] = None
    ShippingAddress: Optional[AddressTypeDef] = None
    MailingAddress: Optional[AddressTypeDef] = None
    BillingAddress: Optional[AddressTypeDef] = None
    Attributes: Optional[Dict[str, str]] = None
    FoundByItems: Optional[List[FoundByKeyValueTypeDef]] = None
    PartyTypeString: Optional[str] = None
    GenderString: Optional[str] = None


class GetMatchesResponseTypeDef(BaseValidatorModel):
    MatchGenerationDate: datetime
    PotentialMatches: int
    Matches: List[MatchItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetSimilarProfilesRequestPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventStreamsRequestPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventTriggersRequestPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListObjectTypeAttributesRequestPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRuleBasedMatchesRequestPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSegmentDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountIntegrationsResponseTypeDef(BaseValidatorModel):
    Items: List[ListIntegrationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIntegrationsResponseTypeDef(BaseValidatorModel):
    Items: List[ListIntegrationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCalculatedAttributeDefinitionsResponseTypeDef(BaseValidatorModel):
    Items: List[ListCalculatedAttributeDefinitionItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCalculatedAttributesForProfileResponseTypeDef(BaseValidatorModel):
    Items: List[ListCalculatedAttributeForProfileItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDomainsResponseTypeDef(BaseValidatorModel):
    Items: List[ListDomainItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListObjectTypeAttributesResponseTypeDef(BaseValidatorModel):
    Items: List[ListObjectTypeAttributeItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProfileObjectTypesResponseTypeDef(BaseValidatorModel):
    Items: List[ListProfileObjectTypeItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProfileObjectTypeTemplatesResponseTypeDef(BaseValidatorModel):
    Items: List[ListProfileObjectTypeTemplateItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProfileObjectsResponseTypeDef(BaseValidatorModel):
    Items: List[ListProfileObjectsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProfileObjectsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ObjectFilter: Optional[ObjectFilterTypeDef] = None


class ListSegmentDefinitionsResponseTypeDef(BaseValidatorModel):
    Items: List[SegmentDefinitionItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    Items: List[ListWorkflowsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SourceConnectorPropertiesTypeDef(BaseValidatorModel):
    Marketo: Optional[MarketoSourcePropertiesTypeDef] = None
    S3: Optional[S3SourcePropertiesTypeDef] = None
    Salesforce: Optional[SalesforceSourcePropertiesTypeDef] = None
    ServiceNow: Optional[ServiceNowSourcePropertiesTypeDef] = None
    Zendesk: Optional[ZendeskSourcePropertiesTypeDef] = None


class UpdateProfileRequestTypeDef(BaseValidatorModel):
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
    Address: Optional[UpdateAddressTypeDef] = None
    ShippingAddress: Optional[UpdateAddressTypeDef] = None
    MailingAddress: Optional[UpdateAddressTypeDef] = None
    BillingAddress: Optional[UpdateAddressTypeDef] = None
    Attributes: Optional[Mapping[str, str]] = None
    PartyTypeString: Optional[str] = None
    GenderString: Optional[str] = None


class ProfileAttributesOutputTypeDef(BaseValidatorModel):
    AccountNumber: Optional[ProfileDimensionOutputTypeDef] = None
    AdditionalInformation: Optional[ExtraLengthValueProfileDimensionOutputTypeDef] = None
    FirstName: Optional[ProfileDimensionOutputTypeDef] = None
    LastName: Optional[ProfileDimensionOutputTypeDef] = None
    MiddleName: Optional[ProfileDimensionOutputTypeDef] = None
    GenderString: Optional[ProfileDimensionOutputTypeDef] = None
    PartyTypeString: Optional[ProfileDimensionOutputTypeDef] = None
    BirthDate: Optional[DateDimensionOutputTypeDef] = None
    PhoneNumber: Optional[ProfileDimensionOutputTypeDef] = None
    BusinessName: Optional[ProfileDimensionOutputTypeDef] = None
    BusinessPhoneNumber: Optional[ProfileDimensionOutputTypeDef] = None
    HomePhoneNumber: Optional[ProfileDimensionOutputTypeDef] = None
    MobilePhoneNumber: Optional[ProfileDimensionOutputTypeDef] = None
    EmailAddress: Optional[ProfileDimensionOutputTypeDef] = None
    PersonalEmailAddress: Optional[ProfileDimensionOutputTypeDef] = None
    BusinessEmailAddress: Optional[ProfileDimensionOutputTypeDef] = None
    Address: Optional[AddressDimensionOutputTypeDef] = None
    ShippingAddress: Optional[AddressDimensionOutputTypeDef] = None
    MailingAddress: Optional[AddressDimensionOutputTypeDef] = None
    BillingAddress: Optional[AddressDimensionOutputTypeDef] = None
    Attributes: Optional[Dict[str, AttributeDimensionOutputTypeDef]] = None


class GetWorkflowResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    Status: StatusType
    ErrorDescription: str
    StartDate: datetime
    LastUpdatedAt: datetime
    Attributes: WorkflowAttributesTypeDef
    Metrics: WorkflowMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkflowStepsResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    Items: List[WorkflowStepItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TriggerPropertiesTypeDef(BaseValidatorModel):
    Scheduled: Optional[ScheduledTriggerPropertiesTypeDef] = None


class BatchGetCalculatedAttributeForProfileRequestTypeDef(BaseValidatorModel):
    CalculatedAttributeName: str
    DomainName: str
    ProfileIds: Sequence[str]
    ConditionOverrides: Optional[ConditionOverridesTypeDef] = None


class BatchGetCalculatedAttributeForProfileResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchGetCalculatedAttributeForProfileErrorTypeDef]
    CalculatedAttributeValues: List[CalculatedAttributeValueTypeDef]
    ConditionOverrides: ConditionOverridesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CalculatedAttributeDimensionOutputTypeDef(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: List[str]
    ConditionOverrides: Optional[ConditionOverridesTypeDef] = None


class CalculatedAttributeDimensionTypeDef(BaseValidatorModel):
    DimensionType: AttributeDimensionTypeType
    Values: Sequence[str]
    ConditionOverrides: Optional[ConditionOverridesTypeDef] = None


class UpdateCalculatedAttributeDefinitionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Conditions: Optional[ConditionsTypeDef] = None


class UpdateCalculatedAttributeDefinitionResponseTypeDef(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Statistic: StatisticType
    Conditions: ConditionsTypeDef
    AttributeDetails: AttributeDetailsOutputTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ConsolidationUnionTypeDef(BaseValidatorModel):
    pass


class AutoMergingTypeDef(BaseValidatorModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationUnionTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None


class GetAutoMergingPreviewRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Consolidation: ConsolidationUnionTypeDef
    ConflictResolution: ConflictResolutionTypeDef
    MinAllowedConfidenceScoreForMerging: Optional[float] = None


class ListEventStreamsResponseTypeDef(BaseValidatorModel):
    Items: List[EventStreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DetectProfileObjectTypeResponseTypeDef(BaseValidatorModel):
    DetectedProfileObjectTypes: List[DetectedProfileObjectTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EventTriggerConditionOutputTypeDef(BaseValidatorModel):
    EventTriggerDimensions: List[EventTriggerDimensionOutputTypeDef]
    LogicalOperator: EventTriggerLogicalOperatorType


class MatchingResponseTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    JobSchedule: Optional[JobScheduleTypeDef] = None
    AutoMerging: Optional[AutoMergingOutputTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None


class RuleBasedMatchingResponseTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    MatchingRules: Optional[List[MatchingRuleOutputTypeDef]] = None
    Status: Optional[RuleBasedMatchingStatusType] = None
    MaxAllowedRuleLevelForMerging: Optional[int] = None
    MaxAllowedRuleLevelForMatching: Optional[int] = None
    AttributeTypesSelector: Optional[AttributeTypesSelectorOutputTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None


class GetIdentityResolutionJobResponseTypeDef(BaseValidatorModel):
    DomainName: str
    JobId: str
    Status: IdentityResolutionJobStatusType
    Message: str
    JobStartTime: datetime
    JobEndTime: datetime
    LastUpdatedAt: datetime
    JobExpirationTime: datetime
    AutoMerging: AutoMergingOutputTypeDef
    ExportingLocation: ExportingLocationTypeDef
    JobStats: JobStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IdentityResolutionJobTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    JobId: Optional[str] = None
    Status: Optional[IdentityResolutionJobStatusType] = None
    JobStartTime: Optional[datetime] = None
    JobEndTime: Optional[datetime] = None
    JobStats: Optional[JobStatsTypeDef] = None
    ExportingLocation: Optional[ExportingLocationTypeDef] = None
    Message: Optional[str] = None


class BatchGetProfileResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchGetProfileErrorTypeDef]
    Profiles: List[ProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ProfileQueryResultTypeDef(BaseValidatorModel):
    ProfileId: str
    QueryResult: QueryResultType
    Profile: Optional[ProfileTypeDef] = None


class SearchProfilesResponseTypeDef(BaseValidatorModel):
    Items: List[ProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AttributeTypesSelectorUnionTypeDef(BaseValidatorModel):
    pass


class MatchingRuleUnionTypeDef(BaseValidatorModel):
    pass


class RuleBasedMatchingRequestTypeDef(BaseValidatorModel):
    Enabled: bool
    MatchingRules: Optional[Sequence[MatchingRuleUnionTypeDef]] = None
    MaxAllowedRuleLevelForMerging: Optional[int] = None
    MaxAllowedRuleLevelForMatching: Optional[int] = None
    AttributeTypesSelector: Optional[AttributeTypesSelectorUnionTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None


class ObjectAttributeUnionTypeDef(BaseValidatorModel):
    pass


class EventTriggerDimensionTypeDef(BaseValidatorModel):
    ObjectAttributes: Sequence[ObjectAttributeUnionTypeDef]


class ObjectTypeKeyUnionTypeDef(BaseValidatorModel):
    pass


class PutProfileObjectTypeRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    Description: str
    TemplateId: Optional[str] = None
    ExpirationDays: Optional[int] = None
    EncryptionKey: Optional[str] = None
    AllowProfileCreation: Optional[bool] = None
    SourceLastUpdatedTimestampFormat: Optional[str] = None
    MaxProfileObjectCount: Optional[int] = None
    Fields: Optional[Mapping[str, ObjectTypeFieldTypeDef]] = None
    Keys: Optional[Mapping[str, Sequence[ObjectTypeKeyUnionTypeDef]]] = None
    Tags: Optional[Mapping[str, str]] = None


class ProfileDimensionUnionTypeDef(BaseValidatorModel):
    pass


class AddressDimensionTypeDef(BaseValidatorModel):
    City: Optional[ProfileDimensionUnionTypeDef] = None
    Country: Optional[ProfileDimensionUnionTypeDef] = None
    County: Optional[ProfileDimensionUnionTypeDef] = None
    PostalCode: Optional[ProfileDimensionUnionTypeDef] = None
    Province: Optional[ProfileDimensionUnionTypeDef] = None
    State: Optional[ProfileDimensionUnionTypeDef] = None


class SourceFlowConfigTypeDef(BaseValidatorModel):
    ConnectorType: SourceConnectorTypeType
    SourceConnectorProperties: SourceConnectorPropertiesTypeDef
    ConnectorProfileName: Optional[str] = None
    IncrementalPullConfig: Optional[IncrementalPullConfigTypeDef] = None


class TriggerConfigTypeDef(BaseValidatorModel):
    TriggerType: TriggerTypeType
    TriggerProperties: Optional[TriggerPropertiesTypeDef] = None


class DimensionOutputTypeDef(BaseValidatorModel):
    ProfileAttributes: Optional[ProfileAttributesOutputTypeDef] = None
    CalculatedAttributes: Optional[Dict[str, CalculatedAttributeDimensionOutputTypeDef]] = None


class CreateEventTriggerResponseTypeDef(BaseValidatorModel):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutputTypeDef]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutputTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetEventTriggerResponseTypeDef(BaseValidatorModel):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutputTypeDef]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutputTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEventTriggerResponseTypeDef(BaseValidatorModel):
    EventTriggerName: str
    ObjectTypeName: str
    Description: str
    EventTriggerConditions: List[EventTriggerConditionOutputTypeDef]
    SegmentFilter: str
    EventTriggerLimits: EventTriggerLimitsOutputTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDomainResponseTypeDef(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: MatchingResponseTypeDef
    RuleBasedMatching: RuleBasedMatchingResponseTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDomainResponseTypeDef(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Stats: DomainStatsTypeDef
    Matching: MatchingResponseTypeDef
    RuleBasedMatching: RuleBasedMatchingResponseTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDomainResponseTypeDef(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: str
    DeadLetterQueueUrl: str
    Matching: MatchingResponseTypeDef
    RuleBasedMatching: RuleBasedMatchingResponseTypeDef
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListIdentityResolutionJobsResponseTypeDef(BaseValidatorModel):
    IdentityResolutionJobsList: List[IdentityResolutionJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FilterGroupOutputTypeDef(BaseValidatorModel):
    pass


class FilterOutputTypeDef(BaseValidatorModel):
    Include: IncludeType
    Groups: List[FilterGroupOutputTypeDef]


class FilterGroupTypeDef(BaseValidatorModel):
    pass


class FilterTypeDef(BaseValidatorModel):
    Include: IncludeType
    Groups: Sequence[FilterGroupTypeDef]


class GetSegmentMembershipResponseTypeDef(BaseValidatorModel):
    SegmentDefinitionName: str
    Profiles: List[ProfileQueryResultTypeDef]
    Failures: List[ProfileQueryFailuresTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FlowDefinitionTypeDef(BaseValidatorModel):
    FlowName: str
    KmsArn: str
    SourceFlowConfig: SourceFlowConfigTypeDef
    Tasks: Sequence[TaskTypeDef]
    TriggerConfig: TriggerConfigTypeDef
    Description: Optional[str] = None


class AutoMergingUnionTypeDef(BaseValidatorModel):
    pass


class MatchingRequestTypeDef(BaseValidatorModel):
    Enabled: bool
    JobSchedule: Optional[JobScheduleTypeDef] = None
    AutoMerging: Optional[AutoMergingUnionTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None


class CreateCalculatedAttributeDefinitionResponseTypeDef(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    AttributeDetails: AttributeDetailsOutputTypeDef
    Conditions: ConditionsTypeDef
    Filter: FilterOutputTypeDef
    Statistic: StatisticType
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetCalculatedAttributeDefinitionResponseTypeDef(BaseValidatorModel):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Statistic: StatisticType
    Filter: FilterOutputTypeDef
    Conditions: ConditionsTypeDef
    AttributeDetails: AttributeDetailsOutputTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EventTriggerDimensionUnionTypeDef(BaseValidatorModel):
    pass


class EventTriggerConditionTypeDef(BaseValidatorModel):
    EventTriggerDimensions: Sequence[EventTriggerDimensionUnionTypeDef]
    LogicalOperator: EventTriggerLogicalOperatorType


class AddressDimensionUnionTypeDef(BaseValidatorModel):
    pass


class DateDimensionUnionTypeDef(BaseValidatorModel):
    pass


class AttributeDimensionUnionTypeDef(BaseValidatorModel):
    pass


class ExtraLengthValueProfileDimensionUnionTypeDef(BaseValidatorModel):
    pass


class ProfileAttributesTypeDef(BaseValidatorModel):
    AccountNumber: Optional[ProfileDimensionUnionTypeDef] = None
    AdditionalInformation: Optional[ExtraLengthValueProfileDimensionUnionTypeDef] = None
    FirstName: Optional[ProfileDimensionUnionTypeDef] = None
    LastName: Optional[ProfileDimensionUnionTypeDef] = None
    MiddleName: Optional[ProfileDimensionUnionTypeDef] = None
    GenderString: Optional[ProfileDimensionUnionTypeDef] = None
    PartyTypeString: Optional[ProfileDimensionUnionTypeDef] = None
    BirthDate: Optional[DateDimensionUnionTypeDef] = None
    PhoneNumber: Optional[ProfileDimensionUnionTypeDef] = None
    BusinessName: Optional[ProfileDimensionUnionTypeDef] = None
    BusinessPhoneNumber: Optional[ProfileDimensionUnionTypeDef] = None
    HomePhoneNumber: Optional[ProfileDimensionUnionTypeDef] = None
    MobilePhoneNumber: Optional[ProfileDimensionUnionTypeDef] = None
    EmailAddress: Optional[ProfileDimensionUnionTypeDef] = None
    PersonalEmailAddress: Optional[ProfileDimensionUnionTypeDef] = None
    BusinessEmailAddress: Optional[ProfileDimensionUnionTypeDef] = None
    Address: Optional[AddressDimensionUnionTypeDef] = None
    ShippingAddress: Optional[AddressDimensionUnionTypeDef] = None
    MailingAddress: Optional[AddressDimensionUnionTypeDef] = None
    BillingAddress: Optional[AddressDimensionUnionTypeDef] = None
    Attributes: Optional[Mapping[str, AttributeDimensionUnionTypeDef]] = None


class AppflowIntegrationTypeDef(BaseValidatorModel):
    FlowDefinition: FlowDefinitionTypeDef
    Batches: Optional[Sequence[BatchTypeDef]] = None


class PutIntegrationRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: Optional[str] = None
    ObjectTypeName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    FlowDefinition: Optional[FlowDefinitionTypeDef] = None
    ObjectTypeNames: Optional[Mapping[str, str]] = None
    RoleArn: Optional[str] = None
    EventTriggerNames: Optional[Sequence[str]] = None


class GroupOutputTypeDef(BaseValidatorModel):
    pass


class SegmentGroupOutputTypeDef(BaseValidatorModel):
    Groups: Optional[List[GroupOutputTypeDef]] = None
    Include: Optional[IncludeOptionsType] = None


class CreateDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequestTypeDef] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequestTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: Optional[int] = None
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequestTypeDef] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequestTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class FilterUnionTypeDef(BaseValidatorModel):
    pass


class AttributeDetailsUnionTypeDef(BaseValidatorModel):
    pass


class CreateCalculatedAttributeDefinitionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str
    AttributeDetails: AttributeDetailsUnionTypeDef
    Statistic: StatisticType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Conditions: Optional[ConditionsTypeDef] = None
    Filter: Optional[FilterUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class IntegrationConfigTypeDef(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationTypeDef] = None


class GetSegmentDefinitionResponseTypeDef(BaseValidatorModel):
    SegmentDefinitionName: str
    DisplayName: str
    Description: str
    SegmentGroups: SegmentGroupOutputTypeDef
    SegmentDefinitionArn: str
    CreatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EventTriggerLimitsUnionTypeDef(BaseValidatorModel):
    pass


class EventTriggerConditionUnionTypeDef(BaseValidatorModel):
    pass


class CreateEventTriggerRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str
    ObjectTypeName: str
    EventTriggerConditions: Sequence[EventTriggerConditionUnionTypeDef]
    Description: Optional[str] = None
    SegmentFilter: Optional[str] = None
    EventTriggerLimits: Optional[EventTriggerLimitsUnionTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateEventTriggerRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventTriggerName: str
    ObjectTypeName: Optional[str] = None
    Description: Optional[str] = None
    EventTriggerConditions: Optional[Sequence[EventTriggerConditionUnionTypeDef]] = None
    SegmentFilter: Optional[str] = None
    EventTriggerLimits: Optional[EventTriggerLimitsUnionTypeDef] = None


class CalculatedAttributeDimensionUnionTypeDef(BaseValidatorModel):
    pass


class ProfileAttributesUnionTypeDef(BaseValidatorModel):
    pass


class DimensionTypeDef(BaseValidatorModel):
    ProfileAttributes: Optional[ProfileAttributesUnionTypeDef] = None
    CalculatedAttributes: Optional[Mapping[str, CalculatedAttributeDimensionUnionTypeDef]] = None


class CreateIntegrationWorkflowRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    IntegrationConfig: IntegrationConfigTypeDef
    ObjectTypeName: str
    RoleArn: str
    Tags: Optional[Mapping[str, str]] = None


class GroupTypeDef(BaseValidatorModel):
    pass


class SegmentGroupTypeDef(BaseValidatorModel):
    Groups: Optional[Sequence[GroupTypeDef]] = None
    Include: Optional[IncludeOptionsType] = None


class GroupUnionTypeDef(BaseValidatorModel):
    pass


class SegmentGroupStructureTypeDef(BaseValidatorModel):
    Groups: Optional[Sequence[GroupUnionTypeDef]] = None
    Include: Optional[IncludeOptionsType] = None


class CreateSegmentEstimateRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SegmentQuery: SegmentGroupStructureTypeDef


class SegmentGroupUnionTypeDef(BaseValidatorModel):
    pass


class CreateSegmentDefinitionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    SegmentDefinitionName: str
    DisplayName: str
    SegmentGroups: SegmentGroupUnionTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


