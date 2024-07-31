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
from aws_resource_validator.pydantic_models.config_constants import *

class AccountAggregationSourceExtraOutputTypeDef(BaseModel):
    AccountIds: List[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[List[str]] = None

class AccountAggregationSourceOutputTypeDef(BaseModel):
    AccountIds: List[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[List[str]] = None

class AccountAggregationSourceTypeDef(BaseModel):
    AccountIds: Sequence[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[Sequence[str]] = None

class AggregateConformancePackComplianceTypeDef(BaseModel):
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    CompliantRuleCount: Optional[int] = None
    NonCompliantRuleCount: Optional[int] = None
    TotalRuleCount: Optional[int] = None

class AggregateConformancePackComplianceCountTypeDef(BaseModel):
    CompliantConformancePackCount: Optional[int] = None
    NonCompliantConformancePackCount: Optional[int] = None

class AggregateConformancePackComplianceFiltersTypeDef(BaseModel):
    ConformancePackName: Optional[str] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class AggregateConformancePackComplianceSummaryFiltersTypeDef(BaseModel):
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class AggregateResourceIdentifierTypeDef(BaseModel):
    SourceAccountId: str
    SourceRegion: str
    ResourceId: str
    ResourceType: ResourceTypeType
    ResourceName: Optional[str] = None

class AggregatedSourceStatusTypeDef(BaseModel):
    SourceId: Optional[str] = None
    SourceType: Optional[AggregatedSourceTypeType] = None
    AwsRegion: Optional[str] = None
    LastUpdateStatus: Optional[AggregatedSourceStatusTypeType] = None
    LastUpdateTime: Optional[datetime] = None
    LastErrorCode: Optional[str] = None
    LastErrorMessage: Optional[str] = None

class AggregationAuthorizationTypeDef(BaseModel):
    AggregationAuthorizationArn: Optional[str] = None
    AuthorizedAccountId: Optional[str] = None
    AuthorizedAwsRegion: Optional[str] = None
    CreationTime: Optional[datetime] = None

class BaseConfigurationItemTypeDef(BaseModel):
    version: Optional[str] = None
    accountId: Optional[str] = None
    configurationItemCaptureTime: Optional[datetime] = None
    configurationItemStatus: Optional[ConfigurationItemStatusType] = None
    configurationStateId: Optional[str] = None
    arn: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    awsRegion: Optional[str] = None
    availabilityZone: Optional[str] = None
    resourceCreationTime: Optional[datetime] = None
    configuration: Optional[str] = None
    supplementaryConfiguration: Optional[Dict[str, str]] = None
    recordingFrequency: Optional[RecordingFrequencyType] = None
    configurationItemDeliveryTime: Optional[datetime] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ResourceKeyTypeDef(BaseModel):
    resourceType: ResourceTypeType
    resourceId: str

class ComplianceContributorCountTypeDef(BaseModel):
    CappedCount: Optional[int] = None
    CapExceeded: Optional[bool] = None

class ConfigExportDeliveryInfoTypeDef(BaseModel):
    lastStatus: Optional[DeliveryStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastAttemptTime: Optional[datetime] = None
    lastSuccessfulTime: Optional[datetime] = None
    nextDeliveryTime: Optional[datetime] = None

class ConfigRuleComplianceFiltersTypeDef(BaseModel):
    ConfigRuleName: Optional[str] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ConfigRuleComplianceSummaryFiltersTypeDef(BaseModel):
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ConfigRuleEvaluationStatusTypeDef(BaseModel):
    ConfigRuleName: Optional[str] = None
    ConfigRuleArn: Optional[str] = None
    ConfigRuleId: Optional[str] = None
    LastSuccessfulInvocationTime: Optional[datetime] = None
    LastFailedInvocationTime: Optional[datetime] = None
    LastSuccessfulEvaluationTime: Optional[datetime] = None
    LastFailedEvaluationTime: Optional[datetime] = None
    FirstActivatedTime: Optional[datetime] = None
    LastDeactivatedTime: Optional[datetime] = None
    LastErrorCode: Optional[str] = None
    LastErrorMessage: Optional[str] = None
    FirstEvaluationStarted: Optional[bool] = None
    LastDebugLogDeliveryStatus: Optional[str] = None
    LastDebugLogDeliveryStatusReason: Optional[str] = None
    LastDebugLogDeliveryTime: Optional[datetime] = None

class EvaluationModeConfigurationTypeDef(BaseModel):
    Mode: Optional[EvaluationModeType] = None

class ScopeExtraOutputTypeDef(BaseModel):
    ComplianceResourceTypes: Optional[List[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None

class ScopeOutputTypeDef(BaseModel):
    ComplianceResourceTypes: Optional[List[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None

class ScopeTypeDef(BaseModel):
    ComplianceResourceTypes: Optional[Sequence[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None

class ConfigSnapshotDeliveryPropertiesTypeDef(BaseModel):
    deliveryFrequency: Optional[MaximumExecutionFrequencyType] = None

class ConfigStreamDeliveryInfoTypeDef(BaseModel):
    lastStatus: Optional[DeliveryStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastStatusChangeTime: Optional[datetime] = None

class OrganizationAggregationSourceOutputTypeDef(BaseModel):
    RoleArn: str
    AwsRegions: Optional[List[str]] = None
    AllAwsRegions: Optional[bool] = None

class RelationshipTypeDef(BaseModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    relationshipName: Optional[str] = None

class ConfigurationRecorderStatusTypeDef(BaseModel):
    name: Optional[str] = None
    lastStartTime: Optional[datetime] = None
    lastStopTime: Optional[datetime] = None
    recording: Optional[bool] = None
    lastStatus: Optional[RecorderStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastStatusChangeTime: Optional[datetime] = None

class ConformancePackComplianceFiltersTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None

class ConformancePackComplianceScoreTypeDef(BaseModel):
    Score: Optional[str] = None
    ConformancePackName: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None

class ConformancePackComplianceScoresFiltersTypeDef(BaseModel):
    ConformancePackNames: Sequence[str]

class ConformancePackComplianceSummaryTypeDef(BaseModel):
    ConformancePackName: str
    ConformancePackComplianceStatus: ConformancePackComplianceTypeType

class ConformancePackInputParameterTypeDef(BaseModel):
    ParameterName: str
    ParameterValue: str

class TemplateSSMDocumentDetailsTypeDef(BaseModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None

class ConformancePackEvaluationFiltersTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    ResourceType: Optional[str] = None
    ResourceIds: Optional[Sequence[str]] = None

class ConformancePackRuleComplianceTypeDef(BaseModel):
    ConfigRuleName: Optional[str] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    Controls: Optional[List[str]] = None

class ConformancePackStatusDetailTypeDef(BaseModel):
    ConformancePackName: str
    ConformancePackId: str
    ConformancePackArn: str
    ConformancePackState: ConformancePackStateType
    StackArn: str
    LastUpdateRequestedTime: datetime
    ConformancePackStatusReason: Optional[str] = None
    LastUpdateCompletedTime: Optional[datetime] = None

class CustomPolicyDetailsTypeDef(BaseModel):
    PolicyRuntime: str
    PolicyText: str
    EnableDebugLogDelivery: Optional[bool] = None

class DeleteAggregationAuthorizationRequestRequestTypeDef(BaseModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str

class DeleteConfigRuleRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str

class DeleteConfigurationAggregatorRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str

class DeleteConfigurationRecorderRequestRequestTypeDef(BaseModel):
    ConfigurationRecorderName: str

class DeleteConformancePackRequestRequestTypeDef(BaseModel):
    ConformancePackName: str

class DeleteDeliveryChannelRequestRequestTypeDef(BaseModel):
    DeliveryChannelName: str

class DeleteEvaluationResultsRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str

class DeleteOrganizationConfigRuleRequestRequestTypeDef(BaseModel):
    OrganizationConfigRuleName: str

class DeleteOrganizationConformancePackRequestRequestTypeDef(BaseModel):
    OrganizationConformancePackName: str

class DeletePendingAggregationRequestRequestRequestTypeDef(BaseModel):
    RequesterAccountId: str
    RequesterAwsRegion: str

class DeleteRemediationConfigurationRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceType: Optional[str] = None

class RemediationExceptionResourceKeyTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None

class DeleteResourceConfigRequestRequestTypeDef(BaseModel):
    ResourceType: str
    ResourceId: str

class DeleteRetentionConfigurationRequestRequestTypeDef(BaseModel):
    RetentionConfigurationName: str

class DeleteStoredQueryRequestRequestTypeDef(BaseModel):
    QueryName: str

class DeliverConfigSnapshotRequestRequestTypeDef(BaseModel):
    deliveryChannelName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAggregationAuthorizationsRequestRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeComplianceByConfigRuleRequestRequestTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None

class DescribeComplianceByResourceRequestRequestTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConfigRuleEvaluationStatusRequestRequestTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConfigRulesFiltersTypeDef(BaseModel):
    EvaluationMode: Optional[EvaluationModeType] = None

class DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConfigurationAggregatorsRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConfigurationRecorderStatusRequestRequestTypeDef(BaseModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None

class DescribeConfigurationRecordersRequestRequestTypeDef(BaseModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None

class DescribeConformancePackStatusRequestRequestTypeDef(BaseModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConformancePacksRequestRequestTypeDef(BaseModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDeliveryChannelStatusRequestRequestTypeDef(BaseModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None

class DescribeDeliveryChannelsRequestRequestTypeDef(BaseModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None

class DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef(BaseModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class OrganizationConfigRuleStatusTypeDef(BaseModel):
    OrganizationConfigRuleName: str
    OrganizationRuleStatus: OrganizationRuleStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class DescribeOrganizationConfigRulesRequestRequestTypeDef(BaseModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeOrganizationConformancePackStatusesRequestRequestTypeDef(BaseModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class OrganizationConformancePackStatusTypeDef(BaseModel):
    OrganizationConformancePackName: str
    Status: OrganizationResourceStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class DescribeOrganizationConformancePacksRequestRequestTypeDef(BaseModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePendingAggregationRequestsRequestRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class PendingAggregationRequestTypeDef(BaseModel):
    RequesterAccountId: Optional[str] = None
    RequesterAwsRegion: Optional[str] = None

class DescribeRemediationConfigurationsRequestRequestTypeDef(BaseModel):
    ConfigRuleNames: Sequence[str]

class RemediationExceptionTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceType: str
    ResourceId: str
    Message: Optional[str] = None
    ExpirationTime: Optional[datetime] = None

class DescribeRetentionConfigurationsRequestRequestTypeDef(BaseModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class RetentionConfigurationTypeDef(BaseModel):
    Name: str
    RetentionPeriodInDays: int

class EvaluationContextTypeDef(BaseModel):
    EvaluationContextIdentifier: Optional[str] = None

class EvaluationOutputTypeDef(BaseModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: datetime
    Annotation: Optional[str] = None

class EvaluationResultQualifierTypeDef(BaseModel):
    ConfigRuleName: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    EvaluationMode: Optional[EvaluationModeType] = None

class EvaluationStatusTypeDef(BaseModel):
    Status: ResourceEvaluationStatusType
    FailureReason: Optional[str] = None

class ExclusionByResourceTypesOutputTypeDef(BaseModel):
    resourceTypes: Optional[List[ResourceTypeType]] = None

class ExclusionByResourceTypesTypeDef(BaseModel):
    resourceTypes: Optional[Sequence[ResourceTypeType]] = None

class SsmControlsTypeDef(BaseModel):
    ConcurrentExecutionRatePercentage: Optional[int] = None
    ErrorPercentage: Optional[int] = None

class FieldInfoTypeDef(BaseModel):
    Name: Optional[str] = None

class GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: Optional[ComplianceTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ResourceCountFiltersTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    AccountId: Optional[str] = None
    Region: Optional[str] = None

class GroupedResourceCountTypeDef(BaseModel):
    GroupName: str
    ResourceCount: int

class GetComplianceDetailsByConfigRuleRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetComplianceDetailsByResourceRequestRequestTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None
    ResourceEvaluationId: Optional[str] = None

class GetComplianceSummaryByResourceTypeRequestRequestTypeDef(BaseModel):
    ResourceTypes: Optional[Sequence[str]] = None

class GetConformancePackComplianceSummaryRequestRequestTypeDef(BaseModel):
    ConformancePackNames: Sequence[str]
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetCustomRulePolicyRequestRequestTypeDef(BaseModel):
    ConfigRuleName: Optional[str] = None

class GetDiscoveredResourceCountsRequestRequestTypeDef(BaseModel):
    resourceTypes: Optional[Sequence[str]] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ResourceCountTypeDef(BaseModel):
    resourceType: Optional[ResourceTypeType] = None
    count: Optional[int] = None

class StatusDetailFiltersTypeDef(BaseModel):
    AccountId: Optional[str] = None
    MemberAccountRuleStatus: Optional[MemberAccountRuleStatusType] = None

class MemberAccountStatusTypeDef(BaseModel):
    AccountId: str
    ConfigRuleName: str
    MemberAccountRuleStatus: MemberAccountRuleStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class OrganizationResourceDetailedStatusFiltersTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Status: Optional[OrganizationResourceDetailedStatusType] = None

class OrganizationConformancePackDetailedStatusTypeDef(BaseModel):
    AccountId: str
    ConformancePackName: str
    Status: OrganizationResourceDetailedStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class GetOrganizationCustomRulePolicyRequestRequestTypeDef(BaseModel):
    OrganizationConfigRuleName: str

class GetResourceEvaluationSummaryRequestRequestTypeDef(BaseModel):
    ResourceEvaluationId: str

class ResourceDetailsTypeDef(BaseModel):
    ResourceId: str
    ResourceType: str
    ResourceConfiguration: str
    ResourceConfigurationSchemaType: Optional[Literal["CFN_RESOURCE_SCHEMA"]] = None

class GetStoredQueryRequestRequestTypeDef(BaseModel):
    QueryName: str

class StoredQueryTypeDef(BaseModel):
    QueryName: str
    QueryId: Optional[str] = None
    QueryArn: Optional[str] = None
    Description: Optional[str] = None
    Expression: Optional[str] = None

class ResourceFiltersTypeDef(BaseModel):
    AccountId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceName: Optional[str] = None
    Region: Optional[str] = None

class ListDiscoveredResourcesRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    resourceIds: Optional[Sequence[str]] = None
    resourceName: Optional[str] = None
    limit: Optional[int] = None
    includeDeletedResources: Optional[bool] = None
    nextToken: Optional[str] = None

class ResourceIdentifierTypeDef(BaseModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    resourceDeletionTime: Optional[datetime] = None

class ResourceEvaluationTypeDef(BaseModel):
    ResourceEvaluationId: Optional[str] = None
    EvaluationMode: Optional[EvaluationModeType] = None
    EvaluationStartTimestamp: Optional[datetime] = None

class ListStoredQueriesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StoredQueryMetadataTypeDef(BaseModel):
    QueryId: str
    QueryArn: str
    QueryName: str
    Description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class OrganizationAggregationSourceExtraOutputTypeDef(BaseModel):
    RoleArn: str
    AwsRegions: Optional[List[str]] = None
    AllAwsRegions: Optional[bool] = None

class OrganizationAggregationSourceTypeDef(BaseModel):
    RoleArn: str
    AwsRegions: Optional[Sequence[str]] = None
    AllAwsRegions: Optional[bool] = None

class OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef(BaseModel):
    Description: Optional[str] = None
    OrganizationConfigRuleTriggerTypes: Optional[       List[OrganizationConfigRuleTriggerTypeNoSNType]     ] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None
    PolicyRuntime: Optional[str] = None
    DebugLogDeliveryAccounts: Optional[List[str]] = None

class OrganizationCustomRuleMetadataOutputTypeDef(BaseModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: List[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationManagedRuleMetadataOutputTypeDef(BaseModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationCustomPolicyRuleMetadataTypeDef(BaseModel):
    PolicyRuntime: str
    PolicyText: str
    Description: Optional[str] = None
    OrganizationConfigRuleTriggerTypes: Optional[       Sequence[OrganizationConfigRuleTriggerTypeNoSNType]     ] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None
    DebugLogDeliveryAccounts: Optional[Sequence[str]] = None

class OrganizationCustomRuleMetadataExtraOutputTypeDef(BaseModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: List[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationCustomRuleMetadataTypeDef(BaseModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: Sequence[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationManagedRuleMetadataExtraOutputTypeDef(BaseModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationManagedRuleMetadataTypeDef(BaseModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class PutResourceConfigRequestRequestTypeDef(BaseModel):
    ResourceType: str
    SchemaVersionId: str
    ResourceId: str
    Configuration: str
    ResourceName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class PutRetentionConfigurationRequestRequestTypeDef(BaseModel):
    RetentionPeriodInDays: int

class RecordingStrategyTypeDef(BaseModel):
    useOnly: Optional[RecordingStrategyTypeType] = None

class RecordingModeOverrideOutputTypeDef(BaseModel):
    resourceTypes: List[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: Optional[str] = None

class RecordingModeOverrideTypeDef(BaseModel):
    resourceTypes: Sequence[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: Optional[str] = None

class RemediationExecutionStepTypeDef(BaseModel):
    Name: Optional[str] = None
    State: Optional[RemediationExecutionStepStateType] = None
    ErrorMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None

class ResourceValueTypeDef(BaseModel):
    Value: Literal["RESOURCE_ID"]

class StaticValueOutputTypeDef(BaseModel):
    Values: List[str]

class StaticValueTypeDef(BaseModel):
    Values: Sequence[str]

class SelectAggregateResourceConfigRequestRequestTypeDef(BaseModel):
    Expression: str
    ConfigurationAggregatorName: str
    Limit: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SelectResourceConfigRequestRequestTypeDef(BaseModel):
    Expression: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class SourceDetailTypeDef(BaseModel):
    EventSource: Optional[Literal["aws.config"]] = None
    MessageType: Optional[MessageTypeType] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None

class StartConfigRulesEvaluationRequestRequestTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None

class StartConfigurationRecorderRequestRequestTypeDef(BaseModel):
    ConfigurationRecorderName: str

class StopConfigurationRecorderRequestRequestTypeDef(BaseModel):
    ConfigurationRecorderName: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AggregateComplianceByConformancePackTypeDef(BaseModel):
    ConformancePackName: Optional[str] = None
    Compliance: Optional[AggregateConformancePackComplianceTypeDef] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class AggregateConformancePackComplianceSummaryTypeDef(BaseModel):
    ComplianceSummary: Optional[AggregateConformancePackComplianceCountTypeDef] = None
    GroupName: Optional[str] = None

class DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceSummaryFiltersTypeDef] = None
    GroupByKey: Optional[AggregateConformancePackComplianceSummaryGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class BatchGetAggregateResourceConfigRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    ResourceIdentifiers: Sequence[AggregateResourceIdentifierTypeDef]

class GetAggregateResourceConfigRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    ResourceIdentifier: AggregateResourceIdentifierTypeDef

class BatchGetAggregateResourceConfigResponseTypeDef(BaseModel):
    BaseConfigurationItems: List[BaseConfigurationItemTypeDef]
    UnprocessedResourceIdentifiers: List[AggregateResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeliverConfigSnapshotResponseTypeDef(BaseModel):
    configSnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAggregationAuthorizationsResponseTypeDef(BaseModel):
    AggregationAuthorizations: List[AggregationAuthorizationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConfigurationAggregatorSourcesStatusResponseTypeDef(BaseModel):
    AggregatedSourceStatusList: List[AggregatedSourceStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomRulePolicyResponseTypeDef(BaseModel):
    PolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationCustomRulePolicyResponseTypeDef(BaseModel):
    PolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregateDiscoveredResourcesResponseTypeDef(BaseModel):
    ResourceIdentifiers: List[AggregateResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutAggregationAuthorizationResponseTypeDef(BaseModel):
    AggregationAuthorization: AggregationAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConformancePackResponseTypeDef(BaseModel):
    ConformancePackArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutOrganizationConfigRuleResponseTypeDef(BaseModel):
    OrganizationConfigRuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutOrganizationConformancePackResponseTypeDef(BaseModel):
    OrganizationConformancePackArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutStoredQueryResponseTypeDef(BaseModel):
    QueryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceEvaluationResponseTypeDef(BaseModel):
    ResourceEvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetResourceConfigRequestRequestTypeDef(BaseModel):
    resourceKeys: Sequence[ResourceKeyTypeDef]

class BatchGetResourceConfigResponseTypeDef(BaseModel):
    baseConfigurationItems: List[BaseConfigurationItemTypeDef]
    unprocessedResourceKeys: List[ResourceKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRemediationExecutionStatusRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKeyTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class StartRemediationExecutionRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[ResourceKeyTypeDef]

class StartRemediationExecutionResponseTypeDef(BaseModel):
    FailureMessage: str
    FailedItems: List[ResourceKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ComplianceSummaryTypeDef(BaseModel):
    CompliantResourceCount: Optional[ComplianceContributorCountTypeDef] = None
    NonCompliantResourceCount: Optional[ComplianceContributorCountTypeDef] = None
    ComplianceSummaryTimestamp: Optional[datetime] = None

class ComplianceTypeDef(BaseModel):
    ComplianceType: Optional[ComplianceTypeType] = None
    ComplianceContributorCount: Optional[ComplianceContributorCountTypeDef] = None

class DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceSummaryFiltersTypeDef] = None
    GroupByKey: Optional[ConfigRuleComplianceSummaryGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConfigRuleEvaluationStatusResponseTypeDef(BaseModel):
    ConfigRulesEvaluationStatus: List[ConfigRuleEvaluationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeliveryChannelTypeDef(BaseModel):
    name: Optional[str] = None
    s3BucketName: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    s3KmsKeyArn: Optional[str] = None
    snsTopicARN: Optional[str] = None
    configSnapshotDeliveryProperties: Optional[ConfigSnapshotDeliveryPropertiesTypeDef] = None

class DeliveryChannelStatusTypeDef(BaseModel):
    name: Optional[str] = None
    configSnapshotDeliveryInfo: Optional[ConfigExportDeliveryInfoTypeDef] = None
    configHistoryDeliveryInfo: Optional[ConfigExportDeliveryInfoTypeDef] = None
    configStreamDeliveryInfo: Optional[ConfigStreamDeliveryInfoTypeDef] = None

class ConfigurationAggregatorTypeDef(BaseModel):
    ConfigurationAggregatorName: Optional[str] = None
    ConfigurationAggregatorArn: Optional[str] = None
    AccountAggregationSources: Optional[List[AccountAggregationSourceOutputTypeDef]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceOutputTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None

class ConfigurationItemTypeDef(BaseModel):
    version: Optional[str] = None
    accountId: Optional[str] = None
    configurationItemCaptureTime: Optional[datetime] = None
    configurationItemStatus: Optional[ConfigurationItemStatusType] = None
    configurationStateId: Optional[str] = None
    configurationItemMD5Hash: Optional[str] = None
    arn: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    awsRegion: Optional[str] = None
    availabilityZone: Optional[str] = None
    resourceCreationTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    relatedEvents: Optional[List[str]] = None
    relationships: Optional[List[RelationshipTypeDef]] = None
    configuration: Optional[str] = None
    supplementaryConfiguration: Optional[Dict[str, str]] = None
    recordingFrequency: Optional[RecordingFrequencyType] = None
    configurationItemDeliveryTime: Optional[datetime] = None

class DescribeConfigurationRecorderStatusResponseTypeDef(BaseModel):
    ConfigurationRecordersStatus: List[ConfigurationRecorderStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConformancePackComplianceRequestRequestTypeDef(BaseModel):
    ConformancePackName: str
    Filters: Optional[ConformancePackComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListConformancePackComplianceScoresResponseTypeDef(BaseModel):
    ConformancePackComplianceScores: List[ConformancePackComplianceScoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListConformancePackComplianceScoresRequestRequestTypeDef(BaseModel):
    Filters: Optional[ConformancePackComplianceScoresFiltersTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal["SCORE"]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetConformancePackComplianceSummaryResponseTypeDef(BaseModel):
    ConformancePackComplianceSummaryList: List[ConformancePackComplianceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OrganizationConformancePackTypeDef(BaseModel):
    OrganizationConformancePackName: str
    OrganizationConformancePackArn: str
    LastUpdateTime: datetime
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[List[ConformancePackInputParameterTypeDef]] = None
    ExcludedAccounts: Optional[List[str]] = None

class PutOrganizationConformancePackRequestRequestTypeDef(BaseModel):
    OrganizationConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[       Sequence[ConformancePackInputParameterTypeDef]     ] = None
    ExcludedAccounts: Optional[Sequence[str]] = None

class ConformancePackDetailTypeDef(BaseModel):
    ConformancePackName: str
    ConformancePackArn: str
    ConformancePackId: str
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[List[ConformancePackInputParameterTypeDef]] = None
    LastUpdateRequestedTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    TemplateSSMDocumentDetails: Optional[TemplateSSMDocumentDetailsTypeDef] = None

class PutConformancePackRequestRequestTypeDef(BaseModel):
    ConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[       Sequence[ConformancePackInputParameterTypeDef]     ] = None
    TemplateSSMDocumentDetails: Optional[TemplateSSMDocumentDetailsTypeDef] = None

class GetConformancePackComplianceDetailsRequestRequestTypeDef(BaseModel):
    ConformancePackName: str
    Filters: Optional[ConformancePackEvaluationFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConformancePackComplianceResponseTypeDef(BaseModel):
    ConformancePackName: str
    ConformancePackRuleComplianceList: List[ConformancePackRuleComplianceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConformancePackStatusResponseTypeDef(BaseModel):
    ConformancePackStatusDetails: List[ConformancePackStatusDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeleteRemediationExceptionsRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKeyTypeDef]

class DescribeRemediationExceptionsRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[RemediationExceptionResourceKeyTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class FailedDeleteRemediationExceptionsBatchTypeDef(BaseModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationExceptionResourceKeyTypeDef]] = None

class DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef(BaseModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef(BaseModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef(BaseModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef(BaseModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef(BaseModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef(BaseModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef(BaseModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKeyTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef(BaseModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: Optional[ComplianceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef(BaseModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    ResourceEvaluationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef(BaseModel):
    ConformancePackNames: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef(BaseModel):
    resourceType: ResourceTypeType
    resourceIds: Optional[Sequence[str]] = None
    resourceName: Optional[str] = None
    includeDeletedResources: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef(BaseModel):
    Expression: str
    ConfigurationAggregatorName: str
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SelectResourceConfigRequestSelectResourceConfigPaginateTypeDef(BaseModel):
    Expression: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    Filters: Optional[DescribeConfigRulesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigRulesRequestRequestTypeDef(BaseModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Filters: Optional[DescribeConfigRulesFiltersTypeDef] = None

class DescribeOrganizationConfigRuleStatusesResponseTypeDef(BaseModel):
    OrganizationConfigRuleStatuses: List[OrganizationConfigRuleStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOrganizationConformancePackStatusesResponseTypeDef(BaseModel):
    OrganizationConformancePackStatuses: List[OrganizationConformancePackStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePendingAggregationRequestsResponseTypeDef(BaseModel):
    PendingAggregationRequests: List[PendingAggregationRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRemediationExceptionsResponseTypeDef(BaseModel):
    RemediationExceptions: List[RemediationExceptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailedRemediationExceptionBatchTypeDef(BaseModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationExceptionTypeDef]] = None

class DescribeRetentionConfigurationsResponseTypeDef(BaseModel):
    RetentionConfigurations: List[RetentionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutRetentionConfigurationResponseTypeDef(BaseModel):
    RetentionConfiguration: RetentionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEvaluationsResponseTypeDef(BaseModel):
    FailedEvaluations: List[EvaluationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationResultIdentifierTypeDef(BaseModel):
    EvaluationResultQualifier: Optional[EvaluationResultQualifierTypeDef] = None
    OrderingTimestamp: Optional[datetime] = None
    ResourceEvaluationId: Optional[str] = None

class EvaluationTypeDef(BaseModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: TimestampTypeDef
    Annotation: Optional[str] = None

class ExternalEvaluationTypeDef(BaseModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: TimestampTypeDef
    Annotation: Optional[str] = None

class GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef(BaseModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[TimestampTypeDef] = None
    earlierTime: Optional[TimestampTypeDef] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceConfigHistoryRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[TimestampTypeDef] = None
    earlierTime: Optional[TimestampTypeDef] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class PutRemediationExceptionsRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKeyTypeDef]
    Message: Optional[str] = None
    ExpirationTime: Optional[TimestampTypeDef] = None

class TimeWindowTypeDef(BaseModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None

class ExecutionControlsTypeDef(BaseModel):
    SsmControls: Optional[SsmControlsTypeDef] = None

class QueryInfoTypeDef(BaseModel):
    SelectFields: Optional[List[FieldInfoTypeDef]] = None

class GetAggregateDiscoveredResourceCountsRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ResourceCountFiltersTypeDef] = None
    GroupByKey: Optional[ResourceCountGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetAggregateDiscoveredResourceCountsResponseTypeDef(BaseModel):
    TotalDiscoveredResources: int
    GroupByKey: str
    GroupedResourceCounts: List[GroupedResourceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDiscoveredResourceCountsResponseTypeDef(BaseModel):
    totalDiscoveredResources: int
    resourceCounts: List[ResourceCountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef(BaseModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef(BaseModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetOrganizationConfigRuleDetailedStatusResponseTypeDef(BaseModel):
    OrganizationConfigRuleDetailedStatus: List[MemberAccountStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef(BaseModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef(BaseModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetOrganizationConformancePackDetailedStatusResponseTypeDef(BaseModel):
    OrganizationConformancePackDetailedStatuses: List[       OrganizationConformancePackDetailedStatusTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetResourceEvaluationSummaryResponseTypeDef(BaseModel):
    ResourceEvaluationId: str
    EvaluationMode: EvaluationModeType
    EvaluationStatus: EvaluationStatusTypeDef
    EvaluationStartTimestamp: datetime
    Compliance: ComplianceTypeType
    EvaluationContext: EvaluationContextTypeDef
    ResourceDetails: ResourceDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceEvaluationRequestRequestTypeDef(BaseModel):
    ResourceDetails: ResourceDetailsTypeDef
    EvaluationMode: EvaluationModeType
    EvaluationContext: Optional[EvaluationContextTypeDef] = None
    EvaluationTimeout: Optional[int] = None
    ClientToken: Optional[str] = None

class GetStoredQueryResponseTypeDef(BaseModel):
    StoredQuery: StoredQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAggregateDiscoveredResourcesRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListDiscoveredResourcesResponseTypeDef(BaseModel):
    resourceIdentifiers: List[ResourceIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceEvaluationsResponseTypeDef(BaseModel):
    ResourceEvaluations: List[ResourceEvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStoredQueriesResponseTypeDef(BaseModel):
    StoredQueryMetadata: List[StoredQueryMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutAggregationAuthorizationRequestRequestTypeDef(BaseModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class PutStoredQueryRequestRequestTypeDef(BaseModel):
    StoredQuery: StoredQueryTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class OrganizationConfigRuleTypeDef(BaseModel):
    OrganizationConfigRuleName: str
    OrganizationConfigRuleArn: str
    OrganizationManagedRuleMetadata: Optional[       OrganizationManagedRuleMetadataOutputTypeDef     ] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataOutputTypeDef] = None
    ExcludedAccounts: Optional[List[str]] = None
    LastUpdateTime: Optional[datetime] = None
    OrganizationCustomPolicyRuleMetadata: Optional[       OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef     ] = None

class PutOrganizationConfigRuleRequestRequestTypeDef(BaseModel):
    OrganizationConfigRuleName: str
    OrganizationManagedRuleMetadata: Optional[OrganizationManagedRuleMetadataTypeDef] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataTypeDef] = None
    ExcludedAccounts: Optional[Sequence[str]] = None
    OrganizationCustomPolicyRuleMetadata: Optional[       OrganizationCustomPolicyRuleMetadataTypeDef     ] = None

class RecordingGroupOutputTypeDef(BaseModel):
    allSupported: Optional[bool] = None
    includeGlobalResourceTypes: Optional[bool] = None
    resourceTypes: Optional[List[ResourceTypeType]] = None
    exclusionByResourceTypes: Optional[ExclusionByResourceTypesOutputTypeDef] = None
    recordingStrategy: Optional[RecordingStrategyTypeDef] = None

class RecordingGroupTypeDef(BaseModel):
    allSupported: Optional[bool] = None
    includeGlobalResourceTypes: Optional[bool] = None
    resourceTypes: Optional[Sequence[ResourceTypeType]] = None
    exclusionByResourceTypes: Optional[ExclusionByResourceTypesTypeDef] = None
    recordingStrategy: Optional[RecordingStrategyTypeDef] = None

class RecordingModeOutputTypeDef(BaseModel):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: Optional[List[RecordingModeOverrideOutputTypeDef]] = None

class RecordingModeTypeDef(BaseModel):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: Optional[Sequence[RecordingModeOverrideTypeDef]] = None

class RemediationExecutionStatusTypeDef(BaseModel):
    ResourceKey: Optional[ResourceKeyTypeDef] = None
    State: Optional[RemediationExecutionStateType] = None
    StepDetails: Optional[List[RemediationExecutionStepTypeDef]] = None
    InvocationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class RemediationParameterValueOutputTypeDef(BaseModel):
    ResourceValue: Optional[ResourceValueTypeDef] = None
    StaticValue: Optional[StaticValueOutputTypeDef] = None

class RemediationParameterValueTypeDef(BaseModel):
    ResourceValue: Optional[ResourceValueTypeDef] = None
    StaticValue: Optional[StaticValueTypeDef] = None

class SourceExtraOutputTypeDef(BaseModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[List[SourceDetailTypeDef]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetailsTypeDef] = None

class SourceOutputTypeDef(BaseModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[List[SourceDetailTypeDef]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetailsTypeDef] = None

class SourceTypeDef(BaseModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[Sequence[SourceDetailTypeDef]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetailsTypeDef] = None

class PutConfigurationAggregatorRequestRequestTypeDef(BaseModel):
    ConfigurationAggregatorName: str
    AccountAggregationSources: Optional[Sequence[AccountAggregationSourceUnionTypeDef]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeAggregateComplianceByConformancePacksResponseTypeDef(BaseModel):
    AggregateComplianceByConformancePacks: List[AggregateComplianceByConformancePackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetAggregateConformancePackComplianceSummaryResponseTypeDef(BaseModel):
    AggregateConformancePackComplianceSummaries: List[       AggregateConformancePackComplianceSummaryTypeDef     ]
    GroupByKey: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AggregateComplianceCountTypeDef(BaseModel):
    GroupName: Optional[str] = None
    ComplianceSummary: Optional[ComplianceSummaryTypeDef] = None

class ComplianceSummaryByResourceTypeTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ComplianceSummary: Optional[ComplianceSummaryTypeDef] = None

class GetComplianceSummaryByConfigRuleResponseTypeDef(BaseModel):
    ComplianceSummary: ComplianceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AggregateComplianceByConfigRuleTypeDef(BaseModel):
    ConfigRuleName: Optional[str] = None
    Compliance: Optional[ComplianceTypeDef] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ComplianceByConfigRuleTypeDef(BaseModel):
    ConfigRuleName: Optional[str] = None
    Compliance: Optional[ComplianceTypeDef] = None

class ComplianceByResourceTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Compliance: Optional[ComplianceTypeDef] = None

class DescribeDeliveryChannelsResponseTypeDef(BaseModel):
    DeliveryChannels: List[DeliveryChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryChannelRequestRequestTypeDef(BaseModel):
    DeliveryChannel: DeliveryChannelTypeDef

class DescribeDeliveryChannelStatusResponseTypeDef(BaseModel):
    DeliveryChannelsStatus: List[DeliveryChannelStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationAggregatorsResponseTypeDef(BaseModel):
    ConfigurationAggregators: List[ConfigurationAggregatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutConfigurationAggregatorResponseTypeDef(BaseModel):
    ConfigurationAggregator: ConfigurationAggregatorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAggregateResourceConfigResponseTypeDef(BaseModel):
    ConfigurationItem: ConfigurationItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceConfigHistoryResponseTypeDef(BaseModel):
    configurationItems: List[ConfigurationItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConformancePacksResponseTypeDef(BaseModel):
    OrganizationConformancePacks: List[OrganizationConformancePackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConformancePacksResponseTypeDef(BaseModel):
    ConformancePackDetails: List[ConformancePackDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeleteRemediationExceptionsResponseTypeDef(BaseModel):
    FailedBatches: List[FailedDeleteRemediationExceptionsBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRemediationExceptionsResponseTypeDef(BaseModel):
    FailedBatches: List[FailedRemediationExceptionBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AggregateEvaluationResultTypeDef(BaseModel):
    EvaluationResultIdentifier: Optional[EvaluationResultIdentifierTypeDef] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    ResultRecordedTime: Optional[datetime] = None
    ConfigRuleInvokedTime: Optional[datetime] = None
    Annotation: Optional[str] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ConformancePackEvaluationResultTypeDef(BaseModel):
    ComplianceType: ConformancePackComplianceTypeType
    EvaluationResultIdentifier: EvaluationResultIdentifierTypeDef
    ConfigRuleInvokedTime: datetime
    ResultRecordedTime: datetime
    Annotation: Optional[str] = None

class EvaluationResultTypeDef(BaseModel):
    EvaluationResultIdentifier: Optional[EvaluationResultIdentifierTypeDef] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    ResultRecordedTime: Optional[datetime] = None
    ConfigRuleInvokedTime: Optional[datetime] = None
    Annotation: Optional[str] = None
    ResultToken: Optional[str] = None

class PutExternalEvaluationRequestRequestTypeDef(BaseModel):
    ConfigRuleName: str
    ExternalEvaluation: ExternalEvaluationTypeDef

class ResourceEvaluationFiltersTypeDef(BaseModel):
    EvaluationMode: Optional[EvaluationModeType] = None
    TimeWindow: Optional[TimeWindowTypeDef] = None
    EvaluationContextIdentifier: Optional[str] = None

class SelectAggregateResourceConfigResponseTypeDef(BaseModel):
    Results: List[str]
    QueryInfo: QueryInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SelectResourceConfigResponseTypeDef(BaseModel):
    Results: List[str]
    QueryInfo: QueryInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOrganizationConfigRulesResponseTypeDef(BaseModel):
    OrganizationConfigRules: List[OrganizationConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ConfigurationRecorderOutputTypeDef(BaseModel):
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroupOutputTypeDef] = None
    recordingMode: Optional[RecordingModeOutputTypeDef] = None

class ConfigurationRecorderTypeDef(BaseModel):
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroupTypeDef] = None
    recordingMode: Optional[RecordingModeTypeDef] = None

class DescribeRemediationExecutionStatusResponseTypeDef(BaseModel):
    RemediationExecutionStatuses: List[RemediationExecutionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RemediationConfigurationOutputTypeDef(BaseModel):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str
    TargetVersion: Optional[str] = None
    Parameters: Optional[Dict[str, RemediationParameterValueOutputTypeDef]] = None
    ResourceType: Optional[str] = None
    Automatic: Optional[bool] = None
    ExecutionControls: Optional[ExecutionControlsTypeDef] = None
    MaximumAutomaticAttempts: Optional[int] = None
    RetryAttemptSeconds: Optional[int] = None
    Arn: Optional[str] = None
    CreatedByService: Optional[str] = None

class RemediationConfigurationTypeDef(BaseModel):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str
    TargetVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, RemediationParameterValueTypeDef]] = None
    ResourceType: Optional[str] = None
    Automatic: Optional[bool] = None
    ExecutionControls: Optional[ExecutionControlsTypeDef] = None
    MaximumAutomaticAttempts: Optional[int] = None
    RetryAttemptSeconds: Optional[int] = None
    Arn: Optional[str] = None
    CreatedByService: Optional[str] = None

class ConfigRuleExtraOutputTypeDef(BaseModel):
    Source: SourceExtraOutputTypeDef
    ConfigRuleName: Optional[str] = None
    ConfigRuleArn: Optional[str] = None
    ConfigRuleId: Optional[str] = None
    Description: Optional[str] = None
    Scope: Optional[ScopeExtraOutputTypeDef] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ConfigRuleState: Optional[ConfigRuleStateType] = None
    CreatedBy: Optional[str] = None
    EvaluationModes: Optional[List[EvaluationModeConfigurationTypeDef]] = None

class ConfigRuleOutputTypeDef(BaseModel):
    Source: SourceOutputTypeDef
    ConfigRuleName: Optional[str] = None
    ConfigRuleArn: Optional[str] = None
    ConfigRuleId: Optional[str] = None
    Description: Optional[str] = None
    Scope: Optional[ScopeOutputTypeDef] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ConfigRuleState: Optional[ConfigRuleStateType] = None
    CreatedBy: Optional[str] = None
    EvaluationModes: Optional[List[EvaluationModeConfigurationTypeDef]] = None

class ConfigRuleTypeDef(BaseModel):
    Source: SourceTypeDef
    ConfigRuleName: Optional[str] = None
    ConfigRuleArn: Optional[str] = None
    ConfigRuleId: Optional[str] = None
    Description: Optional[str] = None
    Scope: Optional[ScopeTypeDef] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ConfigRuleState: Optional[ConfigRuleStateType] = None
    CreatedBy: Optional[str] = None
    EvaluationModes: Optional[Sequence[EvaluationModeConfigurationTypeDef]] = None

class GetAggregateConfigRuleComplianceSummaryResponseTypeDef(BaseModel):
    GroupByKey: str
    AggregateComplianceCounts: List[AggregateComplianceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComplianceSummaryByResourceTypeResponseTypeDef(BaseModel):
    ComplianceSummariesByResourceType: List[ComplianceSummaryByResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAggregateComplianceByConfigRulesResponseTypeDef(BaseModel):
    AggregateComplianceByConfigRules: List[AggregateComplianceByConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeComplianceByConfigRuleResponseTypeDef(BaseModel):
    ComplianceByConfigRules: List[ComplianceByConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeComplianceByResourceResponseTypeDef(BaseModel):
    ComplianceByResources: List[ComplianceByResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetAggregateComplianceDetailsByConfigRuleResponseTypeDef(BaseModel):
    AggregateEvaluationResults: List[AggregateEvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetConformancePackComplianceDetailsResponseTypeDef(BaseModel):
    ConformancePackName: str
    ConformancePackRuleEvaluationResults: List[ConformancePackEvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComplianceDetailsByConfigRuleResponseTypeDef(BaseModel):
    EvaluationResults: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComplianceDetailsByResourceResponseTypeDef(BaseModel):
    EvaluationResults: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutEvaluationsRequestRequestTypeDef(BaseModel):
    ResultToken: str
    Evaluations: Optional[Sequence[EvaluationUnionTypeDef]] = None
    TestMode: Optional[bool] = None

class ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef(BaseModel):
    Filters: Optional[ResourceEvaluationFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceEvaluationsRequestRequestTypeDef(BaseModel):
    Filters: Optional[ResourceEvaluationFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConfigurationRecordersResponseTypeDef(BaseModel):
    ConfigurationRecorders: List[ConfigurationRecorderOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigurationRecorderRequestRequestTypeDef(BaseModel):
    ConfigurationRecorder: ConfigurationRecorderTypeDef

class DescribeRemediationConfigurationsResponseTypeDef(BaseModel):
    RemediationConfigurations: List[RemediationConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FailedRemediationBatchTypeDef(BaseModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationConfigurationOutputTypeDef]] = None

class DescribeConfigRulesResponseTypeDef(BaseModel):
    ConfigRules: List[ConfigRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutConfigRuleRequestRequestTypeDef(BaseModel):
    ConfigRule: ConfigRuleTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class PutRemediationConfigurationsResponseTypeDef(BaseModel):
    FailedBatches: List[FailedRemediationBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRemediationConfigurationsRequestRequestTypeDef(BaseModel):
    RemediationConfigurations: Sequence[RemediationConfigurationUnionTypeDef]

