from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.eks.eks_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessConfigResponse(BaseValidatorModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None


class AccessEntry(BaseValidatorModel):
    clusterName: Optional[str] = None
    principalArn: Optional[str] = None
    kubernetesGroups: Optional[List[str]] = None
    accessEntryArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    username: Optional[str] = None
    type: Optional[str] = None


class AccessPolicy(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


class AccessScopeOutput(BaseValidatorModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[List[str]] = None


class AccessScope(BaseValidatorModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[List[str]] = None


class AddonCompatibilityDetail(BaseValidatorModel):
    name: Optional[str] = None
    compatibleVersions: Optional[List[str]] = None


class AddonIssue(BaseValidatorModel):
    code: Optional[AddonIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class MarketplaceInformation(BaseValidatorModel):
    productId: Optional[str] = None
    productUrl: Optional[str] = None


class AddonPodIdentityAssociations(BaseValidatorModel):
    serviceAccount: str
    roleArn: str


class AddonPodIdentityConfiguration(BaseValidatorModel):
    serviceAccount: Optional[str] = None
    recommendedManagedPolicies: Optional[List[str]] = None


class Compatibility(BaseValidatorModel):
    clusterVersion: Optional[str] = None
    platformVersions: Optional[List[str]] = None
    defaultVersion: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class OidcIdentityProviderConfigRequest(BaseValidatorModel):
    identityProviderConfigName: str
    issuerUrl: str
    clientId: str
    usernameClaim: Optional[str] = None
    usernamePrefix: Optional[str] = None
    groupsClaim: Optional[str] = None
    groupsPrefix: Optional[str] = None
    requiredClaims: Optional[Dict[str, str]] = None


class AutoScalingGroup(BaseValidatorModel):
    name: Optional[str] = None


class BlockStorage(BaseValidatorModel):
    enabled: Optional[bool] = None


class Certificate(BaseValidatorModel):
    data: Optional[str] = None


class ClientStat(BaseValidatorModel):
    userAgent: Optional[str] = None
    numberOfRequestsLast30Days: Optional[int] = None
    lastRequestTime: Optional[datetime] = None


class ClusterIssue(BaseValidatorModel):
    code: Optional[ClusterIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class ComputeConfigResponse(BaseValidatorModel):
    enabled: Optional[bool] = None
    nodePools: Optional[List[str]] = None
    nodeRoleArn: Optional[str] = None


class ConnectorConfigResponse(BaseValidatorModel):
    activationId: Optional[str] = None
    activationCode: Optional[str] = None
    activationExpiry: Optional[datetime] = None
    provider: Optional[str] = None
    roleArn: Optional[str] = None


class UpgradePolicyResponse(BaseValidatorModel):
    supportType: Optional[SupportTypeType] = None


class VpcConfigResponse(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    clusterSecurityGroupId: Optional[str] = None
    vpcId: Optional[str] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[List[str]] = None


class ZonalShiftConfigResponse(BaseValidatorModel):
    enabled: Optional[bool] = None


class ClusterVersionInformation(BaseValidatorModel):
    clusterVersion: Optional[str] = None
    clusterType: Optional[str] = None
    defaultPlatformVersion: Optional[str] = None
    defaultVersion: Optional[bool] = None
    releaseDate: Optional[datetime] = None
    endOfStandardSupportDate: Optional[datetime] = None
    endOfExtendedSupportDate: Optional[datetime] = None
    status: Optional[ClusterVersionStatusType] = None
    versionStatus: Optional[VersionStatusType] = None
    kubernetesPatchVersion: Optional[str] = None


class ComputeConfigRequest(BaseValidatorModel):
    enabled: Optional[bool] = None
    nodePools: Optional[List[str]] = None
    nodeRoleArn: Optional[str] = None


class ConnectorConfigRequest(BaseValidatorModel):
    roleArn: str
    provider: ConnectorConfigProviderType


class ControlPlanePlacementRequest(BaseValidatorModel):
    groupName: Optional[str] = None


class ControlPlanePlacementResponse(BaseValidatorModel):
    groupName: Optional[str] = None


class CreateAccessConfigRequest(BaseValidatorModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None


# This class is the input for the 'create_access_entry' function.
class CreateAccessEntryRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None
    type: Optional[str] = None


class UpgradePolicyRequest(BaseValidatorModel):
    supportType: Optional[SupportTypeType] = None


class VpcConfigRequest(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[List[str]] = None


class ZonalShiftConfigRequest(BaseValidatorModel):
    enabled: Optional[bool] = None


class EksAnywhereSubscriptionTerm(BaseValidatorModel):
    duration: Optional[int] = None
    unit: Optional[Literal['MONTHS']] = None


class LaunchTemplateSpecification(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[str] = None
    id: Optional[str] = None


class NodeRepairConfig(BaseValidatorModel):
    enabled: Optional[bool] = None


class NodegroupScalingConfig(BaseValidatorModel):
    minSize: Optional[int] = None
    maxSize: Optional[int] = None
    desiredSize: Optional[int] = None


class NodegroupUpdateConfig(BaseValidatorModel):
    maxUnavailable: Optional[int] = None
    maxUnavailablePercentage: Optional[int] = None
    updateStrategy: Optional[NodegroupUpdateStrategiesType] = None


class Taint(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None
    effect: Optional[TaintEffectType] = None


# This class is the input for the 'create_pod_identity_association' function.
class CreatePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    namespace: str
    serviceAccount: str
    roleArn: str
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class PodIdentityAssociation(BaseValidatorModel):
    clusterName: Optional[str] = None
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    roleArn: Optional[str] = None
    associationArn: Optional[str] = None
    associationId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    ownerArn: Optional[str] = None


class DeleteAccessEntryRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str


# This class is the input for the 'delete_addon' function.
class DeleteAddonRequest(BaseValidatorModel):
    clusterName: str
    addonName: str
    preserve: Optional[bool] = None


# This class is the input for the 'delete_cluster' function.
class DeleteClusterRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_eks_anywhere_subscription' function.
class DeleteEksAnywhereSubscriptionRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_fargate_profile' function.
class DeleteFargateProfileRequest(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str


# This class is the input for the 'delete_nodegroup' function.
class DeleteNodegroupRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str


# This class is the input for the 'delete_pod_identity_association' function.
class DeletePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    associationId: str


# This class is the input for the 'deregister_cluster' function.
class DeregisterClusterRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'describe_access_entry' function.
class DescribeAccessEntryRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str


# This class is the input for the 'describe_addon_configuration' function.
class DescribeAddonConfigurationRequest(BaseValidatorModel):
    addonName: str
    addonVersion: str


# This class is the input for the 'describe_addon' function.
class DescribeAddonRequest(BaseValidatorModel):
    clusterName: str
    addonName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_addon_versions' function.
class DescribeAddonVersionsRequest(BaseValidatorModel):
    kubernetesVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    addonName: Optional[str] = None
    types: Optional[List[str]] = None
    publishers: Optional[List[str]] = None
    owners: Optional[List[str]] = None


# This class is the input for the 'describe_cluster' function.
class DescribeClusterRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'describe_cluster_versions' function.
class DescribeClusterVersionsRequest(BaseValidatorModel):
    clusterType: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    defaultOnly: Optional[bool] = None
    includeAll: Optional[bool] = None
    clusterVersions: Optional[List[str]] = None
    status: Optional[ClusterVersionStatusType] = None
    versionStatus: Optional[VersionStatusType] = None


# This class is the input for the 'describe_eks_anywhere_subscription' function.
class DescribeEksAnywhereSubscriptionRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'describe_fargate_profile' function.
class DescribeFargateProfileRequest(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str


class IdentityProviderConfig(BaseValidatorModel):
    type: str
    name: str


# This class is the input for the 'describe_insight' function.
class DescribeInsightRequest(BaseValidatorModel):
    clusterName: str
    id: str


# This class is the input for the 'describe_nodegroup' function.
class DescribeNodegroupRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str


# This class is the input for the 'describe_pod_identity_association' function.
class DescribePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    associationId: str


# This class is the input for the 'describe_update' function.
class DescribeUpdateRequest(BaseValidatorModel):
    name: str
    updateId: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None


class DisassociateAccessPolicyRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    policyArn: str


class License(BaseValidatorModel):
    id: Optional[str] = None
    token: Optional[str] = None


class ElasticLoadBalancing(BaseValidatorModel):
    enabled: Optional[bool] = None


class Provider(BaseValidatorModel):
    keyArn: Optional[str] = None


class ErrorDetail(BaseValidatorModel):
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class FargateProfileIssue(BaseValidatorModel):
    code: Optional[FargateProfileIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class FargateProfileSelectorOutput(BaseValidatorModel):
    namespace: Optional[str] = None
    labels: Optional[Dict[str, str]] = None


class FargateProfileSelector(BaseValidatorModel):
    namespace: Optional[str] = None
    labels: Optional[Dict[str, str]] = None


class OidcIdentityProviderConfig(BaseValidatorModel):
    identityProviderConfigName: Optional[str] = None
    identityProviderConfigArn: Optional[str] = None
    clusterName: Optional[str] = None
    issuerUrl: Optional[str] = None
    clientId: Optional[str] = None
    usernameClaim: Optional[str] = None
    usernamePrefix: Optional[str] = None
    groupsClaim: Optional[str] = None
    groupsPrefix: Optional[str] = None
    requiredClaims: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    status: Optional[ConfigStatusType] = None


class OIDC(BaseValidatorModel):
    issuer: Optional[str] = None


class InsightStatus(BaseValidatorModel):
    status: Optional[InsightStatusValueType] = None
    reason: Optional[str] = None


class InsightsFilter(BaseValidatorModel):
    categories: Optional[List[Literal['UPGRADE_READINESS']]] = None
    kubernetesVersions: Optional[List[str]] = None
    statuses: Optional[List[InsightStatusValueType]] = None


class Issue(BaseValidatorModel):
    code: Optional[NodegroupIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


# This class is the input for the 'list_access_entries' function.
class ListAccessEntriesRequest(BaseValidatorModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_access_policies' function.
class ListAccessPoliciesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_addons' function.
class ListAddonsRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_associated_access_policies' function.
class ListAssociatedAccessPoliciesRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_clusters' function.
class ListClustersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    include: Optional[List[str]] = None


# This class is the input for the 'list_eks_anywhere_subscriptions' function.
class ListEksAnywhereSubscriptionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeStatus: Optional[List[EksAnywhereSubscriptionStatusType]] = None


# This class is the input for the 'list_fargate_profiles' function.
class ListFargateProfilesRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_identity_provider_configs' function.
class ListIdentityProviderConfigsRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_nodegroups' function.
class ListNodegroupsRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_pod_identity_associations' function.
class ListPodIdentityAssociationsRequest(BaseValidatorModel):
    clusterName: str
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PodIdentityAssociationSummary(BaseValidatorModel):
    clusterName: Optional[str] = None
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    associationArn: Optional[str] = None
    associationId: Optional[str] = None
    ownerArn: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_updates' function.
class ListUpdatesRequest(BaseValidatorModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LogSetupOutput(BaseValidatorModel):
    types: Optional[List[LogTypeType]] = None
    enabled: Optional[bool] = None


class LogSetup(BaseValidatorModel):
    types: Optional[List[LogTypeType]] = None
    enabled: Optional[bool] = None


class RemoteAccessConfigOutput(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[List[str]] = None


class RemoteAccessConfig(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[List[str]] = None


class RemoteNodeNetworkOutput(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class RemotePodNetworkOutput(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class RemoteNodeNetwork(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class RemotePodNetwork(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateAccessConfigRequest(BaseValidatorModel):
    authenticationMode: Optional[AuthenticationModeType] = None


# This class is the input for the 'update_access_entry' function.
class UpdateAccessEntryRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[List[str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None


# This class is the input for the 'update_cluster_version' function.
class UpdateClusterVersionRequest(BaseValidatorModel):
    name: str
    version: str
    clientRequestToken: Optional[str] = None


# This class is the input for the 'update_eks_anywhere_subscription' function.
class UpdateEksAnywhereSubscriptionRequest(BaseValidatorModel):
    id: str
    autoRenew: bool
    clientRequestToken: Optional[str] = None


class UpdateLabelsPayload(BaseValidatorModel):
    addOrUpdateLabels: Optional[Dict[str, str]] = None
    removeLabels: Optional[List[str]] = None


class UpdateParam(BaseValidatorModel):
    type: Optional[UpdateParamTypeType] = None
    value: Optional[str] = None


# This class is the input for the 'update_pod_identity_association' function.
class UpdatePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    associationId: str
    roleArn: Optional[str] = None
    clientRequestToken: Optional[str] = None


class AssociatedAccessPolicy(BaseValidatorModel):
    policyArn: Optional[str] = None
    accessScope: Optional[AccessScopeOutput] = None
    associatedAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None

AccessScopeUnion = Union[AccessScope, AccessScopeOutput]


class AddonHealth(BaseValidatorModel):
    issues: Optional[List[AddonIssue]] = None


# This class is the input for the 'create_addon' function.
class CreateAddonRequest(BaseValidatorModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[List[AddonPodIdentityAssociations]] = None


# This class is the input for the 'update_addon' function.
class UpdateAddonRequest(BaseValidatorModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[List[AddonPodIdentityAssociations]] = None


class AddonVersionInfo(BaseValidatorModel):
    addonVersion: Optional[str] = None
    architecture: Optional[List[str]] = None
    computeTypes: Optional[List[str]] = None
    compatibilities: Optional[List[Compatibility]] = None
    requiresConfiguration: Optional[bool] = None
    requiresIamPermissions: Optional[bool] = None


# This class is the output for the 'create_access_entry' function.
class CreateAccessEntryResponse(BaseValidatorModel):
    accessEntry: AccessEntry
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_access_entry' function.
class DescribeAccessEntryResponse(BaseValidatorModel):
    accessEntry: AccessEntry
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_addon_configuration' function.
class DescribeAddonConfigurationResponse(BaseValidatorModel):
    addonName: str
    addonVersion: str
    configurationSchema: str
    podIdentityConfiguration: List[AddonPodIdentityConfiguration]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_access_entries' function.
class ListAccessEntriesResponse(BaseValidatorModel):
    accessEntries: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_access_policies' function.
class ListAccessPoliciesResponse(BaseValidatorModel):
    accessPolicies: List[AccessPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_addons' function.
class ListAddonsResponse(BaseValidatorModel):
    addons: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_clusters' function.
class ListClustersResponse(BaseValidatorModel):
    clusters: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_fargate_profiles' function.
class ListFargateProfilesResponse(BaseValidatorModel):
    fargateProfileNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_nodegroups' function.
class ListNodegroupsResponse(BaseValidatorModel):
    nodegroups: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_updates' function.
class ListUpdatesResponse(BaseValidatorModel):
    updateIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_access_entry' function.
class UpdateAccessEntryResponse(BaseValidatorModel):
    accessEntry: AccessEntry
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_identity_provider_config' function.
class AssociateIdentityProviderConfigRequest(BaseValidatorModel):
    clusterName: str
    oidc: OidcIdentityProviderConfigRequest
    tags: Optional[Dict[str, str]] = None
    clientRequestToken: Optional[str] = None


class NodegroupResources(BaseValidatorModel):
    autoScalingGroups: Optional[List[AutoScalingGroup]] = None
    remoteAccessSecurityGroup: Optional[str] = None


class StorageConfigRequest(BaseValidatorModel):
    blockStorage: Optional[BlockStorage] = None


class StorageConfigResponse(BaseValidatorModel):
    blockStorage: Optional[BlockStorage] = None


class DeprecationDetail(BaseValidatorModel):
    usage: Optional[str] = None
    replacedWith: Optional[str] = None
    stopServingVersion: Optional[str] = None
    startServingReplacementVersion: Optional[str] = None
    clientStats: Optional[List[ClientStat]] = None


class ClusterHealth(BaseValidatorModel):
    issues: Optional[List[ClusterIssue]] = None


# This class is the output for the 'describe_cluster_versions' function.
class DescribeClusterVersionsResponse(BaseValidatorModel):
    clusterVersions: List[ClusterVersionInformation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'register_cluster' function.
class RegisterClusterRequest(BaseValidatorModel):
    name: str
    connectorConfig: ConnectorConfigRequest
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class OutpostConfigRequest(BaseValidatorModel):
    outpostArns: List[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementRequest] = None


class OutpostConfigResponse(BaseValidatorModel):
    outpostArns: List[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementResponse] = None


# This class is the input for the 'create_eks_anywhere_subscription' function.
class CreateEksAnywhereSubscriptionRequest(BaseValidatorModel):
    name: str
    term: EksAnywhereSubscriptionTerm
    licenseQuantity: Optional[int] = None
    licenseType: Optional[Literal['Cluster']] = None
    autoRenew: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_nodegroup_version' function.
class UpdateNodegroupVersionRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    version: Optional[str] = None
    releaseVersion: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecification] = None
    force: Optional[bool] = None
    clientRequestToken: Optional[str] = None


class UpdateTaintsPayload(BaseValidatorModel):
    addOrUpdateTaints: Optional[List[Taint]] = None
    removeTaints: Optional[List[Taint]] = None


# This class is the output for the 'create_pod_identity_association' function.
class CreatePodIdentityAssociationResponse(BaseValidatorModel):
    association: PodIdentityAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_pod_identity_association' function.
class DeletePodIdentityAssociationResponse(BaseValidatorModel):
    association: PodIdentityAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_pod_identity_association' function.
class DescribePodIdentityAssociationResponse(BaseValidatorModel):
    association: PodIdentityAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pod_identity_association' function.
class UpdatePodIdentityAssociationResponse(BaseValidatorModel):
    association: PodIdentityAssociation
    ResponseMetadata: ResponseMetadata


class DescribeAddonRequestWaitExtra(BaseValidatorModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeAddonRequestWait(BaseValidatorModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClusterRequestWaitExtra(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClusterRequestWait(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeFargateProfileRequestWaitExtra(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeFargateProfileRequestWait(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNodegroupRequestWaitExtra(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNodegroupRequestWait(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeAddonVersionsRequestPaginate(BaseValidatorModel):
    kubernetesVersion: Optional[str] = None
    addonName: Optional[str] = None
    types: Optional[List[str]] = None
    publishers: Optional[List[str]] = None
    owners: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterVersionsRequestPaginate(BaseValidatorModel):
    clusterType: Optional[str] = None
    defaultOnly: Optional[bool] = None
    includeAll: Optional[bool] = None
    clusterVersions: Optional[List[str]] = None
    status: Optional[ClusterVersionStatusType] = None
    versionStatus: Optional[VersionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccessEntriesRequestPaginate(BaseValidatorModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccessPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAddonsRequestPaginate(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociatedAccessPoliciesRequestPaginate(BaseValidatorModel):
    clusterName: str
    principalArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersRequestPaginate(BaseValidatorModel):
    include: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEksAnywhereSubscriptionsRequestPaginate(BaseValidatorModel):
    includeStatus: Optional[List[EksAnywhereSubscriptionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFargateProfilesRequestPaginate(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIdentityProviderConfigsRequestPaginate(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNodegroupsRequestPaginate(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPodIdentityAssociationsRequestPaginate(BaseValidatorModel):
    clusterName: str
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUpdatesRequestPaginate(BaseValidatorModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_identity_provider_config' function.
class DescribeIdentityProviderConfigRequest(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfig


# This class is the input for the 'disassociate_identity_provider_config' function.
class DisassociateIdentityProviderConfigRequest(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfig
    clientRequestToken: Optional[str] = None


# This class is the output for the 'list_identity_provider_configs' function.
class ListIdentityProviderConfigsResponse(BaseValidatorModel):
    identityProviderConfigs: List[IdentityProviderConfig]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EksAnywhereSubscription(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    effectiveDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    licenseQuantity: Optional[int] = None
    licenseType: Optional[Literal['Cluster']] = None
    term: Optional[EksAnywhereSubscriptionTerm] = None
    status: Optional[str] = None
    autoRenew: Optional[bool] = None
    licenseArns: Optional[List[str]] = None
    licenses: Optional[List[License]] = None
    tags: Optional[Dict[str, str]] = None


class KubernetesNetworkConfigRequest(BaseValidatorModel):
    serviceIpv4Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None
    elasticLoadBalancing: Optional[ElasticLoadBalancing] = None


class KubernetesNetworkConfigResponse(BaseValidatorModel):
    serviceIpv4Cidr: Optional[str] = None
    serviceIpv6Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None
    elasticLoadBalancing: Optional[ElasticLoadBalancing] = None


class EncryptionConfigOutput(BaseValidatorModel):
    resources: Optional[List[str]] = None
    provider: Optional[Provider] = None


class EncryptionConfig(BaseValidatorModel):
    resources: Optional[List[str]] = None
    provider: Optional[Provider] = None


class FargateProfileHealth(BaseValidatorModel):
    issues: Optional[List[FargateProfileIssue]] = None

FargateProfileSelectorUnion = Union[FargateProfileSelector, FargateProfileSelectorOutput]


class IdentityProviderConfigResponse(BaseValidatorModel):
    oidc: Optional[OidcIdentityProviderConfig] = None


class Identity(BaseValidatorModel):
    oidc: Optional[OIDC] = None


class InsightResourceDetail(BaseValidatorModel):
    insightStatus: Optional[InsightStatus] = None
    kubernetesResourceUri: Optional[str] = None
    arn: Optional[str] = None


class InsightSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    category: Optional[Literal['UPGRADE_READINESS']] = None
    kubernetesVersion: Optional[str] = None
    lastRefreshTime: Optional[datetime] = None
    lastTransitionTime: Optional[datetime] = None
    description: Optional[str] = None
    insightStatus: Optional[InsightStatus] = None


class ListInsightsRequestPaginate(BaseValidatorModel):
    clusterName: str
    filter: Optional[InsightsFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_insights' function.
class ListInsightsRequest(BaseValidatorModel):
    clusterName: str
    filter: Optional[InsightsFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NodegroupHealth(BaseValidatorModel):
    issues: Optional[List[Issue]] = None


# This class is the output for the 'list_pod_identity_associations' function.
class ListPodIdentityAssociationsResponse(BaseValidatorModel):
    associations: List[PodIdentityAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LoggingOutput(BaseValidatorModel):
    clusterLogging: Optional[List[LogSetupOutput]] = None


class Logging(BaseValidatorModel):
    clusterLogging: Optional[List[LogSetup]] = None

RemoteAccessConfigUnion = Union[RemoteAccessConfig, RemoteAccessConfigOutput]


class RemoteNetworkConfigResponse(BaseValidatorModel):
    remoteNodeNetworks: Optional[List[RemoteNodeNetworkOutput]] = None
    remotePodNetworks: Optional[List[RemotePodNetworkOutput]] = None

RemoteNodeNetworkUnion = Union[RemoteNodeNetwork, RemoteNodeNetworkOutput]

RemotePodNetworkUnion = Union[RemotePodNetwork, RemotePodNetworkOutput]


class Update(BaseValidatorModel):
    id: Optional[str] = None
    status: Optional[UpdateStatusType] = None
    type: Optional[UpdateTypeType] = None
    params: Optional[List[UpdateParam]] = None
    createdAt: Optional[datetime] = None
    errors: Optional[List[ErrorDetail]] = None


# This class is the output for the 'associate_access_policy' function.
class AssociateAccessPolicyResponse(BaseValidatorModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicy: AssociatedAccessPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_associated_access_policies' function.
class ListAssociatedAccessPoliciesResponse(BaseValidatorModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicies: List[AssociatedAccessPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'associate_access_policy' function.
class AssociateAccessPolicyRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    policyArn: str
    accessScope: AccessScopeUnion


class Addon(BaseValidatorModel):
    addonName: Optional[str] = None
    clusterName: Optional[str] = None
    status: Optional[AddonStatusType] = None
    addonVersion: Optional[str] = None
    health: Optional[AddonHealth] = None
    addonArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    serviceAccountRoleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    publisher: Optional[str] = None
    owner: Optional[str] = None
    marketplaceInformation: Optional[MarketplaceInformation] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[List[str]] = None


class AddonInfo(BaseValidatorModel):
    addonName: Optional[str] = None
    type: Optional[str] = None
    addonVersions: Optional[List[AddonVersionInfo]] = None
    publisher: Optional[str] = None
    owner: Optional[str] = None
    marketplaceInformation: Optional[MarketplaceInformation] = None


class InsightCategorySpecificSummary(BaseValidatorModel):
    deprecationDetails: Optional[List[DeprecationDetail]] = None
    addonCompatibilityDetails: Optional[List[AddonCompatibilityDetail]] = None


# This class is the input for the 'update_nodegroup_config' function.
class UpdateNodegroupConfigRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    labels: Optional[UpdateLabelsPayload] = None
    taints: Optional[UpdateTaintsPayload] = None
    scalingConfig: Optional[NodegroupScalingConfig] = None
    updateConfig: Optional[NodegroupUpdateConfig] = None
    nodeRepairConfig: Optional[NodeRepairConfig] = None
    clientRequestToken: Optional[str] = None


# This class is the output for the 'create_eks_anywhere_subscription' function.
class CreateEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_eks_anywhere_subscription' function.
class DeleteEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_eks_anywhere_subscription' function.
class DescribeEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_eks_anywhere_subscriptions' function.
class ListEksAnywhereSubscriptionsResponse(BaseValidatorModel):
    subscriptions: List[EksAnywhereSubscription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_eks_anywhere_subscription' function.
class UpdateEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata

EncryptionConfigUnion = Union[EncryptionConfig, EncryptionConfigOutput]


class FargateProfile(BaseValidatorModel):
    fargateProfileName: Optional[str] = None
    fargateProfileArn: Optional[str] = None
    clusterName: Optional[str] = None
    createdAt: Optional[datetime] = None
    podExecutionRoleArn: Optional[str] = None
    subnets: Optional[List[str]] = None
    selectors: Optional[List[FargateProfileSelectorOutput]] = None
    status: Optional[FargateProfileStatusType] = None
    tags: Optional[Dict[str, str]] = None
    health: Optional[FargateProfileHealth] = None


# This class is the input for the 'create_fargate_profile' function.
class CreateFargateProfileRequest(BaseValidatorModel):
    fargateProfileName: str
    clusterName: str
    podExecutionRoleArn: str
    subnets: Optional[List[str]] = None
    selectors: Optional[List[FargateProfileSelectorUnion]] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_identity_provider_config' function.
class DescribeIdentityProviderConfigResponse(BaseValidatorModel):
    identityProviderConfig: IdentityProviderConfigResponse
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_insights' function.
class ListInsightsResponse(BaseValidatorModel):
    insights: List[InsightSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Nodegroup(BaseValidatorModel):
    nodegroupName: Optional[str] = None
    nodegroupArn: Optional[str] = None
    clusterName: Optional[str] = None
    version: Optional[str] = None
    releaseVersion: Optional[str] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    status: Optional[NodegroupStatusType] = None
    capacityType: Optional[CapacityTypesType] = None
    scalingConfig: Optional[NodegroupScalingConfig] = None
    instanceTypes: Optional[List[str]] = None
    subnets: Optional[List[str]] = None
    remoteAccess: Optional[RemoteAccessConfigOutput] = None
    amiType: Optional[AMITypesType] = None
    nodeRole: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    taints: Optional[List[Taint]] = None
    resources: Optional[NodegroupResources] = None
    diskSize: Optional[int] = None
    health: Optional[NodegroupHealth] = None
    updateConfig: Optional[NodegroupUpdateConfig] = None
    nodeRepairConfig: Optional[NodeRepairConfig] = None
    launchTemplate: Optional[LaunchTemplateSpecification] = None
    tags: Optional[Dict[str, str]] = None

LoggingUnion = Union[Logging, LoggingOutput]


# This class is the input for the 'create_nodegroup' function.
class CreateNodegroupRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    subnets: List[str]
    nodeRole: str
    scalingConfig: Optional[NodegroupScalingConfig] = None
    diskSize: Optional[int] = None
    instanceTypes: Optional[List[str]] = None
    amiType: Optional[AMITypesType] = None
    remoteAccess: Optional[RemoteAccessConfigUnion] = None
    labels: Optional[Dict[str, str]] = None
    taints: Optional[List[Taint]] = None
    tags: Optional[Dict[str, str]] = None
    clientRequestToken: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecification] = None
    updateConfig: Optional[NodegroupUpdateConfig] = None
    nodeRepairConfig: Optional[NodeRepairConfig] = None
    capacityType: Optional[CapacityTypesType] = None
    version: Optional[str] = None
    releaseVersion: Optional[str] = None


class Cluster(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    version: Optional[str] = None
    endpoint: Optional[str] = None
    roleArn: Optional[str] = None
    resourcesVpcConfig: Optional[VpcConfigResponse] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigResponse] = None
    logging: Optional[LoggingOutput] = None
    identity: Optional[Identity] = None
    status: Optional[ClusterStatusType] = None
    certificateAuthority: Optional[Certificate] = None
    clientRequestToken: Optional[str] = None
    platformVersion: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    encryptionConfig: Optional[List[EncryptionConfigOutput]] = None
    connectorConfig: Optional[ConnectorConfigResponse] = None
    id: Optional[str] = None
    health: Optional[ClusterHealth] = None
    outpostConfig: Optional[OutpostConfigResponse] = None
    accessConfig: Optional[AccessConfigResponse] = None
    upgradePolicy: Optional[UpgradePolicyResponse] = None
    zonalShiftConfig: Optional[ZonalShiftConfigResponse] = None
    remoteNetworkConfig: Optional[RemoteNetworkConfigResponse] = None
    computeConfig: Optional[ComputeConfigResponse] = None
    storageConfig: Optional[StorageConfigResponse] = None


class RemoteNetworkConfigRequest(BaseValidatorModel):
    remoteNodeNetworks: Optional[List[RemoteNodeNetworkUnion]] = None
    remotePodNetworks: Optional[List[RemotePodNetworkUnion]] = None


# This class is the output for the 'associate_encryption_config' function.
class AssociateEncryptionConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_identity_provider_config' function.
class AssociateIdentityProviderConfigResponse(BaseValidatorModel):
    update: Update
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_update' function.
class DescribeUpdateResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_identity_provider_config' function.
class DisassociateIdentityProviderConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_addon' function.
class UpdateAddonResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster_config' function.
class UpdateClusterConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster_version' function.
class UpdateClusterVersionResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_nodegroup_config' function.
class UpdateNodegroupConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_nodegroup_version' function.
class UpdateNodegroupVersionResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_addon' function.
class CreateAddonResponse(BaseValidatorModel):
    addon: Addon
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_addon' function.
class DeleteAddonResponse(BaseValidatorModel):
    addon: Addon
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_addon' function.
class DescribeAddonResponse(BaseValidatorModel):
    addon: Addon
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_addon_versions' function.
class DescribeAddonVersionsResponse(BaseValidatorModel):
    addons: List[AddonInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Insight(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    category: Optional[Literal['UPGRADE_READINESS']] = None
    kubernetesVersion: Optional[str] = None
    lastRefreshTime: Optional[datetime] = None
    lastTransitionTime: Optional[datetime] = None
    description: Optional[str] = None
    insightStatus: Optional[InsightStatus] = None
    recommendation: Optional[str] = None
    additionalInfo: Optional[Dict[str, str]] = None
    resources: Optional[List[InsightResourceDetail]] = None
    categorySpecificSummary: Optional[InsightCategorySpecificSummary] = None


# This class is the input for the 'associate_encryption_config' function.
class AssociateEncryptionConfigRequest(BaseValidatorModel):
    clusterName: str
    encryptionConfig: List[EncryptionConfigUnion]
    clientRequestToken: Optional[str] = None


# This class is the output for the 'create_fargate_profile' function.
class CreateFargateProfileResponse(BaseValidatorModel):
    fargateProfile: FargateProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_fargate_profile' function.
class DeleteFargateProfileResponse(BaseValidatorModel):
    fargateProfile: FargateProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fargate_profile' function.
class DescribeFargateProfileResponse(BaseValidatorModel):
    fargateProfile: FargateProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_nodegroup' function.
class CreateNodegroupResponse(BaseValidatorModel):
    nodegroup: Nodegroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_nodegroup' function.
class DeleteNodegroupResponse(BaseValidatorModel):
    nodegroup: Nodegroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_nodegroup' function.
class DescribeNodegroupResponse(BaseValidatorModel):
    nodegroup: Nodegroup
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_cluster_config' function.
class UpdateClusterConfigRequest(BaseValidatorModel):
    name: str
    resourcesVpcConfig: Optional[VpcConfigRequest] = None
    logging: Optional[LoggingUnion] = None
    clientRequestToken: Optional[str] = None
    accessConfig: Optional[UpdateAccessConfigRequest] = None
    upgradePolicy: Optional[UpgradePolicyRequest] = None
    zonalShiftConfig: Optional[ZonalShiftConfigRequest] = None
    computeConfig: Optional[ComputeConfigRequest] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequest] = None
    storageConfig: Optional[StorageConfigRequest] = None


# This class is the output for the 'create_cluster' function.
class CreateClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster' function.
class DeleteClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_cluster' function.
class DeregisterClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster' function.
class DescribeClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_cluster' function.
class RegisterClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_cluster' function.
class CreateClusterRequest(BaseValidatorModel):
    name: str
    roleArn: str
    resourcesVpcConfig: VpcConfigRequest
    version: Optional[str] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequest] = None
    logging: Optional[LoggingUnion] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    encryptionConfig: Optional[List[EncryptionConfigUnion]] = None
    outpostConfig: Optional[OutpostConfigRequest] = None
    accessConfig: Optional[CreateAccessConfigRequest] = None
    bootstrapSelfManagedAddons: Optional[bool] = None
    upgradePolicy: Optional[UpgradePolicyRequest] = None
    zonalShiftConfig: Optional[ZonalShiftConfigRequest] = None
    remoteNetworkConfig: Optional[RemoteNetworkConfigRequest] = None
    computeConfig: Optional[ComputeConfigRequest] = None
    storageConfig: Optional[StorageConfigRequest] = None


# This class is the output for the 'describe_insight' function.
class DescribeInsightResponse(BaseValidatorModel):
    insight: Insight
    ResponseMetadata: ResponseMetadata