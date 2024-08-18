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
from aws_resource_validator.pydantic_models.customer_profiles_constants import *

class AddProfileKeyRequestRequestTypeDef(BaseValidatorModel):
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

class ConflictResolutionTypeDef(BaseValidatorModel):
    ConflictResolvingModel: ConflictResolvingModelType
    SourceName: Optional[str] = None

class ConsolidationOutputTypeDef(BaseValidatorModel):
    MatchingAttributesList: List[List[str]]

class ConsolidationTypeDef(BaseValidatorModel):
    MatchingAttributesList: Sequence[Sequence[str]]

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

class CreateEventStreamRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: str
    EventStreamName: str
    Tags: Optional[Mapping[str, str]] = None

class DeleteCalculatedAttributeDefinitionRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class DeleteEventStreamRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventStreamName: str

class DeleteIntegrationRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: str

class DeleteProfileKeyRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    KeyName: str
    Values: Sequence[str]
    DomainName: str

class DeleteProfileObjectRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    ProfileObjectUniqueKey: str
    ObjectTypeName: str
    DomainName: str

class DeleteProfileObjectTypeRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str

class DeleteProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    DomainName: str

class DeleteWorkflowRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowId: str

class DestinationSummaryTypeDef(BaseValidatorModel):
    Uri: str
    Status: EventStreamDestinationStatusType
    UnhealthySince: Optional[datetime] = None

class DetectProfileObjectTypeRequestRequestTypeDef(BaseValidatorModel):
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

class S3ExportingConfigTypeDef(BaseValidatorModel):
    S3BucketName: str
    S3KeyName: Optional[str] = None

class S3ExportingLocationTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3KeyName: Optional[str] = None

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

class FoundByKeyValueTypeDef(BaseValidatorModel):
    KeyName: Optional[str] = None
    Values: Optional[List[str]] = None

class GetCalculatedAttributeDefinitionRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str

class GetCalculatedAttributeForProfileRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ProfileId: str
    CalculatedAttributeName: str

class GetDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str

class GetEventStreamRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EventStreamName: str

class GetIdentityResolutionJobRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    JobId: str

class JobStatsTypeDef(BaseValidatorModel):
    NumberOfProfilesReviewed: Optional[int] = None
    NumberOfMatchesFound: Optional[int] = None
    NumberOfMergesDone: Optional[int] = None

class GetIntegrationRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: str

class GetMatchesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MatchItemTypeDef(BaseValidatorModel):
    MatchId: Optional[str] = None
    ProfileIds: Optional[List[str]] = None
    ConfidenceScore: Optional[float] = None

class GetProfileObjectTypeRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str

class GetProfileObjectTypeTemplateRequestRequestTypeDef(BaseValidatorModel):
    TemplateId: str

class GetSimilarProfilesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MatchType: MatchTypeType
    SearchKey: str
    SearchValue: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetWorkflowRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowId: str

class GetWorkflowStepsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class IncrementalPullConfigTypeDef(BaseValidatorModel):
    DatetimeTypeFieldName: Optional[str] = None

class JobScheduleTypeDef(BaseValidatorModel):
    DayOfTheWeek: JobScheduleDayOfTheWeekType
    Time: str

class ListAccountIntegrationsRequestRequestTypeDef(BaseValidatorModel):
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

class ListCalculatedAttributeDefinitionItemTypeDef(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Tags: Optional[Dict[str, str]] = None

class ListCalculatedAttributeDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCalculatedAttributeForProfileItemTypeDef(BaseValidatorModel):
    CalculatedAttributeName: Optional[str] = None
    DisplayName: Optional[str] = None
    IsDataPartial: Optional[str] = None
    Value: Optional[str] = None

class ListCalculatedAttributesForProfileRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDomainItemTypeDef(BaseValidatorModel):
    DomainName: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Tags: Optional[Dict[str, str]] = None

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListEventStreamsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIdentityResolutionJobsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIntegrationsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IncludeHidden: Optional[bool] = None

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

class ListProfileObjectTypeTemplatesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListProfileObjectTypesRequestRequestTypeDef(BaseValidatorModel):
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

class ListRuleBasedMatchesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class ObjectTypeKeyTypeDef(BaseValidatorModel):
    StandardIdentifiers: Optional[Sequence[StandardIdentifierType]] = None
    FieldNames: Optional[Sequence[str]] = None

class PutProfileObjectRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteDomainResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class PutProfileObjectResponseTypeDef(BaseValidatorModel):
    ProfileObjectUniqueKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileResponseTypeDef(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchProfilesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    KeyName: str
    Values: Sequence[str]
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AdditionalSearchKeys: Optional[Sequence[AdditionalSearchKeyTypeDef]] = None
    LogicalOperator: Optional[LogicalOperatorType] = None

class CreateProfileRequestRequestTypeDef(BaseValidatorModel):
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

class AutoMergingOutputTypeDef(BaseValidatorModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationOutputTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None

class AutoMergingTypeDef(BaseValidatorModel):
    Enabled: bool
    Consolidation: Optional[ConsolidationTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
    MinAllowedConfidenceScoreForMerging: Optional[float] = None

class GetAutoMergingPreviewRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Consolidation: ConsolidationTypeDef
    ConflictResolution: ConflictResolutionTypeDef
    MinAllowedConfidenceScoreForMerging: Optional[float] = None

class BatchTypeDef(BaseValidatorModel):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class ListWorkflowsRequestRequestTypeDef(BaseValidatorModel):
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

class ExportingConfigTypeDef(BaseValidatorModel):
    S3Exporting: Optional[S3ExportingConfigTypeDef] = None

class ExportingLocationTypeDef(BaseValidatorModel):
    S3Exporting: Optional[S3ExportingLocationTypeDef] = None

class MergeProfilesRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MainProfileId: str
    ProfileIdsToBeMerged: Sequence[str]
    FieldSourceProfileIds: Optional[FieldSourceProfileIdsTypeDef] = None

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

class ListEventStreamsRequestListEventStreamsPaginateTypeDef(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

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

class ListProfileObjectsRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ObjectTypeName: str
    ProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ObjectFilter: Optional[ObjectFilterTypeDef] = None

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

class UpdateProfileRequestRequestTypeDef(BaseValidatorModel):
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

class CreateCalculatedAttributeDefinitionRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    CalculatedAttributeName: str
    AttributeDetails: AttributeDetailsTypeDef
    Statistic: StatisticType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    Conditions: Optional[ConditionsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateCalculatedAttributeDefinitionResponseTypeDef(BaseValidatorModel):
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

class GetCalculatedAttributeDefinitionResponseTypeDef(BaseValidatorModel):
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

class UpdateCalculatedAttributeDefinitionRequestRequestTypeDef(BaseValidatorModel):
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

class ListEventStreamsResponseTypeDef(BaseValidatorModel):
    Items: List[EventStreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetectProfileObjectTypeResponseTypeDef(BaseValidatorModel):
    DetectedProfileObjectTypes: List[DetectedProfileObjectTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MatchingRequestTypeDef(BaseValidatorModel):
    Enabled: bool
    JobSchedule: Optional[JobScheduleTypeDef] = None
    AutoMerging: Optional[AutoMergingTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None

class MatchingResponseTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    JobSchedule: Optional[JobScheduleTypeDef] = None
    AutoMerging: Optional[AutoMergingOutputTypeDef] = None
    ExportingConfig: Optional[ExportingConfigTypeDef] = None

class RuleBasedMatchingRequestTypeDef(BaseValidatorModel):
    Enabled: bool
    MatchingRules: Optional[Sequence[MatchingRuleTypeDef]] = None
    MaxAllowedRuleLevelForMerging: Optional[int] = None
    MaxAllowedRuleLevelForMatching: Optional[int] = None
    AttributeTypesSelector: Optional[AttributeTypesSelectorTypeDef] = None
    ConflictResolution: Optional[ConflictResolutionTypeDef] = None
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

class SearchProfilesResponseTypeDef(BaseValidatorModel):
    Items: List[ProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutProfileObjectTypeRequestRequestTypeDef(BaseValidatorModel):
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

class SourceFlowConfigTypeDef(BaseValidatorModel):
    ConnectorType: SourceConnectorTypeType
    SourceConnectorProperties: SourceConnectorPropertiesTypeDef
    ConnectorProfileName: Optional[str] = None
    IncrementalPullConfig: Optional[IncrementalPullConfigTypeDef] = None

class TriggerConfigTypeDef(BaseValidatorModel):
    TriggerType: TriggerTypeType
    TriggerProperties: Optional[TriggerPropertiesTypeDef] = None

class CreateDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: int
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequestTypeDef] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequestTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DefaultExpirationDays: Optional[int] = None
    DefaultEncryptionKey: Optional[str] = None
    DeadLetterQueueUrl: Optional[str] = None
    Matching: Optional[MatchingRequestTypeDef] = None
    RuleBasedMatching: Optional[RuleBasedMatchingRequestTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

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

class FlowDefinitionTypeDef(BaseValidatorModel):
    FlowName: str
    KmsArn: str
    SourceFlowConfig: SourceFlowConfigTypeDef
    Tasks: Sequence[TaskTypeDef]
    TriggerConfig: TriggerConfigTypeDef
    Description: Optional[str] = None

class AppflowIntegrationTypeDef(BaseValidatorModel):
    FlowDefinition: FlowDefinitionTypeDef
    Batches: Optional[Sequence[BatchTypeDef]] = None

class PutIntegrationRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Uri: Optional[str] = None
    ObjectTypeName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    FlowDefinition: Optional[FlowDefinitionTypeDef] = None
    ObjectTypeNames: Optional[Mapping[str, str]] = None

class IntegrationConfigTypeDef(BaseValidatorModel):
    AppflowIntegration: Optional[AppflowIntegrationTypeDef] = None

class CreateIntegrationWorkflowRequestRequestTypeDef(BaseValidatorModel):
    DomainName: str
    WorkflowType: Literal["APPFLOW_INTEGRATION"]
    IntegrationConfig: IntegrationConfigTypeDef
    ObjectTypeName: str
    RoleArn: str
    Tags: Optional[Mapping[str, str]] = None

