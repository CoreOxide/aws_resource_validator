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
from aws_resource_validator.pydantic_models.eks_constants import *

class AccessConfigResponse(BaseValidatorModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None


class AccessPolicy(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


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
    requiredClaims: Optional[Mapping[str, str]] = None


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
    nodePools: Optional[Sequence[str]] = None
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


class UpgradePolicyRequest(BaseValidatorModel):
    supportType: Optional[SupportTypeType] = None


class VpcConfigRequest(BaseValidatorModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[Sequence[str]] = None


class ZonalShiftConfigRequest(BaseValidatorModel):
    enabled: Optional[bool] = None


class EksAnywhereSubscriptionTerm(BaseValidatorModel):
    duration: Optional[int] = None
    unit: Optional[Literal["MONTHS"]] = None


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


class CreatePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    namespace: str
    serviceAccount: str
    roleArn: str
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


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


class DeleteAddonRequest(BaseValidatorModel):
    clusterName: str
    addonName: str
    preserve: Optional[bool] = None


class DeleteClusterRequest(BaseValidatorModel):
    name: str


class DeleteFargateProfileRequest(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str


class DeleteNodegroupRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str


class DeletePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    associationId: str


class DeregisterClusterRequest(BaseValidatorModel):
    name: str


class DescribeAccessEntryRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str


class DescribeAddonConfigurationRequest(BaseValidatorModel):
    addonName: str
    addonVersion: str


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


class DescribeClusterRequest(BaseValidatorModel):
    name: str


class DescribeClusterVersionsRequest(BaseValidatorModel):
    clusterType: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    defaultOnly: Optional[bool] = None
    includeAll: Optional[bool] = None
    clusterVersions: Optional[Sequence[str]] = None
    status: Optional[ClusterVersionStatusType] = None
    versionStatus: Optional[VersionStatusType] = None


class DescribeFargateProfileRequest(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str


class DescribeNodegroupRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str


class DescribePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    associationId: str


class DescribeUpdateRequest(BaseValidatorModel):
    name: str
    updateId: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None


class DisassociateAccessPolicyRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    policyArn: str


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
    labels: Optional[Mapping[str, str]] = None


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
    categories: Optional[Sequence[Literal["UPGRADE_READINESS"]]] = None
    kubernetesVersions: Optional[Sequence[str]] = None
    statuses: Optional[Sequence[InsightStatusValueType]] = None


class Issue(BaseValidatorModel):
    code: Optional[NodegroupIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class ListAccessEntriesRequest(BaseValidatorModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAccessPoliciesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAddonsRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssociatedAccessPoliciesRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListClustersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    include: Optional[Sequence[str]] = None


class ListEksAnywhereSubscriptionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None


class ListFargateProfilesRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdentityProviderConfigsRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListNodegroupsRequest(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListUpdatesRequest(BaseValidatorModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RemoteAccessConfigOutput(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[List[str]] = None


class RemoteAccessConfig(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[Sequence[str]] = None


class RemoteNodeNetworkOutput(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class RemotePodNetworkOutput(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class RemoteNodeNetwork(BaseValidatorModel):
    cidrs: Optional[Sequence[str]] = None


class RemotePodNetwork(BaseValidatorModel):
    cidrs: Optional[Sequence[str]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAccessConfigRequest(BaseValidatorModel):
    authenticationMode: Optional[AuthenticationModeType] = None


class UpdateAccessEntryRequest(BaseValidatorModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[Sequence[str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None


class UpdateClusterVersionRequest(BaseValidatorModel):
    name: str
    version: str
    clientRequestToken: Optional[str] = None


class UpdateLabelsPayload(BaseValidatorModel):
    addOrUpdateLabels: Optional[Mapping[str, str]] = None
    removeLabels: Optional[Sequence[str]] = None


class UpdatePodIdentityAssociationRequest(BaseValidatorModel):
    clusterName: str
    associationId: str
    roleArn: Optional[str] = None
    clientRequestToken: Optional[str] = None


class AccessScopeOutput(BaseValidatorModel):
    pass


class AssociatedAccessPolicy(BaseValidatorModel):
    policyArn: Optional[str] = None
    accessScope: Optional[AccessScopeOutput] = None
    associatedAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None


class AddonHealth(BaseValidatorModel):
    issues: Optional[List[AddonIssue]] = None


class CreateAddonRequest(BaseValidatorModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[Sequence[AddonPodIdentityAssociations]] = None


class UpdateAddonRequest(BaseValidatorModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[Sequence[AddonPodIdentityAssociations]] = None


class AddonVersionInfo(BaseValidatorModel):
    addonVersion: Optional[str] = None
    architecture: Optional[List[str]] = None
    computeTypes: Optional[List[str]] = None
    compatibilities: Optional[List[Compatibility]] = None
    requiresConfiguration: Optional[bool] = None
    requiresIamPermissions: Optional[bool] = None


class AccessEntry(BaseValidatorModel):
    pass


class CreateAccessEntryResponse(BaseValidatorModel):
    accessEntry: AccessEntry
    ResponseMetadata: ResponseMetadata


class DescribeAccessEntryResponse(BaseValidatorModel):
    accessEntry: AccessEntry
    ResponseMetadata: ResponseMetadata


class DescribeAddonConfigurationResponse(BaseValidatorModel):
    addonName: str
    addonVersion: str
    configurationSchema: str
    podIdentityConfiguration: List[AddonPodIdentityConfiguration]
    ResponseMetadata: ResponseMetadata


class ListAccessEntriesResponse(BaseValidatorModel):
    accessEntries: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAccessPoliciesResponse(BaseValidatorModel):
    accessPolicies: List[AccessPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAddonsResponse(BaseValidatorModel):
    addons: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListClustersResponse(BaseValidatorModel):
    clusters: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListFargateProfilesResponse(BaseValidatorModel):
    fargateProfileNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListNodegroupsResponse(BaseValidatorModel):
    nodegroups: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListUpdatesResponse(BaseValidatorModel):
    updateIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateAccessEntryResponse(BaseValidatorModel):
    accessEntry: AccessEntry
    ResponseMetadata: ResponseMetadata


class AssociateIdentityProviderConfigRequest(BaseValidatorModel):
    clusterName: str
    oidc: OidcIdentityProviderConfigRequest
    tags: Optional[Mapping[str, str]] = None
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


class DescribeClusterVersionsResponse(BaseValidatorModel):
    clusterVersions: List[ClusterVersionInformation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RegisterClusterRequest(BaseValidatorModel):
    name: str
    connectorConfig: ConnectorConfigRequest
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class OutpostConfigRequest(BaseValidatorModel):
    outpostArns: Sequence[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementRequest] = None


class OutpostConfigResponse(BaseValidatorModel):
    outpostArns: List[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementResponse] = None


class CreateEksAnywhereSubscriptionRequest(BaseValidatorModel):
    name: str
    term: EksAnywhereSubscriptionTerm
    licenseQuantity: Optional[int] = None
    licenseType: Optional[Literal["Cluster"]] = None
    autoRenew: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class LaunchTemplateSpecification(BaseValidatorModel):
    pass


class UpdateNodegroupVersionRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    version: Optional[str] = None
    releaseVersion: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecification] = None
    force: Optional[bool] = None
    clientRequestToken: Optional[str] = None


class UpdateTaintsPayload(BaseValidatorModel):
    addOrUpdateTaints: Optional[Sequence[Taint]] = None
    removeTaints: Optional[Sequence[Taint]] = None


class CreatePodIdentityAssociationResponse(BaseValidatorModel):
    association: PodIdentityAssociation
    ResponseMetadata: ResponseMetadata


class DeletePodIdentityAssociationResponse(BaseValidatorModel):
    association: PodIdentityAssociation
    ResponseMetadata: ResponseMetadata


class DescribePodIdentityAssociationResponse(BaseValidatorModel):
    association: PodIdentityAssociation
    ResponseMetadata: ResponseMetadata


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


class DescribeClusterVersionsRequestPaginate(BaseValidatorModel):
    clusterType: Optional[str] = None
    defaultOnly: Optional[bool] = None
    includeAll: Optional[bool] = None
    clusterVersions: Optional[Sequence[str]] = None
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
    include: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEksAnywhereSubscriptionsRequestPaginate(BaseValidatorModel):
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None
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


class IdentityProviderConfig(BaseValidatorModel):
    pass


class DescribeIdentityProviderConfigRequest(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfig


class DisassociateIdentityProviderConfigRequest(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfig
    clientRequestToken: Optional[str] = None


class ListIdentityProviderConfigsResponse(BaseValidatorModel):
    identityProviderConfigs: List[IdentityProviderConfig]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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
    resources: Optional[Sequence[str]] = None
    provider: Optional[Provider] = None


class FargateProfileHealth(BaseValidatorModel):
    issues: Optional[List[FargateProfileIssue]] = None


class IdentityProviderConfigResponse(BaseValidatorModel):
    oidc: Optional[OidcIdentityProviderConfig] = None


class Identity(BaseValidatorModel):
    oidc: Optional[OIDC] = None


class InsightResourceDetail(BaseValidatorModel):
    insightStatus: Optional[InsightStatus] = None
    kubernetesResourceUri: Optional[str] = None
    arn: Optional[str] = None


class NodegroupHealth(BaseValidatorModel):
    issues: Optional[List[Issue]] = None


class ListPodIdentityAssociationsResponse(BaseValidatorModel):
    associations: List[PodIdentityAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LogSetupOutput(BaseValidatorModel):
    pass


class LoggingOutput(BaseValidatorModel):
    clusterLogging: Optional[List[LogSetupOutput]] = None


class LogSetup(BaseValidatorModel):
    pass


class Logging(BaseValidatorModel):
    clusterLogging: Optional[Sequence[LogSetup]] = None


class RemoteNetworkConfigResponse(BaseValidatorModel):
    remoteNodeNetworks: Optional[List[RemoteNodeNetworkOutput]] = None
    remotePodNetworks: Optional[List[RemotePodNetworkOutput]] = None


class AssociateAccessPolicyResponse(BaseValidatorModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicy: AssociatedAccessPolicy
    ResponseMetadata: ResponseMetadata


class ListAssociatedAccessPoliciesResponse(BaseValidatorModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicies: List[AssociatedAccessPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AccessScopeUnion(BaseValidatorModel):
    pass


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


class InsightCategorySpecificSummary(BaseValidatorModel):
    deprecationDetails: Optional[List[DeprecationDetail]] = None
    addonCompatibilityDetails: Optional[List[AddonCompatibilityDetail]] = None


class UpdateNodegroupConfigRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    labels: Optional[UpdateLabelsPayload] = None
    taints: Optional[UpdateTaintsPayload] = None
    scalingConfig: Optional[NodegroupScalingConfig] = None
    updateConfig: Optional[NodegroupUpdateConfig] = None
    nodeRepairConfig: Optional[NodeRepairConfig] = None
    clientRequestToken: Optional[str] = None


class EksAnywhereSubscription(BaseValidatorModel):
    pass


class CreateEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata


class DeleteEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata


class DescribeEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata


class ListEksAnywhereSubscriptionsResponse(BaseValidatorModel):
    subscriptions: List[EksAnywhereSubscription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateEksAnywhereSubscriptionResponse(BaseValidatorModel):
    subscription: EksAnywhereSubscription
    ResponseMetadata: ResponseMetadata


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


class FargateProfileSelectorUnion(BaseValidatorModel):
    pass


class CreateFargateProfileRequest(BaseValidatorModel):
    fargateProfileName: str
    clusterName: str
    podExecutionRoleArn: str
    subnets: Optional[Sequence[str]] = None
    selectors: Optional[Sequence[FargateProfileSelectorUnion]] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeIdentityProviderConfigResponse(BaseValidatorModel):
    identityProviderConfig: IdentityProviderConfigResponse
    ResponseMetadata: ResponseMetadata


class InsightSummary(BaseValidatorModel):
    pass


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


class RemoteAccessConfigUnion(BaseValidatorModel):
    pass


class CreateNodegroupRequest(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    subnets: Sequence[str]
    nodeRole: str
    scalingConfig: Optional[NodegroupScalingConfig] = None
    diskSize: Optional[int] = None
    instanceTypes: Optional[Sequence[str]] = None
    amiType: Optional[AMITypesType] = None
    remoteAccess: Optional[RemoteAccessConfigUnion] = None
    labels: Optional[Mapping[str, str]] = None
    taints: Optional[Sequence[Taint]] = None
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecification] = None
    updateConfig: Optional[NodegroupUpdateConfig] = None
    nodeRepairConfig: Optional[NodeRepairConfig] = None
    capacityType: Optional[CapacityTypesType] = None
    version: Optional[str] = None
    releaseVersion: Optional[str] = None


class RemoteNodeNetworkUnion(BaseValidatorModel):
    pass


class RemotePodNetworkUnion(BaseValidatorModel):
    pass


class RemoteNetworkConfigRequest(BaseValidatorModel):
    remoteNodeNetworks: Optional[Sequence[RemoteNodeNetworkUnion]] = None
    remotePodNetworks: Optional[Sequence[RemotePodNetworkUnion]] = None


class Update(BaseValidatorModel):
    pass


class AssociateEncryptionConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class AssociateIdentityProviderConfigResponse(BaseValidatorModel):
    update: Update
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeUpdateResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class DisassociateIdentityProviderConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class UpdateAddonResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class UpdateClusterConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class UpdateClusterVersionResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class UpdateNodegroupConfigResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class UpdateNodegroupVersionResponse(BaseValidatorModel):
    update: Update
    ResponseMetadata: ResponseMetadata


class CreateAddonResponse(BaseValidatorModel):
    addon: Addon
    ResponseMetadata: ResponseMetadata


class DeleteAddonResponse(BaseValidatorModel):
    addon: Addon
    ResponseMetadata: ResponseMetadata


class DescribeAddonResponse(BaseValidatorModel):
    addon: Addon
    ResponseMetadata: ResponseMetadata


class AddonInfo(BaseValidatorModel):
    pass


class DescribeAddonVersionsResponse(BaseValidatorModel):
    addons: List[AddonInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EncryptionConfigUnion(BaseValidatorModel):
    pass


class AssociateEncryptionConfigRequest(BaseValidatorModel):
    clusterName: str
    encryptionConfig: Sequence[EncryptionConfigUnion]
    clientRequestToken: Optional[str] = None


class CreateFargateProfileResponse(BaseValidatorModel):
    fargateProfile: FargateProfile
    ResponseMetadata: ResponseMetadata


class DeleteFargateProfileResponse(BaseValidatorModel):
    fargateProfile: FargateProfile
    ResponseMetadata: ResponseMetadata


class DescribeFargateProfileResponse(BaseValidatorModel):
    fargateProfile: FargateProfile
    ResponseMetadata: ResponseMetadata


class CreateNodegroupResponse(BaseValidatorModel):
    nodegroup: Nodegroup
    ResponseMetadata: ResponseMetadata


class DeleteNodegroupResponse(BaseValidatorModel):
    nodegroup: Nodegroup
    ResponseMetadata: ResponseMetadata


class DescribeNodegroupResponse(BaseValidatorModel):
    nodegroup: Nodegroup
    ResponseMetadata: ResponseMetadata


class LoggingUnion(BaseValidatorModel):
    pass


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


class Cluster(BaseValidatorModel):
    pass


class CreateClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DeleteClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DeregisterClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DescribeClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class RegisterClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class CreateClusterRequest(BaseValidatorModel):
    name: str
    roleArn: str
    resourcesVpcConfig: VpcConfigRequest
    version: Optional[str] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequest] = None
    logging: Optional[LoggingUnion] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    encryptionConfig: Optional[Sequence[EncryptionConfigUnion]] = None
    outpostConfig: Optional[OutpostConfigRequest] = None
    accessConfig: Optional[CreateAccessConfigRequest] = None
    bootstrapSelfManagedAddons: Optional[bool] = None
    upgradePolicy: Optional[UpgradePolicyRequest] = None
    zonalShiftConfig: Optional[ZonalShiftConfigRequest] = None
    remoteNetworkConfig: Optional[RemoteNetworkConfigRequest] = None
    computeConfig: Optional[ComputeConfigRequest] = None
    storageConfig: Optional[StorageConfigRequest] = None


class Insight(BaseValidatorModel):
    pass


class DescribeInsightResponse(BaseValidatorModel):
    insight: Insight
    ResponseMetadata: ResponseMetadata


