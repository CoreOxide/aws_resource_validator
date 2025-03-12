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


class AssociateResourceTypesRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderArn: str
    ResourceTypes: Sequence[ResourceTypeType]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class ConfigurationRecorderFilterTypeDef(BaseValidatorModel):
    filterName: Optional[Literal["recordingScope"]] = None
    filterValue: Optional[Sequence[str]] = None


class ConfigurationRecorderStatusTypeDef(BaseValidatorModel):
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


class ConfigurationRecorderSummaryTypeDef(BaseValidatorModel):
    arn: str
    name: str
    recordingScope: RecordingScopeType
    servicePrincipal: Optional[str] = None


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


class DeleteAggregationAuthorizationRequestTypeDef(BaseValidatorModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str


class DeleteConfigRuleRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str


class DeleteConfigurationAggregatorRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str


class DeleteConfigurationRecorderRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderName: str


class DeleteConformancePackRequestTypeDef(BaseValidatorModel):
    ConformancePackName: str


class DeleteDeliveryChannelRequestTypeDef(BaseValidatorModel):
    DeliveryChannelName: str


class DeleteEvaluationResultsRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str


class DeleteOrganizationConfigRuleRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str


class DeleteOrganizationConformancePackRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str


class DeletePendingAggregationRequestRequestTypeDef(BaseValidatorModel):
    RequesterAccountId: str
    RequesterAwsRegion: str


class DeleteRemediationConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceType: Optional[str] = None


class RemediationExceptionResourceKeyTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None


class DeleteResourceConfigRequestTypeDef(BaseValidatorModel):
    ResourceType: str
    ResourceId: str


class DeleteRetentionConfigurationRequestTypeDef(BaseValidatorModel):
    RetentionConfigurationName: str


class DeleteServiceLinkedConfigurationRecorderRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: str


class DeleteStoredQueryRequestTypeDef(BaseValidatorModel):
    QueryName: str


class DeliverConfigSnapshotRequestTypeDef(BaseValidatorModel):
    deliveryChannelName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAggregationAuthorizationsRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeComplianceByConfigRuleRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None


class DescribeComplianceByResourceRequestTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConfigRuleEvaluationStatusRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeConfigRulesFiltersTypeDef(BaseValidatorModel):
    EvaluationMode: Optional[EvaluationModeType] = None


class DescribeConfigurationAggregatorSourcesStatusRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeConfigurationAggregatorsRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeConfigurationRecorderStatusRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None
    ServicePrincipal: Optional[str] = None
    Arn: Optional[str] = None


class DescribeConfigurationRecordersRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderNames: Optional[Sequence[str]] = None
    ServicePrincipal: Optional[str] = None
    Arn: Optional[str] = None


class DescribeConformancePackStatusRequestTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConformancePacksRequestTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDeliveryChannelStatusRequestTypeDef(BaseValidatorModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None


class DescribeDeliveryChannelsRequestTypeDef(BaseValidatorModel):
    DeliveryChannelNames: Optional[Sequence[str]] = None


class DescribeOrganizationConfigRuleStatusesRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class OrganizationConfigRuleStatusTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationRuleStatus: OrganizationRuleStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class DescribeOrganizationConfigRulesRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeOrganizationConformancePackStatusesRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class OrganizationConformancePackStatusTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    Status: OrganizationResourceStatusType
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None


class DescribeOrganizationConformancePacksRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePendingAggregationRequestsRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class PendingAggregationRequestTypeDef(BaseValidatorModel):
    RequesterAccountId: Optional[str] = None
    RequesterAwsRegion: Optional[str] = None


class DescribeRemediationConfigurationsRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Sequence[str]


class RemediationExceptionTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceType: str
    ResourceId: str
    Message: Optional[str] = None
    ExpirationTime: Optional[datetime] = None


class DescribeRetentionConfigurationsRequestTypeDef(BaseValidatorModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None


class RetentionConfigurationTypeDef(BaseValidatorModel):
    Name: str
    RetentionPeriodInDays: int


class DisassociateResourceTypesRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderArn: str
    ResourceTypes: Sequence[ResourceTypeType]


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


class GetAggregateComplianceDetailsByConfigRuleRequestTypeDef(BaseValidatorModel):
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


class GetComplianceDetailsByConfigRuleRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetComplianceDetailsByResourceRequestTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    NextToken: Optional[str] = None
    ResourceEvaluationId: Optional[str] = None


class GetComplianceSummaryByResourceTypeRequestTypeDef(BaseValidatorModel):
    ResourceTypes: Optional[Sequence[str]] = None


class GetConformancePackComplianceSummaryRequestTypeDef(BaseValidatorModel):
    ConformancePackNames: Sequence[str]
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetCustomRulePolicyRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: Optional[str] = None


class GetDiscoveredResourceCountsRequestTypeDef(BaseValidatorModel):
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


class GetOrganizationCustomRulePolicyRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str


class GetResourceEvaluationSummaryRequestTypeDef(BaseValidatorModel):
    ResourceEvaluationId: str


class ResourceDetailsTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceType: str
    ResourceConfiguration: str
    ResourceConfigurationSchemaType: Optional[Literal["CFN_RESOURCE_SCHEMA"]] = None


class GetStoredQueryRequestTypeDef(BaseValidatorModel):
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


class ListDiscoveredResourcesRequestTypeDef(BaseValidatorModel):
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


class ListStoredQueriesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StoredQueryMetadataTypeDef(BaseValidatorModel):
    QueryId: str
    QueryArn: str
    QueryName: str
    Description: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class OrganizationAggregationSourceTypeDef(BaseValidatorModel):
    RoleArn: str
    AwsRegions: Optional[Sequence[str]] = None
    AllAwsRegions: Optional[bool] = None


class OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef(BaseValidatorModel):
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
    OrganizationConfigRuleTriggerTypes: Optional[ Sequence[OrganizationConfigRuleTriggerTypeNoSNType] ] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None
    DebugLogDeliveryAccounts: Optional[Sequence[str]] = None


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


class OrganizationManagedRuleMetadataTypeDef(BaseValidatorModel):
    RuleIdentifier: str
    Description: Optional[str] = None
    InputParameters: Optional[str] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None
    ResourceTypesScope: Optional[Sequence[str]] = None
    ResourceIdScope: Optional[str] = None
    TagKeyScope: Optional[str] = None
    TagValueScope: Optional[str] = None


class PutResourceConfigRequestTypeDef(BaseValidatorModel):
    ResourceType: str
    SchemaVersionId: str
    ResourceId: str
    Configuration: str
    ResourceName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class PutRetentionConfigurationRequestTypeDef(BaseValidatorModel):
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


class SelectAggregateResourceConfigRequestTypeDef(BaseValidatorModel):
    Expression: str
    ConfigurationAggregatorName: str
    Limit: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SelectResourceConfigRequestTypeDef(BaseValidatorModel):
    Expression: str
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class SourceDetailTypeDef(BaseValidatorModel):
    EventSource: Optional[Literal["aws.config"]] = None
    MessageType: Optional[MessageTypeType] = None
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequencyType] = None


class StartConfigRulesEvaluationRequestTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None


class StartConfigurationRecorderRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderName: str


class StaticValueTypeDef(BaseValidatorModel):
    Values: Sequence[str]


class StopConfigurationRecorderRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorderName: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
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


class DescribeAggregateComplianceByConformancePacksRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetAggregateConformancePackComplianceSummaryRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceSummaryFiltersTypeDef] = None
    GroupByKey: Optional[AggregateConformancePackComplianceSummaryGroupKeyType] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class BatchGetAggregateResourceConfigRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceIdentifiers: Sequence[AggregateResourceIdentifierTypeDef]


class GetAggregateResourceConfigRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceIdentifier: AggregateResourceIdentifierTypeDef


class AggregatorFilterResourceTypeOutputTypeDef(BaseValidatorModel):
    pass


class AggregatorFilterServicePrincipalOutputTypeDef(BaseValidatorModel):
    pass


class AggregatorFiltersOutputTypeDef(BaseValidatorModel):
    ResourceType: Optional[AggregatorFilterResourceTypeOutputTypeDef] = None
    ServicePrincipal: Optional[AggregatorFilterServicePrincipalOutputTypeDef] = None


class AggregatorFilterServicePrincipalTypeDef(BaseValidatorModel):
    pass


class AggregatorFilterResourceTypeTypeDef(BaseValidatorModel):
    pass


class AggregatorFiltersTypeDef(BaseValidatorModel):
    ResourceType: Optional[AggregatorFilterResourceTypeTypeDef] = None
    ServicePrincipal: Optional[AggregatorFilterServicePrincipalTypeDef] = None


class DeleteServiceLinkedConfigurationRecorderResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
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


class PutServiceLinkedConfigurationRecorderResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutStoredQueryResponseTypeDef(BaseValidatorModel):
    QueryArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartResourceEvaluationResponseTypeDef(BaseValidatorModel):
    ResourceEvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetAggregateResourceConfigResponseTypeDef(BaseValidatorModel):
    BaseConfigurationItems: List[BaseConfigurationItemTypeDef]
    UnprocessedResourceIdentifiers: List[AggregateResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetResourceConfigRequestTypeDef(BaseValidatorModel):
    resourceKeys: Sequence[ResourceKeyTypeDef]


class BatchGetResourceConfigResponseTypeDef(BaseValidatorModel):
    baseConfigurationItems: List[BaseConfigurationItemTypeDef]
    unprocessedResourceKeys: List[ResourceKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRemediationExecutionStatusRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKeyTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class StartRemediationExecutionRequestTypeDef(BaseValidatorModel):
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


class DescribeAggregateComplianceByConfigRulesRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetAggregateConfigRuleComplianceSummaryRequestTypeDef(BaseValidatorModel):
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


class ListConfigurationRecordersRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ConfigurationRecorderFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeConfigurationRecorderStatusResponseTypeDef(BaseValidatorModel):
    ConfigurationRecordersStatus: List[ConfigurationRecorderStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListConfigurationRecordersResponseTypeDef(BaseValidatorModel):
    ConfigurationRecorderSummaries: List[ConfigurationRecorderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeConformancePackComplianceRequestTypeDef(BaseValidatorModel):
    ConformancePackName: str
    Filters: Optional[ConformancePackComplianceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListConformancePackComplianceScoresResponseTypeDef(BaseValidatorModel):
    ConformancePackComplianceScores: List[ConformancePackComplianceScoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListConformancePackComplianceScoresRequestTypeDef(BaseValidatorModel):
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


class PutOrganizationConformancePackRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[Sequence[ConformancePackInputParameterTypeDef]] = None
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


class PutConformancePackRequestTypeDef(BaseValidatorModel):
    ConformancePackName: str
    TemplateS3Uri: Optional[str] = None
    TemplateBody: Optional[str] = None
    DeliveryS3Bucket: Optional[str] = None
    DeliveryS3KeyPrefix: Optional[str] = None
    ConformancePackInputParameters: Optional[Sequence[ConformancePackInputParameterTypeDef]] = None
    TemplateSSMDocumentDetails: Optional[TemplateSSMDocumentDetailsTypeDef] = None


class GetConformancePackComplianceDetailsRequestTypeDef(BaseValidatorModel):
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


class DeleteRemediationExceptionsRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Sequence[RemediationExceptionResourceKeyTypeDef]


class DescribeRemediationExceptionsRequestTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[RemediationExceptionResourceKeyTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class FailedDeleteRemediationExceptionsBatchTypeDef(BaseValidatorModel):
    FailureMessage: Optional[str] = None
    FailedItems: Optional[List[RemediationExceptionResourceKeyTypeDef]] = None


class DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[ConfigRuleComplianceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    Filters: Optional[AggregateConformancePackComplianceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAggregationAuthorizationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeComplianceByConfigRuleRequestPaginateTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeComplianceByResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    UpdateStatus: Optional[Sequence[AggregatedSourceStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConfigurationAggregatorsRequestPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConformancePackStatusRequestPaginateTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConformancePacksRequestPaginateTypeDef(BaseValidatorModel):
    ConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOrganizationConfigRulesRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationConfigRuleNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOrganizationConformancePacksRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationConformancePackNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePendingAggregationRequestsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRemediationExecutionStatusRequestPaginateTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ResourceKeys: Optional[Sequence[ResourceKeyTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRetentionConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    RetentionConfigurationNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ConfigRuleName: str
    AccountId: str
    AwsRegion: str
    ComplianceType: Optional[ComplianceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetComplianceDetailsByConfigRuleRequestPaginateTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetComplianceDetailsByResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ComplianceTypes: Optional[Sequence[ComplianceTypeType]] = None
    ResourceEvaluationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetConformancePackComplianceSummaryRequestPaginateTypeDef(BaseValidatorModel):
    ConformancePackNames: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfigurationRecordersRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ConfigurationRecorderFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDiscoveredResourcesRequestPaginateTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceIds: Optional[Sequence[str]] = None
    resourceName: Optional[str] = None
    includeDeletedResources: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SelectAggregateResourceConfigRequestPaginateTypeDef(BaseValidatorModel):
    Expression: str
    ConfigurationAggregatorName: str
    MaxResults: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SelectResourceConfigRequestPaginateTypeDef(BaseValidatorModel):
    Expression: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConfigRulesRequestPaginateTypeDef(BaseValidatorModel):
    ConfigRuleNames: Optional[Sequence[str]] = None
    Filters: Optional[DescribeConfigRulesFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeConfigRulesRequestTypeDef(BaseValidatorModel):
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


class TimestampTypeDef(BaseValidatorModel):
    pass


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


class GetResourceConfigHistoryRequestPaginateTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[TimestampTypeDef] = None
    earlierTime: Optional[TimestampTypeDef] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourceConfigHistoryRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceId: str
    laterTime: Optional[TimestampTypeDef] = None
    earlierTime: Optional[TimestampTypeDef] = None
    chronologicalOrder: Optional[ChronologicalOrderType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class PutRemediationExceptionsRequestTypeDef(BaseValidatorModel):
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


class GetAggregateDiscoveredResourceCountsRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetOrganizationConfigRuleDetailedStatusRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    Filters: Optional[StatusDetailFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetOrganizationConfigRuleDetailedStatusResponseTypeDef(BaseValidatorModel):
    OrganizationConfigRuleDetailedStatus: List[MemberAccountStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetOrganizationConformancePackDetailedStatusRequestTypeDef(BaseValidatorModel):
    OrganizationConformancePackName: str
    Filters: Optional[OrganizationResourceDetailedStatusFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class GetOrganizationConformancePackDetailedStatusResponseTypeDef(BaseValidatorModel):
    OrganizationConformancePackDetailedStatuses: List[ OrganizationConformancePackDetailedStatusTypeDef ]
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


class StartResourceEvaluationRequestTypeDef(BaseValidatorModel):
    ResourceDetails: ResourceDetailsTypeDef
    EvaluationMode: EvaluationModeType
    EvaluationContext: Optional[EvaluationContextTypeDef] = None
    EvaluationTimeout: Optional[int] = None
    ClientToken: Optional[str] = None


class GetStoredQueryResponseTypeDef(BaseValidatorModel):
    StoredQuery: StoredQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAggregateDiscoveredResourcesRequestPaginateTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAggregateDiscoveredResourcesRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    ResourceType: ResourceTypeType
    Filters: Optional[ResourceFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class ListDiscoveredResourcesResponseTypeDef(BaseValidatorModel):
    resourceIdentifiers: List[ResourceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class PutAggregationAuthorizationRequestTypeDef(BaseValidatorModel):
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class PutServiceLinkedConfigurationRecorderRequestTypeDef(BaseValidatorModel):
    ServicePrincipal: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class PutStoredQueryRequestTypeDef(BaseValidatorModel):
    StoredQuery: StoredQueryTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class OrganizationConfigRuleTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationConfigRuleArn: str
    OrganizationManagedRuleMetadata: Optional[OrganizationManagedRuleMetadataOutputTypeDef] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataOutputTypeDef] = None
    ExcludedAccounts: Optional[List[str]] = None
    LastUpdateTime: Optional[datetime] = None
    OrganizationCustomPolicyRuleMetadata: Optional[ OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef ] = None


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


class DescribeAggregateComplianceByConformancePacksResponseTypeDef(BaseValidatorModel):
    AggregateComplianceByConformancePacks: List[AggregateComplianceByConformancePackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetAggregateConformancePackComplianceSummaryResponseTypeDef(BaseValidatorModel):
    AggregateConformancePackComplianceSummaries: List[ AggregateConformancePackComplianceSummaryTypeDef ]
    GroupByKey: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ConfigurationAggregatorTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: Optional[str] = None
    ConfigurationAggregatorArn: Optional[str] = None
    AccountAggregationSources: Optional[List[AccountAggregationSourceOutputTypeDef]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceOutputTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    AggregatorFilters: Optional[AggregatorFiltersOutputTypeDef] = None


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


class PutDeliveryChannelRequestTypeDef(BaseValidatorModel):
    DeliveryChannel: DeliveryChannelTypeDef


class DescribeDeliveryChannelStatusResponseTypeDef(BaseValidatorModel):
    DeliveryChannelsStatus: List[DeliveryChannelStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetAggregateResourceConfigResponseTypeDef(BaseValidatorModel):
    ConfigurationItem: ConfigurationItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceConfigHistoryResponseTypeDef(BaseValidatorModel):
    configurationItems: List[ConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class PutExternalEvaluationRequestTypeDef(BaseValidatorModel):
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


class OrganizationManagedRuleMetadataUnionTypeDef(BaseValidatorModel):
    pass


class OrganizationCustomRuleMetadataUnionTypeDef(BaseValidatorModel):
    pass


class PutOrganizationConfigRuleRequestTypeDef(BaseValidatorModel):
    OrganizationConfigRuleName: str
    OrganizationManagedRuleMetadata: Optional[OrganizationManagedRuleMetadataUnionTypeDef] = None
    OrganizationCustomRuleMetadata: Optional[OrganizationCustomRuleMetadataUnionTypeDef] = None
    ExcludedAccounts: Optional[Sequence[str]] = None
    OrganizationCustomPolicyRuleMetadata: Optional[OrganizationCustomPolicyRuleMetadataTypeDef] = None


class ConfigurationRecorderOutputTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroupOutputTypeDef] = None
    recordingMode: Optional[RecordingModeOutputTypeDef] = None
    recordingScope: Optional[RecordingScopeType] = None
    servicePrincipal: Optional[str] = None


class ConfigurationRecorderTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    roleARN: Optional[str] = None
    recordingGroup: Optional[RecordingGroupTypeDef] = None
    recordingMode: Optional[RecordingModeTypeDef] = None
    recordingScope: Optional[RecordingScopeType] = None
    servicePrincipal: Optional[str] = None


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


class StaticValueUnionTypeDef(BaseValidatorModel):
    pass


class RemediationParameterValueTypeDef(BaseValidatorModel):
    ResourceValue: Optional[ResourceValueTypeDef] = None
    StaticValue: Optional[StaticValueUnionTypeDef] = None


class DescribeConfigurationAggregatorsResponseTypeDef(BaseValidatorModel):
    ConfigurationAggregators: List[ConfigurationAggregatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutConfigurationAggregatorResponseTypeDef(BaseValidatorModel):
    ConfigurationAggregator: ConfigurationAggregatorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AggregatorFiltersUnionTypeDef(BaseValidatorModel):
    pass


class OrganizationAggregationSourceUnionTypeDef(BaseValidatorModel):
    pass


class AccountAggregationSourceUnionTypeDef(BaseValidatorModel):
    pass


class PutConfigurationAggregatorRequestTypeDef(BaseValidatorModel):
    ConfigurationAggregatorName: str
    AccountAggregationSources: Optional[Sequence[AccountAggregationSourceUnionTypeDef]] = None
    OrganizationAggregationSource: Optional[OrganizationAggregationSourceUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AggregatorFilters: Optional[AggregatorFiltersUnionTypeDef] = None


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


class EvaluationUnionTypeDef(BaseValidatorModel):
    pass


class PutEvaluationsRequestTypeDef(BaseValidatorModel):
    ResultToken: str
    Evaluations: Optional[Sequence[EvaluationUnionTypeDef]] = None
    TestMode: Optional[bool] = None


class ListResourceEvaluationsRequestPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[ResourceEvaluationFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceEvaluationsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[ResourceEvaluationFiltersTypeDef] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class AssociateResourceTypesResponseTypeDef(BaseValidatorModel):
    ConfigurationRecorder: ConfigurationRecorderOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConfigurationRecordersResponseTypeDef(BaseValidatorModel):
    ConfigurationRecorders: List[ConfigurationRecorderOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateResourceTypesResponseTypeDef(BaseValidatorModel):
    ConfigurationRecorder: ConfigurationRecorderOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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


class ConfigurationRecorderUnionTypeDef(BaseValidatorModel):
    pass


class PutConfigurationRecorderRequestTypeDef(BaseValidatorModel):
    ConfigurationRecorder: ConfigurationRecorderUnionTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class PutRemediationConfigurationsResponseTypeDef(BaseValidatorModel):
    FailedBatches: List[FailedRemediationBatchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ConfigRuleUnionTypeDef(BaseValidatorModel):
    pass


class PutConfigRuleRequestTypeDef(BaseValidatorModel):
    ConfigRule: ConfigRuleUnionTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class RemediationParameterValueUnionTypeDef(BaseValidatorModel):
    pass


class RemediationConfigurationTypeDef(BaseValidatorModel):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str
    TargetVersion: Optional[str] = None
    Parameters: Optional[Mapping[str, RemediationParameterValueUnionTypeDef]] = None
    ResourceType: Optional[str] = None
    Automatic: Optional[bool] = None
    ExecutionControls: Optional[ExecutionControlsTypeDef] = None
    MaximumAutomaticAttempts: Optional[int] = None
    RetryAttemptSeconds: Optional[int] = None
    Arn: Optional[str] = None
    CreatedByService: Optional[str] = None


class RemediationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutRemediationConfigurationsRequestTypeDef(BaseValidatorModel):
    RemediationConfigurations: Sequence[RemediationConfigurationUnionTypeDef]


