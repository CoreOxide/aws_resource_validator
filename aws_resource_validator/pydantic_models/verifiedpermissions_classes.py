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
from aws_resource_validator.pydantic_models.verifiedpermissions_constants import *

class ActionIdentifierTypeDef(BaseValidatorModel):
    actionType: str
    actionId: str


class EntityIdentifierTypeDef(BaseValidatorModel):
    entityType: str
    entityId: str


class BatchGetPolicyErrorItemTypeDef(BaseValidatorModel):
    code: BatchGetPolicyErrorCodeType
    policyStoreId: str
    policyId: str
    message: str


class BatchGetPolicyInputItemTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeterminingPolicyItemTypeDef(BaseValidatorModel):
    policyId: str


class EvaluationErrorItemTypeDef(BaseValidatorModel):
    errorDescription: str


class CognitoGroupConfigurationDetailTypeDef(BaseValidatorModel):
    groupEntityType: Optional[str] = None


class CognitoGroupConfigurationItemTypeDef(BaseValidatorModel):
    groupEntityType: Optional[str] = None


class CognitoGroupConfigurationTypeDef(BaseValidatorModel):
    groupEntityType: str


class ValidationSettingsTypeDef(BaseValidatorModel):
    mode: ValidationModeType


class CreatePolicyTemplateInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    statement: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class DeleteIdentitySourceInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    identitySourceId: str


class DeletePolicyInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyId: str


class DeletePolicyStoreInputTypeDef(BaseValidatorModel):
    policyStoreId: str


class DeletePolicyTemplateInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str


class GetIdentitySourceInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    identitySourceId: str


class IdentitySourceDetailsTypeDef(BaseValidatorModel):
    clientIds: Optional[List[str]] = None
    userPoolArn: Optional[str] = None
    discoveryUrl: Optional[str] = None
    openIdIssuer: Optional[Literal["COGNITO"]] = None


class GetPolicyInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyId: str


class GetPolicyStoreInputTypeDef(BaseValidatorModel):
    policyStoreId: str


class GetPolicyTemplateInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str


class GetSchemaInputTypeDef(BaseValidatorModel):
    policyStoreId: str


class IdentitySourceFilterTypeDef(BaseValidatorModel):
    principalEntityType: Optional[str] = None


class IdentitySourceItemDetailsTypeDef(BaseValidatorModel):
    clientIds: Optional[List[str]] = None
    userPoolArn: Optional[str] = None
    discoveryUrl: Optional[str] = None
    openIdIssuer: Optional[Literal["COGNITO"]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListPolicyStoresInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PolicyStoreItemTypeDef(BaseValidatorModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: Optional[datetime] = None
    description: Optional[str] = None


class ListPolicyTemplatesInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PolicyTemplateItemTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    description: Optional[str] = None


class OpenIdConnectAccessTokenConfigurationDetailTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None


class OpenIdConnectAccessTokenConfigurationItemTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None


class OpenIdConnectAccessTokenConfigurationTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[Sequence[str]] = None


class OpenIdConnectGroupConfigurationDetailTypeDef(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class OpenIdConnectGroupConfigurationItemTypeDef(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class OpenIdConnectGroupConfigurationTypeDef(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class OpenIdConnectIdentityTokenConfigurationDetailTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None


class OpenIdConnectIdentityTokenConfigurationItemTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None


class OpenIdConnectIdentityTokenConfigurationTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[Sequence[str]] = None


class StaticPolicyDefinitionDetailTypeDef(BaseValidatorModel):
    statement: str
    description: Optional[str] = None


class StaticPolicyDefinitionItemTypeDef(BaseValidatorModel):
    description: Optional[str] = None


class StaticPolicyDefinitionTypeDef(BaseValidatorModel):
    statement: str
    description: Optional[str] = None


class SchemaDefinitionTypeDef(BaseValidatorModel):
    cedarJson: Optional[str] = None


class UpdateCognitoGroupConfigurationTypeDef(BaseValidatorModel):
    groupEntityType: str


class UpdateOpenIdConnectAccessTokenConfigurationTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[Sequence[str]] = None


class UpdateOpenIdConnectGroupConfigurationTypeDef(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class UpdateOpenIdConnectIdentityTokenConfigurationTypeDef(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[Sequence[str]] = None


class UpdateStaticPolicyDefinitionTypeDef(BaseValidatorModel):
    statement: str
    description: Optional[str] = None


class UpdatePolicyTemplateInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    statement: str
    description: Optional[str] = None


class EntityReferenceTypeDef(BaseValidatorModel):
    unspecified: Optional[bool] = None
    identifier: Optional[EntityIdentifierTypeDef] = None


class TemplateLinkedPolicyDefinitionDetailTypeDef(BaseValidatorModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None


class TemplateLinkedPolicyDefinitionItemTypeDef(BaseValidatorModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None


class TemplateLinkedPolicyDefinitionTypeDef(BaseValidatorModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None


class BatchGetPolicyInputTypeDef(BaseValidatorModel):
    requests: Sequence[BatchGetPolicyInputItemTypeDef]


class CreateIdentitySourceOutputTypeDef(BaseValidatorModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePolicyOutputTypeDef(BaseValidatorModel):
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


class CreatePolicyStoreOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePolicyTemplateOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetPolicyTemplateOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    description: str
    statement: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    schema: str
    createdDate: datetime
    lastUpdatedDate: datetime
    namespaces: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutSchemaOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    namespaces: List[str]
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIdentitySourceOutputTypeDef(BaseValidatorModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePolicyOutputTypeDef(BaseValidatorModel):
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


class UpdatePolicyStoreOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePolicyTemplateOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class IsAuthorizedOutputTypeDef(BaseValidatorModel):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IsAuthorizedWithTokenOutputTypeDef(BaseValidatorModel):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]
    principal: EntityIdentifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CognitoUserPoolConfigurationDetailTypeDef(BaseValidatorModel):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: Optional[CognitoGroupConfigurationDetailTypeDef] = None


class CognitoUserPoolConfigurationItemTypeDef(BaseValidatorModel):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: Optional[CognitoGroupConfigurationItemTypeDef] = None


class CognitoUserPoolConfigurationTypeDef(BaseValidatorModel):
    userPoolArn: str
    clientIds: Optional[Sequence[str]] = None
    groupConfiguration: Optional[CognitoGroupConfigurationTypeDef] = None


class CreatePolicyStoreInputTypeDef(BaseValidatorModel):
    validationSettings: ValidationSettingsTypeDef
    clientToken: Optional[str] = None
    description: Optional[str] = None


class GetPolicyStoreOutputTypeDef(BaseValidatorModel):
    policyStoreId: str
    arn: str
    validationSettings: ValidationSettingsTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePolicyStoreInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    validationSettings: ValidationSettingsTypeDef
    description: Optional[str] = None


class ListIdentitySourcesInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[Sequence[IdentitySourceFilterTypeDef]] = None


class ListIdentitySourcesInputPaginateTypeDef(BaseValidatorModel):
    policyStoreId: str
    filters: Optional[Sequence[IdentitySourceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyStoresInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyTemplatesInputPaginateTypeDef(BaseValidatorModel):
    policyStoreId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyStoresOutputTypeDef(BaseValidatorModel):
    policyStores: List[PolicyStoreItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPolicyTemplatesOutputTypeDef(BaseValidatorModel):
    policyTemplates: List[PolicyTemplateItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class OpenIdConnectTokenSelectionDetailTypeDef(BaseValidatorModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationDetailTypeDef] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationDetailTypeDef] = None


class OpenIdConnectTokenSelectionItemTypeDef(BaseValidatorModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationItemTypeDef] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationItemTypeDef] = None


class OpenIdConnectTokenSelectionTypeDef(BaseValidatorModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationTypeDef] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationTypeDef] = None


class PutSchemaInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    definition: SchemaDefinitionTypeDef


class UpdateCognitoUserPoolConfigurationTypeDef(BaseValidatorModel):
    userPoolArn: str
    clientIds: Optional[Sequence[str]] = None
    groupConfiguration: Optional[UpdateCognitoGroupConfigurationTypeDef] = None


class UpdateOpenIdConnectTokenSelectionTypeDef(BaseValidatorModel):
    accessTokenOnly: Optional[UpdateOpenIdConnectAccessTokenConfigurationTypeDef] = None
    identityTokenOnly: Optional[UpdateOpenIdConnectIdentityTokenConfigurationTypeDef] = None


class UpdatePolicyDefinitionTypeDef(BaseValidatorModel):
    static: Optional[UpdateStaticPolicyDefinitionTypeDef] = None


class AttributeValueOutputTypeDef(BaseValidatorModel):
    pass


class ContextDefinitionOutputTypeDef(BaseValidatorModel):
    contextMap: Optional[Dict[str, AttributeValueOutputTypeDef]] = None
    cedarJson: Optional[str] = None


class PolicyFilterTypeDef(BaseValidatorModel):
    principal: Optional[EntityReferenceTypeDef] = None
    resource: Optional[EntityReferenceTypeDef] = None
    policyType: Optional[PolicyTypeType] = None
    policyTemplateId: Optional[str] = None


class PolicyDefinitionDetailTypeDef(BaseValidatorModel):
    static: Optional[StaticPolicyDefinitionDetailTypeDef] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionDetailTypeDef] = None


class PolicyDefinitionItemTypeDef(BaseValidatorModel):
    static: Optional[StaticPolicyDefinitionItemTypeDef] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionItemTypeDef] = None


class PolicyDefinitionTypeDef(BaseValidatorModel):
    static: Optional[StaticPolicyDefinitionTypeDef] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionTypeDef] = None


class OpenIdConnectConfigurationDetailTypeDef(BaseValidatorModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionDetailTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationDetailTypeDef] = None


class OpenIdConnectConfigurationItemTypeDef(BaseValidatorModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionItemTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationItemTypeDef] = None


class OpenIdConnectConfigurationTypeDef(BaseValidatorModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationTypeDef] = None


class UpdateOpenIdConnectConfigurationTypeDef(BaseValidatorModel):
    issuer: str
    tokenSelection: UpdateOpenIdConnectTokenSelectionTypeDef
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[UpdateOpenIdConnectGroupConfigurationTypeDef] = None


class UpdatePolicyInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    definition: UpdatePolicyDefinitionTypeDef


class BatchIsAuthorizedInputItemOutputTypeDef(BaseValidatorModel):
    principal: Optional[EntityIdentifierTypeDef] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionOutputTypeDef] = None


class BatchIsAuthorizedWithTokenInputItemOutputTypeDef(BaseValidatorModel):
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionOutputTypeDef] = None


class AttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class ContextDefinitionTypeDef(BaseValidatorModel):
    contextMap: Optional[Mapping[str, AttributeValueUnionTypeDef]] = None
    cedarJson: Optional[str] = None


class EntityItemTypeDef(BaseValidatorModel):
    identifier: EntityIdentifierTypeDef
    attributes: Optional[Mapping[str, AttributeValueUnionTypeDef]] = None
    parents: Optional[Sequence[EntityIdentifierTypeDef]] = None


class BatchGetPolicyOutputItemTypeDef(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    definition: PolicyDefinitionDetailTypeDef
    createdDate: datetime
    lastUpdatedDate: datetime


class GetPolicyOutputTypeDef(BaseValidatorModel):
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


class PolicyItemTypeDef(BaseValidatorModel):
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


class CreatePolicyInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    definition: PolicyDefinitionTypeDef
    clientToken: Optional[str] = None


class ConfigurationDetailTypeDef(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationDetailTypeDef] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationDetailTypeDef] = None


class ConfigurationItemTypeDef(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationItemTypeDef] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationItemTypeDef] = None


class ConfigurationTypeDef(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationTypeDef] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationTypeDef] = None


class UpdateConfigurationTypeDef(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[UpdateCognitoUserPoolConfigurationTypeDef] = None
    openIdConnectConfiguration: Optional[UpdateOpenIdConnectConfigurationTypeDef] = None


class BatchIsAuthorizedOutputItemTypeDef(BaseValidatorModel):
    request: BatchIsAuthorizedInputItemOutputTypeDef
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]


class BatchIsAuthorizedWithTokenOutputItemTypeDef(BaseValidatorModel):
    request: BatchIsAuthorizedWithTokenInputItemOutputTypeDef
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItemTypeDef]
    errors: List[EvaluationErrorItemTypeDef]


class EntitiesDefinitionTypeDef(BaseValidatorModel):
    entityList: Optional[Sequence[EntityItemTypeDef]] = None
    cedarJson: Optional[str] = None


class BatchGetPolicyOutputTypeDef(BaseValidatorModel):
    results: List[BatchGetPolicyOutputItemTypeDef]
    errors: List[BatchGetPolicyErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListPoliciesOutputTypeDef(BaseValidatorModel):
    policies: List[PolicyItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetIdentitySourceOutputTypeDef(BaseValidatorModel):
    createdDate: datetime
    details: IdentitySourceDetailsTypeDef
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    configuration: ConfigurationDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IdentitySourceItemTypeDef(BaseValidatorModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    details: Optional[IdentitySourceItemDetailsTypeDef] = None
    configuration: Optional[ConfigurationItemTypeDef] = None


class CreateIdentitySourceInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    configuration: ConfigurationTypeDef
    clientToken: Optional[str] = None
    principalEntityType: Optional[str] = None


class UpdateIdentitySourceInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    identitySourceId: str
    updateConfiguration: UpdateConfigurationTypeDef
    principalEntityType: Optional[str] = None


class BatchIsAuthorizedOutputTypeDef(BaseValidatorModel):
    results: List[BatchIsAuthorizedOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchIsAuthorizedWithTokenOutputTypeDef(BaseValidatorModel):
    principal: EntityIdentifierTypeDef
    results: List[BatchIsAuthorizedWithTokenOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ContextDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class BatchIsAuthorizedInputItemTypeDef(BaseValidatorModel):
    principal: Optional[EntityIdentifierTypeDef] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionUnionTypeDef] = None


class BatchIsAuthorizedWithTokenInputItemTypeDef(BaseValidatorModel):
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionUnionTypeDef] = None


class IsAuthorizedInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    principal: Optional[EntityIdentifierTypeDef] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionUnionTypeDef] = None
    entities: Optional[EntitiesDefinitionTypeDef] = None


class IsAuthorizedWithTokenInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    identityToken: Optional[str] = None
    accessToken: Optional[str] = None
    action: Optional[ActionIdentifierTypeDef] = None
    resource: Optional[EntityIdentifierTypeDef] = None
    context: Optional[ContextDefinitionUnionTypeDef] = None
    entities: Optional[EntitiesDefinitionTypeDef] = None


class ListIdentitySourcesOutputTypeDef(BaseValidatorModel):
    identitySources: List[IdentitySourceItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchIsAuthorizedInputItemUnionTypeDef(BaseValidatorModel):
    pass


class BatchIsAuthorizedInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    requests: Sequence[BatchIsAuthorizedInputItemUnionTypeDef]
    entities: Optional[EntitiesDefinitionTypeDef] = None


class BatchIsAuthorizedWithTokenInputItemUnionTypeDef(BaseValidatorModel):
    pass


class BatchIsAuthorizedWithTokenInputTypeDef(BaseValidatorModel):
    policyStoreId: str
    requests: Sequence[BatchIsAuthorizedWithTokenInputItemUnionTypeDef]
    identityToken: Optional[str] = None
    accessToken: Optional[str] = None
    entities: Optional[EntitiesDefinitionTypeDef] = None


