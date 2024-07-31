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
from aws_resource_validator.pydantic_models.verifiedpermissions_constants import *

class ActionIdentifierTypeDef(BaseModel):
    actionType: str
    actionId: str

class EntityIdentifierTypeDef(BaseModel):
    entityType: str
    entityId: str

class ContextDefinitionOutputTypeDef(BaseModel):
    contextMap: Optional[Dict[str, "AttributeValueOutputTypeDef"]] = None

class ContextDefinitionTypeDef(BaseModel):
    contextMap: Optional[Mapping[str, "AttributeValueTypeDef"]] = None

class DeterminingPolicyItemTypeDef(BaseModel):
    policyId: str

class EvaluationErrorItemTypeDef(BaseModel):
    errorDescription: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CognitoGroupConfigurationDetailTypeDef(BaseModel):
    groupEntityType: Optional[str] = None

class CognitoGroupConfigurationItemTypeDef(BaseModel):
    groupEntityType: Optional[str] = None

class CognitoGroupConfigurationTypeDef(BaseModel):
    groupEntityType: str

class ValidationSettingsTypeDef(BaseModel):
    mode: ValidationModeType

class CreatePolicyTemplateInputRequestTypeDef(BaseModel):
    policyStoreId: str
    statement: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class DeleteIdentitySourceInputRequestTypeDef(BaseModel):
    policyStoreId: str
    identitySourceId: str

class DeletePolicyInputRequestTypeDef(BaseModel):
    policyStoreId: str
    policyId: str

class DeletePolicyStoreInputRequestTypeDef(BaseModel):
    policyStoreId: str

class DeletePolicyTemplateInputRequestTypeDef(BaseModel):
    policyStoreId: str
    policyTemplateId: str

class GetIdentitySourceInputRequestTypeDef(BaseModel):
    policyStoreId: str
    identitySourceId: str

class IdentitySourceDetailsTypeDef(BaseModel):
    clientIds: Optional[List[str]] = None
    userPoolArn: Optional[str] = None
    discoveryUrl: Optional[str] = None
    openIdIssuer: Optional[Literal["COGNITO"]] = None

class GetPolicyInputRequestTypeDef(BaseModel):
    policyStoreId: str
    policyId: str

class GetPolicyStoreInputRequestTypeDef(BaseModel):
    policyStoreId: str

class GetPolicyTemplateInputRequestTypeDef(BaseModel):
    policyStoreId: str
    policyTemplateId: str

class GetSchemaInputRequestTypeDef(BaseModel):
    policyStoreId: str

class IdentitySourceFilterTypeDef(BaseModel):
    principalEntityType: Optional[str] = None

class IdentitySourceItemDetailsTypeDef(BaseModel):
    clientIds: Optional[List[str]] = None
    userPoolArn: Optional[str] = None
    discoveryUrl: Optional[str] = None
    openIdIssuer: Optional[Literal["COGNITO"]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListPolicyStoresInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PolicyStoreItemTypeDef(BaseModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: Optional[datetime] = None
    description: Optional[str] = None

class ListPolicyTemplatesInputRequestTypeDef(BaseModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PolicyTemplateItemTypeDef(BaseModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    description: Optional[str] = None

class OpenIdConnectAccessTokenConfigurationDetailTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None

class OpenIdConnectAccessTokenConfigurationItemTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None

class OpenIdConnectAccessTokenConfigurationTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[Sequence[str]] = None

class OpenIdConnectGroupConfigurationDetailTypeDef(BaseModel):
    groupClaim: str
    groupEntityType: str

class OpenIdConnectGroupConfigurationItemTypeDef(BaseModel):
    groupClaim: str
    groupEntityType: str

class OpenIdConnectGroupConfigurationTypeDef(BaseModel):
    groupClaim: str
    groupEntityType: str

class OpenIdConnectIdentityTokenConfigurationDetailTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None

class OpenIdConnectIdentityTokenConfigurationItemTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None

class OpenIdConnectIdentityTokenConfigurationTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[Sequence[str]] = None

class StaticPolicyDefinitionDetailTypeDef(BaseModel):
    statement: str
    description: Optional[str] = None

class StaticPolicyDefinitionItemTypeDef(BaseModel):
    description: Optional[str] = None

class StaticPolicyDefinitionTypeDef(BaseModel):
    statement: str
    description: Optional[str] = None

class SchemaDefinitionTypeDef(BaseModel):
    cedarJson: Optional[str] = None

class UpdateCognitoGroupConfigurationTypeDef(BaseModel):
    groupEntityType: str

class UpdateOpenIdConnectAccessTokenConfigurationTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[Sequence[str]] = None

class UpdateOpenIdConnectGroupConfigurationTypeDef(BaseModel):
    groupClaim: str
    groupEntityType: str

class UpdateOpenIdConnectIdentityTokenConfigurationTypeDef(BaseModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[Sequence[str]] = None

class UpdateStaticPolicyDefinitionTypeDef(BaseModel):
    statement: str
    description: Optional[str] = None

class UpdatePolicyTemplateInputRequestTypeDef(BaseModel):
    policyStoreId: str
    policyTemplateId: str
    statement: str
    description: Optional[str] = None

class AttributeValueOutputTypeDef(BaseModel):
    boolean: Optional[bool] = None
    entityIdentifier: Optional[EntityIdentifierTypeDef] = None
    long: Optional[int] = None
    string: Optional[str] = None
    set: Optional[List[Dict[str, Any]]] = None
    record: Optional[Dict[str, Dict[str, Any]]] = None

class AttributeValueTypeDef(BaseModel):
    boolean: Optional[bool] = None
    entityIdentifier: Optional[EntityIdentifierTypeDef] = None
    long: Optional[int] = None
    string: Optional[str] = None
    set: Optional[Sequence[Dict[str, Any]]] = None
    record: Optional[Mapping[str, Dict[str, Any]]] = None

class EntityItemTypeDef(BaseModel):
    identifier: EntityIdentifierTypeDef
    attributes: Optional[Mapping[str, "AttributeValueTypeDef"]] = None
    parents: Optional[Sequence[EntityIdentifierTypeDef]] = None

class EntityReferenceTypeDef(BaseModel):
    unspecified: Optional[bool] = None
    identifier: Optional[EntityIdentifierTypeDef] = None

class TemplateLinkedPolicyDefinitionDetailTypeDef(BaseModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None

class TemplateLinkedPolicyDefinitionItemTypeDef(BaseModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None

class TemplateLinkedPolicyDefinitionTypeDef(BaseModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None

class BatchIsAuthorizedInputItemOutputTypeDef(BaseModel):
    principal: Optional[EntityIdentifierTypeDef] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionOutputTypeDef] = None

class BatchIsAuthorizedWithTokenInputItemOutputTypeDef(BaseModel):
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionOutputTypeDef] = None

class BatchIsAuthorizedInputItemTypeDef(BaseModel):
    principal: Optional[EntityIdentifierTypeDef] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionTypeDef] = None

class BatchIsAuthorizedWithTokenInputItemTypeDef(BaseModel):
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionTypeDef] = None

class CreateIdentitySourceOutputTypeDef(BaseModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyOutputTypeDef(BaseModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifierTypeDef
    resource: EntityIdentifierTypeDef
    actions: List[ActionIdentifierTypeDef]
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyStoreOutputTypeDef(BaseModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyTemplateOutputTypeDef(BaseModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyTemplateOutputTypeDef(BaseModel):
    policyStoreId: str
    policyTemplateId: str
    description: str
    statement: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaOutputTypeDef(BaseModel):
    policyStoreId: str
    schema: str
    createdDate: datetime
    lastUpdatedDate: datetime
    namespaces: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class IsAuthorizedOutputTypeDef(BaseModel):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IsAuthorizedWithTokenOutputTypeDef(BaseModel):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]
    principal: EntityIdentifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSchemaOutputTypeDef(BaseModel):
    policyStoreId: str
    namespaces: List[str]
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdentitySourceOutputTypeDef(BaseModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyOutputTypeDef(BaseModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifierTypeDef
    resource: EntityIdentifierTypeDef
    actions: List[ActionIdentifierTypeDef]
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyStoreOutputTypeDef(BaseModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyTemplateOutputTypeDef(BaseModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CognitoUserPoolConfigurationDetailTypeDef(BaseModel):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: Optional[CognitoGroupConfigurationDetailTypeDef] = None

class CognitoUserPoolConfigurationItemTypeDef(BaseModel):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: Optional[CognitoGroupConfigurationItemTypeDef] = None

class CognitoUserPoolConfigurationTypeDef(BaseModel):
    userPoolArn: str
    clientIds: Optional[Sequence[str]] = None
    groupConfiguration: Optional[CognitoGroupConfigurationTypeDef] = None

class CreatePolicyStoreInputRequestTypeDef(BaseModel):
    validationSettings: ValidationSettingsTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None

class GetPolicyStoreOutputTypeDef(BaseModel):
    policyStoreId: str
    arn: str
    validationSettings: ValidationSettingsTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyStoreInputRequestTypeDef(BaseModel):
    policyStoreId: str
    validationSettings: ValidationSettingsTypeDef
    description: Optional[str] = None

class ListIdentitySourcesInputRequestTypeDef(BaseModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[IdentitySourceFilterTypeDef]] = None

class ListIdentitySourcesInputListIdentitySourcesPaginateTypeDef(BaseModel):
    policyStoreId: str
    filters: Optional[Sequence[IdentitySourceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyStoresInputListPolicyStoresPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyTemplatesInputListPolicyTemplatesPaginateTypeDef(BaseModel):
    policyStoreId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyStoresOutputTypeDef(BaseModel):
    nextToken: str
    policyStores: List[PolicyStoreItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyTemplatesOutputTypeDef(BaseModel):
    nextToken: str
    policyTemplates: List[PolicyTemplateItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OpenIdConnectTokenSelectionDetailTypeDef(BaseModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationDetailTypeDef] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationDetailTypeDef] = None

class OpenIdConnectTokenSelectionItemTypeDef(BaseModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationItemTypeDef] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationItemTypeDef] = None

class OpenIdConnectTokenSelectionTypeDef(BaseModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationTypeDef] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationTypeDef] = None

class PutSchemaInputRequestTypeDef(BaseModel):
    policyStoreId: str
    definition: SchemaDefinitionTypeDef

class UpdateCognitoUserPoolConfigurationTypeDef(BaseModel):
    userPoolArn: str
    clientIds: Optional[Sequence[str]] = None
    groupConfiguration: Optional[UpdateCognitoGroupConfigurationTypeDef] = None

class UpdateOpenIdConnectTokenSelectionTypeDef(BaseModel):
    accessTokenOnly: Optional[UpdateOpenIdConnectAccessTokenConfigurationTypeDef] = None
    identityTokenOnly: Optional[UpdateOpenIdConnectIdentityTokenConfigurationTypeDef] = None

class UpdatePolicyDefinitionTypeDef(BaseModel):
    static: Optional[UpdateStaticPolicyDefinitionTypeDef] = None

class EntitiesDefinitionTypeDef(BaseModel):
    entityList: Optional[Sequence[EntityItemTypeDef]] = None

class PolicyFilterTypeDef(BaseModel):
    principal: Optional[EntityReferenceTypeDef] = None
    resource: Optional[EntityReferenceTypeDef] = None
    policyType: Optional[PolicyTypeType] = None
    policyTemplateId: Optional[str] = None

class PolicyDefinitionDetailTypeDef(BaseModel):
    static: Optional[StaticPolicyDefinitionDetailTypeDef] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionDetailTypeDef] = None

class PolicyDefinitionItemTypeDef(BaseModel):
    static: Optional[StaticPolicyDefinitionItemTypeDef] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionItemTypeDef] = None

class PolicyDefinitionTypeDef(BaseModel):
    static: Optional[StaticPolicyDefinitionTypeDef] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionTypeDef] = None

class BatchIsAuthorizedOutputItemTypeDef(BaseModel):
    request: BatchIsAuthorizedInputItemOutputTypeDef
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]

class BatchIsAuthorizedWithTokenOutputItemTypeDef(BaseModel):
    request: BatchIsAuthorizedWithTokenInputItemOutputTypeDef
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]

class OpenIdConnectConfigurationDetailTypeDef(BaseModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionDetailTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationDetailTypeDef] = None

class OpenIdConnectConfigurationItemTypeDef(BaseModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionItemTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationItemTypeDef] = None

class OpenIdConnectConfigurationTypeDef(BaseModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationTypeDef] = None

class UpdateOpenIdConnectConfigurationTypeDef(BaseModel):
    issuer: str
    tokenSelection: UpdateOpenIdConnectTokenSelectionTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[UpdateOpenIdConnectGroupConfigurationTypeDef] = None

class UpdatePolicyInputRequestTypeDef(BaseModel):
    policyStoreId: str
    policyId: str
    definition: UpdatePolicyDefinitionTypeDef

class IsAuthorizedInputRequestTypeDef(BaseModel):
    policyStoreId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionTypeDef] = None
    entities: Optional[EntitiesDefinitionTypeDef] = None

class IsAuthorizedWithTokenInputRequestTypeDef(BaseModel):
    policyStoreId: str
    identityToken: Optional[str] = None
    accessToken: Optional[str] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionTypeDef] = None
    entities: Optional[EntitiesDefinitionTypeDef] = None

class ListPoliciesInputListPoliciesPaginateTypeDef(BaseModel):
    policyStoreId: str
    filter: Optional[PolicyFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesInputRequestTypeDef(BaseModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[PolicyFilterTypeDef] = None

class GetPolicyOutputTypeDef(BaseModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifierTypeDef
    resource: EntityIdentifierTypeDef
    actions: List[ActionIdentifierTypeDef]
    definition: PolicyDefinitionDetailTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyItemTypeDef(BaseModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    definition: PolicyDefinitionItemTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime
    principal: Optional[EntityIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    actions: Optional[List[ActionIdentifierTypeDef]] = None
    effect: Optional[PolicyEffectType] = None

class CreatePolicyInputRequestTypeDef(BaseModel):
    policyStoreId: str
    definition: PolicyDefinitionTypeDef
    clientToken: Optional[str] = None

class BatchIsAuthorizedOutputTypeDef(BaseModel):
    results: List[BatchIsAuthorizedOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchIsAuthorizedWithTokenOutputTypeDef(BaseModel):
    principal: EntityIdentifierTypeDef
    results: List[BatchIsAuthorizedWithTokenOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchIsAuthorizedInputRequestTypeDef(BaseModel):
    policyStoreId: str
    requests: Sequence[BatchIsAuthorizedInputItemUnionTypeDef]
    entities: Optional[EntitiesDefinitionTypeDef] = None

class BatchIsAuthorizedWithTokenInputRequestTypeDef(BaseModel):
    policyStoreId: str
    requests: Sequence[BatchIsAuthorizedWithTokenInputItemUnionTypeDef]
    identityToken: Optional[str] = None
    accessToken: Optional[str] = None
    entities: Optional[EntitiesDefinitionTypeDef] = None

class ConfigurationDetailTypeDef(BaseModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationDetailTypeDef] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationDetailTypeDef] = None

class ConfigurationItemTypeDef(BaseModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationItemTypeDef] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationItemTypeDef] = None

class ConfigurationTypeDef(BaseModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationTypeDef] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationTypeDef] = None

class UpdateConfigurationTypeDef(BaseModel):
    cognitoUserPoolConfiguration: Optional[UpdateCognitoUserPoolConfigurationTypeDef] = None
    openIdConnectConfiguration: Optional[UpdateOpenIdConnectConfigurationTypeDef] = None

class ListPoliciesOutputTypeDef(BaseModel):
    nextToken: str
    policies: List[PolicyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentitySourceOutputTypeDef(BaseModel):
    createdDate: datetime
    details: IdentitySourceDetailsTypeDef
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    configuration: ConfigurationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IdentitySourceItemTypeDef(BaseModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    details: Optional[IdentitySourceItemDetailsTypeDef] = None
    configuration: Optional[ConfigurationItemTypeDef] = None

class CreateIdentitySourceInputRequestTypeDef(BaseModel):
    policyStoreId: str
    configuration: ConfigurationTypeDef
    clientToken: Optional[str] = None
    principalEntityType: Optional[str] = None

class UpdateIdentitySourceInputRequestTypeDef(BaseModel):
    policyStoreId: str
    identitySourceId: str
    updateConfiguration: UpdateConfigurationTypeDef
    principalEntityType: Optional[str] = None

class ListIdentitySourcesOutputTypeDef(BaseModel):
    nextToken: str
    identitySources: List[IdentitySourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

