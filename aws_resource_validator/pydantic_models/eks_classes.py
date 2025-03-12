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

class AccessConfigResponseTypeDef(BaseValidatorModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None


class AccessPolicyTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None


class AddonCompatibilityDetailTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    compatibleVersions: Optional[List[str]] = None


class AddonIssueTypeDef(BaseValidatorModel):
    code: Optional[AddonIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class MarketplaceInformationTypeDef(BaseValidatorModel):
    productId: Optional[str] = None
    productUrl: Optional[str] = None


class AddonPodIdentityAssociationsTypeDef(BaseValidatorModel):
    serviceAccount: str
    roleArn: str


class AddonPodIdentityConfigurationTypeDef(BaseValidatorModel):
    serviceAccount: Optional[str] = None
    recommendedManagedPolicies: Optional[List[str]] = None


class CompatibilityTypeDef(BaseValidatorModel):
    clusterVersion: Optional[str] = None
    platformVersions: Optional[List[str]] = None
    defaultVersion: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class OidcIdentityProviderConfigRequestTypeDef(BaseValidatorModel):
    identityProviderConfigName: str
    issuerUrl: str
    clientId: str
    usernameClaim: Optional[str] = None
    usernamePrefix: Optional[str] = None
    groupsClaim: Optional[str] = None
    groupsPrefix: Optional[str] = None
    requiredClaims: Optional[Mapping[str, str]] = None


class AutoScalingGroupTypeDef(BaseValidatorModel):
    name: Optional[str] = None


class BlockStorageTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None


class CertificateTypeDef(BaseValidatorModel):
    data: Optional[str] = None


class ClientStatTypeDef(BaseValidatorModel):
    userAgent: Optional[str] = None
    numberOfRequestsLast30Days: Optional[int] = None
    lastRequestTime: Optional[datetime] = None


class ClusterIssueTypeDef(BaseValidatorModel):
    code: Optional[ClusterIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class ComputeConfigResponseTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    nodePools: Optional[List[str]] = None
    nodeRoleArn: Optional[str] = None


class ConnectorConfigResponseTypeDef(BaseValidatorModel):
    activationId: Optional[str] = None
    activationCode: Optional[str] = None
    activationExpiry: Optional[datetime] = None
    provider: Optional[str] = None
    roleArn: Optional[str] = None


class UpgradePolicyResponseTypeDef(BaseValidatorModel):
    supportType: Optional[SupportTypeType] = None


class VpcConfigResponseTypeDef(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    clusterSecurityGroupId: Optional[str] = None
    vpcId: Optional[str] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[List[str]] = None


class ZonalShiftConfigResponseTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None


class ClusterVersionInformationTypeDef(BaseValidatorModel):
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


class ComputeConfigRequestTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    nodePools: Optional[Sequence[str]] = None
    nodeRoleArn: Optional[str] = None


class ConnectorConfigRequestTypeDef(BaseValidatorModel):
    roleArn: str
    provider: ConnectorConfigProviderType


class ControlPlanePlacementRequestTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None


class ControlPlanePlacementResponseTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None


class CreateAccessConfigRequestTypeDef(BaseValidatorModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None


class UpgradePolicyRequestTypeDef(BaseValidatorModel):
    supportType: Optional[SupportTypeType] = None


class VpcConfigRequestTypeDef(BaseValidatorModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[Sequence[str]] = None


class ZonalShiftConfigRequestTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None


class EksAnywhereSubscriptionTermTypeDef(BaseValidatorModel):
    duration: Optional[int] = None
    unit: Optional[Literal["MONTHS"]] = None


class NodeRepairConfigTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None


class NodegroupScalingConfigTypeDef(BaseValidatorModel):
    minSize: Optional[int] = None
    maxSize: Optional[int] = None
    desiredSize: Optional[int] = None


class NodegroupUpdateConfigTypeDef(BaseValidatorModel):
    maxUnavailable: Optional[int] = None
    maxUnavailablePercentage: Optional[int] = None
    updateStrategy: Optional[NodegroupUpdateStrategiesType] = None


class TaintTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None
    effect: Optional[TaintEffectType] = None


class CreatePodIdentityAssociationRequestTypeDef(BaseValidatorModel):
    clusterName: str
    namespace: str
    serviceAccount: str
    roleArn: str
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class PodIdentityAssociationTypeDef(BaseValidatorModel):
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


class DeleteAccessEntryRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str


class DeleteAddonRequestTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    preserve: Optional[bool] = None


class DeleteClusterRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteFargateProfileRequestTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str


class DeleteNodegroupRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str


class DeletePodIdentityAssociationRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associationId: str


class DeregisterClusterRequestTypeDef(BaseValidatorModel):
    name: str


class DescribeAccessEntryRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str


class DescribeAddonConfigurationRequestTypeDef(BaseValidatorModel):
    addonName: str
    addonVersion: str


class DescribeAddonRequestTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeClusterRequestTypeDef(BaseValidatorModel):
    name: str


class DescribeClusterVersionsRequestTypeDef(BaseValidatorModel):
    clusterType: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    defaultOnly: Optional[bool] = None
    includeAll: Optional[bool] = None
    clusterVersions: Optional[Sequence[str]] = None
    status: Optional[ClusterVersionStatusType] = None
    versionStatus: Optional[VersionStatusType] = None


class DescribeFargateProfileRequestTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str


class DescribeNodegroupRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str


class DescribePodIdentityAssociationRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associationId: str


class DescribeUpdateRequestTypeDef(BaseValidatorModel):
    name: str
    updateId: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None


class DisassociateAccessPolicyRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    policyArn: str


class ElasticLoadBalancingTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None


class ProviderTypeDef(BaseValidatorModel):
    keyArn: Optional[str] = None


class ErrorDetailTypeDef(BaseValidatorModel):
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class FargateProfileIssueTypeDef(BaseValidatorModel):
    code: Optional[FargateProfileIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class FargateProfileSelectorOutputTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None
    labels: Optional[Dict[str, str]] = None


class FargateProfileSelectorTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None
    labels: Optional[Mapping[str, str]] = None


class OidcIdentityProviderConfigTypeDef(BaseValidatorModel):
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


class OIDCTypeDef(BaseValidatorModel):
    issuer: Optional[str] = None


class InsightStatusTypeDef(BaseValidatorModel):
    status: Optional[InsightStatusValueType] = None
    reason: Optional[str] = None


class InsightsFilterTypeDef(BaseValidatorModel):
    categories: Optional[Sequence[Literal["UPGRADE_READINESS"]]] = None
    kubernetesVersions: Optional[Sequence[str]] = None
    statuses: Optional[Sequence[InsightStatusValueType]] = None


class IssueTypeDef(BaseValidatorModel):
    code: Optional[NodegroupIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None


class ListAccessEntriesRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAccessPoliciesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAddonsRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssociatedAccessPoliciesRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListClustersRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    include: Optional[Sequence[str]] = None


class ListEksAnywhereSubscriptionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None


class ListFargateProfilesRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdentityProviderConfigsRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListNodegroupsRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPodIdentityAssociationsRequestTypeDef(BaseValidatorModel):
    clusterName: str
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PodIdentityAssociationSummaryTypeDef(BaseValidatorModel):
    clusterName: Optional[str] = None
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    associationArn: Optional[str] = None
    associationId: Optional[str] = None
    ownerArn: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListUpdatesRequestTypeDef(BaseValidatorModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RemoteAccessConfigOutputTypeDef(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[List[str]] = None


class RemoteAccessConfigTypeDef(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[Sequence[str]] = None


class RemoteNodeNetworkOutputTypeDef(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class RemotePodNetworkOutputTypeDef(BaseValidatorModel):
    cidrs: Optional[List[str]] = None


class RemoteNodeNetworkTypeDef(BaseValidatorModel):
    cidrs: Optional[Sequence[str]] = None


class RemotePodNetworkTypeDef(BaseValidatorModel):
    cidrs: Optional[Sequence[str]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAccessConfigRequestTypeDef(BaseValidatorModel):
    authenticationMode: Optional[AuthenticationModeType] = None


class UpdateAccessEntryRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[Sequence[str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None


class UpdateClusterVersionRequestTypeDef(BaseValidatorModel):
    name: str
    version: str
    clientRequestToken: Optional[str] = None


class UpdateLabelsPayloadTypeDef(BaseValidatorModel):
    addOrUpdateLabels: Optional[Mapping[str, str]] = None
    removeLabels: Optional[Sequence[str]] = None


class UpdatePodIdentityAssociationRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associationId: str
    roleArn: Optional[str] = None
    clientRequestToken: Optional[str] = None


class AccessScopeOutputTypeDef(BaseValidatorModel):
    pass


class AssociatedAccessPolicyTypeDef(BaseValidatorModel):
    policyArn: Optional[str] = None
    accessScope: Optional[AccessScopeOutputTypeDef] = None
    associatedAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None


class AddonHealthTypeDef(BaseValidatorModel):
    issues: Optional[List[AddonIssueTypeDef]] = None


class CreateAddonRequestTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[Sequence[AddonPodIdentityAssociationsTypeDef]] = None


class UpdateAddonRequestTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[Sequence[AddonPodIdentityAssociationsTypeDef]] = None


class AddonVersionInfoTypeDef(BaseValidatorModel):
    addonVersion: Optional[str] = None
    architecture: Optional[List[str]] = None
    computeTypes: Optional[List[str]] = None
    compatibilities: Optional[List[CompatibilityTypeDef]] = None
    requiresConfiguration: Optional[bool] = None
    requiresIamPermissions: Optional[bool] = None


class AccessEntryTypeDef(BaseValidatorModel):
    pass


class CreateAccessEntryResponseTypeDef(BaseValidatorModel):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccessEntryResponseTypeDef(BaseValidatorModel):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAddonConfigurationResponseTypeDef(BaseValidatorModel):
    addonName: str
    addonVersion: str
    configurationSchema: str
    podIdentityConfiguration: List[AddonPodIdentityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccessEntriesResponseTypeDef(BaseValidatorModel):
    accessEntries: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAccessPoliciesResponseTypeDef(BaseValidatorModel):
    accessPolicies: List[AccessPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAddonsResponseTypeDef(BaseValidatorModel):
    addons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListClustersResponseTypeDef(BaseValidatorModel):
    clusters: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListFargateProfilesResponseTypeDef(BaseValidatorModel):
    fargateProfileNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListNodegroupsResponseTypeDef(BaseValidatorModel):
    nodegroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListUpdatesResponseTypeDef(BaseValidatorModel):
    updateIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateAccessEntryResponseTypeDef(BaseValidatorModel):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateIdentityProviderConfigRequestTypeDef(BaseValidatorModel):
    clusterName: str
    oidc: OidcIdentityProviderConfigRequestTypeDef
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None


class NodegroupResourcesTypeDef(BaseValidatorModel):
    autoScalingGroups: Optional[List[AutoScalingGroupTypeDef]] = None
    remoteAccessSecurityGroup: Optional[str] = None


class StorageConfigRequestTypeDef(BaseValidatorModel):
    blockStorage: Optional[BlockStorageTypeDef] = None


class StorageConfigResponseTypeDef(BaseValidatorModel):
    blockStorage: Optional[BlockStorageTypeDef] = None


class DeprecationDetailTypeDef(BaseValidatorModel):
    usage: Optional[str] = None
    replacedWith: Optional[str] = None
    stopServingVersion: Optional[str] = None
    startServingReplacementVersion: Optional[str] = None
    clientStats: Optional[List[ClientStatTypeDef]] = None


class ClusterHealthTypeDef(BaseValidatorModel):
    issues: Optional[List[ClusterIssueTypeDef]] = None


class DescribeClusterVersionsResponseTypeDef(BaseValidatorModel):
    clusterVersions: List[ClusterVersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RegisterClusterRequestTypeDef(BaseValidatorModel):
    name: str
    connectorConfig: ConnectorConfigRequestTypeDef
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class OutpostConfigRequestTypeDef(BaseValidatorModel):
    outpostArns: Sequence[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementRequestTypeDef] = None


class OutpostConfigResponseTypeDef(BaseValidatorModel):
    outpostArns: List[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementResponseTypeDef] = None


class CreateEksAnywhereSubscriptionRequestTypeDef(BaseValidatorModel):
    name: str
    term: EksAnywhereSubscriptionTermTypeDef
    licenseQuantity: Optional[int] = None
    licenseType: Optional[Literal["Cluster"]] = None
    autoRenew: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class LaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    pass


class UpdateNodegroupVersionRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    version: Optional[str] = None
    releaseVersion: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    force: Optional[bool] = None
    clientRequestToken: Optional[str] = None


class UpdateTaintsPayloadTypeDef(BaseValidatorModel):
    addOrUpdateTaints: Optional[Sequence[TaintTypeDef]] = None
    removeTaints: Optional[Sequence[TaintTypeDef]] = None


class CreatePodIdentityAssociationResponseTypeDef(BaseValidatorModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePodIdentityAssociationResponseTypeDef(BaseValidatorModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePodIdentityAssociationResponseTypeDef(BaseValidatorModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePodIdentityAssociationResponseTypeDef(BaseValidatorModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAddonRequestWaitExtraTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeAddonRequestWaitTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeClusterRequestWaitExtraTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeClusterRequestWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeFargateProfileRequestWaitExtraTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeFargateProfileRequestWaitTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeNodegroupRequestWaitExtraTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeNodegroupRequestWaitTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeClusterVersionsRequestPaginateTypeDef(BaseValidatorModel):
    clusterType: Optional[str] = None
    defaultOnly: Optional[bool] = None
    includeAll: Optional[bool] = None
    clusterVersions: Optional[Sequence[str]] = None
    status: Optional[ClusterVersionStatusType] = None
    versionStatus: Optional[VersionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccessEntriesRequestPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccessPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAddonsRequestPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociatedAccessPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClustersRequestPaginateTypeDef(BaseValidatorModel):
    include: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEksAnywhereSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFargateProfilesRequestPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIdentityProviderConfigsRequestPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNodegroupsRequestPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPodIdentityAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUpdatesRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class IdentityProviderConfigTypeDef(BaseValidatorModel):
    pass


class DescribeIdentityProviderConfigRequestTypeDef(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef


class DisassociateIdentityProviderConfigRequestTypeDef(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef
    clientRequestToken: Optional[str] = None


class ListIdentityProviderConfigsResponseTypeDef(BaseValidatorModel):
    identityProviderConfigs: List[IdentityProviderConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class KubernetesNetworkConfigRequestTypeDef(BaseValidatorModel):
    serviceIpv4Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None
    elasticLoadBalancing: Optional[ElasticLoadBalancingTypeDef] = None


class KubernetesNetworkConfigResponseTypeDef(BaseValidatorModel):
    serviceIpv4Cidr: Optional[str] = None
    serviceIpv6Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None
    elasticLoadBalancing: Optional[ElasticLoadBalancingTypeDef] = None


class EncryptionConfigOutputTypeDef(BaseValidatorModel):
    resources: Optional[List[str]] = None
    provider: Optional[ProviderTypeDef] = None


class EncryptionConfigTypeDef(BaseValidatorModel):
    resources: Optional[Sequence[str]] = None
    provider: Optional[ProviderTypeDef] = None


class FargateProfileHealthTypeDef(BaseValidatorModel):
    issues: Optional[List[FargateProfileIssueTypeDef]] = None


class IdentityProviderConfigResponseTypeDef(BaseValidatorModel):
    oidc: Optional[OidcIdentityProviderConfigTypeDef] = None


class IdentityTypeDef(BaseValidatorModel):
    oidc: Optional[OIDCTypeDef] = None


class InsightResourceDetailTypeDef(BaseValidatorModel):
    insightStatus: Optional[InsightStatusTypeDef] = None
    kubernetesResourceUri: Optional[str] = None
    arn: Optional[str] = None


class NodegroupHealthTypeDef(BaseValidatorModel):
    issues: Optional[List[IssueTypeDef]] = None


class ListPodIdentityAssociationsResponseTypeDef(BaseValidatorModel):
    associations: List[PodIdentityAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LogSetupOutputTypeDef(BaseValidatorModel):
    pass


class LoggingOutputTypeDef(BaseValidatorModel):
    clusterLogging: Optional[List[LogSetupOutputTypeDef]] = None


class LogSetupTypeDef(BaseValidatorModel):
    pass


class LoggingTypeDef(BaseValidatorModel):
    clusterLogging: Optional[Sequence[LogSetupTypeDef]] = None


class RemoteNetworkConfigResponseTypeDef(BaseValidatorModel):
    remoteNodeNetworks: Optional[List[RemoteNodeNetworkOutputTypeDef]] = None
    remotePodNetworks: Optional[List[RemotePodNetworkOutputTypeDef]] = None


class AssociateAccessPolicyResponseTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicy: AssociatedAccessPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssociatedAccessPoliciesResponseTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicies: List[AssociatedAccessPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AccessScopeUnionTypeDef(BaseValidatorModel):
    pass


class AssociateAccessPolicyRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    policyArn: str
    accessScope: AccessScopeUnionTypeDef


class AddonTypeDef(BaseValidatorModel):
    addonName: Optional[str] = None
    clusterName: Optional[str] = None
    status: Optional[AddonStatusType] = None
    addonVersion: Optional[str] = None
    health: Optional[AddonHealthTypeDef] = None
    addonArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    serviceAccountRoleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    publisher: Optional[str] = None
    owner: Optional[str] = None
    marketplaceInformation: Optional[MarketplaceInformationTypeDef] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[List[str]] = None


class InsightCategorySpecificSummaryTypeDef(BaseValidatorModel):
    deprecationDetails: Optional[List[DeprecationDetailTypeDef]] = None
    addonCompatibilityDetails: Optional[List[AddonCompatibilityDetailTypeDef]] = None


class UpdateNodegroupConfigRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    labels: Optional[UpdateLabelsPayloadTypeDef] = None
    taints: Optional[UpdateTaintsPayloadTypeDef] = None
    scalingConfig: Optional[NodegroupScalingConfigTypeDef] = None
    updateConfig: Optional[NodegroupUpdateConfigTypeDef] = None
    nodeRepairConfig: Optional[NodeRepairConfigTypeDef] = None
    clientRequestToken: Optional[str] = None


class EksAnywhereSubscriptionTypeDef(BaseValidatorModel):
    pass


class CreateEksAnywhereSubscriptionResponseTypeDef(BaseValidatorModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEksAnywhereSubscriptionResponseTypeDef(BaseValidatorModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEksAnywhereSubscriptionResponseTypeDef(BaseValidatorModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEksAnywhereSubscriptionsResponseTypeDef(BaseValidatorModel):
    subscriptions: List[EksAnywhereSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateEksAnywhereSubscriptionResponseTypeDef(BaseValidatorModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FargateProfileTypeDef(BaseValidatorModel):
    fargateProfileName: Optional[str] = None
    fargateProfileArn: Optional[str] = None
    clusterName: Optional[str] = None
    createdAt: Optional[datetime] = None
    podExecutionRoleArn: Optional[str] = None
    subnets: Optional[List[str]] = None
    selectors: Optional[List[FargateProfileSelectorOutputTypeDef]] = None
    status: Optional[FargateProfileStatusType] = None
    tags: Optional[Dict[str, str]] = None
    health: Optional[FargateProfileHealthTypeDef] = None


class FargateProfileSelectorUnionTypeDef(BaseValidatorModel):
    pass


class CreateFargateProfileRequestTypeDef(BaseValidatorModel):
    fargateProfileName: str
    clusterName: str
    podExecutionRoleArn: str
    subnets: Optional[Sequence[str]] = None
    selectors: Optional[Sequence[FargateProfileSelectorUnionTypeDef]] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeIdentityProviderConfigResponseTypeDef(BaseValidatorModel):
    identityProviderConfig: IdentityProviderConfigResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InsightSummaryTypeDef(BaseValidatorModel):
    pass


class ListInsightsResponseTypeDef(BaseValidatorModel):
    insights: List[InsightSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NodegroupTypeDef(BaseValidatorModel):
    nodegroupName: Optional[str] = None
    nodegroupArn: Optional[str] = None
    clusterName: Optional[str] = None
    version: Optional[str] = None
    releaseVersion: Optional[str] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    status: Optional[NodegroupStatusType] = None
    capacityType: Optional[CapacityTypesType] = None
    scalingConfig: Optional[NodegroupScalingConfigTypeDef] = None
    instanceTypes: Optional[List[str]] = None
    subnets: Optional[List[str]] = None
    remoteAccess: Optional[RemoteAccessConfigOutputTypeDef] = None
    amiType: Optional[AMITypesType] = None
    nodeRole: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    taints: Optional[List[TaintTypeDef]] = None
    resources: Optional[NodegroupResourcesTypeDef] = None
    diskSize: Optional[int] = None
    health: Optional[NodegroupHealthTypeDef] = None
    updateConfig: Optional[NodegroupUpdateConfigTypeDef] = None
    nodeRepairConfig: Optional[NodeRepairConfigTypeDef] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    tags: Optional[Dict[str, str]] = None


class RemoteAccessConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateNodegroupRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    subnets: Sequence[str]
    nodeRole: str
    scalingConfig: Optional[NodegroupScalingConfigTypeDef] = None
    diskSize: Optional[int] = None
    instanceTypes: Optional[Sequence[str]] = None
    amiType: Optional[AMITypesType] = None
    remoteAccess: Optional[RemoteAccessConfigUnionTypeDef] = None
    labels: Optional[Mapping[str, str]] = None
    taints: Optional[Sequence[TaintTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    updateConfig: Optional[NodegroupUpdateConfigTypeDef] = None
    nodeRepairConfig: Optional[NodeRepairConfigTypeDef] = None
    capacityType: Optional[CapacityTypesType] = None
    version: Optional[str] = None
    releaseVersion: Optional[str] = None


class RemoteNodeNetworkUnionTypeDef(BaseValidatorModel):
    pass


class RemotePodNetworkUnionTypeDef(BaseValidatorModel):
    pass


class RemoteNetworkConfigRequestTypeDef(BaseValidatorModel):
    remoteNodeNetworks: Optional[Sequence[RemoteNodeNetworkUnionTypeDef]] = None
    remotePodNetworks: Optional[Sequence[RemotePodNetworkUnionTypeDef]] = None


class UpdateTypeDef(BaseValidatorModel):
    pass


class AssociateEncryptionConfigResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateIdentityProviderConfigResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeUpdateResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateIdentityProviderConfigResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAddonResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateClusterConfigResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateClusterVersionResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNodegroupConfigResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNodegroupVersionResponseTypeDef(BaseValidatorModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAddonResponseTypeDef(BaseValidatorModel):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAddonResponseTypeDef(BaseValidatorModel):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAddonResponseTypeDef(BaseValidatorModel):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AddonInfoTypeDef(BaseValidatorModel):
    pass


class DescribeAddonVersionsResponseTypeDef(BaseValidatorModel):
    addons: List[AddonInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EncryptionConfigUnionTypeDef(BaseValidatorModel):
    pass


class AssociateEncryptionConfigRequestTypeDef(BaseValidatorModel):
    clusterName: str
    encryptionConfig: Sequence[EncryptionConfigUnionTypeDef]
    clientRequestToken: Optional[str] = None


class CreateFargateProfileResponseTypeDef(BaseValidatorModel):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteFargateProfileResponseTypeDef(BaseValidatorModel):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFargateProfileResponseTypeDef(BaseValidatorModel):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNodegroupResponseTypeDef(BaseValidatorModel):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteNodegroupResponseTypeDef(BaseValidatorModel):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeNodegroupResponseTypeDef(BaseValidatorModel):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoggingUnionTypeDef(BaseValidatorModel):
    pass


class UpdateClusterConfigRequestTypeDef(BaseValidatorModel):
    name: str
    resourcesVpcConfig: Optional[VpcConfigRequestTypeDef] = None
    logging: Optional[LoggingUnionTypeDef] = None
    clientRequestToken: Optional[str] = None
    accessConfig: Optional[UpdateAccessConfigRequestTypeDef] = None
    upgradePolicy: Optional[UpgradePolicyRequestTypeDef] = None
    zonalShiftConfig: Optional[ZonalShiftConfigRequestTypeDef] = None
    computeConfig: Optional[ComputeConfigRequestTypeDef] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequestTypeDef] = None
    storageConfig: Optional[StorageConfigRequestTypeDef] = None


class ClusterTypeDef(BaseValidatorModel):
    pass


class CreateClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateClusterRequestTypeDef(BaseValidatorModel):
    name: str
    roleArn: str
    resourcesVpcConfig: VpcConfigRequestTypeDef
    version: Optional[str] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequestTypeDef] = None
    logging: Optional[LoggingUnionTypeDef] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    encryptionConfig: Optional[Sequence[EncryptionConfigUnionTypeDef]] = None
    outpostConfig: Optional[OutpostConfigRequestTypeDef] = None
    accessConfig: Optional[CreateAccessConfigRequestTypeDef] = None
    bootstrapSelfManagedAddons: Optional[bool] = None
    upgradePolicy: Optional[UpgradePolicyRequestTypeDef] = None
    zonalShiftConfig: Optional[ZonalShiftConfigRequestTypeDef] = None
    remoteNetworkConfig: Optional[RemoteNetworkConfigRequestTypeDef] = None
    computeConfig: Optional[ComputeConfigRequestTypeDef] = None
    storageConfig: Optional[StorageConfigRequestTypeDef] = None


class InsightTypeDef(BaseValidatorModel):
    pass


class DescribeInsightResponseTypeDef(BaseValidatorModel):
    insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


