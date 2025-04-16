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
from aws_resource_validator.pydantic_models.datazone_constants import *

class AcceptChoice(BaseValidatorModel):
    predictionTarget: str
    editedValue: Optional[str] = None
    predictionChoice: Optional[int] = None


class AcceptRule(BaseValidatorModel):
    rule: Optional[AcceptRuleBehaviorType] = None
    threshold: Optional[float] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AcceptedAssetScope(BaseValidatorModel):
    assetId: str
    filterIds: Sequence[str]


class FormOutput(BaseValidatorModel):
    formName: str
    content: Optional[str] = None
    typeName: Optional[str] = None
    typeRevision: Optional[str] = None


class AwsConsoleLinkParameters(BaseValidatorModel):
    uri: Optional[str] = None


class AddToProjectMemberPoolPolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class ColumnFilterConfigurationOutput(BaseValidatorModel):
    includedColumnNames: Optional[List[str]] = None


class ColumnFilterConfiguration(BaseValidatorModel):
    includedColumnNames: Optional[Sequence[str]] = None


class AssetInDataProductListingItem(BaseValidatorModel):
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None


class AssetListingDetails(BaseValidatorModel):
    listingId: str
    listingStatus: ListingStatusType


class DetailedGlossaryTerm(BaseValidatorModel):
    name: Optional[str] = None
    shortDescription: Optional[str] = None


class AssetScope(BaseValidatorModel):
    assetId: str
    filterIds: List[str]
    status: str
    errorMessage: Optional[str] = None


class AssetTargetNameMap(BaseValidatorModel):
    assetId: str
    targetName: str


class FormEntryOutput(BaseValidatorModel):
    typeName: str
    typeRevision: str
    required: Optional[bool] = None


class AssetTypesForRuleOutput(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificAssetTypes: Optional[List[str]] = None


class AssetTypesForRule(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificAssetTypes: Optional[Sequence[str]] = None


class AssociateEnvironmentRoleInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str


class AthenaPropertiesInput(BaseValidatorModel):
    workgroupName: Optional[str] = None


class AthenaPropertiesOutput(BaseValidatorModel):
    workgroupName: Optional[str] = None


class AthenaPropertiesPatch(BaseValidatorModel):
    workgroupName: Optional[str] = None


class BasicAuthenticationCredentials(BaseValidatorModel):
    password: Optional[str] = None
    userName: Optional[str] = None


class AuthorizationCodeProperties(BaseValidatorModel):
    authorizationCode: Optional[str] = None
    redirectUri: Optional[str] = None


class AwsAccount(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    awsAccountIdPath: Optional[str] = None


class AwsLocation(BaseValidatorModel):
    accessRole: Optional[str] = None
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    iamConnectionId: Optional[str] = None


class BusinessNameGenerationConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None


class CancelMetadataGenerationRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class CancelSubscriptionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class CloudFormationProperties(BaseValidatorModel):
    templateUrl: str


class ConfigurableActionParameter(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ConnectionCredentials(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    expiration: Optional[datetime] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None


class HyperPodPropertiesInput(BaseValidatorModel):
    clusterName: str


class IamPropertiesInput(BaseValidatorModel):
    glueLineageSyncEnabled: Optional[bool] = None


class SparkEmrPropertiesInput(BaseValidatorModel):
    computeArn: Optional[str] = None
    instanceProfileArn: Optional[str] = None
    javaVirtualEnv: Optional[str] = None
    logUri: Optional[str] = None
    pythonVirtualEnv: Optional[str] = None
    runtimeRole: Optional[str] = None
    trustedCertificatesS3Uri: Optional[str] = None


class GluePropertiesOutput(BaseValidatorModel):
    errorMessage: Optional[str] = None
    status: Optional[ConnectionStatusType] = None


class HyperPodPropertiesOutput(BaseValidatorModel):
    clusterName: str
    clusterArn: Optional[str] = None
    orchestrator: Optional[HyperPodOrchestratorType] = None


class IamPropertiesOutput(BaseValidatorModel):
    environmentId: Optional[str] = None
    glueLineageSyncEnabled: Optional[bool] = None


class IamPropertiesPatch(BaseValidatorModel):
    glueLineageSyncEnabled: Optional[bool] = None


class SparkEmrPropertiesPatch(BaseValidatorModel):
    computeArn: Optional[str] = None
    instanceProfileArn: Optional[str] = None
    javaVirtualEnv: Optional[str] = None
    logUri: Optional[str] = None
    pythonVirtualEnv: Optional[str] = None
    runtimeRole: Optional[str] = None
    trustedCertificatesS3Uri: Optional[str] = None


class FormInput(BaseValidatorModel):
    formName: str
    content: Optional[str] = None
    typeIdentifier: Optional[str] = None
    typeRevision: Optional[str] = None


class FormEntryInput(BaseValidatorModel):
    typeIdentifier: str
    typeRevision: str
    required: Optional[bool] = None


class CreateAssetTypePolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class DataProductItemOutput(BaseValidatorModel):
    identifier: str
    itemType: Literal["ASSET"]
    glossaryTerms: Optional[List[str]] = None
    revision: Optional[str] = None


class RecommendationConfiguration(BaseValidatorModel):
    enableBusinessNameGeneration: Optional[bool] = None


class ScheduleConfiguration(BaseValidatorModel):
    schedule: Optional[str] = None
    timezone: Optional[TimezoneType] = None


class DataSourceErrorMessage(BaseValidatorModel):
    errorType: DataSourceErrorTypeType
    errorDetail: Optional[str] = None


class CreateDomainUnitInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    parentDomainUnitIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class CreateDomainUnitPolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class EnvironmentParameter(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class CustomParameter(BaseValidatorModel):
    fieldType: str
    keyName: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    isEditable: Optional[bool] = None
    isOptional: Optional[bool] = None


class DeploymentProperties(BaseValidatorModel):
    endTimeoutMinutes: Optional[int] = None
    startTimeoutMinutes: Optional[int] = None


class CreateEnvironmentProfilePolicyGrantDetail(BaseValidatorModel):
    domainUnitId: Optional[str] = None


class Model(BaseValidatorModel):
    smithy: Optional[str] = None


class CreateFormTypePolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class CreateGlossaryInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    status: Optional[GlossaryStatusType] = None


class CreateGlossaryPolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class TermRelationsOutput(BaseValidatorModel):
    classifies: Optional[List[str]] = None
    isA: Optional[List[str]] = None


class CreateGroupProfileInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    clientToken: Optional[str] = None


class CreateListingChangeSetInput(BaseValidatorModel):
    action: ChangeActionType
    domainIdentifier: str
    entityIdentifier: str
    entityType: EntityTypeType
    clientToken: Optional[str] = None
    entityRevision: Optional[str] = None


class CreateProjectFromProjectProfilePolicyGrantDetailOutput(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None
    projectProfiles: Optional[List[str]] = None


class CreateProjectFromProjectProfilePolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None
    projectProfiles: Optional[Sequence[str]] = None


class Member(BaseValidatorModel):
    groupIdentifier: Optional[str] = None
    userIdentifier: Optional[str] = None


class ProjectDeletionError(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class CreateProjectPolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class SubscribedListingInput(BaseValidatorModel):
    identifier: str


class SubscriptionTargetForm(BaseValidatorModel):
    content: str
    formName: str


class CreateUserProfileInput(BaseValidatorModel):
    domainIdentifier: str
    userIdentifier: str
    clientToken: Optional[str] = None
    userType: Optional[UserTypeType] = None


class DataProductItem(BaseValidatorModel):
    identifier: str
    itemType: Literal["ASSET"]
    glossaryTerms: Optional[Sequence[str]] = None
    revision: Optional[str] = None


class DataProductListingItemAdditionalAttributes(BaseValidatorModel):
    forms: Optional[str] = None


class SageMakerRunConfigurationInput(BaseValidatorModel):
    trackingAssets: Mapping[str, Sequence[str]]


class SageMakerRunConfigurationOutput(BaseValidatorModel):
    trackingAssets: Dict[str, List[str]]
    accountId: Optional[str] = None
    region: Optional[str] = None


class LineageInfo(BaseValidatorModel):
    errorMessage: Optional[str] = None
    eventId: Optional[str] = None
    eventStatus: Optional[LineageEventProcessingStatusType] = None


class DataSourceRunLineageSummary(BaseValidatorModel):
    importStatus: Optional[LineageImportStatusType] = None


class RunStatisticsForAssets(BaseValidatorModel):
    added: Optional[int] = None
    failed: Optional[int] = None
    skipped: Optional[int] = None
    unchanged: Optional[int] = None
    updated: Optional[int] = None


class DeleteAssetFilterInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str


class DeleteAssetInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteAssetTypeInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteDataProductInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteDataSourceInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None


class DeleteDomainInput(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    skipDeletionCheck: Optional[bool] = None


class DeleteDomainUnitInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class DeleteEnvironmentBlueprintConfigurationInput(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str


class DeleteEnvironmentInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteEnvironmentProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteFormTypeInput(BaseValidatorModel):
    domainIdentifier: str
    formTypeIdentifier: str


class DeleteGlossaryInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteGlossaryTermInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteListingInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteProjectInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    skipDeletionCheck: Optional[bool] = None


class DeleteProjectProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteRuleInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteSubscriptionGrantInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteSubscriptionTargetInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class DeleteTimeSeriesDataPointsInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    clientToken: Optional[str] = None


class EnvironmentError(BaseValidatorModel):
    message: str
    code: Optional[str] = None


class DisassociateEnvironmentRoleInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str


class DomainUnitFilterForProject(BaseValidatorModel):
    domainUnit: str
    includeChildDomainUnits: Optional[bool] = None


class DomainUnitGrantFilterOutput(BaseValidatorModel):
    allDomainUnitsGrantFilter: Optional[Dict[str, Any]] = None


class DomainUnitGrantFilter(BaseValidatorModel):
    allDomainUnitsGrantFilter: Optional[Mapping[str, Any]] = None


class DomainUnitGroupProperties(BaseValidatorModel):
    groupId: Optional[str] = None


class DomainUnitUserProperties(BaseValidatorModel):
    userId: Optional[str] = None


class DomainUnitTarget(BaseValidatorModel):
    domainUnitId: str
    includeChildDomainUnits: Optional[bool] = None


class Region(BaseValidatorModel):
    regionName: Optional[str] = None
    regionNamePath: Optional[str] = None


class EnvironmentConfigurationParameter(BaseValidatorModel):
    isEditable: Optional[bool] = None
    name: Optional[str] = None
    value: Optional[str] = None


class EqualToExpression(BaseValidatorModel):
    columnName: str
    value: str


class FailureCause(BaseValidatorModel):
    message: Optional[str] = None


class Filter(BaseValidatorModel):
    attribute: str
    value: str


class Import(BaseValidatorModel):
    name: str
    revision: str


class GetAssetFilterInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str


class GetAssetInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetAssetTypeInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    withSecret: Optional[bool] = None


class GetDataProductInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetDataSourceInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetDataSourceRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetDomainInput(BaseValidatorModel):
    identifier: str


class GetDomainUnitInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class GetEnvironmentBlueprintConfigurationInput(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str


class GetEnvironmentBlueprintInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetEnvironmentCredentialsInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str


class GetEnvironmentInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetEnvironmentProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetFormTypeInput(BaseValidatorModel):
    domainIdentifier: str
    formTypeIdentifier: str
    revision: Optional[str] = None


class GetGlossaryInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetGlossaryTermInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetGroupProfileInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str


class GetIamPortalLoginUrlInput(BaseValidatorModel):
    domainIdentifier: str


class GetJobRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class JobRunError(BaseValidatorModel):
    message: str


class GetLineageEventInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetListingInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    listingRevision: Optional[str] = None


class GetMetadataGenerationRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetProjectInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetProjectProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetRuleInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetSubscriptionGrantInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetSubscriptionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetSubscriptionRequestDetailsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetSubscriptionTargetInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class GetTimeSeriesDataPointInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    identifier: str


class PhysicalConnectionRequirementsOutput(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    securityGroupIdList: Optional[List[str]] = None
    subnetId: Optional[str] = None
    subnetIdList: Optional[List[str]] = None


class GlueOAuth2Credentials(BaseValidatorModel):
    accessToken: Optional[str] = None
    jwtToken: Optional[str] = None
    refreshToken: Optional[str] = None
    userManagedClientApplicationClientSecret: Optional[str] = None


class SelfGrantStatusDetail(BaseValidatorModel):
    databaseName: str
    status: SelfGrantStatusType
    failureCause: Optional[str] = None
    schemaName: Optional[str] = None


class ListingRevisionInput(BaseValidatorModel):
    identifier: str
    revision: str


class GreaterThanExpression(BaseValidatorModel):
    columnName: str
    value: str


class GreaterThanOrEqualToExpression(BaseValidatorModel):
    columnName: str
    value: str


class GroupDetails(BaseValidatorModel):
    groupId: str


class GroupPolicyGrantPrincipal(BaseValidatorModel):
    groupIdentifier: Optional[str] = None


class IamUserProfileDetails(BaseValidatorModel):
    arn: Optional[str] = None


class InExpressionOutput(BaseValidatorModel):
    columnName: str
    values: List[str]


class InExpression(BaseValidatorModel):
    columnName: str
    values: Sequence[str]


class IsNotNullExpression(BaseValidatorModel):
    columnName: str


class IsNullExpression(BaseValidatorModel):
    columnName: str


class LakeFormationConfigurationOutput(BaseValidatorModel):
    locationRegistrationExcludeS3Locations: Optional[List[str]] = None
    locationRegistrationRole: Optional[str] = None


class LakeFormationConfiguration(BaseValidatorModel):
    locationRegistrationExcludeS3Locations: Optional[Sequence[str]] = None
    locationRegistrationRole: Optional[str] = None


class LessThanExpression(BaseValidatorModel):
    columnName: str
    value: str


class LessThanOrEqualToExpression(BaseValidatorModel):
    columnName: str
    value: str


class LikeExpression(BaseValidatorModel):
    columnName: str
    value: str


class LineageSqlQueryRunDetails(BaseValidatorModel):
    errorMessages: Optional[List[str]] = None
    numQueriesFailed: Optional[int] = None
    queryEndTime: Optional[datetime] = None
    queryStartTime: Optional[datetime] = None
    totalQueriesProcessed: Optional[int] = None


class LineageSyncSchedule(BaseValidatorModel):
    schedule: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssetFiltersInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[FilterStatusType] = None


class ListAssetRevisionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataProductRevisionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataSourceRunActivitiesInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataAssetActivityStatusType] = None


class ListDataSourceRunsInput(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceRunStatusType] = None


class ListDomainUnitsForParentInput(BaseValidatorModel):
    domainIdentifier: str
    parentDomainUnitIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDomainsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DomainStatusType] = None


class ListEntityOwnersInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentActionsInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentBlueprintConfigurationsInput(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentBlueprintsInput(BaseValidatorModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None


class ListEnvironmentProfilesInput(BaseValidatorModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    projectIdentifier: Optional[str] = None


class ListEnvironmentsInput(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    environmentProfileIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[EnvironmentStatusType] = None


class ListJobRunsInput(BaseValidatorModel):
    domainIdentifier: str
    jobIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[JobRunStatusType] = None


class ListPolicyGrantsInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListProjectMembershipsInput(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListProjectProfilesInput(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListProjectsInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    userIdentifier: Optional[str] = None


class ListRulesInput(BaseValidatorModel):
    domainIdentifier: str
    targetIdentifier: str
    targetType: Literal["DOMAIN_UNIT"]
    action: Optional[Literal["CREATE_SUBSCRIPTION_REQUEST"]] = None
    assetTypes: Optional[Sequence[str]] = None
    dataProduct: Optional[bool] = None
    includeCascaded: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    projectIds: Optional[Sequence[str]] = None
    ruleType: Optional[Literal["METADATA_FORM_ENFORCEMENT"]] = None


class ListSubscriptionGrantsInput(BaseValidatorModel):
    domainIdentifier: str
    environmentId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    subscribedListingId: Optional[str] = None
    subscriptionId: Optional[str] = None
    subscriptionTargetId: Optional[str] = None


class ListSubscriptionRequestsInput(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None


class ListSubscriptionTargetsInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None


class ListSubscriptionsInput(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionStatusType] = None
    subscribedListingId: Optional[str] = None
    subscriptionRequestIdentifier: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class UserDetails(BaseValidatorModel):
    userId: str


class MetadataFormReference(BaseValidatorModel):
    typeIdentifier: str
    typeRevision: str


class MetadataFormSummary(BaseValidatorModel):
    typeName: str
    typeRevision: str
    formName: Optional[str] = None


class NameIdentifier(BaseValidatorModel):
    name: Optional[str] = None
    namespace: Optional[str] = None


class NotEqualToExpression(BaseValidatorModel):
    columnName: str
    value: str


class NotInExpressionOutput(BaseValidatorModel):
    columnName: str
    values: List[str]


class NotInExpression(BaseValidatorModel):
    columnName: str
    values: Sequence[str]


class NotLikeExpression(BaseValidatorModel):
    columnName: str
    value: str


class OAuth2ClientApplication(BaseValidatorModel):
    aWSManagedClientApplicationReference: Optional[str] = None
    userManagedClientApplicationClientId: Optional[str] = None


class OverrideDomainUnitOwnersPolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class OverrideProjectOwnersPolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class OwnerGroupPropertiesOutput(BaseValidatorModel):
    groupId: Optional[str] = None


class OwnerGroupProperties(BaseValidatorModel):
    groupIdentifier: str


class OwnerUserPropertiesOutput(BaseValidatorModel):
    userId: Optional[str] = None


class OwnerUserProperties(BaseValidatorModel):
    userIdentifier: str


class PhysicalConnectionRequirements(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    securityGroupIdList: Optional[Sequence[str]] = None
    subnetId: Optional[str] = None
    subnetIdList: Optional[Sequence[str]] = None


class UserPolicyGrantPrincipalOutput(BaseValidatorModel):
    allUsersGrantFilter: Optional[Dict[str, Any]] = None
    userIdentifier: Optional[str] = None


class UserPolicyGrantPrincipal(BaseValidatorModel):
    allUsersGrantFilter: Optional[Mapping[str, Any]] = None
    userIdentifier: Optional[str] = None


class ProjectsForRuleOutput(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: Optional[List[str]] = None


class ProjectsForRule(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: Optional[Sequence[str]] = None


class RedshiftClusterStorage(BaseValidatorModel):
    clusterName: str


class RedshiftCredentialConfiguration(BaseValidatorModel):
    secretManagerArn: str


class UsernamePassword(BaseValidatorModel):
    password: str
    username: str


class RedshiftStorageProperties(BaseValidatorModel):
    clusterName: Optional[str] = None
    workgroupName: Optional[str] = None


class RedshiftServerlessStorage(BaseValidatorModel):
    workgroupName: str


class RejectChoice(BaseValidatorModel):
    predictionTarget: str
    predictionChoices: Optional[Sequence[int]] = None


class RejectRule(BaseValidatorModel):
    rule: Optional[RejectRuleBehaviorType] = None
    threshold: Optional[float] = None


class RejectSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    decisionComment: Optional[str] = None


class RevokeSubscriptionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    retainPermissions: Optional[bool] = None


class SearchGroupProfilesInput(BaseValidatorModel):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchText: Optional[str] = None


class SearchInItem(BaseValidatorModel):
    attribute: str


class SearchSort(BaseValidatorModel):
    attribute: str
    order: Optional[SortOrderType] = None


class SearchUserProfilesInput(BaseValidatorModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchText: Optional[str] = None


class SparkGlueArgs(BaseValidatorModel):
    connection: Optional[str] = None


class SsoUserProfileDetails(BaseValidatorModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    username: Optional[str] = None


class StartDataSourceRunInput(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    clientToken: Optional[str] = None


class SubscribedProjectInput(BaseValidatorModel):
    identifier: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TermRelations(BaseValidatorModel):
    classifies: Optional[Sequence[str]] = None
    isA: Optional[Sequence[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDomainUnitInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None


class UpdateEnvironmentInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None


class UpdateGlossaryInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[GlossaryStatusType] = None


class UpdateGroupProfileInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    status: GroupProfileStatusType


class UpdateSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    requestReason: str


class AcceptPredictionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    acceptChoices: Optional[Sequence[AcceptChoice]] = None
    acceptRule: Optional[AcceptRule] = None
    clientToken: Optional[str] = None
    revision: Optional[str] = None


class AcceptPredictionsOutput(BaseValidatorModel):
    assetId: str
    domainId: str
    revision: str
    ResponseMetadata: ResponseMetadata


class CreateFormTypeOutput(BaseValidatorModel):
    description: str
    domainId: str
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    ResponseMetadata: ResponseMetadata


class CreateListingChangeSetOutput(BaseValidatorModel):
    listingId: str
    listingRevision: str
    status: ListingStatusType
    ResponseMetadata: ResponseMetadata


class DeleteConnectionOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


class DeleteDomainOutput(BaseValidatorModel):
    status: DomainStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetEnvironmentCredentialsOutput(BaseValidatorModel):
    accessKeyId: str
    expiration: datetime
    secretAccessKey: str
    sessionToken: str
    ResponseMetadata: ResponseMetadata


class GetIamPortalLoginUrlOutput(BaseValidatorModel):
    authCodeUrl: str
    userProfileId: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RejectPredictionsOutput(BaseValidatorModel):
    assetId: str
    assetRevision: str
    domainId: str
    ResponseMetadata: ResponseMetadata


class AcceptSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    assetScopes: Optional[Sequence[AcceptedAssetScope]] = None
    decisionComment: Optional[str] = None


class ActionParameters(BaseValidatorModel):
    awsConsoleLink: Optional[AwsConsoleLinkParameters] = None


class AssetFilterSummary(BaseValidatorModel):
    pass


class ListAssetFiltersOutput(BaseValidatorModel):
    items: List[AssetFilterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TimeSeriesDataPointSummaryFormOutput(BaseValidatorModel):
    pass


class AssetItemAdditionalAttributes(BaseValidatorModel):
    formsOutput: Optional[List[FormOutput]] = None
    latestTimeSeriesDataPointFormsOutput: Optional[ List[TimeSeriesDataPointSummaryFormOutput] ] = None
    readOnlyFormsOutput: Optional[List[FormOutput]] = None


class AssetListingItemAdditionalAttributes(BaseValidatorModel):
    forms: Optional[str] = None
    latestTimeSeriesDataPointForms: Optional[List[TimeSeriesDataPointSummaryFormOutput]] = None


class ListTimeSeriesDataPointsOutput(BaseValidatorModel):
    items: List[TimeSeriesDataPointSummaryFormOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssetListing(BaseValidatorModel):
    assetId: Optional[str] = None
    assetRevision: Optional[str] = None
    assetType: Optional[str] = None
    createdAt: Optional[datetime] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None
    latestTimeSeriesDataPointForms: Optional[List[TimeSeriesDataPointSummaryFormOutput]] = None
    owningProjectId: Optional[str] = None


class ListingSummaryItem(BaseValidatorModel):
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None


class ListingSummary(BaseValidatorModel):
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None


class SubscribedProductListing(BaseValidatorModel):
    assetListings: Optional[List[AssetInDataProductListingItem]] = None
    description: Optional[str] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None
    name: Optional[str] = None


class AssetRevision(BaseValidatorModel):
    pass


class ListAssetRevisionsOutput(BaseValidatorModel):
    items: List[AssetRevision]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SubscribedAssetListing(BaseValidatorModel):
    assetScope: Optional[AssetScope] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None


class AssetTypeItem(BaseValidatorModel):
    domainId: str
    formsOutput: Dict[str, FormEntryOutput]
    name: str
    owningProjectId: str
    revision: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    originDomainId: Optional[str] = None
    originProjectId: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class CreateAssetTypeOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    formsOutput: Dict[str, FormEntryOutput]
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class GetAssetTypeOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    formsOutput: Dict[str, FormEntryOutput]
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class LineageNodeTypeItem(BaseValidatorModel):
    domainId: str
    formsOutput: Dict[str, FormEntryOutput]
    revision: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class AuthenticationConfigurationPatch(BaseValidatorModel):
    basicAuthenticationCredentials: Optional[BasicAuthenticationCredentials] = None
    secretArn: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class PostLineageEventInput(BaseValidatorModel):
    domainIdentifier: str
    event: Blob
    clientToken: Optional[str] = None


class PredictionConfiguration(BaseValidatorModel):
    businessNameGeneration: Optional[BusinessNameGenerationConfiguration] = None


class ProvisioningProperties(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationProperties] = None


class CreateAssetTypeInput(BaseValidatorModel):
    domainIdentifier: str
    formsInput: Mapping[str, FormEntryInput]
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None


class SingleSignOn(BaseValidatorModel):
    pass


class CreateDomainInput(BaseValidatorModel):
    domainExecutionRole: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainVersion: Optional[DomainVersionType] = None
    kmsKeyIdentifier: Optional[str] = None
    serviceRole: Optional[str] = None
    singleSignOn: Optional[SingleSignOn] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateDomainInput(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainExecutionRole: Optional[str] = None
    name: Optional[str] = None
    serviceRole: Optional[str] = None
    singleSignOn: Optional[SingleSignOn] = None


class CreateEnvironmentInput(BaseValidatorModel):
    domainIdentifier: str
    environmentProfileIdentifier: str
    name: str
    projectIdentifier: str
    deploymentOrder: Optional[int] = None
    description: Optional[str] = None
    environmentAccountIdentifier: Optional[str] = None
    environmentAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    environmentConfigurationId: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    userParameters: Optional[Sequence[EnvironmentParameter]] = None


class CreateEnvironmentProfileInput(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str
    name: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameter]] = None


class EnvironmentConfigurationUserParameterOutput(BaseValidatorModel):
    environmentConfigurationName: Optional[str] = None
    environmentParameters: Optional[List[EnvironmentParameter]] = None


class EnvironmentConfigurationUserParameter(BaseValidatorModel):
    environmentConfigurationName: Optional[str] = None
    environmentParameters: Optional[Sequence[EnvironmentParameter]] = None


class UpdateEnvironmentProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameter]] = None


class CreateFormTypeInput(BaseValidatorModel):
    domainIdentifier: str
    model: Model
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None
    status: Optional[FormTypeStatusType] = None


class CreateProjectMembershipInput(BaseValidatorModel):
    designation: UserDesignationType
    domainIdentifier: str
    member: Member
    projectIdentifier: str


class DeleteProjectMembershipInput(BaseValidatorModel):
    domainIdentifier: str
    member: Member
    projectIdentifier: str


class UpdateSubscriptionTargetInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    applicableAssetTypes: Optional[Sequence[str]] = None
    authorizedPrincipals: Optional[Sequence[str]] = None
    manageAccessRole: Optional[str] = None
    name: Optional[str] = None
    provider: Optional[str] = None
    subscriptionTargetConfig: Optional[Sequence[SubscriptionTargetForm]] = None


class DataProductRevision(BaseValidatorModel):
    pass


class ListDataProductRevisionsOutput(BaseValidatorModel):
    items: List[DataProductRevision]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataSourceRunActivity(BaseValidatorModel):
    createdAt: datetime
    dataAssetStatus: DataAssetActivityStatusType
    dataSourceRunId: str
    database: str
    projectId: str
    technicalName: str
    updatedAt: datetime
    dataAssetId: Optional[str] = None
    errorMessage: Optional[DataSourceErrorMessage] = None
    lineageSummary: Optional[LineageInfo] = None
    technicalDescription: Optional[str] = None


class Deployment(BaseValidatorModel):
    deploymentId: Optional[str] = None
    deploymentStatus: Optional[DeploymentStatusType] = None
    deploymentType: Optional[DeploymentTypeType] = None
    failureReason: Optional[EnvironmentError] = None
    isDeploymentComplete: Optional[bool] = None
    messages: Optional[List[str]] = None


class EnvironmentDeploymentDetailsOutput(BaseValidatorModel):
    environmentFailureReasons: Optional[Dict[str, List[EnvironmentError]]] = None
    overallDeploymentStatus: Optional[OverallDeploymentStatusType] = None


class EnvironmentDeploymentDetails(BaseValidatorModel):
    environmentFailureReasons: Optional[Mapping[str, Sequence[EnvironmentError]]] = None
    overallDeploymentStatus: Optional[OverallDeploymentStatusType] = None


class DomainSummary(BaseValidatorModel):
    pass


class ListDomainsOutput(BaseValidatorModel):
    items: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ProjectGrantFilter(BaseValidatorModel):
    domainUnitFilter: Optional[DomainUnitFilterForProject] = None


class DomainUnitPolicyGrantPrincipalOutput(BaseValidatorModel):
    domainUnitDesignation: Literal["OWNER"]
    domainUnitGrantFilter: Optional[DomainUnitGrantFilterOutput] = None
    domainUnitIdentifier: Optional[str] = None


class DomainUnitPolicyGrantPrincipal(BaseValidatorModel):
    domainUnitDesignation: Literal["OWNER"]
    domainUnitGrantFilter: Optional[DomainUnitGrantFilter] = None
    domainUnitIdentifier: Optional[str] = None


class DomainUnitOwnerProperties(BaseValidatorModel):
    group: Optional[DomainUnitGroupProperties] = None
    user: Optional[DomainUnitUserProperties] = None


class DomainUnitSummary(BaseValidatorModel):
    pass


class ListDomainUnitsForParentOutput(BaseValidatorModel):
    items: List[DomainUnitSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RuleTarget(BaseValidatorModel):
    domainUnitTarget: Optional[DomainUnitTarget] = None


class EnvironmentConfigurationParametersDetailsOutput(BaseValidatorModel):
    parameterOverrides: Optional[List[EnvironmentConfigurationParameter]] = None
    resolvedParameters: Optional[List[EnvironmentConfigurationParameter]] = None
    ssmPath: Optional[str] = None


class EnvironmentConfigurationParametersDetails(BaseValidatorModel):
    parameterOverrides: Optional[Sequence[EnvironmentConfigurationParameter]] = None
    resolvedParameters: Optional[Sequence[EnvironmentConfigurationParameter]] = None
    ssmPath: Optional[str] = None


class EnvironmentProfileSummary(BaseValidatorModel):
    pass


class ListEnvironmentProfilesOutput(BaseValidatorModel):
    items: List[EnvironmentProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EnvironmentSummary(BaseValidatorModel):
    pass


class ListEnvironmentsOutput(BaseValidatorModel):
    items: List[EnvironmentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SubscribedAsset(BaseValidatorModel):
    assetId: str
    assetRevision: str
    status: SubscriptionGrantStatusType
    assetScope: Optional[AssetScope] = None
    failureCause: Optional[FailureCause] = None
    failureTimestamp: Optional[datetime] = None
    grantedTimestamp: Optional[datetime] = None
    targetName: Optional[str] = None


class UpdateSubscriptionGrantStatusInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    status: SubscriptionGrantStatusType
    failureCause: Optional[FailureCause] = None
    targetName: Optional[str] = None


class FilterExpression(BaseValidatorModel):
    pass


class RelationalFilterConfigurationOutput(BaseValidatorModel):
    databaseName: str
    filterExpressions: Optional[List[FilterExpression]] = None
    schemaName: Optional[str] = None


class RelationalFilterConfiguration(BaseValidatorModel):
    databaseName: str
    filterExpressions: Optional[Sequence[FilterExpression]] = None
    schemaName: Optional[str] = None


class FormTypeData(BaseValidatorModel):
    domainId: str
    name: str
    revision: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    imports: Optional[List[Import]] = None
    model: Optional[Model] = None
    originDomainId: Optional[str] = None
    originProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    status: Optional[FormTypeStatusType] = None


class GetFormTypeOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    imports: List[Import]
    model: Model
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    status: FormTypeStatusType
    ResponseMetadata: ResponseMetadata


class JobRunSummary(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    domainId: Optional[str] = None
    endTime: Optional[datetime] = None
    error: Optional[JobRunError] = None
    jobId: Optional[str] = None
    jobType: Optional[Literal["LINEAGE"]] = None
    runId: Optional[str] = None
    runMode: Optional[JobRunModeType] = None
    startTime: Optional[datetime] = None
    status: Optional[JobRunStatusType] = None


class Timestamp(BaseValidatorModel):
    pass


class GetLineageNodeInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    eventTimestamp: Optional[Timestamp] = None


class ListLineageEventsInput(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    processingStatus: Optional[LineageEventProcessingStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    timestampAfter: Optional[Timestamp] = None
    timestampBefore: Optional[Timestamp] = None


class ListLineageNodeHistoryInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[Timestamp] = None
    eventTimestampLTE: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None


class ListTimeSeriesDataPointsInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startedAt: Optional[Timestamp] = None


class TimeSeriesDataPointFormInput(BaseValidatorModel):
    formName: str
    timestamp: Timestamp
    typeIdentifier: str
    content: Optional[str] = None
    typeRevision: Optional[str] = None


class TimeSeriesDataPointFormOutput(BaseValidatorModel):
    pass


class GetTimeSeriesDataPointOutput(BaseValidatorModel):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    form: TimeSeriesDataPointFormOutput
    formName: str
    ResponseMetadata: ResponseMetadata


class PostTimeSeriesDataPointsOutput(BaseValidatorModel):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    forms: List[TimeSeriesDataPointFormOutput]
    ResponseMetadata: ResponseMetadata


class GlueSelfGrantStatusOutput(BaseValidatorModel):
    selfGrantStatusDetails: List[SelfGrantStatusDetail]


class RedshiftSelfGrantStatusOutput(BaseValidatorModel):
    selfGrantStatusDetails: List[SelfGrantStatusDetail]


class GrantedEntityInput(BaseValidatorModel):
    listing: Optional[ListingRevisionInput] = None


class ListingRevision(BaseValidatorModel):
    pass


class GrantedEntity(BaseValidatorModel):
    listing: Optional[ListingRevision] = None


class GroupProfileSummary(BaseValidatorModel):
    pass


class SearchGroupProfilesOutput(BaseValidatorModel):
    items: List[GroupProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ProvisioningConfigurationOutput(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationOutput] = None


class LineageNodeSummary(BaseValidatorModel):
    pass


class ListLineageNodeHistoryOutput(BaseValidatorModel):
    nodes: List[LineageNodeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LineageRunDetails(BaseValidatorModel):
    sqlQueryRunDetails: Optional[LineageSqlQueryRunDetails] = None


class RedshiftLineageSyncConfigurationInput(BaseValidatorModel):
    enabled: Optional[bool] = None
    schedule: Optional[LineageSyncSchedule] = None


class RedshiftLineageSyncConfigurationOutput(BaseValidatorModel):
    enabled: Optional[bool] = None
    lineageJobId: Optional[str] = None
    schedule: Optional[LineageSyncSchedule] = None


class ListAssetFiltersInputPaginate(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    status: Optional[FilterStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssetRevisionsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataProductRevisionsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSourceRunActivitiesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    status: Optional[DataAssetActivityStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSourceRunsInputPaginate(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    status: Optional[DataSourceRunStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainUnitsForParentInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    parentDomainUnitIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainsInputPaginate(BaseValidatorModel):
    status: Optional[DomainStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEntityOwnersInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentActionsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentBlueprintConfigurationsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentBlueprintsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentProfilesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    name: Optional[str] = None
    projectIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnvironmentsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    environmentProfileIdentifier: Optional[str] = None
    name: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[EnvironmentStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobRunsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    jobIdentifier: str
    sortOrder: Optional[SortOrderType] = None
    status: Optional[JobRunStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLineageEventsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    processingStatus: Optional[LineageEventProcessingStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    timestampAfter: Optional[Timestamp] = None
    timestampBefore: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLineageNodeHistoryInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[Timestamp] = None
    eventTimestampLTE: Optional[Timestamp] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyGrantsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectMembershipsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectProfilesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    name: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    name: Optional[str] = None
    userIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    targetIdentifier: str
    targetType: Literal["DOMAIN_UNIT"]
    action: Optional[Literal["CREATE_SUBSCRIPTION_REQUEST"]] = None
    assetTypes: Optional[Sequence[str]] = None
    dataProduct: Optional[bool] = None
    includeCascaded: Optional[bool] = None
    projectIds: Optional[Sequence[str]] = None
    ruleType: Optional[Literal["METADATA_FORM_ENFORCEMENT"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionGrantsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    environmentId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    subscribedListingId: Optional[str] = None
    subscriptionId: Optional[str] = None
    subscriptionTargetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionRequestsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionTargetsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionStatusType] = None
    subscribedListingId: Optional[str] = None
    subscriptionRequestIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTimeSeriesDataPointsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: Optional[Timestamp] = None
    startedAt: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchGroupProfilesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchUserProfilesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ProjectProfileSummary(BaseValidatorModel):
    pass


class ListProjectProfilesOutput(BaseValidatorModel):
    items: List[ProjectProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MemberDetails(BaseValidatorModel):
    group: Optional[GroupDetails] = None
    user: Optional[UserDetails] = None


class MetadataFormEnforcementDetailOutput(BaseValidatorModel):
    requiredMetadataForms: Optional[List[MetadataFormReference]] = None


class MetadataFormEnforcementDetail(BaseValidatorModel):
    requiredMetadataForms: Optional[Sequence[MetadataFormReference]] = None


class OpenLineageRunEventSummary(BaseValidatorModel):
    eventType: Optional[OpenLineageRunStateType] = None
    inputs: Optional[List[NameIdentifier]] = None
    job: Optional[NameIdentifier] = None
    outputs: Optional[List[NameIdentifier]] = None
    runId: Optional[str] = None


class NotificationResource(BaseValidatorModel):
    pass


class Topic(BaseValidatorModel):
    resource: NotificationResource
    role: NotificationRoleType
    subject: str


class OAuth2PropertiesOutput(BaseValidatorModel):
    authorizationCodeProperties: Optional[AuthorizationCodeProperties] = None
    oAuth2ClientApplication: Optional[OAuth2ClientApplication] = None
    oAuth2Credentials: Optional[GlueOAuth2Credentials] = None
    oAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    tokenUrl: Optional[str] = None
    tokenUrlParametersMap: Optional[Dict[str, str]] = None


class OAuth2Properties(BaseValidatorModel):
    authorizationCodeProperties: Optional[AuthorizationCodeProperties] = None
    oAuth2ClientApplication: Optional[OAuth2ClientApplication] = None
    oAuth2Credentials: Optional[GlueOAuth2Credentials] = None
    oAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    tokenUrl: Optional[str] = None
    tokenUrlParametersMap: Optional[Mapping[str, str]] = None


class PolicyGrantDetailOutput(BaseValidatorModel):
    addToProjectMemberPool: Optional[AddToProjectMemberPoolPolicyGrantDetail] = None
    createAssetType: Optional[CreateAssetTypePolicyGrantDetail] = None
    createDomainUnit: Optional[CreateDomainUnitPolicyGrantDetail] = None
    createEnvironment: Optional[Dict[str, Any]] = None
    createEnvironmentFromBlueprint: Optional[Dict[str, Any]] = None
    createEnvironmentProfile: Optional[CreateEnvironmentProfilePolicyGrantDetail] = None
    createFormType: Optional[CreateFormTypePolicyGrantDetail] = None
    createGlossary: Optional[CreateGlossaryPolicyGrantDetail] = None
    createProject: Optional[CreateProjectPolicyGrantDetail] = None
    createProjectFromProjectProfile: Optional[ CreateProjectFromProjectProfilePolicyGrantDetailOutput ] = None
    delegateCreateEnvironmentProfile: Optional[Dict[str, Any]] = None
    overrideDomainUnitOwners: Optional[OverrideDomainUnitOwnersPolicyGrantDetail] = None
    overrideProjectOwners: Optional[OverrideProjectOwnersPolicyGrantDetail] = None


class PolicyGrantDetail(BaseValidatorModel):
    addToProjectMemberPool: Optional[AddToProjectMemberPoolPolicyGrantDetail] = None
    createAssetType: Optional[CreateAssetTypePolicyGrantDetail] = None
    createDomainUnit: Optional[CreateDomainUnitPolicyGrantDetail] = None
    createEnvironment: Optional[Mapping[str, Any]] = None
    createEnvironmentFromBlueprint: Optional[Mapping[str, Any]] = None
    createEnvironmentProfile: Optional[CreateEnvironmentProfilePolicyGrantDetail] = None
    createFormType: Optional[CreateFormTypePolicyGrantDetail] = None
    createGlossary: Optional[CreateGlossaryPolicyGrantDetail] = None
    createProject: Optional[CreateProjectPolicyGrantDetail] = None
    createProjectFromProjectProfile: Optional[ CreateProjectFromProjectProfilePolicyGrantDetail ] = None
    delegateCreateEnvironmentProfile: Optional[Mapping[str, Any]] = None
    overrideDomainUnitOwners: Optional[OverrideDomainUnitOwnersPolicyGrantDetail] = None
    overrideProjectOwners: Optional[OverrideProjectOwnersPolicyGrantDetail] = None


class OwnerPropertiesOutput(BaseValidatorModel):
    group: Optional[OwnerGroupPropertiesOutput] = None
    user: Optional[OwnerUserPropertiesOutput] = None


class OwnerProperties(BaseValidatorModel):
    group: Optional[OwnerGroupProperties] = None
    user: Optional[OwnerUserProperties] = None


class RuleScopeOutput(BaseValidatorModel):
    assetType: Optional[AssetTypesForRuleOutput] = None
    dataProduct: Optional[bool] = None
    project: Optional[ProjectsForRuleOutput] = None


class RuleScope(BaseValidatorModel):
    assetType: Optional[AssetTypesForRule] = None
    dataProduct: Optional[bool] = None
    project: Optional[ProjectsForRule] = None


class RedshiftCredentials(BaseValidatorModel):
    secretArn: Optional[str] = None
    usernamePassword: Optional[UsernamePassword] = None


class SparkEmrPropertiesOutput(BaseValidatorModel):
    computeArn: Optional[str] = None
    credentials: Optional[UsernamePassword] = None
    credentialsExpiration: Optional[datetime] = None
    governanceType: Optional[GovernanceTypeType] = None
    instanceProfileArn: Optional[str] = None
    javaVirtualEnv: Optional[str] = None
    livyEndpoint: Optional[str] = None
    logUri: Optional[str] = None
    pythonVirtualEnv: Optional[str] = None
    runtimeRole: Optional[str] = None
    trustedCertificatesS3Uri: Optional[str] = None


class RedshiftStorage(BaseValidatorModel):
    redshiftClusterSource: Optional[RedshiftClusterStorage] = None
    redshiftServerlessSource: Optional[RedshiftServerlessStorage] = None


class RejectPredictionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    rejectChoices: Optional[Sequence[RejectChoice]] = None
    rejectRule: Optional[RejectRule] = None
    revision: Optional[str] = None


class SparkGluePropertiesInput(BaseValidatorModel):
    additionalArgs: Optional[SparkGlueArgs] = None
    glueConnectionName: Optional[str] = None
    glueVersion: Optional[str] = None
    idleTimeout: Optional[int] = None
    javaVirtualEnv: Optional[str] = None
    numberOfWorkers: Optional[int] = None
    pythonVirtualEnv: Optional[str] = None
    workerType: Optional[str] = None


class SparkGluePropertiesOutput(BaseValidatorModel):
    additionalArgs: Optional[SparkGlueArgs] = None
    glueConnectionName: Optional[str] = None
    glueVersion: Optional[str] = None
    idleTimeout: Optional[int] = None
    javaVirtualEnv: Optional[str] = None
    numberOfWorkers: Optional[int] = None
    pythonVirtualEnv: Optional[str] = None
    workerType: Optional[str] = None


class UserProfileDetails(BaseValidatorModel):
    iam: Optional[IamUserProfileDetails] = None
    sso: Optional[SsoUserProfileDetails] = None


class SubscribedPrincipalInput(BaseValidatorModel):
    project: Optional[SubscribedProjectInput] = None


class SubscribedProject(BaseValidatorModel):
    pass


class SubscribedPrincipal(BaseValidatorModel):
    project: Optional[SubscribedProject] = None


class CreateEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    parameters: ActionParameters
    description: Optional[str] = None


class UpdateEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[ActionParameters] = None


class AssetItem(BaseValidatorModel):
    domainId: str
    identifier: str
    name: str
    owningProjectId: str
    typeIdentifier: str
    typeRevision: str
    additionalAttributes: Optional[AssetItemAdditionalAttributes] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    externalIdentifier: Optional[str] = None
    firstRevisionCreatedAt: Optional[datetime] = None
    firstRevisionCreatedBy: Optional[str] = None
    glossaryTerms: Optional[List[str]] = None


class AssetListingItem(BaseValidatorModel):
    additionalAttributes: Optional[AssetListingItemAdditionalAttributes] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None
    listingCreatedBy: Optional[str] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None
    listingUpdatedBy: Optional[str] = None
    name: Optional[str] = None
    owningProjectId: Optional[str] = None


class DataProductListingItem(BaseValidatorModel):
    additionalAttributes: Optional[DataProductListingItemAdditionalAttributes] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None
    items: Optional[List[ListingSummaryItem]] = None
    listingCreatedBy: Optional[str] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None
    listingUpdatedBy: Optional[str] = None
    name: Optional[str] = None
    owningProjectId: Optional[str] = None


class DataProductListing(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    dataProductId: Optional[str] = None
    dataProductRevision: Optional[str] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTerm]] = None
    items: Optional[List[ListingSummary]] = None
    owningProjectId: Optional[str] = None


class SubscribedListingItem(BaseValidatorModel):
    assetListing: Optional[SubscribedAssetListing] = None
    productListing: Optional[SubscribedProductListing] = None


class GlueConnectionPatch(BaseValidatorModel):
    authenticationConfiguration: Optional[AuthenticationConfigurationPatch] = None
    connectionProperties: Optional[Mapping[str, str]] = None
    description: Optional[str] = None


class CreateAssetInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    typeIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    externalIdentifier: Optional[str] = None
    formsInput: Optional[Sequence[FormInput]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    predictionConfiguration: Optional[PredictionConfiguration] = None
    typeRevision: Optional[str] = None


class CreateAssetRevisionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInput]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    predictionConfiguration: Optional[PredictionConfiguration] = None
    typeRevision: Optional[str] = None


class DataSourceSummary(BaseValidatorModel):
    pass


class ListDataSourcesOutput(BaseValidatorModel):
    items: List[DataSourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ProjectSummary(BaseValidatorModel):
    pass


class ListProjectsOutput(BaseValidatorModel):
    items: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SubscriptionTargetSummary(BaseValidatorModel):
    pass


class ListSubscriptionTargetsOutput(BaseValidatorModel):
    items: List[SubscriptionTargetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataProductItemUnion(BaseValidatorModel):
    pass


class CreateDataProductInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInput]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    items: Optional[Sequence[DataProductItemUnion]] = None


class CreateDataProductRevisionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInput]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    items: Optional[Sequence[DataProductItemUnion]] = None


class ListDataSourceRunActivitiesOutput(BaseValidatorModel):
    items: List[DataSourceRunActivity]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataSourceRunSummary(BaseValidatorModel):
    pass


class ListDataSourceRunsOutput(BaseValidatorModel):
    items: List[DataSourceRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ProjectPolicyGrantPrincipal(BaseValidatorModel):
    projectDesignation: ProjectDesignationType
    projectGrantFilter: Optional[ProjectGrantFilter] = None
    projectIdentifier: Optional[str] = None


class FilterClausePaginator(BaseValidatorModel):
    pass


class SearchInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClausePaginator] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchListingsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClausePaginator] = None
    searchIn: Optional[Sequence[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchTypesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClausePaginator] = None
    searchIn: Optional[Sequence[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class FilterClause(BaseValidatorModel):
    pass


class SearchInput(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClause] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None


class SearchListingsInput(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClause] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None


class SearchTypesInput(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClause] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None


class GlueRunConfigurationOutput(BaseValidatorModel):
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutput]
    accountId: Optional[str] = None
    autoImportDataQualityResult: Optional[bool] = None
    catalogName: Optional[str] = None
    dataAccessRole: Optional[str] = None
    region: Optional[str] = None


class SearchTypesResultItem(BaseValidatorModel):
    assetTypeItem: Optional[AssetTypeItem] = None
    formTypeItem: Optional[FormTypeData] = None
    lineageNodeTypeItem: Optional[LineageNodeTypeItem] = None


class ListJobRunsOutput(BaseValidatorModel):
    items: List[JobRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PostTimeSeriesDataPointsInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    forms: Sequence[TimeSeriesDataPointFormInput]
    clientToken: Optional[str] = None


class MetadataGenerationRunItem(BaseValidatorModel):
    pass


class ListMetadataGenerationRunsOutput(BaseValidatorModel):
    items: List[MetadataGenerationRunItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SelfGrantStatusOutput(BaseValidatorModel):
    glueSelfGrantStatus: Optional[GlueSelfGrantStatusOutput] = None
    redshiftSelfGrantStatus: Optional[RedshiftSelfGrantStatusOutput] = None


class CreateSubscriptionGrantInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    grantedEntity: GrantedEntityInput
    assetTargetNames: Optional[Sequence[AssetTargetNameMap]] = None
    clientToken: Optional[str] = None
    subscriptionTargetIdentifier: Optional[str] = None


class EnvironmentBlueprintConfigurationItem(BaseValidatorModel):
    domainId: str
    environmentBlueprintId: str
    createdAt: Optional[datetime] = None
    enabledRegions: Optional[List[str]] = None
    environmentRolePermissionBoundary: Optional[str] = None
    manageAccessRoleArn: Optional[str] = None
    provisioningConfigurations: Optional[List[ProvisioningConfigurationOutput]] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Dict[str, Dict[str, str]]] = None
    updatedAt: Optional[datetime] = None


class GetEnvironmentBlueprintConfigurationOutput(BaseValidatorModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    environmentRolePermissionBoundary: str
    manageAccessRoleArn: str
    provisioningConfigurations: List[ProvisioningConfigurationOutput]
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class PutEnvironmentBlueprintConfigurationOutput(BaseValidatorModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    environmentRolePermissionBoundary: str
    manageAccessRoleArn: str
    provisioningConfigurations: List[ProvisioningConfigurationOutput]
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class LakeFormationConfigurationUnion(BaseValidatorModel):
    pass


class ProvisioningConfiguration(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationUnion] = None


class JobRunDetails(BaseValidatorModel):
    lineageRunDetails: Optional[LineageRunDetails] = None


class ProjectMember(BaseValidatorModel):
    designation: UserDesignationType
    memberDetails: MemberDetails


class RuleDetailOutput(BaseValidatorModel):
    metadataFormEnforcementDetail: Optional[MetadataFormEnforcementDetailOutput] = None


class RuleDetail(BaseValidatorModel):
    metadataFormEnforcementDetail: Optional[MetadataFormEnforcementDetail] = None


class EventSummary(BaseValidatorModel):
    openLineageRunEventSummary: Optional[OpenLineageRunEventSummary] = None


class AuthenticationConfiguration(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    oAuth2Properties: Optional[OAuth2PropertiesOutput] = None
    secretArn: Optional[str] = None


class ListEntityOwnersOutput(BaseValidatorModel):
    owners: List[OwnerPropertiesOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AddEntityOwnerInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    owner: OwnerProperties
    clientToken: Optional[str] = None


class RemoveEntityOwnerInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    owner: OwnerProperties
    clientToken: Optional[str] = None


class RuleSummary(BaseValidatorModel):
    action: Optional[Literal["CREATE_SUBSCRIPTION_REQUEST"]] = None
    identifier: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    name: Optional[str] = None
    revision: Optional[str] = None
    ruleType: Optional[Literal["METADATA_FORM_ENFORCEMENT"]] = None
    scope: Optional[RuleScopeOutput] = None
    target: Optional[RuleTarget] = None
    targetType: Optional[Literal["DOMAIN_UNIT"]] = None
    updatedAt: Optional[datetime] = None


class RedshiftPropertiesInput(BaseValidatorModel):
    credentials: Optional[RedshiftCredentials] = None
    databaseName: Optional[str] = None
    host: Optional[str] = None
    lineageSync: Optional[RedshiftLineageSyncConfigurationInput] = None
    port: Optional[int] = None
    storage: Optional[RedshiftStorageProperties] = None


class RedshiftPropertiesOutput(BaseValidatorModel):
    credentials: Optional[RedshiftCredentials] = None
    databaseName: Optional[str] = None
    isProvisionedSecret: Optional[bool] = None
    jdbcIamUrl: Optional[str] = None
    jdbcUrl: Optional[str] = None
    lineageSync: Optional[RedshiftLineageSyncConfigurationOutput] = None
    redshiftTempDir: Optional[str] = None
    status: Optional[ConnectionStatusType] = None
    storage: Optional[RedshiftStorageProperties] = None


class RedshiftPropertiesPatch(BaseValidatorModel):
    credentials: Optional[RedshiftCredentials] = None
    databaseName: Optional[str] = None
    host: Optional[str] = None
    lineageSync: Optional[RedshiftLineageSyncConfigurationInput] = None
    port: Optional[int] = None
    storage: Optional[RedshiftStorageProperties] = None


class RedshiftRunConfigurationOutput(BaseValidatorModel):
    redshiftStorage: RedshiftStorage
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutput]
    accountId: Optional[str] = None
    dataAccessRole: Optional[str] = None
    redshiftCredentialConfiguration: Optional[RedshiftCredentialConfiguration] = None
    region: Optional[str] = None


class CreateSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    requestReason: str
    subscribedListings: Sequence[SubscribedListingInput]
    subscribedPrincipals: Sequence[SubscribedPrincipalInput]
    clientToken: Optional[str] = None
    metadataForms: Optional[Sequence[FormInput]] = None


class TermRelationsUnion(BaseValidatorModel):
    pass


class CreateGlossaryTermInput(BaseValidatorModel):
    domainIdentifier: str
    glossaryIdentifier: str
    name: str
    clientToken: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsUnion] = None


class UpdateGlossaryTermInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    glossaryIdentifier: Optional[str] = None
    longDescription: Optional[str] = None
    name: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsUnion] = None


class EnvironmentActionSummary(BaseValidatorModel):
    pass


class ListEnvironmentActionsOutput(BaseValidatorModel):
    items: List[EnvironmentActionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataProductResultItem(BaseValidatorModel):
    pass


class GlossaryItem(BaseValidatorModel):
    pass


class GlossaryTermItem(BaseValidatorModel):
    pass


class SearchInventoryResultItem(BaseValidatorModel):
    assetItem: Optional[AssetItem] = None
    dataProductItem: Optional[DataProductResultItem] = None
    glossaryItem: Optional[GlossaryItem] = None
    glossaryTermItem: Optional[GlossaryTermItem] = None


class SearchResultItem(BaseValidatorModel):
    assetListing: Optional[AssetListingItem] = None
    dataProductListing: Optional[DataProductListingItem] = None


class ListingItem(BaseValidatorModel):
    assetListing: Optional[AssetListing] = None
    dataProductListing: Optional[DataProductListing] = None


class GluePropertiesPatch(BaseValidatorModel):
    glueConnectionInput: Optional[GlueConnectionPatch] = None


class EnvironmentBlueprintSummary(BaseValidatorModel):
    pass


class ListEnvironmentBlueprintsOutput(BaseValidatorModel):
    items: List[EnvironmentBlueprintSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EnvironmentConfigurationUserParameterUnion(BaseValidatorModel):
    pass


class CreateProjectInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    domainUnitId: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    projectProfileId: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentConfigurationUserParameterUnion]] = None


class EnvironmentDeploymentDetailsUnion(BaseValidatorModel):
    pass


class UpdateProjectInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    environmentDeploymentDetails: Optional[EnvironmentDeploymentDetailsUnion] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None


class PolicyGrantPrincipalOutput(BaseValidatorModel):
    domainUnit: Optional[DomainUnitPolicyGrantPrincipalOutput] = None
    group: Optional[GroupPolicyGrantPrincipal] = None
    project: Optional[ProjectPolicyGrantPrincipal] = None
    user: Optional[UserPolicyGrantPrincipalOutput] = None


class PolicyGrantPrincipal(BaseValidatorModel):
    domainUnit: Optional[DomainUnitPolicyGrantPrincipal] = None
    group: Optional[GroupPolicyGrantPrincipal] = None
    project: Optional[ProjectPolicyGrantPrincipal] = None
    user: Optional[UserPolicyGrantPrincipal] = None


class RelationalFilterConfigurationUnion(BaseValidatorModel):
    pass


class GlueRunConfigurationInput(BaseValidatorModel):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationUnion]
    autoImportDataQualityResult: Optional[bool] = None
    catalogName: Optional[str] = None
    dataAccessRole: Optional[str] = None


class RedshiftRunConfigurationInput(BaseValidatorModel):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationUnion]
    dataAccessRole: Optional[str] = None
    redshiftCredentialConfiguration: Optional[RedshiftCredentialConfiguration] = None
    redshiftStorage: Optional[RedshiftStorage] = None


class SearchTypesOutput(BaseValidatorModel):
    items: List[SearchTypesResultItem]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SubscriptionGrantSummary(BaseValidatorModel):
    pass


class ListSubscriptionGrantsOutput(BaseValidatorModel):
    items: List[SubscriptionGrantSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListEnvironmentBlueprintConfigurationsOutput(BaseValidatorModel):
    items: List[EnvironmentBlueprintConfigurationItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListProjectMembershipsOutput(BaseValidatorModel):
    members: List[ProjectMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateRuleOutput(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutput
    identifier: str
    name: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutput
    target: RuleTarget
    targetType: Literal["DOMAIN_UNIT"]
    ResponseMetadata: ResponseMetadata


class GetRuleOutput(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutput
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutput
    target: RuleTarget
    targetType: Literal["DOMAIN_UNIT"]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateRuleOutput(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutput
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutput
    target: RuleTarget
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class RowFilterOutput(BaseValidatorModel):
    pass


class RowFilterConfigurationOutput(BaseValidatorModel):
    rowFilter: RowFilterOutput
    sensitive: Optional[bool] = None


class RowFilter(BaseValidatorModel):
    pass


class RowFilterConfiguration(BaseValidatorModel):
    rowFilter: RowFilter
    sensitive: Optional[bool] = None


class NotificationOutput(BaseValidatorModel):
    pass


class ListNotificationsOutput(BaseValidatorModel):
    notifications: List[NotificationOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GlueConnection(BaseValidatorModel):
    athenaProperties: Optional[Dict[str, str]] = None
    authenticationConfiguration: Optional[AuthenticationConfiguration] = None
    compatibleComputeEnvironments: Optional[List[ComputeEnvironmentsType]] = None
    connectionProperties: Optional[Dict[str, str]] = None
    connectionSchemaVersion: Optional[int] = None
    connectionType: Optional[ConnectionTypeType] = None
    creationTime: Optional[datetime] = None
    description: Optional[str] = None
    lastConnectionValidationTime: Optional[datetime] = None
    lastUpdatedBy: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    matchCriteria: Optional[List[str]] = None
    name: Optional[str] = None
    physicalConnectionRequirements: Optional[PhysicalConnectionRequirementsOutput] = None
    pythonProperties: Optional[Dict[str, str]] = None
    sparkProperties: Optional[Dict[str, str]] = None
    status: Optional[ConnectionStatusType] = None
    statusReason: Optional[str] = None


class OAuth2PropertiesUnion(BaseValidatorModel):
    pass


class AuthenticationConfigurationInput(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    basicAuthenticationCredentials: Optional[BasicAuthenticationCredentials] = None
    customAuthenticationCredentials: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None
    oAuth2Properties: Optional[OAuth2PropertiesUnion] = None
    secretArn: Optional[str] = None


class ListRulesOutput(BaseValidatorModel):
    items: List[RuleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectionPropertiesOutput(BaseValidatorModel):
    athenaProperties: Optional[AthenaPropertiesOutput] = None
    glueProperties: Optional[GluePropertiesOutput] = None
    hyperPodProperties: Optional[HyperPodPropertiesOutput] = None
    iamProperties: Optional[IamPropertiesOutput] = None
    redshiftProperties: Optional[RedshiftPropertiesOutput] = None
    sparkEmrProperties: Optional[SparkEmrPropertiesOutput] = None
    sparkGlueProperties: Optional[SparkGluePropertiesOutput] = None


class DataSourceConfigurationOutput(BaseValidatorModel):
    glueRunConfiguration: Optional[GlueRunConfigurationOutput] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationOutput] = None
    sageMakerRunConfiguration: Optional[SageMakerRunConfigurationOutput] = None


class UserProfileSummary(BaseValidatorModel):
    pass


class SearchUserProfilesOutput(BaseValidatorModel):
    items: List[UserProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchOutput(BaseValidatorModel):
    items: List[SearchInventoryResultItem]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchListingsOutput(BaseValidatorModel):
    items: List[SearchResultItem]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectionPropertiesPatch(BaseValidatorModel):
    athenaProperties: Optional[AthenaPropertiesPatch] = None
    glueProperties: Optional[GluePropertiesPatch] = None
    iamProperties: Optional[IamPropertiesPatch] = None
    redshiftProperties: Optional[RedshiftPropertiesPatch] = None
    sparkEmrProperties: Optional[SparkEmrPropertiesPatch] = None


class PolicyGrantMember(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    detail: Optional[PolicyGrantDetailOutput] = None
    principal: Optional[PolicyGrantPrincipalOutput] = None


class DataSourceConfigurationInput(BaseValidatorModel):
    glueRunConfiguration: Optional[GlueRunConfigurationInput] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationInput] = None
    sageMakerRunConfiguration: Optional[SageMakerRunConfigurationInput] = None


class ProvisioningConfigurationUnion(BaseValidatorModel):
    pass


class PutEnvironmentBlueprintConfigurationInput(BaseValidatorModel):
    domainIdentifier: str
    enabledRegions: Sequence[str]
    environmentBlueprintIdentifier: str
    environmentRolePermissionBoundary: Optional[str] = None
    manageAccessRoleArn: Optional[str] = None
    provisioningConfigurations: Optional[Sequence[ProvisioningConfigurationUnion]] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Mapping[str, Mapping[str, str]]] = None


class RuleScopeUnion(BaseValidatorModel):
    pass


class RuleDetailUnion(BaseValidatorModel):
    pass


class CreateRuleInput(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    detail: RuleDetailUnion
    domainIdentifier: str
    name: str
    scope: RuleScopeUnion
    target: RuleTarget
    clientToken: Optional[str] = None
    description: Optional[str] = None


class UpdateRuleInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    detail: Optional[RuleDetailUnion] = None
    includeChildDomainUnits: Optional[bool] = None
    name: Optional[str] = None
    scope: Optional[RuleScopeUnion] = None


class LineageEventSummary(BaseValidatorModel):
    pass


class ListLineageEventsOutput(BaseValidatorModel):
    items: List[LineageEventSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssetFilterConfigurationOutput(BaseValidatorModel):
    columnConfiguration: Optional[ColumnFilterConfigurationOutput] = None
    rowConfiguration: Optional[RowFilterConfigurationOutput] = None


class AssetFilterConfiguration(BaseValidatorModel):
    columnConfiguration: Optional[ColumnFilterConfiguration] = None
    rowConfiguration: Optional[RowFilterConfiguration] = None


class PhysicalEndpoint(BaseValidatorModel):
    awsLocation: Optional[AwsLocation] = None
    glueConnection: Optional[GlueConnection] = None
    glueConnectionName: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[ProtocolType] = None
    stage: Optional[str] = None


class PhysicalConnectionRequirementsUnion(BaseValidatorModel):
    pass


class GlueConnectionInput(BaseValidatorModel):
    athenaProperties: Optional[Mapping[str, str]] = None
    authenticationConfiguration: Optional[AuthenticationConfigurationInput] = None
    connectionProperties: Optional[Mapping[str, str]] = None
    connectionType: Optional[GlueConnectionTypeType] = None
    description: Optional[str] = None
    matchCriteria: Optional[str] = None
    name: Optional[str] = None
    physicalConnectionRequirements: Optional[PhysicalConnectionRequirementsUnion] = None
    pythonProperties: Optional[Mapping[str, str]] = None
    sparkProperties: Optional[Mapping[str, str]] = None
    validateCredentials: Optional[bool] = None
    validateForComputeEnvironments: Optional[Sequence[ComputeEnvironmentsType]] = None


class SubscriptionRequestSummary(BaseValidatorModel):
    pass


class ListSubscriptionRequestsOutput(BaseValidatorModel):
    items: List[SubscriptionRequestSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SubscriptionSummary(BaseValidatorModel):
    pass


class ListSubscriptionsOutput(BaseValidatorModel):
    items: List[SubscriptionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    awsLocation: Optional[AwsLocation] = None
    description: Optional[str] = None
    props: Optional[ConnectionPropertiesPatch] = None


class ListPolicyGrantsOutput(BaseValidatorModel):
    grantList: List[PolicyGrantMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PolicyGrantDetailUnion(BaseValidatorModel):
    pass


class PolicyGrantPrincipalUnion(BaseValidatorModel):
    pass


class AddPolicyGrantInput(BaseValidatorModel):
    detail: PolicyGrantDetailUnion
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    principal: PolicyGrantPrincipalUnion
    clientToken: Optional[str] = None


class RemovePolicyGrantInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    principal: PolicyGrantPrincipalUnion
    clientToken: Optional[str] = None


class EnvironmentConfigurationUnion(BaseValidatorModel):
    pass


class CreateProjectProfileInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    domainUnitIdentifier: Optional[str] = None
    environmentConfigurations: Optional[Sequence[EnvironmentConfigurationUnion]] = None
    status: Optional[StatusType] = None


class UpdateProjectProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    domainUnitIdentifier: Optional[str] = None
    environmentConfigurations: Optional[Sequence[EnvironmentConfigurationUnion]] = None
    name: Optional[str] = None
    status: Optional[StatusType] = None


class UpdateDataSourceInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    assetFormsInput: Optional[Sequence[FormInput]] = None
    configuration: Optional[DataSourceConfigurationInput] = None
    description: Optional[str] = None
    enableSetting: Optional[EnableSettingType] = None
    name: Optional[str] = None
    publishOnImport: Optional[bool] = None
    recommendation: Optional[RecommendationConfiguration] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None
    schedule: Optional[ScheduleConfiguration] = None


class GluePropertiesInput(BaseValidatorModel):
    glueConnectionInput: Optional[GlueConnectionInput] = None


class AssetFilterConfigurationUnion(BaseValidatorModel):
    pass


class CreateAssetFilterInput(BaseValidatorModel):
    assetIdentifier: str
    configuration: AssetFilterConfigurationUnion
    domainIdentifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class UpdateAssetFilterInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    configuration: Optional[AssetFilterConfigurationUnion] = None
    description: Optional[str] = None
    name: Optional[str] = None


class ConnectionSummary(BaseValidatorModel):
    pass


class ListConnectionsOutput(BaseValidatorModel):
    items: List[ConnectionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectionPropertiesInput(BaseValidatorModel):
    athenaProperties: Optional[AthenaPropertiesInput] = None
    glueProperties: Optional[GluePropertiesInput] = None
    hyperPodProperties: Optional[HyperPodPropertiesInput] = None
    iamProperties: Optional[IamPropertiesInput] = None
    redshiftProperties: Optional[RedshiftPropertiesInput] = None
    sparkEmrProperties: Optional[SparkEmrPropertiesInput] = None
    sparkGlueProperties: Optional[SparkGluePropertiesInput] = None


class CreateConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    awsLocation: Optional[AwsLocation] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    props: Optional[ConnectionPropertiesInput] = None


