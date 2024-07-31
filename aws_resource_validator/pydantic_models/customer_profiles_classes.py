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
from aws_resource_validator.pydantic_models.customer_profiles_constants import *

class AddProfileKeyRequestRequestTypeDef(BaseModel):
    ProfileId: str
    KeyName: str
    Values: Sequence[str]
    DomainName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AdditionalSearchKeyTypeDef(BaseModel):
    KeyName: str
    Values: Sequence[str]

class AddressTypeDef(BaseModel):
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

class AppflowIntegrationWorkflowAttributesTypeDef(BaseModel):
    SourceConnectorType: SourceConnectorTypeType
    ConnectorProfileName: str
    RoleArn: Optional[str] = None

class AppflowIntegrationWorkflowMetricsTypeDef(BaseModel):
    RecordsProcessed: int
    StepsCompleted: int
    TotalSteps: int

class AppflowIntegrationWorkflowStepTypeDef(BaseModel):
    FlowName: str
    Status: StatusType
    ExecutionMessage: str
    RecordsProcessed: int
    BatchRecordsStartTime: str
    BatchRecordsEndTime: str
    CreatedAt: datetime
    LastUpdatedAt: datetime

class AttributeItemTypeDef(BaseModel):
    Name: str

class AttributeTypesSelectorOutputTypeDef(BaseModel):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: Optional[List[str]] = None
    PhoneNumber: Optional[List[str]] = None
    EmailAddress: Optional[List[str]] = None

class AttributeTypesSelectorTypeDef(BaseModel):
    AttributeMatchingModel: AttributeMatchingModelType
    Address: Optional[Sequence[str]] = None
    PhoneNumber: Optional[Sequence[str]] = None
    EmailAddress: Optional[Sequence[str]] = None

class ConflictResolutionTypeDef(BaseModel):
    ConflictResolvingModel: ConflictResolvingModelType
    SourceName: Optional[str] = None

class ConsolidationOutputTypeDef(BaseModel):
    MatchingAttributesList: List[List[str]]

class ConsolidationTypeDef(BaseModel):
    MatchingAttributesList: Sequence[Sequence[str]]

class RangeTypeDef(BaseModel):
    Value: int
    Unit: Literal["DAYS"]

class ThresholdTypeDef(BaseModel):
    Value: str
    Operator: OperatorType

class ConnectorOperatorTypeDef(BaseModel):
    Marketo: Optional[MarketoConnectorOperatorType] = None
    S3: Optional[S3ConnectorOperatorType] = None
    Salesforce: Optional[SalesforceConnectorOperatorType] = None
    ServiceNow: Optional[ServiceNowConnectorOperatorType] = None
    Zendesk: Optional[ZendeskConnectorOperatorType] = None

class CreateEventStreamRequestRequestTypeDef(BaseModel):
    DomainName: str
    Uri: str
    EventStreamName: str
    Tags: Optional[Mapping[str, str]] = None

class DeleteCalculatedAttributeDefinitionRequestRequestTypeDef(BaseModel):
    DomainName: str
    CalculatedAttributeName: str

class DeleteDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class DeleteEventStreamRequestRequestTypeDef(BaseModel):
    DomainName: str
    EventStreamName: str

class DeleteIntegrationRequestRequestTypeDef(BaseModel):
    DomainName: str
    Uri: str

class DeleteProfileKeyRequestRequestTypeDef(BaseModel):
    ProfileId: str
    KeyName: str
    Values: Sequence[str]
    DomainName: str

class DeleteProfileObjectRequestRequestTypeDef(BaseModel):
    ProfileId: str
    ProfileObjectUniqueKey: str
    ObjectTypeName: str
    DomainName: str

class DeleteProfileObjectTypeRequestRequestTypeDef(BaseModel):
    DomainName: str
    ObjectTypeName: str

class DeleteProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str
    DomainName: str

class DeleteWorkflowRequestRequestTypeDef(BaseModel):
    DomainName: str
    WorkflowId: str

class DestinationSummaryTypeDef(BaseModel):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: Optional[datetime] = None

class DetectProfileObjectTypeRequestRequestTypeDef(BaseModel):
    Objects: Sequence[str]
    DomainName: str

class ObjectTypeFieldTypeDef(BaseModel):
    Source: Optional[str] = None
    Target: Optional[str] = None
    ContentType: Optional[FieldContentTypeType] = None

class ObjectTypeKeyOutputTypeDef(BaseModel):
    StandardIdentifiers: Optional[List[StandardIdentifierType]] = None
    FieldNames: Optional[List[str]] = None

class DomainStatsTypeDef(BaseModel):
    ProfileCount: Optional[int] = None
    MeteringProfileCount: Optional[int] = None
    ObjectCount: Optional[int] = None
    TotalSize: Optional[int] = None

class EventStreamDestinationDetailsTypeDef(BaseModel):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: Optional[datetime] = None
    Message: Optional[str] = None

class S3ExportingConfigTypeDef(BaseModel):
    S3BucketName: str
    S3KeyName: Optional[str] = None

class S3ExportingLocationTypeDef(BaseModel):
    S3BucketName: Optional[str] = None
    S3KeyName: Optional[str] = None

class FieldSourceProfileIdsTypeDef(BaseModel):
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

class FoundByKeyValueTypeDef(BaseModel):
    KeyName: Optional[str] = None
    Values: Optional[List[str]] = None

class GetCalculatedAttributeDefinitionRequestRequestTypeDef(BaseModel):
    DomainName: str
    CalculatedAttributeName: str

class GetCalculatedAttributeForProfileRequestRequestTypeDef(BaseModel):
    DomainName: str
    ProfileId: str
    CalculatedAttributeName: str

class GetDomainRequestRequestTypeDef(BaseModel):
    DomainName: str

class GetEventStreamRequestRequestTypeDef(BaseModel):
    DomainName: str
    EventStreamName: str

class GetIdentityResolutionJobRequestRequestTypeDef(BaseModel):
    DomainName: str
    JobId: str

class JobStatsTypeDef(BaseModel):
    NumberOfProfilesReviewed: Optional[int] = None
    NumberOfMatchesFound: Optional[int] = None
    NumberOfMergesDone: Optional[int] = None

class GetIntegrationRequestRequestTypeDef(BaseModel):
    DomainName: str
    Uri: str

class GetMatchesRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MatchItemTypeDef(BaseModel):
    MatchId: Optional[str] = None
    ProfileIds: Optional[List[str]] = None
    ConfidenceScore: Optional[float] = None

class GetProfileObjectTypeRequestRequestTypeDef(BaseModel):
    DomainName: str
    ObjectTypeName: str

class GetProfileObjectTypeTemplateRequestRequestTypeDef(BaseModel):
    TemplateId: str

class GetSimilarProfilesRequestRequestTypeDef(BaseModel):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetWorkflowRequestRequestTypeDef(BaseModel):
    DomainName: str
    WorkflowId: str

class GetWorkflowStepsRequestRequestTypeDef(BaseModel):
    DomainName: str
    WorkflowId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class IncrementalPullConfigTypeDef(BaseModel):
    DatetimeTypeFieldName: Optional[str] = None

class JobScheduleTypeDef(BaseModel):
    DayOfTheWeek: JobScheduleDayOfTheWeekType
    Time: str

class ListAccountIntegrationsRequestRequestTypeDef(BaseModel):
    Uri: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeHidden: Optional[bool] = None

class ListIntegrationItemTypeDef(BaseModel):
    DomainName: str
    Uri: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ObjectTypeName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    ObjectTypeNames: Optional[Dict[str, str]] = None
    WorkflowId: Optional[str] = None
    IsUnstructured: Optional[bool] = None

class ListCalculatedAttributeDefinitionItemTypeDef(BaseModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class ListCalculatedAttributeDefinitionsRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCalculatedAttributeForProfileItemTypeDef(BaseModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    IsDataPartial: Optional[str] = None
    Value: Optional[str] = None

class ListCalculatedAttributesForProfileRequestRequestTypeDef(BaseModel):
    DomainName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDomainItemTypeDef(BaseModel):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Optional[Dict[str, str]] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEventStreamsRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentityResolutionJobsRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIntegrationsRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeHidden: Optional[bool] = None

class ListProfileObjectTypeItemTypeDef(BaseModel):
    ObjectTypeName: str
    Description: str
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    MaxProfileObjectCount: Optional[int] = None
    MaxAvailableProfileObjectCount: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None

class ListProfileObjectTypeTemplateItemTypeDef(BaseModel):
    TemplateId: Optional[str] = None
    SourceName: Optional[str] = None
    SourceObject: Optional[str] = None

class ListProfileObjectTypeTemplatesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProfileObjectTypesRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProfileObjectsItemTypeDef(BaseModel):
    ObjectTypeName: Optional[str] = None
    ProfileObjectUniqueKey: Optional[str] = None
    Object: Optional[str] = None

class ObjectFilterTypeDef(BaseModel):
    KeyName: str
    Values: Sequence[str]

class ListRuleBasedMatchesRequestRequestTypeDef(BaseModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListWorkflowsItemTypeDef(BaseModel):
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    WorkflowId: str
    Status: StatusType
    StatusDescription: str
    CreatedAt: datetime
    LastUpdatedAt: datetime

class MarketoSourcePropertiesTypeDef(BaseModel):
    Object: str

class MatchingRuleOutputTypeDef(BaseModel):
    Rule: List[str]

class MatchingRuleTypeDef(BaseModel):
    Rule: Sequence[str]

class ObjectTypeKeyTypeDef(BaseModel):
    StandardIdentifiers: Optional[Sequence[StandardIdentifierType]] = None
    FieldNames: Optional[Sequence[str]] = None

class PutProfileObjectRequestRequestTypeDef(BaseModel):
    ObjectTypeName: str
    Object: str
    DomainName: str

class S3SourcePropertiesTypeDef(BaseModel):
    BucketName: str
    BucketPrefix: Optional[str] = None

class SalesforceSourcePropertiesTypeDef(BaseModel):
    Object: str
    EnableDynamicFieldUpdate: Optional[bool] = None
    IncludeDeletedRecords: Optional[bool] = None

class ServiceNowSourcePropertiesTypeDef(BaseModel):
    Object: str

class ZendeskSourcePropertiesTypeDef(BaseModel):
    Object: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAddressTypeDef(BaseModel):
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

class AddProfileKeyResponseTypeDef(BaseModel):
    KeyName: str
    Values: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventStreamResponseTypeDef(BaseModel):
    EventStreamArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationWorkflowResponseTypeDef(BaseModel):
    WorkflowId: str
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileResponseTypeDef(BaseModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIntegrationResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileKeyResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileObjectResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileObjectTypeResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAutoMergingPreviewResponseTypeDef(BaseModel):
    DomainName: str
    NumberOfMatchesInSample: int
    NumberOfProfilesInSample: int
    NumberOfProfilesWillBeMerged: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculatedAttributeForProfileResponseTypeDef(BaseModel):
    CalculatedAttributeName: str
    DisplayName: str
    IsDataPartial: str
    Value: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationResponseTypeDef(BaseModel):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ObjectTypeNames: Dict[str, str]
    WorkflowId: str
    IsUnstructured: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetSimilarProfilesResponseTypeDef(BaseModel):
    ProfileIds: List[str]
    MatchId: str
    MatchType: MatchTypeType
    RuleLevel: int
    ConfidenceScore: float
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRuleBasedMatchesResponseTypeDef(BaseModel):
    MatchIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MergeProfilesResponseTypeDef(BaseModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutIntegrationResponseTypeDef(BaseModel):
    DomainName: str
    Uri: str
    ObjectTypeName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ObjectTypeNames: Dict[str, str]
    WorkflowId: str
    IsUnstructured: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutProfileObjectResponseTypeDef(BaseModel):
    ProfileObjectUniqueKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileResponseTypeDef(BaseModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchProfilesRequestRequestTypeDef(BaseModel):
    DomainName: str
    KeyName: str
    Values: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AdditionalSearchKeys: Optional[Sequence[AdditionalSearchKeyTypeDef]] = None
    LogicalOperator: Optional[LogicalOperatorType] = None

class CreateProfileRequestRequestTypeDef(BaseModel):
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

class WorkflowAttributesTypeDef(BaseModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowAttributesTypeDef] = None

class WorkflowMetricsTypeDef(BaseModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowMetricsTypeDef] = None

class WorkflowStepItemTypeDef(BaseModel):
    AppflowIntegration: Optional[AppflowIntegrationWorkflowStepTypeDef] = None

class AttributeDetailsOutputTypeDef(BaseModel):
    Attributes: List[AttributeItemTypeDef]
    Expression: str

class AttributeDetailsTypeDef(BaseModel):
    Attributes: Sequence[AttributeItemTypeDef]
    Expression: str

class AutoMergingOutputTypeDef(BaseModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationOutputTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None

class AutoMergingTypeDef(BaseModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None

class GetAutoMergingPreviewRequestRequestTypeDef(BaseModel):
    DomainName: str
    Consolidation: ConsolidationTypeDef
    ConflictResolution: ConflictResolutionTypeDef
    MinAllowedConfidenceScoreForMerging: Optional[float] = None

class BatchTypeDef(BaseModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class ListWorkflowsRequestRequestTypeDef(BaseModel):
    DomainName: str
    WorkflowType: Optional[Literal["APPFLOW_INTEGRATION"]] = None
    Status: Optional[StatusType] = None
    QueryStartDate: Optional[TimestampTypeDef] = None
    QueryEndDate: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ScheduledTriggerPropertiesTypeDef(BaseModel):
    ScheduleExpression: str
    DataPullMode: Optional[DataPullModeType] = None
    ScheduleStartTime: Optional[TimestampTypeDef] = None
    ScheduleEndTime: Optional[TimestampTypeDef] = None
    Timezone: Optional[str] = None
    ScheduleOffset: Optional[int] = None
    FirstExecutionFrom: Optional[TimestampTypeDef] = None

class ConditionsTypeDef(BaseModel):
    Range: Optional[RangeTypeDef] = None
    ObjectCount: Optional[int] = None
    Threshold: Optional[ThresholdTypeDef] = None

class TaskTypeDef(BaseModel):
    SourceFields: Sequence[str]
    TaskType: TaskTypeType
    ConnectorOperator: Optional[ConnectorOperatorTypeDef] = None
    DestinationField: Optional[str] = None
    TaskProperties: Optional[Mapping[OperatorPropertiesKeysType, str]] = None

class EventStreamSummaryTypeDef(BaseModel):
    DomainName: str
    EventStreamName: str
    EventStreamArn: str
    State: EventStreamStateType
    StoppedSince: Optional[datetime] = None
    DestinationSummary: Optional[DestinationSummaryTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

class DetectedProfileObjectTypeTypeDef(BaseModel):
    SourceLastUpdatedTimestampFormat: Optional[str] = None
    Fields: Optional[Dict[str, ObjectTypeFieldTypeDef]] = None
    Keys: Optional[Dict[str, List[ObjectTypeKeyOutputTypeDef]]] = None

class GetProfileObjectTypeResponseTypeDef(BaseModel):
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

class GetProfileObjectTypeTemplateResponseTypeDef(BaseModel):
    TemplateId: str
    SourceName: str
    SourceObject: str
    AllowProfileCreation: bool
    SourceLastUpdatedTimestampFormat: str
    Fields: Dict[str, ObjectTypeFieldTypeDef]
    Keys: Dict[str, List[ObjectTypeKeyOutputTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class PutProfileObjectTypeResponseTypeDef(BaseModel):
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

class GetEventStreamResponseTypeDef(BaseModel):
    DomainName: str
    EventStreamArn: str
    CreatedAt: datetime
    State: EventStreamStateType
    StoppedSince: datetime
    DestinationDetails: EventStreamDestinationDetailsTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportingConfigTypeDef(BaseModel):
    S3Exporting: Optional[S3ExportingConfigTypeDef] = None

class ExportingLocationTypeDef(BaseModel):
    S3Exporting: Optional[S3ExportingLocationTypeDef] = None

class MergeProfilesRequestRequestTypeDef(BaseModel):
    DomainName: str
    MainProfileId: str
    ProfileIdsToBeMerged: Sequence[str]
    FieldSourceProfileIds: Optional[FieldSourceProfileIdsTypeDef] = None

class ProfileTypeDef(BaseModel):
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

class GetMatchesResponseTypeDef(BaseModel):
    MatchGenerationDate: datetime
    PotentialMatches: int
    Matches: List[MatchItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAccountIntegrationsResponseTypeDef(BaseModel):
    Items: List[ListIntegrationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIntegrationsResponseTypeDef(BaseModel):
    Items: List[ListIntegrationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCalculatedAttributeDefinitionsResponseTypeDef(BaseModel):
    Items: List[ListCalculatedAttributeDefinitionItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCalculatedAttributesForProfileResponseTypeDef(BaseModel):
    Items: List[ListCalculatedAttributeForProfileItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDomainsResponseTypeDef(BaseModel):
    Items: List[ListDomainItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEventStreamsRequestListEventStreamsPaginateTypeDef(BaseModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfileObjectTypesResponseTypeDef(BaseModel):
    Items: List[ListProfileObjectTypeItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProfileObjectTypeTemplatesResponseTypeDef(BaseModel):
    Items: List[ListProfileObjectTypeTemplateItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProfileObjectsResponseTypeDef(BaseModel):
    Items: List[ListProfileObjectsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProfileObjectsRequestRequestTypeDef(BaseModel):
    DomainName: str
    ObjectTypeName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ObjectFilter: Optional[ObjectFilterTypeDef] = None

class ListWorkflowsResponseTypeDef(BaseModel):
    Items: List[ListWorkflowsItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SourceConnectorPropertiesTypeDef(BaseModel):
    Marketo: Optional[MarketoSourcePropertiesTypeDef] = None
    S3: Optional[S3SourcePropertiesTypeDef] = None
    Salesforce: Optional[SalesforceSourcePropertiesTypeDef] = None
    ServiceNow: Optional[ServiceNowSourcePropertiesTypeDef] = None
    Zendesk: Optional[ZendeskSourcePropertiesTypeDef] = None

class UpdateProfileRequestRequestTypeDef(BaseModel):
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

class GetWorkflowResponseTypeDef(BaseModel):
    WorkflowId: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    Status: StatusType
    ErrorDescription: str
    StartDate: datetime
    LastUpdatedAt: datetime
    Attributes: WorkflowAttributesTypeDef
    Metrics: WorkflowMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowStepsResponseTypeDef(BaseModel):
    WorkflowId: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    Items: List[WorkflowStepItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TriggerPropertiesTypeDef(BaseModel):
    Scheduled: Optional[ScheduledTriggerPropertiesTypeDef] = None

class CreateCalculatedAttributeDefinitionRequestRequestTypeDef(BaseModel):
    DomainName: str
    CalculatedAttributeName: str
    AttributeDetails: AttributeDetailsTypeDef
    Statistic: StatisticType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Conditions: Optional[ConditionsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateCalculatedAttributeDefinitionResponseTypeDef(BaseModel):
    CalculatedAttributeName: str
    DisplayName: str
    Description: str
    AttributeDetails: AttributeDetailsOutputTypeDef
    Conditions: ConditionsTypeDef
    Statistic: StatisticType
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCalculatedAttributeDefinitionResponseTypeDef(BaseModel):
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

class UpdateCalculatedAttributeDefinitionRequestRequestTypeDef(BaseModel):
    DomainName: str
    CalculatedAttributeName: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Conditions: Optional[ConditionsTypeDef] = None

class UpdateCalculatedAttributeDefinitionResponseTypeDef(BaseModel):
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

class ListEventStreamsResponseTypeDef(BaseModel):
    Items: List[EventStreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetectProfileObjectTypeResponseTypeDef(BaseModel):
    DetectedProfileObjectTypes: List[DetectedProfileObjectTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MatchingRequestTypeDef(BaseModel):
    Enabled: bool
    JobSchedule: Optional[JobScheduleTypeDef] = None
    AutoMerging: Optional[AutoMergingTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None

class MatchingResponseTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    JobSchedule: Optional[JobScheduleTypeDef] = None
    AutoMerging: Optional[AutoMergingOutputTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None

class RuleBasedMatchingRequestTypeDef(BaseModel):
    Enabled: bool
    MatchingRules: Optional[Sequence[MatchingRuleTypeDef]] = None
    MaxAllowedRuleLevelForMerging: Optional[int] = None
    MaxAllowedRuleLevelForMatching: Optional[int] = None
    AttributeTypesSelector: Optional[AttributeTypesSelectorTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None

class RuleBasedMatchingResponseTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    MatchingRules: Optional[List[MatchingRuleOutputTypeDef]] = None
    Status: Optional[RuleBasedMatchingStatusType] = None
    MaxAllowedRuleLevelForMerging: Optional[int] = None
    MaxAllowedRuleLevelForMatching: Optional[int] = None
    AttributeTypesSelector: Optional[AttributeTypesSelectorOutputTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None

class GetIdentityResolutionJobResponseTypeDef(BaseModel):
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

class IdentityResolutionJobTypeDef(BaseModel):
    DomainName: Optional[str] = None
    JobId: Optional[str] = None
    Status: Optional[IdentityResolutionJobStatusType] = None
    JobStartTime: Optional[datetime] = None
    JobEndTime: Optional[datetime] = None
    JobStats: Optional[JobStatsTypeDef] = None
    ExportingLocation: Optional[ExportingLocationTypeDef] = None
    Message: Optional[str] = None

class SearchProfilesResponseTypeDef(BaseModel):
    Items: List[ProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutProfileObjectTypeRequestRequestTypeDef(BaseModel):
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

class SourceFlowConfigTypeDef(BaseModel):
    ConnectorType: SourceConnectorTypeType
    SourceConnectorProperties: SourceConnectorPropertiesTypeDef
    ConnectorProfileName: Optional[str] = None
    IncrementalPullConfig: Optional[IncrementalPullConfigTypeDef] = None

class TriggerConfigTypeDef(BaseModel):
    TriggerType: TriggerTypeType
    TriggerProperties: Optional[TriggerPropertiesTypeDef] = None

class CreateDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequestTypeDef] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequestTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateDomainRequestRequestTypeDef(BaseModel):
    DomainName: str
    DefaultExpirationDays: Optional[int] = None
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequestTypeDef] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequestTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateDomainResponseTypeDef(BaseModel):
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

class GetDomainResponseTypeDef(BaseModel):
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

class UpdateDomainResponseTypeDef(BaseModel):
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

class ListIdentityResolutionJobsResponseTypeDef(BaseModel):
    IdentityResolutionJobsList: List[IdentityResolutionJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FlowDefinitionTypeDef(BaseModel):
    FlowName: str
    KmsArn: str
    SourceFlowConfig: SourceFlowConfigTypeDef
    Tasks: Sequence[TaskTypeDef]
    TriggerConfig: TriggerConfigTypeDef
    Description: Optional[str] = None

class AppflowIntegrationTypeDef(BaseModel):
    FlowDefinition: FlowDefinitionTypeDef
    Batches: Optional[Sequence[BatchTypeDef]] = None

class PutIntegrationRequestRequestTypeDef(BaseModel):
    DomainName: str
    Uri: Optional[str] = None
    ObjectTypeName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    FlowDefinition: Optional[FlowDefinitionTypeDef] = None
    ObjectTypeNames: Optional[Mapping[str, str]] = None

class IntegrationConfigTypeDef(BaseModel):
    AppflowIntegration: Optional[AppflowIntegrationTypeDef] = None

class CreateIntegrationWorkflowRequestRequestTypeDef(BaseModel):
    DomainName: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    IntegrationConfig: IntegrationConfigTypeDef
    ObjectTypeName: str
    RoleArn: str
    Tags: Optional[Mapping[str, str]] = None

