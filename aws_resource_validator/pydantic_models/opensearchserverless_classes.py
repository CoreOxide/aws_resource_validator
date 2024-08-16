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
from aws_resource_validator.pydantic_models.opensearchserverless_constants import *

class AccessPolicyDetailTypeDef(BaseValidatorModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["data"]] = None

class AccessPolicyStatsTypeDef(BaseValidatorModel):
    DataPolicyCount: Optional[int] = None

class AccessPolicySummaryTypeDef(BaseValidatorModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["data"]] = None

class CapacityLimitsTypeDef(BaseValidatorModel):
    maxIndexingCapacityInOCU: Optional[int] = None
    maxSearchCapacityInOCU: Optional[int] = None

class BatchGetCollectionRequestRequestTypeDef(BaseValidatorModel):
    ids: Optional[Sequence[str]] = None
    names: Optional[Sequence[str]] = None

class CollectionDetailTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    collectionEndpoint: Optional[str] = None
    createdDate: Optional[int] = None
    dashboardEndpoint: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    standbyReplicas: Optional[StandbyReplicasType] = None
    status: Optional[CollectionStatusType] = None
    type: Optional[CollectionTypeType] = None

class CollectionErrorDetailTypeDef(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class LifecyclePolicyResourceIdentifierTypeDef(BaseValidatorModel):
    resource: str
    type: Literal["retention"]

class EffectiveLifecyclePolicyDetailTypeDef(BaseValidatorModel):
    noMinRetentionPeriod: Optional[bool] = None
    policyName: Optional[str] = None
    resource: Optional[str] = None
    resourceType: Optional[Literal["index"]] = None
    retentionPeriod: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class EffectiveLifecyclePolicyErrorDetailTypeDef(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    resource: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class LifecyclePolicyIdentifierTypeDef(BaseValidatorModel):
    name: str
    type: Literal["retention"]

class LifecyclePolicyDetailTypeDef(BaseValidatorModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class LifecyclePolicyErrorDetailTypeDef(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    name: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class BatchGetVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    ids: Sequence[str]

class VpcEndpointDetailTypeDef(BaseValidatorModel):
    createdDate: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[VpcEndpointStatusType] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None

class VpcEndpointErrorDetailTypeDef(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    id: Optional[str] = None

class CollectionFiltersTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None

class CollectionSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None

class CreateAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    policy: str
    type: Literal["data"]
    clientToken: Optional[str] = None
    description: Optional[str] = None

class CreateCollectionDetailTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdDate: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    standbyReplicas: Optional[StandbyReplicasType] = None
    status: Optional[CollectionStatusType] = None
    type: Optional[CollectionTypeType] = None

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class CreateLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    policy: str
    type: Literal["retention"]
    clientToken: Optional[str] = None
    description: Optional[str] = None

class SamlConfigOptionsTypeDef(BaseValidatorModel):
    metadata: str
    groupAttribute: Optional[str] = None
    sessionTimeout: Optional[int] = None
    userAttribute: Optional[str] = None

class CreateSecurityPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    policy: str
    type: SecurityPolicyTypeType
    clientToken: Optional[str] = None
    description: Optional[str] = None

class SecurityPolicyDetailTypeDef(BaseValidatorModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    policyVersion: Optional[str] = None
    type: Optional[SecurityPolicyTypeType] = None

class CreateVpcEndpointDetailTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None

class CreateVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    name: str
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None

class DeleteAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: Literal["data"]
    clientToken: Optional[str] = None

class DeleteCollectionDetailTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None

class DeleteCollectionRequestRequestTypeDef(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None

class DeleteLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: Literal["retention"]
    clientToken: Optional[str] = None

class DeleteSecurityConfigRequestRequestTypeDef(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None

class DeleteSecurityPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: SecurityPolicyTypeType
    clientToken: Optional[str] = None

class DeleteVpcEndpointDetailTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None

class DeleteVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None

class GetAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: Literal["data"]

class LifecyclePolicyStatsTypeDef(BaseValidatorModel):
    RetentionPolicyCount: Optional[int] = None

class SecurityConfigStatsTypeDef(BaseValidatorModel):
    SamlConfigCount: Optional[int] = None

class SecurityPolicyStatsTypeDef(BaseValidatorModel):
    EncryptionPolicyCount: Optional[int] = None
    NetworkPolicyCount: Optional[int] = None

class GetSecurityConfigRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetSecurityPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: SecurityPolicyTypeType

class LifecyclePolicySummaryTypeDef(BaseValidatorModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class ListAccessPoliciesRequestRequestTypeDef(BaseValidatorModel):
    type: Literal["data"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resource: Optional[Sequence[str]] = None

class ListLifecyclePoliciesRequestRequestTypeDef(BaseValidatorModel):
    type: Literal["retention"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resources: Optional[Sequence[str]] = None

class ListSecurityConfigsRequestRequestTypeDef(BaseValidatorModel):
    type: Literal["saml"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SecurityConfigSummaryTypeDef(BaseValidatorModel):
    configVersion: Optional[str] = None
    createdDate: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    type: Optional[Literal["saml"]] = None

class ListSecurityPoliciesRequestRequestTypeDef(BaseValidatorModel):
    type: SecurityPolicyTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resource: Optional[Sequence[str]] = None

class SecurityPolicySummaryTypeDef(BaseValidatorModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    type: Optional[SecurityPolicyTypeType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class VpcEndpointFiltersTypeDef(BaseValidatorModel):
    status: Optional[VpcEndpointStatusType] = None

class VpcEndpointSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    policyVersion: str
    type: Literal["data"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[str] = None

class UpdateCollectionDetailTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdDate: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None
    type: Optional[CollectionTypeType] = None

class UpdateCollectionRequestRequestTypeDef(BaseValidatorModel):
    id: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class UpdateLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    policyVersion: str
    type: Literal["retention"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[str] = None

class UpdateSecurityPolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    policyVersion: str
    type: SecurityPolicyTypeType
    clientToken: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[str] = None

class UpdateVpcEndpointDetailTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[VpcEndpointStatusType] = None
    subnetIds: Optional[List[str]] = None

class UpdateVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    id: str
    addSecurityGroupIds: Optional[Sequence[str]] = None
    addSubnetIds: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    removeSecurityGroupIds: Optional[Sequence[str]] = None
    removeSubnetIds: Optional[Sequence[str]] = None

class AccountSettingsDetailTypeDef(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimitsTypeDef] = None

class UpdateAccountSettingsRequestRequestTypeDef(BaseValidatorModel):
    capacityLimits: Optional[CapacityLimitsTypeDef] = None

class BatchGetCollectionResponseTypeDef(BaseValidatorModel):
    collectionDetails: List[CollectionDetailTypeDef]
    collectionErrorDetails: List[CollectionErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPoliciesResponseTypeDef(BaseValidatorModel):
    accessPolicySummaries: List[AccessPolicySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessPolicyResponseTypeDef(BaseValidatorModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetEffectiveLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceIdentifiers: Sequence[LifecyclePolicyResourceIdentifierTypeDef]

class BatchGetEffectiveLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    effectiveLifecyclePolicyDetails: List[EffectiveLifecyclePolicyDetailTypeDef]
    effectiveLifecyclePolicyErrorDetails: List[EffectiveLifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    identifiers: Sequence[LifecyclePolicyIdentifierTypeDef]

class CreateLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyDetails: List[LifecyclePolicyDetailTypeDef]
    lifecyclePolicyErrorDetails: List[LifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetVpcEndpointResponseTypeDef(BaseValidatorModel):
    vpcEndpointDetails: List[VpcEndpointDetailTypeDef]
    vpcEndpointErrorDetails: List[VpcEndpointErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollectionsRequestRequestTypeDef(BaseValidatorModel):
    collectionFilters: Optional[CollectionFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCollectionsResponseTypeDef(BaseValidatorModel):
    collectionSummaries: List[CollectionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollectionResponseTypeDef(BaseValidatorModel):
    createCollectionDetail: CreateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollectionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    standbyReplicas: Optional[StandbyReplicasType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    type: Optional[CollectionTypeType] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateSecurityConfigRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: Literal["saml"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    samlOptions: Optional[SamlConfigOptionsTypeDef] = None

class SecurityConfigDetailTypeDef(BaseValidatorModel):
    configVersion: Optional[str] = None
    createdDate: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    samlOptions: Optional[SamlConfigOptionsTypeDef] = None
    type: Optional[Literal["saml"]] = None

class UpdateSecurityConfigRequestRequestTypeDef(BaseValidatorModel):
    configVersion: str
    id: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    samlOptions: Optional[SamlConfigOptionsTypeDef] = None

class CreateSecurityPolicyResponseTypeDef(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityPolicyResponseTypeDef(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityPolicyResponseTypeDef(BaseValidatorModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcEndpointResponseTypeDef(BaseValidatorModel):
    createVpcEndpointDetail: CreateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCollectionResponseTypeDef(BaseValidatorModel):
    deleteCollectionDetail: DeleteCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointResponseTypeDef(BaseValidatorModel):
    deleteVpcEndpointDetail: DeleteVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPoliciesStatsResponseTypeDef(BaseValidatorModel):
    AccessPolicyStats: AccessPolicyStatsTypeDef
    LifecyclePolicyStats: LifecyclePolicyStatsTypeDef
    SecurityConfigStats: SecurityConfigStatsTypeDef
    SecurityPolicyStats: SecurityPolicyStatsTypeDef
    TotalPolicyCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListLifecyclePoliciesResponseTypeDef(BaseValidatorModel):
    lifecyclePolicySummaries: List[LifecyclePolicySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityConfigsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    securityConfigSummaries: List[SecurityConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityPoliciesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    securityPolicySummaries: List[SecurityPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    vpcEndpointFilters: Optional[VpcEndpointFiltersTypeDef] = None

class ListVpcEndpointsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    vpcEndpointSummaries: List[VpcEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCollectionResponseTypeDef(BaseValidatorModel):
    updateCollectionDetail: UpdateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcEndpointResponseTypeDef(BaseValidatorModel):
    UpdateVpcEndpointDetail: UpdateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(BaseValidatorModel):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigResponseTypeDef(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityConfigResponseTypeDef(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityConfigResponseTypeDef(BaseValidatorModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

