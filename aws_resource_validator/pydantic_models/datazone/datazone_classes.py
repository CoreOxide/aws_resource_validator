from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.datazone.datazone_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    filterIds: List[str]


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
    includedColumnNames: Optional[List[str]] = None


class AssetFilterSummary(BaseValidatorModel):
    assetId: str
    domainId: str
    id: str
    name: str
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    effectiveColumnNames: Optional[List[str]] = None
    effectiveRowFilter: Optional[str] = None
    errorMessage: Optional[str] = None
    status: Optional[FilterStatusType] = None


class AssetInDataProductListingItem(BaseValidatorModel):
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None


class TimeSeriesDataPointSummaryFormOutput(BaseValidatorModel):
    formName: str
    timestamp: datetime
    typeIdentifier: str
    contentSummary: Optional[str] = None
    id: Optional[str] = None
    typeRevision: Optional[str] = None


class AssetListingDetails(BaseValidatorModel):
    listingId: str
    listingStatus: ListingStatusType


class DetailedGlossaryTerm(BaseValidatorModel):
    name: Optional[str] = None
    shortDescription: Optional[str] = None


class AssetRevision(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    domainId: Optional[str] = None
    id: Optional[str] = None
    revision: Optional[str] = None


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
    specificAssetTypes: Optional[List[str]] = None


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

Blob = Union[str, bytes, IO[Any], StreamingBody]


class BusinessNameGenerationConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None


class CancelMetadataGenerationRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'cancel_subscription' function.
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
    itemType: Literal['ASSET']
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


class SingleSignOn(BaseValidatorModel):
    type: Optional[AuthTypeType] = None
    userAssignment: Optional[UserAssignmentType] = None


# This class is the input for the 'create_domain_unit' function.
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


class Resource(BaseValidatorModel):
    type: str
    value: str
    name: Optional[str] = None
    provider: Optional[str] = None


class CreateEnvironmentProfilePolicyGrantDetail(BaseValidatorModel):
    domainUnitId: Optional[str] = None


class Model(BaseValidatorModel):
    smithy: Optional[str] = None


class CreateFormTypePolicyGrantDetail(BaseValidatorModel):
    includeChildDomainUnits: Optional[bool] = None


# This class is the input for the 'create_glossary' function.
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


# This class is the input for the 'create_group_profile' function.
class CreateGroupProfileInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    clientToken: Optional[str] = None


# This class is the input for the 'create_listing_change_set' function.
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
    projectProfiles: Optional[List[str]] = None


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


# This class is the input for the 'create_user_profile' function.
class CreateUserProfileInput(BaseValidatorModel):
    domainIdentifier: str
    userIdentifier: str
    clientToken: Optional[str] = None
    userType: Optional[UserTypeType] = None


class DataProductItem(BaseValidatorModel):
    identifier: str
    itemType: Literal['ASSET']
    glossaryTerms: Optional[List[str]] = None
    revision: Optional[str] = None


class DataProductListingItemAdditionalAttributes(BaseValidatorModel):
    forms: Optional[str] = None


class DataProductResultItem(BaseValidatorModel):
    domainId: str
    id: str
    name: str
    owningProjectId: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    firstRevisionCreatedAt: Optional[datetime] = None
    firstRevisionCreatedBy: Optional[str] = None
    glossaryTerms: Optional[List[str]] = None


class DataProductRevision(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    domainId: Optional[str] = None
    id: Optional[str] = None
    revision: Optional[str] = None


class SageMakerRunConfigurationInput(BaseValidatorModel):
    trackingAssets: Dict[str, List[str]]


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


# This class is the input for the 'delete_asset_filter' function.
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


# This class is the input for the 'delete_connection' function.
class DeleteConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class DeleteDataProductInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'delete_data_source' function.
class DeleteDataSourceInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None


# This class is the input for the 'delete_domain' function.
class DeleteDomainInput(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    skipDeletionCheck: Optional[bool] = None


class DeleteDomainUnitInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'delete_environment_action' function.
class DeleteEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


class DeleteEnvironmentBlueprintConfigurationInput(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str


# This class is the input for the 'delete_environment' function.
class DeleteEnvironmentInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'delete_environment_profile' function.
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


# This class is the input for the 'delete_subscription_grant' function.
class DeleteSubscriptionGrantInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'delete_subscription_request' function.
class DeleteSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'delete_subscription_target' function.
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


class DomainSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    managedAccountId: str
    name: str
    status: DomainStatusType
    description: Optional[str] = None
    domainVersion: Optional[DomainVersionType] = None
    lastUpdatedAt: Optional[datetime] = None
    portalUrl: Optional[str] = None


class DomainUnitFilterForProject(BaseValidatorModel):
    domainUnit: str
    includeChildDomainUnits: Optional[bool] = None


class DomainUnitGrantFilterOutput(BaseValidatorModel):
    allDomainUnitsGrantFilter: Optional[Dict[str, Any]] = None


class DomainUnitGrantFilter(BaseValidatorModel):
    allDomainUnitsGrantFilter: Optional[Dict[str, Any]] = None


class DomainUnitGroupProperties(BaseValidatorModel):
    groupId: Optional[str] = None


class DomainUnitUserProperties(BaseValidatorModel):
    userId: Optional[str] = None


class DomainUnitSummary(BaseValidatorModel):
    id: str
    name: str


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


class EnvironmentProfileSummary(BaseValidatorModel):
    createdBy: str
    domainId: str
    environmentBlueprintId: str
    id: str
    name: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    projectId: Optional[str] = None
    updatedAt: Optional[datetime] = None


class EnvironmentSummary(BaseValidatorModel):
    createdBy: str
    domainId: str
    name: str
    projectId: str
    provider: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    environmentProfileId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[EnvironmentStatusType] = None
    updatedAt: Optional[datetime] = None


class EqualToExpression(BaseValidatorModel):
    columnName: str
    value: str


class FailureCause(BaseValidatorModel):
    message: Optional[str] = None


class Filter(BaseValidatorModel):
    attribute: str
    value: str


class FilterExpression(BaseValidatorModel):
    expression: str
    type: FilterExpressionTypeType


class Import(BaseValidatorModel):
    name: str
    revision: str


# This class is the input for the 'get_asset_filter' function.
class GetAssetFilterInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_asset' function.
class GetAssetInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


# This class is the input for the 'get_asset_type' function.
class GetAssetTypeInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


# This class is the input for the 'get_connection' function.
class GetConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    withSecret: Optional[bool] = None


# This class is the input for the 'get_data_product' function.
class GetDataProductInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


# This class is the input for the 'get_data_source' function.
class GetDataSourceInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_data_source_run' function.
class GetDataSourceRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_domain' function.
class GetDomainInput(BaseValidatorModel):
    identifier: str


# This class is the input for the 'get_domain_unit' function.
class GetDomainUnitInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_environment_action' function.
class GetEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


# This class is the input for the 'get_environment_blueprint_configuration' function.
class GetEnvironmentBlueprintConfigurationInput(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str


# This class is the input for the 'get_environment_blueprint' function.
class GetEnvironmentBlueprintInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_environment_credentials' function.
class GetEnvironmentCredentialsInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str


# This class is the input for the 'get_environment' function.
class GetEnvironmentInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_environment_profile' function.
class GetEnvironmentProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_form_type' function.
class GetFormTypeInput(BaseValidatorModel):
    domainIdentifier: str
    formTypeIdentifier: str
    revision: Optional[str] = None


# This class is the input for the 'get_glossary' function.
class GetGlossaryInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_glossary_term' function.
class GetGlossaryTermInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_group_profile' function.
class GetGroupProfileInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str


# This class is the input for the 'get_iam_portal_login_url' function.
class GetIamPortalLoginUrlInput(BaseValidatorModel):
    domainIdentifier: str


# This class is the input for the 'get_job_run' function.
class GetJobRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class JobRunError(BaseValidatorModel):
    message: str


# This class is the input for the 'get_lineage_event' function.
class GetLineageEventInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

Timestamp = Union[datetime, str]


class LineageNodeReference(BaseValidatorModel):
    eventTimestamp: Optional[datetime] = None
    id: Optional[str] = None


# This class is the input for the 'get_listing' function.
class GetListingInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    listingRevision: Optional[str] = None


# This class is the input for the 'get_metadata_generation_run' function.
class GetMetadataGenerationRunInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


class MetadataGenerationRunTarget(BaseValidatorModel):
    identifier: str
    type: Literal['ASSET']
    revision: Optional[str] = None


# This class is the input for the 'get_project' function.
class GetProjectInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_project_profile' function.
class GetProjectProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_rule' function.
class GetRuleInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None


# This class is the input for the 'get_subscription_grant' function.
class GetSubscriptionGrantInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_subscription' function.
class GetSubscriptionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_subscription_request_details' function.
class GetSubscriptionRequestDetailsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str


# This class is the input for the 'get_subscription_target' function.
class GetSubscriptionTargetInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str


# This class is the input for the 'get_time_series_data_point' function.
class GetTimeSeriesDataPointInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    identifier: str


class TimeSeriesDataPointFormOutput(BaseValidatorModel):
    formName: str
    timestamp: datetime
    typeIdentifier: str
    content: Optional[str] = None
    id: Optional[str] = None
    typeRevision: Optional[str] = None


# This class is the input for the 'get_user_profile' function.
class GetUserProfileInput(BaseValidatorModel):
    domainIdentifier: str
    userIdentifier: str
    type: Optional[UserProfileTypeType] = None


class GlossaryItem(BaseValidatorModel):
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


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


class ListingRevision(BaseValidatorModel):
    id: str
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


class GroupProfileSummary(BaseValidatorModel):
    domainId: Optional[str] = None
    groupName: Optional[str] = None
    id: Optional[str] = None
    status: Optional[GroupProfileStatusType] = None


class IamUserProfileDetails(BaseValidatorModel):
    arn: Optional[str] = None


class InExpressionOutput(BaseValidatorModel):
    columnName: str
    values: List[str]


class InExpression(BaseValidatorModel):
    columnName: str
    values: List[str]


class IsNotNullExpression(BaseValidatorModel):
    columnName: str


class IsNullExpression(BaseValidatorModel):
    columnName: str


class LakeFormationConfigurationOutput(BaseValidatorModel):
    locationRegistrationExcludeS3Locations: Optional[List[str]] = None
    locationRegistrationRole: Optional[str] = None


class LakeFormationConfiguration(BaseValidatorModel):
    locationRegistrationExcludeS3Locations: Optional[List[str]] = None
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


class LineageNodeSummary(BaseValidatorModel):
    domainId: str
    id: str
    typeName: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    eventTimestamp: Optional[datetime] = None
    name: Optional[str] = None
    sourceIdentifier: Optional[str] = None
    typeRevision: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


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


# This class is the input for the 'list_asset_filters' function.
class ListAssetFiltersInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[FilterStatusType] = None


# This class is the input for the 'list_asset_revisions' function.
class ListAssetRevisionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_connections' function.
class ListConnectionsInput(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    environmentIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['NAME']] = None
    sortOrder: Optional[SortOrderType] = None
    type: Optional[ConnectionTypeType] = None


# This class is the input for the 'list_data_product_revisions' function.
class ListDataProductRevisionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_data_source_run_activities' function.
class ListDataSourceRunActivitiesInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataAssetActivityStatusType] = None


# This class is the input for the 'list_data_source_runs' function.
class ListDataSourceRunsInput(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceRunStatusType] = None


# This class is the input for the 'list_data_sources' function.
class ListDataSourcesInput(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    connectionIdentifier: Optional[str] = None
    environmentIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceStatusType] = None
    type: Optional[str] = None


# This class is the input for the 'list_domain_units_for_parent' function.
class ListDomainUnitsForParentInput(BaseValidatorModel):
    domainIdentifier: str
    parentDomainUnitIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_domains' function.
class ListDomainsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DomainStatusType] = None


# This class is the input for the 'list_entity_owners' function.
class ListEntityOwnersInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal['DOMAIN_UNIT']
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_environment_actions' function.
class ListEnvironmentActionsInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_environment_blueprint_configurations' function.
class ListEnvironmentBlueprintConfigurationsInput(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_environment_blueprints' function.
class ListEnvironmentBlueprintsInput(BaseValidatorModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_environment_profiles' function.
class ListEnvironmentProfilesInput(BaseValidatorModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    projectIdentifier: Optional[str] = None


# This class is the input for the 'list_environments' function.
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


# This class is the input for the 'list_job_runs' function.
class ListJobRunsInput(BaseValidatorModel):
    domainIdentifier: str
    jobIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[JobRunStatusType] = None


# This class is the input for the 'list_metadata_generation_runs' function.
class ListMetadataGenerationRunsInput(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[MetadataGenerationRunStatusType] = None
    type: Optional[Literal['BUSINESS_DESCRIPTIONS']] = None


# This class is the input for the 'list_policy_grants' function.
class ListPolicyGrantsInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TargetEntityTypeType
    policyType: ManagedPolicyTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_project_memberships' function.
class ListProjectMembershipsInput(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['NAME']] = None
    sortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_project_profiles' function.
class ListProjectProfilesInput(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['NAME']] = None
    sortOrder: Optional[SortOrderType] = None


class ProjectProfileSummary(BaseValidatorModel):
    createdBy: str
    domainId: str
    id: str
    name: str
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    domainUnitId: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    status: Optional[StatusType] = None


# This class is the input for the 'list_projects' function.
class ListProjectsInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    userIdentifier: Optional[str] = None


# This class is the input for the 'list_rules' function.
class ListRulesInput(BaseValidatorModel):
    domainIdentifier: str
    targetIdentifier: str
    targetType: Literal['DOMAIN_UNIT']
    action: Optional[Literal['CREATE_SUBSCRIPTION_REQUEST']] = None
    assetTypes: Optional[List[str]] = None
    dataProduct: Optional[bool] = None
    includeCascaded: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    projectIds: Optional[List[str]] = None
    ruleType: Optional[Literal['METADATA_FORM_ENFORCEMENT']] = None


# This class is the input for the 'list_subscription_grants' function.
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


# This class is the input for the 'list_subscription_requests' function.
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


# This class is the input for the 'list_subscription_targets' function.
class ListSubscriptionTargetsInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_subscriptions' function.
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


# This class is the input for the 'list_tags_for_resource' function.
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
    values: List[str]


class NotLikeExpression(BaseValidatorModel):
    columnName: str
    value: str


class NotificationResource(BaseValidatorModel):
    id: str
    type: Literal['PROJECT']
    name: Optional[str] = None


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
    securityGroupIdList: Optional[List[str]] = None
    subnetId: Optional[str] = None
    subnetIdList: Optional[List[str]] = None


class UserPolicyGrantPrincipalOutput(BaseValidatorModel):
    allUsersGrantFilter: Optional[Dict[str, Any]] = None
    userIdentifier: Optional[str] = None


class UserPolicyGrantPrincipal(BaseValidatorModel):
    allUsersGrantFilter: Optional[Dict[str, Any]] = None
    userIdentifier: Optional[str] = None


class ProjectsForRuleOutput(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: Optional[List[str]] = None


class ProjectsForRule(BaseValidatorModel):
    selectionMode: RuleScopeSelectionModeType
    specificProjects: Optional[List[str]] = None


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
    predictionChoices: Optional[List[int]] = None


class RejectRule(BaseValidatorModel):
    rule: Optional[RejectRuleBehaviorType] = None
    threshold: Optional[float] = None


# This class is the input for the 'reject_subscription_request' function.
class RejectSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    decisionComment: Optional[str] = None


# This class is the input for the 'revoke_subscription' function.
class RevokeSubscriptionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    retainPermissions: Optional[bool] = None


# This class is the input for the 'search_group_profiles' function.
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


# This class is the input for the 'search_user_profiles' function.
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


# This class is the input for the 'start_data_source_run' function.
class StartDataSourceRunInput(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    clientToken: Optional[str] = None


class SubscribedProjectInput(BaseValidatorModel):
    identifier: Optional[str] = None


class SubscribedProject(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TermRelations(BaseValidatorModel):
    classifies: Optional[List[str]] = None
    isA: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_domain_unit' function.
class UpdateDomainUnitInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None


# This class is the input for the 'update_environment' function.
class UpdateEnvironmentInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    glossaryTerms: Optional[List[str]] = None
    name: Optional[str] = None


# This class is the input for the 'update_glossary' function.
class UpdateGlossaryInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[GlossaryStatusType] = None


# This class is the input for the 'update_group_profile' function.
class UpdateGroupProfileInput(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    status: GroupProfileStatusType


# This class is the input for the 'update_subscription_request' function.
class UpdateSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    requestReason: str


# This class is the input for the 'update_user_profile' function.
class UpdateUserProfileInput(BaseValidatorModel):
    domainIdentifier: str
    status: UserProfileStatusType
    userIdentifier: str
    type: Optional[UserProfileTypeType] = None


# This class is the input for the 'accept_predictions' function.
class AcceptPredictionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    acceptChoices: Optional[List[AcceptChoice]] = None
    acceptRule: Optional[AcceptRule] = None
    clientToken: Optional[str] = None
    revision: Optional[str] = None


# This class is the output for the 'accept_predictions' function.
class AcceptPredictionsOutput(BaseValidatorModel):
    assetId: str
    domainId: str
    revision: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_form_type' function.
class CreateFormTypeOutput(BaseValidatorModel):
    description: str
    domainId: str
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_glossary' function.
class CreateGlossaryOutput(BaseValidatorModel):
    description: str
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_group_profile' function.
class CreateGroupProfileOutput(BaseValidatorModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_listing_change_set' function.
class CreateListingChangeSetOutput(BaseValidatorModel):
    listingId: str
    listingRevision: str
    status: ListingStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_connection' function.
class DeleteConnectionOutput(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain' function.
class DeleteDomainOutput(BaseValidatorModel):
    status: DomainStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_subscription_target' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment_credentials' function.
class GetEnvironmentCredentialsOutput(BaseValidatorModel):
    accessKeyId: str
    expiration: datetime
    secretAccessKey: str
    sessionToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_glossary' function.
class GetGlossaryOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group_profile' function.
class GetGroupProfileOutput(BaseValidatorModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_iam_portal_login_url' function.
class GetIamPortalLoginUrlOutput(BaseValidatorModel):
    authCodeUrl: str
    userProfileId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_lineage_event' function.
class GetLineageEventOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    event: StreamingBody
    eventTime: datetime
    id: str
    processingStatus: LineageEventProcessingStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'post_lineage_event' function.
class PostLineageEventOutput(BaseValidatorModel):
    domainId: str
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_predictions' function.
class RejectPredictionsOutput(BaseValidatorModel):
    assetId: str
    assetRevision: str
    domainId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_metadata_generation_run' function.
class StartMetadataGenerationRunOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    owningProjectId: str
    status: MetadataGenerationRunStatusType
    type: Literal['BUSINESS_DESCRIPTIONS']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_glossary' function.
class UpdateGlossaryOutput(BaseValidatorModel):
    description: str
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_group_profile' function.
class UpdateGroupProfileOutput(BaseValidatorModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'accept_subscription_request' function.
class AcceptSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    assetScopes: Optional[List[AcceptedAssetScope]] = None
    decisionComment: Optional[str] = None


class ActionParameters(BaseValidatorModel):
    awsConsoleLink: Optional[AwsConsoleLinkParameters] = None


# This class is the output for the 'list_asset_filters' function.
class ListAssetFiltersOutput(BaseValidatorModel):
    items: List[AssetFilterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssetItemAdditionalAttributes(BaseValidatorModel):
    formsOutput: Optional[List[FormOutput]] = None
    latestTimeSeriesDataPointFormsOutput: Optional[List[TimeSeriesDataPointSummaryFormOutput]] = None
    readOnlyFormsOutput: Optional[List[FormOutput]] = None


class AssetListingItemAdditionalAttributes(BaseValidatorModel):
    forms: Optional[str] = None
    latestTimeSeriesDataPointForms: Optional[List[TimeSeriesDataPointSummaryFormOutput]] = None


# This class is the output for the 'list_time_series_data_points' function.
class ListTimeSeriesDataPointsOutput(BaseValidatorModel):
    items: List[TimeSeriesDataPointSummaryFormOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_asset' function.
class GetAssetOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    externalIdentifier: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutput]
    glossaryTerms: List[str]
    id: str
    latestTimeSeriesDataPointFormsOutput: List[TimeSeriesDataPointSummaryFormOutput]
    listing: AssetListingDetails
    name: str
    owningProjectId: str
    readOnlyFormsOutput: List[FormOutput]
    revision: str
    typeIdentifier: str
    typeRevision: str
    ResponseMetadata: ResponseMetadata


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


# This class is the output for the 'list_asset_revisions' function.
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


# This class is the output for the 'create_asset_type' function.
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


# This class is the output for the 'get_asset_type' function.
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


# This class is the input for the 'post_lineage_event' function.
class PostLineageEventInput(BaseValidatorModel):
    domainIdentifier: str
    event: Blob
    clientToken: Optional[str] = None


class PredictionConfiguration(BaseValidatorModel):
    businessNameGeneration: Optional[BusinessNameGenerationConfiguration] = None


class ProvisioningProperties(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationProperties] = None


class ConfigurableEnvironmentAction(BaseValidatorModel):
    parameters: List[ConfigurableActionParameter]
    type: str
    auth: Optional[ConfigurableActionTypeAuthorizationType] = None


# This class is the input for the 'create_asset_type' function.
class CreateAssetTypeInput(BaseValidatorModel):
    domainIdentifier: str
    formsInput: Dict[str, FormEntryInput]
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None


# This class is the output for the 'create_data_product' function.
class CreateDataProductOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutput]
    glossaryTerms: List[str]
    id: str
    items: List[DataProductItemOutput]
    name: str
    owningProjectId: str
    revision: str
    status: DataProductStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_product_revision' function.
class CreateDataProductRevisionOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutput]
    glossaryTerms: List[str]
    id: str
    items: List[DataProductItemOutput]
    name: str
    owningProjectId: str
    revision: str
    status: DataProductStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_product' function.
class GetDataProductOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutput]
    glossaryTerms: List[str]
    id: str
    items: List[DataProductItemOutput]
    name: str
    owningProjectId: str
    revision: str
    status: DataProductStatusType
    ResponseMetadata: ResponseMetadata


class DataSourceSummary(BaseValidatorModel):
    dataSourceId: str
    domainId: str
    name: str
    status: DataSourceStatusType
    type: str
    connectionId: Optional[str] = None
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    enableSetting: Optional[EnableSettingType] = None
    environmentId: Optional[str] = None
    lastRunAssetCount: Optional[int] = None
    lastRunAt: Optional[datetime] = None
    lastRunErrorMessage: Optional[DataSourceErrorMessage] = None
    lastRunStatus: Optional[DataSourceRunStatusType] = None
    schedule: Optional[ScheduleConfiguration] = None
    updatedAt: Optional[datetime] = None


# This class is the input for the 'create_domain' function.
class CreateDomainInput(BaseValidatorModel):
    domainExecutionRole: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainVersion: Optional[DomainVersionType] = None
    kmsKeyIdentifier: Optional[str] = None
    serviceRole: Optional[str] = None
    singleSignOn: Optional[SingleSignOn] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_domain' function.
class CreateDomainOutput(BaseValidatorModel):
    arn: str
    description: str
    domainExecutionRole: str
    domainVersion: DomainVersionType
    id: str
    kmsKeyIdentifier: str
    name: str
    portalUrl: str
    rootDomainUnitId: str
    serviceRole: str
    singleSignOn: SingleSignOn
    status: DomainStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain' function.
class GetDomainOutput(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    domainExecutionRole: str
    domainVersion: DomainVersionType
    id: str
    kmsKeyIdentifier: str
    lastUpdatedAt: datetime
    name: str
    portalUrl: str
    rootDomainUnitId: str
    serviceRole: str
    singleSignOn: SingleSignOn
    status: DomainStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_domain' function.
class UpdateDomainInput(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainExecutionRole: Optional[str] = None
    name: Optional[str] = None
    serviceRole: Optional[str] = None
    singleSignOn: Optional[SingleSignOn] = None


# This class is the output for the 'update_domain' function.
class UpdateDomainOutput(BaseValidatorModel):
    description: str
    domainExecutionRole: str
    id: str
    lastUpdatedAt: datetime
    name: str
    rootDomainUnitId: str
    serviceRole: str
    singleSignOn: SingleSignOn
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_environment' function.
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
    glossaryTerms: Optional[List[str]] = None
    userParameters: Optional[List[EnvironmentParameter]] = None


# This class is the input for the 'create_environment_profile' function.
class CreateEnvironmentProfileInput(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str
    name: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    userParameters: Optional[List[EnvironmentParameter]] = None


class EnvironmentConfigurationUserParameterOutput(BaseValidatorModel):
    environmentConfigurationName: Optional[str] = None
    environmentParameters: Optional[List[EnvironmentParameter]] = None


class EnvironmentConfigurationUserParameter(BaseValidatorModel):
    environmentConfigurationName: Optional[str] = None
    environmentParameters: Optional[List[EnvironmentParameter]] = None


# This class is the input for the 'update_environment_profile' function.
class UpdateEnvironmentProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    userParameters: Optional[List[EnvironmentParameter]] = None


# This class is the output for the 'create_environment_profile' function.
class CreateEnvironmentProfileOutput(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    environmentBlueprintId: str
    id: str
    name: str
    projectId: str
    updatedAt: datetime
    userParameters: List[CustomParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment_profile' function.
class GetEnvironmentProfileOutput(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    environmentBlueprintId: str
    id: str
    name: str
    projectId: str
    updatedAt: datetime
    userParameters: List[CustomParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_environment_profile' function.
class UpdateEnvironmentProfileOutput(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    environmentBlueprintId: str
    id: str
    name: str
    projectId: str
    updatedAt: datetime
    userParameters: List[CustomParameter]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_form_type' function.
class CreateFormTypeInput(BaseValidatorModel):
    domainIdentifier: str
    model: Model
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None
    status: Optional[FormTypeStatusType] = None


# This class is the output for the 'create_glossary_term' function.
class CreateGlossaryTermOutput(BaseValidatorModel):
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_glossary_term' function.
class GetGlossaryTermOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutput
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class GlossaryTermItem(BaseValidatorModel):
    domainId: str
    glossaryId: str
    id: str
    name: str
    status: GlossaryTermStatusType
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None
    termRelations: Optional[TermRelationsOutput] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


# This class is the output for the 'update_glossary_term' function.
class UpdateGlossaryTermOutput(BaseValidatorModel):
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutput
    ResponseMetadata: ResponseMetadata


class CreateProjectMembershipInput(BaseValidatorModel):
    designation: UserDesignationType
    domainIdentifier: str
    member: Member
    projectIdentifier: str


class DeleteProjectMembershipInput(BaseValidatorModel):
    domainIdentifier: str
    member: Member
    projectIdentifier: str


class ProjectSummary(BaseValidatorModel):
    createdBy: str
    domainId: str
    id: str
    name: str
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    domainUnitId: Optional[str] = None
    failureReasons: Optional[List[ProjectDeletionError]] = None
    projectStatus: Optional[ProjectStatusType] = None
    updatedAt: Optional[datetime] = None


# This class is the input for the 'create_subscription_target' function.
class CreateSubscriptionTargetInput(BaseValidatorModel):
    applicableAssetTypes: List[str]
    authorizedPrincipals: List[str]
    domainIdentifier: str
    environmentIdentifier: str
    manageAccessRole: str
    name: str
    subscriptionTargetConfig: List[SubscriptionTargetForm]
    type: str
    clientToken: Optional[str] = None
    provider: Optional[str] = None


# This class is the output for the 'create_subscription_target' function.
class CreateSubscriptionTargetOutput(BaseValidatorModel):
    applicableAssetTypes: List[str]
    authorizedPrincipals: List[str]
    createdAt: datetime
    createdBy: str
    domainId: str
    environmentId: str
    id: str
    manageAccessRole: str
    name: str
    projectId: str
    provider: str
    subscriptionTargetConfig: List[SubscriptionTargetForm]
    type: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_subscription_target' function.
class GetSubscriptionTargetOutput(BaseValidatorModel):
    applicableAssetTypes: List[str]
    authorizedPrincipals: List[str]
    createdAt: datetime
    createdBy: str
    domainId: str
    environmentId: str
    id: str
    manageAccessRole: str
    name: str
    projectId: str
    provider: str
    subscriptionTargetConfig: List[SubscriptionTargetForm]
    type: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class SubscriptionTargetSummary(BaseValidatorModel):
    applicableAssetTypes: List[str]
    authorizedPrincipals: List[str]
    createdAt: datetime
    createdBy: str
    domainId: str
    environmentId: str
    id: str
    name: str
    projectId: str
    provider: str
    subscriptionTargetConfig: List[SubscriptionTargetForm]
    type: str
    manageAccessRole: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None


# This class is the input for the 'update_subscription_target' function.
class UpdateSubscriptionTargetInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    applicableAssetTypes: Optional[List[str]] = None
    authorizedPrincipals: Optional[List[str]] = None
    manageAccessRole: Optional[str] = None
    name: Optional[str] = None
    provider: Optional[str] = None
    subscriptionTargetConfig: Optional[List[SubscriptionTargetForm]] = None


# This class is the output for the 'update_subscription_target' function.
class UpdateSubscriptionTargetOutput(BaseValidatorModel):
    applicableAssetTypes: List[str]
    authorizedPrincipals: List[str]
    createdAt: datetime
    createdBy: str
    domainId: str
    environmentId: str
    id: str
    manageAccessRole: str
    name: str
    projectId: str
    provider: str
    subscriptionTargetConfig: List[SubscriptionTargetForm]
    type: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata

DataProductItemUnion = Union[DataProductItem, DataProductItemOutput]


# This class is the output for the 'list_data_product_revisions' function.
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


class DataSourceRunSummary(BaseValidatorModel):
    createdAt: datetime
    dataSourceId: str
    id: str
    projectId: str
    status: DataSourceRunStatusType
    type: DataSourceRunTypeType
    updatedAt: datetime
    errorMessage: Optional[DataSourceErrorMessage] = None
    lineageSummary: Optional[DataSourceRunLineageSummary] = None
    runStatisticsForAssets: Optional[RunStatisticsForAssets] = None
    startedAt: Optional[datetime] = None
    stoppedAt: Optional[datetime] = None


# This class is the output for the 'get_data_source_run' function.
class GetDataSourceRunOutput(BaseValidatorModel):
    createdAt: datetime
    dataSourceConfigurationSnapshot: str
    dataSourceId: str
    domainId: str
    errorMessage: DataSourceErrorMessage
    id: str
    lineageSummary: DataSourceRunLineageSummary
    projectId: str
    runStatisticsForAssets: RunStatisticsForAssets
    startedAt: datetime
    status: DataSourceRunStatusType
    stoppedAt: datetime
    type: DataSourceRunTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_data_source_run' function.
class StartDataSourceRunOutput(BaseValidatorModel):
    createdAt: datetime
    dataSourceConfigurationSnapshot: str
    dataSourceId: str
    domainId: str
    errorMessage: DataSourceErrorMessage
    id: str
    projectId: str
    runStatisticsForAssets: RunStatisticsForAssets
    startedAt: datetime
    status: DataSourceRunStatusType
    stoppedAt: datetime
    type: DataSourceRunTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


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
    environmentFailureReasons: Optional[Dict[str, List[EnvironmentError]]] = None
    overallDeploymentStatus: Optional[OverallDeploymentStatusType] = None


# This class is the output for the 'list_domains' function.
class ListDomainsOutput(BaseValidatorModel):
    items: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ProjectGrantFilter(BaseValidatorModel):
    domainUnitFilter: Optional[DomainUnitFilterForProject] = None


class DomainUnitPolicyGrantPrincipalOutput(BaseValidatorModel):
    domainUnitDesignation: Literal['OWNER']
    domainUnitGrantFilter: Optional[DomainUnitGrantFilterOutput] = None
    domainUnitIdentifier: Optional[str] = None


class DomainUnitPolicyGrantPrincipal(BaseValidatorModel):
    domainUnitDesignation: Literal['OWNER']
    domainUnitGrantFilter: Optional[DomainUnitGrantFilter] = None
    domainUnitIdentifier: Optional[str] = None


class DomainUnitOwnerProperties(BaseValidatorModel):
    group: Optional[DomainUnitGroupProperties] = None
    user: Optional[DomainUnitUserProperties] = None


# This class is the output for the 'list_domain_units_for_parent' function.
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
    parameterOverrides: Optional[List[EnvironmentConfigurationParameter]] = None
    resolvedParameters: Optional[List[EnvironmentConfigurationParameter]] = None
    ssmPath: Optional[str] = None


# This class is the output for the 'list_environment_profiles' function.
class ListEnvironmentProfilesOutput(BaseValidatorModel):
    items: List[EnvironmentProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environments' function.
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


# This class is the input for the 'update_subscription_grant_status' function.
class UpdateSubscriptionGrantStatusInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    status: SubscriptionGrantStatusType
    failureCause: Optional[FailureCause] = None
    targetName: Optional[str] = None


class FilterClausePaginator(BaseValidatorModel):
    and_: Optional[List[Dict[str, Any]]] = None
    filter: Optional[Filter] = None
    or_: Optional[List[Dict[str, Any]]] = None


class FilterClause(BaseValidatorModel):
    and_: Optional[List[Dict[str, Any]]] = None
    filter: Optional[Filter] = None
    or_: Optional[List[Dict[str, Any]]] = None


class RelationalFilterConfigurationOutput(BaseValidatorModel):
    databaseName: str
    filterExpressions: Optional[List[FilterExpression]] = None
    schemaName: Optional[str] = None


class RelationalFilterConfiguration(BaseValidatorModel):
    databaseName: str
    filterExpressions: Optional[List[FilterExpression]] = None
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


# This class is the output for the 'get_form_type' function.
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
    jobType: Optional[Literal['LINEAGE']] = None
    runId: Optional[str] = None
    runMode: Optional[JobRunModeType] = None
    startTime: Optional[datetime] = None
    status: Optional[JobRunStatusType] = None


# This class is the input for the 'get_lineage_node' function.
class GetLineageNodeInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    eventTimestamp: Optional[Timestamp] = None


# This class is the input for the 'list_lineage_events' function.
class ListLineageEventsInput(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    processingStatus: Optional[LineageEventProcessingStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    timestampAfter: Optional[Timestamp] = None
    timestampBefore: Optional[Timestamp] = None


# This class is the input for the 'list_lineage_node_history' function.
class ListLineageNodeHistoryInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[Timestamp] = None
    eventTimestampLTE: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_notifications' function.
class ListNotificationsInput(BaseValidatorModel):
    domainIdentifier: str
    type: NotificationTypeType
    afterTimestamp: Optional[Timestamp] = None
    beforeTimestamp: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    subjects: Optional[List[str]] = None
    taskStatus: Optional[TaskStatusType] = None


# This class is the input for the 'list_time_series_data_points' function.
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


# This class is the output for the 'get_lineage_node' function.
class GetLineageNodeOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    downstreamNodes: List[LineageNodeReference]
    eventTimestamp: datetime
    formsOutput: List[FormOutput]
    id: str
    name: str
    sourceIdentifier: str
    typeName: str
    typeRevision: str
    updatedAt: datetime
    updatedBy: str
    upstreamNodes: List[LineageNodeReference]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_metadata_generation_run' function.
class GetMetadataGenerationRunOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    owningProjectId: str
    status: MetadataGenerationRunStatusType
    target: MetadataGenerationRunTarget
    type: Literal['BUSINESS_DESCRIPTIONS']
    ResponseMetadata: ResponseMetadata


class MetadataGenerationRunItem(BaseValidatorModel):
    domainId: str
    id: str
    owningProjectId: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    status: Optional[MetadataGenerationRunStatusType] = None
    target: Optional[MetadataGenerationRunTarget] = None
    type: Optional[Literal['BUSINESS_DESCRIPTIONS']] = None


# This class is the input for the 'start_metadata_generation_run' function.
class StartMetadataGenerationRunInput(BaseValidatorModel):
    domainIdentifier: str
    owningProjectIdentifier: str
    target: MetadataGenerationRunTarget
    type: Literal['BUSINESS_DESCRIPTIONS']
    clientToken: Optional[str] = None


# This class is the output for the 'get_time_series_data_point' function.
class GetTimeSeriesDataPointOutput(BaseValidatorModel):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    form: TimeSeriesDataPointFormOutput
    formName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'post_time_series_data_points' function.
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


class GrantedEntity(BaseValidatorModel):
    listing: Optional[ListingRevision] = None


# This class is the output for the 'search_group_profiles' function.
class SearchGroupProfilesOutput(BaseValidatorModel):
    items: List[GroupProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ProvisioningConfigurationOutput(BaseValidatorModel):
    lakeFormationConfiguration: Optional[LakeFormationConfigurationOutput] = None

LakeFormationConfigurationUnion = Union[LakeFormationConfiguration, LakeFormationConfigurationOutput]


# This class is the output for the 'list_lineage_node_history' function.
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


class ListConnectionsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    environmentIdentifier: Optional[str] = None
    name: Optional[str] = None
    sortBy: Optional[Literal['NAME']] = None
    sortOrder: Optional[SortOrderType] = None
    type: Optional[ConnectionTypeType] = None
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


class ListDataSourcesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    connectionIdentifier: Optional[str] = None
    environmentIdentifier: Optional[str] = None
    name: Optional[str] = None
    status: Optional[DataSourceStatusType] = None
    type: Optional[str] = None
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
    entityType: Literal['DOMAIN_UNIT']
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


class ListMetadataGenerationRunsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    status: Optional[MetadataGenerationRunStatusType] = None
    type: Optional[Literal['BUSINESS_DESCRIPTIONS']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    type: NotificationTypeType
    afterTimestamp: Optional[Timestamp] = None
    beforeTimestamp: Optional[Timestamp] = None
    subjects: Optional[List[str]] = None
    taskStatus: Optional[TaskStatusType] = None
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
    sortBy: Optional[Literal['NAME']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectProfilesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    name: Optional[str] = None
    sortBy: Optional[Literal['NAME']] = None
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
    targetType: Literal['DOMAIN_UNIT']
    action: Optional[Literal['CREATE_SUBSCRIPTION_REQUEST']] = None
    assetTypes: Optional[List[str]] = None
    dataProduct: Optional[bool] = None
    includeCascaded: Optional[bool] = None
    projectIds: Optional[List[str]] = None
    ruleType: Optional[Literal['METADATA_FORM_ENFORCEMENT']] = None
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


# This class is the output for the 'list_project_profiles' function.
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
    requiredMetadataForms: Optional[List[MetadataFormReference]] = None


class OpenLineageRunEventSummary(BaseValidatorModel):
    eventType: Optional[OpenLineageRunStateType] = None
    inputs: Optional[List[NameIdentifier]] = None
    job: Optional[NameIdentifier] = None
    outputs: Optional[List[NameIdentifier]] = None
    runId: Optional[str] = None


class RowFilterExpressionOutput(BaseValidatorModel):
    equalTo: Optional[EqualToExpression] = None
    greaterThan: Optional[GreaterThanExpression] = None
    greaterThanOrEqualTo: Optional[GreaterThanOrEqualToExpression] = None
    in_: Optional[InExpressionOutput] = None
    isNotNull: Optional[IsNotNullExpression] = None
    isNull: Optional[IsNullExpression] = None
    lessThan: Optional[LessThanExpression] = None
    lessThanOrEqualTo: Optional[LessThanOrEqualToExpression] = None
    like: Optional[LikeExpression] = None
    notEqualTo: Optional[NotEqualToExpression] = None
    notIn: Optional[NotInExpressionOutput] = None
    notLike: Optional[NotLikeExpression] = None


class RowFilterExpression(BaseValidatorModel):
    equalTo: Optional[EqualToExpression] = None
    greaterThan: Optional[GreaterThanExpression] = None
    greaterThanOrEqualTo: Optional[GreaterThanOrEqualToExpression] = None
    in_: Optional[InExpression] = None
    isNotNull: Optional[IsNotNullExpression] = None
    isNull: Optional[IsNullExpression] = None
    lessThan: Optional[LessThanExpression] = None
    lessThanOrEqualTo: Optional[LessThanOrEqualToExpression] = None
    like: Optional[LikeExpression] = None
    notEqualTo: Optional[NotEqualToExpression] = None
    notIn: Optional[NotInExpression] = None
    notLike: Optional[NotLikeExpression] = None


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
    tokenUrlParametersMap: Optional[Dict[str, str]] = None


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
    createProjectFromProjectProfile: Optional[CreateProjectFromProjectProfilePolicyGrantDetailOutput] = None
    delegateCreateEnvironmentProfile: Optional[Dict[str, Any]] = None
    overrideDomainUnitOwners: Optional[OverrideDomainUnitOwnersPolicyGrantDetail] = None
    overrideProjectOwners: Optional[OverrideProjectOwnersPolicyGrantDetail] = None


class PolicyGrantDetail(BaseValidatorModel):
    addToProjectMemberPool: Optional[AddToProjectMemberPoolPolicyGrantDetail] = None
    createAssetType: Optional[CreateAssetTypePolicyGrantDetail] = None
    createDomainUnit: Optional[CreateDomainUnitPolicyGrantDetail] = None
    createEnvironment: Optional[Dict[str, Any]] = None
    createEnvironmentFromBlueprint: Optional[Dict[str, Any]] = None
    createEnvironmentProfile: Optional[CreateEnvironmentProfilePolicyGrantDetail] = None
    createFormType: Optional[CreateFormTypePolicyGrantDetail] = None
    createGlossary: Optional[CreateGlossaryPolicyGrantDetail] = None
    createProject: Optional[CreateProjectPolicyGrantDetail] = None
    createProjectFromProjectProfile: Optional[CreateProjectFromProjectProfilePolicyGrantDetail] = None
    delegateCreateEnvironmentProfile: Optional[Dict[str, Any]] = None
    overrideDomainUnitOwners: Optional[OverrideDomainUnitOwnersPolicyGrantDetail] = None
    overrideProjectOwners: Optional[OverrideProjectOwnersPolicyGrantDetail] = None


class OwnerPropertiesOutput(BaseValidatorModel):
    group: Optional[OwnerGroupPropertiesOutput] = None
    user: Optional[OwnerUserPropertiesOutput] = None


class OwnerProperties(BaseValidatorModel):
    group: Optional[OwnerGroupProperties] = None
    user: Optional[OwnerUserProperties] = None

PhysicalConnectionRequirementsUnion = Union[PhysicalConnectionRequirements, PhysicalConnectionRequirementsOutput]


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


# This class is the input for the 'reject_predictions' function.
class RejectPredictionsInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    rejectChoices: Optional[List[RejectChoice]] = None
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


class SubscribedPrincipal(BaseValidatorModel):
    project: Optional[SubscribedProject] = None

TermRelationsUnion = Union[TermRelations, TermRelationsOutput]


# This class is the input for the 'create_environment_action' function.
class CreateEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    parameters: ActionParameters
    description: Optional[str] = None


# This class is the output for the 'create_environment_action' function.
class CreateEnvironmentActionOutput(BaseValidatorModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParameters
    ResponseMetadata: ResponseMetadata


class EnvironmentActionSummary(BaseValidatorModel):
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParameters
    description: Optional[str] = None


# This class is the output for the 'get_environment_action' function.
class GetEnvironmentActionOutput(BaseValidatorModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParameters
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_environment_action' function.
class UpdateEnvironmentActionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[ActionParameters] = None


# This class is the output for the 'update_environment_action' function.
class UpdateEnvironmentActionOutput(BaseValidatorModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParameters
    ResponseMetadata: ResponseMetadata


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
    connectionProperties: Optional[Dict[str, str]] = None
    description: Optional[str] = None


# This class is the input for the 'create_asset' function.
class CreateAssetInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    typeIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    externalIdentifier: Optional[str] = None
    formsInput: Optional[List[FormInput]] = None
    glossaryTerms: Optional[List[str]] = None
    predictionConfiguration: Optional[PredictionConfiguration] = None
    typeRevision: Optional[str] = None


# This class is the output for the 'create_asset' function.
class CreateAssetOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    externalIdentifier: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutput]
    glossaryTerms: List[str]
    id: str
    latestTimeSeriesDataPointFormsOutput: List[TimeSeriesDataPointSummaryFormOutput]
    listing: AssetListingDetails
    name: str
    owningProjectId: str
    predictionConfiguration: PredictionConfiguration
    readOnlyFormsOutput: List[FormOutput]
    revision: str
    typeIdentifier: str
    typeRevision: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_asset_revision' function.
class CreateAssetRevisionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[List[FormInput]] = None
    glossaryTerms: Optional[List[str]] = None
    predictionConfiguration: Optional[PredictionConfiguration] = None
    typeRevision: Optional[str] = None


# This class is the output for the 'create_asset_revision' function.
class CreateAssetRevisionOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    externalIdentifier: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutput]
    glossaryTerms: List[str]
    id: str
    latestTimeSeriesDataPointFormsOutput: List[TimeSeriesDataPointSummaryFormOutput]
    listing: AssetListingDetails
    name: str
    owningProjectId: str
    predictionConfiguration: PredictionConfiguration
    readOnlyFormsOutput: List[FormOutput]
    revision: str
    typeIdentifier: str
    typeRevision: str
    ResponseMetadata: ResponseMetadata


class EnvironmentBlueprintSummary(BaseValidatorModel):
    id: str
    name: str
    provider: str
    provisioningProperties: ProvisioningProperties
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    updatedAt: Optional[datetime] = None


# This class is the output for the 'get_environment_blueprint' function.
class GetEnvironmentBlueprintOutput(BaseValidatorModel):
    createdAt: datetime
    deploymentProperties: DeploymentProperties
    description: str
    glossaryTerms: List[str]
    id: str
    name: str
    provider: str
    provisioningProperties: ProvisioningProperties
    updatedAt: datetime
    userParameters: List[CustomParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_sources' function.
class ListDataSourcesOutput(BaseValidatorModel):
    items: List[DataSourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

EnvironmentConfigurationUserParameterUnion = Union[EnvironmentConfigurationUserParameter, EnvironmentConfigurationUserParameterOutput]


# This class is the output for the 'list_projects' function.
class ListProjectsOutput(BaseValidatorModel):
    items: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_subscription_targets' function.
class ListSubscriptionTargetsOutput(BaseValidatorModel):
    items: List[SubscriptionTargetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_data_product' function.
class CreateDataProductInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[List[FormInput]] = None
    glossaryTerms: Optional[List[str]] = None
    items: Optional[List[DataProductItemUnion]] = None


# This class is the input for the 'create_data_product_revision' function.
class CreateDataProductRevisionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[List[FormInput]] = None
    glossaryTerms: Optional[List[str]] = None
    items: Optional[List[DataProductItemUnion]] = None


# This class is the output for the 'list_data_source_run_activities' function.
class ListDataSourceRunActivitiesOutput(BaseValidatorModel):
    items: List[DataSourceRunActivity]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_data_source_runs' function.
class ListDataSourceRunsOutput(BaseValidatorModel):
    items: List[DataSourceRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_environment' function.
class CreateEnvironmentOutput(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    deploymentProperties: DeploymentProperties
    description: str
    domainId: str
    environmentActions: List[ConfigurableEnvironmentAction]
    environmentBlueprintId: str
    environmentProfileId: str
    glossaryTerms: List[str]
    id: str
    lastDeployment: Deployment
    name: str
    projectId: str
    provider: str
    provisionedResources: List[Resource]
    provisioningProperties: ProvisioningProperties
    status: EnvironmentStatusType
    updatedAt: datetime
    userParameters: List[CustomParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_environment' function.
class GetEnvironmentOutput(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    deploymentProperties: DeploymentProperties
    description: str
    domainId: str
    environmentActions: List[ConfigurableEnvironmentAction]
    environmentBlueprintId: str
    environmentProfileId: str
    glossaryTerms: List[str]
    id: str
    lastDeployment: Deployment
    name: str
    projectId: str
    provider: str
    provisionedResources: List[Resource]
    provisioningProperties: ProvisioningProperties
    status: EnvironmentStatusType
    updatedAt: datetime
    userParameters: List[CustomParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_environment' function.
class UpdateEnvironmentOutput(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    deploymentProperties: DeploymentProperties
    description: str
    domainId: str
    environmentActions: List[ConfigurableEnvironmentAction]
    environmentBlueprintId: str
    environmentProfileId: str
    glossaryTerms: List[str]
    id: str
    lastDeployment: Deployment
    name: str
    projectId: str
    provider: str
    provisionedResources: List[Resource]
    provisioningProperties: ProvisioningProperties
    status: EnvironmentStatusType
    updatedAt: datetime
    userParameters: List[CustomParameter]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_project' function.
class CreateProjectOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    domainUnitId: str
    environmentDeploymentDetails: EnvironmentDeploymentDetailsOutput
    failureReasons: List[ProjectDeletionError]
    glossaryTerms: List[str]
    id: str
    lastUpdatedAt: datetime
    name: str
    projectProfileId: str
    projectStatus: ProjectStatusType
    userParameters: List[EnvironmentConfigurationUserParameterOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_project' function.
class GetProjectOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    domainUnitId: str
    environmentDeploymentDetails: EnvironmentDeploymentDetailsOutput
    failureReasons: List[ProjectDeletionError]
    glossaryTerms: List[str]
    id: str
    lastUpdatedAt: datetime
    name: str
    projectProfileId: str
    projectStatus: ProjectStatusType
    userParameters: List[EnvironmentConfigurationUserParameterOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_project' function.
class UpdateProjectOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    domainUnitId: str
    environmentDeploymentDetails: EnvironmentDeploymentDetailsOutput
    failureReasons: List[ProjectDeletionError]
    glossaryTerms: List[str]
    id: str
    lastUpdatedAt: datetime
    name: str
    projectProfileId: str
    projectStatus: ProjectStatusType
    userParameters: List[EnvironmentConfigurationUserParameterOutput]
    ResponseMetadata: ResponseMetadata

EnvironmentDeploymentDetailsUnion = Union[EnvironmentDeploymentDetails, EnvironmentDeploymentDetailsOutput]


class ProjectPolicyGrantPrincipal(BaseValidatorModel):
    projectDesignation: ProjectDesignationType
    projectGrantFilter: Optional[ProjectGrantFilter] = None
    projectIdentifier: Optional[str] = None


# This class is the output for the 'create_domain_unit' function.
class CreateDomainUnitOutput(BaseValidatorModel):
    ancestorDomainUnitIds: List[str]
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    id: str
    name: str
    owners: List[DomainUnitOwnerProperties]
    parentDomainUnitId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain_unit' function.
class GetDomainUnitOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    id: str
    lastUpdatedAt: datetime
    lastUpdatedBy: str
    name: str
    owners: List[DomainUnitOwnerProperties]
    parentDomainUnitId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_unit' function.
class UpdateDomainUnitOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    id: str
    lastUpdatedAt: datetime
    lastUpdatedBy: str
    name: str
    owners: List[DomainUnitOwnerProperties]
    parentDomainUnitId: str
    ResponseMetadata: ResponseMetadata


class EnvironmentConfigurationOutput(BaseValidatorModel):
    awsAccount: AwsAccount
    awsRegion: Region
    environmentBlueprintId: str
    name: str
    configurationParameters: Optional[EnvironmentConfigurationParametersDetailsOutput] = None
    deploymentMode: Optional[DeploymentModeType] = None
    deploymentOrder: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None

EnvironmentConfigurationParametersDetailsUnion = Union[EnvironmentConfigurationParametersDetails, EnvironmentConfigurationParametersDetailsOutput]


class SearchInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[List[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClausePaginator] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[List[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchListingsInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[List[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClausePaginator] = None
    searchIn: Optional[List[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchTypesInputPaginate(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClausePaginator] = None
    searchIn: Optional[List[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search' function.
class SearchInput(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[List[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClause] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[List[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None


# This class is the input for the 'search_listings' function.
class SearchListingsInput(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[List[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClause] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[List[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None


# This class is the input for the 'search_types' function.
class SearchTypesInput(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClause] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[List[SearchInItem]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSort] = None


class GlueRunConfigurationOutput(BaseValidatorModel):
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutput]
    accountId: Optional[str] = None
    autoImportDataQualityResult: Optional[bool] = None
    catalogName: Optional[str] = None
    dataAccessRole: Optional[str] = None
    region: Optional[str] = None

RelationalFilterConfigurationUnion = Union[RelationalFilterConfiguration, RelationalFilterConfigurationOutput]


class SearchTypesResultItem(BaseValidatorModel):
    assetTypeItem: Optional[AssetTypeItem] = None
    formTypeItem: Optional[FormTypeData] = None
    lineageNodeTypeItem: Optional[LineageNodeTypeItem] = None


# This class is the output for the 'list_job_runs' function.
class ListJobRunsOutput(BaseValidatorModel):
    items: List[JobRunSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'post_time_series_data_points' function.
class PostTimeSeriesDataPointsInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    forms: List[TimeSeriesDataPointFormInput]
    clientToken: Optional[str] = None


# This class is the output for the 'list_metadata_generation_runs' function.
class ListMetadataGenerationRunsOutput(BaseValidatorModel):
    items: List[MetadataGenerationRunItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SelfGrantStatusOutput(BaseValidatorModel):
    glueSelfGrantStatus: Optional[GlueSelfGrantStatusOutput] = None
    redshiftSelfGrantStatus: Optional[RedshiftSelfGrantStatusOutput] = None


# This class is the input for the 'create_subscription_grant' function.
class CreateSubscriptionGrantInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    grantedEntity: GrantedEntityInput
    assetTargetNames: Optional[List[AssetTargetNameMap]] = None
    clientToken: Optional[str] = None
    subscriptionTargetIdentifier: Optional[str] = None


# This class is the output for the 'create_subscription_grant' function.
class CreateSubscriptionGrantOutput(BaseValidatorModel):
    assets: List[SubscribedAsset]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntity
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_subscription_grant' function.
class DeleteSubscriptionGrantOutput(BaseValidatorModel):
    assets: List[SubscribedAsset]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntity
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_subscription_grant' function.
class GetSubscriptionGrantOutput(BaseValidatorModel):
    assets: List[SubscribedAsset]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntity
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class SubscriptionGrantSummary(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntity
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionTargetId: str
    updatedAt: datetime
    assets: Optional[List[SubscribedAsset]] = None
    subscriptionId: Optional[str] = None
    updatedBy: Optional[str] = None


# This class is the output for the 'update_subscription_grant_status' function.
class UpdateSubscriptionGrantStatusOutput(BaseValidatorModel):
    assets: List[SubscribedAsset]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntity
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


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


# This class is the output for the 'get_environment_blueprint_configuration' function.
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


# This class is the output for the 'put_environment_blueprint_configuration' function.
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


class RowFilterOutput(BaseValidatorModel):
    and_: Optional[List[Dict[str, Any]]] = None
    expression: Optional[RowFilterExpressionOutput] = None
    or_: Optional[List[Dict[str, Any]]] = None


class RowFilter(BaseValidatorModel):
    and_: Optional[List[Dict[str, Any]]] = None
    expression: Optional[RowFilterExpression] = None
    or_: Optional[List[Dict[str, Any]]] = None


class NotificationOutput(BaseValidatorModel):
    actionLink: str
    creationTimestamp: datetime
    domainIdentifier: str
    identifier: str
    lastUpdatedTimestamp: datetime
    message: str
    title: str
    topic: Topic
    type: NotificationTypeType
    metadata: Optional[Dict[str, str]] = None
    status: Optional[TaskStatusType] = None


class AuthenticationConfiguration(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    oAuth2Properties: Optional[OAuth2PropertiesOutput] = None
    secretArn: Optional[str] = None

OAuth2PropertiesUnion = Union[OAuth2Properties, OAuth2PropertiesOutput]

PolicyGrantDetailUnion = Union[PolicyGrantDetail, PolicyGrantDetailOutput]


# This class is the output for the 'list_entity_owners' function.
class ListEntityOwnersOutput(BaseValidatorModel):
    owners: List[OwnerPropertiesOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AddEntityOwnerInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal['DOMAIN_UNIT']
    owner: OwnerProperties
    clientToken: Optional[str] = None


class RemoveEntityOwnerInput(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal['DOMAIN_UNIT']
    owner: OwnerProperties
    clientToken: Optional[str] = None


class RuleSummary(BaseValidatorModel):
    action: Optional[Literal['CREATE_SUBSCRIPTION_REQUEST']] = None
    identifier: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    name: Optional[str] = None
    revision: Optional[str] = None
    ruleType: Optional[Literal['METADATA_FORM_ENFORCEMENT']] = None
    scope: Optional[RuleScopeOutput] = None
    target: Optional[RuleTarget] = None
    targetType: Optional[Literal['DOMAIN_UNIT']] = None
    updatedAt: Optional[datetime] = None

RuleScopeUnion = Union[RuleScope, RuleScopeOutput]


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


# This class is the output for the 'create_user_profile' function.
class CreateUserProfileOutput(BaseValidatorModel):
    details: UserProfileDetails
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user_profile' function.
class GetUserProfileOutput(BaseValidatorModel):
    details: UserProfileDetails
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user_profile' function.
class UpdateUserProfileOutput(BaseValidatorModel):
    details: UserProfileDetails
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadata


class UserProfileSummary(BaseValidatorModel):
    details: Optional[UserProfileDetails] = None
    domainId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[UserProfileStatusType] = None
    type: Optional[UserProfileTypeType] = None


# This class is the input for the 'create_subscription_request' function.
class CreateSubscriptionRequestInput(BaseValidatorModel):
    domainIdentifier: str
    requestReason: str
    subscribedListings: List[SubscribedListingInput]
    subscribedPrincipals: List[SubscribedPrincipalInput]
    clientToken: Optional[str] = None
    metadataForms: Optional[List[FormInput]] = None


# This class is the input for the 'create_glossary_term' function.
class CreateGlossaryTermInput(BaseValidatorModel):
    domainIdentifier: str
    glossaryIdentifier: str
    name: str
    clientToken: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsUnion] = None


# This class is the input for the 'update_glossary_term' function.
class UpdateGlossaryTermInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    glossaryIdentifier: Optional[str] = None
    longDescription: Optional[str] = None
    name: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsUnion] = None


# This class is the output for the 'list_environment_actions' function.
class ListEnvironmentActionsOutput(BaseValidatorModel):
    items: List[EnvironmentActionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class SubscribedListing(BaseValidatorModel):
    description: str
    id: str
    item: SubscribedListingItem
    name: str
    ownerProjectId: str
    ownerProjectName: Optional[str] = None
    revision: Optional[str] = None


class GluePropertiesPatch(BaseValidatorModel):
    glueConnectionInput: Optional[GlueConnectionPatch] = None


# This class is the output for the 'list_environment_blueprints' function.
class ListEnvironmentBlueprintsOutput(BaseValidatorModel):
    items: List[EnvironmentBlueprintSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_project' function.
class CreateProjectInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    domainUnitId: Optional[str] = None
    glossaryTerms: Optional[List[str]] = None
    projectProfileId: Optional[str] = None
    userParameters: Optional[List[EnvironmentConfigurationUserParameterUnion]] = None


# This class is the input for the 'update_project' function.
class UpdateProjectInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    environmentDeploymentDetails: Optional[EnvironmentDeploymentDetailsUnion] = None
    glossaryTerms: Optional[List[str]] = None
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


# This class is the output for the 'create_project_profile' function.
class CreateProjectProfileOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    domainUnitId: str
    environmentConfigurations: List[EnvironmentConfigurationOutput]
    id: str
    lastUpdatedAt: datetime
    name: str
    status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_project_profile' function.
class GetProjectProfileOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    domainUnitId: str
    environmentConfigurations: List[EnvironmentConfigurationOutput]
    id: str
    lastUpdatedAt: datetime
    name: str
    status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_project_profile' function.
class UpdateProjectProfileOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    domainUnitId: str
    environmentConfigurations: List[EnvironmentConfigurationOutput]
    id: str
    lastUpdatedAt: datetime
    name: str
    status: StatusType
    ResponseMetadata: ResponseMetadata


class EnvironmentConfiguration(BaseValidatorModel):
    awsAccount: AwsAccount
    awsRegion: Region
    environmentBlueprintId: str
    name: str
    configurationParameters: Optional[EnvironmentConfigurationParametersDetailsUnion] = None
    deploymentMode: Optional[DeploymentModeType] = None
    deploymentOrder: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None


class GlueRunConfigurationInput(BaseValidatorModel):
    relationalFilterConfigurations: List[RelationalFilterConfigurationUnion]
    autoImportDataQualityResult: Optional[bool] = None
    catalogName: Optional[str] = None
    dataAccessRole: Optional[str] = None


class RedshiftRunConfigurationInput(BaseValidatorModel):
    relationalFilterConfigurations: List[RelationalFilterConfigurationUnion]
    dataAccessRole: Optional[str] = None
    redshiftCredentialConfiguration: Optional[RedshiftCredentialConfiguration] = None
    redshiftStorage: Optional[RedshiftStorage] = None


# This class is the output for the 'search_types' function.
class SearchTypesOutput(BaseValidatorModel):
    items: List[SearchTypesResultItem]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_subscription_grants' function.
class ListSubscriptionGrantsOutput(BaseValidatorModel):
    items: List[SubscriptionGrantSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_environment_blueprint_configurations' function.
class ListEnvironmentBlueprintConfigurationsOutput(BaseValidatorModel):
    items: List[EnvironmentBlueprintConfigurationItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ProvisioningConfigurationUnion = Union[ProvisioningConfiguration, ProvisioningConfigurationOutput]


# This class is the output for the 'get_job_run' function.
class GetJobRunOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    details: JobRunDetails
    domainId: str
    endTime: datetime
    error: JobRunError
    id: str
    jobId: str
    jobType: Literal['LINEAGE']
    runMode: JobRunModeType
    startTime: datetime
    status: JobRunStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_project_memberships' function.
class ListProjectMembershipsOutput(BaseValidatorModel):
    members: List[ProjectMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_rule' function.
class CreateRuleOutput(BaseValidatorModel):
    action: Literal['CREATE_SUBSCRIPTION_REQUEST']
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutput
    identifier: str
    name: str
    ruleType: Literal['METADATA_FORM_ENFORCEMENT']
    scope: RuleScopeOutput
    target: RuleTarget
    targetType: Literal['DOMAIN_UNIT']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rule' function.
class GetRuleOutput(BaseValidatorModel):
    action: Literal['CREATE_SUBSCRIPTION_REQUEST']
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutput
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal['METADATA_FORM_ENFORCEMENT']
    scope: RuleScopeOutput
    target: RuleTarget
    targetType: Literal['DOMAIN_UNIT']
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_rule' function.
class UpdateRuleOutput(BaseValidatorModel):
    action: Literal['CREATE_SUBSCRIPTION_REQUEST']
    createdAt: datetime
    createdBy: str
    description: str
    detail: RuleDetailOutput
    identifier: str
    lastUpdatedBy: str
    name: str
    revision: str
    ruleType: Literal['METADATA_FORM_ENFORCEMENT']
    scope: RuleScopeOutput
    target: RuleTarget
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata

RuleDetailUnion = Union[RuleDetail, RuleDetailOutput]


class LineageEventSummary(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    domainId: Optional[str] = None
    eventSummary: Optional[EventSummary] = None
    eventTime: Optional[datetime] = None
    id: Optional[str] = None
    processingStatus: Optional[LineageEventProcessingStatusType] = None


class RowFilterConfigurationOutput(BaseValidatorModel):
    rowFilter: RowFilterOutput
    sensitive: Optional[bool] = None


class RowFilterConfiguration(BaseValidatorModel):
    rowFilter: RowFilter
    sensitive: Optional[bool] = None


# This class is the output for the 'list_notifications' function.
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


class AuthenticationConfigurationInput(BaseValidatorModel):
    authenticationType: Optional[AuthenticationTypeType] = None
    basicAuthenticationCredentials: Optional[BasicAuthenticationCredentials] = None
    customAuthenticationCredentials: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    oAuth2Properties: Optional[OAuth2PropertiesUnion] = None
    secretArn: Optional[str] = None


# This class is the output for the 'list_rules' function.
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


# This class is the output for the 'search_user_profiles' function.
class SearchUserProfilesOutput(BaseValidatorModel):
    items: List[UserProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'search' function.
class SearchOutput(BaseValidatorModel):
    items: List[SearchInventoryResultItem]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'search_listings' function.
class SearchListingsOutput(BaseValidatorModel):
    items: List[SearchResultItem]
    totalMatchCount: int
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_listing' function.
class GetListingOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    id: str
    item: ListingItem
    listingRevision: str
    name: str
    status: ListingStatusType
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_subscription_request' function.
class AcceptSubscriptionRequestOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    existingSubscriptionId: str
    id: str
    metadataForms: List[FormOutput]
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListing]
    subscribedPrincipals: List[SubscribedPrincipal]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_subscription' function.
class CancelSubscriptionOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    retainPermissions: bool
    status: SubscriptionStatusType
    subscribedListing: SubscribedListing
    subscribedPrincipal: SubscribedPrincipal
    subscriptionRequestId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_subscription_request' function.
class CreateSubscriptionRequestOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    existingSubscriptionId: str
    id: str
    metadataForms: List[FormOutput]
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListing]
    subscribedPrincipals: List[SubscribedPrincipal]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_subscription' function.
class GetSubscriptionOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    retainPermissions: bool
    status: SubscriptionStatusType
    subscribedListing: SubscribedListing
    subscribedPrincipal: SubscribedPrincipal
    subscriptionRequestId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_subscription_request_details' function.
class GetSubscriptionRequestDetailsOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    existingSubscriptionId: str
    id: str
    metadataForms: List[FormOutput]
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListing]
    subscribedPrincipals: List[SubscribedPrincipal]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_subscription_request' function.
class RejectSubscriptionRequestOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    existingSubscriptionId: str
    id: str
    metadataForms: List[FormOutput]
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListing]
    subscribedPrincipals: List[SubscribedPrincipal]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_subscription' function.
class RevokeSubscriptionOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    retainPermissions: bool
    status: SubscriptionStatusType
    subscribedListing: SubscribedListing
    subscribedPrincipal: SubscribedPrincipal
    subscriptionRequestId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


class SubscriptionRequestSummary(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    requestReason: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListing]
    subscribedPrincipals: List[SubscribedPrincipal]
    updatedAt: datetime
    decisionComment: Optional[str] = None
    existingSubscriptionId: Optional[str] = None
    metadataFormsSummary: Optional[List[MetadataFormSummary]] = None
    reviewerId: Optional[str] = None
    updatedBy: Optional[str] = None


class SubscriptionSummary(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    status: SubscriptionStatusType
    subscribedListing: SubscribedListing
    subscribedPrincipal: SubscribedPrincipal
    updatedAt: datetime
    retainPermissions: Optional[bool] = None
    subscriptionRequestId: Optional[str] = None
    updatedBy: Optional[str] = None


# This class is the output for the 'update_subscription_request' function.
class UpdateSubscriptionRequestOutput(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    existingSubscriptionId: str
    id: str
    metadataForms: List[FormOutput]
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListing]
    subscribedPrincipals: List[SubscribedPrincipal]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadata


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

PolicyGrantPrincipalUnion = Union[PolicyGrantPrincipal, PolicyGrantPrincipalOutput]

EnvironmentConfigurationUnion = Union[EnvironmentConfiguration, EnvironmentConfigurationOutput]


class DataSourceConfigurationInput(BaseValidatorModel):
    glueRunConfiguration: Optional[GlueRunConfigurationInput] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationInput] = None
    sageMakerRunConfiguration: Optional[SageMakerRunConfigurationInput] = None


# This class is the input for the 'put_environment_blueprint_configuration' function.
class PutEnvironmentBlueprintConfigurationInput(BaseValidatorModel):
    domainIdentifier: str
    enabledRegions: List[str]
    environmentBlueprintIdentifier: str
    environmentRolePermissionBoundary: Optional[str] = None
    manageAccessRoleArn: Optional[str] = None
    provisioningConfigurations: Optional[List[ProvisioningConfigurationUnion]] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Dict[str, Dict[str, str]]] = None


# This class is the input for the 'create_rule' function.
class CreateRuleInput(BaseValidatorModel):
    action: Literal['CREATE_SUBSCRIPTION_REQUEST']
    detail: RuleDetailUnion
    domainIdentifier: str
    name: str
    scope: RuleScopeUnion
    target: RuleTarget
    clientToken: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'update_rule' function.
class UpdateRuleInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    detail: Optional[RuleDetailUnion] = None
    includeChildDomainUnits: Optional[bool] = None
    name: Optional[str] = None
    scope: Optional[RuleScopeUnion] = None


# This class is the output for the 'list_lineage_events' function.
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


class GlueConnectionInput(BaseValidatorModel):
    athenaProperties: Optional[Dict[str, str]] = None
    authenticationConfiguration: Optional[AuthenticationConfigurationInput] = None
    connectionProperties: Optional[Dict[str, str]] = None
    connectionType: Optional[GlueConnectionTypeType] = None
    description: Optional[str] = None
    matchCriteria: Optional[str] = None
    name: Optional[str] = None
    physicalConnectionRequirements: Optional[PhysicalConnectionRequirementsUnion] = None
    pythonProperties: Optional[Dict[str, str]] = None
    sparkProperties: Optional[Dict[str, str]] = None
    validateCredentials: Optional[bool] = None
    validateForComputeEnvironments: Optional[List[ComputeEnvironmentsType]] = None


# This class is the output for the 'create_data_source' function.
class CreateDataSourceOutput(BaseValidatorModel):
    assetFormsOutput: List[FormOutput]
    configuration: DataSourceConfigurationOutput
    connectionId: str
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessage
    id: str
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessage
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    recommendation: RecommendationConfiguration
    schedule: ScheduleConfiguration
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_data_source' function.
class DeleteDataSourceOutput(BaseValidatorModel):
    assetFormsOutput: List[FormOutput]
    configuration: DataSourceConfigurationOutput
    connectionId: str
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessage
    id: str
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessage
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    retainPermissionsOnRevokeFailure: bool
    schedule: ScheduleConfiguration
    selfGrantStatus: SelfGrantStatusOutput
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_source' function.
class GetDataSourceOutput(BaseValidatorModel):
    assetFormsOutput: List[FormOutput]
    configuration: DataSourceConfigurationOutput
    connectionId: str
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessage
    id: str
    lastRunAssetCount: int
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessage
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    recommendation: RecommendationConfiguration
    schedule: ScheduleConfiguration
    selfGrantStatus: SelfGrantStatusOutput
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_data_source' function.
class UpdateDataSourceOutput(BaseValidatorModel):
    assetFormsOutput: List[FormOutput]
    configuration: DataSourceConfigurationOutput
    connectionId: str
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessage
    id: str
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessage
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    recommendation: RecommendationConfiguration
    retainPermissionsOnRevokeFailure: bool
    schedule: ScheduleConfiguration
    selfGrantStatus: SelfGrantStatusOutput
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_subscription_requests' function.
class ListSubscriptionRequestsOutput(BaseValidatorModel):
    items: List[SubscriptionRequestSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_subscriptions' function.
class ListSubscriptionsOutput(BaseValidatorModel):
    items: List[SubscriptionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'update_connection' function.
class UpdateConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    awsLocation: Optional[AwsLocation] = None
    description: Optional[str] = None
    props: Optional[ConnectionPropertiesPatch] = None


# This class is the output for the 'list_policy_grants' function.
class ListPolicyGrantsOutput(BaseValidatorModel):
    grantList: List[PolicyGrantMember]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


# This class is the input for the 'create_project_profile' function.
class CreateProjectProfileInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    domainUnitIdentifier: Optional[str] = None
    environmentConfigurations: Optional[List[EnvironmentConfigurationUnion]] = None
    status: Optional[StatusType] = None


# This class is the input for the 'update_project_profile' function.
class UpdateProjectProfileInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    domainUnitIdentifier: Optional[str] = None
    environmentConfigurations: Optional[List[EnvironmentConfigurationUnion]] = None
    name: Optional[str] = None
    status: Optional[StatusType] = None


# This class is the input for the 'create_data_source' function.
class CreateDataSourceInput(BaseValidatorModel):
    domainIdentifier: str
    name: str
    projectIdentifier: str
    type: str
    assetFormsInput: Optional[List[FormInput]] = None
    clientToken: Optional[str] = None
    configuration: Optional[DataSourceConfigurationInput] = None
    connectionIdentifier: Optional[str] = None
    description: Optional[str] = None
    enableSetting: Optional[EnableSettingType] = None
    environmentIdentifier: Optional[str] = None
    publishOnImport: Optional[bool] = None
    recommendation: Optional[RecommendationConfiguration] = None
    schedule: Optional[ScheduleConfiguration] = None


# This class is the input for the 'update_data_source' function.
class UpdateDataSourceInput(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    assetFormsInput: Optional[List[FormInput]] = None
    configuration: Optional[DataSourceConfigurationInput] = None
    description: Optional[str] = None
    enableSetting: Optional[EnableSettingType] = None
    name: Optional[str] = None
    publishOnImport: Optional[bool] = None
    recommendation: Optional[RecommendationConfiguration] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None
    schedule: Optional[ScheduleConfiguration] = None


# This class is the output for the 'create_asset_filter' function.
class CreateAssetFilterOutput(BaseValidatorModel):
    assetId: str
    configuration: AssetFilterConfigurationOutput
    createdAt: datetime
    description: str
    domainId: str
    effectiveColumnNames: List[str]
    effectiveRowFilter: str
    errorMessage: str
    id: str
    name: str
    status: FilterStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_asset_filter' function.
class GetAssetFilterOutput(BaseValidatorModel):
    assetId: str
    configuration: AssetFilterConfigurationOutput
    createdAt: datetime
    description: str
    domainId: str
    effectiveColumnNames: List[str]
    effectiveRowFilter: str
    errorMessage: str
    id: str
    name: str
    status: FilterStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_asset_filter' function.
class UpdateAssetFilterOutput(BaseValidatorModel):
    assetId: str
    configuration: AssetFilterConfigurationOutput
    createdAt: datetime
    description: str
    domainId: str
    effectiveColumnNames: List[str]
    effectiveRowFilter: str
    errorMessage: str
    id: str
    name: str
    status: FilterStatusType
    ResponseMetadata: ResponseMetadata

AssetFilterConfigurationUnion = Union[AssetFilterConfiguration, AssetFilterConfigurationOutput]


class ConnectionSummary(BaseValidatorModel):
    connectionId: str
    domainId: str
    domainUnitId: str
    name: str
    physicalEndpoints: List[PhysicalEndpoint]
    type: ConnectionTypeType
    environmentId: Optional[str] = None
    projectId: Optional[str] = None
    props: Optional[ConnectionPropertiesOutput] = None


# This class is the output for the 'create_connection' function.
class CreateConnectionOutput(BaseValidatorModel):
    connectionId: str
    description: str
    domainId: str
    domainUnitId: str
    environmentId: str
    name: str
    physicalEndpoints: List[PhysicalEndpoint]
    projectId: str
    props: ConnectionPropertiesOutput
    type: ConnectionTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_connection' function.
class GetConnectionOutput(BaseValidatorModel):
    connectionCredentials: ConnectionCredentials
    connectionId: str
    description: str
    domainId: str
    domainUnitId: str
    environmentId: str
    environmentUserRole: str
    name: str
    physicalEndpoints: List[PhysicalEndpoint]
    projectId: str
    props: ConnectionPropertiesOutput
    type: ConnectionTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_connection' function.
class UpdateConnectionOutput(BaseValidatorModel):
    connectionId: str
    description: str
    domainId: str
    domainUnitId: str
    environmentId: str
    name: str
    physicalEndpoints: List[PhysicalEndpoint]
    projectId: str
    props: ConnectionPropertiesOutput
    type: ConnectionTypeType
    ResponseMetadata: ResponseMetadata


class GluePropertiesInput(BaseValidatorModel):
    glueConnectionInput: Optional[GlueConnectionInput] = None


# This class is the input for the 'create_asset_filter' function.
class CreateAssetFilterInput(BaseValidatorModel):
    assetIdentifier: str
    configuration: AssetFilterConfigurationUnion
    domainIdentifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'update_asset_filter' function.
class UpdateAssetFilterInput(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    configuration: Optional[AssetFilterConfigurationUnion] = None
    description: Optional[str] = None
    name: Optional[str] = None


# This class is the output for the 'list_connections' function.
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


# This class is the input for the 'create_connection' function.
class CreateConnectionInput(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    awsLocation: Optional[AwsLocation] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    props: Optional[ConnectionPropertiesInput] = None