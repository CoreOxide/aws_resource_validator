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
from aws_resource_validator.pydantic_models.config_constants import *

class AccountAggregationSourceOutput(BaseValidatorModel):
    AccountIds: List[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[List[str]] = None


class AccountAggregationSource(BaseValidatorModel):
    AccountIds: Sequence[str]
    AllAwsRegions: Optional[bool] = None
    AwsRegions: Optional[Sequence[str]] = None


class AggregateConformancePackCompliance(BaseValidatorModel):
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    CompliantRuleCount: Optional[int] = None
    NonCompliantRuleCount: Optional[int] = None
    TotalRuleCount: Optional[int] = None


class AggregateConformancePackComplianceCount(BaseValidatorModel):
    CompliantConformancePackCount: Optional[int] = None
    NonCompliantConformancePackCount: Optional[int] = None


class AggregateConformancePackComplianceFilters(BaseValidatorModel):
    ConformancePackName: Optional[str] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None


class AggregateConformancePackComplianceSummaryFilters(BaseValidatorModel):
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None


class AggregateResourceIdentifier(BaseValidatorModel):
    SourceAccountId: str
    SourceRegion: str
    ResourceId: str
    ResourceType: ResourceTypeType
    ResourceName: Optional[str] = None


class AggregatedSourceStatus(BaseValidatorModel):
    SourceId: Optional[str] = None
    SourceType: Optional[AggregatedSourceTypeType] = None
    AwsRegion: Optional[str] = None
    LastUpdateStatus: Optional[AggregatedSourceStatusTypeType] = None
    LastUpdateTime: Optional[datetime] = None
    LastErrorCode: Optional[str] = None
    LastErrorMessage: Optional[str] = None


class AggregationAuthorization(BaseValidatorModel):
    AggregationAuthorizationArn: Optional[str] = None
    AuthorizedAccountId: Optional[str] = None
    AuthorizedAwsRegion: Optional[str] = None
    CreationTime: Optional[datetime] = None


class AssociateResourceTypesRequest(BaseValidatorModel):
    ConfigurationRecorderArn: str
    ResourceTypes: Sequence[ResourceTypeType]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BaseConfigurationItem(BaseValidatorModel):
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


class ResourceKey(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str


class ComplianceContributorCount(BaseValidatorModel):
    CappedCount: Optional[int] = None
    CapExceeded: Optional[bool] = None


class ConfigExportDeliveryInfo(BaseValidatorModel):
    lastStatus: Optional[DeliveryStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastAttemptTime: Optional[datetime] = None
    lastSuccessfulTime: Optional[datetime] = None
    nextDeliveryTime: Optional[datetime] = None


class ConfigRuleComplianceFilters(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None


class ConfigRuleComplianceSummaryFilters(BaseValidatorModel):
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None


class ConfigRuleEvaluationStatus(BaseValidatorModel):
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


class EvaluationModeConfiguration(BaseValidatorModel):
    Mode: Optional[EvaluationModeType] = None


class ScopeOutput(BaseValidatorModel):
    ComplianceResourceTypes: Optional[List[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None


class Scope(BaseValidatorModel):
    ComplianceResourceTypes: Optional[Sequence[str]] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    ComplianceResourceId: Optional[str] = None


class ConfigSnapshotDeliveryProperties(BaseValidatorModel):
    deliveryFrequency: Optional[MaximumExecutionFrequencyType] = None


class ConfigStreamDeliveryInfo(BaseValidatorModel):
    lastStatus: Optional[DeliveryStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastStatusChangeTime: Optional[datetime] = None


class OrganizationAggregationSourceOutput(BaseValidatorModel):
    RoleArn: str
    AwsRegions: Optional[List[str]] = None
    AllAwsRegions: Optional[bool] = None


class Relationship(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    relationshipName: Optional[str] = None


class ConfigurationRecorderFilter(BaseValidatorModel):
    filterName: Optional[Literal["recordingScope"]] = None
    filterValue: Optional[Sequence[str]] = None


class ConfigurationRecorderStatus(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    lastStartTime: Optional[datetime] = None
    lastStopTime: Optional[datetime] = None
    recording: Optional[bool] = None
    lastStatus: Optional[RecorderStatusType] = None
    lastErrorCode: Optional[str] = None
    lastErrorMessage: Optional[str] = None
    lastStatusChangeTime: Optional[datetime] = None
    servicePrincipal: Optional[str] = None


class ConfigurationRecorderSummary(BaseValidatorModel):
    arn: str
    name: str
    recordingScope: RecordingScopeType
    servicePrincipal: Optional[str] = None


class ConformancePackComplianceFilters(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None


class ConformancePackComplianceScore(BaseValidatorModel):
    Score: Optional[str] = None
    ConformancePackName: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None


class ConformancePackComplianceScoresFilters(BaseValidatorModel):
    ConformancePackNames: Sequence[str]


class ConformancePackComplianceSummary(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackComplianceStatus: ConformancePackComplianceTypeType


class ConformancePackInputParameter(BaseValidatorModel):
    ParameterName: str
    ParameterValue: str


class TemplateSSMDocumentDetails(BaseValidatorModel):
    DocumentName: str
    DocumentVersion: Optional[str] = None


class ConformancePackEvaluationFilters(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    ResourceType: Optional[str] = None
    ResourceIds: Optional[Sequence[str]] = None


class ConformancePackRuleCompliance(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    ComplianceType: Optional[ConformancePackComplianceTypeType] = None
    Controls: Optional[List[str]] = None


class ConformancePackStatusDetail(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackId: str
    ConformancePackArn: str
    ConformancePackState: ConformancePackStateType
    StackArn: str
    LastUpdateRequestedTime: datetime
    ConformancePackStatusReason: Optional[str] = None
    LastUpdateCompletedTime: Optional[datetime] = None


class CustomPolicyDetails(BaseValidatorModel):
    PolicyRuntime: str
    PolicyText: str
    EnableDebugLogDelivery: Optional[bool] = None


class DeleteAggregationAuthorizationRequest(BaseValidatorModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str


class DeleteConfigRuleRequest(BaseValidatorModel):
    ConfigRuleName: str


class DeleteConfigurationAggregatorRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str


class DeleteConfigurationRecorderRequest(BaseValidatorModel):
    ConfigurationRecorderName: str


class DeleteConformancePackRequest(BaseValidatorModel):
    ConformancePackName: str


class DeleteDeliveryChannelRequest(BaseValidatorModel):
    DeliveryChannelName: str


class DeleteEvaluationResultsRequest(BaseValidatorModel):
    ConfigRuleName: str


class DeleteOrganizationConfigRuleRequest(BaseValidatorModel):
    OrganizationConfigRuleName: str


class DeleteOrganizationConformancePackRequest(BaseValidatorModel):
    OrganizationConformancePackName: str


class DeletePendingAggregationRequestRequest(BaseValidatorModel):
    RequesterAccountId: str
    RequesterAwsRegion: str


class DeleteRemediationConfigurationRequest(BaseValidatorModel):
    ConfigRuleName: str
    ResourceType: Optional[str] = None


class RemediationExceptionResourceKey(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None


class DeleteResourceConfigRequest(BaseValidatorModel):
    ResourceType: str
    ResourceId: str


class DeleteRetentionConfigurationRequest(BaseValidatorModel):
    RetentionConfigurationName: str


class DeleteServiceLinkedConfigurationRecorderRequest(BaseValidatorModel):
    ServicePrincipal: str


class DeleteStoredQueryRequest(BaseValidatorModel):
    QueryName: str


class DeliverConfigSnapshotRequest(BaseValidatorModel):
    deliveryChannelName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAggregationAuthorizationsRequest(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeComplianceByConfigRuleRequest(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None


class DescribeComplianceByResourceRequest(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConfigRuleEvaluationStatusRequest(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeConfigRulesFilters(BaseValidatorModel):
    EvaluationMode: Optional[EvaluationModeType] = None


class DescribeConfigurationAggregatorSourcesStatusRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeConfigurationAggregatorsRequest(BaseValidatorModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeConfigurationRecorderStatusRequest(BaseValidatorModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None
    ServicePrincipal: Optional[str] = None
    Arn: Optional[str] = None


class DescribeConfigurationRecordersRequest(BaseValidatorModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None
    ServicePrincipal: Optional[str] = None
    Arn: Optional[str] = None


class DescribeConformancePackStatusRequest(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConformancePacksRequest(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDeliveryChannelStatusRequest(BaseValidatorModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None


class DescribeDeliveryChannelsRequest(BaseValidatorModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None


class DescribeOrganizationConfigRuleStatusesRequest(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class OrganizationConfigRuleStatus(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationRuleStatus: OrganizationRuleStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class DescribeOrganizationConfigRulesRequest(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeOrganizationConformancePackStatusesRequest(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class OrganizationConformancePackStatus(BaseValidatorModel):
    OrganizationConformancePackName: str
    Status: OrganizationResourceStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class DescribeOrganizationConformancePacksRequest(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePendingAggregationRequestsRequest(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class PendingAggregationRequest(BaseValidatorModel):
    RequesterAccountId: Optional[str] = None
    RequesterAwsRegion: Optional[str] = None


class DescribeRemediationConfigurationsRequest(BaseValidatorModel):
    ConfigRuleNames: Sequence[str]


class RemediationException(BaseValidatorModel):
    ConfigRuleName: str
    ResourceType: str
    ResourceId: str
    Message: Optional[str] = None
    ExpirationTime: Optional[datetime] = None


class DescribeRetentionConfigurationsRequest(BaseValidatorModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None


class RetentionConfiguration(BaseValidatorModel):
    Name: str
    RetentionPeriodInDays: int


class DisassociateResourceTypesRequest(BaseValidatorModel):
    ConfigurationRecorderArn: str
    ResourceTypes: Sequence[ResourceTypeType]


class EvaluationContext(BaseValidatorModel):
    EvaluationContextIdentifier: Optional[str] = None


class EvaluationOutput(BaseValidatorModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: datetime
    Annotation: Optional[str] = None


class EvaluationResultQualifier(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    EvaluationMode: Optional[EvaluationModeType] = None


class EvaluationStatus(BaseValidatorModel):
    Status: ResourceEvaluationStatusType
    FailureReason: Optional[str] = None


class ExclusionByResourceTypesOutput(BaseValidatorModel):
    resourceTypes: Optional[List[ResourceTypeType]] = None


class ExclusionByResourceTypes(BaseValidatorModel):
    resourceTypes: Optional[Sequence[ResourceTypeType]] = None


class SsmControls(BaseValidatorModel):
    ConcurrentExecutionRatePercentage: Optional[int] = None
    ErrorPercentage: Optional[int] = None


class FieldInfo(BaseValidatorModel):
    Name: Optional[str] = None


class GetAggregateComplianceDetailsByConfigRuleRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: Optional[ComplianceTypeType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ResourceCountFilters(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    AccountId: Optional[str] = None
    Region: Optional[str] = None


class GroupedResourceCount(BaseValidatorModel):
    GroupName: str
    ResourceCount: int


class GetComplianceDetailsByConfigRuleRequest(BaseValidatorModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetComplianceDetailsByResourceRequest(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None
    ResourceEvaluationId: Optional[str] = None


class GetComplianceSummaryByResourceTypeRequest(BaseValidatorModel):
    ResourceTypes: Optional[Sequence[str]] = None


class GetConformancePackComplianceSummaryRequest(BaseValidatorModel):
    ConformancePackNames: Sequence[str]
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetCustomRulePolicyRequest(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None


class GetDiscoveredResourceCountsRequest(BaseValidatorModel):
    resourceTypes: Optional[Sequence[str]] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class ResourceCount(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    count: Optional[int] = None


class StatusDetailFilters(BaseValidatorModel):
    AccountId: Optional[str] = None
    MemberAccountRuleStatus: Optional[MemberAccountRuleStatusType] = None


class MemberAccountStatus(BaseValidatorModel):
    AccountId: str
    ConfigRuleName: str
    MemberAccountRuleStatus: MemberAccountRuleStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class OrganizationResourceDetailedStatusFilters(BaseValidatorModel):
    AccountId: Optional[str] = None
    Status: Optional[OrganizationResourceDetailedStatusType] = None


class OrganizationConformancePackDetailedStatus(BaseValidatorModel):
    AccountId: str
    ConformancePackName: str
    Status: OrganizationResourceDetailedStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class GetOrganizationCustomRulePolicyRequest(BaseValidatorModel):
    OrganizationConfigRuleName: str


class GetResourceEvaluationSummaryRequest(BaseValidatorModel):
    ResourceEvaluationId: str


class ResourceDetails(BaseValidatorModel):
    ResourceId: str
    ResourceType: str
    ResourceConfiguration: str
    ResourceConfigurationSchemaType: Optional[Literal["CFN_RESOURCE_SCHEMA"]] = None


class GetStoredQueryRequest(BaseValidatorModel):
    QueryName: str


class StoredQuery(BaseValidatorModel):
    QueryName: str
    QueryId: Optional[str] = None
    QueryArn: Optional[str] = None
    Description: Optional[str] = None
    Expression: Optional[str] = None


class ResourceFilters(BaseValidatorModel):
    AccountId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceName: Optional[str] = None
    Region: Optional[str] = None


class ListDiscoveredResourcesRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceIds: Optional[Sequence[str]] = None
    resourceName: Optional[str] = None
    limit: Optional[int] = None
    includeDeletedResources: Optional[bool] = None
    nextToken: Optional[str] = None


class ResourceIdentifier(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceId: Optional[str] = None
    resourceName: Optional[str] = None
    resourceDeletionTime: Optional[datetime] = None


class ResourceEvaluation(BaseValidatorModel):
    ResourceEvaluationId: Optional[str] = None
    EvaluationMode: Optional[EvaluationModeType] = None
    EvaluationStartTimestamp: Optional[datetime] = None


class ListStoredQueriesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StoredQueryMetadata(BaseValidatorModel):
    QueryId: str
    QueryArn: str
    QueryName: str
    Description: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class OrganizationAggregationSource(BaseValidatorModel):
    RoleArn: str
    AwsRegions: Optional[Sequence[str]] = None
    AllAwsRegions: Optional[bool] = None


class OrganizationCustomPolicyRuleMetadataNoPolicy(BaseValidatorModel):
    Description: Optional[str] = None
    OrganizationConfigRuleTriggerTypes: Optional[List[OrganizationConfigRuleTriggerTypeNoSNType]] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None
    PolicyRuntime: Optional[str] = None
    DebugLogDeliveryAccounts: Optional[List[str]] = None


class OrganizationCustomRuleMetadataOutput(BaseValidatorModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: List[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None


class OrganizationManagedRuleMetadataOutput(BaseValidatorModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[List[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None


class OrganizationCustomPolicyRuleMetadata(BaseValidatorModel):
    PolicyRuntime: str
    PolicyText: str
    Description: Optional[str] = None
    OrganizationConfigRuleTriggerTypes: Optional[ Sequence[OrganizationConfigRuleTriggerTypeNoSNType] ] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None
    DebugLogDeliveryAccounts: Optional[Sequence[str]] = None


class OrganizationCustomRuleMetadata(BaseValidatorModel):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: Sequence[OrganizationConfigRuleTriggerTypeType]
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None


class OrganizationManagedRuleMetadata(BaseValidatorModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None


class PutResourceConfigRequest(BaseValidatorModel):
    ResourceType: str
    SchemaVersionId: str
    ResourceId: str
    Configuration: str
    ResourceName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class PutRetentionConfigurationRequest(BaseValidatorModel):
    RetentionPeriodInDays: int


class RecordingStrategy(BaseValidatorModel):
    useOnly: Optional[RecordingStrategyTypeType] = None


class RecordingModeOverrideOutput(BaseValidatorModel):
    resourceTypes: List[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: Optional[str] = None


class RecordingModeOverride(BaseValidatorModel):
    resourceTypes: Sequence[ResourceTypeType]
    recordingFrequency: RecordingFrequencyType
    description: Optional[str] = None


class RemediationExecutionStep(BaseValidatorModel):
    Name: Optional[str] = None
    State: Optional[RemediationExecutionStepStateType] = None
    ErrorMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    StopTime: Optional[datetime] = None


class ResourceValue(BaseValidatorModel):
    Value: Literal["RESOURCE_ID"]


class StaticValueOutput(BaseValidatorModel):
    Values: List[str]


class SelectAggregateResourceConfigRequest(BaseValidatorModel):
    Expression: str
    ConfigurationAggregatorName: str
    Limit: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SelectResourceConfigRequest(BaseValidatorModel):
    Expression: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class SourceDetail(BaseValidatorModel):
    EventSource: Optional[Literal["aws.config"]] = None
    MessageType: Optional[MessageTypeType] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None


class StartConfigRulesEvaluationRequest(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None


class StartConfigurationRecorderRequest(BaseValidatorModel):
    ConfigurationRecorderName: str


class StaticValue(BaseValidatorModel):
    Values: Sequence[str]


class StopConfigurationRecorderRequest(BaseValidatorModel):
    ConfigurationRecorderName: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class AggregateComplianceByConformancePack(BaseValidatorModel):
    ConformancePackName: Optional[str] = None
    Compliance: Optional[AggregateConformancePackCompliance] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None


class AggregateConformancePackComplianceSummary(BaseValidatorModel):
    ComplianceSummary: Optional[AggregateConformancePackComplianceCount] = None
    GroupName: Optional[str] = None


class DescribeAggregateComplianceByConformancePacksRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetAggregateConformancePackComplianceSummaryRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceSummaryFilters] = None
    GroupByKey: Optional[AggregateConformancePackComplianceSummaryGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class BatchGetAggregateResourceConfigRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceIdentifiers: Sequence[AggregateResourceIdentifier]


class GetAggregateResourceConfigRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceIdentifier: AggregateResourceIdentifier


class AggregatorFilterResourceTypeOutput(BaseValidatorModel):
    pass


class AggregatorFilterServicePrincipalOutput(BaseValidatorModel):
    pass


class AggregatorFiltersOutput(BaseValidatorModel):
    ResourceType: Optional[AggregatorFilterResourceTypeOutput] = None
    ServicePrincipal: Optional[AggregatorFilterServicePrincipalOutput] = None


class AggregatorFilterServicePrincipal(BaseValidatorModel):
    pass


class AggregatorFilterResourceType(BaseValidatorModel):
    pass


class AggregatorFilters(BaseValidatorModel):
    ResourceType: Optional[AggregatorFilterResourceType] = None
    ServicePrincipal: Optional[AggregatorFilterServicePrincipal] = None


class DeleteServiceLinkedConfigurationRecorderResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class DeliverConfigSnapshotResponse(BaseValidatorModel):
    configSnapshotId: str
    ResponseMetadata: ResponseMetadata


class DescribeAggregationAuthorizationsResponse(BaseValidatorModel):
    AggregationAuthorizations: List[AggregationAuthorization]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeConfigurationAggregatorSourcesStatusResponse(BaseValidatorModel):
    AggregatedSourceStatusList: List[AggregatedSourceStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCustomRulePolicyResponse(BaseValidatorModel):
    PolicyText: str
    ResponseMetadata: ResponseMetadata


class GetOrganizationCustomRulePolicyResponse(BaseValidatorModel):
    PolicyText: str
    ResponseMetadata: ResponseMetadata


class ListAggregateDiscoveredResourcesResponse(BaseValidatorModel):
    ResourceIdentifiers: List[AggregateResourceIdentifier]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutAggregationAuthorizationResponse(BaseValidatorModel):
    AggregationAuthorization: AggregationAuthorization
    ResponseMetadata: ResponseMetadata


class PutConformancePackResponse(BaseValidatorModel):
    ConformancePackArn: str
    ResponseMetadata: ResponseMetadata


class PutOrganizationConfigRuleResponse(BaseValidatorModel):
    OrganizationConfigRuleArn: str
    ResponseMetadata: ResponseMetadata


class PutOrganizationConformancePackResponse(BaseValidatorModel):
    OrganizationConformancePackArn: str
    ResponseMetadata: ResponseMetadata


class PutServiceLinkedConfigurationRecorderResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadata


class PutStoredQueryResponse(BaseValidatorModel):
    QueryArn: str
    ResponseMetadata: ResponseMetadata


class StartResourceEvaluationResponse(BaseValidatorModel):
    ResourceEvaluationId: str
    ResponseMetadata: ResponseMetadata


class BatchGetAggregateResourceConfigResponse(BaseValidatorModel):
    BaseConfigurationItems: List[BaseConfigurationItem]
    UnprocessedResourceIdentifiers: List[AggregateResourceIdentifier]
    ResponseMetadata: ResponseMetadata


class BatchGetResourceConfigRequest(BaseValidatorModel):
    resourceKeys: Sequence[ResourceKey]


class BatchGetResourceConfigResponse(BaseValidatorModel):
    baseConfigurationItems: List[BaseConfigurationItem]
    unprocessedResourceKeys: List[ResourceKey]
    ResponseMetadata: ResponseMetadata


class DescribeRemediationExecutionStatusRequest(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKey]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class StartRemediationExecutionRequest(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[ResourceKey]


class StartRemediationExecutionResponse(BaseValidatorModel):
    FailureMessage: str
    FailedItems: List[ResourceKey]
    ResponseMetadata: ResponseMetadata


class ComplianceSummary(BaseValidatorModel):
    CompliantResourceCount: Optional[ComplianceContributorCount] = None
    NonCompliantResourceCount: Optional[ComplianceContributorCount] = None
    ComplianceSummaryTimestamp: Optional[datetime] = None


class Compliance(BaseValidatorModel):
    ComplianceType: Optional[ComplianceTypeType] = None
    ComplianceContributorCount: Optional[ComplianceContributorCount] = None


class DescribeAggregateComplianceByConfigRulesRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetAggregateConfigRuleComplianceSummaryRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceSummaryFilters] = None
    GroupByKey: Optional[ConfigRuleComplianceSummaryGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConfigRuleEvaluationStatusResponse(BaseValidatorModel):
    ConfigRulesEvaluationStatus: List[ConfigRuleEvaluationStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DeliveryChannel(BaseValidatorModel):
    name: Optional[str] = None
    s3BucketName: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    s3KmsKeyArn: Optional[str] = None
    snsTopicARN: Optional[str] = None
    configSnapshotDeliveryProperties: Optional[ConfigSnapshotDeliveryProperties] = None


class DeliveryChannelStatus(BaseValidatorModel):
    name: Optional[str] = None
    configSnapshotDeliveryInfo: Optional[ConfigExportDeliveryInfo] = None
    configHistoryDeliveryInfo: Optional[ConfigExportDeliveryInfo] = None
    configStreamDeliveryInfo: Optional[ConfigStreamDeliveryInfo] = None


class ConfigurationItem(BaseValidatorModel):
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
    relationships: Optional[List[Relationship]] = None
    configuration: Optional[str] = None
    supplementaryConfiguration: Optional[Dict[str, str]] = None
    recordingFrequency: Optional[RecordingFrequencyType] = None
    configurationItemDeliveryTime: Optional[datetime] = None


class ListConfigurationRecordersRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ConfigurationRecorderFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConfigurationRecorderStatusResponse(BaseValidatorModel):
    ConfigurationRecordersStatus: List[ConfigurationRecorderStatus]
    ResponseMetadata: ResponseMetadata


class ListConfigurationRecordersResponse(BaseValidatorModel):
    ConfigurationRecorderSummaries: List[ConfigurationRecorderSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeConformancePackComplianceRequest(BaseValidatorModel):
    ConformancePackName: str
    Filters: Optional[ConformancePackComplianceFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListConformancePackComplianceScoresResponse(BaseValidatorModel):
    ConformancePackComplianceScores: List[ConformancePackComplianceScore]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListConformancePackComplianceScoresRequest(BaseValidatorModel):
    Filters: Optional[ConformancePackComplianceScoresFilters] = None
    SortOrder: Optional[SortOrderType] = None
    SortBy: Optional[Literal["SCORE"]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetConformancePackComplianceSummaryResponse(BaseValidatorModel):
    ConformancePackComplianceSummaryList: List[ConformancePackComplianceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OrganizationConformancePack(BaseValidatorModel):
    OrganizationConformancePackName: str
    OrganizationConformancePackArn: str
    LastUpdateTime: datetime
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[List[ConformancePackInputParameter]] = None
    ExcludedAccounts: Optional[List[str]] = None


class PutOrganizationConformancePackRequest(BaseValidatorModel):
    OrganizationConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[Sequence[ConformancePackInputParameter]] = None
    ExcludedAccounts: Optional[Sequence[str]] = None


class ConformancePackDetail(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackArn: str
    ConformancePackId: str
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[List[ConformancePackInputParameter]] = None
    LastUpdateRequestedTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    TemplateSSMDocumentDetails: Optional[TemplateSSMDocumentDetails] = None


class PutConformancePackRequest(BaseValidatorModel):
    ConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[Sequence[ConformancePackInputParameter]] = None
    TemplateSSMDocumentDetails: Optional[TemplateSSMDocumentDetails] = None


class GetConformancePackComplianceDetailsRequest(BaseValidatorModel):
    ConformancePackName: str
    Filters: Optional[ConformancePackEvaluationFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConformancePackComplianceResponse(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackRuleComplianceList: List[ConformancePackRuleCompliance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeConformancePackStatusResponse(BaseValidatorModel):
    ConformancePackStatusDetails: List[ConformancePackStatusDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DeleteRemediationExceptionsRequest(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKey]


class DescribeRemediationExceptionsRequest(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[RemediationExceptionResourceKey]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class FailedDeleteRemediationExceptionsBatch(BaseValidatorModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationExceptionResourceKey]] = None


class DescribeAggregateComplianceByConfigRulesRequestPaginate(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAggregateComplianceByConformancePacksRequestPaginate(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAggregationAuthorizationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeComplianceByConfigRuleRequestPaginate(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeComplianceByResourceRequestPaginate(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConfigRuleEvaluationStatusRequestPaginate(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConfigurationAggregatorSourcesStatusRequestPaginate(BaseValidatorModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConfigurationAggregatorsRequestPaginate(BaseValidatorModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConformancePackStatusRequestPaginate(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConformancePacksRequestPaginate(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrganizationConfigRuleStatusesRequestPaginate(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrganizationConfigRulesRequestPaginate(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrganizationConformancePackStatusesRequestPaginate(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrganizationConformancePacksRequestPaginate(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePendingAggregationRequestsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRemediationExecutionStatusRequestPaginate(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKey]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRetentionConfigurationsRequestPaginate(BaseValidatorModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAggregateComplianceDetailsByConfigRuleRequestPaginate(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: Optional[ComplianceTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetComplianceDetailsByConfigRuleRequestPaginate(BaseValidatorModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetComplianceDetailsByResourceRequestPaginate(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    ResourceEvaluationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetConformancePackComplianceSummaryRequestPaginate(BaseValidatorModel):
    ConformancePackNames: Sequence[str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationRecordersRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ConfigurationRecorderFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDiscoveredResourcesRequestPaginate(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceIds: Optional[Sequence[str]] = None
    resourceName: Optional[str] = None
    includeDeletedResources: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class SelectAggregateResourceConfigRequestPaginate(BaseValidatorModel):
    Expression: str
    ConfigurationAggregatorName: str
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SelectResourceConfigRequestPaginate(BaseValidatorModel):
    Expression: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConfigRulesRequestPaginate(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    Filters: Optional[DescribeConfigRulesFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeConfigRulesRequest(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Filters: Optional[DescribeConfigRulesFilters] = None


class DescribeOrganizationConfigRuleStatusesResponse(BaseValidatorModel):
    OrganizationConfigRuleStatuses: List[OrganizationConfigRuleStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOrganizationConformancePackStatusesResponse(BaseValidatorModel):
    OrganizationConformancePackStatuses: List[OrganizationConformancePackStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePendingAggregationRequestsResponse(BaseValidatorModel):
    PendingAggregationRequests: List[PendingAggregationRequest]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeRemediationExceptionsResponse(BaseValidatorModel):
    RemediationExceptions: List[RemediationException]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FailedRemediationExceptionBatch(BaseValidatorModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationException]] = None


class DescribeRetentionConfigurationsResponse(BaseValidatorModel):
    RetentionConfigurations: List[RetentionConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutRetentionConfigurationResponse(BaseValidatorModel):
    RetentionConfiguration: RetentionConfiguration
    ResponseMetadata: ResponseMetadata


class PutEvaluationsResponse(BaseValidatorModel):
    FailedEvaluations: List[EvaluationOutput]
    ResponseMetadata: ResponseMetadata


class EvaluationResultIdentifier(BaseValidatorModel):
    EvaluationResultQualifier: Optional[EvaluationResultQualifier] = None
    OrderingTimestamp: Optional[datetime] = None
    ResourceEvaluationId: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class Evaluation(BaseValidatorModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: Timestamp
    Annotation: Optional[str] = None


class ExternalEvaluation(BaseValidatorModel):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceTypeType
    OrderingTimestamp: Timestamp
    Annotation: Optional[str] = None


class GetResourceConfigHistoryRequestPaginate(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[Timestamp] = None
    earlierTime: Optional[Timestamp] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourceConfigHistoryRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[Timestamp] = None
    earlierTime: Optional[Timestamp] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class PutRemediationExceptionsRequest(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKey]
    Message: Optional[str] = None
    ExpirationTime: Optional[Timestamp] = None


class TimeWindow(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class ExecutionControls(BaseValidatorModel):
    SsmControls: Optional[SsmControls] = None


class QueryInfo(BaseValidatorModel):
    SelectFields: Optional[List[FieldInfo]] = None


class GetAggregateDiscoveredResourceCountsRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ResourceCountFilters] = None
    GroupByKey: Optional[ResourceCountGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetAggregateDiscoveredResourceCountsResponse(BaseValidatorModel):
    TotalDiscoveredResources: int
    GroupByKey: str
    GroupedResourceCounts: List[GroupedResourceCount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDiscoveredResourceCountsResponse(BaseValidatorModel):
    totalDiscoveredResources: int
    resourceCounts: List[ResourceCount]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetOrganizationConfigRuleDetailedStatusRequestPaginate(BaseValidatorModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetOrganizationConfigRuleDetailedStatusRequest(BaseValidatorModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetOrganizationConfigRuleDetailedStatusResponse(BaseValidatorModel):
    OrganizationConfigRuleDetailedStatus: List[MemberAccountStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetOrganizationConformancePackDetailedStatusRequestPaginate(BaseValidatorModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetOrganizationConformancePackDetailedStatusRequest(BaseValidatorModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetOrganizationConformancePackDetailedStatusResponse(BaseValidatorModel):
    OrganizationConformancePackDetailedStatuses: List[ OrganizationConformancePackDetailedStatus ]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetResourceEvaluationSummaryResponse(BaseValidatorModel):
    ResourceEvaluationId: str
    EvaluationMode: EvaluationModeType
    EvaluationStatus: EvaluationStatus
    EvaluationStartTimestamp: datetime
    Compliance: ComplianceTypeType
    EvaluationContext: EvaluationContext
    ResourceDetails: ResourceDetails
    ResponseMetadata: ResponseMetadata


class StartResourceEvaluationRequest(BaseValidatorModel):
    ResourceDetails: ResourceDetails
    EvaluationMode: EvaluationModeType
    EvaluationContext: Optional[EvaluationContext] = None
    EvaluationTimeout: Optional[int] = None
    ClientToken: Optional[str] = None


class GetStoredQueryResponse(BaseValidatorModel):
    StoredQuery: StoredQuery
    ResponseMetadata: ResponseMetadata


class ListAggregateDiscoveredResourcesRequestPaginate(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAggregateDiscoveredResourcesRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListDiscoveredResourcesResponse(BaseValidatorModel):
    resourceIdentifiers: List[ResourceIdentifier]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListResourceEvaluationsResponse(BaseValidatorModel):
    ResourceEvaluations: List[ResourceEvaluation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStoredQueriesResponse(BaseValidatorModel):
    StoredQueryMetadata: List[StoredQueryMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutAggregationAuthorizationRequest(BaseValidatorModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str
    Tags: Optional[Sequence[Tag]] = None


class PutServiceLinkedConfigurationRecorderRequest(BaseValidatorModel):
    ServicePrincipal: str
    Tags: Optional[Sequence[Tag]] = None


class PutStoredQueryRequest(BaseValidatorModel):
    StoredQuery: StoredQuery
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class OrganizationConfigRule(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationConfigRuleArn: str
    OrganizationManagedRuleMetadata: Optional[OrganizationManagedRuleMetadataOutput] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataOutput] = None
    ExcludedAccounts: Optional[List[str]] = None
    LastUpdateTime: Optional[datetime] = None
    OrganizationCustomPolicyRuleMetadata: Optional[ OrganizationCustomPolicyRuleMetadataNoPolicy ] = None


class RecordingGroupOutput(BaseValidatorModel):
    allSupported: Optional[bool] = None
    includeGlobalResourceTypes: Optional[bool] = None
    resourceTypes: Optional[List[ResourceTypeType]] = None
    exclusionByResourceTypes: Optional[ExclusionByResourceTypesOutput] = None
    recordingStrategy: Optional[RecordingStrategy] = None


class RecordingGroup(BaseValidatorModel):
    allSupported: Optional[bool] = None
    includeGlobalResourceTypes: Optional[bool] = None
    resourceTypes: Optional[Sequence[ResourceTypeType]] = None
    exclusionByResourceTypes: Optional[ExclusionByResourceTypes] = None
    recordingStrategy: Optional[RecordingStrategy] = None


class RecordingModeOutput(BaseValidatorModel):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: Optional[List[RecordingModeOverrideOutput]] = None


class RecordingMode(BaseValidatorModel):
    recordingFrequency: RecordingFrequencyType
    recordingModeOverrides: Optional[Sequence[RecordingModeOverride]] = None


class RemediationExecutionStatus(BaseValidatorModel):
    ResourceKey: Optional[ResourceKey] = None
    State: Optional[RemediationExecutionStateType] = None
    StepDetails: Optional[List[RemediationExecutionStep]] = None
    InvocationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class RemediationParameterValueOutput(BaseValidatorModel):
    ResourceValue: Optional[ResourceValue] = None
    StaticValue: Optional[StaticValueOutput] = None


class SourceOutput(BaseValidatorModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[List[SourceDetail]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetails] = None


class Source(BaseValidatorModel):
    Owner: OwnerType
    SourceIdentifier: Optional[str] = None
    SourceDetails: Optional[Sequence[SourceDetail]] = None
    CustomPolicyDetails: Optional[CustomPolicyDetails] = None


class DescribeAggregateComplianceByConformancePacksResponse(BaseValidatorModel):
    AggregateComplianceByConformancePacks: List[AggregateComplianceByConformancePack]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetAggregateConformancePackComplianceSummaryResponse(BaseValidatorModel):
    AggregateConformancePackComplianceSummaries: List[ AggregateConformancePackComplianceSummary ]
    GroupByKey: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConfigurationAggregator(BaseValidatorModel):
    ConfigurationAggregatorName: Optional[str] = None
    ConfigurationAggregatorArn: Optional[str] = None
    AccountAggregationSources: Optional[List[AccountAggregationSourceOutput]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceOutput] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    AggregatorFilters: Optional[AggregatorFiltersOutput] = None


class AggregateComplianceCount(BaseValidatorModel):
    GroupName: Optional[str] = None
    ComplianceSummary: Optional[ComplianceSummary] = None


class ComplianceSummaryByResourceType(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ComplianceSummary: Optional[ComplianceSummary] = None


class GetComplianceSummaryByConfigRuleResponse(BaseValidatorModel):
    ComplianceSummary: ComplianceSummary
    ResponseMetadata: ResponseMetadata


class AggregateComplianceByConfigRule(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    Compliance: Optional[Compliance] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None


class ComplianceByConfigRule(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None
    Compliance: Optional[Compliance] = None


class ComplianceByResource(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    Compliance: Optional[Compliance] = None


class DescribeDeliveryChannelsResponse(BaseValidatorModel):
    DeliveryChannels: List[DeliveryChannel]
    ResponseMetadata: ResponseMetadata


class PutDeliveryChannelRequest(BaseValidatorModel):
    DeliveryChannel: DeliveryChannel


class DescribeDeliveryChannelStatusResponse(BaseValidatorModel):
    DeliveryChannelsStatus: List[DeliveryChannelStatus]
    ResponseMetadata: ResponseMetadata


class GetAggregateResourceConfigResponse(BaseValidatorModel):
    ConfigurationItem: ConfigurationItem
    ResponseMetadata: ResponseMetadata


class GetResourceConfigHistoryResponse(BaseValidatorModel):
    configurationItems: List[ConfigurationItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeOrganizationConformancePacksResponse(BaseValidatorModel):
    OrganizationConformancePacks: List[OrganizationConformancePack]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeConformancePacksResponse(BaseValidatorModel):
    ConformancePackDetails: List[ConformancePackDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DeleteRemediationExceptionsResponse(BaseValidatorModel):
    FailedBatches: List[FailedDeleteRemediationExceptionsBatch]
    ResponseMetadata: ResponseMetadata


class PutRemediationExceptionsResponse(BaseValidatorModel):
    FailedBatches: List[FailedRemediationExceptionBatch]
    ResponseMetadata: ResponseMetadata


class AggregateEvaluationResult(BaseValidatorModel):
    EvaluationResultIdentifier: Optional[EvaluationResultIdentifier] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    ResultRecordedTime: Optional[datetime] = None
    ConfigRuleInvokedTime: Optional[datetime] = None
    Annotation: Optional[str] = None
    AccountId: Optional[str] = None
    AwsRegion: Optional[str] = None


class ConformancePackEvaluationResult(BaseValidatorModel):
    ComplianceType: ConformancePackComplianceTypeType
    EvaluationResultIdentifier: EvaluationResultIdentifier
    ConfigRuleInvokedTime: datetime
    ResultRecordedTime: datetime
    Annotation: Optional[str] = None


class EvaluationResult(BaseValidatorModel):
    EvaluationResultIdentifier: Optional[EvaluationResultIdentifier] = None
    ComplianceType: Optional[ComplianceTypeType] = None
    ResultRecordedTime: Optional[datetime] = None
    ConfigRuleInvokedTime: Optional[datetime] = None
    Annotation: Optional[str] = None
    ResultToken: Optional[str] = None


class PutExternalEvaluationRequest(BaseValidatorModel):
    ConfigRuleName: str
    ExternalEvaluation: ExternalEvaluation


class ResourceEvaluationFilters(BaseValidatorModel):
    EvaluationMode: Optional[EvaluationModeType] = None
    TimeWindow: Optional[TimeWindow] = None
    EvaluationContextIdentifier: Optional[str] = None


class SelectAggregateResourceConfigResponse(BaseValidatorModel):
    Results: List[str]
    QueryInfo: QueryInfo
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SelectResourceConfigResponse(BaseValidatorModel):
    Results: List[str]
    QueryInfo: QueryInfo
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeOrganizationConfigRulesResponse(BaseValidatorModel):
    OrganizationConfigRules: List[OrganizationConfigRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OrganizationManagedRuleMetadataUnion(BaseValidatorModel):
    pass


class OrganizationCustomRuleMetadataUnion(BaseValidatorModel):
    pass


class PutOrganizationConfigRuleRequest(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationManagedRuleMetadata: Optional[OrganizationManagedRuleMetadataUnion] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataUnion] = None
    ExcludedAccounts: Optional[Sequence[str]] = None
    OrganizationCustomPolicyRuleMetadata: Optional[OrganizationCustomPolicyRuleMetadata] = None


class ConfigurationRecorderOutput(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroupOutput] = None
    recordingMode: Optional[RecordingModeOutput] = None
    recordingScope: Optional[RecordingScopeType] = None
    servicePrincipal: Optional[str] = None


class ConfigurationRecorder(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroup] = None
    recordingMode: Optional[RecordingMode] = None
    recordingScope: Optional[RecordingScopeType] = None
    servicePrincipal: Optional[str] = None


class DescribeRemediationExecutionStatusResponse(BaseValidatorModel):
    RemediationExecutionStatuses: List[RemediationExecutionStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RemediationConfigurationOutput(BaseValidatorModel):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str
    TargetVersion: Optional[str] = None
    Parameters: Optional[Dict[str, RemediationParameterValueOutput]] = None
    ResourceType: Optional[str] = None
    Automatic: Optional[bool] = None
    ExecutionControls: Optional[ExecutionControls] = None
    MaximumAutomaticAttempts: Optional[int] = None
    RetryAttemptSeconds: Optional[int] = None
    Arn: Optional[str] = None
    CreatedByService: Optional[str] = None


class ConfigRuleOutput(BaseValidatorModel):
    Source: SourceOutput
    ConfigRuleName: Optional[str] = None
    ConfigRuleArn: Optional[str] = None
    ConfigRuleId: Optional[str] = None
    Description: Optional[str] = None
    Scope: Optional[ScopeOutput] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ConfigRuleState: Optional[ConfigRuleStateType] = None
    CreatedBy: Optional[str] = None
    EvaluationModes: Optional[List[EvaluationModeConfiguration]] = None


class ConfigRule(BaseValidatorModel):
    Source: Source
    ConfigRuleName: Optional[str] = None
    ConfigRuleArn: Optional[str] = None
    ConfigRuleId: Optional[str] = None
    Description: Optional[str] = None
    Scope: Optional[Scope] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ConfigRuleState: Optional[ConfigRuleStateType] = None
    CreatedBy: Optional[str] = None
    EvaluationModes: Optional[Sequence[EvaluationModeConfiguration]] = None


class StaticValueUnion(BaseValidatorModel):
    pass


class RemediationParameterValue(BaseValidatorModel):
    ResourceValue: Optional[ResourceValue] = None
    StaticValue: Optional[StaticValueUnion] = None


class DescribeConfigurationAggregatorsResponse(BaseValidatorModel):
    ConfigurationAggregators: List[ConfigurationAggregator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutConfigurationAggregatorResponse(BaseValidatorModel):
    ConfigurationAggregator: ConfigurationAggregator
    ResponseMetadata: ResponseMetadata


class AggregatorFiltersUnion(BaseValidatorModel):
    pass


class OrganizationAggregationSourceUnion(BaseValidatorModel):
    pass


class AccountAggregationSourceUnion(BaseValidatorModel):
    pass


class PutConfigurationAggregatorRequest(BaseValidatorModel):
    ConfigurationAggregatorName: str
    AccountAggregationSources: Optional[Sequence[AccountAggregationSourceUnion]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceUnion] = None
    Tags: Optional[Sequence[Tag]] = None
    AggregatorFilters: Optional[AggregatorFiltersUnion] = None


class GetAggregateConfigRuleComplianceSummaryResponse(BaseValidatorModel):
    GroupByKey: str
    AggregateComplianceCounts: List[AggregateComplianceCount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetComplianceSummaryByResourceTypeResponse(BaseValidatorModel):
    ComplianceSummariesByResourceType: List[ComplianceSummaryByResourceType]
    ResponseMetadata: ResponseMetadata


class DescribeAggregateComplianceByConfigRulesResponse(BaseValidatorModel):
    AggregateComplianceByConfigRules: List[AggregateComplianceByConfigRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeComplianceByConfigRuleResponse(BaseValidatorModel):
    ComplianceByConfigRules: List[ComplianceByConfigRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeComplianceByResourceResponse(BaseValidatorModel):
    ComplianceByResources: List[ComplianceByResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetAggregateComplianceDetailsByConfigRuleResponse(BaseValidatorModel):
    AggregateEvaluationResults: List[AggregateEvaluationResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetConformancePackComplianceDetailsResponse(BaseValidatorModel):
    ConformancePackName: str
    ConformancePackRuleEvaluationResults: List[ConformancePackEvaluationResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetComplianceDetailsByConfigRuleResponse(BaseValidatorModel):
    EvaluationResults: List[EvaluationResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetComplianceDetailsByResourceResponse(BaseValidatorModel):
    EvaluationResults: List[EvaluationResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EvaluationUnion(BaseValidatorModel):
    pass


class PutEvaluationsRequest(BaseValidatorModel):
    ResultToken: str
    Evaluations: Optional[Sequence[EvaluationUnion]] = None
    TestMode: Optional[bool] = None


class ListResourceEvaluationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[ResourceEvaluationFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceEvaluationsRequest(BaseValidatorModel):
    Filters: Optional[ResourceEvaluationFilters] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class AssociateResourceTypesResponse(BaseValidatorModel):
    ConfigurationRecorder: ConfigurationRecorderOutput
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationRecordersResponse(BaseValidatorModel):
    ConfigurationRecorders: List[ConfigurationRecorderOutput]
    ResponseMetadata: ResponseMetadata


class DisassociateResourceTypesResponse(BaseValidatorModel):
    ConfigurationRecorder: ConfigurationRecorderOutput
    ResponseMetadata: ResponseMetadata


class DescribeRemediationConfigurationsResponse(BaseValidatorModel):
    RemediationConfigurations: List[RemediationConfigurationOutput]
    ResponseMetadata: ResponseMetadata


class FailedRemediationBatch(BaseValidatorModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationConfigurationOutput]] = None


class DescribeConfigRulesResponse(BaseValidatorModel):
    ConfigRules: List[ConfigRuleOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConfigurationRecorderUnion(BaseValidatorModel):
    pass


class PutConfigurationRecorderRequest(BaseValidatorModel):
    ConfigurationRecorder: ConfigurationRecorderUnion
    Tags: Optional[Sequence[Tag]] = None


class PutRemediationConfigurationsResponse(BaseValidatorModel):
    FailedBatches: List[FailedRemediationBatch]
    ResponseMetadata: ResponseMetadata


class ConfigRuleUnion(BaseValidatorModel):
    pass


class PutConfigRuleRequest(BaseValidatorModel):
    ConfigRule: ConfigRuleUnion
    Tags: Optional[Sequence[Tag]] = None


class RemediationParameterValueUnion(BaseValidatorModel):
    pass


class RemediationConfiguration(BaseValidatorModel):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str
    TargetVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, RemediationParameterValueUnion]] = None
    ResourceType: Optional[str] = None
    Automatic: Optional[bool] = None
    ExecutionControls: Optional[ExecutionControls] = None
    MaximumAutomaticAttempts: Optional[int] = None
    RetryAttemptSeconds: Optional[int] = None
    Arn: Optional[str] = None
    CreatedByService: Optional[str] = None


class RemediationConfigurationUnion(BaseValidatorModel):
    pass


class PutRemediationConfigurationsRequest(BaseValidatorModel):
    RemediationConfigurations: Sequence[RemediationConfigurationUnion]


