from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.opensearchserverless.opensearchserverless_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessPolicyDetail(BaseValidatorModel):
    type: Optional[Literal['data']] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


class AccessPolicyStats(BaseValidatorModel):
    DataPolicyCount: Optional[int] = None


class AccessPolicySummary(BaseValidatorModel):
    type: Optional[Literal['data']] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


class CapacityLimits(BaseValidatorModel):
    maxIndexingCapacityInOCU: Optional[int] = None
    maxSearchCapacityInOCU: Optional[int] = None


# This class is the input for the 'batch_get_collection' function.
class BatchGetCollectionRequest(BaseValidatorModel):
    ids: Optional[List[str]] = None
    names: Optional[List[str]] = None


class CollectionDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None
    type: Optional[CollectionTypeType] = None
    description: Optional[str] = None
    arn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    standbyReplicas: Optional[StandbyReplicasType] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None
    collectionEndpoint: Optional[str] = None
    dashboardEndpoint: Optional[str] = None
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None


class CollectionErrorDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LifecyclePolicyResourceIdentifier(BaseValidatorModel):
    type: Literal['retention']
    resource: str


class EffectiveLifecyclePolicyDetail(BaseValidatorModel):
    type: Optional[Literal['retention']] = None
    resource: Optional[str] = None
    policyName: Optional[str] = None
    resourceType: Optional[Literal['index']] = None
    retentionPeriod: Optional[str] = None
    noMinRetentionPeriod: Optional[bool] = None


class EffectiveLifecyclePolicyErrorDetail(BaseValidatorModel):
    type: Optional[Literal['retention']] = None
    resource: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None


class LifecyclePolicyIdentifier(BaseValidatorModel):
    type: Literal['retention']
    name: str


class LifecyclePolicyDetail(BaseValidatorModel):
    type: Optional[Literal['retention']] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


class LifecyclePolicyErrorDetail(BaseValidatorModel):
    type: Optional[Literal['retention']] = None
    name: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None


# This class is the input for the 'batch_get_vpc_endpoint' function.
class BatchGetVpcEndpointRequest(BaseValidatorModel):
    ids: List[str]


class VpcEndpointDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    vpcId: Optional[str] = None
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[VpcEndpointStatusType] = None
    createdDate: Optional[int] = None
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None


class VpcEndpointErrorDetail(BaseValidatorModel):
    id: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None


class CollectionFilters(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None


class CollectionSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None
    arn: Optional[str] = None


# This class is the input for the 'create_access_policy' function.
class CreateAccessPolicyRequest(BaseValidatorModel):
    type: Literal['data']
    name: str
    policy: str
    description: Optional[str] = None
    clientToken: Optional[str] = None


class CreateCollectionDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None
    type: Optional[CollectionTypeType] = None
    description: Optional[str] = None
    arn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    standbyReplicas: Optional[StandbyReplicasType] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class CreateIamIdentityCenterConfigOptions(BaseValidatorModel):
    instanceArn: str
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


# This class is the input for the 'create_lifecycle_policy' function.
class CreateLifecyclePolicyRequest(BaseValidatorModel):
    type: Literal['retention']
    name: str
    policy: str
    description: Optional[str] = None
    clientToken: Optional[str] = None


class SamlConfigOptions(BaseValidatorModel):
    metadata: str
    userAttribute: Optional[str] = None
    groupAttribute: Optional[str] = None
    openSearchServerlessEntityId: Optional[str] = None
    sessionTimeout: Optional[int] = None


# This class is the input for the 'create_security_policy' function.
class CreateSecurityPolicyRequest(BaseValidatorModel):
    type: SecurityPolicyTypeType
    name: str
    policy: str
    description: Optional[str] = None
    clientToken: Optional[str] = None


class SecurityPolicyDetail(BaseValidatorModel):
    type: Optional[SecurityPolicyTypeType] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


class CreateVpcEndpointDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None


# This class is the input for the 'create_vpc_endpoint' function.
class CreateVpcEndpointRequest(BaseValidatorModel):
    name: str
    vpcId: str
    subnetIds: List[str]
    securityGroupIds: Optional[List[str]] = None
    clientToken: Optional[str] = None


class DeleteAccessPolicyRequest(BaseValidatorModel):
    type: Literal['data']
    name: str
    clientToken: Optional[str] = None


class DeleteCollectionDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None


# This class is the input for the 'delete_collection' function.
class DeleteCollectionRequest(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None


class DeleteLifecyclePolicyRequest(BaseValidatorModel):
    type: Literal['retention']
    name: str
    clientToken: Optional[str] = None


class DeleteSecurityConfigRequest(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None


class DeleteSecurityPolicyRequest(BaseValidatorModel):
    type: SecurityPolicyTypeType
    name: str
    clientToken: Optional[str] = None


class DeleteVpcEndpointDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None


# This class is the input for the 'delete_vpc_endpoint' function.
class DeleteVpcEndpointRequest(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None


# This class is the input for the 'get_access_policy' function.
class GetAccessPolicyRequest(BaseValidatorModel):
    type: Literal['data']
    name: str


class LifecyclePolicyStats(BaseValidatorModel):
    RetentionPolicyCount: Optional[int] = None


class SecurityConfigStats(BaseValidatorModel):
    SamlConfigCount: Optional[int] = None


class SecurityPolicyStats(BaseValidatorModel):
    EncryptionPolicyCount: Optional[int] = None
    NetworkPolicyCount: Optional[int] = None


# This class is the input for the 'get_security_config' function.
class GetSecurityConfigRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_security_policy' function.
class GetSecurityPolicyRequest(BaseValidatorModel):
    type: SecurityPolicyTypeType
    name: str


class IamIdentityCenterConfigOptions(BaseValidatorModel):
    instanceArn: Optional[str] = None
    applicationArn: Optional[str] = None
    applicationName: Optional[str] = None
    applicationDescription: Optional[str] = None
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


class LifecyclePolicySummary(BaseValidatorModel):
    type: Optional[Literal['retention']] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


# This class is the input for the 'list_access_policies' function.
class ListAccessPoliciesRequest(BaseValidatorModel):
    type: Literal['data']
    resource: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_lifecycle_policies' function.
class ListLifecyclePoliciesRequest(BaseValidatorModel):
    type: Literal['retention']
    resources: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_security_configs' function.
class ListSecurityConfigsRequest(BaseValidatorModel):
    type: SecurityConfigTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SecurityConfigSummary(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[SecurityConfigTypeType] = None
    configVersion: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


# This class is the input for the 'list_security_policies' function.
class ListSecurityPoliciesRequest(BaseValidatorModel):
    type: SecurityPolicyTypeType
    resource: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SecurityPolicySummary(BaseValidatorModel):
    type: Optional[SecurityPolicyTypeType] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    description: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class VpcEndpointFilters(BaseValidatorModel):
    status: Optional[VpcEndpointStatusType] = None


class VpcEndpointSummary(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_access_policy' function.
class UpdateAccessPolicyRequest(BaseValidatorModel):
    type: Literal['data']
    name: str
    policyVersion: str
    description: Optional[str] = None
    policy: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateCollectionDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None
    type: Optional[CollectionTypeType] = None
    description: Optional[str] = None
    arn: Optional[str] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


# This class is the input for the 'update_collection' function.
class UpdateCollectionRequest(BaseValidatorModel):
    id: str
    description: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateIamIdentityCenterConfigOptions(BaseValidatorModel):
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


# This class is the input for the 'update_lifecycle_policy' function.
class UpdateLifecyclePolicyRequest(BaseValidatorModel):
    type: Literal['retention']
    name: str
    policyVersion: str
    description: Optional[str] = None
    policy: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_security_policy' function.
class UpdateSecurityPolicyRequest(BaseValidatorModel):
    type: SecurityPolicyTypeType
    name: str
    policyVersion: str
    description: Optional[str] = None
    policy: Optional[str] = None
    clientToken: Optional[str] = None


class UpdateVpcEndpointDetail(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    lastModifiedDate: Optional[int] = None


# This class is the input for the 'update_vpc_endpoint' function.
class UpdateVpcEndpointRequest(BaseValidatorModel):
    id: str
    addSubnetIds: Optional[List[str]] = None
    removeSubnetIds: Optional[List[str]] = None
    addSecurityGroupIds: Optional[List[str]] = None
    removeSecurityGroupIds: Optional[List[str]] = None
    clientToken: Optional[str] = None


class AccountSettingsDetail(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimits] = None


# This class is the input for the 'update_account_settings' function.
class UpdateAccountSettingsRequest(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimits] = None


# This class is the output for the 'batch_get_collection' function.
class BatchGetCollectionResponse(BaseValidatorModel):
    collectionDetails: List[CollectionDetail]
    collectionErrorDetails: List[CollectionErrorDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_access_policy' function.
class CreateAccessPolicyResponse(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_access_policy' function.
class GetAccessPolicyResponse(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_access_policies' function.
class ListAccessPoliciesResponse(BaseValidatorModel):
    accessPolicySummaries: List[AccessPolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_access_policy' function.
class UpdateAccessPolicyResponse(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_get_effective_lifecycle_policy' function.
class BatchGetEffectiveLifecyclePolicyRequest(BaseValidatorModel):
    resourceIdentifiers: List[LifecyclePolicyResourceIdentifier]


# This class is the output for the 'batch_get_effective_lifecycle_policy' function.
class BatchGetEffectiveLifecyclePolicyResponse(BaseValidatorModel):
    effectiveLifecyclePolicyDetails: List[EffectiveLifecyclePolicyDetail]
    effectiveLifecyclePolicyErrorDetails: List[EffectiveLifecyclePolicyErrorDetail]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_get_lifecycle_policy' function.
class BatchGetLifecyclePolicyRequest(BaseValidatorModel):
    identifiers: List[LifecyclePolicyIdentifier]


# This class is the output for the 'create_lifecycle_policy' function.
class CreateLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_lifecycle_policy' function.
class UpdateLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_lifecycle_policy' function.
class BatchGetLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyDetails: List[LifecyclePolicyDetail]
    lifecyclePolicyErrorDetails: List[LifecyclePolicyErrorDetail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_vpc_endpoint' function.
class BatchGetVpcEndpointResponse(BaseValidatorModel):
    vpcEndpointDetails: List[VpcEndpointDetail]
    vpcEndpointErrorDetails: List[VpcEndpointErrorDetail]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'list_collections' function.
class ListCollectionsRequest(BaseValidatorModel):
    collectionFilters: Optional[CollectionFilters] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'list_collections' function.
class ListCollectionsResponse(BaseValidatorModel):
    collectionSummaries: List[CollectionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_collection' function.
class CreateCollectionResponse(BaseValidatorModel):
    createCollectionDetail: CreateCollectionDetail
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_collection' function.
class CreateCollectionRequest(BaseValidatorModel):
    name: str
    type: Optional[CollectionTypeType] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None
    standbyReplicas: Optional[StandbyReplicasType] = None
    clientToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the input for the 'create_security_config' function.
class CreateSecurityConfigRequest(BaseValidatorModel):
    type: SecurityConfigTypeType
    name: str
    description: Optional[str] = None
    samlOptions: Optional[SamlConfigOptions] = None
    iamIdentityCenterOptions: Optional[CreateIamIdentityCenterConfigOptions] = None
    clientToken: Optional[str] = None


# This class is the output for the 'create_security_policy' function.
class CreateSecurityPolicyResponse(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_security_policy' function.
class GetSecurityPolicyResponse(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_security_policy' function.
class UpdateSecurityPolicyResponse(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpc_endpoint' function.
class CreateVpcEndpointResponse(BaseValidatorModel):
    createVpcEndpointDetail: CreateVpcEndpointDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_collection' function.
class DeleteCollectionResponse(BaseValidatorModel):
    deleteCollectionDetail: DeleteCollectionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_endpoint' function.
class DeleteVpcEndpointResponse(BaseValidatorModel):
    deleteVpcEndpointDetail: DeleteVpcEndpointDetail
    ResponseMetadata: ResponseMetadata


class GetPoliciesStatsResponse(BaseValidatorModel):
    AccessPolicyStats: AccessPolicyStats
    SecurityPolicyStats: SecurityPolicyStats
    SecurityConfigStats: SecurityConfigStats
    LifecyclePolicyStats: LifecyclePolicyStats
    TotalPolicyCount: int
    ResponseMetadata: ResponseMetadata


class SecurityConfigDetail(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[SecurityConfigTypeType] = None
    configVersion: Optional[str] = None
    description: Optional[str] = None
    samlOptions: Optional[SamlConfigOptions] = None
    iamIdentityCenterOptions: Optional[IamIdentityCenterConfigOptions] = None
    createdDate: Optional[int] = None
    lastModifiedDate: Optional[int] = None


# This class is the output for the 'list_lifecycle_policies' function.
class ListLifecyclePoliciesResponse(BaseValidatorModel):
    lifecyclePolicySummaries: List[LifecyclePolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_security_configs' function.
class ListSecurityConfigsResponse(BaseValidatorModel):
    securityConfigSummaries: List[SecurityConfigSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_security_policies' function.
class ListSecurityPoliciesResponse(BaseValidatorModel):
    securityPolicySummaries: List[SecurityPolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'list_vpc_endpoints' function.
class ListVpcEndpointsRequest(BaseValidatorModel):
    vpcEndpointFilters: Optional[VpcEndpointFilters] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'list_vpc_endpoints' function.
class ListVpcEndpointsResponse(BaseValidatorModel):
    vpcEndpointSummaries: List[VpcEndpointSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_collection' function.
class UpdateCollectionResponse(BaseValidatorModel):
    updateCollectionDetail: UpdateCollectionDetail
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_security_config' function.
class UpdateSecurityConfigRequest(BaseValidatorModel):
    id: str
    configVersion: str
    description: Optional[str] = None
    samlOptions: Optional[SamlConfigOptions] = None
    iamIdentityCenterOptionsUpdates: Optional[UpdateIamIdentityCenterConfigOptions] = None
    clientToken: Optional[str] = None


# This class is the output for the 'update_vpc_endpoint' function.
class UpdateVpcEndpointResponse(BaseValidatorModel):
    UpdateVpcEndpointDetail: UpdateVpcEndpointDetail
    ResponseMetadata: ResponseMetadata


class GetAccountSettingsResponse(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_account_settings' function.
class UpdateAccountSettingsResponse(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_security_config' function.
class CreateSecurityConfigResponse(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_security_config' function.
class GetSecurityConfigResponse(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_security_config' function.
class UpdateSecurityConfigResponse(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetail
    ResponseMetadata: ResponseMetadata