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
from aws_resource_validator.pydantic_models.config_constants import *

class AccountAggregationSourceExtraOutputTypeDef(BaseValidatorModel):
    AccountIds: List[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[List[str]] = None

class AccountAggregationSourceOutputTypeDef(BaseValidatorModel):
    AccountIds: List[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[List[str]] = None

class AccountAggregationSourceTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[Sequence[str]] = None

class AggregateConformancePackComplianceTypeDef(BaseValidatorModel):
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    CompliantRuleCount: Optional[int] = None
    NonCompliantRuleCount: Optional[int] = None
    TotalRuleCount: Optional[int] = None

class AggregateConformancePackComplianceCountTypeDef(BaseValidatorModel):
    CompliantConformancePackCount: Optional[int] = None
    NonCompliantConformancePackCount: Optional[int] = None

class AggregateConformancePackComplianceFiltersTypeDef(BaseValidatorModel):
    ConformancePackName: Optional[str] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class AggregateConformancePackComplianceSummaryFiltersTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class AggregateResourceIdentifierTypeDef(BaseValidatorModel):
    SourceAccountId: str
    SourceRegion: str
    ResourceId: str
    ResourceType: ResourceTypeType
    ResourceName: Optional[str] = None

class AggregatedSourceStatusTypeDef(BaseValidatorModel):
    SourceId: Optional[str] = None
    SourceType: Optional[AggregatedSourceTypeType] = None
    AwsRegion: Optional[str] = None
    LastUpdateStatus: Optional[AggregatedSourceStatusTypeType] = None
    LastUpdateTime: Optional[datetime] = None
    LastErrorCode: Optional[str] = None
    LastErrorMessage: Optional[str] = None

class AggregationAuthorizationTypeDef(BaseValidatorModel):
    AggregationAuthorizationArn: Optional[str] = None
    AuthorizedAccountId: Optional[str] = None
    AuthorizedAwsRegion: Optional[str] = None
    CreationTime: Optional[datetime] = None

class BaseConfigurationItemTypeDef(BaseValidatorModel):
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ResourceKeyTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str

class ComplianceContributorCountTypeDef(BaseValidatorModel):
    CappedCount: Optional[int] = None
    CapExceeded: Optional[bool] = None

class ConfigExportDeliveryInfoTypeDef(BaseValidatorModel):
    lastStatus: Optional[DeliveryStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastAttemptTime: Optional[datetime] = None
    lastSuccessfulTime: Optional[datetime] = None
    nextDeliveryTime: Optional[datetime] = None

class ConfigRuleComplianceFiltersTypeDef(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ConfigRuleComplianceSummaryFiltersTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ConfigRuleEvaluationStatusTypeDef(BaseValidatorModel):
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

class EvaluationModeConfigurationTypeDef(BaseValidatorModel):
    Mode: Optional[EvaluationModeType] = None

class ScopeExtraOutputTypeDef(BaseValidatorModel):
    ComplianceResourceTypes: Optional[List[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None

class ScopeOutputTypeDef(BaseValidatorModel):
    ComplianceResourceTypes: Optional[List[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None

class ScopeTypeDef(BaseValidatorModel):
    ComplianceResourceTypes: Optional[Sequence[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None

class ConfigSnapshotDeliveryPropertiesTypeDef(BaseValidatorModel):
    deliveryFrequency: Optional[MaximumExecutionFrequencyType] = None

class ConfigStreamDeliveryInfoTypeDef(BaseValidatorModel):
    lastStatus: Optional[DeliveryStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastStatusChangeTime: Optional[datetime] = None

class OrganizationAggregationSourceOutputTypeDef(BaseValidatorModel):
    RoleArn: str
    AwsRegions: Optional[List[str]] = None
    AllAwsRegions: Optional[bool] = None

class RelationshipTypeDef(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    relationshipName: Optional[str] = None

class ConfigurationRecorderStatusTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    lastStartTime: Optional[datetime] = None
    lastStopTime: Optional[datetime] = None
    recording: Optional[bool] = None
    lastStatus: Optional[RecorderStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastStatusChangeTime: Optional[datetime] = None

class ConformancePackComplianceFiltersTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None

class ConformancePackComplianceScoreTypeDef(BaseValidatorModel):
    Score: Optional[str] = None
    ConformancePackName: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None

class ConformancePackComplianceScoresFiltersTypeDef(BaseValidatorModel):
    ConformancePackNames: Sequence[str]

class ConformancePackComplianceSummaryTypeDef(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackComplianceStatus: ConformancePackComplianceTypeType

class ConformancePackInputParameterTypeDef(BaseValidatorModel):
    ParameterName: str
    ParameterValue: str

class TemplateSSMDocumentDetailsTypeDef(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None

class ConformancePackEvaluationFiltersTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    ResourceType: Optional[str] = None
    ResourceIds: Optional[Sequence[str]] = None

class ConformancePackRuleComplianceTypeDef(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    Controls: Optional[List[str]] = None

class ConformancePackStatusDetailTypeDef(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackId: str
    ConformancePackArn: str
    ConformancePackState: ConformancePackStateType
    StackArn: str
    LastUpdateRequestedTime: datetime
    ConformancePackStatusReason: Optional[str] = None
    LastUpdateCompletedTime: Optional[datetime] = None

class CustomPolicyDetailsTypeDef(BaseValidatorModel):
    PolicyRuntime: str
    PolicyText: str
    EnableDebugLogDelivery: Optional[bool] = None

class DeleteAggregationAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str

class DeleteConfigRuleRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str

class DeleteConfigurationAggregatorRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str

class DeleteConfigurationRecorderRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderName: str

class DeleteConformancePackRequestRequestTypeDef(BaseValidatorModel):
    ConformancePackName: str

class DeleteDeliveryChannelRequestRequestTypeDef(BaseValidatorModel):
    DeliveryChannelName: str

class DeleteEvaluationResultsRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str

class DeleteOrganizationConfigRuleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str

class DeleteOrganizationConformancePackRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str

class DeletePendingAggregationRequestRequestRequestTypeDef(BaseValidatorModel):
    RequesterAccountId: str
    RequesterAwsRegion: str

class DeleteRemediationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceType: Optional[str] = None

class RemediationExceptionResourceKeyTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None

class DeleteResourceConfigRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: str
    ResourceId: str

class DeleteRetentionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    RetentionConfigurationName: str

class DeleteStoredQueryRequestRequestTypeDef(BaseValidatorModel):
    QueryName: str

class DeliverConfigSnapshotRequestRequestTypeDef(BaseValidatorModel):
    deliveryChannelName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAggregationAuthorizationsRequestRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeComplianceByConfigRuleRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None

class DescribeComplianceByResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConfigRuleEvaluationStatusRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConfigRulesFiltersTypeDef(BaseValidatorModel):
    EvaluationMode: Optional[EvaluationModeType] = None

class DescribeConfigurationAggregatorSourcesStatusRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConfigurationAggregatorsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConfigurationRecorderStatusRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None

class DescribeConfigurationRecordersRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None

class DescribeConformancePackStatusRequestRequestTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConformancePacksRequestRequestTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDeliveryChannelStatusRequestRequestTypeDef(BaseValidatorModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None

class DescribeDeliveryChannelsRequestRequestTypeDef(BaseValidatorModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None

class DescribeOrganizationConfigRuleStatusesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class OrganizationConfigRuleStatusTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationRuleStatus: OrganizationRuleStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class DescribeOrganizationConfigRulesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeOrganizationConformancePackStatusesRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class OrganizationConformancePackStatusTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    Status: OrganizationResourceStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class DescribeOrganizationConformancePacksRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribePendingAggregationRequestsRequestRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class PendingAggregationRequestTypeDef(BaseValidatorModel):
    RequesterAccountId: Optional[str] = None
    RequesterAwsRegion: Optional[str] = None

class DescribeRemediationConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Sequence[str]

class RemediationExceptionTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceType: str
    ResourceId: str
    Message: Optional[str] = None
    ExpirationTime: Optional[datetime] = None

class DescribeRetentionConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class RetentionConfigurationTypeDef(BaseValidatorModel):
    Name: str
    RetentionPeriodInDays: int

class EvaluationContextTypeDef(BaseValidatorModel):
    EvaluationContextIdentifier: Optional[str] = None

class EvaluationOutputTypeDef(BaseValidatorModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: datetime
    Annotation: Optional[str] = None

class EvaluationResultQualifierTypeDef(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    EvaluationMode: Optional[EvaluationModeType] = None

class EvaluationStatusTypeDef(BaseValidatorModel):
    Status: ResourceEvaluationStatusType
    FailureReason: Optional[str] = None

class ExclusionByResourceTypesOutputTypeDef(BaseValidatorModel):
    resourceTypes: Optional[List[ResourceTypeType]] = None

class ExclusionByResourceTypesTypeDef(BaseValidatorModel):
    resourceTypes: Optional[Sequence[ResourceTypeType]] = None

class SsmControlsTypeDef(BaseValidatorModel):
    ConcurrentExecutionRatePercentage: Optional[int] = None
    ErrorPercentage: Optional[int] = None

class FieldInfoTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class GetAggregateComplianceDetailsByConfigRuleRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: Optional[ComplianceTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ResourceCountFiltersTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    AccountId: Optional[str] = None
    Region: Optional[str] = None

class GroupedResourceCountTypeDef(BaseValidatorModel):
    GroupName: str
    ResourceCount: int

class GetComplianceDetailsByConfigRuleRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetComplianceDetailsByResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None
    ResourceEvaluationId: Optional[str] = None

class GetComplianceSummaryByResourceTypeRequestRequestTypeDef(BaseValidatorModel):
    ResourceTypes: Optional[Sequence[str]] = None

class GetConformancePackComplianceSummaryRequestRequestTypeDef(BaseValidatorModel):
    ConformancePackNames: Sequence[str]
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetCustomRulePolicyRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None

class GetDiscoveredResourceCountsRequestRequestTypeDef(BaseValidatorModel):
    resourceTypes: Optional[Sequence[str]] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ResourceCountTypeDef(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    count: Optional[int] = None

class StatusDetailFiltersTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    MemberAccountRuleStatus: Optional[MemberAccountRuleStatusType] = None

class MemberAccountStatusTypeDef(BaseValidatorModel):
    AccountId: str
    ConfigRuleName: str
    MemberAccountRuleStatus: MemberAccountRuleStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class OrganizationResourceDetailedStatusFiltersTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Status: Optional[OrganizationResourceDetailedStatusType] = None

class OrganizationConformancePackDetailedStatusTypeDef(BaseValidatorModel):
    AccountId: str
    ConformancePackName: str
    Status: OrganizationResourceDetailedStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None

class GetOrganizationCustomRulePolicyRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str

class GetResourceEvaluationSummaryRequestRequestTypeDef(BaseValidatorModel):
    ResourceEvaluationId: str

class ResourceDetailsTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceType: str
    ResourceConfiguration: str
    ResourceConfigurationSchemaType: Optional[Literal["CFN_RESOURCE_SCHEMA"]] = None

class GetStoredQueryRequestRequestTypeDef(BaseValidatorModel):
    QueryName: str

class StoredQueryTypeDef(BaseValidatorModel):
    QueryName: str
    QueryId: Optional[str] = None
    QueryArn: Optional[str] = None
    Description: Optional[str] = None
    Expression: Optional[str] = None

class ResourceFiltersTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceName: Optional[str] = None
    Region: Optional[str] = None

class ListDiscoveredResourcesRequestRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceIds: Optional[Sequence[str]] = None
    resourceName: Optional[str] = None
    limit: Optional[int] = None
    includeDeletedResources: Optional[bool] = None
    nextToken: Optional[str] = None

class ResourceIdentifierTypeDef(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    resourceDeletionTime: Optional[datetime] = None

class ResourceEvaluationTypeDef(BaseValidatorModel):
    ResourceEvaluationId: Optional[str] = None
    EvaluationMode: Optional[EvaluationModeType] = None
    EvaluationStartTimestamp: Optional[datetime] = None

class ListStoredQueriesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StoredQueryMetadataTypeDef(BaseValidatorModel):
    QueryId: str
    QueryArn: str
    QueryName: str
    Description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class OrganizationAggregationSourceExtraOutputTypeDef(BaseValidatorModel):
    RoleArn: str
    AwsRegions: Optional[List[str]] = None
    AllAwsRegions: Optional[bool] = None

class OrganizationAggregationSourceTypeDef(BaseValidatorModel):
    RoleArn: str
    AwsRegions: Optional[Sequence[str]] = None
    AllAwsRegions: Optional[bool] = None

class OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef(BaseValidatorModel):
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

class OrganizationCustomRuleMetadataOutputTypeDef(BaseValidatorModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: List[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationManagedRuleMetadataOutputTypeDef(BaseValidatorModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationCustomPolicyRuleMetadataTypeDef(BaseValidatorModel):
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

class OrganizationCustomRuleMetadataExtraOutputTypeDef(BaseValidatorModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: List[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationCustomRuleMetadataTypeDef(BaseValidatorModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: Sequence[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationManagedRuleMetadataExtraOutputTypeDef(BaseValidatorModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class OrganizationManagedRuleMetadataTypeDef(BaseValidatorModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None

class PutResourceConfigRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: str
    SchemaVersionId: str
    ResourceId: str
    Configuration: str
    ResourceName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class PutRetentionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    RetentionPeriodInDays: int

class RecordingStrategyTypeDef(BaseValidatorModel):
    useOnly: Optional[RecordingStrategyTypeType] = None

class RecordingModeOverrideOutputTypeDef(BaseValidatorModel):
    resourceTypes: List[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: Optional[str] = None

class RecordingModeOverrideTypeDef(BaseValidatorModel):
    resourceTypes: Sequence[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: Optional[str] = None

class RemediationExecutionStepTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[RemediationExecutionStepStateType] = None
    ErrorMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None

class ResourceValueTypeDef(BaseValidatorModel):
    Value: Literal["RESOURCE_ID"]

class StaticValueOutputTypeDef(BaseValidatorModel):
    Values: List[str]

class StaticValueTypeDef(BaseValidatorModel):
    Values: Sequence[str]

class SelectAggregateResourceConfigRequestRequestTypeDef(BaseValidatorModel):
    Expression: str
    ConfigurationAggregatorName: str
    Limit: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SelectResourceConfigRequestRequestTypeDef(BaseValidatorModel):
    Expression: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class SourceDetailTypeDef(BaseValidatorModel):
    EventSource: Optional[Literal["aws.config"]] = None
    MessageType: Optional[MessageTypeType] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None

class StartConfigRulesEvaluationRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None

class StartConfigurationRecorderRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderName: str

class StopConfigurationRecorderRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderName: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AggregateComplianceByConformancePackTypeDef(BaseValidatorModel):
    ConformancePackName: Optional[str] = None
    Compliance: Optional[AggregateConformancePackComplianceTypeDef] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class AggregateConformancePackComplianceSummaryTypeDef(BaseValidatorModel):
    ComplianceSummary: Optional[AggregateConformancePackComplianceCountTypeDef] = None
    GroupName: Optional[str] = None

class DescribeAggregateComplianceByConformancePacksRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetAggregateConformancePackComplianceSummaryRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceSummaryFiltersTypeDef] = None
    GroupByKey: Optional[AggregateConformancePackComplianceSummaryGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class BatchGetAggregateResourceConfigRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceIdentifiers: Sequence[AggregateResourceIdentifierTypeDef]

class GetAggregateResourceConfigRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceIdentifier: AggregateResourceIdentifierTypeDef

class BatchGetAggregateResourceConfigResponseTypeDef(BaseValidatorModel):
    BaseConfigurationItems: List[BaseConfigurationItemTypeDef]
    UnprocessedResourceIdentifiers: List[AggregateResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeliverConfigSnapshotResponseTypeDef(BaseValidatorModel):
    configSnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAggregationAuthorizationsResponseTypeDef(BaseValidatorModel):
    AggregationAuthorizations: List[AggregationAuthorizationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConfigurationAggregatorSourcesStatusResponseTypeDef(BaseValidatorModel):
    AggregatedSourceStatusList: List[AggregatedSourceStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomRulePolicyResponseTypeDef(BaseValidatorModel):
    PolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationCustomRulePolicyResponseTypeDef(BaseValidatorModel):
    PolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregateDiscoveredResourcesResponseTypeDef(BaseValidatorModel):
    ResourceIdentifiers: List[AggregateResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutAggregationAuthorizationResponseTypeDef(BaseValidatorModel):
    AggregationAuthorization: AggregationAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConformancePackResponseTypeDef(BaseValidatorModel):
    ConformancePackArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutOrganizationConfigRuleResponseTypeDef(BaseValidatorModel):
    OrganizationConfigRuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutOrganizationConformancePackResponseTypeDef(BaseValidatorModel):
    OrganizationConformancePackArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutStoredQueryResponseTypeDef(BaseValidatorModel):
    QueryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceEvaluationResponseTypeDef(BaseValidatorModel):
    ResourceEvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetResourceConfigRequestRequestTypeDef(BaseValidatorModel):
    resourceKeys: Sequence[ResourceKeyTypeDef]

class BatchGetResourceConfigResponseTypeDef(BaseValidatorModel):
    baseConfigurationItems: List[BaseConfigurationItemTypeDef]
    unprocessedResourceKeys: List[ResourceKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRemediationExecutionStatusRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKeyTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class StartRemediationExecutionRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[ResourceKeyTypeDef]

class StartRemediationExecutionResponseTypeDef(BaseValidatorModel):
    FailureMessage: str
    FailedItems: List[ResourceKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ComplianceSummaryTypeDef(BaseValidatorModel):
    CompliantResourceCount: Optional[ComplianceContributorCountTypeDef] = None
    NonCompliantResourceCount: Optional[ComplianceContributorCountTypeDef] = None
    ComplianceSummaryTimestamp: Optional[datetime] = None

class ComplianceTypeDef(BaseValidatorModel):
    ComplianceType: Optional[ComplianceTypeType] = None
    ComplianceContributorCount: Optional[ComplianceContributorCountTypeDef] = None

class DescribeAggregateComplianceByConfigRulesRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetAggregateConfigRuleComplianceSummaryRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceSummaryFiltersTypeDef] = None
    GroupByKey: Optional[ConfigRuleComplianceSummaryGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConfigRuleEvaluationStatusResponseTypeDef(BaseValidatorModel):
    ConfigRulesEvaluationStatus: List[ConfigRuleEvaluationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeliveryChannelTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    s3BucketName: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    s3KmsKeyArn: Optional[str] = None
    snsTopicARN: Optional[str] = None
    configSnapshotDeliveryProperties: Optional[ConfigSnapshotDeliveryPropertiesTypeDef] = None

class DeliveryChannelStatusTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    configSnapshotDeliveryInfo: Optional[ConfigExportDeliveryInfoTypeDef] = None
    configHistoryDeliveryInfo: Optional[ConfigExportDeliveryInfoTypeDef] = None
    configStreamDeliveryInfo: Optional[ConfigStreamDeliveryInfoTypeDef] = None

class ConfigurationAggregatorTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: Optional[str] = None
    ConfigurationAggregatorArn: Optional[str] = None
    AccountAggregationSources: Optional[List[AccountAggregationSourceOutputTypeDef]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceOutputTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None

class ConfigurationItemTypeDef(BaseValidatorModel):
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

class DescribeConfigurationRecorderStatusResponseTypeDef(BaseValidatorModel):
    ConfigurationRecordersStatus: List[ConfigurationRecorderStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConformancePackComplianceRequestRequestTypeDef(BaseValidatorModel):
    ConformancePackName: str
    Filters: Optional[ConformancePackComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListConformancePackComplianceScoresResponseTypeDef(BaseValidatorModel):
    ConformancePackComplianceScores: List[ConformancePackComplianceScoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListConformancePackComplianceScoresRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[ConformancePackComplianceScoresFiltersTypeDef] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal["SCORE"]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetConformancePackComplianceSummaryResponseTypeDef(BaseValidatorModel):
    ConformancePackComplianceSummaryList: List[ConformancePackComplianceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OrganizationConformancePackTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    OrganizationConformancePackArn: str
    LastUpdateTime: datetime
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[List[ConformancePackInputParameterTypeDef]] = None
    ExcludedAccounts: Optional[List[str]] = None

class PutOrganizationConformancePackRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[       Sequence[ConformancePackInputParameterTypeDef]     ] = None
    ExcludedAccounts: Optional[Sequence[str]] = None

class ConformancePackDetailTypeDef(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackArn: str
    ConformancePackId: str
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[List[ConformancePackInputParameterTypeDef]] = None
    LastUpdateRequestedTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    TemplateSSMDocumentDetails: Optional[TemplateSSMDocumentDetailsTypeDef] = None

class PutConformancePackRequestRequestTypeDef(BaseValidatorModel):
    ConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[       Sequence[ConformancePackInputParameterTypeDef]     ] = None
    TemplateSSMDocumentDetails: Optional[TemplateSSMDocumentDetailsTypeDef] = None

class GetConformancePackComplianceDetailsRequestRequestTypeDef(BaseValidatorModel):
    ConformancePackName: str
    Filters: Optional[ConformancePackEvaluationFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConformancePackComplianceResponseTypeDef(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackRuleComplianceList: List[ConformancePackRuleComplianceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConformancePackStatusResponseTypeDef(BaseValidatorModel):
    ConformancePackStatusDetails: List[ConformancePackStatusDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeleteRemediationExceptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKeyTypeDef]

class DescribeRemediationExceptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[RemediationExceptionResourceKeyTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class FailedDeleteRemediationExceptionsBatchTypeDef(BaseValidatorModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationExceptionResourceKeyTypeDef]] = None

class DescribeAggregateComplianceByConfigRulesRequestDescribeAggregateComplianceByConfigRulesPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAggregateComplianceByConformancePacksRequestDescribeAggregateComplianceByConformancePacksPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeComplianceByConfigRuleRequestDescribeComplianceByConfigRulePaginateTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeComplianceByResourceRequestDescribeComplianceByResourcePaginateTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigRuleEvaluationStatusRequestDescribeConfigRuleEvaluationStatusPaginateTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigurationAggregatorSourcesStatusRequestDescribeConfigurationAggregatorSourcesStatusPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigurationAggregatorsRequestDescribeConfigurationAggregatorsPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConformancePackStatusRequestDescribeConformancePackStatusPaginateTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConformancePacksRequestDescribeConformancePacksPaginateTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConfigRuleStatusesRequestDescribeOrganizationConfigRuleStatusesPaginateTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConfigRulesRequestDescribeOrganizationConfigRulesPaginateTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConformancePackStatusesRequestDescribeOrganizationConformancePackStatusesPaginateTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConformancePacksRequestDescribeOrganizationConformancePacksPaginateTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePendingAggregationRequestsRequestDescribePendingAggregationRequestsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRemediationExecutionStatusRequestDescribeRemediationExecutionStatusPaginateTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKeyTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRetentionConfigurationsRequestDescribeRetentionConfigurationsPaginateTypeDef(BaseValidatorModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAggregateComplianceDetailsByConfigRuleRequestGetAggregateComplianceDetailsByConfigRulePaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: Optional[ComplianceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetComplianceDetailsByConfigRuleRequestGetComplianceDetailsByConfigRulePaginateTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetComplianceDetailsByResourceRequestGetComplianceDetailsByResourcePaginateTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    ResourceEvaluationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConformancePackComplianceSummaryRequestGetConformancePackComplianceSummaryPaginateTypeDef(BaseValidatorModel):
    ConformancePackNames: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceIds: Optional[Sequence[str]] = None
    resourceName: Optional[str] = None
    includeDeletedResources: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SelectAggregateResourceConfigRequestSelectAggregateResourceConfigPaginateTypeDef(BaseValidatorModel):
    Expression: str
    ConfigurationAggregatorName: str
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SelectResourceConfigRequestSelectResourceConfigPaginateTypeDef(BaseValidatorModel):
    Expression: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigRulesRequestDescribeConfigRulesPaginateTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    Filters: Optional[DescribeConfigRulesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeConfigRulesRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Filters: Optional[DescribeConfigRulesFiltersTypeDef] = None

class DescribeOrganizationConfigRuleStatusesResponseTypeDef(BaseValidatorModel):
    OrganizationConfigRuleStatuses: List[OrganizationConfigRuleStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOrganizationConformancePackStatusesResponseTypeDef(BaseValidatorModel):
    OrganizationConformancePackStatuses: List[OrganizationConformancePackStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePendingAggregationRequestsResponseTypeDef(BaseValidatorModel):
    PendingAggregationRequests: List[PendingAggregationRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRemediationExceptionsResponseTypeDef(BaseValidatorModel):
    RemediationExceptions: List[RemediationExceptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailedRemediationExceptionBatchTypeDef(BaseValidatorModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationExceptionTypeDef]] = None

class DescribeRetentionConfigurationsResponseTypeDef(BaseValidatorModel):
    RetentionConfigurations: List[RetentionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutRetentionConfigurationResponseTypeDef(BaseValidatorModel):
    RetentionConfiguration: RetentionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEvaluationsResponseTypeDef(BaseValidatorModel):
    FailedEvaluations: List[EvaluationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationResultIdentifierTypeDef(BaseValidatorModel):
    EvaluationResultQualifier: Optional[EvaluationResultQualifierTypeDef] = None
    OrderingTimestamp: Optional[datetime] = None
    ResourceEvaluationId: Optional[str] = None

class EvaluationTypeDef(BaseValidatorModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: TimestampTypeDef
    Annotation: Optional[str] = None

class ExternalEvaluationTypeDef(BaseValidatorModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: TimestampTypeDef
    Annotation: Optional[str] = None

class GetResourceConfigHistoryRequestGetResourceConfigHistoryPaginateTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[TimestampTypeDef] = None
    earlierTime: Optional[TimestampTypeDef] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceConfigHistoryRequestRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[TimestampTypeDef] = None
    earlierTime: Optional[TimestampTypeDef] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class PutRemediationExceptionsRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKeyTypeDef]
    Message: Optional[str] = None
    ExpirationTime: Optional[TimestampTypeDef] = None

class TimeWindowTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None

class ExecutionControlsTypeDef(BaseValidatorModel):
    SsmControls: Optional[SsmControlsTypeDef] = None

class QueryInfoTypeDef(BaseValidatorModel):
    SelectFields: Optional[List[FieldInfoTypeDef]] = None

class GetAggregateDiscoveredResourceCountsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ResourceCountFiltersTypeDef] = None
    GroupByKey: Optional[ResourceCountGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetAggregateDiscoveredResourceCountsResponseTypeDef(BaseValidatorModel):
    TotalDiscoveredResources: int
    GroupByKey: str
    GroupedResourceCounts: List[GroupedResourceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDiscoveredResourceCountsResponseTypeDef(BaseValidatorModel):
    totalDiscoveredResources: int
    resourceCounts: List[ResourceCountTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrganizationConfigRuleDetailedStatusRequestGetOrganizationConfigRuleDetailedStatusPaginateTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOrganizationConfigRuleDetailedStatusRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetOrganizationConfigRuleDetailedStatusResponseTypeDef(BaseValidatorModel):
    OrganizationConfigRuleDetailedStatus: List[MemberAccountStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetOrganizationConformancePackDetailedStatusRequestGetOrganizationConformancePackDetailedStatusPaginateTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOrganizationConformancePackDetailedStatusRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class GetOrganizationConformancePackDetailedStatusResponseTypeDef(BaseValidatorModel):
    OrganizationConformancePackDetailedStatuses: List[       OrganizationConformancePackDetailedStatusTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetResourceEvaluationSummaryResponseTypeDef(BaseValidatorModel):
    ResourceEvaluationId: str
    EvaluationMode: EvaluationModeType
    EvaluationStatus: EvaluationStatusTypeDef
    EvaluationStartTimestamp: datetime
    Compliance: ComplianceTypeType
    EvaluationContext: EvaluationContextTypeDef
    ResourceDetails: ResourceDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceEvaluationRequestRequestTypeDef(BaseValidatorModel):
    ResourceDetails: ResourceDetailsTypeDef
    EvaluationMode: EvaluationModeType
    EvaluationContext: Optional[EvaluationContextTypeDef] = None
    EvaluationTimeout: Optional[int] = None
    ClientToken: Optional[str] = None

class GetStoredQueryResponseTypeDef(BaseValidatorModel):
    StoredQuery: StoredQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAggregateDiscoveredResourcesRequestListAggregateDiscoveredResourcesPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAggregateDiscoveredResourcesRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class ListDiscoveredResourcesResponseTypeDef(BaseValidatorModel):
    resourceIdentifiers: List[ResourceIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceEvaluationsResponseTypeDef(BaseValidatorModel):
    ResourceEvaluations: List[ResourceEvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListStoredQueriesResponseTypeDef(BaseValidatorModel):
    StoredQueryMetadata: List[StoredQueryMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutAggregationAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class PutStoredQueryRequestRequestTypeDef(BaseValidatorModel):
    StoredQuery: StoredQueryTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class OrganizationConfigRuleTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationConfigRuleArn: str
    OrganizationManagedRuleMetadata: Optional[       OrganizationManagedRuleMetadataOutputTypeDef     ] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataOutputTypeDef] = None
    ExcludedAccounts: Optional[List[str]] = None
    LastUpdateTime: Optional[datetime] = None
    OrganizationCustomPolicyRuleMetadata: Optional[       OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef     ] = None

class PutOrganizationConfigRuleRequestRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationManagedRuleMetadata: Optional[OrganizationManagedRuleMetadataTypeDef] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataTypeDef] = None
    ExcludedAccounts: Optional[Sequence[str]] = None
    OrganizationCustomPolicyRuleMetadata: Optional[       OrganizationCustomPolicyRuleMetadataTypeDef     ] = None

class RecordingGroupOutputTypeDef(BaseValidatorModel):
    allSupported: Optional[bool] = None
    includeGlobalResourceTypes: Optional[bool] = None
    resourceTypes: Optional[List[ResourceTypeType]] = None
    exclusionByResourceTypes: Optional[ExclusionByResourceTypesOutputTypeDef] = None
    recordingStrategy: Optional[RecordingStrategyTypeDef] = None

class RecordingGroupTypeDef(BaseValidatorModel):
    allSupported: Optional[bool] = None
    includeGlobalResourceTypes: Optional[bool] = None
    resourceTypes: Optional[Sequence[ResourceTypeType]] = None
    exclusionByResourceTypes: Optional[ExclusionByResourceTypesTypeDef] = None
    recordingStrategy: Optional[RecordingStrategyTypeDef] = None

class RecordingModeOutputTypeDef(BaseValidatorModel):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: Optional[List[RecordingModeOverrideOutputTypeDef]] = None

class RecordingModeTypeDef(BaseValidatorModel):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: Optional[Sequence[RecordingModeOverrideTypeDef]] = None

class RemediationExecutionStatusTypeDef(BaseValidatorModel):
    ResourceKey: Optional[ResourceKeyTypeDef] = None
    State: Optional[RemediationExecutionStateType] = None
    StepDetails: Optional[List[RemediationExecutionStepTypeDef]] = None
    InvocationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None

class RemediationParameterValueOutputTypeDef(BaseValidatorModel):
    ResourceValue: Optional[ResourceValueTypeDef] = None
    StaticValue: Optional[StaticValueOutputTypeDef] = None

class RemediationParameterValueTypeDef(BaseValidatorModel):
    ResourceValue: Optional[ResourceValueTypeDef] = None
    StaticValue: Optional[StaticValueTypeDef] = None

class SourceExtraOutputTypeDef(BaseValidatorModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[List[SourceDetailTypeDef]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetailsTypeDef] = None

class SourceOutputTypeDef(BaseValidatorModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[List[SourceDetailTypeDef]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetailsTypeDef] = None

class SourceTypeDef(BaseValidatorModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[Sequence[SourceDetailTypeDef]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetailsTypeDef] = None

class PutConfigurationAggregatorRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    AccountAggregationSources: Optional[Sequence[AccountAggregationSourceUnionTypeDef]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeAggregateComplianceByConformancePacksResponseTypeDef(BaseValidatorModel):
    AggregateComplianceByConformancePacks: List[AggregateComplianceByConformancePackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetAggregateConformancePackComplianceSummaryResponseTypeDef(BaseValidatorModel):
    AggregateConformancePackComplianceSummaries: List[       AggregateConformancePackComplianceSummaryTypeDef     ]
    GroupByKey: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AggregateComplianceCountTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    ComplianceSummary: Optional[ComplianceSummaryTypeDef] = None

class ComplianceSummaryByResourceTypeTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ComplianceSummary: Optional[ComplianceSummaryTypeDef] = None

class GetComplianceSummaryByConfigRuleResponseTypeDef(BaseValidatorModel):
    ComplianceSummary: ComplianceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AggregateComplianceByConfigRuleTypeDef(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    Compliance: Optional[ComplianceTypeDef] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ComplianceByConfigRuleTypeDef(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    Compliance: Optional[ComplianceTypeDef] = None

class ComplianceByResourceTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Compliance: Optional[ComplianceTypeDef] = None

class DescribeDeliveryChannelsResponseTypeDef(BaseValidatorModel):
    DeliveryChannels: List[DeliveryChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryChannelRequestRequestTypeDef(BaseValidatorModel):
    DeliveryChannel: DeliveryChannelTypeDef

class DescribeDeliveryChannelStatusResponseTypeDef(BaseValidatorModel):
    DeliveryChannelsStatus: List[DeliveryChannelStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationAggregatorsResponseTypeDef(BaseValidatorModel):
    ConfigurationAggregators: List[ConfigurationAggregatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutConfigurationAggregatorResponseTypeDef(BaseValidatorModel):
    ConfigurationAggregator: ConfigurationAggregatorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAggregateResourceConfigResponseTypeDef(BaseValidatorModel):
    ConfigurationItem: ConfigurationItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceConfigHistoryResponseTypeDef(BaseValidatorModel):
    configurationItems: List[ConfigurationItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeOrganizationConformancePacksResponseTypeDef(BaseValidatorModel):
    OrganizationConformancePacks: List[OrganizationConformancePackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConformancePacksResponseTypeDef(BaseValidatorModel):
    ConformancePackDetails: List[ConformancePackDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeleteRemediationExceptionsResponseTypeDef(BaseValidatorModel):
    FailedBatches: List[FailedDeleteRemediationExceptionsBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRemediationExceptionsResponseTypeDef(BaseValidatorModel):
    FailedBatches: List[FailedRemediationExceptionBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AggregateEvaluationResultTypeDef(BaseValidatorModel):
    EvaluationResultIdentifier: Optional[EvaluationResultIdentifierTypeDef] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    ResultRecordedTime: Optional[datetime] = None
    ConfigRuleInvokedTime: Optional[datetime] = None
    Annotation: Optional[str] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None

class ConformancePackEvaluationResultTypeDef(BaseValidatorModel):
    ComplianceType: ConformancePackComplianceTypeType
    EvaluationResultIdentifier: EvaluationResultIdentifierTypeDef
    ConfigRuleInvokedTime: datetime
    ResultRecordedTime: datetime
    Annotation: Optional[str] = None

class EvaluationResultTypeDef(BaseValidatorModel):
    EvaluationResultIdentifier: Optional[EvaluationResultIdentifierTypeDef] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    ResultRecordedTime: Optional[datetime] = None
    ConfigRuleInvokedTime: Optional[datetime] = None
    Annotation: Optional[str] = None
    ResultToken: Optional[str] = None

class PutExternalEvaluationRequestRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ExternalEvaluation: ExternalEvaluationTypeDef

class ResourceEvaluationFiltersTypeDef(BaseValidatorModel):
    EvaluationMode: Optional[EvaluationModeType] = None
    TimeWindow: Optional[TimeWindowTypeDef] = None
    EvaluationContextIdentifier: Optional[str] = None

class SelectAggregateResourceConfigResponseTypeDef(BaseValidatorModel):
    Results: List[str]
    QueryInfo: QueryInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SelectResourceConfigResponseTypeDef(BaseValidatorModel):
    Results: List[str]
    QueryInfo: QueryInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeOrganizationConfigRulesResponseTypeDef(BaseValidatorModel):
    OrganizationConfigRules: List[OrganizationConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ConfigurationRecorderOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroupOutputTypeDef] = None
    recordingMode: Optional[RecordingModeOutputTypeDef] = None

class ConfigurationRecorderTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroupTypeDef] = None
    recordingMode: Optional[RecordingModeTypeDef] = None

class DescribeRemediationExecutionStatusResponseTypeDef(BaseValidatorModel):
    RemediationExecutionStatuses: List[RemediationExecutionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RemediationConfigurationOutputTypeDef(BaseValidatorModel):
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

class RemediationConfigurationTypeDef(BaseValidatorModel):
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

class ConfigRuleExtraOutputTypeDef(BaseValidatorModel):
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

class ConfigRuleOutputTypeDef(BaseValidatorModel):
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

class ConfigRuleTypeDef(BaseValidatorModel):
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

class GetAggregateConfigRuleComplianceSummaryResponseTypeDef(BaseValidatorModel):
    GroupByKey: str
    AggregateComplianceCounts: List[AggregateComplianceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComplianceSummaryByResourceTypeResponseTypeDef(BaseValidatorModel):
    ComplianceSummariesByResourceType: List[ComplianceSummaryByResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAggregateComplianceByConfigRulesResponseTypeDef(BaseValidatorModel):
    AggregateComplianceByConfigRules: List[AggregateComplianceByConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeComplianceByConfigRuleResponseTypeDef(BaseValidatorModel):
    ComplianceByConfigRules: List[ComplianceByConfigRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeComplianceByResourceResponseTypeDef(BaseValidatorModel):
    ComplianceByResources: List[ComplianceByResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetAggregateComplianceDetailsByConfigRuleResponseTypeDef(BaseValidatorModel):
    AggregateEvaluationResults: List[AggregateEvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetConformancePackComplianceDetailsResponseTypeDef(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackRuleEvaluationResults: List[ConformancePackEvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComplianceDetailsByConfigRuleResponseTypeDef(BaseValidatorModel):
    EvaluationResults: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComplianceDetailsByResourceResponseTypeDef(BaseValidatorModel):
    EvaluationResults: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutEvaluationsRequestRequestTypeDef(BaseValidatorModel):
    ResultToken: str
    Evaluations: Optional[Sequence[EvaluationUnionTypeDef]] = None
    TestMode: Optional[bool] = None

class ListResourceEvaluationsRequestListResourceEvaluationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[ResourceEvaluationFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceEvaluationsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[ResourceEvaluationFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeConfigurationRecordersResponseTypeDef(BaseValidatorModel):
    ConfigurationRecorders: List[ConfigurationRecorderOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigurationRecorderRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorder: ConfigurationRecorderTypeDef

class DescribeRemediationConfigurationsResponseTypeDef(BaseValidatorModel):
    RemediationConfigurations: List[RemediationConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FailedRemediationBatchTypeDef(BaseValidatorModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationConfigurationOutputTypeDef]] = None

class DescribeConfigRulesResponseTypeDef(BaseValidatorModel):
    ConfigRules: List[ConfigRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutConfigRuleRequestRequestTypeDef(BaseValidatorModel):
    ConfigRule: ConfigRuleTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class PutRemediationConfigurationsResponseTypeDef(BaseValidatorModel):
    FailedBatches: List[FailedRemediationBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutRemediationConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    RemediationConfigurations: Sequence[RemediationConfigurationUnionTypeDef]

