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

class AccessPolicyStatsTypeDef(BaseValidatorModel):
    DataPolicyCount: Optional[int] = None


class CapacityLimitsTypeDef(BaseValidatorModel):
    maxIndexingCapacityInOCU: Optional[int] = None
    maxSearchCapacityInOCU: Optional[int] = None


class BatchGetCollectionRequestTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    names: Optional[Sequence[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetVpcEndpointRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]


class CollectionFiltersTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class CreateIamIdentityCenterConfigOptionsTypeDef(BaseValidatorModel):
    instanceArn: str
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


class SamlConfigOptionsTypeDef(BaseValidatorModel):
    metadata: str
    userAttribute: Optional[str] = None
    groupAttribute: Optional[str] = None
    openSearchServerlessEntityId: Optional[str] = None
    sessionTimeout: Optional[int] = None


class CreateVpcEndpointRequestTypeDef(BaseValidatorModel):
    name: str
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None


class LifecyclePolicyStatsTypeDef(BaseValidatorModel):
    RetentionPolicyCount: Optional[int] = None


class SecurityConfigStatsTypeDef(BaseValidatorModel):
    SamlConfigCount: Optional[int] = None


class SecurityPolicyStatsTypeDef(BaseValidatorModel):
    EncryptionPolicyCount: Optional[int] = None
    NetworkPolicyCount: Optional[int] = None


class IamIdentityCenterConfigOptionsTypeDef(BaseValidatorModel):
    instanceArn: Optional[str] = None
    applicationArn: Optional[str] = None
    applicationName: Optional[str] = None
    applicationDescription: Optional[str] = None
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class VpcEndpointFiltersTypeDef(BaseValidatorModel):
    status: Optional[VpcEndpointStatusType] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateIamIdentityCenterConfigOptionsTypeDef(BaseValidatorModel):
    userAttribute: Optional[IamIdentityCenterUserAttributeType] = None
    groupAttribute: Optional[IamIdentityCenterGroupAttributeType] = None


class AccountSettingsDetailTypeDef(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimitsTypeDef] = None


class UpdateAccountSettingsRequestTypeDef(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimitsTypeDef] = None


class CollectionErrorDetailTypeDef(BaseValidatorModel):
    pass


class CollectionDetailTypeDef(BaseValidatorModel):
    pass


class BatchGetCollectionResponseTypeDef(BaseValidatorModel):
    collectionDetails: List[CollectionDetailTypeDef]
    collectionErrorDetails: List[CollectionErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AccessPolicyDetailTypeDef(BaseValidatorModel):
    pass


class CreateAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AccessPolicySummaryTypeDef(BaseValidatorModel):
    pass


class ListAccessPoliciesResponseTypeDef(BaseValidatorModel):
    accessPolicySummaries: List[AccessPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LifecyclePolicyResourceIdentifierTypeDef(BaseValidatorModel):
    pass


class BatchGetEffectiveLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    resourceIdentifiers: Sequence[LifecyclePolicyResourceIdentifierTypeDef]


class EffectiveLifecyclePolicyDetailTypeDef(BaseValidatorModel):
    pass


class EffectiveLifecyclePolicyErrorDetailTypeDef(BaseValidatorModel):
    pass


class BatchGetEffectiveLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    effectiveLifecyclePolicyDetails: List[EffectiveLifecyclePolicyDetailTypeDef]
    effectiveLifecyclePolicyErrorDetails: List[EffectiveLifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LifecyclePolicyIdentifierTypeDef(BaseValidatorModel):
    pass


class BatchGetLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    identifiers: Sequence[LifecyclePolicyIdentifierTypeDef]


class LifecyclePolicyDetailTypeDef(BaseValidatorModel):
    pass


class CreateLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LifecyclePolicyErrorDetailTypeDef(BaseValidatorModel):
    pass


class BatchGetLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyDetails: List[LifecyclePolicyDetailTypeDef]
    lifecyclePolicyErrorDetails: List[LifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class VpcEndpointErrorDetailTypeDef(BaseValidatorModel):
    pass


class VpcEndpointDetailTypeDef(BaseValidatorModel):
    pass


class BatchGetVpcEndpointResponseTypeDef(BaseValidatorModel):
    vpcEndpointDetails: List[VpcEndpointDetailTypeDef]
    vpcEndpointErrorDetails: List[VpcEndpointErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListCollectionsRequestTypeDef(BaseValidatorModel):
    collectionFilters: Optional[CollectionFiltersTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class CollectionSummaryTypeDef(BaseValidatorModel):
    pass


class ListCollectionsResponseTypeDef(BaseValidatorModel):
    collectionSummaries: List[CollectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateCollectionDetailTypeDef(BaseValidatorModel):
    pass


class CreateCollectionResponseTypeDef(BaseValidatorModel):
    createCollectionDetail: CreateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class SecurityPolicyDetailTypeDef(BaseValidatorModel):
    pass


class CreateSecurityPolicyResponseTypeDef(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSecurityPolicyResponseTypeDef(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSecurityPolicyResponseTypeDef(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVpcEndpointDetailTypeDef(BaseValidatorModel):
    pass


class CreateVpcEndpointResponseTypeDef(BaseValidatorModel):
    createVpcEndpointDetail: CreateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCollectionDetailTypeDef(BaseValidatorModel):
    pass


class DeleteCollectionResponseTypeDef(BaseValidatorModel):
    deleteCollectionDetail: DeleteCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVpcEndpointDetailTypeDef(BaseValidatorModel):
    pass


class DeleteVpcEndpointResponseTypeDef(BaseValidatorModel):
    deleteVpcEndpointDetail: DeleteVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPoliciesStatsResponseTypeDef(BaseValidatorModel):
    AccessPolicyStats: AccessPolicyStatsTypeDef
    SecurityPolicyStats: SecurityPolicyStatsTypeDef
    SecurityConfigStats: SecurityConfigStatsTypeDef
    LifecyclePolicyStats: LifecyclePolicyStatsTypeDef
    TotalPolicyCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class LifecyclePolicySummaryTypeDef(BaseValidatorModel):
    pass


class ListLifecyclePoliciesResponseTypeDef(BaseValidatorModel):
    lifecyclePolicySummaries: List[LifecyclePolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SecurityConfigSummaryTypeDef(BaseValidatorModel):
    pass


class ListSecurityConfigsResponseTypeDef(BaseValidatorModel):
    securityConfigSummaries: List[SecurityConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SecurityPolicySummaryTypeDef(BaseValidatorModel):
    pass


class ListSecurityPoliciesResponseTypeDef(BaseValidatorModel):
    securityPolicySummaries: List[SecurityPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListVpcEndpointsRequestTypeDef(BaseValidatorModel):
    vpcEndpointFilters: Optional[VpcEndpointFiltersTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VpcEndpointSummaryTypeDef(BaseValidatorModel):
    pass


class ListVpcEndpointsResponseTypeDef(BaseValidatorModel):
    vpcEndpointSummaries: List[VpcEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateCollectionDetailTypeDef(BaseValidatorModel):
    pass


class UpdateCollectionResponseTypeDef(BaseValidatorModel):
    updateCollectionDetail: UpdateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVpcEndpointDetailTypeDef(BaseValidatorModel):
    pass


class UpdateVpcEndpointResponseTypeDef(BaseValidatorModel):
    UpdateVpcEndpointDetail: UpdateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountSettingsResponseTypeDef(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAccountSettingsResponseTypeDef(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SecurityConfigDetailTypeDef(BaseValidatorModel):
    pass


class CreateSecurityConfigResponseTypeDef(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSecurityConfigResponseTypeDef(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSecurityConfigResponseTypeDef(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


