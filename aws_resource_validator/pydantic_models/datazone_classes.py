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

class AcceptChoiceTypeDef(BaseValidatorModel):
    predictionTarget: str
    editedValue: Optional[str] = None
    predictionChoice: Optional[int] = None


class AcceptRuleTypeDef(BaseValidatorModel):
    rule: Optional[AcceptRuleBehaviorType] = None
    threshold: Optional[float] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AcceptedAssetScopeTypeDef(BaseValidatorModel):
    assetId: str
    filterIds: Sequence[str]


class FormOutputTypeDef(BaseValidatorModel):
    formName: str
    content: Optional[str] = None
    typeName: Optional[str] = None
    typeRevision: Optional[str] = None


class AwsConsoleLinkParametersTypeDef(BaseValidatorModel):
    uri: Optional[str] = None


class AddToProjectMemberPoolPolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class ColumnFilterConfigurationOutputTypeDef(BaseValidatorModel):
    includedColumnNames: Optional[List[str]] = None


class ColumnFilterConfigurationTypeDef(BaseValidatorModel):
    includedColumnNames: Optional[Sequence[str]] = None


class AssetInDataProductListingItemTypeDef(BaseValidatorModel):
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None


class AssetListingDetailsTypeDef(BaseValidatorModel):
    listingId: str
    listingStatus: ListingStatusType


class DetailedGlossaryTermTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    shortDescription: Optional[str] = None


class AssetScopeTypeDef(BaseValidatorModel):
    assetId: str
    filterIds: List[str]
    status: str
    errorMessage: Optional[str] = None


class AssetTargetNameMapTypeDef(BaseValidatorModel):
    assetId: str
    targetName: str


class FormEntryOutputTypeDef(BaseValidatorModel):
    typeName: str
    typeRevision: str
    required: Optional[bool] = None


class AssetTypesForRuleOutputTypeDef(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificAssetTypes: Optional[List[str]] = None


class AssetTypesForRuleTypeDef(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificAssetTypes: Optional[Sequence[str]] = None


class AssociateEnvironmentRoleInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str


class AthenaPropertiesInputTypeDef(BaseValidatorModel):
    workgroupName: Optional[str] = None


class AthenaPropertiesOutputTypeDef(BaseValidatorModel):
    workgroupName: Optional[str] = None


class AthenaPropertiesPatchTypeDef(BaseValidatorModel):
    workgroupName: Optional[str] = None


class BasicAuthenticationCredentialsTypeDef(BaseValidatorModel):
    password: Optional[str] = None
    userName: Optional[str] = None


class AuthorizationCodePropertiesTypeDef(BaseValidatorModel):
    authorizationCode: Optional[str] = None
    redirectUri: Optional[str] = None


class AwsAccountTypeDef(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    awsAccountIdPath: Optional[str] = None


class AwsLocationTypeDef(BaseValidatorModel):
    accessRole: Optional[str] = None
    awsAccountId: Optional[str] = None
    awsRegion: Optional[str] = None
    iamConnectionId: Optional[str] = None


class BusinessNameGenerationConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None


class CancelMetadataGenerationRunInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class CancelSubscriptionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class CloudFormationPropertiesTypeDef(BaseValidatorModel):
    templateUrl: str


class ConfigurableActionParameterTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ConnectionCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    expiration: Optional[datetime] = None
    secretAccessKey: Optional[str] = None
    sessionToken: Optional[str] = None


class HyperPodPropertiesInputTypeDef(BaseValidatorModel):
    clusterName: str


class IamPropertiesInputTypeDef(BaseValidatorModel):
    glueLineageSyncEnabled: Optional[bool] = None


class SparkEmrPropertiesInputTypeDef(BaseValidatorModel):
    computeArn: Optional[str] = None
    instanceProfileArn: Optional[str] = None
    javaVirtualEnv: Optional[str] = None
    logUri: Optional[str] = None
    pythonVirtualEnv: Optional[str] = None
    runtimeRole: Optional[str] = None
    trustedCertificatesS3Uri: Optional[str] = None


class GluePropertiesOutputTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    status: Optional[ConnectionStatusType] = None


class HyperPodPropertiesOutputTypeDef(BaseValidatorModel):
    clusterName: str
    clusterArn: Optional[str] = None
    orchestrator: Optional[HyperPodOrchestratorType] = None


class IamPropertiesOutputTypeDef(BaseValidatorModel):
    environmentId: Optional[str] = None
    glueLineageSyncEnabled: Optional[bool] = None


class IamPropertiesPatchTypeDef(BaseValidatorModel):
    glueLineageSyncEnabled: Optional[bool] = None


class SparkEmrPropertiesPatchTypeDef(BaseValidatorModel):
    computeArn: Optional[str] = None
    instanceProfileArn: Optional[str] = None
    javaVirtualEnv: Optional[str] = None
    logUri: Optional[str] = None
    pythonVirtualEnv: Optional[str] = None
    runtimeRole: Optional[str] = None
    trustedCertificatesS3Uri: Optional[str] = None


class FormInputTypeDef(BaseValidatorModel):
    formName: str
    content: Optional[str] = None
    typeIdentifier: Optional[str] = None
    typeRevision: Optional[str] = None


class FormEntryInputTypeDef(BaseValidatorModel):
    typeIdentifier: str
    typeRevision: str
    required: Optional[bool] = None


class CreateAssetTypePolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class DataProductItemOutputTypeDef(BaseValidatorModel):
    identifier: str
    itemType: Literal["ASSET"]
    glossaryTerms: Optional[List[str]] = None
    revision: Optional[str] = None


class RecommendationConfigurationTypeDef(BaseValidatorModel):
    enableBusinessNameGeneration: Optional[bool] = None


class ScheduleConfigurationTypeDef(BaseValidatorModel):
    schedule: Optional[str] = None
    timezone: Optional[TimezoneType] = None


class DataSourceErrorMessageTypeDef(BaseValidatorModel):
    errorType: DataSourceErrorTypeType
    errorDetail: Optional[str] = None


class CreateDomainUnitInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    parentDomainUnitIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class CreateDomainUnitPolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class EnvironmentParameterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class CustomParameterTypeDef(BaseValidatorModel):
    fieldType: str
    keyName: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    isEditable: Optional[bool] = None
    isOptional: Optional[bool] = None


class DeploymentPropertiesTypeDef(BaseValidatorModel):
    endTimeoutMinutes: Optional[int] = None
    startTimeoutMinutes: Optional[int] = None


class CreateEnvironmentProfilePolicyGrantDetailTypeDef(BaseValidatorModel):
    domainUnitId: Optional[str] = None


class ModelTypeDef(BaseValidatorModel):
    smithy: Optional[str] = None


class CreateFormTypePolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class CreateGlossaryInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    status: Optional[GlossaryStatusType] = None


class CreateGlossaryPolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class TermRelationsOutputTypeDef(BaseValidatorModel):
    classifies: Optional[List[str]] = None
    isA: Optional[List[str]] = None


class CreateGroupProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    clientToken: Optional[str] = None


class CreateListingChangeSetInputTypeDef(BaseValidatorModel):
    action: ChangeActionType
    domainIdentifier: str
    entityIdentifier: str
    entityType: EntityTypeType
    clientToken: Optional[str] = None
    entityRevision: Optional[str] = None


class CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None
    projectProfiles: Optional[List[str]] = None


class CreateProjectFromProjectProfilePolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None
    projectProfiles: Optional[Sequence[str]] = None


class MemberTypeDef(BaseValidatorModel):
    groupIdentifier: Optional[str] = None
    userIdentifier: Optional[str] = None


class ProjectDeletionErrorTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class CreateProjectPolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class SubscribedListingInputTypeDef(BaseValidatorModel):
    identifier: str


class SubscriptionTargetFormTypeDef(BaseValidatorModel):
    content: str
    formName: str


class CreateUserProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    userIdentifier: str
    clientToken: Optional[str] = None
    userType: Optional[UserTypeType] = None


class DataProductItemTypeDef(BaseValidatorModel):
    identifier: str
    itemType: Literal["ASSET"]
    glossaryTerms: Optional[Sequence[str]] = None
    revision: Optional[str] = None


class DataProductListingItemAdditionalAttributesTypeDef(BaseValidatorModel):
    forms: Optional[str] = None


class SageMakerRunConfigurationInputTypeDef(BaseValidatorModel):
    trackingAssets: Mapping[str, Sequence[str]]


class SageMakerRunConfigurationOutputTypeDef(BaseValidatorModel):
    trackingAssets: Dict[str, List[str]]
    accountId: Optional[str] = None
    region: Optional[str] = None


class LineageInfoTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    eventId: Optional[str] = None
    eventStatus: Optional[LineageEventProcessingStatusType] = None


class DataSourceRunLineageSummaryTypeDef(BaseValidatorModel):
    importStatus: Optional[LineageImportStatusType] = None


class RunStatisticsForAssetsTypeDef(BaseValidatorModel):
    added: Optional[int] = None
    failed: Optional[int] = None
    skipped: Optional[int] = None
    unchanged: Optional[int] = None
    updated: Optional[int] = None


class DeleteAssetFilterInputTypeDef(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str


class DeleteAssetInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteAssetTypeInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteConnectionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteDataProductInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteDataSourceInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None


class DeleteDomainInputTypeDef(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    skipDeletionCheck: Optional[bool] = None


class DeleteDomainUnitInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteEnvironmentActionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class DeleteEnvironmentBlueprintConfigurationInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str


class DeleteEnvironmentInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteEnvironmentProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteFormTypeInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    formTypeIdentifier: str


class DeleteGlossaryInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteGlossaryTermInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteListingInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteProjectInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    skipDeletionCheck: Optional[bool] = None


class DeleteProjectProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteRuleInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteSubscriptionGrantInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteSubscriptionRequestInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteSubscriptionTargetInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class DeleteTimeSeriesDataPointsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    clientToken: Optional[str] = None


class EnvironmentErrorTypeDef(BaseValidatorModel):
    message: str
    code: Optional[str] = None


class DisassociateEnvironmentRoleInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str


class DomainUnitFilterForProjectTypeDef(BaseValidatorModel):
    domainUnit: str
    includeChildDomainUnits: Optional[bool] = None


class DomainUnitGrantFilterOutputTypeDef(BaseValidatorModel):
    allDomainUnitsGrantFilter: Optional[Dict[str, Any]] = None


class DomainUnitGrantFilterTypeDef(BaseValidatorModel):
    allDomainUnitsGrantFilter: Optional[Mapping[str, Any]] = None


class DomainUnitGroupPropertiesTypeDef(BaseValidatorModel):
    groupId: Optional[str] = None


class DomainUnitUserPropertiesTypeDef(BaseValidatorModel):
    userId: Optional[str] = None


class DomainUnitTargetTypeDef(BaseValidatorModel):
    domainUnitId: str
    includeChildDomainUnits: Optional[bool] = None


class RegionTypeDef(BaseValidatorModel):
    regionName: Optional[str] = None
    regionNamePath: Optional[str] = None


class EnvironmentConfigurationParameterTypeDef(BaseValidatorModel):
    isEditable: Optional[bool] = None
    name: Optional[str] = None
    value: Optional[str] = None


class EqualToExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class FailureCauseTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    attribute: str
    value: str


class ImportTypeDef(BaseValidatorModel):
    name: str
    revision: str


class GetAssetFilterInputTypeDef(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str


class GetAssetInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetAssetTypeInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetConnectionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    withSecret: Optional[bool] = None


class GetDataProductInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetDataSourceInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetDataSourceRunInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetDomainInputTypeDef(BaseValidatorModel):
    identifier: str


class GetDomainUnitInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetEnvironmentActionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class GetEnvironmentBlueprintConfigurationInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str


class GetEnvironmentBlueprintInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetEnvironmentCredentialsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str


class GetEnvironmentInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetEnvironmentProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetFormTypeInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    formTypeIdentifier: str
    revision: Optional[str] = None


class GetGlossaryInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetGlossaryTermInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetGroupProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str


class GetIamPortalLoginUrlInputTypeDef(BaseValidatorModel):
    domainIdentifier: str


class GetJobRunInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class JobRunErrorTypeDef(BaseValidatorModel):
    message: str


class GetLineageEventInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetListingInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    listingRevision: Optional[str] = None


class GetMetadataGenerationRunInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetProjectInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetProjectProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetRuleInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


class GetSubscriptionGrantInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetSubscriptionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetSubscriptionRequestDetailsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class GetSubscriptionTargetInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class GetTimeSeriesDataPointInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    identifier: str


class PhysicalConnectionRequirementsOutputTypeDef(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    securityGroupIdList: Optional[List[str]] = None
    subnetId: Optional[str] = None
    subnetIdList: Optional[List[str]] = None


class GlueOAuth2CredentialsTypeDef(BaseValidatorModel):
    accessToken: Optional[str] = None
    jwtToken: Optional[str] = None
    refreshToken: Optional[str] = None
    userManagedClientApplicationClientSecret: Optional[str] = None


class SelfGrantStatusDetailTypeDef(BaseValidatorModel):
    databaseName: str
    status: SelfGrantStatusType
    failureCause: Optional[str] = None
    schemaName: Optional[str] = None


class ListingRevisionInputTypeDef(BaseValidatorModel):
    identifier: str
    revision: str


class GreaterThanExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class GreaterThanOrEqualToExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class GroupDetailsTypeDef(BaseValidatorModel):
    groupId: str


class GroupPolicyGrantPrincipalTypeDef(BaseValidatorModel):
    groupIdentifier: Optional[str] = None


class IamUserProfileDetailsTypeDef(BaseValidatorModel):
    arn: Optional[str] = None


class InExpressionOutputTypeDef(BaseValidatorModel):
    columnName: str
    values: List[str]


class InExpressionTypeDef(BaseValidatorModel):
    columnName: str
    values: Sequence[str]


class IsNotNullExpressionTypeDef(BaseValidatorModel):
    columnName: str


class IsNullExpressionTypeDef(BaseValidatorModel):
    columnName: str


class LakeFormationConfigurationOutputTypeDef(BaseValidatorModel):
    locationRegistrationExcludeS3Locations: Optional[List[str]] = None
    locationRegistrationRole: Optional[str] = None


class LakeFormationConfigurationTypeDef(BaseValidatorModel):
    locationRegistrationExcludeS3Locations: Optional[Sequence[str]] = None
    locationRegistrationRole: Optional[str] = None


class LessThanExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class LessThanOrEqualToExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class LikeExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class LineageSqlQueryRunDetailsTypeDef(BaseValidatorModel):
    errorMessages: Optional[List[str]] = None
    numQueriesFailed: Optional[int] = None
    queryEndTime: Optional[datetime] = None
    queryStartTime: Optional[datetime] = None
    totalQueriesProcessed: Optional[int] = None


class LineageSyncScheduleTypeDef(BaseValidatorModel):
    schedule: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssetFiltersInputTypeDef(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[FilterStatusType] = None


class ListAssetRevisionsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataProductRevisionsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDataSourceRunActivitiesInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataAssetActivityStatusType] = None


class ListDataSourceRunsInputTypeDef(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceRunStatusType] = None


class ListDomainUnitsForParentInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    parentDomainUnitIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDomainsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DomainStatusType] = None


class ListEntityOwnersInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentActionsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentBlueprintConfigurationsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEnvironmentBlueprintsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None


class ListEnvironmentProfilesInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    projectIdentifier: Optional[str] = None


class ListEnvironmentsInputTypeDef(BaseValidatorModel):
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


class ListJobRunsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    jobIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[JobRunStatusType] = None


class ListPolicyGrantsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListProjectMembershipsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListProjectProfilesInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListProjectsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    userIdentifier: Optional[str] = None


class ListRulesInputTypeDef(BaseValidatorModel):
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


class ListSubscriptionGrantsInputTypeDef(BaseValidatorModel):
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


class ListSubscriptionRequestsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None


class ListSubscriptionTargetsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None


class ListSubscriptionsInputTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class UserDetailsTypeDef(BaseValidatorModel):
    userId: str


class MetadataFormReferenceTypeDef(BaseValidatorModel):
    typeIdentifier: str
    typeRevision: str


class MetadataFormSummaryTypeDef(BaseValidatorModel):
    typeName: str
    typeRevision: str
    formName: Optional[str] = None


class NameIdentifierTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    namespace: Optional[str] = None


class NotEqualToExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class NotInExpressionOutputTypeDef(BaseValidatorModel):
    columnName: str
    values: List[str]


class NotInExpressionTypeDef(BaseValidatorModel):
    columnName: str
    values: Sequence[str]


class NotLikeExpressionTypeDef(BaseValidatorModel):
    columnName: str
    value: str


class OAuth2ClientApplicationTypeDef(BaseValidatorModel):
    aWSManagedClientApplicationReference: Optional[str] = None
    userManagedClientApplicationClientId: Optional[str] = None


class OverrideDomainUnitOwnersPolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class OverrideProjectOwnersPolicyGrantDetailTypeDef(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


class OwnerGroupPropertiesOutputTypeDef(BaseValidatorModel):
    groupId: Optional[str] = None


class OwnerGroupPropertiesTypeDef(BaseValidatorModel):
    groupIdentifier: str


class OwnerUserPropertiesOutputTypeDef(BaseValidatorModel):
    userId: Optional[str] = None


class OwnerUserPropertiesTypeDef(BaseValidatorModel):
    userIdentifier: str


class PhysicalConnectionRequirementsTypeDef(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    securityGroupIdList: Optional[Sequence[str]] = None
    subnetId: Optional[str] = None
    subnetIdList: Optional[Sequence[str]] = None


class UserPolicyGrantPrincipalOutputTypeDef(BaseValidatorModel):
    allUsersGrantFilter: Optional[Dict[str, Any]] = None
    userIdentifier: Optional[str] = None


class UserPolicyGrantPrincipalTypeDef(BaseValidatorModel):
    allUsersGrantFilter: Optional[Mapping[str, Any]] = None
    userIdentifier: Optional[str] = None


class ProjectsForRuleOutputTypeDef(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: Optional[List[str]] = None


class ProjectsForRuleTypeDef(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: Optional[Sequence[str]] = None


class RedshiftClusterStorageTypeDef(BaseValidatorModel):
    clusterName: str


class RedshiftCredentialConfigurationTypeDef(BaseValidatorModel):
    secretManagerArn: str


class UsernamePasswordTypeDef(BaseValidatorModel):
    password: str
    username: str


class RedshiftStoragePropertiesTypeDef(BaseValidatorModel):
    clusterName: Optional[str] = None
    workgroupName: Optional[str] = None


class RedshiftServerlessStorageTypeDef(BaseValidatorModel):
    workgroupName: str


class RejectChoiceTypeDef(BaseValidatorModel):
    predictionTarget: str
    predictionChoices: Optional[Sequence[int]] = None


class RejectRuleTypeDef(BaseValidatorModel):
    rule: Optional[RejectRuleBehaviorType] = None
    threshold: Optional[float] = None


class RejectSubscriptionRequestInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    decisionComment: Optional[str] = None


class RevokeSubscriptionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    retainPermissions: Optional[bool] = None


class SearchGroupProfilesInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchText: Optional[str] = None


class SearchInItemTypeDef(BaseValidatorModel):
    attribute: str


class SearchSortTypeDef(BaseValidatorModel):
    attribute: str
    order: Optional[SortOrderType] = None


class SearchUserProfilesInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchText: Optional[str] = None


class SparkGlueArgsTypeDef(BaseValidatorModel):
    connection: Optional[str] = None


class SsoUserProfileDetailsTypeDef(BaseValidatorModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    username: Optional[str] = None


class StartDataSourceRunInputTypeDef(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    clientToken: Optional[str] = None


class SubscribedProjectInputTypeDef(BaseValidatorModel):
    identifier: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TermRelationsTypeDef(BaseValidatorModel):
    classifies: Optional[Sequence[str]] = None
    isA: Optional[Sequence[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDomainUnitInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None


class UpdateEnvironmentInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None


class UpdateGlossaryInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[GlossaryStatusType] = None


class UpdateGroupProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    status: GroupProfileStatusType


class UpdateSubscriptionRequestInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    requestReason: str


class AcceptPredictionsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    acceptChoices: Optional[Sequence[AcceptChoiceTypeDef]] = None
    acceptRule: Optional[AcceptRuleTypeDef] = None
    clientToken: Optional[str] = None
    revision: Optional[str] = None


class AcceptPredictionsOutputTypeDef(BaseValidatorModel):
    assetId: str
    domainId: str
    revision: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFormTypeOutputTypeDef(BaseValidatorModel):
    description: str
    domainId: str
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateListingChangeSetOutputTypeDef(BaseValidatorModel):
    listingId: str
    listingRevision: str
    status: ListingStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteConnectionOutputTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDomainOutputTypeDef(BaseValidatorModel):
    status: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetEnvironmentCredentialsOutputTypeDef(BaseValidatorModel):
    accessKeyId: str
    expiration: datetime
    secretAccessKey: str
    sessionToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetIamPortalLoginUrlOutputTypeDef(BaseValidatorModel):
    authCodeUrl: str
    userProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class RejectPredictionsOutputTypeDef(BaseValidatorModel):
    assetId: str
    assetRevision: str
    domainId: str
    ResponseMetadata: ResponseMetadataTypeDef


class AcceptSubscriptionRequestInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    assetScopes: Optional[Sequence[AcceptedAssetScopeTypeDef]] = None
    decisionComment: Optional[str] = None


class ActionParametersTypeDef(BaseValidatorModel):
    awsConsoleLink: Optional[AwsConsoleLinkParametersTypeDef] = None


class AssetFilterSummaryTypeDef(BaseValidatorModel):
    pass


class ListAssetFiltersOutputTypeDef(BaseValidatorModel):
    items: List[AssetFilterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TimeSeriesDataPointSummaryFormOutputTypeDef(BaseValidatorModel):
    pass


class AssetItemAdditionalAttributesTypeDef(BaseValidatorModel):
    formsOutput: Optional[List[FormOutputTypeDef]] = None
    latestTimeSeriesDataPointFormsOutput: Optional[ List[TimeSeriesDataPointSummaryFormOutputTypeDef] ] = None
    readOnlyFormsOutput: Optional[List[FormOutputTypeDef]] = None


class AssetListingItemAdditionalAttributesTypeDef(BaseValidatorModel):
    forms: Optional[str] = None
    latestTimeSeriesDataPointForms: Optional[List[TimeSeriesDataPointSummaryFormOutputTypeDef]] = None


class ListTimeSeriesDataPointsOutputTypeDef(BaseValidatorModel):
    items: List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssetListingTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    assetRevision: Optional[str] = None
    assetType: Optional[str] = None
    createdAt: Optional[datetime] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    latestTimeSeriesDataPointForms: Optional[List[TimeSeriesDataPointSummaryFormOutputTypeDef]] = None
    owningProjectId: Optional[str] = None


class ListingSummaryItemTypeDef(BaseValidatorModel):
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None


class ListingSummaryTypeDef(BaseValidatorModel):
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None


class SubscribedProductListingTypeDef(BaseValidatorModel):
    assetListings: Optional[List[AssetInDataProductListingItemTypeDef]] = None
    description: Optional[str] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    name: Optional[str] = None


class AssetRevisionTypeDef(BaseValidatorModel):
    pass


class ListAssetRevisionsOutputTypeDef(BaseValidatorModel):
    items: List[AssetRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SubscribedAssetListingTypeDef(BaseValidatorModel):
    assetScope: Optional[AssetScopeTypeDef] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None


class AssetTypeItemTypeDef(BaseValidatorModel):
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
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


class CreateAssetTypeOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAssetTypeOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef


class LineageNodeTypeItemTypeDef(BaseValidatorModel):
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    revision: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


class AuthenticationConfigurationPatchTypeDef(BaseValidatorModel):
    basicAuthenticationCredentials: Optional[BasicAuthenticationCredentialsTypeDef] = None
    secretArn: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class PostLineageEventInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    event: BlobTypeDef
    clientToken: Optional[str] = None


class PredictionConfigurationTypeDef(BaseValidatorModel):
    businessNameGeneration: Optional[BusinessNameGenerationConfigurationTypeDef] = None


class ProvisioningPropertiesTypeDef(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationPropertiesTypeDef] = None


class CreateAssetTypeInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    formsInput: Mapping[str, FormEntryInputTypeDef]
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None


class SingleSignOnTypeDef(BaseValidatorModel):
    pass


class CreateDomainInputTypeDef(BaseValidatorModel):
    domainExecutionRole: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainVersion: Optional[DomainVersionType] = None
    kmsKeyIdentifier: Optional[str] = None
    serviceRole: Optional[str] = None
    singleSignOn: Optional[SingleSignOnTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateDomainInputTypeDef(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainExecutionRole: Optional[str] = None
    name: Optional[str] = None
    serviceRole: Optional[str] = None
    singleSignOn: Optional[SingleSignOnTypeDef] = None


class CreateEnvironmentInputTypeDef(BaseValidatorModel):
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
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None


class CreateEnvironmentProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str
    name: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None


class EnvironmentConfigurationUserParameterOutputTypeDef(BaseValidatorModel):
    environmentConfigurationName: Optional[str] = None
    environmentParameters: Optional[List[EnvironmentParameterTypeDef]] = None


class EnvironmentConfigurationUserParameterTypeDef(BaseValidatorModel):
    environmentConfigurationName: Optional[str] = None
    environmentParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None


class UpdateEnvironmentProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None


class CreateFormTypeInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    model: ModelTypeDef
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None
    status: Optional[FormTypeStatusType] = None


class CreateProjectMembershipInputTypeDef(BaseValidatorModel):
    designation: UserDesignationType
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str


class DeleteProjectMembershipInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str


class UpdateSubscriptionTargetInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    applicableAssetTypes: Optional[Sequence[str]] = None
    authorizedPrincipals: Optional[Sequence[str]] = None
    manageAccessRole: Optional[str] = None
    name: Optional[str] = None
    provider: Optional[str] = None
    subscriptionTargetConfig: Optional[Sequence[SubscriptionTargetFormTypeDef]] = None


class DataProductRevisionTypeDef(BaseValidatorModel):
    pass


class ListDataProductRevisionsOutputTypeDef(BaseValidatorModel):
    items: List[DataProductRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DataSourceRunActivityTypeDef(BaseValidatorModel):
    createdAt: datetime
    dataAssetStatus: DataAssetActivityStatusType
    dataSourceRunId: str
    database: str
    projectId: str
    technicalName: str
    updatedAt: datetime
    dataAssetId: Optional[str] = None
    errorMessage: Optional[DataSourceErrorMessageTypeDef] = None
    lineageSummary: Optional[LineageInfoTypeDef] = None
    technicalDescription: Optional[str] = None


class DeploymentTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    deploymentStatus: Optional[DeploymentStatusType] = None
    deploymentType: Optional[DeploymentTypeType] = None
    failureReason: Optional[EnvironmentErrorTypeDef] = None
    isDeploymentComplete: Optional[bool] = None
    messages: Optional[List[str]] = None


class EnvironmentDeploymentDetailsOutputTypeDef(BaseValidatorModel):
    environmentFailureReasons: Optional[Dict[str, List[EnvironmentErrorTypeDef]]] = None
    overallDeploymentStatus: Optional[OverallDeploymentStatusType] = None


class EnvironmentDeploymentDetailsTypeDef(BaseValidatorModel):
    environmentFailureReasons: Optional[Mapping[str, Sequence[EnvironmentErrorTypeDef]]] = None
    overallDeploymentStatus: Optional[OverallDeploymentStatusType] = None


class DomainSummaryTypeDef(BaseValidatorModel):
    pass


class ListDomainsOutputTypeDef(BaseValidatorModel):
    items: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ProjectGrantFilterTypeDef(BaseValidatorModel):
    domainUnitFilter: Optional[DomainUnitFilterForProjectTypeDef] = None


class DomainUnitPolicyGrantPrincipalOutputTypeDef(BaseValidatorModel):
    domainUnitDesignation: Literal["OWNER"]
    domainUnitGrantFilter: Optional[DomainUnitGrantFilterOutputTypeDef] = None
    domainUnitIdentifier: Optional[str] = None


class DomainUnitPolicyGrantPrincipalTypeDef(BaseValidatorModel):
    domainUnitDesignation: Literal["OWNER"]
    domainUnitGrantFilter: Optional[DomainUnitGrantFilterTypeDef] = None
    domainUnitIdentifier: Optional[str] = None


class DomainUnitOwnerPropertiesTypeDef(BaseValidatorModel):
    group: Optional[DomainUnitGroupPropertiesTypeDef] = None
    user: Optional[DomainUnitUserPropertiesTypeDef] = None


class DomainUnitSummaryTypeDef(BaseValidatorModel):
    pass


class ListDomainUnitsForParentOutputTypeDef(BaseValidatorModel):
    items: List[DomainUnitSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RuleTargetTypeDef(BaseValidatorModel):
    domainUnitTarget: Optional[DomainUnitTargetTypeDef] = None


class EnvironmentConfigurationParametersDetailsOutputTypeDef(BaseValidatorModel):
    parameterOverrides: Optional[List[EnvironmentConfigurationParameterTypeDef]] = None
    resolvedParameters: Optional[List[EnvironmentConfigurationParameterTypeDef]] = None
    ssmPath: Optional[str] = None


class EnvironmentConfigurationParametersDetailsTypeDef(BaseValidatorModel):
    parameterOverrides: Optional[Sequence[EnvironmentConfigurationParameterTypeDef]] = None
    resolvedParameters: Optional[Sequence[EnvironmentConfigurationParameterTypeDef]] = None
    ssmPath: Optional[str] = None


class EnvironmentProfileSummaryTypeDef(BaseValidatorModel):
    pass


class ListEnvironmentProfilesOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EnvironmentSummaryTypeDef(BaseValidatorModel):
    pass


class ListEnvironmentsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SubscribedAssetTypeDef(BaseValidatorModel):
    assetId: str
    assetRevision: str
    status: SubscriptionGrantStatusType
    assetScope: Optional[AssetScopeTypeDef] = None
    failureCause: Optional[FailureCauseTypeDef] = None
    failureTimestamp: Optional[datetime] = None
    grantedTimestamp: Optional[datetime] = None
    targetName: Optional[str] = None


class UpdateSubscriptionGrantStatusInputTypeDef(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    status: SubscriptionGrantStatusType
    failureCause: Optional[FailureCauseTypeDef] = None
    targetName: Optional[str] = None


class FilterExpressionTypeDef(BaseValidatorModel):
    pass


class RelationalFilterConfigurationOutputTypeDef(BaseValidatorModel):
    databaseName: str
    filterExpressions: Optional[List[FilterExpressionTypeDef]] = None
    schemaName: Optional[str] = None


class RelationalFilterConfigurationTypeDef(BaseValidatorModel):
    databaseName: str
    filterExpressions: Optional[Sequence[FilterExpressionTypeDef]] = None
    schemaName: Optional[str] = None


class FormTypeDataTypeDef(BaseValidatorModel):
    domainId: str
    name: str
    revision: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    imports: Optional[List[ImportTypeDef]] = None
    model: Optional[ModelTypeDef] = None
    originDomainId: Optional[str] = None
    originProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    status: Optional[FormTypeStatusType] = None


class GetFormTypeOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    imports: List[ImportTypeDef]
    model: ModelTypeDef
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    status: FormTypeStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class JobRunSummaryTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    domainId: Optional[str] = None
    endTime: Optional[datetime] = None
    error: Optional[JobRunErrorTypeDef] = None
    jobId: Optional[str] = None
    jobType: Optional[Literal["LINEAGE"]] = None
    runId: Optional[str] = None
    runMode: Optional[JobRunModeType] = None
    startTime: Optional[datetime] = None
    status: Optional[JobRunStatusType] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetLineageNodeInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    eventTimestamp: Optional[TimestampTypeDef] = None


class ListLineageEventsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    processingStatus: Optional[LineageEventProcessingStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    timestampAfter: Optional[TimestampTypeDef] = None
    timestampBefore: Optional[TimestampTypeDef] = None


class ListLineageNodeHistoryInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[TimestampTypeDef] = None
    eventTimestampLTE: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None


class ListTimeSeriesDataPointsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startedAt: Optional[TimestampTypeDef] = None


class TimeSeriesDataPointFormInputTypeDef(BaseValidatorModel):
    formName: str
    timestamp: TimestampTypeDef
    typeIdentifier: str
    content: Optional[str] = None
    typeRevision: Optional[str] = None


class TimeSeriesDataPointFormOutputTypeDef(BaseValidatorModel):
    pass


class GetTimeSeriesDataPointOutputTypeDef(BaseValidatorModel):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    form: TimeSeriesDataPointFormOutputTypeDef
    formName: str
    ResponseMetadata: ResponseMetadataTypeDef


class PostTimeSeriesDataPointsOutputTypeDef(BaseValidatorModel):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    forms: List[TimeSeriesDataPointFormOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GlueSelfGrantStatusOutputTypeDef(BaseValidatorModel):
    selfGrantStatusDetails: List[SelfGrantStatusDetailTypeDef]


class RedshiftSelfGrantStatusOutputTypeDef(BaseValidatorModel):
    selfGrantStatusDetails: List[SelfGrantStatusDetailTypeDef]


class GrantedEntityInputTypeDef(BaseValidatorModel):
    listing: Optional[ListingRevisionInputTypeDef] = None


class ListingRevisionTypeDef(BaseValidatorModel):
    pass


class GrantedEntityTypeDef(BaseValidatorModel):
    listing: Optional[ListingRevisionTypeDef] = None


class GroupProfileSummaryTypeDef(BaseValidatorModel):
    pass


class SearchGroupProfilesOutputTypeDef(BaseValidatorModel):
    items: List[GroupProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ProvisioningConfigurationOutputTypeDef(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationOutputTypeDef] = None


class LineageNodeSummaryTypeDef(BaseValidatorModel):
    pass


class ListLineageNodeHistoryOutputTypeDef(BaseValidatorModel):
    nodes: List[LineageNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LineageRunDetailsTypeDef(BaseValidatorModel):
    sqlQueryRunDetails: Optional[LineageSqlQueryRunDetailsTypeDef] = None


class RedshiftLineageSyncConfigurationInputTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    schedule: Optional[LineageSyncScheduleTypeDef] = None


class RedshiftLineageSyncConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    lineageJobId: Optional[str] = None
    schedule: Optional[LineageSyncScheduleTypeDef] = None


class ListAssetFiltersInputPaginateTypeDef(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    status: Optional[FilterStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssetRevisionsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataProductRevisionsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSourceRunActivitiesInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    status: Optional[DataAssetActivityStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSourceRunsInputPaginateTypeDef(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    status: Optional[DataSourceRunStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainUnitsForParentInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    parentDomainUnitIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainsInputPaginateTypeDef(BaseValidatorModel):
    status: Optional[DomainStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEntityOwnersInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentActionsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentBlueprintsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentProfilesInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    name: Optional[str] = None
    projectIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEnvironmentsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    environmentProfileIdentifier: Optional[str] = None
    name: Optional[str] = None
    provider: Optional[str] = None
    status: Optional[EnvironmentStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobRunsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    jobIdentifier: str
    sortOrder: Optional[SortOrderType] = None
    status: Optional[JobRunStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLineageEventsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    processingStatus: Optional[LineageEventProcessingStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    timestampAfter: Optional[TimestampTypeDef] = None
    timestampBefore: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLineageNodeHistoryInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[TimestampTypeDef] = None
    eventTimestampLTE: Optional[TimestampTypeDef] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyGrantsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectMembershipsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectProfilesInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    name: Optional[str] = None
    userIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    targetIdentifier: str
    targetType: Literal["DOMAIN_UNIT"]
    action: Optional[Literal["CREATE_SUBSCRIPTION_REQUEST"]] = None
    assetTypes: Optional[Sequence[str]] = None
    dataProduct: Optional[bool] = None
    includeCascaded: Optional[bool] = None
    projectIds: Optional[Sequence[str]] = None
    ruleType: Optional[Literal["METADATA_FORM_ENFORCEMENT"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionGrantsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    subscribedListingId: Optional[str] = None
    subscriptionId: Optional[str] = None
    subscriptionTargetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionRequestsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionTargetsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionStatusType] = None
    subscribedListingId: Optional[str] = None
    subscriptionRequestIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTimeSeriesDataPointsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: Optional[TimestampTypeDef] = None
    startedAt: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchGroupProfilesInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchUserProfilesInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ProjectProfileSummaryTypeDef(BaseValidatorModel):
    pass


class ListProjectProfilesOutputTypeDef(BaseValidatorModel):
    items: List[ProjectProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MemberDetailsTypeDef(BaseValidatorModel):
    group: Optional[GroupDetailsTypeDef] = None
    user: Optional[UserDetailsTypeDef] = None


class MetadataFormEnforcementDetailOutputTypeDef(BaseValidatorModel):
    requiredMetadataForms: Optional[List[MetadataFormReferenceTypeDef]] = None


class MetadataFormEnforcementDetailTypeDef(BaseValidatorModel):
    requiredMetadataForms: Optional[Sequence[MetadataFormReferenceTypeDef]] = None


class OpenLineageRunEventSummaryTypeDef(BaseValidatorModel):
    eventType: Optional[OpenLineageRunStateType] = None
    inputs: Optional[List[NameIdentifierTypeDef]] = None
    job: Optional[NameIdentifierTypeDef] = None
    outputs: Optional[List[NameIdentifierTypeDef]] = None
    runId: Optional[str] = None


class NotificationResourceTypeDef(BaseValidatorModel):
    pass


class TopicTypeDef(BaseValidatorModel):
    resource: NotificationResourceTypeDef
    role: NotificationRoleType
    subject: str


class OAuth2PropertiesOutputTypeDef(BaseValidatorModel):
    authorizationCodeProperties: Optional[AuthorizationCodePropertiesTypeDef] = None
    oAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    oAuth2Credentials: Optional[GlueOAuth2CredentialsTypeDef] = None
    oAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    tokenUrl: Optional[str] = None
    tokenUrlParametersMap: Optional[Dict[str, str]] = None


class OAuth2PropertiesTypeDef(BaseValidatorModel):
    authorizationCodeProperties: Optional[AuthorizationCodePropertiesTypeDef] = None
    oAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    oAuth2Credentials: Optional[GlueOAuth2CredentialsTypeDef] = None
    oAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    tokenUrl: Optional[str] = None
    tokenUrlParametersMap: Optional[Mapping[str, str]] = None


class PolicyGrantDetailOutputTypeDef(BaseValidatorModel):
    addToProjectMemberPool: Optional[AddToProjectMemberPoolPolicyGrantDetailTypeDef] = None
    createAssetType: Optional[CreateAssetTypePolicyGrantDetailTypeDef] = None
    createDomainUnit: Optional[CreateDomainUnitPolicyGrantDetailTypeDef] = None
    createEnvironment: Optional[Dict[str, Any]] = None
    createEnvironmentFromBlueprint: Optional[Dict[str, Any]] = None
    createEnvironmentProfile: Optional[CreateEnvironmentProfilePolicyGrantDetailTypeDef] = None
    createFormType: Optional[CreateFormTypePolicyGrantDetailTypeDef] = None
    createGlossary: Optional[CreateGlossaryPolicyGrantDetailTypeDef] = None
    createProject: Optional[CreateProjectPolicyGrantDetailTypeDef] = None
    createProjectFromProjectProfile: Optional[ CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef ] = None
    delegateCreateEnvironmentProfile: Optional[Dict[str, Any]] = None
    overrideDomainUnitOwners: Optional[OverrideDomainUnitOwnersPolicyGrantDetailTypeDef] = None
    overrideProjectOwners: Optional[OverrideProjectOwnersPolicyGrantDetailTypeDef] = None


class PolicyGrantDetailTypeDef(BaseValidatorModel):
    addToProjectMemberPool: Optional[AddToProjectMemberPoolPolicyGrantDetailTypeDef] = None
    createAssetType: Optional[CreateAssetTypePolicyGrantDetailTypeDef] = None
    createDomainUnit: Optional[CreateDomainUnitPolicyGrantDetailTypeDef] = None
    createEnvironment: Optional[Mapping[str, Any]] = None
    createEnvironmentFromBlueprint: Optional[Mapping[str, Any]] = None
    createEnvironmentProfile: Optional[CreateEnvironmentProfilePolicyGrantDetailTypeDef] = None
    createFormType: Optional[CreateFormTypePolicyGrantDetailTypeDef] = None
    createGlossary: Optional[CreateGlossaryPolicyGrantDetailTypeDef] = None
    createProject: Optional[CreateProjectPolicyGrantDetailTypeDef] = None
    createProjectFromProjectProfile: Optional[ CreateProjectFromProjectProfilePolicyGrantDetailTypeDef ] = None
    delegateCreateEnvironmentProfile: Optional[Mapping[str, Any]] = None
    overrideDomainUnitOwners: Optional[OverrideDomainUnitOwnersPolicyGrantDetailTypeDef] = None
    overrideProjectOwners: Optional[OverrideProjectOwnersPolicyGrantDetailTypeDef] = None


class OwnerPropertiesOutputTypeDef(BaseValidatorModel):
    group: Optional[OwnerGroupPropertiesOutputTypeDef] = None
    user: Optional[OwnerUserPropertiesOutputTypeDef] = None


class OwnerPropertiesTypeDef(BaseValidatorModel):
    group: Optional[OwnerGroupPropertiesTypeDef] = None
    user: Optional[OwnerUserPropertiesTypeDef] = None


class RuleScopeOutputTypeDef(BaseValidatorModel):
    assetType: Optional[AssetTypesForRuleOutputTypeDef] = None
    dataProduct: Optional[bool] = None
    project: Optional[ProjectsForRuleOutputTypeDef] = None


class RuleScopeTypeDef(BaseValidatorModel):
    assetType: Optional[AssetTypesForRuleTypeDef] = None
    dataProduct: Optional[bool] = None
    project: Optional[ProjectsForRuleTypeDef] = None


class RedshiftCredentialsTypeDef(BaseValidatorModel):
    secretArn: Optional[str] = None
    usernamePassword: Optional[UsernamePasswordTypeDef] = None


class SparkEmrPropertiesOutputTypeDef(BaseValidatorModel):
    computeArn: Optional[str] = None
    credentials: Optional[UsernamePasswordTypeDef] = None
    credentialsExpiration: Optional[datetime] = None
    governanceType: Optional[GovernanceTypeType] = None
    instanceProfileArn: Optional[str] = None
    javaVirtualEnv: Optional[str] = None
    livyEndpoint: Optional[str] = None
    logUri: Optional[str] = None
    pythonVirtualEnv: Optional[str] = None
    runtimeRole: Optional[str] = None
    trustedCertificatesS3Uri: Optional[str] = None


class RedshiftStorageTypeDef(BaseValidatorModel):
    redshiftClusterSource: Optional[RedshiftClusterStorageTypeDef] = None
    redshiftServerlessSource: Optional[RedshiftServerlessStorageTypeDef] = None


class RejectPredictionsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    rejectChoices: Optional[Sequence[RejectChoiceTypeDef]] = None
    rejectRule: Optional[RejectRuleTypeDef] = None
    revision: Optional[str] = None


class SparkGluePropertiesInputTypeDef(BaseValidatorModel):
    additionalArgs: Optional[SparkGlueArgsTypeDef] = None
    glueConnectionName: Optional[str] = None
    glueVersion: Optional[str] = None
    idleTimeout: Optional[int] = None
    javaVirtualEnv: Optional[str] = None
    numberOfWorkers: Optional[int] = None
    pythonVirtualEnv: Optional[str] = None
    workerType: Optional[str] = None


class SparkGluePropertiesOutputTypeDef(BaseValidatorModel):
    additionalArgs: Optional[SparkGlueArgsTypeDef] = None
    glueConnectionName: Optional[str] = None
    glueVersion: Optional[str] = None
    idleTimeout: Optional[int] = None
    javaVirtualEnv: Optional[str] = None
    numberOfWorkers: Optional[int] = None
    pythonVirtualEnv: Optional[str] = None
    workerType: Optional[str] = None


class UserProfileDetailsTypeDef(BaseValidatorModel):
    iam: Optional[IamUserProfileDetailsTypeDef] = None
    sso: Optional[SsoUserProfileDetailsTypeDef] = None


class SubscribedPrincipalInputTypeDef(BaseValidatorModel):
    project: Optional[SubscribedProjectInputTypeDef] = None


class SubscribedProjectTypeDef(BaseValidatorModel):
    pass


class SubscribedPrincipalTypeDef(BaseValidatorModel):
    project: Optional[SubscribedProjectTypeDef] = None


class CreateEnvironmentActionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    parameters: ActionParametersTypeDef
    description: Optional[str] = None


class UpdateEnvironmentActionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[ActionParametersTypeDef] = None


class AssetItemTypeDef(BaseValidatorModel):
    domainId: str
    identifier: str
    name: str
    owningProjectId: str
    typeIdentifier: str
    typeRevision: str
    additionalAttributes: Optional[AssetItemAdditionalAttributesTypeDef] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    externalIdentifier: Optional[str] = None
    firstRevisionCreatedAt: Optional[datetime] = None
    firstRevisionCreatedBy: Optional[str] = None
    glossaryTerms: Optional[List[str]] = None


class AssetListingItemTypeDef(BaseValidatorModel):
    additionalAttributes: Optional[AssetListingItemAdditionalAttributesTypeDef] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    listingCreatedBy: Optional[str] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None
    listingUpdatedBy: Optional[str] = None
    name: Optional[str] = None
    owningProjectId: Optional[str] = None


class DataProductListingItemTypeDef(BaseValidatorModel):
    additionalAttributes: Optional[DataProductListingItemAdditionalAttributesTypeDef] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    items: Optional[List[ListingSummaryItemTypeDef]] = None
    listingCreatedBy: Optional[str] = None
    listingId: Optional[str] = None
    listingRevision: Optional[str] = None
    listingUpdatedBy: Optional[str] = None
    name: Optional[str] = None
    owningProjectId: Optional[str] = None


class DataProductListingTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    dataProductId: Optional[str] = None
    dataProductRevision: Optional[str] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    items: Optional[List[ListingSummaryTypeDef]] = None
    owningProjectId: Optional[str] = None


class SubscribedListingItemTypeDef(BaseValidatorModel):
    assetListing: Optional[SubscribedAssetListingTypeDef] = None
    productListing: Optional[SubscribedProductListingTypeDef] = None


class GlueConnectionPatchTypeDef(BaseValidatorModel):
    authenticationConfiguration: Optional[AuthenticationConfigurationPatchTypeDef] = None
    connectionProperties: Optional[Mapping[str, str]] = None
    description: Optional[str] = None


class CreateAssetInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    typeIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    externalIdentifier: Optional[str] = None
    formsInput: Optional[Sequence[FormInputTypeDef]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    predictionConfiguration: Optional[PredictionConfigurationTypeDef] = None
    typeRevision: Optional[str] = None


class CreateAssetRevisionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInputTypeDef]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    predictionConfiguration: Optional[PredictionConfigurationTypeDef] = None
    typeRevision: Optional[str] = None


class DataSourceSummaryTypeDef(BaseValidatorModel):
    pass


class ListDataSourcesOutputTypeDef(BaseValidatorModel):
    items: List[DataSourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ProjectSummaryTypeDef(BaseValidatorModel):
    pass


class ListProjectsOutputTypeDef(BaseValidatorModel):
    items: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SubscriptionTargetSummaryTypeDef(BaseValidatorModel):
    pass


class ListSubscriptionTargetsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionTargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DataProductItemUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataProductInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInputTypeDef]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    items: Optional[Sequence[DataProductItemUnionTypeDef]] = None


class CreateDataProductRevisionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInputTypeDef]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    items: Optional[Sequence[DataProductItemUnionTypeDef]] = None


class ListDataSourceRunActivitiesOutputTypeDef(BaseValidatorModel):
    items: List[DataSourceRunActivityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DataSourceRunSummaryTypeDef(BaseValidatorModel):
    pass


class ListDataSourceRunsOutputTypeDef(BaseValidatorModel):
    items: List[DataSourceRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ProjectPolicyGrantPrincipalTypeDef(BaseValidatorModel):
    projectDesignation: ProjectDesignationType
    projectGrantFilter: Optional[ProjectGrantFilterTypeDef] = None
    projectIdentifier: Optional[str] = None


class FilterClausePaginatorTypeDef(BaseValidatorModel):
    pass


class SearchInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClausePaginatorTypeDef] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchListingsInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClausePaginatorTypeDef] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchTypesInputPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClausePaginatorTypeDef] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class FilterClauseTypeDef(BaseValidatorModel):
    pass


class SearchInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClauseTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None


class SearchListingsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClauseTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None


class SearchTypesInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClauseTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None


class GlueRunConfigurationOutputTypeDef(BaseValidatorModel):
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: Optional[str] = None
    autoImportDataQualityResult: Optional[bool] = None
    catalogName: Optional[str] = None
    dataAccessRole: Optional[str] = None
    region: Optional[str] = None


class SearchTypesResultItemTypeDef(BaseValidatorModel):
    assetTypeItem: Optional[AssetTypeItemTypeDef] = None
    formTypeItem: Optional[FormTypeDataTypeDef] = None
    lineageNodeTypeItem: Optional[LineageNodeTypeItemTypeDef] = None


class ListJobRunsOutputTypeDef(BaseValidatorModel):
    items: List[JobRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PostTimeSeriesDataPointsInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    forms: Sequence[TimeSeriesDataPointFormInputTypeDef]
    clientToken: Optional[str] = None


class MetadataGenerationRunItemTypeDef(BaseValidatorModel):
    pass


class ListMetadataGenerationRunsOutputTypeDef(BaseValidatorModel):
    items: List[MetadataGenerationRunItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SelfGrantStatusOutputTypeDef(BaseValidatorModel):
    glueSelfGrantStatus: Optional[GlueSelfGrantStatusOutputTypeDef] = None
    redshiftSelfGrantStatus: Optional[RedshiftSelfGrantStatusOutputTypeDef] = None


class CreateSubscriptionGrantInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    grantedEntity: GrantedEntityInputTypeDef
    assetTargetNames: Optional[Sequence[AssetTargetNameMapTypeDef]] = None
    clientToken: Optional[str] = None
    subscriptionTargetIdentifier: Optional[str] = None


class EnvironmentBlueprintConfigurationItemTypeDef(BaseValidatorModel):
    domainId: str
    environmentBlueprintId: str
    createdAt: Optional[datetime] = None
    enabledRegions: Optional[List[str]] = None
    environmentRolePermissionBoundary: Optional[str] = None
    manageAccessRoleArn: Optional[str] = None
    provisioningConfigurations: Optional[List[ProvisioningConfigurationOutputTypeDef]] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Dict[str, Dict[str, str]]] = None
    updatedAt: Optional[datetime] = None


class GetEnvironmentBlueprintConfigurationOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    environmentRolePermissionBoundary: str
    manageAccessRoleArn: str
    provisioningConfigurations: List[ProvisioningConfigurationOutputTypeDef]
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PutEnvironmentBlueprintConfigurationOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    environmentRolePermissionBoundary: str
    manageAccessRoleArn: str
    provisioningConfigurations: List[ProvisioningConfigurationOutputTypeDef]
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class LakeFormationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ProvisioningConfigurationTypeDef(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationUnionTypeDef] = None


class JobRunDetailsTypeDef(BaseValidatorModel):
    lineageRunDetails: Optional[LineageRunDetailsTypeDef] = None


class ProjectMemberTypeDef(BaseValidatorModel):
    designation: UserDesignationType
    memberDetails: MemberDetailsTypeDef


class RuleDetailOutputTypeDef(BaseValidatorModel):
    metadataFormEnforcementDetail: Optional[MetadataFormEnforcementDetailOutputTypeDef] = None


class RuleDetailTypeDef(BaseValidatorModel):
    metadataFormEnforcementDetail: Optional[MetadataFormEnforcementDetailTypeDef] = None


class EventSummaryTypeDef(BaseValidatorModel):
    openLineageRunEventSummary: Optional[OpenLineageRunEventSummaryTypeDef] = None


class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    oAuth2Properties: Optional[OAuth2PropertiesOutputTypeDef] = None
    secretArn: Optional[str] = None


class ListEntityOwnersOutputTypeDef(BaseValidatorModel):
    owners: List[OwnerPropertiesOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AddEntityOwnerInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    owner: OwnerPropertiesTypeDef
    clientToken: Optional[str] = None


class RemoveEntityOwnerInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["DOMAIN_UNIT"]
    owner: OwnerPropertiesTypeDef
    clientToken: Optional[str] = None


class RuleSummaryTypeDef(BaseValidatorModel):
    action: Optional[Literal["CREATE_SUBSCRIPTION_REQUEST"]] = None
    identifier: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    name: Optional[str] = None
    revision: Optional[str] = None
    ruleType: Optional[Literal["METADATA_FORM_ENFORCEMENT"]] = None
    scope: Optional[RuleScopeOutputTypeDef] = None
    target: Optional[RuleTargetTypeDef] = None
    targetType: Optional[Literal["DOMAIN_UNIT"]] = None
    updatedAt: Optional[datetime] = None


class RedshiftPropertiesInputTypeDef(BaseValidatorModel):
    credentials: Optional[RedshiftCredentialsTypeDef] = None
    databaseName: Optional[str] = None
    host: Optional[str] = None
    lineageSync: Optional[RedshiftLineageSyncConfigurationInputTypeDef] = None
    port: Optional[int] = None
    storage: Optional[RedshiftStoragePropertiesTypeDef] = None


class RedshiftPropertiesOutputTypeDef(BaseValidatorModel):
    credentials: Optional[RedshiftCredentialsTypeDef] = None
    databaseName: Optional[str] = None
    isProvisionedSecret: Optional[bool] = None
    jdbcIamUrl: Optional[str] = None
    jdbcUrl: Optional[str] = None
    lineageSync: Optional[RedshiftLineageSyncConfigurationOutputTypeDef] = None
    redshiftTempDir: Optional[str] = None
    status: Optional[ConnectionStatusType] = None
    storage: Optional[RedshiftStoragePropertiesTypeDef] = None


class RedshiftPropertiesPatchTypeDef(BaseValidatorModel):
    credentials: Optional[RedshiftCredentialsTypeDef] = None
    databaseName: Optional[str] = None
    host: Optional[str] = None
    lineageSync: Optional[RedshiftLineageSyncConfigurationInputTypeDef] = None
    port: Optional[int] = None
    storage: Optional[RedshiftStoragePropertiesTypeDef] = None


class RedshiftRunConfigurationOutputTypeDef(BaseValidatorModel):
    redshiftStorage: RedshiftStorageTypeDef
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: Optional[str] = None
    dataAccessRole: Optional[str] = None
    redshiftCredentialConfiguration: Optional[RedshiftCredentialConfigurationTypeDef] = None
    region: Optional[str] = None


class CreateSubscriptionRequestInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    requestReason: str
    subscribedListings: Sequence[SubscribedListingInputTypeDef]
    subscribedPrincipals: Sequence[SubscribedPrincipalInputTypeDef]
    clientToken: Optional[str] = None
    metadataForms: Optional[Sequence[FormInputTypeDef]] = None


class TermRelationsUnionTypeDef(BaseValidatorModel):
    pass


class CreateGlossaryTermInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    glossaryIdentifier: str
    name: str
    clientToken: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsUnionTypeDef] = None


class UpdateGlossaryTermInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    glossaryIdentifier: Optional[str] = None
    longDescription: Optional[str] = None
    name: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsUnionTypeDef] = None


class EnvironmentActionSummaryTypeDef(BaseValidatorModel):
    pass


class ListEnvironmentActionsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DataProductResultItemTypeDef(BaseValidatorModel):
    pass


class GlossaryItemTypeDef(BaseValidatorModel):
    pass


class GlossaryTermItemTypeDef(BaseValidatorModel):
    pass


class SearchInventoryResultItemTypeDef(BaseValidatorModel):
    assetItem: Optional[AssetItemTypeDef] = None
    dataProductItem: Optional[DataProductResultItemTypeDef] = None
    glossaryItem: Optional[GlossaryItemTypeDef] = None
    glossaryTermItem: Optional[GlossaryTermItemTypeDef] = None


class SearchResultItemTypeDef(BaseValidatorModel):
    assetListing: Optional[AssetListingItemTypeDef] = None
    dataProductListing: Optional[DataProductListingItemTypeDef] = None


class ListingItemTypeDef(BaseValidatorModel):
    assetListing: Optional[AssetListingTypeDef] = None
    dataProductListing: Optional[DataProductListingTypeDef] = None


class GluePropertiesPatchTypeDef(BaseValidatorModel):
    glueConnectionInput: Optional[GlueConnectionPatchTypeDef] = None


class EnvironmentBlueprintSummaryTypeDef(BaseValidatorModel):
    pass


class ListEnvironmentBlueprintsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentBlueprintSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EnvironmentConfigurationUserParameterUnionTypeDef(BaseValidatorModel):
    pass


class CreateProjectInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    domainUnitId: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    projectProfileId: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentConfigurationUserParameterUnionTypeDef]] = None


class EnvironmentDeploymentDetailsUnionTypeDef(BaseValidatorModel):
    pass


class UpdateProjectInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    environmentDeploymentDetails: Optional[EnvironmentDeploymentDetailsUnionTypeDef] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None


class PolicyGrantPrincipalOutputTypeDef(BaseValidatorModel):
    domainUnit: Optional[DomainUnitPolicyGrantPrincipalOutputTypeDef] = None
    group: Optional[GroupPolicyGrantPrincipalTypeDef] = None
    project: Optional[ProjectPolicyGrantPrincipalTypeDef] = None
    user: Optional[UserPolicyGrantPrincipalOutputTypeDef] = None


class PolicyGrantPrincipalTypeDef(BaseValidatorModel):
    domainUnit: Optional[DomainUnitPolicyGrantPrincipalTypeDef] = None
    group: Optional[GroupPolicyGrantPrincipalTypeDef] = None
    project: Optional[ProjectPolicyGrantPrincipalTypeDef] = None
    user: Optional[UserPolicyGrantPrincipalTypeDef] = None


class RelationalFilterConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class GlueRunConfigurationInputTypeDef(BaseValidatorModel):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationUnionTypeDef]
    autoImportDataQualityResult: Optional[bool] = None
    catalogName: Optional[str] = None
    dataAccessRole: Optional[str] = None


class RedshiftRunConfigurationInputTypeDef(BaseValidatorModel):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationUnionTypeDef]
    dataAccessRole: Optional[str] = None
    redshiftCredentialConfiguration: Optional[RedshiftCredentialConfigurationTypeDef] = None
    redshiftStorage: Optional[RedshiftStorageTypeDef] = None


class SearchTypesOutputTypeDef(BaseValidatorModel):
    items: List[SearchTypesResultItemTypeDef]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SubscriptionGrantSummaryTypeDef(BaseValidatorModel):
    pass


class ListSubscriptionGrantsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionGrantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListEnvironmentBlueprintConfigurationsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentBlueprintConfigurationItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListProjectMembershipsOutputTypeDef(BaseValidatorModel):
    members: List[ProjectMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateRuleOutputTypeDef(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutputTypeDef
    identifier: str
    name: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutputTypeDef
    target: RuleTargetTypeDef
    targetType: Literal["DOMAIN_UNIT"]
    ResponseMetadata: ResponseMetadataTypeDef


class GetRuleOutputTypeDef(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutputTypeDef
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutputTypeDef
    target: RuleTargetTypeDef
    targetType: Literal["DOMAIN_UNIT"]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRuleOutputTypeDef(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutputTypeDef
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal["METADATA_FORM_ENFORCEMENT"]
    scope: RuleScopeOutputTypeDef
    target: RuleTargetTypeDef
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class RowFilterOutputTypeDef(BaseValidatorModel):
    pass


class RowFilterConfigurationOutputTypeDef(BaseValidatorModel):
    rowFilter: RowFilterOutputTypeDef
    sensitive: Optional[bool] = None


class RowFilterTypeDef(BaseValidatorModel):
    pass


class RowFilterConfigurationTypeDef(BaseValidatorModel):
    rowFilter: RowFilterTypeDef
    sensitive: Optional[bool] = None


class NotificationOutputTypeDef(BaseValidatorModel):
    pass


class ListNotificationsOutputTypeDef(BaseValidatorModel):
    notifications: List[NotificationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GlueConnectionTypeDef(BaseValidatorModel):
    athenaProperties: Optional[Dict[str, str]] = None
    authenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None
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
    physicalConnectionRequirements: Optional[PhysicalConnectionRequirementsOutputTypeDef] = None
    pythonProperties: Optional[Dict[str, str]] = None
    sparkProperties: Optional[Dict[str, str]] = None
    status: Optional[ConnectionStatusType] = None
    statusReason: Optional[str] = None


class OAuth2PropertiesUnionTypeDef(BaseValidatorModel):
    pass


class AuthenticationConfigurationInputTypeDef(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    basicAuthenticationCredentials: Optional[BasicAuthenticationCredentialsTypeDef] = None
    customAuthenticationCredentials: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None
    oAuth2Properties: Optional[OAuth2PropertiesUnionTypeDef] = None
    secretArn: Optional[str] = None


class ListRulesOutputTypeDef(BaseValidatorModel):
    items: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConnectionPropertiesOutputTypeDef(BaseValidatorModel):
    athenaProperties: Optional[AthenaPropertiesOutputTypeDef] = None
    glueProperties: Optional[GluePropertiesOutputTypeDef] = None
    hyperPodProperties: Optional[HyperPodPropertiesOutputTypeDef] = None
    iamProperties: Optional[IamPropertiesOutputTypeDef] = None
    redshiftProperties: Optional[RedshiftPropertiesOutputTypeDef] = None
    sparkEmrProperties: Optional[SparkEmrPropertiesOutputTypeDef] = None
    sparkGlueProperties: Optional[SparkGluePropertiesOutputTypeDef] = None


class DataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    glueRunConfiguration: Optional[GlueRunConfigurationOutputTypeDef] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationOutputTypeDef] = None
    sageMakerRunConfiguration: Optional[SageMakerRunConfigurationOutputTypeDef] = None


class UserProfileSummaryTypeDef(BaseValidatorModel):
    pass


class SearchUserProfilesOutputTypeDef(BaseValidatorModel):
    items: List[UserProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchOutputTypeDef(BaseValidatorModel):
    items: List[SearchInventoryResultItemTypeDef]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchListingsOutputTypeDef(BaseValidatorModel):
    items: List[SearchResultItemTypeDef]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConnectionPropertiesPatchTypeDef(BaseValidatorModel):
    athenaProperties: Optional[AthenaPropertiesPatchTypeDef] = None
    glueProperties: Optional[GluePropertiesPatchTypeDef] = None
    iamProperties: Optional[IamPropertiesPatchTypeDef] = None
    redshiftProperties: Optional[RedshiftPropertiesPatchTypeDef] = None
    sparkEmrProperties: Optional[SparkEmrPropertiesPatchTypeDef] = None


class PolicyGrantMemberTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    detail: Optional[PolicyGrantDetailOutputTypeDef] = None
    principal: Optional[PolicyGrantPrincipalOutputTypeDef] = None


class DataSourceConfigurationInputTypeDef(BaseValidatorModel):
    glueRunConfiguration: Optional[GlueRunConfigurationInputTypeDef] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationInputTypeDef] = None
    sageMakerRunConfiguration: Optional[SageMakerRunConfigurationInputTypeDef] = None


class ProvisioningConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutEnvironmentBlueprintConfigurationInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    enabledRegions: Sequence[str]
    environmentBlueprintIdentifier: str
    environmentRolePermissionBoundary: Optional[str] = None
    manageAccessRoleArn: Optional[str] = None
    provisioningConfigurations: Optional[Sequence[ProvisioningConfigurationUnionTypeDef]] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Mapping[str, Mapping[str, str]]] = None


class RuleScopeUnionTypeDef(BaseValidatorModel):
    pass


class RuleDetailUnionTypeDef(BaseValidatorModel):
    pass


class CreateRuleInputTypeDef(BaseValidatorModel):
    action: Literal["CREATE_SUBSCRIPTION_REQUEST"]
    detail: RuleDetailUnionTypeDef
    domainIdentifier: str
    name: str
    scope: RuleScopeUnionTypeDef
    target: RuleTargetTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None


class UpdateRuleInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    detail: Optional[RuleDetailUnionTypeDef] = None
    includeChildDomainUnits: Optional[bool] = None
    name: Optional[str] = None
    scope: Optional[RuleScopeUnionTypeDef] = None


class LineageEventSummaryTypeDef(BaseValidatorModel):
    pass


class ListLineageEventsOutputTypeDef(BaseValidatorModel):
    items: List[LineageEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssetFilterConfigurationOutputTypeDef(BaseValidatorModel):
    columnConfiguration: Optional[ColumnFilterConfigurationOutputTypeDef] = None
    rowConfiguration: Optional[RowFilterConfigurationOutputTypeDef] = None


class AssetFilterConfigurationTypeDef(BaseValidatorModel):
    columnConfiguration: Optional[ColumnFilterConfigurationTypeDef] = None
    rowConfiguration: Optional[RowFilterConfigurationTypeDef] = None


class PhysicalEndpointTypeDef(BaseValidatorModel):
    awsLocation: Optional[AwsLocationTypeDef] = None
    glueConnection: Optional[GlueConnectionTypeDef] = None
    glueConnectionName: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[ProtocolType] = None
    stage: Optional[str] = None


class PhysicalConnectionRequirementsUnionTypeDef(BaseValidatorModel):
    pass


class GlueConnectionInputTypeDef(BaseValidatorModel):
    athenaProperties: Optional[Mapping[str, str]] = None
    authenticationConfiguration: Optional[AuthenticationConfigurationInputTypeDef] = None
    connectionProperties: Optional[Mapping[str, str]] = None
    connectionType: Optional[GlueConnectionTypeType] = None
    description: Optional[str] = None
    matchCriteria: Optional[str] = None
    name: Optional[str] = None
    physicalConnectionRequirements: Optional[PhysicalConnectionRequirementsUnionTypeDef] = None
    pythonProperties: Optional[Mapping[str, str]] = None
    sparkProperties: Optional[Mapping[str, str]] = None
    validateCredentials: Optional[bool] = None
    validateForComputeEnvironments: Optional[Sequence[ComputeEnvironmentsType]] = None


class SubscriptionRequestSummaryTypeDef(BaseValidatorModel):
    pass


class ListSubscriptionRequestsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionRequestSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SubscriptionSummaryTypeDef(BaseValidatorModel):
    pass


class ListSubscriptionsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateConnectionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    awsLocation: Optional[AwsLocationTypeDef] = None
    description: Optional[str] = None
    props: Optional[ConnectionPropertiesPatchTypeDef] = None


class ListPolicyGrantsOutputTypeDef(BaseValidatorModel):
    grantList: List[PolicyGrantMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PolicyGrantDetailUnionTypeDef(BaseValidatorModel):
    pass


class PolicyGrantPrincipalUnionTypeDef(BaseValidatorModel):
    pass


class AddPolicyGrantInputTypeDef(BaseValidatorModel):
    detail: PolicyGrantDetailUnionTypeDef
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    principal: PolicyGrantPrincipalUnionTypeDef
    clientToken: Optional[str] = None


class RemovePolicyGrantInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    principal: PolicyGrantPrincipalUnionTypeDef
    clientToken: Optional[str] = None


class EnvironmentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateProjectProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    domainUnitIdentifier: Optional[str] = None
    environmentConfigurations: Optional[Sequence[EnvironmentConfigurationUnionTypeDef]] = None
    status: Optional[StatusType] = None


class UpdateProjectProfileInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    domainUnitIdentifier: Optional[str] = None
    environmentConfigurations: Optional[Sequence[EnvironmentConfigurationUnionTypeDef]] = None
    name: Optional[str] = None
    status: Optional[StatusType] = None


class UpdateDataSourceInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    assetFormsInput: Optional[Sequence[FormInputTypeDef]] = None
    configuration: Optional[DataSourceConfigurationInputTypeDef] = None
    description: Optional[str] = None
    enableSetting: Optional[EnableSettingType] = None
    name: Optional[str] = None
    publishOnImport: Optional[bool] = None
    recommendation: Optional[RecommendationConfigurationTypeDef] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None
    schedule: Optional[ScheduleConfigurationTypeDef] = None


class GluePropertiesInputTypeDef(BaseValidatorModel):
    glueConnectionInput: Optional[GlueConnectionInputTypeDef] = None


class AssetFilterConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateAssetFilterInputTypeDef(BaseValidatorModel):
    assetIdentifier: str
    configuration: AssetFilterConfigurationUnionTypeDef
    domainIdentifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class UpdateAssetFilterInputTypeDef(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    configuration: Optional[AssetFilterConfigurationUnionTypeDef] = None
    description: Optional[str] = None
    name: Optional[str] = None


class ConnectionSummaryTypeDef(BaseValidatorModel):
    pass


class ListConnectionsOutputTypeDef(BaseValidatorModel):
    items: List[ConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConnectionPropertiesInputTypeDef(BaseValidatorModel):
    athenaProperties: Optional[AthenaPropertiesInputTypeDef] = None
    glueProperties: Optional[GluePropertiesInputTypeDef] = None
    hyperPodProperties: Optional[HyperPodPropertiesInputTypeDef] = None
    iamProperties: Optional[IamPropertiesInputTypeDef] = None
    redshiftProperties: Optional[RedshiftPropertiesInputTypeDef] = None
    sparkEmrProperties: Optional[SparkEmrPropertiesInputTypeDef] = None
    sparkGlueProperties: Optional[SparkGluePropertiesInputTypeDef] = None


class CreateConnectionInputTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    awsLocation: Optional[AwsLocationTypeDef] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    props: Optional[ConnectionPropertiesInputTypeDef] = None


