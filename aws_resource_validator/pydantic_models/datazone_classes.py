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

class AcceptSubscriptionRequestInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    decisionComment: Optional[str] = None

class AwsConsoleLinkParametersTypeDef(BaseValidatorModel):
    uri: Optional[str] = None

class FormOutputTypeDef(BaseValidatorModel):
    formName: str
    content: Optional[str] = None
    typeName: Optional[str] = None
    typeRevision: Optional[str] = None

class TimeSeriesDataPointSummaryFormOutputTypeDef(BaseValidatorModel):
    formName: str
    timestamp: datetime
    typeIdentifier: str
    contentSummary: Optional[str] = None
    id: Optional[str] = None
    typeRevision: Optional[str] = None

class AssetListingDetailsTypeDef(BaseValidatorModel):
    listingId: str
    listingStatus: ListingStatusType

class DetailedGlossaryTermTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    shortDescription: Optional[str] = None

class AssetRevisionTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    domainId: Optional[str] = None
    id: Optional[str] = None
    revision: Optional[str] = None

class AssetTargetNameMapTypeDef(BaseValidatorModel):
    assetId: str
    targetName: str

class FormEntryOutputTypeDef(BaseValidatorModel):
    typeName: str
    typeRevision: str
    required: Optional[bool] = None

class AssociateEnvironmentRoleInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str

class BusinessNameGenerationConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None

class CancelMetadataGenerationRunInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class CancelSubscriptionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class CloudFormationPropertiesTypeDef(BaseValidatorModel):
    templateUrl: str

class ConfigurableActionParameterTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class FormInputTypeDef(BaseValidatorModel):
    formName: str
    content: Optional[str] = None
    typeIdentifier: Optional[str] = None
    typeRevision: Optional[str] = None

class FormEntryInputTypeDef(BaseValidatorModel):
    typeIdentifier: str
    typeRevision: str
    required: Optional[bool] = None

class RecommendationConfigurationTypeDef(BaseValidatorModel):
    enableBusinessNameGeneration: Optional[bool] = None

class ScheduleConfigurationTypeDef(BaseValidatorModel):
    schedule: Optional[str] = None
    timezone: Optional[TimezoneType] = None

class DataSourceErrorMessageTypeDef(BaseValidatorModel):
    errorType: DataSourceErrorTypeType
    errorDetail: Optional[str] = None

class SingleSignOnTypeDef(BaseValidatorModel):
    type: Optional[AuthTypeType] = None
    userAssignment: Optional[UserAssignmentType] = None

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

class ResourceTypeDef(BaseValidatorModel):
    type: str
    value: str
    name: Optional[str] = None
    provider: Optional[str] = None

class ModelTypeDef(BaseValidatorModel):
    smithy: Optional[str] = None

class CreateGlossaryInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    status: Optional[GlossaryStatusType] = None

class TermRelationsTypeDef(BaseValidatorModel):
    classifies: Optional[Sequence[str]] = None
    isA: Optional[Sequence[str]] = None

class TermRelationsOutputTypeDef(BaseValidatorModel):
    classifies: Optional[List[str]] = None
    isA: Optional[List[str]] = None

class CreateGroupProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    clientToken: Optional[str] = None

class CreateListingChangeSetInputRequestTypeDef(BaseValidatorModel):
    action: ChangeActionType
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["ASSET"]
    clientToken: Optional[str] = None
    entityRevision: Optional[str] = None

class CreateProjectInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None

class MemberTypeDef(BaseValidatorModel):
    groupIdentifier: Optional[str] = None
    userIdentifier: Optional[str] = None

class ProjectDeletionErrorTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None

class SubscribedListingInputTypeDef(BaseValidatorModel):
    identifier: str

class SubscriptionTargetFormTypeDef(BaseValidatorModel):
    content: str
    formName: str

class CreateUserProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    userIdentifier: str
    clientToken: Optional[str] = None
    userType: Optional[UserTypeType] = None

class DataProductItemTypeDef(BaseValidatorModel):
    domainId: Optional[str] = None
    itemId: Optional[str] = None

class RunStatisticsForAssetsTypeDef(BaseValidatorModel):
    added: Optional[int] = None
    failed: Optional[int] = None
    skipped: Optional[int] = None
    unchanged: Optional[int] = None
    updated: Optional[int] = None

class DeleteAssetInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteAssetTypeInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteDataSourceInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None

class DeleteDomainInputRequestTypeDef(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    skipDeletionCheck: Optional[bool] = None

class DeleteEnvironmentActionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str

class DeleteEnvironmentInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteEnvironmentProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteFormTypeInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    formTypeIdentifier: str

class DeleteGlossaryInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteGlossaryTermInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteListingInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteProjectInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    skipDeletionCheck: Optional[bool] = None

class DeleteSubscriptionGrantInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteSubscriptionRequestInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class DeleteSubscriptionTargetInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class DeleteTimeSeriesDataPointsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    clientToken: Optional[str] = None

class EnvironmentErrorTypeDef(BaseValidatorModel):
    message: str
    code: Optional[str] = None

class DisassociateEnvironmentRoleInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str

class DomainSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    managedAccountId: str
    name: str
    status: DomainStatusType
    description: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    portalUrl: Optional[str] = None

class EnvironmentBlueprintConfigurationItemTypeDef(BaseValidatorModel):
    domainId: str
    environmentBlueprintId: str
    createdAt: Optional[datetime] = None
    enabledRegions: Optional[List[str]] = None
    manageAccessRoleArn: Optional[str] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Dict[str, Dict[str, str]]] = None
    updatedAt: Optional[datetime] = None

class EnvironmentProfileSummaryTypeDef(BaseValidatorModel):
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

class EnvironmentSummaryTypeDef(BaseValidatorModel):
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

class FailureCauseTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    attribute: str
    value: str

class FilterExpressionTypeDef(BaseValidatorModel):
    expression: str
    type: FilterExpressionTypeType

class ImportTypeDef(BaseValidatorModel):
    name: str
    revision: str

class GetAssetInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None

class GetAssetTypeInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None

class GetDataSourceInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetDataSourceRunInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetDomainInputRequestTypeDef(BaseValidatorModel):
    identifier: str

class GetEnvironmentActionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class GetEnvironmentBlueprintConfigurationInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str

class GetEnvironmentBlueprintInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetEnvironmentInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetEnvironmentProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetFormTypeInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    formTypeIdentifier: str
    revision: Optional[str] = None

class GetGlossaryInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetGlossaryTermInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetGroupProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str

class GetIamPortalLoginUrlInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str

class LineageNodeReferenceTypeDef(BaseValidatorModel):
    eventTimestamp: Optional[datetime] = None
    id: Optional[str] = None

class GetListingInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    listingRevision: Optional[str] = None

class GetMetadataGenerationRunInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class MetadataGenerationRunTargetTypeDef(BaseValidatorModel):
    identifier: str
    type: Literal["ASSET"]
    revision: Optional[str] = None

class GetProjectInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionGrantInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionRequestDetailsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionTargetInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class GetTimeSeriesDataPointInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    identifier: str

class TimeSeriesDataPointFormOutputTypeDef(BaseValidatorModel):
    formName: str
    timestamp: datetime
    typeIdentifier: str
    content: Optional[str] = None
    id: Optional[str] = None
    typeRevision: Optional[str] = None

class GetUserProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    userIdentifier: str
    type: Optional[UserProfileTypeType] = None

class GlossaryItemTypeDef(BaseValidatorModel):
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

class SelfGrantStatusDetailTypeDef(BaseValidatorModel):
    databaseName: str
    status: SelfGrantStatusType
    failureCause: Optional[str] = None
    schemaName: Optional[str] = None

class ListingRevisionInputTypeDef(BaseValidatorModel):
    identifier: str
    revision: str

class ListingRevisionTypeDef(BaseValidatorModel):
    id: str
    revision: str

class GroupDetailsTypeDef(BaseValidatorModel):
    groupId: str

class GroupProfileSummaryTypeDef(BaseValidatorModel):
    domainId: Optional[str] = None
    groupName: Optional[str] = None
    id: Optional[str] = None
    status: Optional[GroupProfileStatusType] = None

class IamUserProfileDetailsTypeDef(BaseValidatorModel):
    arn: Optional[str] = None

class LineageNodeSummaryTypeDef(BaseValidatorModel):
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

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssetRevisionsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataSourceRunActivitiesInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataAssetActivityStatusType] = None

class ListDataSourceRunsInputRequestTypeDef(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceRunStatusType] = None

class ListDataSourcesInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    environmentIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceStatusType] = None
    type: Optional[str] = None

class ListDomainsInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DomainStatusType] = None

class ListEnvironmentActionsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentBlueprintConfigurationsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentBlueprintsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListEnvironmentProfilesInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    projectIdentifier: Optional[str] = None

class ListEnvironmentsInputRequestTypeDef(BaseValidatorModel):
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

class ListMetadataGenerationRunsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[MetadataGenerationRunStatusType] = None
    type: Optional[Literal["BUSINESS_DESCRIPTIONS"]] = None

class ListProjectMembershipsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListProjectsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    userIdentifier: Optional[str] = None

class ListSubscriptionGrantsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    subscribedListingId: Optional[str] = None
    subscriptionId: Optional[str] = None
    subscriptionTargetId: Optional[str] = None

class ListSubscriptionRequestsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None

class ListSubscriptionTargetsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None

class ListSubscriptionsInputRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class UserDetailsTypeDef(BaseValidatorModel):
    userId: str

class NotificationResourceTypeDef(BaseValidatorModel):
    id: str
    type: Literal["PROJECT"]
    name: Optional[str] = None

class PutEnvironmentBlueprintConfigurationInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    enabledRegions: Sequence[str]
    environmentBlueprintIdentifier: str
    manageAccessRoleArn: Optional[str] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Mapping[str, Mapping[str, str]]] = None

class RedshiftClusterStorageTypeDef(BaseValidatorModel):
    clusterName: str

class RedshiftCredentialConfigurationTypeDef(BaseValidatorModel):
    secretManagerArn: str

class RedshiftServerlessStorageTypeDef(BaseValidatorModel):
    workgroupName: str

class RejectChoiceTypeDef(BaseValidatorModel):
    predictionTarget: str
    predictionChoices: Optional[Sequence[int]] = None

class RejectRuleTypeDef(BaseValidatorModel):
    rule: Optional[RejectRuleBehaviorType] = None
    threshold: Optional[float] = None

class RejectSubscriptionRequestInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    decisionComment: Optional[str] = None

class RevokeSubscriptionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    retainPermissions: Optional[bool] = None

class SearchGroupProfilesInputRequestTypeDef(BaseValidatorModel):
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

class SearchUserProfilesInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchText: Optional[str] = None

class SsoUserProfileDetailsTypeDef(BaseValidatorModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    username: Optional[str] = None

class StartDataSourceRunInputRequestTypeDef(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    clientToken: Optional[str] = None

class SubscribedProjectInputTypeDef(BaseValidatorModel):
    identifier: Optional[str] = None

class SubscribedProjectTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TermRelationsExtraOutputTypeDef(BaseValidatorModel):
    classifies: Optional[List[str]] = None
    isA: Optional[List[str]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEnvironmentInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None

class UpdateGlossaryInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[GlossaryStatusType] = None

class UpdateGroupProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: str
    status: GroupProfileStatusType

class UpdateProjectInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None

class UpdateSubscriptionRequestInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    requestReason: str

class UpdateUserProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    status: UserProfileStatusType
    userIdentifier: str
    type: Optional[UserProfileTypeType] = None

class AcceptPredictionsInputRequestTypeDef(BaseValidatorModel):
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

class CreateGlossaryOutputTypeDef(BaseValidatorModel):
    description: str
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupProfileOutputTypeDef(BaseValidatorModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateListingChangeSetOutputTypeDef(BaseValidatorModel):
    listingId: str
    listingRevision: str
    status: ListingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainOutputTypeDef(BaseValidatorModel):
    status: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentBlueprintConfigurationOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    manageAccessRoleArn: str
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlossaryOutputTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupProfileOutputTypeDef(BaseValidatorModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetIamPortalLoginUrlOutputTypeDef(BaseValidatorModel):
    authCodeUrl: str
    userProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutEnvironmentBlueprintConfigurationOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    manageAccessRoleArn: str
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RejectPredictionsOutputTypeDef(BaseValidatorModel):
    assetId: str
    assetRevision: str
    domainId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataGenerationRunOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    owningProjectId: str
    status: MetadataGenerationRunStatusType
    type: Literal["BUSINESS_DESCRIPTIONS"]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlossaryOutputTypeDef(BaseValidatorModel):
    description: str
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupProfileOutputTypeDef(BaseValidatorModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ActionParametersTypeDef(BaseValidatorModel):
    awsConsoleLink: Optional[AwsConsoleLinkParametersTypeDef] = None

class AssetItemAdditionalAttributesTypeDef(BaseValidatorModel):
    formsOutput: Optional[List[FormOutputTypeDef]] = None
    latestTimeSeriesDataPointFormsOutput: Optional[       List[TimeSeriesDataPointSummaryFormOutputTypeDef]     ] = None
    readOnlyFormsOutput: Optional[List[FormOutputTypeDef]] = None

class AssetListingItemAdditionalAttributesTypeDef(BaseValidatorModel):
    forms: Optional[str] = None
    latestTimeSeriesDataPointForms: Optional[       List[TimeSeriesDataPointSummaryFormOutputTypeDef]     ] = None

class ListTimeSeriesDataPointsOutputTypeDef(BaseValidatorModel):
    items: List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssetOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    externalIdentifier: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutputTypeDef]
    glossaryTerms: List[str]
    id: str
    latestTimeSeriesDataPointFormsOutput: List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    listing: AssetListingDetailsTypeDef
    name: str
    owningProjectId: str
    readOnlyFormsOutput: List[FormOutputTypeDef]
    revision: str
    typeIdentifier: str
    typeRevision: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetListingTypeDef(BaseValidatorModel):
    assetId: Optional[str] = None
    assetRevision: Optional[str] = None
    assetType: Optional[str] = None
    createdAt: Optional[datetime] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    latestTimeSeriesDataPointForms: Optional[       List[TimeSeriesDataPointSummaryFormOutputTypeDef]     ] = None
    owningProjectId: Optional[str] = None

class SubscribedAssetListingTypeDef(BaseValidatorModel):
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None

class ListAssetRevisionsOutputTypeDef(BaseValidatorModel):
    items: List[AssetRevisionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class PostLineageEventInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    event: BlobTypeDef
    clientToken: Optional[str] = None

class PredictionConfigurationTypeDef(BaseValidatorModel):
    businessNameGeneration: Optional[BusinessNameGenerationConfigurationTypeDef] = None

class ProvisioningPropertiesTypeDef(BaseValidatorModel):
    cloudFormation: Optional[CloudFormationPropertiesTypeDef] = None

class ConfigurableEnvironmentActionTypeDef(BaseValidatorModel):
    parameters: List[ConfigurableActionParameterTypeDef]
    type: str
    auth: Optional[ConfigurableActionTypeAuthorizationType] = None

class CreateAssetTypeInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    formsInput: Mapping[str, FormEntryInputTypeDef]
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None

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
    technicalDescription: Optional[str] = None

class DataSourceSummaryTypeDef(BaseValidatorModel):
    dataSourceId: str
    domainId: str
    environmentId: str
    name: str
    status: DataSourceStatusType
    type: str
    createdAt: Optional[datetime] = None
    enableSetting: Optional[EnableSettingType] = None
    lastRunAssetCount: Optional[int] = None
    lastRunAt: Optional[datetime] = None
    lastRunErrorMessage: Optional[DataSourceErrorMessageTypeDef] = None
    lastRunStatus: Optional[DataSourceRunStatusType] = None
    schedule: Optional[ScheduleConfigurationTypeDef] = None
    updatedAt: Optional[datetime] = None

class CreateDomainInputRequestTypeDef(BaseValidatorModel):
    domainExecutionRole: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyIdentifier: Optional[str] = None
    singleSignOn: Optional[SingleSignOnTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDomainOutputTypeDef(BaseValidatorModel):
    arn: str
    description: str
    domainExecutionRole: str
    id: str
    kmsKeyIdentifier: str
    name: str
    portalUrl: str
    singleSignOn: SingleSignOnTypeDef
    status: DomainStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainOutputTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    description: str
    domainExecutionRole: str
    id: str
    kmsKeyIdentifier: str
    lastUpdatedAt: datetime
    name: str
    portalUrl: str
    singleSignOn: SingleSignOnTypeDef
    status: DomainStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainInputRequestTypeDef(BaseValidatorModel):
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainExecutionRole: Optional[str] = None
    name: Optional[str] = None
    singleSignOn: Optional[SingleSignOnTypeDef] = None

class UpdateDomainOutputTypeDef(BaseValidatorModel):
    description: str
    domainExecutionRole: str
    id: str
    lastUpdatedAt: datetime
    name: str
    singleSignOn: SingleSignOnTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentProfileIdentifier: str
    name: str
    projectIdentifier: str
    description: Optional[str] = None
    environmentAccountIdentifier: Optional[str] = None
    environmentAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None

class CreateEnvironmentProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str
    name: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None

class UpdateEnvironmentProfileInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None

class CreateEnvironmentProfileOutputTypeDef(BaseValidatorModel):
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
    userParameters: List[CustomParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentProfileOutputTypeDef(BaseValidatorModel):
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
    userParameters: List[CustomParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentProfileOutputTypeDef(BaseValidatorModel):
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
    userParameters: List[CustomParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFormTypeInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    model: ModelTypeDef
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None
    status: Optional[FormTypeStatusType] = None

class CreateGlossaryTermInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    glossaryIdentifier: str
    name: str
    clientToken: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsTypeDef] = None

class UpdateGlossaryTermInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    glossaryIdentifier: Optional[str] = None
    longDescription: Optional[str] = None
    name: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsTypeDef] = None

class CreateGlossaryTermOutputTypeDef(BaseValidatorModel):
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlossaryTermOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutputTypeDef
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GlossaryTermItemTypeDef(BaseValidatorModel):
    domainId: str
    glossaryId: str
    id: str
    name: str
    status: GlossaryTermStatusType
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None
    termRelations: Optional[TermRelationsOutputTypeDef] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class UpdateGlossaryTermOutputTypeDef(BaseValidatorModel):
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectMembershipInputRequestTypeDef(BaseValidatorModel):
    designation: UserDesignationType
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str

class DeleteProjectMembershipInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str

class CreateProjectOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    failureReasons: List[ProjectDeletionErrorTypeDef]
    glossaryTerms: List[str]
    id: str
    lastUpdatedAt: datetime
    name: str
    projectStatus: ProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    failureReasons: List[ProjectDeletionErrorTypeDef]
    glossaryTerms: List[str]
    id: str
    lastUpdatedAt: datetime
    name: str
    projectStatus: ProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectSummaryTypeDef(BaseValidatorModel):
    createdBy: str
    domainId: str
    id: str
    name: str
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    failureReasons: Optional[List[ProjectDeletionErrorTypeDef]] = None
    projectStatus: Optional[ProjectStatusType] = None
    updatedAt: Optional[datetime] = None

class UpdateProjectOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    failureReasons: List[ProjectDeletionErrorTypeDef]
    glossaryTerms: List[str]
    id: str
    lastUpdatedAt: datetime
    name: str
    projectStatus: ProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionTargetInputRequestTypeDef(BaseValidatorModel):
    applicableAssetTypes: Sequence[str]
    authorizedPrincipals: Sequence[str]
    domainIdentifier: str
    environmentIdentifier: str
    manageAccessRole: str
    name: str
    subscriptionTargetConfig: Sequence[SubscriptionTargetFormTypeDef]
    type: str
    clientToken: Optional[str] = None
    provider: Optional[str] = None

class CreateSubscriptionTargetOutputTypeDef(BaseValidatorModel):
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
    subscriptionTargetConfig: List[SubscriptionTargetFormTypeDef]
    type: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionTargetOutputTypeDef(BaseValidatorModel):
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
    subscriptionTargetConfig: List[SubscriptionTargetFormTypeDef]
    type: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionTargetSummaryTypeDef(BaseValidatorModel):
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
    subscriptionTargetConfig: List[SubscriptionTargetFormTypeDef]
    type: str
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class UpdateSubscriptionTargetInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    applicableAssetTypes: Optional[Sequence[str]] = None
    authorizedPrincipals: Optional[Sequence[str]] = None
    manageAccessRole: Optional[str] = None
    name: Optional[str] = None
    provider: Optional[str] = None
    subscriptionTargetConfig: Optional[Sequence[SubscriptionTargetFormTypeDef]] = None

class UpdateSubscriptionTargetOutputTypeDef(BaseValidatorModel):
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
    subscriptionTargetConfig: List[SubscriptionTargetFormTypeDef]
    type: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataProductSummaryTypeDef(BaseValidatorModel):
    domainId: str
    id: str
    name: str
    owningProjectId: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    dataProductItems: Optional[List[DataProductItemTypeDef]] = None
    description: Optional[str] = None
    glossaryTerms: Optional[List[str]] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class DataSourceRunSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    dataSourceId: str
    id: str
    projectId: str
    status: DataSourceRunStatusType
    type: DataSourceRunTypeType
    updatedAt: datetime
    errorMessage: Optional[DataSourceErrorMessageTypeDef] = None
    runStatisticsForAssets: Optional[RunStatisticsForAssetsTypeDef] = None
    startedAt: Optional[datetime] = None
    stoppedAt: Optional[datetime] = None

class GetDataSourceRunOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    dataSourceConfigurationSnapshot: str
    dataSourceId: str
    domainId: str
    errorMessage: DataSourceErrorMessageTypeDef
    id: str
    projectId: str
    runStatisticsForAssets: RunStatisticsForAssetsTypeDef
    startedAt: datetime
    status: DataSourceRunStatusType
    stoppedAt: datetime
    type: DataSourceRunTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceRunOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    dataSourceConfigurationSnapshot: str
    dataSourceId: str
    domainId: str
    errorMessage: DataSourceErrorMessageTypeDef
    id: str
    projectId: str
    runStatisticsForAssets: RunStatisticsForAssetsTypeDef
    startedAt: datetime
    status: DataSourceRunStatusType
    stoppedAt: datetime
    type: DataSourceRunTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    deploymentStatus: Optional[DeploymentStatusType] = None
    deploymentType: Optional[DeploymentTypeType] = None
    failureReason: Optional[EnvironmentErrorTypeDef] = None
    isDeploymentComplete: Optional[bool] = None
    messages: Optional[List[str]] = None

class ListDomainsOutputTypeDef(BaseValidatorModel):
    items: List[DomainSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentBlueprintConfigurationsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentBlueprintConfigurationItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentProfilesOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribedAssetTypeDef(BaseValidatorModel):
    assetId: str
    assetRevision: str
    status: SubscriptionGrantStatusType
    failureCause: Optional[FailureCauseTypeDef] = None
    failureTimestamp: Optional[datetime] = None
    grantedTimestamp: Optional[datetime] = None
    targetName: Optional[str] = None

class UpdateSubscriptionGrantStatusInputRequestTypeDef(BaseValidatorModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    status: SubscriptionGrantStatusType
    failureCause: Optional[FailureCauseTypeDef] = None
    targetName: Optional[str] = None

class FilterClauseTypeDef(BaseValidatorModel):
    and: Optional[Sequence[Dict[str, Any]]] = None
    filter: Optional[FilterTypeDef] = None
    or: Optional[Sequence[Dict[str, Any]]] = None

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

class GetLineageNodeInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    eventTimestamp: Optional[TimestampTypeDef] = None

class ListLineageNodeHistoryInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[TimestampTypeDef] = None
    eventTimestampLTE: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None

class ListNotificationsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    type: NotificationTypeType
    afterTimestamp: Optional[TimestampTypeDef] = None
    beforeTimestamp: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    subjects: Optional[Sequence[str]] = None
    taskStatus: Optional[TaskStatusType] = None

class ListTimeSeriesDataPointsInputRequestTypeDef(BaseValidatorModel):
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

class GetLineageNodeOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    downstreamNodes: List[LineageNodeReferenceTypeDef]
    eventTimestamp: datetime
    formsOutput: List[FormOutputTypeDef]
    id: str
    name: str
    sourceIdentifier: str
    typeName: str
    typeRevision: str
    updatedAt: datetime
    updatedBy: str
    upstreamNodes: List[LineageNodeReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetadataGenerationRunOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    owningProjectId: str
    status: MetadataGenerationRunStatusType
    target: MetadataGenerationRunTargetTypeDef
    type: Literal["BUSINESS_DESCRIPTIONS"]
    ResponseMetadata: ResponseMetadataTypeDef

class MetadataGenerationRunItemTypeDef(BaseValidatorModel):
    domainId: str
    id: str
    owningProjectId: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    status: Optional[MetadataGenerationRunStatusType] = None
    target: Optional[MetadataGenerationRunTargetTypeDef] = None
    type: Optional[Literal["BUSINESS_DESCRIPTIONS"]] = None

class StartMetadataGenerationRunInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    owningProjectIdentifier: str
    target: MetadataGenerationRunTargetTypeDef
    type: Literal["BUSINESS_DESCRIPTIONS"]
    clientToken: Optional[str] = None

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

class GrantedEntityTypeDef(BaseValidatorModel):
    listing: Optional[ListingRevisionTypeDef] = None

class SearchGroupProfilesOutputTypeDef(BaseValidatorModel):
    items: List[GroupProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLineageNodeHistoryOutputTypeDef(BaseValidatorModel):
    nextToken: str
    nodes: List[LineageNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    status: Optional[DataAssetActivityStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef(BaseValidatorModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    status: Optional[DataSourceRunStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesInputListDataSourcesPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    environmentIdentifier: Optional[str] = None
    name: Optional[str] = None
    status: Optional[DataSourceStatusType] = None
    type: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsInputListDomainsPaginateTypeDef(BaseValidatorModel):
    status: Optional[DomainStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentActionsInputListEnvironmentActionsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    name: Optional[str] = None
    projectIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsInputListEnvironmentsPaginateTypeDef(BaseValidatorModel):
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

class ListLineageNodeHistoryInputListLineageNodeHistoryPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[TimestampTypeDef] = None
    eventTimestampLTE: Optional[TimestampTypeDef] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetadataGenerationRunsInputListMetadataGenerationRunsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    status: Optional[MetadataGenerationRunStatusType] = None
    type: Optional[Literal["BUSINESS_DESCRIPTIONS"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationsInputListNotificationsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    type: NotificationTypeType
    afterTimestamp: Optional[TimestampTypeDef] = None
    beforeTimestamp: Optional[TimestampTypeDef] = None
    subjects: Optional[Sequence[str]] = None
    taskStatus: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    projectIdentifier: str
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsInputListProjectsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    name: Optional[str] = None
    userIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    subscribedListingId: Optional[str] = None
    subscriptionId: Optional[str] = None
    subscriptionTargetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionsInputListSubscriptionsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionStatusType] = None
    subscribedListingId: Optional[str] = None
    subscriptionRequestIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTimeSeriesDataPointsInputListTimeSeriesDataPointsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: Optional[TimestampTypeDef] = None
    startedAt: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchUserProfilesInputSearchUserProfilesPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MemberDetailsTypeDef(BaseValidatorModel):
    group: Optional[GroupDetailsTypeDef] = None
    user: Optional[UserDetailsTypeDef] = None

class TopicTypeDef(BaseValidatorModel):
    resource: NotificationResourceTypeDef
    role: NotificationRoleType
    subject: str

class RedshiftStorageTypeDef(BaseValidatorModel):
    redshiftClusterSource: Optional[RedshiftClusterStorageTypeDef] = None
    redshiftServerlessSource: Optional[RedshiftServerlessStorageTypeDef] = None

class RejectPredictionsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    rejectChoices: Optional[Sequence[RejectChoiceTypeDef]] = None
    rejectRule: Optional[RejectRuleTypeDef] = None
    revision: Optional[str] = None

class SearchInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional["FilterClauseTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None

class SearchListingsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional["FilterClauseTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None

class SearchTypesInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional["FilterClauseTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None

class UserProfileDetailsTypeDef(BaseValidatorModel):
    iam: Optional[IamUserProfileDetailsTypeDef] = None
    sso: Optional[SsoUserProfileDetailsTypeDef] = None

class SubscribedPrincipalInputTypeDef(BaseValidatorModel):
    project: Optional[SubscribedProjectInputTypeDef] = None

class SubscribedPrincipalTypeDef(BaseValidatorModel):
    project: Optional[SubscribedProjectTypeDef] = None

class CreateEnvironmentActionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    parameters: ActionParametersTypeDef
    description: Optional[str] = None

class CreateEnvironmentActionOutputTypeDef(BaseValidatorModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentActionSummaryTypeDef(BaseValidatorModel):
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    description: Optional[str] = None

class GetEnvironmentActionOutputTypeDef(BaseValidatorModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentActionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[ActionParametersTypeDef] = None

class UpdateEnvironmentActionOutputTypeDef(BaseValidatorModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListingItemTypeDef(BaseValidatorModel):
    assetListing: Optional[AssetListingTypeDef] = None

class SubscribedListingItemTypeDef(BaseValidatorModel):
    assetListing: Optional[SubscribedAssetListingTypeDef] = None

class CreateAssetInputRequestTypeDef(BaseValidatorModel):
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

class CreateAssetOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    externalIdentifier: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutputTypeDef]
    glossaryTerms: List[str]
    id: str
    latestTimeSeriesDataPointFormsOutput: List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    listing: AssetListingDetailsTypeDef
    name: str
    owningProjectId: str
    predictionConfiguration: PredictionConfigurationTypeDef
    readOnlyFormsOutput: List[FormOutputTypeDef]
    revision: str
    typeIdentifier: str
    typeRevision: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssetRevisionInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInputTypeDef]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    predictionConfiguration: Optional[PredictionConfigurationTypeDef] = None
    typeRevision: Optional[str] = None

class CreateAssetRevisionOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    externalIdentifier: str
    firstRevisionCreatedAt: datetime
    firstRevisionCreatedBy: str
    formsOutput: List[FormOutputTypeDef]
    glossaryTerms: List[str]
    id: str
    latestTimeSeriesDataPointFormsOutput: List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    listing: AssetListingDetailsTypeDef
    name: str
    owningProjectId: str
    predictionConfiguration: PredictionConfigurationTypeDef
    readOnlyFormsOutput: List[FormOutputTypeDef]
    revision: str
    typeIdentifier: str
    typeRevision: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentBlueprintSummaryTypeDef(BaseValidatorModel):
    id: str
    name: str
    provider: str
    provisioningProperties: ProvisioningPropertiesTypeDef
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    updatedAt: Optional[datetime] = None

class GetEnvironmentBlueprintOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    deploymentProperties: DeploymentPropertiesTypeDef
    description: str
    glossaryTerms: List[str]
    id: str
    name: str
    provider: str
    provisioningProperties: ProvisioningPropertiesTypeDef
    updatedAt: datetime
    userParameters: List[CustomParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourceRunActivitiesOutputTypeDef(BaseValidatorModel):
    items: List[DataSourceRunActivityTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesOutputTypeDef(BaseValidatorModel):
    items: List[DataSourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsOutputTypeDef(BaseValidatorModel):
    items: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionTargetsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionTargetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourceRunsOutputTypeDef(BaseValidatorModel):
    items: List[DataSourceRunSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentOutputTypeDef(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    deploymentProperties: DeploymentPropertiesTypeDef
    description: str
    domainId: str
    environmentActions: List[ConfigurableEnvironmentActionTypeDef]
    environmentBlueprintId: str
    environmentProfileId: str
    glossaryTerms: List[str]
    id: str
    lastDeployment: DeploymentTypeDef
    name: str
    projectId: str
    provider: str
    provisionedResources: List[ResourceTypeDef]
    provisioningProperties: ProvisioningPropertiesTypeDef
    status: EnvironmentStatusType
    updatedAt: datetime
    userParameters: List[CustomParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentOutputTypeDef(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    deploymentProperties: DeploymentPropertiesTypeDef
    description: str
    domainId: str
    environmentActions: List[ConfigurableEnvironmentActionTypeDef]
    environmentBlueprintId: str
    environmentProfileId: str
    glossaryTerms: List[str]
    id: str
    lastDeployment: DeploymentTypeDef
    name: str
    projectId: str
    provider: str
    provisionedResources: List[ResourceTypeDef]
    provisioningProperties: ProvisioningPropertiesTypeDef
    status: EnvironmentStatusType
    updatedAt: datetime
    userParameters: List[CustomParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentOutputTypeDef(BaseValidatorModel):
    awsAccountId: str
    awsAccountRegion: str
    createdAt: datetime
    createdBy: str
    deploymentProperties: DeploymentPropertiesTypeDef
    description: str
    domainId: str
    environmentActions: List[ConfigurableEnvironmentActionTypeDef]
    environmentBlueprintId: str
    environmentProfileId: str
    glossaryTerms: List[str]
    id: str
    lastDeployment: DeploymentTypeDef
    name: str
    projectId: str
    provider: str
    provisionedResources: List[ResourceTypeDef]
    provisioningProperties: ProvisioningPropertiesTypeDef
    status: EnvironmentStatusType
    updatedAt: datetime
    userParameters: List[CustomParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchInputSearchPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClauseTypeDef] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchListingsInputSearchListingsPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClauseTypeDef] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTypesInputSearchTypesPaginateTypeDef(BaseValidatorModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClauseTypeDef] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GlueRunConfigurationOutputTypeDef(BaseValidatorModel):
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: Optional[str] = None
    autoImportDataQualityResult: Optional[bool] = None
    dataAccessRole: Optional[str] = None
    region: Optional[str] = None

class GlueRunConfigurationInputTypeDef(BaseValidatorModel):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationTypeDef]
    autoImportDataQualityResult: Optional[bool] = None
    dataAccessRole: Optional[str] = None

class SearchTypesResultItemTypeDef(BaseValidatorModel):
    assetTypeItem: Optional[AssetTypeItemTypeDef] = None
    formTypeItem: Optional[FormTypeDataTypeDef] = None
    lineageNodeTypeItem: Optional[LineageNodeTypeItemTypeDef] = None

class PostTimeSeriesDataPointsInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    forms: Sequence[TimeSeriesDataPointFormInputTypeDef]
    clientToken: Optional[str] = None

class ListMetadataGenerationRunsOutputTypeDef(BaseValidatorModel):
    items: List[MetadataGenerationRunItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SelfGrantStatusOutputTypeDef(BaseValidatorModel):
    glueSelfGrantStatus: Optional[GlueSelfGrantStatusOutputTypeDef] = None
    redshiftSelfGrantStatus: Optional[RedshiftSelfGrantStatusOutputTypeDef] = None

class CreateSubscriptionGrantInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    grantedEntity: GrantedEntityInputTypeDef
    subscriptionTargetIdentifier: str
    assetTargetNames: Optional[Sequence[AssetTargetNameMapTypeDef]] = None
    clientToken: Optional[str] = None

class CreateSubscriptionGrantOutputTypeDef(BaseValidatorModel):
    assets: List[SubscribedAssetTypeDef]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntityTypeDef
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSubscriptionGrantOutputTypeDef(BaseValidatorModel):
    assets: List[SubscribedAssetTypeDef]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntityTypeDef
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionGrantOutputTypeDef(BaseValidatorModel):
    assets: List[SubscribedAssetTypeDef]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntityTypeDef
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionGrantSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntityTypeDef
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionTargetId: str
    updatedAt: datetime
    assets: Optional[List[SubscribedAssetTypeDef]] = None
    subscriptionId: Optional[str] = None
    updatedBy: Optional[str] = None

class UpdateSubscriptionGrantStatusOutputTypeDef(BaseValidatorModel):
    assets: List[SubscribedAssetTypeDef]
    createdAt: datetime
    createdBy: str
    domainId: str
    grantedEntity: GrantedEntityTypeDef
    id: str
    status: SubscriptionGrantOverallStatusType
    subscriptionId: str
    subscriptionTargetId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProjectMemberTypeDef(BaseValidatorModel):
    designation: UserDesignationType
    memberDetails: MemberDetailsTypeDef

class NotificationOutputTypeDef(BaseValidatorModel):
    actionLink: str
    creationTimestamp: datetime
    domainIdentifier: str
    identifier: str
    lastUpdatedTimestamp: datetime
    message: str
    title: str
    topic: TopicTypeDef
    type: NotificationTypeType
    metadata: Optional[Dict[str, str]] = None
    status: Optional[TaskStatusType] = None

class RedshiftRunConfigurationInputTypeDef(BaseValidatorModel):
    redshiftCredentialConfiguration: RedshiftCredentialConfigurationTypeDef
    redshiftStorage: RedshiftStorageTypeDef
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationTypeDef]
    dataAccessRole: Optional[str] = None

class RedshiftRunConfigurationOutputTypeDef(BaseValidatorModel):
    redshiftCredentialConfiguration: RedshiftCredentialConfigurationTypeDef
    redshiftStorage: RedshiftStorageTypeDef
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: Optional[str] = None
    dataAccessRole: Optional[str] = None
    region: Optional[str] = None

class CreateUserProfileOutputTypeDef(BaseValidatorModel):
    details: UserProfileDetailsTypeDef
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserProfileOutputTypeDef(BaseValidatorModel):
    details: UserProfileDetailsTypeDef
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserProfileOutputTypeDef(BaseValidatorModel):
    details: UserProfileDetailsTypeDef
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UserProfileSummaryTypeDef(BaseValidatorModel):
    details: Optional[UserProfileDetailsTypeDef] = None
    domainId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[UserProfileStatusType] = None
    type: Optional[UserProfileTypeType] = None

class CreateSubscriptionRequestInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    requestReason: str
    subscribedListings: Sequence[SubscribedListingInputTypeDef]
    subscribedPrincipals: Sequence[SubscribedPrincipalInputTypeDef]
    clientToken: Optional[str] = None

class ListEnvironmentActionsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentActionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchInventoryResultItemTypeDef(BaseValidatorModel):
    assetItem: Optional[AssetItemTypeDef] = None
    dataProductItem: Optional[DataProductSummaryTypeDef] = None
    glossaryItem: Optional[GlossaryItemTypeDef] = None
    glossaryTermItem: Optional[GlossaryTermItemTypeDef] = None

class SearchResultItemTypeDef(BaseValidatorModel):
    assetListing: Optional[AssetListingItemTypeDef] = None

class GetListingOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    description: str
    domainId: str
    id: str
    item: ListingItemTypeDef
    listingRevision: str
    name: str
    status: ListingStatusType
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribedListingTypeDef(BaseValidatorModel):
    description: str
    id: str
    item: SubscribedListingItemTypeDef
    name: str
    ownerProjectId: str
    ownerProjectName: Optional[str] = None
    revision: Optional[str] = None

class ListEnvironmentBlueprintsOutputTypeDef(BaseValidatorModel):
    items: List[EnvironmentBlueprintSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchTypesOutputTypeDef(BaseValidatorModel):
    items: List[SearchTypesResultItemTypeDef]
    nextToken: str
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionGrantsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionGrantSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectMembershipsOutputTypeDef(BaseValidatorModel):
    members: List[ProjectMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    notifications: List[NotificationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationInputTypeDef(BaseValidatorModel):
    glueRunConfiguration: Optional[GlueRunConfigurationInputTypeDef] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationInputTypeDef] = None

class DataSourceConfigurationOutputTypeDef(BaseValidatorModel):
    glueRunConfiguration: Optional[GlueRunConfigurationOutputTypeDef] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationOutputTypeDef] = None

class SearchUserProfilesOutputTypeDef(BaseValidatorModel):
    items: List[UserProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchOutputTypeDef(BaseValidatorModel):
    items: List[SearchInventoryResultItemTypeDef]
    nextToken: str
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class SearchListingsOutputTypeDef(BaseValidatorModel):
    items: List[SearchResultItemTypeDef]
    nextToken: str
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptSubscriptionRequestOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    id: str
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListingTypeDef]
    subscribedPrincipals: List[SubscribedPrincipalTypeDef]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelSubscriptionOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    retainPermissions: bool
    status: SubscriptionStatusType
    subscribedListing: SubscribedListingTypeDef
    subscribedPrincipal: SubscribedPrincipalTypeDef
    subscriptionRequestId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriptionRequestOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    id: str
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListingTypeDef]
    subscribedPrincipals: List[SubscribedPrincipalTypeDef]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    retainPermissions: bool
    status: SubscriptionStatusType
    subscribedListing: SubscribedListingTypeDef
    subscribedPrincipal: SubscribedPrincipalTypeDef
    subscriptionRequestId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionRequestDetailsOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    id: str
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListingTypeDef]
    subscribedPrincipals: List[SubscribedPrincipalTypeDef]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectSubscriptionRequestOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    id: str
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListingTypeDef]
    subscribedPrincipals: List[SubscribedPrincipalTypeDef]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeSubscriptionOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    retainPermissions: bool
    status: SubscriptionStatusType
    subscribedListing: SubscribedListingTypeDef
    subscribedPrincipal: SubscribedPrincipalTypeDef
    subscriptionRequestId: str
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionRequestSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    requestReason: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListingTypeDef]
    subscribedPrincipals: List[SubscribedPrincipalTypeDef]
    updatedAt: datetime
    decisionComment: Optional[str] = None
    reviewerId: Optional[str] = None
    updatedBy: Optional[str] = None

class SubscriptionSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    status: SubscriptionStatusType
    subscribedListing: SubscribedListingTypeDef
    subscribedPrincipal: SubscribedPrincipalTypeDef
    updatedAt: datetime
    retainPermissions: Optional[bool] = None
    subscriptionRequestId: Optional[str] = None
    updatedBy: Optional[str] = None

class UpdateSubscriptionRequestOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    createdBy: str
    decisionComment: str
    domainId: str
    id: str
    requestReason: str
    reviewerId: str
    status: SubscriptionRequestStatusType
    subscribedListings: List[SubscribedListingTypeDef]
    subscribedPrincipals: List[SubscribedPrincipalTypeDef]
    updatedAt: datetime
    updatedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceInputRequestTypeDef(BaseValidatorModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    projectIdentifier: str
    type: str
    assetFormsInput: Optional[Sequence[FormInputTypeDef]] = None
    clientToken: Optional[str] = None
    configuration: Optional[DataSourceConfigurationInputTypeDef] = None
    description: Optional[str] = None
    enableSetting: Optional[EnableSettingType] = None
    publishOnImport: Optional[bool] = None
    recommendation: Optional[RecommendationConfigurationTypeDef] = None
    schedule: Optional[ScheduleConfigurationTypeDef] = None

class UpdateDataSourceInputRequestTypeDef(BaseValidatorModel):
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

class CreateDataSourceOutputTypeDef(BaseValidatorModel):
    assetFormsOutput: List[FormOutputTypeDef]
    configuration: DataSourceConfigurationOutputTypeDef
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessageTypeDef
    id: str
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessageTypeDef
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    recommendation: RecommendationConfigurationTypeDef
    schedule: ScheduleConfigurationTypeDef
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceOutputTypeDef(BaseValidatorModel):
    assetFormsOutput: List[FormOutputTypeDef]
    configuration: DataSourceConfigurationOutputTypeDef
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessageTypeDef
    id: str
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessageTypeDef
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    retainPermissionsOnRevokeFailure: bool
    schedule: ScheduleConfigurationTypeDef
    selfGrantStatus: SelfGrantStatusOutputTypeDef
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceOutputTypeDef(BaseValidatorModel):
    assetFormsOutput: List[FormOutputTypeDef]
    configuration: DataSourceConfigurationOutputTypeDef
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessageTypeDef
    id: str
    lastRunAssetCount: int
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessageTypeDef
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    recommendation: RecommendationConfigurationTypeDef
    schedule: ScheduleConfigurationTypeDef
    selfGrantStatus: SelfGrantStatusOutputTypeDef
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceOutputTypeDef(BaseValidatorModel):
    assetFormsOutput: List[FormOutputTypeDef]
    configuration: DataSourceConfigurationOutputTypeDef
    createdAt: datetime
    description: str
    domainId: str
    enableSetting: EnableSettingType
    environmentId: str
    errorMessage: DataSourceErrorMessageTypeDef
    id: str
    lastRunAt: datetime
    lastRunErrorMessage: DataSourceErrorMessageTypeDef
    lastRunStatus: DataSourceRunStatusType
    name: str
    projectId: str
    publishOnImport: bool
    recommendation: RecommendationConfigurationTypeDef
    retainPermissionsOnRevokeFailure: bool
    schedule: ScheduleConfigurationTypeDef
    selfGrantStatus: SelfGrantStatusOutputTypeDef
    status: DataSourceStatusType
    type: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionRequestsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionRequestSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionsOutputTypeDef(BaseValidatorModel):
    items: List[SubscriptionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

