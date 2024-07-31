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
from aws_resource_validator.pydantic_models.opensearchserverless_constants import *

class AccessPolicyDetailTypeDef(BaseModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["data"]] = None

class AccessPolicyStatsTypeDef(BaseModel):
    DataPolicyCount: Optional[int] = None

class AccessPolicySummaryTypeDef(BaseModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["data"]] = None

class CapacityLimitsTypeDef(BaseModel):
    maxIndexingCapacityInOCU: Optional[int] = None
    maxSearchCapacityInOCU: Optional[int] = None

class BatchGetCollectionRequestRequestTypeDef(BaseModel):
    ids: Optional[Sequence[str]] = None
    names: Optional[Sequence[str]] = None

class CollectionDetailTypeDef(BaseModel):
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

class CollectionErrorDetailTypeDef(BaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class LifecyclePolicyResourceIdentifierTypeDef(BaseModel):
    resource: str
    type: Literal["retention"]

class EffectiveLifecyclePolicyDetailTypeDef(BaseModel):
    noMinRetentionPeriod: Optional[bool] = None
    policyName: Optional[str] = None
    resource: Optional[str] = None
    resourceType: Optional[Literal["index"]] = None
    retentionPeriod: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class EffectiveLifecyclePolicyErrorDetailTypeDef(BaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    resource: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class LifecyclePolicyIdentifierTypeDef(BaseModel):
    name: str
    type: Literal["retention"]

class LifecyclePolicyDetailTypeDef(BaseModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class LifecyclePolicyErrorDetailTypeDef(BaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    name: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class BatchGetVpcEndpointRequestRequestTypeDef(BaseModel):
    ids: Sequence[str]

class VpcEndpointDetailTypeDef(BaseModel):
    createdDate: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[VpcEndpointStatusType] = None
    subnetIds: Optional[List[str]] = None
    vpcId: Optional[str] = None

class VpcEndpointErrorDetailTypeDef(BaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    id: Optional[str] = None

class CollectionFiltersTypeDef(BaseModel):
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None

class CollectionSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None

class CreateAccessPolicyRequestRequestTypeDef(BaseModel):
    name: str
    policy: str
    type: Literal["data"]
    clientToken: Optional[str] = None
    description: Optional[str] = None

class CreateCollectionDetailTypeDef(BaseModel):
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

class TagTypeDef(BaseModel):
    key: str
    value: str

class CreateLifecyclePolicyRequestRequestTypeDef(BaseModel):
    name: str
    policy: str
    type: Literal["retention"]
    clientToken: Optional[str] = None
    description: Optional[str] = None

class SamlConfigOptionsTypeDef(BaseModel):
    metadata: str
    groupAttribute: Optional[str] = None
    sessionTimeout: Optional[int] = None
    userAttribute: Optional[str] = None

class CreateSecurityPolicyRequestRequestTypeDef(BaseModel):
    name: str
    policy: str
    type: SecurityPolicyTypeType
    clientToken: Optional[str] = None
    description: Optional[str] = None

class SecurityPolicyDetailTypeDef(BaseModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policy: Optional[Dict[str, Any]] = None
    policyVersion: Optional[str] = None
    type: Optional[SecurityPolicyTypeType] = None

class CreateVpcEndpointDetailTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None

class CreateVpcEndpointRequestRequestTypeDef(BaseModel):
    name: str
    subnetIds: Sequence[str]
    vpcId: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None

class DeleteAccessPolicyRequestRequestTypeDef(BaseModel):
    name: str
    type: Literal["data"]
    clientToken: Optional[str] = None

class DeleteCollectionDetailTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None

class DeleteCollectionRequestRequestTypeDef(BaseModel):
    id: str
    clientToken: Optional[str] = None

class DeleteLifecyclePolicyRequestRequestTypeDef(BaseModel):
    name: str
    type: Literal["retention"]
    clientToken: Optional[str] = None

class DeleteSecurityConfigRequestRequestTypeDef(BaseModel):
    id: str
    clientToken: Optional[str] = None

class DeleteSecurityPolicyRequestRequestTypeDef(BaseModel):
    name: str
    type: SecurityPolicyTypeType
    clientToken: Optional[str] = None

class DeleteVpcEndpointDetailTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None

class DeleteVpcEndpointRequestRequestTypeDef(BaseModel):
    id: str
    clientToken: Optional[str] = None

class GetAccessPolicyRequestRequestTypeDef(BaseModel):
    name: str
    type: Literal["data"]

class LifecyclePolicyStatsTypeDef(BaseModel):
    RetentionPolicyCount: Optional[int] = None

class SecurityConfigStatsTypeDef(BaseModel):
    SamlConfigCount: Optional[int] = None

class SecurityPolicyStatsTypeDef(BaseModel):
    EncryptionPolicyCount: Optional[int] = None
    NetworkPolicyCount: Optional[int] = None

class GetSecurityConfigRequestRequestTypeDef(BaseModel):
    id: str

class GetSecurityPolicyRequestRequestTypeDef(BaseModel):
    name: str
    type: SecurityPolicyTypeType

class LifecyclePolicySummaryTypeDef(BaseModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    type: Optional[Literal["retention"]] = None

class ListAccessPoliciesRequestRequestTypeDef(BaseModel):
    type: Literal["data"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resource: Optional[Sequence[str]] = None

class ListLifecyclePoliciesRequestRequestTypeDef(BaseModel):
    type: Literal["retention"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resources: Optional[Sequence[str]] = None

class ListSecurityConfigsRequestRequestTypeDef(BaseModel):
    type: Literal["saml"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SecurityConfigSummaryTypeDef(BaseModel):
    configVersion: Optional[str] = None
    createdDate: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    type: Optional[Literal["saml"]] = None

class ListSecurityPoliciesRequestRequestTypeDef(BaseModel):
    type: SecurityPolicyTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resource: Optional[Sequence[str]] = None

class SecurityPolicySummaryTypeDef(BaseModel):
    createdDate: Optional[int] = None
    description: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    policyVersion: Optional[str] = None
    type: Optional[SecurityPolicyTypeType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class VpcEndpointFiltersTypeDef(BaseModel):
    status: Optional[VpcEndpointStatusType] = None

class VpcEndpointSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[VpcEndpointStatusType] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessPolicyRequestRequestTypeDef(BaseModel):
    name: str
    policyVersion: str
    type: Literal["data"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[str] = None

class UpdateCollectionDetailTypeDef(BaseModel):
    arn: Optional[str] = None
    createdDate: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    status: Optional[CollectionStatusType] = None
    type: Optional[CollectionTypeType] = None

class UpdateCollectionRequestRequestTypeDef(BaseModel):
    id: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class UpdateLifecyclePolicyRequestRequestTypeDef(BaseModel):
    name: str
    policyVersion: str
    type: Literal["retention"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[str] = None

class UpdateSecurityPolicyRequestRequestTypeDef(BaseModel):
    name: str
    policyVersion: str
    type: SecurityPolicyTypeType
    clientToken: Optional[str] = None
    description: Optional[str] = None
    policy: Optional[str] = None

class UpdateVpcEndpointDetailTypeDef(BaseModel):
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    name: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[VpcEndpointStatusType] = None
    subnetIds: Optional[List[str]] = None

class UpdateVpcEndpointRequestRequestTypeDef(BaseModel):
    id: str
    addSecurityGroupIds: Optional[Sequence[str]] = None
    addSubnetIds: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    removeSecurityGroupIds: Optional[Sequence[str]] = None
    removeSubnetIds: Optional[Sequence[str]] = None

class AccountSettingsDetailTypeDef(BaseModel):
    capacityLimits: Optional[CapacityLimitsTypeDef] = None

class UpdateAccountSettingsRequestRequestTypeDef(BaseModel):
    capacityLimits: Optional[CapacityLimitsTypeDef] = None

class BatchGetCollectionResponseTypeDef(BaseModel):
    collectionDetails: List[CollectionDetailTypeDef]
    collectionErrorDetails: List[CollectionErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPolicyResponseTypeDef(BaseModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessPolicyResponseTypeDef(BaseModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessPoliciesResponseTypeDef(BaseModel):
    accessPolicySummaries: List[AccessPolicySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessPolicyResponseTypeDef(BaseModel):
    accessPolicyDetail: AccessPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetEffectiveLifecyclePolicyRequestRequestTypeDef(BaseModel):
    resourceIdentifiers: Sequence[LifecyclePolicyResourceIdentifierTypeDef]

class BatchGetEffectiveLifecyclePolicyResponseTypeDef(BaseModel):
    effectiveLifecyclePolicyDetails: List[EffectiveLifecyclePolicyDetailTypeDef]
    effectiveLifecyclePolicyErrorDetails: List[EffectiveLifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetLifecyclePolicyRequestRequestTypeDef(BaseModel):
    identifiers: Sequence[LifecyclePolicyIdentifierTypeDef]

class CreateLifecyclePolicyResponseTypeDef(BaseModel):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLifecyclePolicyResponseTypeDef(BaseModel):
    lifecyclePolicyDetail: LifecyclePolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetLifecyclePolicyResponseTypeDef(BaseModel):
    lifecyclePolicyDetails: List[LifecyclePolicyDetailTypeDef]
    lifecyclePolicyErrorDetails: List[LifecyclePolicyErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetVpcEndpointResponseTypeDef(BaseModel):
    vpcEndpointDetails: List[VpcEndpointDetailTypeDef]
    vpcEndpointErrorDetails: List[VpcEndpointErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollectionsRequestRequestTypeDef(BaseModel):
    collectionFilters: Optional[CollectionFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCollectionsResponseTypeDef(BaseModel):
    collectionSummaries: List[CollectionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollectionResponseTypeDef(BaseModel):
    createCollectionDetail: CreateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCollectionRequestRequestTypeDef(BaseModel):
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    standbyReplicas: Optional[StandbyReplicasType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    type: Optional[CollectionTypeType] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateSecurityConfigRequestRequestTypeDef(BaseModel):
    name: str
    type: Literal["saml"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    samlOptions: Optional[SamlConfigOptionsTypeDef] = None

class SecurityConfigDetailTypeDef(BaseModel):
    configVersion: Optional[str] = None
    createdDate: Optional[int] = None
    description: Optional[str] = None
    id: Optional[str] = None
    lastModifiedDate: Optional[int] = None
    samlOptions: Optional[SamlConfigOptionsTypeDef] = None
    type: Optional[Literal["saml"]] = None

class UpdateSecurityConfigRequestRequestTypeDef(BaseModel):
    configVersion: str
    id: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    samlOptions: Optional[SamlConfigOptionsTypeDef] = None

class CreateSecurityPolicyResponseTypeDef(BaseModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityPolicyResponseTypeDef(BaseModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityPolicyResponseTypeDef(BaseModel):
    securityPolicyDetail: SecurityPolicyDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcEndpointResponseTypeDef(BaseModel):
    createVpcEndpointDetail: CreateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCollectionResponseTypeDef(BaseModel):
    deleteCollectionDetail: DeleteCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointResponseTypeDef(BaseModel):
    deleteVpcEndpointDetail: DeleteVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPoliciesStatsResponseTypeDef(BaseModel):
    AccessPolicyStats: AccessPolicyStatsTypeDef
    LifecyclePolicyStats: LifecyclePolicyStatsTypeDef
    SecurityConfigStats: SecurityConfigStatsTypeDef
    SecurityPolicyStats: SecurityPolicyStatsTypeDef
    TotalPolicyCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListLifecyclePoliciesResponseTypeDef(BaseModel):
    lifecyclePolicySummaries: List[LifecyclePolicySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityConfigsResponseTypeDef(BaseModel):
    nextToken: str
    securityConfigSummaries: List[SecurityConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityPoliciesResponseTypeDef(BaseModel):
    nextToken: str
    securityPolicySummaries: List[SecurityPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVpcEndpointsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    vpcEndpointFilters: Optional[VpcEndpointFiltersTypeDef] = None

class ListVpcEndpointsResponseTypeDef(BaseModel):
    nextToken: str
    vpcEndpointSummaries: List[VpcEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCollectionResponseTypeDef(BaseModel):
    updateCollectionDetail: UpdateCollectionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcEndpointResponseTypeDef(BaseModel):
    UpdateVpcEndpointDetail: UpdateVpcEndpointDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(BaseModel):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(BaseModel):
    accountSettingsDetail: AccountSettingsDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigResponseTypeDef(BaseModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityConfigResponseTypeDef(BaseModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityConfigResponseTypeDef(BaseModel):
    securityConfigDetail: SecurityConfigDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

