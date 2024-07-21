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
from aws_resource_validator.pydantic_models.datazone_constants import *

class AcceptChoiceTypeDef(BaseModel):
    predictionTarget: str
    editedValue: Optional[str] = None
    predictionChoice: Optional[int] = None

class AcceptRuleTypeDef(BaseModel):
    rule: Optional[AcceptRuleBehaviorType] = None
    threshold: Optional[float] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AcceptSubscriptionRequestInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    decisionComment: Optional[str] = None

class AwsConsoleLinkParametersTypeDef(BaseModel):
    uri: Optional[str] = None

class FormOutputTypeDef(BaseModel):
    formName: str
    content: Optional[str] = None
    typeName: Optional[str] = None
    typeRevision: Optional[str] = None

class TimeSeriesDataPointSummaryFormOutputTypeDef(BaseModel):
    formName: str
    timestamp: datetime
    typeIdentifier: str
    contentSummary: Optional[str] = None
    id: Optional[str] = None
    typeRevision: Optional[str] = None

class AssetListingDetailsTypeDef(BaseModel):
    listingId: str
    listingStatus: ListingStatusType

class DetailedGlossaryTermTypeDef(BaseModel):
    name: Optional[str] = None
    shortDescription: Optional[str] = None

class AssetRevisionTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    domainId: Optional[str] = None
    id: Optional[str] = None
    revision: Optional[str] = None

class AssetTargetNameMapTypeDef(BaseModel):
    assetId: str
    targetName: str

class FormEntryOutputTypeDef(BaseModel):
    typeName: str
    typeRevision: str
    required: Optional[bool] = None

class AssociateEnvironmentRoleInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str

class BusinessNameGenerationConfigurationTypeDef(BaseModel):
    enabled: Optional[bool] = None

class CancelMetadataGenerationRunInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class CancelSubscriptionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class CloudFormationPropertiesTypeDef(BaseModel):
    templateUrl: str

class ConfigurableActionParameterTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class FormInputTypeDef(BaseModel):
    formName: str
    content: Optional[str] = None
    typeIdentifier: Optional[str] = None
    typeRevision: Optional[str] = None

class FormEntryInputTypeDef(BaseModel):
    typeIdentifier: str
    typeRevision: str
    required: Optional[bool] = None

class RecommendationConfigurationTypeDef(BaseModel):
    enableBusinessNameGeneration: Optional[bool] = None

class ScheduleConfigurationTypeDef(BaseModel):
    schedule: Optional[str] = None
    timezone: Optional[TimezoneType] = None

class DataSourceErrorMessageTypeDef(BaseModel):
    errorType: DataSourceErrorTypeType
    errorDetail: Optional[str] = None

class SingleSignOnTypeDef(BaseModel):
    type: Optional[AuthTypeType] = None
    userAssignment: Optional[UserAssignmentType] = None

class EnvironmentParameterTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class CustomParameterTypeDef(BaseModel):
    fieldType: str
    keyName: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    isEditable: Optional[bool] = None
    isOptional: Optional[bool] = None

class DeploymentPropertiesTypeDef(BaseModel):
    endTimeoutMinutes: Optional[int] = None
    startTimeoutMinutes: Optional[int] = None

class ResourceTypeDef(BaseModel):
    type: str
    value: str
    name: Optional[str] = None
    provider: Optional[str] = None

class ModelTypeDef(BaseModel):
    smithy: Optional[str] = None

class CreateGlossaryInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    name: str
    owningProjectIdentifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    status: Optional[GlossaryStatusType] = None

class TermRelationsTypeDef(BaseModel):
    classifies: Optional[Sequence[str]] = None
    isA: Optional[Sequence[str]] = None

class TermRelationsOutputTypeDef(BaseModel):
    classifies: Optional[List[str]] = None
    isA: Optional[List[str]] = None

class CreateGroupProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    groupIdentifier: str
    clientToken: Optional[str] = None

class CreateListingChangeSetInputRequestTypeDef(BaseModel):
    action: ChangeActionType
    domainIdentifier: str
    entityIdentifier: str
    entityType: Literal["ASSET"]
    clientToken: Optional[str] = None
    entityRevision: Optional[str] = None

class CreateProjectInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    name: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None

class MemberTypeDef(BaseModel):
    groupIdentifier: Optional[str] = None
    userIdentifier: Optional[str] = None

class ProjectDeletionErrorTypeDef(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

class SubscribedListingInputTypeDef(BaseModel):
    identifier: str

class SubscriptionTargetFormTypeDef(BaseModel):
    content: str
    formName: str

class CreateUserProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    userIdentifier: str
    clientToken: Optional[str] = None
    userType: Optional[UserTypeType] = None

class DataProductItemTypeDef(BaseModel):
    domainId: Optional[str] = None
    itemId: Optional[str] = None

class RunStatisticsForAssetsTypeDef(BaseModel):
    added: Optional[int] = None
    failed: Optional[int] = None
    skipped: Optional[int] = None
    unchanged: Optional[int] = None
    updated: Optional[int] = None

class DeleteAssetInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteAssetTypeInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteDataSourceInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    retainPermissionsOnRevokeFailure: Optional[bool] = None

class DeleteDomainInputRequestTypeDef(BaseModel):
    identifier: str
    clientToken: Optional[str] = None
    skipDeletionCheck: Optional[bool] = None

class DeleteEnvironmentActionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str

class DeleteEnvironmentInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteEnvironmentProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteFormTypeInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    formTypeIdentifier: str

class DeleteGlossaryInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteGlossaryTermInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteListingInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteProjectInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    skipDeletionCheck: Optional[bool] = None

class DeleteSubscriptionGrantInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteSubscriptionRequestInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class DeleteSubscriptionTargetInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class DeleteTimeSeriesDataPointsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    clientToken: Optional[str] = None

class EnvironmentErrorTypeDef(BaseModel):
    message: str
    code: Optional[str] = None

class DisassociateEnvironmentRoleInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    environmentRoleArn: str

class DomainSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    id: str
    managedAccountId: str
    name: str
    status: DomainStatusType
    description: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    portalUrl: Optional[str] = None

class EnvironmentBlueprintConfigurationItemTypeDef(BaseModel):
    domainId: str
    environmentBlueprintId: str
    createdAt: Optional[datetime] = None
    enabledRegions: Optional[List[str]] = None
    manageAccessRoleArn: Optional[str] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Dict[str, Dict[str, str]]] = None
    updatedAt: Optional[datetime] = None

class EnvironmentProfileSummaryTypeDef(BaseModel):
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

class EnvironmentSummaryTypeDef(BaseModel):
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

class FailureCauseTypeDef(BaseModel):
    message: Optional[str] = None

class FilterTypeDef(BaseModel):
    attribute: str
    value: str

class FilterExpressionTypeDef(BaseModel):
    expression: str
    type: FilterExpressionTypeType

class ImportTypeDef(BaseModel):
    name: str
    revision: str

class GetAssetInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None

class GetAssetTypeInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    revision: Optional[str] = None

class GetDataSourceInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetDataSourceRunInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetDomainInputRequestTypeDef(BaseModel):
    identifier: str

class GetEnvironmentActionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class GetEnvironmentBlueprintConfigurationInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str

class GetEnvironmentBlueprintInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetEnvironmentInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetEnvironmentProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetFormTypeInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    formTypeIdentifier: str
    revision: Optional[str] = None

class GetGlossaryInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetGlossaryTermInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetGroupProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    groupIdentifier: str

class GetIamPortalLoginUrlInputRequestTypeDef(BaseModel):
    domainIdentifier: str

class LineageNodeReferenceTypeDef(BaseModel):
    eventTimestamp: Optional[datetime] = None
    id: Optional[str] = None

class GetListingInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    listingRevision: Optional[str] = None

class GetMetadataGenerationRunInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class MetadataGenerationRunTargetTypeDef(BaseModel):
    identifier: str
    type: Literal["ASSET"]
    revision: Optional[str] = None

class GetProjectInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionGrantInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionRequestDetailsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str

class GetSubscriptionTargetInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str

class GetTimeSeriesDataPointInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    identifier: str

class TimeSeriesDataPointFormOutputTypeDef(BaseModel):
    formName: str
    timestamp: datetime
    typeIdentifier: str
    content: Optional[str] = None
    id: Optional[str] = None
    typeRevision: Optional[str] = None

class GetUserProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    userIdentifier: str
    type: Optional[UserProfileTypeType] = None

class GlossaryItemTypeDef(BaseModel):
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

class SelfGrantStatusDetailTypeDef(BaseModel):
    databaseName: str
    status: SelfGrantStatusType
    failureCause: Optional[str] = None
    schemaName: Optional[str] = None

class ListingRevisionInputTypeDef(BaseModel):
    identifier: str
    revision: str

class ListingRevisionTypeDef(BaseModel):
    id: str
    revision: str

class GroupDetailsTypeDef(BaseModel):
    groupId: str

class GroupProfileSummaryTypeDef(BaseModel):
    domainId: Optional[str] = None
    groupName: Optional[str] = None
    id: Optional[str] = None
    status: Optional[GroupProfileStatusType] = None

class IamUserProfileDetailsTypeDef(BaseModel):
    arn: Optional[str] = None

class LineageNodeSummaryTypeDef(BaseModel):
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

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssetRevisionsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDataSourceRunActivitiesInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataAssetActivityStatusType] = None

class ListDataSourceRunsInputRequestTypeDef(BaseModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceRunStatusType] = None

class ListDataSourcesInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    projectIdentifier: str
    environmentIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    status: Optional[DataSourceStatusType] = None
    type: Optional[str] = None

class ListDomainsInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[DomainStatusType] = None

class ListEnvironmentActionsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentBlueprintConfigurationsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEnvironmentBlueprintsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None

class ListEnvironmentProfilesInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    projectIdentifier: Optional[str] = None

class ListEnvironmentsInputRequestTypeDef(BaseModel):
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

class ListMetadataGenerationRunsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[MetadataGenerationRunStatusType] = None
    type: Optional[Literal["BUSINESS_DESCRIPTIONS"]] = None

class ListProjectMembershipsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    projectIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListProjectsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    name: Optional[str] = None
    nextToken: Optional[str] = None
    userIdentifier: Optional[str] = None

class ListSubscriptionGrantsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    subscribedListingId: Optional[str] = None
    subscriptionId: Optional[str] = None
    subscriptionTargetId: Optional[str] = None

class ListSubscriptionRequestsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None

class ListSubscriptionTargetsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None

class ListSubscriptionsInputRequestTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class UserDetailsTypeDef(BaseModel):
    userId: str

class NotificationResourceTypeDef(BaseModel):
    id: str
    type: Literal["PROJECT"]
    name: Optional[str] = None

class PutEnvironmentBlueprintConfigurationInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    enabledRegions: Sequence[str]
    environmentBlueprintIdentifier: str
    manageAccessRoleArn: Optional[str] = None
    provisioningRoleArn: Optional[str] = None
    regionalParameters: Optional[Mapping[str, Mapping[str, str]]] = None

class RedshiftClusterStorageTypeDef(BaseModel):
    clusterName: str

class RedshiftCredentialConfigurationTypeDef(BaseModel):
    secretManagerArn: str

class RedshiftServerlessStorageTypeDef(BaseModel):
    workgroupName: str

class RejectChoiceTypeDef(BaseModel):
    predictionTarget: str
    predictionChoices: Optional[Sequence[int]] = None

class RejectRuleTypeDef(BaseModel):
    rule: Optional[RejectRuleBehaviorType] = None
    threshold: Optional[float] = None

class RejectSubscriptionRequestInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    decisionComment: Optional[str] = None

class RevokeSubscriptionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    retainPermissions: Optional[bool] = None

class SearchGroupProfilesInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchText: Optional[str] = None

class SearchInItemTypeDef(BaseModel):
    attribute: str

class SearchSortTypeDef(BaseModel):
    attribute: str
    order: Optional[SortOrderType] = None

class SearchUserProfilesInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchText: Optional[str] = None

class SsoUserProfileDetailsTypeDef(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    username: Optional[str] = None

class StartDataSourceRunInputRequestTypeDef(BaseModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    clientToken: Optional[str] = None

class SubscribedProjectInputTypeDef(BaseModel):
    identifier: Optional[str] = None

class SubscribedProjectTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TermRelationsExtraOutputTypeDef(BaseModel):
    classifies: Optional[List[str]] = None
    isA: Optional[List[str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEnvironmentInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None

class UpdateGlossaryInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    status: Optional[GlossaryStatusType] = None

class UpdateGroupProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    groupIdentifier: str
    status: GroupProfileStatusType

class UpdateProjectInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    description: Optional[str] = None
    glossaryTerms: Optional[Sequence[str]] = None
    name: Optional[str] = None

class UpdateSubscriptionRequestInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    requestReason: str

class UpdateUserProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    status: UserProfileStatusType
    userIdentifier: str
    type: Optional[UserProfileTypeType] = None

class AcceptPredictionsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    acceptChoices: Optional[Sequence[AcceptChoiceTypeDef]] = None
    acceptRule: Optional[AcceptRuleTypeDef] = None
    clientToken: Optional[str] = None
    revision: Optional[str] = None

class AcceptPredictionsOutputTypeDef(BaseModel):
    assetId: str
    domainId: str
    revision: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFormTypeOutputTypeDef(BaseModel):
    description: str
    domainId: str
    name: str
    originDomainId: str
    originProjectId: str
    owningProjectId: str
    revision: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGlossaryOutputTypeDef(BaseModel):
    description: str
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupProfileOutputTypeDef(BaseModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateListingChangeSetOutputTypeDef(BaseModel):
    listingId: str
    listingRevision: str
    status: ListingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainOutputTypeDef(BaseModel):
    status: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentBlueprintConfigurationOutputTypeDef(BaseModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    manageAccessRoleArn: str
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlossaryOutputTypeDef(BaseModel):
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

class GetGroupProfileOutputTypeDef(BaseModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetIamPortalLoginUrlOutputTypeDef(BaseModel):
    authCodeUrl: str
    userProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutEnvironmentBlueprintConfigurationOutputTypeDef(BaseModel):
    createdAt: datetime
    domainId: str
    enabledRegions: List[str]
    environmentBlueprintId: str
    manageAccessRoleArn: str
    provisioningRoleArn: str
    regionalParameters: Dict[str, Dict[str, str]]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RejectPredictionsOutputTypeDef(BaseModel):
    assetId: str
    assetRevision: str
    domainId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataGenerationRunOutputTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    owningProjectId: str
    status: MetadataGenerationRunStatusType
    type: Literal["BUSINESS_DESCRIPTIONS"]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlossaryOutputTypeDef(BaseModel):
    description: str
    domainId: str
    id: str
    name: str
    owningProjectId: str
    status: GlossaryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupProfileOutputTypeDef(BaseModel):
    domainId: str
    groupName: str
    id: str
    status: GroupProfileStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ActionParametersTypeDef(BaseModel):
    awsConsoleLink: Optional[AwsConsoleLinkParametersTypeDef] = None

class AssetItemAdditionalAttributesTypeDef(BaseModel):
    formsOutput: Optional[List[FormOutputTypeDef]] = None
    latestTimeSeriesDataPointFormsOutput: Optional[       List[TimeSeriesDataPointSummaryFormOutputTypeDef]     ] = None
    readOnlyFormsOutput: Optional[List[FormOutputTypeDef]] = None

class AssetListingItemAdditionalAttributesTypeDef(BaseModel):
    forms: Optional[str] = None
    latestTimeSeriesDataPointForms: Optional[       List[TimeSeriesDataPointSummaryFormOutputTypeDef]     ] = None

class ListTimeSeriesDataPointsOutputTypeDef(BaseModel):
    items: List[TimeSeriesDataPointSummaryFormOutputTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssetOutputTypeDef(BaseModel):
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

class AssetListingTypeDef(BaseModel):
    assetId: Optional[str] = None
    assetRevision: Optional[str] = None
    assetType: Optional[str] = None
    createdAt: Optional[datetime] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None
    latestTimeSeriesDataPointForms: Optional[       List[TimeSeriesDataPointSummaryFormOutputTypeDef]     ] = None
    owningProjectId: Optional[str] = None

class SubscribedAssetListingTypeDef(BaseModel):
    entityId: Optional[str] = None
    entityRevision: Optional[str] = None
    entityType: Optional[str] = None
    forms: Optional[str] = None
    glossaryTerms: Optional[List[DetailedGlossaryTermTypeDef]] = None

class ListAssetRevisionsOutputTypeDef(BaseModel):
    items: List[AssetRevisionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssetTypeItemTypeDef(BaseModel):
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

class CreateAssetTypeOutputTypeDef(BaseModel):
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

class GetAssetTypeOutputTypeDef(BaseModel):
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

class LineageNodeTypeItemTypeDef(BaseModel):
    domainId: str
    formsOutput: Dict[str, FormEntryOutputTypeDef]
    revision: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    updatedAt: Optional[datetime] = None
    updatedBy: Optional[str] = None

class PostLineageEventInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    event: BlobTypeDef
    clientToken: Optional[str] = None

class PredictionConfigurationTypeDef(BaseModel):
    businessNameGeneration: Optional[BusinessNameGenerationConfigurationTypeDef] = None

class ProvisioningPropertiesTypeDef(BaseModel):
    cloudFormation: Optional[CloudFormationPropertiesTypeDef] = None

class ConfigurableEnvironmentActionTypeDef(BaseModel):
    parameters: List[ConfigurableActionParameterTypeDef]
    type: str
    auth: Optional[ConfigurableActionTypeAuthorizationType] = None

class CreateAssetTypeInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    formsInput: Mapping[str, FormEntryInputTypeDef]
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None

class DataSourceRunActivityTypeDef(BaseModel):
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

class DataSourceSummaryTypeDef(BaseModel):
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

class CreateDomainInputRequestTypeDef(BaseModel):
    domainExecutionRole: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    kmsKeyIdentifier: Optional[str] = None
    singleSignOn: Optional[SingleSignOnTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateDomainOutputTypeDef(BaseModel):
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

class GetDomainOutputTypeDef(BaseModel):
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

class UpdateDomainInputRequestTypeDef(BaseModel):
    identifier: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    domainExecutionRole: Optional[str] = None
    name: Optional[str] = None
    singleSignOn: Optional[SingleSignOnTypeDef] = None

class UpdateDomainOutputTypeDef(BaseModel):
    description: str
    domainExecutionRole: str
    id: str
    lastUpdatedAt: datetime
    name: str
    singleSignOn: SingleSignOnTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentInputRequestTypeDef(BaseModel):
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

class CreateEnvironmentProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentBlueprintIdentifier: str
    name: str
    projectIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None

class UpdateEnvironmentProfileInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None
    userParameters: Optional[Sequence[EnvironmentParameterTypeDef]] = None

class CreateEnvironmentProfileOutputTypeDef(BaseModel):
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

class GetEnvironmentProfileOutputTypeDef(BaseModel):
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

class UpdateEnvironmentProfileOutputTypeDef(BaseModel):
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

class CreateFormTypeInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    model: ModelTypeDef
    name: str
    owningProjectIdentifier: str
    description: Optional[str] = None
    status: Optional[FormTypeStatusType] = None

class CreateGlossaryTermInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    glossaryIdentifier: str
    name: str
    clientToken: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsTypeDef] = None

class UpdateGlossaryTermInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    glossaryIdentifier: Optional[str] = None
    longDescription: Optional[str] = None
    name: Optional[str] = None
    shortDescription: Optional[str] = None
    status: Optional[GlossaryTermStatusType] = None
    termRelations: Optional[TermRelationsTypeDef] = None

class CreateGlossaryTermOutputTypeDef(BaseModel):
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlossaryTermOutputTypeDef(BaseModel):
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

class GlossaryTermItemTypeDef(BaseModel):
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

class UpdateGlossaryTermOutputTypeDef(BaseModel):
    domainId: str
    glossaryId: str
    id: str
    longDescription: str
    name: str
    shortDescription: str
    status: GlossaryTermStatusType
    termRelations: TermRelationsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectMembershipInputRequestTypeDef(BaseModel):
    designation: UserDesignationType
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str

class DeleteProjectMembershipInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    member: MemberTypeDef
    projectIdentifier: str

class CreateProjectOutputTypeDef(BaseModel):
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

class GetProjectOutputTypeDef(BaseModel):
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

class ProjectSummaryTypeDef(BaseModel):
    createdBy: str
    domainId: str
    id: str
    name: str
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    failureReasons: Optional[List[ProjectDeletionErrorTypeDef]] = None
    projectStatus: Optional[ProjectStatusType] = None
    updatedAt: Optional[datetime] = None

class UpdateProjectOutputTypeDef(BaseModel):
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

class CreateSubscriptionTargetInputRequestTypeDef(BaseModel):
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

class CreateSubscriptionTargetOutputTypeDef(BaseModel):
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

class GetSubscriptionTargetOutputTypeDef(BaseModel):
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

class SubscriptionTargetSummaryTypeDef(BaseModel):
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

class UpdateSubscriptionTargetInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    applicableAssetTypes: Optional[Sequence[str]] = None
    authorizedPrincipals: Optional[Sequence[str]] = None
    manageAccessRole: Optional[str] = None
    name: Optional[str] = None
    provider: Optional[str] = None
    subscriptionTargetConfig: Optional[Sequence[SubscriptionTargetFormTypeDef]] = None

class UpdateSubscriptionTargetOutputTypeDef(BaseModel):
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

class DataProductSummaryTypeDef(BaseModel):
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

class DataSourceRunSummaryTypeDef(BaseModel):
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

class GetDataSourceRunOutputTypeDef(BaseModel):
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

class StartDataSourceRunOutputTypeDef(BaseModel):
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

class DeploymentTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    deploymentStatus: Optional[DeploymentStatusType] = None
    deploymentType: Optional[DeploymentTypeType] = None
    failureReason: Optional[EnvironmentErrorTypeDef] = None
    isDeploymentComplete: Optional[bool] = None
    messages: Optional[List[str]] = None

class ListDomainsOutputTypeDef(BaseModel):
    items: List[DomainSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentBlueprintConfigurationsOutputTypeDef(BaseModel):
    items: List[EnvironmentBlueprintConfigurationItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentProfilesOutputTypeDef(BaseModel):
    items: List[EnvironmentProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEnvironmentsOutputTypeDef(BaseModel):
    items: List[EnvironmentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribedAssetTypeDef(BaseModel):
    assetId: str
    assetRevision: str
    status: SubscriptionGrantStatusType
    failureCause: Optional[FailureCauseTypeDef] = None
    failureTimestamp: Optional[datetime] = None
    grantedTimestamp: Optional[datetime] = None
    targetName: Optional[str] = None

class UpdateSubscriptionGrantStatusInputRequestTypeDef(BaseModel):
    assetIdentifier: str
    domainIdentifier: str
    identifier: str
    status: SubscriptionGrantStatusType
    failureCause: Optional[FailureCauseTypeDef] = None
    targetName: Optional[str] = None

class FilterClauseTypeDef(BaseModel):
    and: Optional[Sequence[Dict[str, Any]]] = None
    filter: Optional[FilterTypeDef] = None
    or: Optional[Sequence[Dict[str, Any]]] = None

class RelationalFilterConfigurationOutputTypeDef(BaseModel):
    databaseName: str
    filterExpressions: Optional[List[FilterExpressionTypeDef]] = None
    schemaName: Optional[str] = None

class RelationalFilterConfigurationTypeDef(BaseModel):
    databaseName: str
    filterExpressions: Optional[Sequence[FilterExpressionTypeDef]] = None
    schemaName: Optional[str] = None

class FormTypeDataTypeDef(BaseModel):
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

class GetFormTypeOutputTypeDef(BaseModel):
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

class GetLineageNodeInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    eventTimestamp: Optional[TimestampTypeDef] = None

class ListLineageNodeHistoryInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[TimestampTypeDef] = None
    eventTimestampLTE: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None

class ListNotificationsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    type: NotificationTypeType
    afterTimestamp: Optional[TimestampTypeDef] = None
    beforeTimestamp: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    subjects: Optional[Sequence[str]] = None
    taskStatus: Optional[TaskStatusType] = None

class ListTimeSeriesDataPointsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startedAt: Optional[TimestampTypeDef] = None

class TimeSeriesDataPointFormInputTypeDef(BaseModel):
    formName: str
    timestamp: TimestampTypeDef
    typeIdentifier: str
    content: Optional[str] = None
    typeRevision: Optional[str] = None

class GetLineageNodeOutputTypeDef(BaseModel):
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

class GetMetadataGenerationRunOutputTypeDef(BaseModel):
    createdAt: datetime
    createdBy: str
    domainId: str
    id: str
    owningProjectId: str
    status: MetadataGenerationRunStatusType
    target: MetadataGenerationRunTargetTypeDef
    type: Literal["BUSINESS_DESCRIPTIONS"]
    ResponseMetadata: ResponseMetadataTypeDef

class MetadataGenerationRunItemTypeDef(BaseModel):
    domainId: str
    id: str
    owningProjectId: str
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    status: Optional[MetadataGenerationRunStatusType] = None
    target: Optional[MetadataGenerationRunTargetTypeDef] = None
    type: Optional[Literal["BUSINESS_DESCRIPTIONS"]] = None

class StartMetadataGenerationRunInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    owningProjectIdentifier: str
    target: MetadataGenerationRunTargetTypeDef
    type: Literal["BUSINESS_DESCRIPTIONS"]
    clientToken: Optional[str] = None

class GetTimeSeriesDataPointOutputTypeDef(BaseModel):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    form: TimeSeriesDataPointFormOutputTypeDef
    formName: str
    ResponseMetadata: ResponseMetadataTypeDef

class PostTimeSeriesDataPointsOutputTypeDef(BaseModel):
    domainId: str
    entityId: str
    entityType: TimeSeriesEntityTypeType
    forms: List[TimeSeriesDataPointFormOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlueSelfGrantStatusOutputTypeDef(BaseModel):
    selfGrantStatusDetails: List[SelfGrantStatusDetailTypeDef]

class RedshiftSelfGrantStatusOutputTypeDef(BaseModel):
    selfGrantStatusDetails: List[SelfGrantStatusDetailTypeDef]

class GrantedEntityInputTypeDef(BaseModel):
    listing: Optional[ListingRevisionInputTypeDef] = None

class GrantedEntityTypeDef(BaseModel):
    listing: Optional[ListingRevisionTypeDef] = None

class SearchGroupProfilesOutputTypeDef(BaseModel):
    items: List[GroupProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListLineageNodeHistoryOutputTypeDef(BaseModel):
    nextToken: str
    nodes: List[LineageNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    status: Optional[DataAssetActivityStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef(BaseModel):
    dataSourceIdentifier: str
    domainIdentifier: str
    status: Optional[DataSourceRunStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesInputListDataSourcesPaginateTypeDef(BaseModel):
    domainIdentifier: str
    projectIdentifier: str
    environmentIdentifier: Optional[str] = None
    name: Optional[str] = None
    status: Optional[DataSourceStatusType] = None
    type: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsInputListDomainsPaginateTypeDef(BaseModel):
    status: Optional[DomainStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentActionsInputListEnvironmentActionsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    managed: Optional[bool] = None
    name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef(BaseModel):
    domainIdentifier: str
    awsAccountId: Optional[str] = None
    awsAccountRegion: Optional[str] = None
    environmentBlueprintIdentifier: Optional[str] = None
    name: Optional[str] = None
    projectIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnvironmentsInputListEnvironmentsPaginateTypeDef(BaseModel):
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

class ListLineageNodeHistoryInputListLineageNodeHistoryPaginateTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    direction: Optional[EdgeDirectionType] = None
    eventTimestampGTE: Optional[TimestampTypeDef] = None
    eventTimestampLTE: Optional[TimestampTypeDef] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetadataGenerationRunsInputListMetadataGenerationRunsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    status: Optional[MetadataGenerationRunStatusType] = None
    type: Optional[Literal["BUSINESS_DESCRIPTIONS"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationsInputListNotificationsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    type: NotificationTypeType
    afterTimestamp: Optional[TimestampTypeDef] = None
    beforeTimestamp: Optional[TimestampTypeDef] = None
    subjects: Optional[Sequence[str]] = None
    taskStatus: Optional[TaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    projectIdentifier: str
    sortBy: Optional[Literal["NAME"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsInputListProjectsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    groupIdentifier: Optional[str] = None
    name: Optional[str] = None
    userIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    environmentId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    subscribedListingId: Optional[str] = None
    subscriptionId: Optional[str] = None
    subscriptionTargetId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionRequestStatusType] = None
    subscribedListingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubscriptionsInputListSubscriptionsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    approverProjectId: Optional[str] = None
    owningProjectId: Optional[str] = None
    sortBy: Optional[SortKeyType] = None
    sortOrder: Optional[SortOrderType] = None
    status: Optional[SubscriptionStatusType] = None
    subscribedListingId: Optional[str] = None
    subscriptionRequestIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTimeSeriesDataPointsInputListTimeSeriesDataPointsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    formName: str
    endedAt: Optional[TimestampTypeDef] = None
    startedAt: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef(BaseModel):
    domainIdentifier: str
    groupType: GroupSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchUserProfilesInputSearchUserProfilesPaginateTypeDef(BaseModel):
    domainIdentifier: str
    userType: UserSearchTypeType
    searchText: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MemberDetailsTypeDef(BaseModel):
    group: Optional[GroupDetailsTypeDef] = None
    user: Optional[UserDetailsTypeDef] = None

class TopicTypeDef(BaseModel):
    resource: NotificationResourceTypeDef
    role: NotificationRoleType
    subject: str

class RedshiftStorageTypeDef(BaseModel):
    redshiftClusterSource: Optional[RedshiftClusterStorageTypeDef] = None
    redshiftServerlessSource: Optional[RedshiftServerlessStorageTypeDef] = None

class RejectPredictionsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    clientToken: Optional[str] = None
    rejectChoices: Optional[Sequence[RejectChoiceTypeDef]] = None
    rejectRule: Optional[RejectRuleTypeDef] = None
    revision: Optional[str] = None

class SearchInputRequestTypeDef(BaseModel):
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

class SearchListingsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional["FilterClauseTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None

class SearchTypesInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional["FilterClauseTypeDef"] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None

class UserProfileDetailsTypeDef(BaseModel):
    iam: Optional[IamUserProfileDetailsTypeDef] = None
    sso: Optional[SsoUserProfileDetailsTypeDef] = None

class SubscribedPrincipalInputTypeDef(BaseModel):
    project: Optional[SubscribedProjectInputTypeDef] = None

class SubscribedPrincipalTypeDef(BaseModel):
    project: Optional[SubscribedProjectTypeDef] = None

class CreateEnvironmentActionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    name: str
    parameters: ActionParametersTypeDef
    description: Optional[str] = None

class CreateEnvironmentActionOutputTypeDef(BaseModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentActionSummaryTypeDef(BaseModel):
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    description: Optional[str] = None

class GetEnvironmentActionOutputTypeDef(BaseModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentActionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    identifier: str
    description: Optional[str] = None
    name: Optional[str] = None
    parameters: Optional[ActionParametersTypeDef] = None

class UpdateEnvironmentActionOutputTypeDef(BaseModel):
    description: str
    domainId: str
    environmentId: str
    id: str
    name: str
    parameters: ActionParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssetItemTypeDef(BaseModel):
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

class AssetListingItemTypeDef(BaseModel):
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

class ListingItemTypeDef(BaseModel):
    assetListing: Optional[AssetListingTypeDef] = None

class SubscribedListingItemTypeDef(BaseModel):
    assetListing: Optional[SubscribedAssetListingTypeDef] = None

class CreateAssetInputRequestTypeDef(BaseModel):
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

class CreateAssetOutputTypeDef(BaseModel):
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

class CreateAssetRevisionInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    identifier: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    formsInput: Optional[Sequence[FormInputTypeDef]] = None
    glossaryTerms: Optional[Sequence[str]] = None
    predictionConfiguration: Optional[PredictionConfigurationTypeDef] = None
    typeRevision: Optional[str] = None

class CreateAssetRevisionOutputTypeDef(BaseModel):
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

class EnvironmentBlueprintSummaryTypeDef(BaseModel):
    id: str
    name: str
    provider: str
    provisioningProperties: ProvisioningPropertiesTypeDef
    createdAt: Optional[datetime] = None
    description: Optional[str] = None
    updatedAt: Optional[datetime] = None

class GetEnvironmentBlueprintOutputTypeDef(BaseModel):
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

class ListDataSourceRunActivitiesOutputTypeDef(BaseModel):
    items: List[DataSourceRunActivityTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourcesOutputTypeDef(BaseModel):
    items: List[DataSourceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsOutputTypeDef(BaseModel):
    items: List[ProjectSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionTargetsOutputTypeDef(BaseModel):
    items: List[SubscriptionTargetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataSourceRunsOutputTypeDef(BaseModel):
    items: List[DataSourceRunSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentOutputTypeDef(BaseModel):
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

class GetEnvironmentOutputTypeDef(BaseModel):
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

class UpdateEnvironmentOutputTypeDef(BaseModel):
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

class SearchInputSearchPaginateTypeDef(BaseModel):
    domainIdentifier: str
    searchScope: InventorySearchScopeType
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClauseTypeDef] = None
    owningProjectIdentifier: Optional[str] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchListingsInputSearchListingsPaginateTypeDef(BaseModel):
    domainIdentifier: str
    additionalAttributes: Optional[Sequence[SearchOutputAdditionalAttributeType]] = None
    filters: Optional[FilterClauseTypeDef] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTypesInputSearchTypesPaginateTypeDef(BaseModel):
    domainIdentifier: str
    managed: bool
    searchScope: TypesSearchScopeType
    filters: Optional[FilterClauseTypeDef] = None
    searchIn: Optional[Sequence[SearchInItemTypeDef]] = None
    searchText: Optional[str] = None
    sort: Optional[SearchSortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GlueRunConfigurationOutputTypeDef(BaseModel):
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: Optional[str] = None
    autoImportDataQualityResult: Optional[bool] = None
    dataAccessRole: Optional[str] = None
    region: Optional[str] = None

class GlueRunConfigurationInputTypeDef(BaseModel):
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationTypeDef]
    autoImportDataQualityResult: Optional[bool] = None
    dataAccessRole: Optional[str] = None

class SearchTypesResultItemTypeDef(BaseModel):
    assetTypeItem: Optional[AssetTypeItemTypeDef] = None
    formTypeItem: Optional[FormTypeDataTypeDef] = None
    lineageNodeTypeItem: Optional[LineageNodeTypeItemTypeDef] = None

class PostTimeSeriesDataPointsInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    entityIdentifier: str
    entityType: TimeSeriesEntityTypeType
    forms: Sequence[TimeSeriesDataPointFormInputTypeDef]
    clientToken: Optional[str] = None

class ListMetadataGenerationRunsOutputTypeDef(BaseModel):
    items: List[MetadataGenerationRunItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SelfGrantStatusOutputTypeDef(BaseModel):
    glueSelfGrantStatus: Optional[GlueSelfGrantStatusOutputTypeDef] = None
    redshiftSelfGrantStatus: Optional[RedshiftSelfGrantStatusOutputTypeDef] = None

class CreateSubscriptionGrantInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    environmentIdentifier: str
    grantedEntity: GrantedEntityInputTypeDef
    subscriptionTargetIdentifier: str
    assetTargetNames: Optional[Sequence[AssetTargetNameMapTypeDef]] = None
    clientToken: Optional[str] = None

class CreateSubscriptionGrantOutputTypeDef(BaseModel):
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

class DeleteSubscriptionGrantOutputTypeDef(BaseModel):
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

class GetSubscriptionGrantOutputTypeDef(BaseModel):
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

class SubscriptionGrantSummaryTypeDef(BaseModel):
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

class UpdateSubscriptionGrantStatusOutputTypeDef(BaseModel):
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

class ProjectMemberTypeDef(BaseModel):
    designation: UserDesignationType
    memberDetails: MemberDetailsTypeDef

class NotificationOutputTypeDef(BaseModel):
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

class RedshiftRunConfigurationInputTypeDef(BaseModel):
    redshiftCredentialConfiguration: RedshiftCredentialConfigurationTypeDef
    redshiftStorage: RedshiftStorageTypeDef
    relationalFilterConfigurations: Sequence[RelationalFilterConfigurationTypeDef]
    dataAccessRole: Optional[str] = None

class RedshiftRunConfigurationOutputTypeDef(BaseModel):
    redshiftCredentialConfiguration: RedshiftCredentialConfigurationTypeDef
    redshiftStorage: RedshiftStorageTypeDef
    relationalFilterConfigurations: List[RelationalFilterConfigurationOutputTypeDef]
    accountId: Optional[str] = None
    dataAccessRole: Optional[str] = None
    region: Optional[str] = None

class CreateUserProfileOutputTypeDef(BaseModel):
    details: UserProfileDetailsTypeDef
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserProfileOutputTypeDef(BaseModel):
    details: UserProfileDetailsTypeDef
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserProfileOutputTypeDef(BaseModel):
    details: UserProfileDetailsTypeDef
    domainId: str
    id: str
    status: UserProfileStatusType
    type: UserProfileTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UserProfileSummaryTypeDef(BaseModel):
    details: Optional[UserProfileDetailsTypeDef] = None
    domainId: Optional[str] = None
    id: Optional[str] = None
    status: Optional[UserProfileStatusType] = None
    type: Optional[UserProfileTypeType] = None

class CreateSubscriptionRequestInputRequestTypeDef(BaseModel):
    domainIdentifier: str
    requestReason: str
    subscribedListings: Sequence[SubscribedListingInputTypeDef]
    subscribedPrincipals: Sequence[SubscribedPrincipalInputTypeDef]
    clientToken: Optional[str] = None

class ListEnvironmentActionsOutputTypeDef(BaseModel):
    items: List[EnvironmentActionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchInventoryResultItemTypeDef(BaseModel):
    assetItem: Optional[AssetItemTypeDef] = None
    dataProductItem: Optional[DataProductSummaryTypeDef] = None
    glossaryItem: Optional[GlossaryItemTypeDef] = None
    glossaryTermItem: Optional[GlossaryTermItemTypeDef] = None

class SearchResultItemTypeDef(BaseModel):
    assetListing: Optional[AssetListingItemTypeDef] = None

class GetListingOutputTypeDef(BaseModel):
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

class SubscribedListingTypeDef(BaseModel):
    description: str
    id: str
    item: SubscribedListingItemTypeDef
    name: str
    ownerProjectId: str
    ownerProjectName: Optional[str] = None
    revision: Optional[str] = None

class ListEnvironmentBlueprintsOutputTypeDef(BaseModel):
    items: List[EnvironmentBlueprintSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchTypesOutputTypeDef(BaseModel):
    items: List[SearchTypesResultItemTypeDef]
    nextToken: str
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionGrantsOutputTypeDef(BaseModel):
    items: List[SubscriptionGrantSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectMembershipsOutputTypeDef(BaseModel):
    members: List[ProjectMemberTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNotificationsOutputTypeDef(BaseModel):
    nextToken: str
    notifications: List[NotificationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceConfigurationInputTypeDef(BaseModel):
    glueRunConfiguration: Optional[GlueRunConfigurationInputTypeDef] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationInputTypeDef] = None

class DataSourceConfigurationOutputTypeDef(BaseModel):
    glueRunConfiguration: Optional[GlueRunConfigurationOutputTypeDef] = None
    redshiftRunConfiguration: Optional[RedshiftRunConfigurationOutputTypeDef] = None

class SearchUserProfilesOutputTypeDef(BaseModel):
    items: List[UserProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchOutputTypeDef(BaseModel):
    items: List[SearchInventoryResultItemTypeDef]
    nextToken: str
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class SearchListingsOutputTypeDef(BaseModel):
    items: List[SearchResultItemTypeDef]
    nextToken: str
    totalMatchCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptSubscriptionRequestOutputTypeDef(BaseModel):
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

class CancelSubscriptionOutputTypeDef(BaseModel):
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

class CreateSubscriptionRequestOutputTypeDef(BaseModel):
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

class GetSubscriptionOutputTypeDef(BaseModel):
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

class GetSubscriptionRequestDetailsOutputTypeDef(BaseModel):
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

class RejectSubscriptionRequestOutputTypeDef(BaseModel):
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

class RevokeSubscriptionOutputTypeDef(BaseModel):
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

class SubscriptionRequestSummaryTypeDef(BaseModel):
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

class SubscriptionSummaryTypeDef(BaseModel):
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

class UpdateSubscriptionRequestOutputTypeDef(BaseModel):
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

class CreateDataSourceInputRequestTypeDef(BaseModel):
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

class UpdateDataSourceInputRequestTypeDef(BaseModel):
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

class CreateDataSourceOutputTypeDef(BaseModel):
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

class DeleteDataSourceOutputTypeDef(BaseModel):
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

class GetDataSourceOutputTypeDef(BaseModel):
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

class UpdateDataSourceOutputTypeDef(BaseModel):
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

class ListSubscriptionRequestsOutputTypeDef(BaseModel):
    items: List[SubscriptionRequestSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscriptionsOutputTypeDef(BaseModel):
    items: List[SubscriptionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

