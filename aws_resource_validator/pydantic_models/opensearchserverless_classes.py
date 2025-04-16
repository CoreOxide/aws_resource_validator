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
from aws_resource_validator.pydantic_models.opensearchserverless_constants import *

class AccessPolicyStats(BaseValidatorModel):
    DataPolicyCount: Optional[int] = None


class CapacityLimits(BaseValidatorModel):
    maxIndexingCapacityInOCU: Optional[int] = None
    maxSearchCapacityInOCU: Optional[int] = None


class BatchGetCollectionRequest(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    names: Optional[Sequence[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetVpcEndpointRequest(BaseValidatorModel):
    ids: Sequence[str]


class CollectionFilters(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class CreateIamIdentityCenterConfigOptions(BaseValidatorModel):
    instanceArn: str
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


class SamlConfigOptions(BaseValidatorModel):
    metadata: str
    userAttribute: Optional[str] = None
    groupAttribute: Optional[str] = None
    openSearchServerlessEntityId: Optional[str] = None
    sessionTimeout: Optional[int] = None


class CreateVpcEndpointRequest(BaseValidatorModel):
    name: str
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None


class LifecyclePolicyStats(BaseValidatorModel):
    RetentionPolicyCount: Optional[int] = None


class SecurityConfigStats(BaseValidatorModel):
    SamlConfigCount: Optional[int] = None


class SecurityPolicyStats(BaseValidatorModel):
    EncryptionPolicyCount: Optional[int] = None
    NetworkPolicyCount: Optional[int] = None


class IamIdentityCenterConfigOptions(BaseValidatorModel):
    instanceArn: Optional[str] = None
    applicationArn: Optional[str] = None
    applicationName: Optional[str] = None
    applicationDescription: Optional[str] = None
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class VpcEndpointFilters(BaseValidatorModel):
    status: Optional[VpcEndpointStatusType] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateIamIdentityCenterConfigOptions(BaseValidatorModel):
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


class AccountSettingsDetail(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimits] = None


class UpdateAccountSettingsRequest(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimits] = None


class CollectionErrorDetail(BaseValidatorModel):
    pass


class CollectionDetail(BaseValidatorModel):
    pass


class BatchGetCollectionResponse(BaseValidatorModel):
    collectionDetails: List[CollectionDetail]
    collectionErrorDetails: List[CollectionErrorDetail]
    ResponseMetadata: ResponseMetadata


class AccessPolicyDetail(BaseValidatorModel):
    pass


class CreateAccessPolicyResponse(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetail
    ResponseMetadata: ResponseMetadata


class GetAccessPolicyResponse(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetail
    ResponseMetadata: ResponseMetadata


class AccessPolicySummary(BaseValidatorModel):
    pass


class ListAccessPoliciesResponse(BaseValidatorModel):
    accessPolicySummaries: List[AccessPolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateAccessPolicyResponse(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetail
    ResponseMetadata: ResponseMetadata


class LifecyclePolicyResourceIdentifier(BaseValidatorModel):
    pass


class BatchGetEffectiveLifecyclePolicyRequest(BaseValidatorModel):
    resourceIdentifiers: Sequence[LifecyclePolicyResourceIdentifier]


class EffectiveLifecyclePolicyDetail(BaseValidatorModel):
    pass


class EffectiveLifecyclePolicyErrorDetail(BaseValidatorModel):
    pass


class BatchGetEffectiveLifecyclePolicyResponse(BaseValidatorModel):
    effectiveLifecyclePolicyDetails: List[EffectiveLifecyclePolicyDetail]
    effectiveLifecyclePolicyErrorDetails: List[EffectiveLifecyclePolicyErrorDetail]
    ResponseMetadata: ResponseMetadata


class LifecyclePolicyIdentifier(BaseValidatorModel):
    pass


class BatchGetLifecyclePolicyRequest(BaseValidatorModel):
    identifiers: Sequence[LifecyclePolicyIdentifier]


class LifecyclePolicyDetail(BaseValidatorModel):
    pass


class CreateLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetail
    ResponseMetadata: ResponseMetadata


class UpdateLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetail
    ResponseMetadata: ResponseMetadata


class LifecyclePolicyErrorDetail(BaseValidatorModel):
    pass


class BatchGetLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyDetails: List[LifecyclePolicyDetail]
    lifecyclePolicyErrorDetails: List[LifecyclePolicyErrorDetail]
    ResponseMetadata: ResponseMetadata


class VpcEndpointErrorDetail(BaseValidatorModel):
    pass


class VpcEndpointDetail(BaseValidatorModel):
    pass


class BatchGetVpcEndpointResponse(BaseValidatorModel):
    vpcEndpointDetails: List[VpcEndpointDetail]
    vpcEndpointErrorDetails: List[VpcEndpointErrorDetail]
    ResponseMetadata: ResponseMetadata


class ListCollectionsRequest(BaseValidatorModel):
    collectionFilters: Optional[CollectionFilters] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class CollectionSummary(BaseValidatorModel):
    pass


class ListCollectionsResponse(BaseValidatorModel):
    collectionSummaries: List[CollectionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateCollectionDetail(BaseValidatorModel):
    pass


class CreateCollectionResponse(BaseValidatorModel):
    createCollectionDetail: CreateCollectionDetail
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class SecurityPolicyDetail(BaseValidatorModel):
    pass


class CreateSecurityPolicyResponse(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetail
    ResponseMetadata: ResponseMetadata


class GetSecurityPolicyResponse(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetail
    ResponseMetadata: ResponseMetadata


class UpdateSecurityPolicyResponse(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetail
    ResponseMetadata: ResponseMetadata


class CreateVpcEndpointDetail(BaseValidatorModel):
    pass


class CreateVpcEndpointResponse(BaseValidatorModel):
    createVpcEndpointDetail: CreateVpcEndpointDetail
    ResponseMetadata: ResponseMetadata


class DeleteCollectionDetail(BaseValidatorModel):
    pass


class DeleteCollectionResponse(BaseValidatorModel):
    deleteCollectionDetail: DeleteCollectionDetail
    ResponseMetadata: ResponseMetadata


class DeleteVpcEndpointDetail(BaseValidatorModel):
    pass


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


class LifecyclePolicySummary(BaseValidatorModel):
    pass


class ListLifecyclePoliciesResponse(BaseValidatorModel):
    lifecyclePolicySummaries: List[LifecyclePolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SecurityConfigSummary(BaseValidatorModel):
    pass


class ListSecurityConfigsResponse(BaseValidatorModel):
    securityConfigSummaries: List[SecurityConfigSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SecurityPolicySummary(BaseValidatorModel):
    pass


class ListSecurityPoliciesResponse(BaseValidatorModel):
    securityPolicySummaries: List[SecurityPolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListVpcEndpointsRequest(BaseValidatorModel):
    vpcEndpointFilters: Optional[VpcEndpointFilters] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VpcEndpointSummary(BaseValidatorModel):
    pass


class ListVpcEndpointsResponse(BaseValidatorModel):
    vpcEndpointSummaries: List[VpcEndpointSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateCollectionDetail(BaseValidatorModel):
    pass


class UpdateCollectionResponse(BaseValidatorModel):
    updateCollectionDetail: UpdateCollectionDetail
    ResponseMetadata: ResponseMetadata


class UpdateVpcEndpointDetail(BaseValidatorModel):
    pass


class UpdateVpcEndpointResponse(BaseValidatorModel):
    UpdateVpcEndpointDetail: UpdateVpcEndpointDetail
    ResponseMetadata: ResponseMetadata


class GetAccountSettingsResponse(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetail
    ResponseMetadata: ResponseMetadata


class UpdateAccountSettingsResponse(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetail
    ResponseMetadata: ResponseMetadata


class SecurityConfigDetail(BaseValidatorModel):
    pass


class CreateSecurityConfigResponse(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetail
    ResponseMetadata: ResponseMetadata


class GetSecurityConfigResponse(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetail
    ResponseMetadata: ResponseMetadata


class UpdateSecurityConfigResponse(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetail
    ResponseMetadata: ResponseMetadata


