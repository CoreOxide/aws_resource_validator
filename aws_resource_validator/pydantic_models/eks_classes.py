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
from aws_resource_validator.pydantic_models.eks_constants import *

class AccessConfigResponseTypeDef(BaseValidatorModel):
    bootstrapClusterCreatorAdminPermissions: Optional[bool] = None
    authenticationMode: Optional[AuthenticationModeType] = None

class AccessEntryTypeDef(BaseValidatorModel):
    clusterName: Optional[str] = None
    principalArn: Optional[str] = None
    kubernetesGroups: Optional[List[str]] = None
    accessEntryArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    username: Optional[str] = None
    type: Optional[str] = None

class AccessPolicyTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None

class AccessScopeExtraOutputTypeDef(BaseValidatorModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[List[str]] = None

class AccessScopeOutputTypeDef(BaseValidatorModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[List[str]] = None

class AccessScopeTypeDef(BaseValidatorModel):
    type: Optional[AccessScopeTypeType] = None
    namespaces: Optional[Sequence[str]] = None

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

class ConnectorConfigResponseTypeDef(BaseValidatorModel):
    activationId: Optional[str] = None
    activationCode: Optional[str] = None
    activationExpiry: Optional[datetime] = None
    provider: Optional[str] = None
    roleArn: Optional[str] = None

class KubernetesNetworkConfigResponseTypeDef(BaseValidatorModel):
    serviceIpv4Cidr: Optional[str] = None
    serviceIpv6Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None

class VpcConfigResponseTypeDef(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    clusterSecurityGroupId: Optional[str] = None
    vpcId: Optional[str] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[List[str]] = None

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

class CreateAccessEntryRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None
    type: Optional[str] = None

class KubernetesNetworkConfigRequestTypeDef(BaseValidatorModel):
    serviceIpv4Cidr: Optional[str] = None
    ipFamily: Optional[IpFamilyType] = None

class VpcConfigRequestTypeDef(BaseValidatorModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    endpointPublicAccess: Optional[bool] = None
    endpointPrivateAccess: Optional[bool] = None
    publicAccessCidrs: Optional[Sequence[str]] = None

class EksAnywhereSubscriptionTermTypeDef(BaseValidatorModel):
    duration: Optional[int] = None
    unit: Optional[Literal["MONTHS"]] = None

class LaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[str] = None
    id: Optional[str] = None

class NodegroupScalingConfigTypeDef(BaseValidatorModel):
    minSize: Optional[int] = None
    maxSize: Optional[int] = None
    desiredSize: Optional[int] = None

class NodegroupUpdateConfigTypeDef(BaseValidatorModel):
    maxUnavailable: Optional[int] = None
    maxUnavailablePercentage: Optional[int] = None

class RemoteAccessConfigTypeDef(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[Sequence[str]] = None

class TaintTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None
    effect: Optional[TaintEffectType] = None

class CreatePodIdentityAssociationRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteAccessEntryRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str

class DeleteAddonRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    preserve: Optional[bool] = None

class DeleteClusterRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteEksAnywhereSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteFargateProfileRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str

class DeleteNodegroupRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str

class DeletePodIdentityAssociationRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associationId: str

class DeregisterClusterRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DescribeAccessEntryRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str

class DescribeAddonConfigurationRequestRequestTypeDef(BaseValidatorModel):
    addonName: str
    addonVersion: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeAddonRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAddonVersionsRequestRequestTypeDef(BaseValidatorModel):
    kubernetesVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    addonName: Optional[str] = None
    types: Optional[Sequence[str]] = None
    publishers: Optional[Sequence[str]] = None
    owners: Optional[Sequence[str]] = None

class DescribeClusterRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DescribeEksAnywhereSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DescribeFargateProfileRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str

class IdentityProviderConfigTypeDef(BaseValidatorModel):
    type: str
    name: str

class DescribeInsightRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    id: str

class DescribeNodegroupRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str

class DescribePodIdentityAssociationRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associationId: str

class DescribeUpdateRequestRequestTypeDef(BaseValidatorModel):
    name: str
    updateId: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None

class DisassociateAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    policyArn: str

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

class ListAccessEntriesRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAccessPoliciesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAddonsRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAssociatedAccessPoliciesRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListClustersRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    include: Optional[Sequence[str]] = None

class ListEksAnywhereSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None

class ListFargateProfilesRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdentityProviderConfigsRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListNodegroupsRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPodIdentityAssociationsRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListUpdatesRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LogSetupOutputTypeDef(BaseValidatorModel):
    types: Optional[List[LogTypeType]] = None
    enabled: Optional[bool] = None

class LogSetupTypeDef(BaseValidatorModel):
    types: Optional[Sequence[LogTypeType]] = None
    enabled: Optional[bool] = None

class RemoteAccessConfigOutputTypeDef(BaseValidatorModel):
    ec2SshKey: Optional[str] = None
    sourceSecurityGroups: Optional[List[str]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessConfigRequestTypeDef(BaseValidatorModel):
    authenticationMode: Optional[AuthenticationModeType] = None

class UpdateAccessEntryRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    kubernetesGroups: Optional[Sequence[str]] = None
    clientRequestToken: Optional[str] = None
    username: Optional[str] = None

class UpdateClusterVersionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    version: str
    clientRequestToken: Optional[str] = None

class UpdateEksAnywhereSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    id: str
    autoRenew: bool
    clientRequestToken: Optional[str] = None

class UpdateLabelsPayloadTypeDef(BaseValidatorModel):
    addOrUpdateLabels: Optional[Mapping[str, str]] = None
    removeLabels: Optional[Sequence[str]] = None

class UpdateParamTypeDef(BaseValidatorModel):
    type: Optional[UpdateParamTypeType] = None
    value: Optional[str] = None

class UpdatePodIdentityAssociationRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    associationId: str
    roleArn: Optional[str] = None
    clientRequestToken: Optional[str] = None

class AssociatedAccessPolicyTypeDef(BaseValidatorModel):
    policyArn: Optional[str] = None
    accessScope: Optional[AccessScopeOutputTypeDef] = None
    associatedAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None

class AssociateAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    policyArn: str
    accessScope: AccessScopeTypeDef

class AddonHealthTypeDef(BaseValidatorModel):
    issues: Optional[List[AddonIssueTypeDef]] = None

class CreateAddonRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    addonVersion: Optional[str] = None
    serviceAccountRoleArn: Optional[str] = None
    resolveConflicts: Optional[ResolveConflictsType] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    configurationValues: Optional[str] = None
    podIdentityAssociations: Optional[Sequence[AddonPodIdentityAssociationsTypeDef]] = None

class UpdateAddonRequestRequestTypeDef(BaseValidatorModel):
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
    compatibilities: Optional[List[CompatibilityTypeDef]] = None
    requiresConfiguration: Optional[bool] = None
    requiresIamPermissions: Optional[bool] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPoliciesResponseTypeDef(BaseValidatorModel):
    accessPolicies: List[AccessPolicyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAddonsResponseTypeDef(BaseValidatorModel):
    addons: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersResponseTypeDef(BaseValidatorModel):
    clusters: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFargateProfilesResponseTypeDef(BaseValidatorModel):
    fargateProfileNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListNodegroupsResponseTypeDef(BaseValidatorModel):
    nodegroups: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListUpdatesResponseTypeDef(BaseValidatorModel):
    updateIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessEntryResponseTypeDef(BaseValidatorModel):
    accessEntry: AccessEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateIdentityProviderConfigRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    oidc: OidcIdentityProviderConfigRequestTypeDef
    tags: Optional[Mapping[str, str]] = None
    clientRequestToken: Optional[str] = None

class NodegroupResourcesTypeDef(BaseValidatorModel):
    autoScalingGroups: Optional[List[AutoScalingGroupTypeDef]] = None
    remoteAccessSecurityGroup: Optional[str] = None

class DeprecationDetailTypeDef(BaseValidatorModel):
    usage: Optional[str] = None
    replacedWith: Optional[str] = None
    stopServingVersion: Optional[str] = None
    startServingReplacementVersion: Optional[str] = None
    clientStats: Optional[List[ClientStatTypeDef]] = None

class ClusterHealthTypeDef(BaseValidatorModel):
    issues: Optional[List[ClusterIssueTypeDef]] = None

class RegisterClusterRequestRequestTypeDef(BaseValidatorModel):
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

class CreateEksAnywhereSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    term: EksAnywhereSubscriptionTermTypeDef
    licenseQuantity: Optional[int] = None
    licenseType: Optional[Literal["Cluster"]] = None
    autoRenew: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class EksAnywhereSubscriptionTypeDef(BaseValidatorModel):
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

class UpdateNodegroupVersionRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    version: Optional[str] = None
    releaseVersion: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    force: Optional[bool] = None
    clientRequestToken: Optional[str] = None

class CreateNodegroupRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeAddonRequestAddonActiveWaitTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAddonRequestAddonDeletedWaitTypeDef(BaseValidatorModel):
    clusterName: str
    addonName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterRequestClusterActiveWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterRequestClusterDeletedWaitTypeDef(BaseValidatorModel):
    name: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFargateProfileRequestFargateProfileActiveWaitTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFargateProfileRequestFargateProfileDeletedWaitTypeDef(BaseValidatorModel):
    clusterName: str
    fargateProfileName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNodegroupRequestNodegroupActiveWaitTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNodegroupRequestNodegroupDeletedWaitTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeAddonVersionsRequestDescribeAddonVersionsPaginateTypeDef(BaseValidatorModel):
    kubernetesVersion: Optional[str] = None
    addonName: Optional[str] = None
    types: Optional[Sequence[str]] = None
    publishers: Optional[Sequence[str]] = None
    owners: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessEntriesRequestListAccessEntriesPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    associatedPolicyArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessPoliciesRequestListAccessPoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAddonsRequestListAddonsPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedAccessPoliciesRequestListAssociatedAccessPoliciesPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseValidatorModel):
    include: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEksAnywhereSubscriptionsRequestListEksAnywhereSubscriptionsPaginateTypeDef(BaseValidatorModel):
    includeStatus: Optional[Sequence[EksAnywhereSubscriptionStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFargateProfilesRequestListFargateProfilesPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdentityProviderConfigsRequestListIdentityProviderConfigsPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNodegroupsRequestListNodegroupsPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPodIdentityAssociationsRequestListPodIdentityAssociationsPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    namespace: Optional[str] = None
    serviceAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUpdatesRequestListUpdatesPaginateTypeDef(BaseValidatorModel):
    name: str
    nodegroupName: Optional[str] = None
    addonName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIdentityProviderConfigRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef

class DisassociateIdentityProviderConfigRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    identityProviderConfig: IdentityProviderConfigTypeDef
    clientRequestToken: Optional[str] = None

class ListIdentityProviderConfigsResponseTypeDef(BaseValidatorModel):
    identityProviderConfigs: List[IdentityProviderConfigTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class InsightSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    category: Optional[Literal["UPGRADE_READINESS"]] = None
    kubernetesVersion: Optional[str] = None
    lastRefreshTime: Optional[datetime] = None
    lastTransitionTime: Optional[datetime] = None
    description: Optional[str] = None
    insightStatus: Optional[InsightStatusTypeDef] = None

class ListInsightsRequestListInsightsPaginateTypeDef(BaseValidatorModel):
    clusterName: str
    filter: Optional[InsightsFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    filter: Optional[InsightsFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class NodegroupHealthTypeDef(BaseValidatorModel):
    issues: Optional[List[IssueTypeDef]] = None

class ListPodIdentityAssociationsResponseTypeDef(BaseValidatorModel):
    associations: List[PodIdentityAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingOutputTypeDef(BaseValidatorModel):
    clusterLogging: Optional[List[LogSetupOutputTypeDef]] = None

class LoggingTypeDef(BaseValidatorModel):
    clusterLogging: Optional[Sequence[LogSetupTypeDef]] = None

class UpdateTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    status: Optional[UpdateStatusType] = None
    type: Optional[UpdateTypeType] = None
    params: Optional[List[UpdateParamTypeDef]] = None
    createdAt: Optional[datetime] = None
    errors: Optional[List[ErrorDetailTypeDef]] = None

class AssociateAccessPolicyResponseTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    associatedAccessPolicy: AssociatedAccessPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedAccessPoliciesResponseTypeDef(BaseValidatorModel):
    clusterName: str
    principalArn: str
    nextToken: str
    associatedAccessPolicies: List[AssociatedAccessPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class AddonInfoTypeDef(BaseValidatorModel):
    addonName: Optional[str] = None
    type: Optional[str] = None
    addonVersions: Optional[List[AddonVersionInfoTypeDef]] = None
    publisher: Optional[str] = None
    owner: Optional[str] = None
    marketplaceInformation: Optional[MarketplaceInformationTypeDef] = None

class InsightCategorySpecificSummaryTypeDef(BaseValidatorModel):
    deprecationDetails: Optional[List[DeprecationDetailTypeDef]] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEksAnywhereSubscriptionResponseTypeDef(BaseValidatorModel):
    subscription: EksAnywhereSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNodegroupConfigRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    nodegroupName: str
    labels: Optional[UpdateLabelsPayloadTypeDef] = None
    taints: Optional[UpdateTaintsPayloadTypeDef] = None
    scalingConfig: Optional[NodegroupScalingConfigTypeDef] = None
    updateConfig: Optional[NodegroupUpdateConfigTypeDef] = None
    clientRequestToken: Optional[str] = None

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

class CreateFargateProfileRequestRequestTypeDef(BaseValidatorModel):
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

class ListInsightsResponseTypeDef(BaseValidatorModel):
    insights: List[InsightSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class ClusterTypeDef(BaseValidatorModel):
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

class UpdateClusterConfigRequestRequestTypeDef(BaseValidatorModel):
    name: str
    resourcesVpcConfig: Optional[VpcConfigRequestTypeDef] = None
    logging: Optional[LoggingTypeDef] = None
    clientRequestToken: Optional[str] = None
    accessConfig: Optional[UpdateAccessConfigRequestTypeDef] = None

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

class DescribeAddonVersionsResponseTypeDef(BaseValidatorModel):
    addons: List[AddonInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InsightTypeDef(BaseValidatorModel):
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

class AssociateEncryptionConfigRequestRequestTypeDef(BaseValidatorModel):
    clusterName: str
    encryptionConfig: Sequence[EncryptionConfigUnionTypeDef]
    clientRequestToken: Optional[str] = None

class CreateClusterRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeInsightResponseTypeDef(BaseValidatorModel):
    insight: InsightTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

