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
from aws_resource_validator.pydantic_models.eks_constants import *

class AccessConfigResponseTypeDef(BaseModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None

class AccessEntryTypeDef(BaseModel):
    clusterName: Optional[str] = None
    principalArn: Optional[str] = None
    kubernetesGroups: Optional[List[str]] = None
    accessEntryArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    username: Optional[str] = None
    type: Optional[str] = None

class AccessPolicyTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None

class AccessScopeExtraOutputTypeDef(BaseModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[List[str]] = None

class AccessScopeOutputTypeDef(BaseModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[List[str]] = None

class AccessScopeTypeDef(BaseModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[Sequence[str]] = None

class AddonIssueTypeDef(BaseModel):
    code: Optional[AddonIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None

class MarketplaceInformationTypeDef(BaseModel):
    productId: Optional[str] = None
    productUrl: Optional[str] = None

class AddonPodIdentityAssociationsTypeDef(BaseModel):
    serviceAccount: str
    roleArn: str

class AddonPodIdentityConfigurationTypeDef(BaseModel):
    serviceAccount: Optional[str] = None
    recommendedManagedPolicies: Optional[List[str]] = None

class CompatibilityTypeDef(BaseModel):
    clusterVersion: Optional[str] = None
    platformVersions: Optional[List[str]] = None
    defaultVersion: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class OidcIdentityProviderConfigRequestTypeDef(BaseModel):
    identityProviderConfigName: str
    issuerUrl: str
    clientId: str
    usernameClaim: Optional[str] = None
    usernamePrefix: Optional[str] = None
    groupsClaim: Optional[str] = None
    groupsPrefix: Optional[str] = None
    requiredClaims: Optional[Mapping[str, str]] = None

class AutoScalingGroupTypeDef(BaseModel):
    name: Optional[str] = None

class CertificateTypeDef(BaseModel):
    data: Optional[str] = None

class ClientStatTypeDef(BaseModel):
    userAgent: Optional[str] = None
    numberOfRequestsLast30Days: Optional[int] = None
    lastRequestTime: Optional[datetime] = None

class ClusterIssueTypeDef(BaseModel):
    code: Optional[ClusterIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None

class ConnectorConfigResponseTypeDef(BaseModel):
    activationId: Optional[str] = None
    activationCode: Optional[str] = None
    activationExpiry: Optional[datetime] = None
    provider: Optional[str] = None
    roleArn: Optional[str] = None

class KubernetesNetworkConfigResponseTypeDef(BaseModel):
    serviceIpv4Cidr: Optional[str] = None
    serviceIpv6Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None

class VpcConfigResponseTypeDef(BaseModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    clusterSecurityGroupId: Optional[str] = None
    vpcId: Optional[str] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[List[str]] = None

class ConnectorConfigRequestTypeDef(BaseModel):
    roleArn: str
    provider: ConnectorConfigProviderType

class ControlPlanePlacementRequestTypeDef(BaseModel):
    groupName: Optional[str] = None

class ControlPlanePlacementResponseTypeDef(BaseModel):
    groupName: Optional[str] = None

class CreateAccessConfigRequestTypeDef(BaseModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None

class CreateAccessEntryRequestRequestTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None
    type: Optional[str] = None

class KubernetesNetworkConfigRequestTypeDef(BaseModel):
    serviceIpv4Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None

class VpcConfigRequestTypeDef(BaseModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[Sequence[str]] = None

class EksAnywhereSubscriptionTermTypeDef(BaseModel):
    duration: Optional[int] = None
    unit: Optional[Literal["MONTHS"]] = None

class LaunchTemplateSpecificationTypeDef(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    id: Optional[str] = None

class NodegroupScalingConfigTypeDef(BaseModel):
    minSize: Optional[int] = None
    maxSize: Optional[int] = None
    desiredSize: Optional[int] = None

class NodegroupUpdateConfigTypeDef(BaseModel):
    maxUnavailable: Optional[int] = None
    maxUnavailablePercentage: Optional[int] = None

class RemoteAccessConfigTypeDef(BaseModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[Sequence[str]] = None

class TaintTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None
    effect: Optional[TaintEffectType] = None

class CreatePodIdentityAssociationRequestRequestTypeDef(BaseModel):
    clusterName: str
    namespace: str
    serviceAccount: str
    roleArn: str
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class PodIdentityAssociationTypeDef(BaseModel):
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

class DeleteAccessEntryRequestRequestTypeDef(BaseModel):
    clusterName: str
    principalArn: str

class DeleteAddonRequestRequestTypeDef(BaseModel):
    clusterName: str
    addonName: str
    preserve: Optional[bool] = None

class DeleteClusterRequestRequestTypeDef(BaseModel):
    name: str

class DeleteEksAnywhereSubscriptionRequestRequestTypeDef(BaseModel):
    id: str

class DeleteFargateProfileRequestRequestTypeDef(BaseModel):
    clusterName: str
    fargateProfileName: str

class DeleteNodegroupRequestRequestTypeDef(BaseModel):
    clusterName: str
    nodegroupName: str

class DeletePodIdentityAssociationRequestRequestTypeDef(BaseModel):
    clusterName: str
    associationId: str

class DeregisterClusterRequestRequestTypeDef(BaseModel):
    name: str

class DescribeAccessEntryRequestRequestTypeDef(BaseModel):
    clusterName: str
    principalArn: str

class DescribeAddonConfigurationRequestRequestTypeDef(BaseModel):
    addonName: str
    addonVersion: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAddonRequestRequestTypeDef(BaseModel):
    clusterName: str
    addonName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAddonVersionsRequestRequestTypeDef(BaseModel):
    kubernetesVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    addonName: Optional[str] = None
    types: Optional[Sequence[str]] = None
    publishers: Optional[Sequence[str]] = None
    owners: Optional[Sequence[str]] = None

class DescribeClusterRequestRequestTypeDef(BaseModel):
    name: str

class DescribeEksAnywhereSubscriptionRequestRequestTypeDef(BaseModel):
    id: str

class DescribeFargateProfileRequestRequestTypeDef(BaseModel):
    clusterName: str
    fargateProfileName: str

class IdentityProviderConfigTypeDef(BaseModel):
    type: str
    name: str

class DescribeInsightRequestRequestTypeDef(BaseModel):
    clusterName: str
    id: str

class DescribeNodegroupRequestRequestTypeDef(BaseModel):
    clusterName: str
    nodegroupName: str

class DescribePodIdentityAssociationRequestRequestTypeDef(BaseModel):
    clusterName: str
    associationId: str

class DescribeUpdateRequestRequestTypeDef(BaseModel):
    name: str
    updateId: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None

class DisassociateAccessPolicyRequestRequestTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    policyArn: str

class ProviderTypeDef(BaseModel):
    keyArn: Optional[str] = None

class ErrorDetailTypeDef(BaseModel):
    errorCode: Optional[ErrorCodeType] = None
    errorMessage: Optional[str] = None
    resourceIds: Optional[List[str]] = None

class FargateProfileIssueTypeDef(BaseModel):
    code: Optional[FargateProfileIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None

class FargateProfileSelectorOutputTypeDef(BaseModel):
    namespace: Optional[str] = None
    labels: Optional[Dict[str, str]] = None

class FargateProfileSelectorTypeDef(BaseModel):
    namespace: Optional[str] = None
    labels: Optional[Mapping[str, str]] = None

class OidcIdentityProviderConfigTypeDef(BaseModel):
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

class OIDCTypeDef(BaseModel):
    issuer: Optional[str] = None

class InsightStatusTypeDef(BaseModel):
    status: Optional[InsightStatusValueType] = None
    reason: Optional[str] = None

class InsightsFilterTypeDef(BaseModel):
    categories: Optional[Sequence[Literal["UPGRADE_READINESS"]]] = None
    kubernetesVersions: Optional[Sequence[str]] = None
    statuses: Optional[Sequence[InsightStatusValueType]] = None

class IssueTypeDef(BaseModel):
    code: Optional[NodegroupIssueCodeType] = None
    message: Optional[str] = None
    resourceIds: Optional[List[str]] = None

class ListAccessEntriesRequestRequestTypeDef(BaseModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAccessPoliciesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAddonsRequestRequestTypeDef(BaseModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAssociatedAccessPoliciesRequestRequestTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListClustersRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    include: Optional[Sequence[str]] = None

class ListEksAnywhereSubscriptionsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None

class ListFargateProfilesRequestRequestTypeDef(BaseModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdentityProviderConfigsRequestRequestTypeDef(BaseModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListNodegroupsRequestRequestTypeDef(BaseModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPodIdentityAssociationsRequestRequestTypeDef(BaseModel):
    clusterName: str
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PodIdentityAssociationSummaryTypeDef(BaseModel):
    clusterName: Optional[str] = None
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    associationArn: Optional[str] = None
    associationId: Optional[str] = None
    ownerArn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListUpdatesRequestRequestTypeDef(BaseModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LogSetupOutputTypeDef(BaseModel):
    types: Optional[List[LogTypeType]] = None
    enabled: Optional[bool] = None

class LogSetupTypeDef(BaseModel):
    types: Optional[Sequence[LogTypeType]] = None
    enabled: Optional[bool] = None

class RemoteAccessConfigOutputTypeDef(BaseModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessConfigRequestTypeDef(BaseModel):
    authenticationMode: Optional[AuthenticationModeType] = None

class UpdateAccessEntryRequestRequestTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[Sequence[str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None

class UpdateClusterVersionRequestRequestTypeDef(BaseModel):
    name: str
    version: str
    clientRequestToken: Optional[str] = None

class UpdateEksAnywhereSubscriptionRequestRequestTypeDef(BaseModel):
    id: str
    autoRenew: bool
    clientRequestToken: Optional[str] = None

class UpdateLabelsPayloadTypeDef(BaseModel):
    addOrUpdateLabels: Optional[Mapping[str, str]] = None
    removeLabels: Optional[Sequence[str]] = None

class UpdateParamTypeDef(BaseModel):
    type: Optional[UpdateParamTypeType] = None
    value: Optional[str] = None

class UpdatePodIdentityAssociationRequestRequestTypeDef(BaseModel):
    clusterName: str
    associationId: str
    roleArn: Optional[str] = None
    clientRequestToken: Optional[str] = None

class AssociatedAccessPolicyTypeDef(BaseModel):
    policyArn: Optional[str] = None
    accessScope: Optional[AccessScopeOutputTypeDef] = None
    associatedAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None

class AssociateAccessPolicyRequestRequestTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    policyArn: str
    accessScope: AccessScopeTypeDef

class AddonHealthTypeDef(BaseModel):
    issues: Optional[List[AddonIssueTypeDef]] = None

class CreateAddonRequestRequestTypeDef(BaseModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[Sequence[AddonPodIdentityAssociationsTypeDef]] = None

class UpdateAddonRequestRequestTypeDef(BaseModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[Sequence[AddonPodIdentityAssociationsTypeDef]] = None

class AddonVersionInfoTypeDef(BaseModel):
    addonVersion: Optional[str] = None
    architecture: Optional[List[str]] = None
    compatibilities: Optional[List[CompatibilityTypeDef]] = None
    requiresConfiguration: Optional[bool] = None
    requiresIamPermissions: Optional[bool] = None

class CreateAccessEntryResponseTypeDef(BaseModel):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessEntryResponseTypeDef(BaseModel):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonConfigurationResponseTypeDef(BaseModel):
    addonName: str
    addonVersion: str
    configurationSchema: str
    podIdentityConfiguration: List[AddonPodIdentityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessEntriesResponseTypeDef(BaseModel):
    accessEntries: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPoliciesResponseTypeDef(BaseModel):
    accessPolicies: List[AccessPolicyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAddonsResponseTypeDef(BaseModel):
    addons: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersResponseTypeDef(BaseModel):
    clusters: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFargateProfilesResponseTypeDef(BaseModel):
    fargateProfileNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNodegroupsResponseTypeDef(BaseModel):
    nodegroups: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListUpdatesResponseTypeDef(BaseModel):
    updateIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessEntryResponseTypeDef(BaseModel):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIdentityProviderConfigRequestRequestTypeDef(BaseModel):
    clusterName: str
    oidc: OidcIdentityProviderConfigRequestTypeDef
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None

class NodegroupResourcesTypeDef(BaseModel):
    autoScalingGroups: Optional[List[AutoScalingGroupTypeDef]] = None
    remoteAccessSecurityGroup: Optional[str] = None

class DeprecationDetailTypeDef(BaseModel):
    usage: Optional[str] = None
    replacedWith: Optional[str] = None
    stopServingVersion: Optional[str] = None
    startServingReplacementVersion: Optional[str] = None
    clientStats: Optional[List[ClientStatTypeDef]] = None

class ClusterHealthTypeDef(BaseModel):
    issues: Optional[List[ClusterIssueTypeDef]] = None

class RegisterClusterRequestRequestTypeDef(BaseModel):
    name: str
    connectorConfig: ConnectorConfigRequestTypeDef
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class OutpostConfigRequestTypeDef(BaseModel):
    outpostArns: Sequence[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementRequestTypeDef] = None

class OutpostConfigResponseTypeDef(BaseModel):
    outpostArns: List[str]
    controlPlaneInstanceType: str
    controlPlanePlacement: Optional[ControlPlanePlacementResponseTypeDef] = None

class CreateEksAnywhereSubscriptionRequestRequestTypeDef(BaseModel):
    name: str
    term: EksAnywhereSubscriptionTermTypeDef
    licenseQuantity: Optional[int] = None
    licenseType: Optional[Literal["Cluster"]] = None
    autoRenew: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class EksAnywhereSubscriptionTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    effectiveDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    licenseQuantity: Optional[int] = None
    licenseType: Optional[Literal["Cluster"]] = None
    term: Optional[EksAnywhereSubscriptionTermTypeDef] = None
    status: Optional[str] = None
    autoRenew: Optional[bool] = None
    licenseArns: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None

class UpdateNodegroupVersionRequestRequestTypeDef(BaseModel):
    clusterName: str
    nodegroupName: str
    version: Optional[str] = None
    releaseVersion: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    force: Optional[bool] = None
    clientRequestToken: Optional[str] = None

class CreateNodegroupRequestRequestTypeDef(BaseModel):
    clusterName: str
    nodegroupName: str
    subnets: Sequence[str]
    nodeRole: str
    scalingConfig: Optional[NodegroupScalingConfigTypeDef] = None
    diskSize: Optional[int] = None
    instanceTypes: Optional[Sequence[str]] = None
    amiType: Optional[AMITypesType] = None
    remoteAccess: Optional[RemoteAccessConfigTypeDef] = None
    labels: Optional[Mapping[str, str]] = None
    taints: Optional[Sequence[TaintTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    updateConfig: Optional[NodegroupUpdateConfigTypeDef] = None
    capacityType: Optional[CapacityTypesType] = None
    version: Optional[str] = None
    releaseVersion: Optional[str] = None

class UpdateTaintsPayloadTypeDef(BaseModel):
    addOrUpdateTaints: Optional[Sequence[TaintTypeDef]] = None
    removeTaints: Optional[Sequence[TaintTypeDef]] = None

class CreatePodIdentityAssociationResponseTypeDef(BaseModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePodIdentityAssociationResponseTypeDef(BaseModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePodIdentityAssociationResponseTypeDef(BaseModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePodIdentityAssociationResponseTypeDef(BaseModel):
    association: PodIdentityAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonRequestAddonActiveWaitTypeDef(BaseModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAddonRequestAddonDeletedWaitTypeDef(BaseModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterRequestClusterActiveWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterRequestClusterDeletedWaitTypeDef(BaseModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFargateProfileRequestFargateProfileActiveWaitTypeDef(BaseModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFargateProfileRequestFargateProfileDeletedWaitTypeDef(BaseModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNodegroupRequestNodegroupActiveWaitTypeDef(BaseModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNodegroupRequestNodegroupDeletedWaitTypeDef(BaseModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAddonVersionsRequestDescribeAddonVersionsPaginateTypeDef(BaseModel):
    kubernetesVersion: Optional[str] = None
    addonName: Optional[str] = None
    types: Optional[Sequence[str]] = None
    publishers: Optional[Sequence[str]] = None
    owners: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessEntriesRequestListAccessEntriesPaginateTypeDef(BaseModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAddonsRequestListAddonsPaginateTypeDef(BaseModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedAccessPoliciesRequestListAssociatedAccessPoliciesPaginateTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseModel):
    include: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEksAnywhereSubscriptionsRequestListEksAnywhereSubscriptionsPaginateTypeDef(BaseModel):
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFargateProfilesRequestListFargateProfilesPaginateTypeDef(BaseModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdentityProviderConfigsRequestListIdentityProviderConfigsPaginateTypeDef(BaseModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNodegroupsRequestListNodegroupsPaginateTypeDef(BaseModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPodIdentityAssociationsRequestListPodIdentityAssociationsPaginateTypeDef(BaseModel):
    clusterName: str
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUpdatesRequestListUpdatesPaginateTypeDef(BaseModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIdentityProviderConfigRequestRequestTypeDef(BaseModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef

class DisassociateIdentityProviderConfigRequestRequestTypeDef(BaseModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef
    clientRequestToken: Optional[str] = None

class ListIdentityProviderConfigsResponseTypeDef(BaseModel):
    identityProviderConfigs: List[IdentityProviderConfigTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptionConfigOutputTypeDef(BaseModel):
    resources: Optional[List[str]] = None
    provider: Optional[ProviderTypeDef] = None

class EncryptionConfigTypeDef(BaseModel):
    resources: Optional[Sequence[str]] = None
    provider: Optional[ProviderTypeDef] = None

class FargateProfileHealthTypeDef(BaseModel):
    issues: Optional[List[FargateProfileIssueTypeDef]] = None

class IdentityProviderConfigResponseTypeDef(BaseModel):
    oidc: Optional[OidcIdentityProviderConfigTypeDef] = None

class IdentityTypeDef(BaseModel):
    oidc: Optional[OIDCTypeDef] = None

class InsightResourceDetailTypeDef(BaseModel):
    insightStatus: Optional[InsightStatusTypeDef] = None
    kubernetesResourceUri: Optional[str] = None
    arn: Optional[str] = None

class InsightSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    category: Optional[Literal["UPGRADE_READINESS"]] = None
    kubernetesVersion: Optional[str] = None
    lastRefreshTime: Optional[datetime] = None
    lastTransitionTime: Optional[datetime] = None
    description: Optional[str] = None
    insightStatus: Optional[InsightStatusTypeDef] = None

class ListInsightsRequestListInsightsPaginateTypeDef(BaseModel):
    clusterName: str
    filter: Optional[InsightsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsRequestRequestTypeDef(BaseModel):
    clusterName: str
    filter: Optional[InsightsFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NodegroupHealthTypeDef(BaseModel):
    issues: Optional[List[IssueTypeDef]] = None

class ListPodIdentityAssociationsResponseTypeDef(BaseModel):
    associations: List[PodIdentityAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingOutputTypeDef(BaseModel):
    clusterLogging: Optional[List[LogSetupOutputTypeDef]] = None

class LoggingTypeDef(BaseModel):
    clusterLogging: Optional[Sequence[LogSetupTypeDef]] = None

class UpdateTypeDef(BaseModel):
    id: Optional[str] = None
    status: Optional[UpdateStatusType] = None
    type: Optional[UpdateTypeType] = None
    params: Optional[List[UpdateParamTypeDef]] = None
    createdAt: Optional[datetime] = None
    errors: Optional[List[ErrorDetailTypeDef]] = None

class AssociateAccessPolicyResponseTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicy: AssociatedAccessPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedAccessPoliciesResponseTypeDef(BaseModel):
    clusterName: str
    principalArn: str
    nextToken: str
    associatedAccessPolicies: List[AssociatedAccessPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AddonTypeDef(BaseModel):
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

class AddonInfoTypeDef(BaseModel):
    addonName: Optional[str] = None
    type: Optional[str] = None
    addonVersions: Optional[List[AddonVersionInfoTypeDef]] = None
    publisher: Optional[str] = None
    owner: Optional[str] = None
    marketplaceInformation: Optional[MarketplaceInformationTypeDef] = None

class InsightCategorySpecificSummaryTypeDef(BaseModel):
    deprecationDetails: Optional[List[DeprecationDetailTypeDef]] = None

class CreateEksAnywhereSubscriptionResponseTypeDef(BaseModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEksAnywhereSubscriptionResponseTypeDef(BaseModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEksAnywhereSubscriptionResponseTypeDef(BaseModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEksAnywhereSubscriptionsResponseTypeDef(BaseModel):
    subscriptions: List[EksAnywhereSubscriptionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEksAnywhereSubscriptionResponseTypeDef(BaseModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNodegroupConfigRequestRequestTypeDef(BaseModel):
    clusterName: str
    nodegroupName: str
    labels: Optional[UpdateLabelsPayloadTypeDef] = None
    taints: Optional[UpdateTaintsPayloadTypeDef] = None
    scalingConfig: Optional[NodegroupScalingConfigTypeDef] = None
    updateConfig: Optional[NodegroupUpdateConfigTypeDef] = None
    clientRequestToken: Optional[str] = None

class FargateProfileTypeDef(BaseModel):
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

class CreateFargateProfileRequestRequestTypeDef(BaseModel):
    fargateProfileName: str
    clusterName: str
    podExecutionRoleArn: str
    subnets: Optional[Sequence[str]] = None
    selectors: Optional[Sequence[FargateProfileSelectorUnionTypeDef]] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DescribeIdentityProviderConfigResponseTypeDef(BaseModel):
    identityProviderConfig: IdentityProviderConfigResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInsightsResponseTypeDef(BaseModel):
    insights: List[InsightSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NodegroupTypeDef(BaseModel):
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
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class ClusterTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    version: Optional[str] = None
    endpoint: Optional[str] = None
    roleArn: Optional[str] = None
    resourcesVpcConfig: Optional[VpcConfigResponseTypeDef] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigResponseTypeDef] = None
    logging: Optional[LoggingOutputTypeDef] = None
    identity: Optional[IdentityTypeDef] = None
    status: Optional[ClusterStatusType] = None
    certificateAuthority: Optional[CertificateTypeDef] = None
    clientRequestToken: Optional[str] = None
    platformVersion: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    encryptionConfig: Optional[List[EncryptionConfigOutputTypeDef]] = None
    connectorConfig: Optional[ConnectorConfigResponseTypeDef] = None
    id: Optional[str] = None
    health: Optional[ClusterHealthTypeDef] = None
    outpostConfig: Optional[OutpostConfigResponseTypeDef] = None
    accessConfig: Optional[AccessConfigResponseTypeDef] = None

class UpdateClusterConfigRequestRequestTypeDef(BaseModel):
    name: str
    resourcesVpcConfig: Optional[VpcConfigRequestTypeDef] = None
    logging: Optional[LoggingTypeDef] = None
    clientRequestToken: Optional[str] = None
    accessConfig: Optional[UpdateAccessConfigRequestTypeDef] = None

class AssociateEncryptionConfigResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIdentityProviderConfigResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUpdateResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateIdentityProviderConfigResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAddonResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterConfigResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterVersionResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNodegroupConfigResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNodegroupVersionResponseTypeDef(BaseModel):
    update: UpdateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAddonResponseTypeDef(BaseModel):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAddonResponseTypeDef(BaseModel):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonResponseTypeDef(BaseModel):
    addon: AddonTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddonVersionsResponseTypeDef(BaseModel):
    addons: List[AddonInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InsightTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    category: Optional[Literal["UPGRADE_READINESS"]] = None
    kubernetesVersion: Optional[str] = None
    lastRefreshTime: Optional[datetime] = None
    lastTransitionTime: Optional[datetime] = None
    description: Optional[str] = None
    insightStatus: Optional[InsightStatusTypeDef] = None
    recommendation: Optional[str] = None
    additionalInfo: Optional[Dict[str, str]] = None
    resources: Optional[List[InsightResourceDetailTypeDef]] = None
    categorySpecificSummary: Optional[InsightCategorySpecificSummaryTypeDef] = None

class AssociateEncryptionConfigRequestRequestTypeDef(BaseModel):
    clusterName: str
    encryptionConfig: Sequence[EncryptionConfigUnionTypeDef]
    clientRequestToken: Optional[str] = None

class CreateClusterRequestRequestTypeDef(BaseModel):
    name: str
    roleArn: str
    resourcesVpcConfig: VpcConfigRequestTypeDef
    version: Optional[str] = None
    kubernetesNetworkConfig: Optional[KubernetesNetworkConfigRequestTypeDef] = None
    logging: Optional[LoggingTypeDef] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    encryptionConfig: Optional[Sequence[EncryptionConfigUnionTypeDef]] = None
    outpostConfig: Optional[OutpostConfigRequestTypeDef] = None
    accessConfig: Optional[CreateAccessConfigRequestTypeDef] = None
    bootstrapSelfManagedAddons: Optional[bool] = None

class CreateFargateProfileResponseTypeDef(BaseModel):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFargateProfileResponseTypeDef(BaseModel):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFargateProfileResponseTypeDef(BaseModel):
    fargateProfile: FargateProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNodegroupResponseTypeDef(BaseModel):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNodegroupResponseTypeDef(BaseModel):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNodegroupResponseTypeDef(BaseModel):
    nodegroup: NodegroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInsightResponseTypeDef(BaseModel):
    insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

