from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActionIdentifier(BaseValidatorModel):
    actionType: str
    actionId: str


class EntityIdentifier(BaseValidatorModel):
    entityType: str
    entityId: str


class BatchGetPolicyErrorItem(BaseValidatorModel):
    code: BatchGetPolicyErrorCodeType
    policyStoreId: str
    policyId: str
    message: str


class BatchGetPolicyInputItem(BaseValidatorModel):
    policyStoreId: str
    policyId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeterminingPolicyItem(BaseValidatorModel):
    policyId: str


class EvaluationErrorItem(BaseValidatorModel):
    errorDescription: str


class CognitoGroupConfigurationDetail(BaseValidatorModel):
    groupEntityType: Optional[str] = None


class CognitoGroupConfigurationItem(BaseValidatorModel):
    groupEntityType: Optional[str] = None


class CognitoGroupConfiguration(BaseValidatorModel):
    groupEntityType: str


class ValidationSettings(BaseValidatorModel):
    mode: ValidationModeType


# This class is the input for the 'create_policy_template' function.
class CreatePolicyTemplateInput(BaseValidatorModel):
    policyStoreId: str
    statement: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class DeleteIdentitySourceInput(BaseValidatorModel):
    policyStoreId: str
    identitySourceId: str


class DeletePolicyInput(BaseValidatorModel):
    policyStoreId: str
    policyId: str


class DeletePolicyStoreInput(BaseValidatorModel):
    policyStoreId: str


class DeletePolicyTemplateInput(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str


# This class is the input for the 'get_identity_source' function.
class GetIdentitySourceInput(BaseValidatorModel):
    policyStoreId: str
    identitySourceId: str


class IdentitySourceDetails(BaseValidatorModel):
    clientIds: Optional[List[str]] = None
    userPoolArn: Optional[str] = None
    discoveryUrl: Optional[str] = None
    openIdIssuer: Optional[Literal['COGNITO']] = None


# This class is the input for the 'get_policy' function.
class GetPolicyInput(BaseValidatorModel):
    policyStoreId: str
    policyId: str


# This class is the input for the 'get_policy_store' function.
class GetPolicyStoreInput(BaseValidatorModel):
    policyStoreId: str


# This class is the input for the 'get_policy_template' function.
class GetPolicyTemplateInput(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str


# This class is the input for the 'get_schema' function.
class GetSchemaInput(BaseValidatorModel):
    policyStoreId: str


class IdentitySourceFilter(BaseValidatorModel):
    principalEntityType: Optional[str] = None


class IdentitySourceItemDetails(BaseValidatorModel):
    clientIds: Optional[List[str]] = None
    userPoolArn: Optional[str] = None
    discoveryUrl: Optional[str] = None
    openIdIssuer: Optional[Literal['COGNITO']] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_policy_stores' function.
class ListPolicyStoresInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PolicyStoreItem(BaseValidatorModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: Optional[datetime] = None
    description: Optional[str] = None


# This class is the input for the 'list_policy_templates' function.
class ListPolicyTemplatesInput(BaseValidatorModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PolicyTemplateItem(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    description: Optional[str] = None


class OpenIdConnectAccessTokenConfigurationDetail(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None


class OpenIdConnectAccessTokenConfigurationItem(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None


class OpenIdConnectAccessTokenConfiguration(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None


class OpenIdConnectGroupConfigurationDetail(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class OpenIdConnectGroupConfigurationItem(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class OpenIdConnectGroupConfiguration(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class OpenIdConnectIdentityTokenConfigurationDetail(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None


class OpenIdConnectIdentityTokenConfigurationItem(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None


class OpenIdConnectIdentityTokenConfiguration(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None


class StaticPolicyDefinitionDetail(BaseValidatorModel):
    statement: str
    description: Optional[str] = None


class StaticPolicyDefinitionItem(BaseValidatorModel):
    description: Optional[str] = None


class StaticPolicyDefinition(BaseValidatorModel):
    statement: str
    description: Optional[str] = None


class SchemaDefinition(BaseValidatorModel):
    cedarJson: Optional[str] = None


class UpdateCognitoGroupConfiguration(BaseValidatorModel):
    groupEntityType: str


class UpdateOpenIdConnectAccessTokenConfiguration(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    audiences: Optional[List[str]] = None


class UpdateOpenIdConnectGroupConfiguration(BaseValidatorModel):
    groupClaim: str
    groupEntityType: str


class UpdateOpenIdConnectIdentityTokenConfiguration(BaseValidatorModel):
    principalIdClaim: Optional[str] = None
    clientIds: Optional[List[str]] = None


class UpdateStaticPolicyDefinition(BaseValidatorModel):
    statement: str
    description: Optional[str] = None


# This class is the input for the 'update_policy_template' function.
class UpdatePolicyTemplateInput(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    statement: str
    description: Optional[str] = None


class AttributeValueOutput(BaseValidatorModel):
    boolean: Optional[bool] = None
    entityIdentifier: Optional[EntityIdentifier] = None
    long: Optional[int] = None
    string: Optional[str] = None
    set: Optional[List[Dict[str, Any]]] = None
    record: Optional[Dict[str, Dict[str, Any]]] = None
    ipaddr: Optional[str] = None
    decimal: Optional[str] = None


class AttributeValue(BaseValidatorModel):
    boolean: Optional[bool] = None
    entityIdentifier: Optional[EntityIdentifier] = None
    long: Optional[int] = None
    string: Optional[str] = None
    set: Optional[List[Dict[str, Any]]] = None
    record: Optional[Dict[str, Dict[str, Any]]] = None
    ipaddr: Optional[str] = None
    decimal: Optional[str] = None


class EntityReference(BaseValidatorModel):
    unspecified: Optional[bool] = None
    identifier: Optional[EntityIdentifier] = None


class TemplateLinkedPolicyDefinitionDetail(BaseValidatorModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifier] = None
    resource: Optional[EntityIdentifier] = None


class TemplateLinkedPolicyDefinitionItem(BaseValidatorModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifier] = None
    resource: Optional[EntityIdentifier] = None


class TemplateLinkedPolicyDefinition(BaseValidatorModel):
    policyTemplateId: str
    principal: Optional[EntityIdentifier] = None
    resource: Optional[EntityIdentifier] = None


# This class is the input for the 'batch_get_policy' function.
class BatchGetPolicyInput(BaseValidatorModel):
    requests: List[BatchGetPolicyInputItem]


# This class is the output for the 'create_identity_source' function.
class CreateIdentitySourceOutput(BaseValidatorModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_policy' function.
class CreatePolicyOutput(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifier
    resource: EntityIdentifier
    actions: List[ActionIdentifier]
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_policy_store' function.
class CreatePolicyStoreOutput(BaseValidatorModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_policy_template' function.
class CreatePolicyTemplateOutput(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_policy_template' function.
class GetPolicyTemplateOutput(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    description: str
    statement: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_schema' function.
class GetSchemaOutput(BaseValidatorModel):
    policyStoreId: str
    schema: str
    createdDate: datetime
    lastUpdatedDate: datetime
    namespaces: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_schema' function.
class PutSchemaOutput(BaseValidatorModel):
    policyStoreId: str
    namespaces: List[str]
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_identity_source' function.
class UpdateIdentitySourceOutput(BaseValidatorModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_policy' function.
class UpdatePolicyOutput(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifier
    resource: EntityIdentifier
    actions: List[ActionIdentifier]
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_policy_store' function.
class UpdatePolicyStoreOutput(BaseValidatorModel):
    policyStoreId: str
    arn: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_policy_template' function.
class UpdatePolicyTemplateOutput(BaseValidatorModel):
    policyStoreId: str
    policyTemplateId: str
    createdDate: datetime
    lastUpdatedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'is_authorized' function.
class IsAuthorizedOutput(BaseValidatorModel):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItem]
    errors: List[EvaluationErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'is_authorized_with_token' function.
class IsAuthorizedWithTokenOutput(BaseValidatorModel):
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItem]
    errors: List[EvaluationErrorItem]
    principal: EntityIdentifier
    ResponseMetadata: ResponseMetadata


class CognitoUserPoolConfigurationDetail(BaseValidatorModel):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: Optional[CognitoGroupConfigurationDetail] = None


class CognitoUserPoolConfigurationItem(BaseValidatorModel):
    userPoolArn: str
    clientIds: List[str]
    issuer: str
    groupConfiguration: Optional[CognitoGroupConfigurationItem] = None


class CognitoUserPoolConfiguration(BaseValidatorModel):
    userPoolArn: str
    clientIds: Optional[List[str]] = None
    groupConfiguration: Optional[CognitoGroupConfiguration] = None


# This class is the input for the 'create_policy_store' function.
class CreatePolicyStoreInput(BaseValidatorModel):
    validationSettings: ValidationSettings
    clientToken: Optional[str] = None
    description: Optional[str] = None


# This class is the output for the 'get_policy_store' function.
class GetPolicyStoreOutput(BaseValidatorModel):
    policyStoreId: str
    arn: str
    validationSettings: ValidationSettings
    createdDate: datetime
    lastUpdatedDate: datetime
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_policy_store' function.
class UpdatePolicyStoreInput(BaseValidatorModel):
    policyStoreId: str
    validationSettings: ValidationSettings
    description: Optional[str] = None


# This class is the input for the 'list_identity_sources' function.
class ListIdentitySourcesInput(BaseValidatorModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filters: Optional[List[IdentitySourceFilter]] = None


class ListIdentitySourcesInputPaginate(BaseValidatorModel):
    policyStoreId: str
    filters: Optional[List[IdentitySourceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyStoresInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyTemplatesInputPaginate(BaseValidatorModel):
    policyStoreId: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_policy_stores' function.
class ListPolicyStoresOutput(BaseValidatorModel):
    policyStores: List[PolicyStoreItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_policy_templates' function.
class ListPolicyTemplatesOutput(BaseValidatorModel):
    policyTemplates: List[PolicyTemplateItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class OpenIdConnectTokenSelectionDetail(BaseValidatorModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationDetail] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationDetail] = None


class OpenIdConnectTokenSelectionItem(BaseValidatorModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfigurationItem] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfigurationItem] = None


class OpenIdConnectTokenSelection(BaseValidatorModel):
    accessTokenOnly: Optional[OpenIdConnectAccessTokenConfiguration] = None
    identityTokenOnly: Optional[OpenIdConnectIdentityTokenConfiguration] = None


# This class is the input for the 'put_schema' function.
class PutSchemaInput(BaseValidatorModel):
    policyStoreId: str
    definition: SchemaDefinition


class UpdateCognitoUserPoolConfiguration(BaseValidatorModel):
    userPoolArn: str
    clientIds: Optional[List[str]] = None
    groupConfiguration: Optional[UpdateCognitoGroupConfiguration] = None


class UpdateOpenIdConnectTokenSelection(BaseValidatorModel):
    accessTokenOnly: Optional[UpdateOpenIdConnectAccessTokenConfiguration] = None
    identityTokenOnly: Optional[UpdateOpenIdConnectIdentityTokenConfiguration] = None


class UpdatePolicyDefinition(BaseValidatorModel):
    static: Optional[UpdateStaticPolicyDefinition] = None


class ContextDefinitionOutput(BaseValidatorModel):
    contextMap: Optional[Dict[str, AttributeValueOutput]] = None
    cedarJson: Optional[str] = None

AttributeValueUnion = Union[AttributeValue, AttributeValueOutput]


class PolicyFilter(BaseValidatorModel):
    principal: Optional[EntityReference] = None
    resource: Optional[EntityReference] = None
    policyType: Optional[PolicyTypeType] = None
    policyTemplateId: Optional[str] = None


class PolicyDefinitionDetail(BaseValidatorModel):
    static: Optional[StaticPolicyDefinitionDetail] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionDetail] = None


class PolicyDefinitionItem(BaseValidatorModel):
    static: Optional[StaticPolicyDefinitionItem] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinitionItem] = None


class PolicyDefinition(BaseValidatorModel):
    static: Optional[StaticPolicyDefinition] = None
    templateLinked: Optional[TemplateLinkedPolicyDefinition] = None


class OpenIdConnectConfigurationDetail(BaseValidatorModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionDetail
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationDetail] = None


class OpenIdConnectConfigurationItem(BaseValidatorModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelectionItem
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfigurationItem] = None


class OpenIdConnectConfiguration(BaseValidatorModel):
    issuer: str
    tokenSelection: OpenIdConnectTokenSelection
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[OpenIdConnectGroupConfiguration] = None


class UpdateOpenIdConnectConfiguration(BaseValidatorModel):
    issuer: str
    tokenSelection: UpdateOpenIdConnectTokenSelection
    entityIdPrefix: Optional[str] = None
    groupConfiguration: Optional[UpdateOpenIdConnectGroupConfiguration] = None


# This class is the input for the 'update_policy' function.
class UpdatePolicyInput(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    definition: UpdatePolicyDefinition


class BatchIsAuthorizedInputItemOutput(BaseValidatorModel):
    principal: Optional[EntityIdentifier] = None
    action: Optional[ActionIdentifier] = None
    resource: Optional[EntityIdentifier] = None
    context: Optional[ContextDefinitionOutput] = None


class BatchIsAuthorizedWithTokenInputItemOutput(BaseValidatorModel):
    action: Optional[ActionIdentifier] = None
    resource: Optional[EntityIdentifier] = None
    context: Optional[ContextDefinitionOutput] = None


class ContextDefinition(BaseValidatorModel):
    contextMap: Optional[Dict[str, AttributeValueUnion]] = None
    cedarJson: Optional[str] = None


class EntityItem(BaseValidatorModel):
    identifier: EntityIdentifier
    attributes: Optional[Dict[str, AttributeValueUnion]] = None
    parents: Optional[List[EntityIdentifier]] = None


class ListPoliciesInputPaginate(BaseValidatorModel):
    policyStoreId: str
    filter: Optional[PolicyFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_policies' function.
class ListPoliciesInput(BaseValidatorModel):
    policyStoreId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[PolicyFilter] = None


class BatchGetPolicyOutputItem(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    definition: PolicyDefinitionDetail
    createdDate: datetime
    lastUpdatedDate: datetime


# This class is the output for the 'get_policy' function.
class GetPolicyOutput(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    principal: EntityIdentifier
    resource: EntityIdentifier
    actions: List[ActionIdentifier]
    definition: PolicyDefinitionDetail
    createdDate: datetime
    lastUpdatedDate: datetime
    effect: PolicyEffectType
    ResponseMetadata: ResponseMetadata


class PolicyItem(BaseValidatorModel):
    policyStoreId: str
    policyId: str
    policyType: PolicyTypeType
    definition: PolicyDefinitionItem
    createdDate: datetime
    lastUpdatedDate: datetime
    principal: Optional[EntityIdentifier] = None
    resource: Optional[EntityIdentifier] = None
    actions: Optional[List[ActionIdentifier]] = None
    effect: Optional[PolicyEffectType] = None


# This class is the input for the 'create_policy' function.
class CreatePolicyInput(BaseValidatorModel):
    policyStoreId: str
    definition: PolicyDefinition
    clientToken: Optional[str] = None


class ConfigurationDetail(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationDetail] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationDetail] = None


class ConfigurationItem(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfigurationItem] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfigurationItem] = None


class Configuration(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[CognitoUserPoolConfiguration] = None
    openIdConnectConfiguration: Optional[OpenIdConnectConfiguration] = None


class UpdateConfiguration(BaseValidatorModel):
    cognitoUserPoolConfiguration: Optional[UpdateCognitoUserPoolConfiguration] = None
    openIdConnectConfiguration: Optional[UpdateOpenIdConnectConfiguration] = None


class BatchIsAuthorizedOutputItem(BaseValidatorModel):
    request: BatchIsAuthorizedInputItemOutput
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItem]
    errors: List[EvaluationErrorItem]


class BatchIsAuthorizedWithTokenOutputItem(BaseValidatorModel):
    request: BatchIsAuthorizedWithTokenInputItemOutput
    decision: DecisionType
    determiningPolicies: List[DeterminingPolicyItem]
    errors: List[EvaluationErrorItem]

ContextDefinitionUnion = Union[ContextDefinition, ContextDefinitionOutput]


class EntitiesDefinition(BaseValidatorModel):
    entityList: Optional[List[EntityItem]] = None
    cedarJson: Optional[str] = None


# This class is the output for the 'batch_get_policy' function.
class BatchGetPolicyOutput(BaseValidatorModel):
    results: List[BatchGetPolicyOutputItem]
    errors: List[BatchGetPolicyErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_policies' function.
class ListPoliciesOutput(BaseValidatorModel):
    policies: List[PolicyItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_identity_source' function.
class GetIdentitySourceOutput(BaseValidatorModel):
    createdDate: datetime
    details: IdentitySourceDetails
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    configuration: ConfigurationDetail
    ResponseMetadata: ResponseMetadata


class IdentitySourceItem(BaseValidatorModel):
    createdDate: datetime
    identitySourceId: str
    lastUpdatedDate: datetime
    policyStoreId: str
    principalEntityType: str
    details: Optional[IdentitySourceItemDetails] = None
    configuration: Optional[ConfigurationItem] = None


# This class is the input for the 'create_identity_source' function.
class CreateIdentitySourceInput(BaseValidatorModel):
    policyStoreId: str
    configuration: Configuration
    clientToken: Optional[str] = None
    principalEntityType: Optional[str] = None


# This class is the input for the 'update_identity_source' function.
class UpdateIdentitySourceInput(BaseValidatorModel):
    policyStoreId: str
    identitySourceId: str
    updateConfiguration: UpdateConfiguration
    principalEntityType: Optional[str] = None


# This class is the output for the 'batch_is_authorized' function.
class BatchIsAuthorizedOutput(BaseValidatorModel):
    results: List[BatchIsAuthorizedOutputItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_is_authorized_with_token' function.
class BatchIsAuthorizedWithTokenOutput(BaseValidatorModel):
    principal: EntityIdentifier
    results: List[BatchIsAuthorizedWithTokenOutputItem]
    ResponseMetadata: ResponseMetadata


class BatchIsAuthorizedInputItem(BaseValidatorModel):
    principal: Optional[EntityIdentifier] = None
    action: Optional[ActionIdentifier] = None
    resource: Optional[EntityIdentifier] = None
    context: Optional[ContextDefinitionUnion] = None


class BatchIsAuthorizedWithTokenInputItem(BaseValidatorModel):
    action: Optional[ActionIdentifier] = None
    resource: Optional[EntityIdentifier] = None
    context: Optional[ContextDefinitionUnion] = None


# This class is the input for the 'is_authorized' function.
class IsAuthorizedInput(BaseValidatorModel):
    policyStoreId: str
    principal: Optional[EntityIdentifier] = None
    action: Optional[ActionIdentifier] = None
    resource: Optional[EntityIdentifier] = None
    context: Optional[ContextDefinitionUnion] = None
    entities: Optional[EntitiesDefinition] = None


# This class is the input for the 'is_authorized_with_token' function.
class IsAuthorizedWithTokenInput(BaseValidatorModel):
    policyStoreId: str
    identityToken: Optional[str] = None
    accessToken: Optional[str] = None
    action: Optional[ActionIdentifier] = None
    resource: Optional[EntityIdentifier] = None
    context: Optional[ContextDefinitionUnion] = None
    entities: Optional[EntitiesDefinition] = None


# This class is the output for the 'list_identity_sources' function.
class ListIdentitySourcesOutput(BaseValidatorModel):
    identitySources: List[IdentitySourceItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

BatchIsAuthorizedInputItemUnion = Union[BatchIsAuthorizedInputItem, BatchIsAuthorizedInputItemOutput]

BatchIsAuthorizedWithTokenInputItemUnion = Union[BatchIsAuthorizedWithTokenInputItem, BatchIsAuthorizedWithTokenInputItemOutput]


# This class is the input for the 'batch_is_authorized' function.
class BatchIsAuthorizedInput(BaseValidatorModel):
    policyStoreId: str
    requests: List[BatchIsAuthorizedInputItemUnion]
    entities: Optional[EntitiesDefinition] = None


# This class is the input for the 'batch_is_authorized_with_token' function.
class BatchIsAuthorizedWithTokenInput(BaseValidatorModel):
    policyStoreId: str
    requests: List[BatchIsAuthorizedWithTokenInputItemUnion]
    identityToken: Optional[str] = None
    accessToken: Optional[str] = None
    entities: Optional[EntitiesDefinition] = None