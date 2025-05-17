from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class GraphQLRenderConfig(BaseValidatorModel):
    typesFilePath: str
    queriesFilePath: str
    mutationsFilePath: str
    subscriptionsFilePath: str
    fragmentsFilePath: str


class CodegenDependency(BaseValidatorModel):
    name: Optional[str] = None
    supportedVersion: Optional[str] = None
    isSemVer: Optional[bool] = None
    reason: Optional[str] = None


class CodegenFeatureFlags(BaseValidatorModel):
    isRelationshipSupported: Optional[bool] = None
    isNonModelSupported: Optional[bool] = None


class CodegenGenericDataEnumOutput(BaseValidatorModel):
    values: List[str]


class CodegenGenericDataEnum(BaseValidatorModel):
    values: List[str]


class CodegenGenericDataRelationshipTypeOutput(BaseValidatorModel):
    type: GenericDataRelationshipTypeType
    relatedModelName: str
    relatedModelFields: Optional[List[str]] = None
    canUnlinkAssociatedModel: Optional[bool] = None
    relatedJoinFieldName: Optional[str] = None
    relatedJoinTableName: Optional[str] = None
    belongsToFieldOnRelatedModel: Optional[str] = None
    associatedFields: Optional[List[str]] = None
    isHasManyIndex: Optional[bool] = None


class CodegenGenericDataRelationshipType(BaseValidatorModel):
    type: GenericDataRelationshipTypeType
    relatedModelName: str
    relatedModelFields: Optional[List[str]] = None
    canUnlinkAssociatedModel: Optional[bool] = None
    relatedJoinFieldName: Optional[str] = None
    relatedJoinTableName: Optional[str] = None
    belongsToFieldOnRelatedModel: Optional[str] = None
    associatedFields: Optional[List[str]] = None
    isHasManyIndex: Optional[bool] = None


class CodegenJobAsset(BaseValidatorModel):
    downloadUrl: Optional[str] = None


class CodegenJobSummary(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None


class PredicateOutput(BaseValidatorModel):
    or_: Optional[List[Dict[str, Any]]] = None
    and_: Optional[List[Dict[str, Any]]] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    operandType: Optional[str] = None


class PredicatePaginator(BaseValidatorModel):
    or_: Optional[List[Dict[str, Any]]] = None
    and_: Optional[List[Dict[str, Any]]] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    operandType: Optional[str] = None


class ComponentConditionPropertyOutput(BaseValidatorModel):
    property: Optional[str] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    then: Optional[Dict[str, Any]] = None
    else_: Optional[Dict[str, Any]] = None
    operandType: Optional[str] = None


class ComponentConditionPropertyPaginator(BaseValidatorModel):
    property: Optional[str] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    then: Optional[Dict[str, Any]] = None
    else_: Optional[Dict[str, Any]] = None
    operandType: Optional[str] = None


class ComponentConditionProperty(BaseValidatorModel):
    property: Optional[str] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    then: Optional[Dict[str, Any]] = None
    else_: Optional[Dict[str, Any]] = None
    operandType: Optional[str] = None


class SortProperty(BaseValidatorModel):
    field: str
    direction: SortDirectionType


class ComponentVariantOutput(BaseValidatorModel):
    variantValues: Optional[Dict[str, str]] = None
    overrides: Optional[Dict[str, Dict[str, str]]] = None


class ComponentPropertyBindingProperties(BaseValidatorModel):
    property: str
    field: Optional[str] = None


class FormBindingElement(BaseValidatorModel):
    element: str
    property: str


class ComponentSummary(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    componentType: str


class ComponentVariant(BaseValidatorModel):
    variantValues: Optional[Dict[str, str]] = None
    overrides: Optional[Dict[str, Dict[str, str]]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FormDataTypeConfig(BaseValidatorModel):
    dataSourceType: FormDataSourceTypeType
    dataTypeName: str


# This class is the input for the 'delete_component' function.
class DeleteComponentRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str


# This class is the input for the 'delete_form' function.
class DeleteFormRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str


# This class is the input for the 'delete_theme' function.
class DeleteThemeRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str


class ExchangeCodeForTokenRequestBody(BaseValidatorModel):
    code: str
    redirectUri: str
    clientId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'export_components' function.
class ExportComponentsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


# This class is the input for the 'export_forms' function.
class ExportFormsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


# This class is the input for the 'export_themes' function.
class ExportThemesRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


class FieldPosition(BaseValidatorModel):
    fixed: Optional[Literal['first']] = None
    rightOf: Optional[str] = None
    below: Optional[str] = None


class FieldValidationConfigurationOutput(BaseValidatorModel):
    type: str
    strValues: Optional[List[str]] = None
    numValues: Optional[List[int]] = None
    validationMessage: Optional[str] = None


class FileUploaderFieldConfigOutput(BaseValidatorModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: List[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None


class FieldValidationConfiguration(BaseValidatorModel):
    type: str
    strValues: Optional[List[str]] = None
    numValues: Optional[List[int]] = None
    validationMessage: Optional[str] = None


class FileUploaderFieldConfig(BaseValidatorModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: List[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None


class FormInputBindingPropertiesValueProperties(BaseValidatorModel):
    model: Optional[str] = None


class FormInputValuePropertyBindingProperties(BaseValidatorModel):
    property: str
    field: Optional[str] = None


class FormStyleConfig(BaseValidatorModel):
    tokenReference: Optional[str] = None
    value: Optional[str] = None


# This class is the input for the 'get_codegen_job' function.
class GetCodegenJobRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str


# This class is the input for the 'get_component' function.
class GetComponentRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str


# This class is the input for the 'get_form' function.
class GetFormRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str


# This class is the input for the 'get_metadata' function.
class GetMetadataRequest(BaseValidatorModel):
    appId: str
    environmentName: str


# This class is the input for the 'get_theme' function.
class GetThemeRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str


# This class is the input for the 'list_codegen_jobs' function.
class ListCodegenJobsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_components' function.
class ListComponentsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_forms' function.
class ListFormsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_themes' function.
class ListThemesRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ThemeSummary(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str


class Predicate(BaseValidatorModel):
    or_: Optional[List[Dict[str, Any]]] = None
    and_: Optional[List[Dict[str, Any]]] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    operandType: Optional[str] = None


class PutMetadataFlagBody(BaseValidatorModel):
    newValue: str


class RefreshTokenRequestBody(BaseValidatorModel):
    token: str
    clientId: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class ThemeValueOutput(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List[Dict[str, Any]]] = None


class ThemeValuePaginator(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List[Dict[str, Any]]] = None


class ThemeValue(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List[Dict[str, Any]]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class ApiConfigurationOutput(BaseValidatorModel):
    graphQLConfig: Optional[GraphQLRenderConfig] = None
    dataStoreConfig: Optional[Dict[str, Any]] = None
    noApiConfig: Optional[Dict[str, Any]] = None


class ApiConfiguration(BaseValidatorModel):
    graphQLConfig: Optional[GraphQLRenderConfig] = None
    dataStoreConfig: Optional[Dict[str, Any]] = None
    noApiConfig: Optional[Dict[str, Any]] = None

CodegenGenericDataEnumUnion = Union[CodegenGenericDataEnum, CodegenGenericDataEnumOutput]


class CodegenGenericDataFieldOutput(BaseValidatorModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeOutput] = None

CodegenGenericDataRelationshipTypeUnion = Union[CodegenGenericDataRelationshipType, CodegenGenericDataRelationshipTypeOutput]


class ComponentBindingPropertiesValuePropertiesOutput(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List[PredicateOutput]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


class ComponentBindingPropertiesValuePropertiesPaginator(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List[PredicatePaginator]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None

ComponentConditionPropertyUnion = Union[ComponentConditionProperty, ComponentConditionPropertyOutput]


class ComponentDataConfigurationOutput(BaseValidatorModel):
    model: str
    sort: Optional[List[SortProperty]] = None
    predicate: Optional[PredicateOutput] = None
    identifiers: Optional[List[str]] = None


class ComponentDataConfigurationPaginator(BaseValidatorModel):
    model: str
    sort: Optional[List[SortProperty]] = None
    predicate: Optional[PredicatePaginator] = None
    identifiers: Optional[List[str]] = None


class ComponentPropertyOutput(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[ComponentPropertyBindingProperties] = None
    collectionBindingProperties: Optional[ComponentPropertyBindingProperties] = None
    defaultValue: Optional[str] = None
    model: Optional[str] = None
    bindings: Optional[Dict[str, FormBindingElement]] = None
    event: Optional[str] = None
    userAttribute: Optional[str] = None
    concat: Optional[List[Dict[str, Any]]] = None
    condition: Optional[ComponentConditionPropertyOutput] = None
    configured: Optional[bool] = None
    type: Optional[str] = None
    importedValue: Optional[str] = None
    componentName: Optional[str] = None
    property: Optional[str] = None


class ComponentPropertyPaginator(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[ComponentPropertyBindingProperties] = None
    collectionBindingProperties: Optional[ComponentPropertyBindingProperties] = None
    defaultValue: Optional[str] = None
    model: Optional[str] = None
    bindings: Optional[Dict[str, FormBindingElement]] = None
    event: Optional[str] = None
    userAttribute: Optional[str] = None
    concat: Optional[List[Dict[str, Any]]] = None
    condition: Optional[ComponentConditionPropertyPaginator] = None
    configured: Optional[bool] = None
    type: Optional[str] = None
    importedValue: Optional[str] = None
    componentName: Optional[str] = None
    property: Optional[str] = None

ComponentVariantUnion = Union[ComponentVariant, ComponentVariantOutput]


# This class is the output for the 'put_metadata_flag' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'exchange_code_for_token' function.
class ExchangeCodeForTokenResponse(BaseValidatorModel):
    accessToken: str
    expiresIn: int
    refreshToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_metadata' function.
class GetMetadataResponse(BaseValidatorModel):
    features: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_codegen_jobs' function.
class ListCodegenJobsResponse(BaseValidatorModel):
    entities: List[CodegenJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_components' function.
class ListComponentsResponse(BaseValidatorModel):
    entities: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'refresh_token' function.
class RefreshTokenResponse(BaseValidatorModel):
    accessToken: str
    expiresIn: int
    ResponseMetadata: ResponseMetadata


class FormSummary(BaseValidatorModel):
    appId: str
    dataType: FormDataTypeConfig
    environmentName: str
    formActionType: FormActionTypeType
    id: str
    name: str


# This class is the input for the 'exchange_code_for_token' function.
class ExchangeCodeForTokenRequest(BaseValidatorModel):
    provider: Literal['figma']
    request: ExchangeCodeForTokenRequestBody


class ExportComponentsRequestPaginate(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ExportFormsRequestPaginate(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ExportThemesRequestPaginate(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCodegenJobsRequestPaginate(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComponentsRequestPaginate(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFormsRequestPaginate(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThemesRequestPaginate(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class FormButton(BaseValidatorModel):
    excluded: Optional[bool] = None
    children: Optional[str] = None
    position: Optional[FieldPosition] = None


class SectionalElement(BaseValidatorModel):
    type: str
    position: Optional[FieldPosition] = None
    text: Optional[str] = None
    level: Optional[int] = None
    orientation: Optional[str] = None
    excluded: Optional[bool] = None

FieldValidationConfigurationUnion = Union[FieldValidationConfiguration, FieldValidationConfigurationOutput]

FileUploaderFieldConfigUnion = Union[FileUploaderFieldConfig, FileUploaderFieldConfigOutput]


class FormInputBindingPropertiesValue(BaseValidatorModel):
    type: Optional[str] = None
    bindingProperties: Optional[FormInputBindingPropertiesValueProperties] = None


class FormInputValuePropertyOutput(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingProperties] = None
    concat: Optional[List[Dict[str, Any]]] = None


class FormInputValuePropertyPaginator(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingProperties] = None
    concat: Optional[List[Dict[str, Any]]] = None


class FormInputValueProperty(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingProperties] = None
    concat: Optional[List[Dict[str, Any]]] = None


class FormStyle(BaseValidatorModel):
    horizontalGap: Optional[FormStyleConfig] = None
    verticalGap: Optional[FormStyleConfig] = None
    outerPadding: Optional[FormStyleConfig] = None


# This class is the output for the 'list_themes' function.
class ListThemesResponse(BaseValidatorModel):
    entities: List[ThemeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

PredicateUnion = Union[Predicate, PredicateOutput]


# This class is the input for the 'put_metadata_flag' function.
class PutMetadataFlagRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    featureName: str
    body: PutMetadataFlagBody


# This class is the input for the 'refresh_token' function.
class RefreshTokenRequest(BaseValidatorModel):
    provider: Literal['figma']
    refreshTokenBody: RefreshTokenRequestBody


class ThemeValuesOutput(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValueOutput] = None


class ThemeValuesPaginator(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValuePaginator] = None

ThemeValueUnion = Union[ThemeValue, ThemeValueOutput]


class ReactStartCodegenJobDataOutput(BaseValidatorModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationOutput] = None
    dependencies: Optional[Dict[str, str]] = None

ApiConfigurationUnion = Union[ApiConfiguration, ApiConfigurationOutput]


class CodegenGenericDataModelOutput(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldOutput]
    primaryKeys: List[str]
    isJoinTable: Optional[bool] = None


class CodegenGenericDataNonModelOutput(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldOutput]


class CodegenGenericDataField(BaseValidatorModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeUnion] = None


class ComponentBindingPropertiesValueOutput(BaseValidatorModel):
    type: Optional[str] = None
    bindingProperties: Optional[ComponentBindingPropertiesValuePropertiesOutput] = None
    defaultValue: Optional[str] = None


class ComponentBindingPropertiesValuePaginator(BaseValidatorModel):
    type: Optional[str] = None
    bindingProperties: Optional[ComponentBindingPropertiesValuePropertiesPaginator] = None
    defaultValue: Optional[str] = None


class ComponentProperty(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[ComponentPropertyBindingProperties] = None
    collectionBindingProperties: Optional[ComponentPropertyBindingProperties] = None
    defaultValue: Optional[str] = None
    model: Optional[str] = None
    bindings: Optional[Dict[str, FormBindingElement]] = None
    event: Optional[str] = None
    userAttribute: Optional[str] = None
    concat: Optional[List[Dict[str, Any]]] = None
    condition: Optional[ComponentConditionPropertyUnion] = None
    configured: Optional[bool] = None
    type: Optional[str] = None
    importedValue: Optional[str] = None
    componentName: Optional[str] = None
    property: Optional[str] = None


class MutationActionSetStateParameterOutput(BaseValidatorModel):
    componentName: str
    property: str
    set: ComponentPropertyOutput


class MutationActionSetStateParameterPaginator(BaseValidatorModel):
    componentName: str
    property: str
    set: ComponentPropertyPaginator


# This class is the output for the 'list_forms' function.
class ListFormsResponse(BaseValidatorModel):
    entities: List[FormSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FormCTA(BaseValidatorModel):
    position: Optional[FormButtonsPositionType] = None
    clear: Optional[FormButton] = None
    cancel: Optional[FormButton] = None
    submit: Optional[FormButton] = None


class ValueMappingOutput(BaseValidatorModel):
    value: FormInputValuePropertyOutput
    displayValue: Optional[FormInputValuePropertyOutput] = None


class ValueMappingPaginator(BaseValidatorModel):
    value: FormInputValuePropertyPaginator
    displayValue: Optional[FormInputValuePropertyPaginator] = None

FormInputValuePropertyUnion = Union[FormInputValueProperty, FormInputValuePropertyOutput]


class ComponentBindingPropertiesValueProperties(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List[PredicateUnion]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


class ComponentDataConfiguration(BaseValidatorModel):
    model: str
    sort: Optional[List[SortProperty]] = None
    predicate: Optional[PredicateUnion] = None
    identifiers: Optional[List[str]] = None


class Theme(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    createdAt: datetime
    values: List[ThemeValuesOutput]
    modifiedAt: Optional[datetime] = None
    overrides: Optional[List[ThemeValuesOutput]] = None
    tags: Optional[Dict[str, str]] = None


class ThemePaginator(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    createdAt: datetime
    values: List[ThemeValuesPaginator]
    modifiedAt: Optional[datetime] = None
    overrides: Optional[List[ThemeValuesPaginator]] = None
    tags: Optional[Dict[str, str]] = None


class ThemeValues(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValueUnion] = None


class CodegenJobRenderConfigOutput(BaseValidatorModel):
    react: Optional[ReactStartCodegenJobDataOutput] = None


class ReactStartCodegenJobData(BaseValidatorModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationUnion] = None
    dependencies: Optional[Dict[str, str]] = None


class CodegenJobGenericDataSchemaOutput(BaseValidatorModel):
    dataSourceType: Literal['DataStore']
    models: Dict[str, CodegenGenericDataModelOutput]
    enums: Dict[str, CodegenGenericDataEnumOutput]
    nonModels: Dict[str, CodegenGenericDataNonModelOutput]

CodegenGenericDataFieldUnion = Union[CodegenGenericDataField, CodegenGenericDataFieldOutput]


class CodegenGenericDataModel(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataField]
    primaryKeys: List[str]
    isJoinTable: Optional[bool] = None

ComponentPropertyUnion = Union[ComponentProperty, ComponentPropertyOutput]


class ActionParametersOutput(BaseValidatorModel):
    type: Optional[ComponentPropertyOutput] = None
    url: Optional[ComponentPropertyOutput] = None
    anchor: Optional[ComponentPropertyOutput] = None
    target: Optional[ComponentPropertyOutput] = None
    global_: Optional[ComponentPropertyOutput] = None
    model: Optional[str] = None
    id: Optional[ComponentPropertyOutput] = None
    fields: Optional[Dict[str, ComponentPropertyOutput]] = None
    state: Optional[MutationActionSetStateParameterOutput] = None


class ActionParametersPaginator(BaseValidatorModel):
    type: Optional[ComponentPropertyPaginator] = None
    url: Optional[ComponentPropertyPaginator] = None
    anchor: Optional[ComponentPropertyPaginator] = None
    target: Optional[ComponentPropertyPaginator] = None
    global_: Optional[ComponentPropertyPaginator] = None
    model: Optional[str] = None
    id: Optional[ComponentPropertyPaginator] = None
    fields: Optional[Dict[str, ComponentPropertyPaginator]] = None
    state: Optional[MutationActionSetStateParameterPaginator] = None


class ValueMappingsOutput(BaseValidatorModel):
    values: List[ValueMappingOutput]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValue]] = None


class ValueMappingsPaginator(BaseValidatorModel):
    values: List[ValueMappingPaginator]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValue]] = None


class ValueMapping(BaseValidatorModel):
    value: FormInputValuePropertyUnion
    displayValue: Optional[FormInputValuePropertyUnion] = None

ComponentBindingPropertiesValuePropertiesUnion = Union[ComponentBindingPropertiesValueProperties, ComponentBindingPropertiesValuePropertiesOutput]

ComponentDataConfigurationUnion = Union[ComponentDataConfiguration, ComponentDataConfigurationOutput]


# This class is the output for the 'create_theme' function.
class CreateThemeResponse(BaseValidatorModel):
    entity: Theme
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_themes' function.
class ExportThemesResponse(BaseValidatorModel):
    entities: List[Theme]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_theme' function.
class GetThemeResponse(BaseValidatorModel):
    theme: Theme
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_theme' function.
class UpdateThemeResponse(BaseValidatorModel):
    entity: Theme
    ResponseMetadata: ResponseMetadata


class ExportThemesResponsePaginator(BaseValidatorModel):
    entities: List[ThemePaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ThemeValuesUnion = Union[ThemeValues, ThemeValuesOutput]

ReactStartCodegenJobDataUnion = Union[ReactStartCodegenJobData, ReactStartCodegenJobDataOutput]


class CodegenJob(BaseValidatorModel):
    id: str
    appId: str
    environmentName: str
    renderConfig: Optional[CodegenJobRenderConfigOutput] = None
    genericDataSchema: Optional[CodegenJobGenericDataSchemaOutput] = None
    autoGenerateForms: Optional[bool] = None
    features: Optional[CodegenFeatureFlags] = None
    status: Optional[CodegenJobStatusType] = None
    statusMessage: Optional[str] = None
    asset: Optional[CodegenJobAsset] = None
    tags: Optional[Dict[str, str]] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    dependencies: Optional[List[CodegenDependency]] = None


class CodegenGenericDataNonModel(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldUnion]

CodegenGenericDataModelUnion = Union[CodegenGenericDataModel, CodegenGenericDataModelOutput]


class MutationActionSetStateParameter(BaseValidatorModel):
    componentName: str
    property: str
    set: ComponentPropertyUnion


class ComponentEventOutput(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersOutput] = None
    bindingEvent: Optional[str] = None


class ComponentEventPaginator(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersPaginator] = None
    bindingEvent: Optional[str] = None


class FieldInputConfigOutput(BaseValidatorModel):
    type: str
    required: Optional[bool] = None
    readOnly: Optional[bool] = None
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None
    descriptiveText: Optional[str] = None
    defaultChecked: Optional[bool] = None
    defaultCountryCode: Optional[str] = None
    valueMappings: Optional[ValueMappingsOutput] = None
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    step: Optional[float] = None
    value: Optional[str] = None
    isArray: Optional[bool] = None
    fileUploaderConfig: Optional[FileUploaderFieldConfigOutput] = None


class FieldInputConfigPaginator(BaseValidatorModel):
    type: str
    required: Optional[bool] = None
    readOnly: Optional[bool] = None
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None
    descriptiveText: Optional[str] = None
    defaultChecked: Optional[bool] = None
    defaultCountryCode: Optional[str] = None
    valueMappings: Optional[ValueMappingsPaginator] = None
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    step: Optional[float] = None
    value: Optional[str] = None
    isArray: Optional[bool] = None
    fileUploaderConfig: Optional[FileUploaderFieldConfigOutput] = None

ValueMappingUnion = Union[ValueMapping, ValueMappingOutput]


class ComponentBindingPropertiesValue(BaseValidatorModel):
    type: Optional[str] = None
    bindingProperties: Optional[ComponentBindingPropertiesValuePropertiesUnion] = None
    defaultValue: Optional[str] = None


class CreateThemeData(BaseValidatorModel):
    name: str
    values: List[ThemeValuesUnion]
    overrides: Optional[List[ThemeValues]] = None
    tags: Optional[Dict[str, str]] = None


class UpdateThemeData(BaseValidatorModel):
    values: List[ThemeValuesUnion]
    id: Optional[str] = None
    name: Optional[str] = None
    overrides: Optional[List[ThemeValues]] = None


class CodegenJobRenderConfig(BaseValidatorModel):
    react: Optional[ReactStartCodegenJobDataUnion] = None


# This class is the output for the 'get_codegen_job' function.
class GetCodegenJobResponse(BaseValidatorModel):
    job: CodegenJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_codegen_job' function.
class StartCodegenJobResponse(BaseValidatorModel):
    entity: CodegenJob
    ResponseMetadata: ResponseMetadata

CodegenGenericDataNonModelUnion = Union[CodegenGenericDataNonModel, CodegenGenericDataNonModelOutput]

MutationActionSetStateParameterUnion = Union[MutationActionSetStateParameter, MutationActionSetStateParameterOutput]


class ComponentChildOutput(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, ComponentPropertyOutput]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventOutput]] = None
    sourceId: Optional[str] = None


class ComponentChildPaginator(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, ComponentPropertyPaginator]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventPaginator]] = None
    sourceId: Optional[str] = None


class FieldConfigOutput(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPosition] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigOutput] = None
    validations: Optional[List[FieldValidationConfigurationOutput]] = None


class FieldConfigPaginator(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPosition] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigPaginator] = None
    validations: Optional[List[FieldValidationConfigurationOutput]] = None


class ValueMappings(BaseValidatorModel):
    values: List[ValueMappingUnion]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValue]] = None

ComponentBindingPropertiesValueUnion = Union[ComponentBindingPropertiesValue, ComponentBindingPropertiesValueOutput]


# This class is the input for the 'create_theme' function.
class CreateThemeRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    themeToCreate: CreateThemeData
    clientToken: Optional[str] = None


# This class is the input for the 'update_theme' function.
class UpdateThemeRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    updatedTheme: UpdateThemeData
    clientToken: Optional[str] = None

CodegenJobRenderConfigUnion = Union[CodegenJobRenderConfig, CodegenJobRenderConfigOutput]


class CodegenJobGenericDataSchema(BaseValidatorModel):
    dataSourceType: Literal['DataStore']
    models: Dict[str, CodegenGenericDataModelUnion]
    enums: Dict[str, CodegenGenericDataEnumUnion]
    nonModels: Dict[str, CodegenGenericDataNonModelUnion]


class ActionParameters(BaseValidatorModel):
    type: Optional[ComponentPropertyUnion] = None
    url: Optional[ComponentPropertyUnion] = None
    anchor: Optional[ComponentPropertyUnion] = None
    target: Optional[ComponentPropertyUnion] = None
    global_: Optional[ComponentPropertyUnion] = None
    model: Optional[str] = None
    id: Optional[ComponentPropertyUnion] = None
    fields: Optional[Dict[str, ComponentProperty]] = None
    state: Optional[MutationActionSetStateParameterUnion] = None


class Component(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    componentType: str
    properties: Dict[str, ComponentPropertyOutput]
    variants: List[ComponentVariantOutput]
    overrides: Dict[str, Dict[str, str]]
    bindingProperties: Dict[str, ComponentBindingPropertiesValueOutput]
    createdAt: datetime
    sourceId: Optional[str] = None
    children: Optional[List[ComponentChildOutput]] = None
    collectionProperties: Optional[Dict[str, ComponentDataConfigurationOutput]] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    events: Optional[Dict[str, ComponentEventOutput]] = None
    schemaVersion: Optional[str] = None


class ComponentPaginator(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    componentType: str
    properties: Dict[str, ComponentPropertyPaginator]
    variants: List[ComponentVariantOutput]
    overrides: Dict[str, Dict[str, str]]
    bindingProperties: Dict[str, ComponentBindingPropertiesValuePaginator]
    createdAt: datetime
    sourceId: Optional[str] = None
    children: Optional[List[ComponentChildPaginator]] = None
    collectionProperties: Optional[Dict[str, ComponentDataConfigurationPaginator]] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    events: Optional[Dict[str, ComponentEventPaginator]] = None
    schemaVersion: Optional[str] = None


class Form(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    formActionType: FormActionTypeType
    style: FormStyle
    dataType: FormDataTypeConfig
    fields: Dict[str, FieldConfigOutput]
    sectionalElements: Dict[str, SectionalElement]
    schemaVersion: str
    tags: Optional[Dict[str, str]] = None
    cta: Optional[FormCTA] = None
    labelDecorator: Optional[LabelDecoratorType] = None


class FormPaginator(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    formActionType: FormActionTypeType
    style: FormStyle
    dataType: FormDataTypeConfig
    fields: Dict[str, FieldConfigPaginator]
    sectionalElements: Dict[str, SectionalElement]
    schemaVersion: str
    tags: Optional[Dict[str, str]] = None
    cta: Optional[FormCTA] = None
    labelDecorator: Optional[LabelDecoratorType] = None

ValueMappingsUnion = Union[ValueMappings, ValueMappingsOutput]

CodegenJobGenericDataSchemaUnion = Union[CodegenJobGenericDataSchema, CodegenJobGenericDataSchemaOutput]

ActionParametersUnion = Union[ActionParameters, ActionParametersOutput]


# This class is the output for the 'create_component' function.
class CreateComponentResponse(BaseValidatorModel):
    entity: Component
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_components' function.
class ExportComponentsResponse(BaseValidatorModel):
    entities: List[Component]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_component' function.
class GetComponentResponse(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_component' function.
class UpdateComponentResponse(BaseValidatorModel):
    entity: Component
    ResponseMetadata: ResponseMetadata


class ExportComponentsResponsePaginator(BaseValidatorModel):
    entities: List[ComponentPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_form' function.
class CreateFormResponse(BaseValidatorModel):
    entity: Form
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_forms' function.
class ExportFormsResponse(BaseValidatorModel):
    entities: List[Form]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_form' function.
class GetFormResponse(BaseValidatorModel):
    form: Form
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_form' function.
class UpdateFormResponse(BaseValidatorModel):
    entity: Form
    ResponseMetadata: ResponseMetadata


class ExportFormsResponsePaginator(BaseValidatorModel):
    entities: List[FormPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FieldInputConfig(BaseValidatorModel):
    type: str
    required: Optional[bool] = None
    readOnly: Optional[bool] = None
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None
    descriptiveText: Optional[str] = None
    defaultChecked: Optional[bool] = None
    defaultCountryCode: Optional[str] = None
    valueMappings: Optional[ValueMappingsUnion] = None
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    step: Optional[float] = None
    value: Optional[str] = None
    isArray: Optional[bool] = None
    fileUploaderConfig: Optional[FileUploaderFieldConfigUnion] = None


class StartCodegenJobData(BaseValidatorModel):
    renderConfig: CodegenJobRenderConfigUnion
    genericDataSchema: Optional[CodegenJobGenericDataSchemaUnion] = None
    autoGenerateForms: Optional[bool] = None
    features: Optional[CodegenFeatureFlags] = None
    tags: Optional[Dict[str, str]] = None


class ComponentEvent(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersUnion] = None
    bindingEvent: Optional[str] = None

FieldInputConfigUnion = Union[FieldInputConfig, FieldInputConfigOutput]


# This class is the input for the 'start_codegen_job' function.
class StartCodegenJobRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    codegenJobToCreate: StartCodegenJobData
    clientToken: Optional[str] = None


class ComponentChild(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, ComponentProperty]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEvent]] = None
    sourceId: Optional[str] = None

ComponentEventUnion = Union[ComponentEvent, ComponentEventOutput]


class FieldConfig(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPosition] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigUnion] = None
    validations: Optional[List[FieldValidationConfigurationUnion]] = None

ComponentChildUnion = Union[ComponentChild, ComponentChildOutput]

FieldConfigUnion = Union[FieldConfig, FieldConfigOutput]


class CreateComponentData(BaseValidatorModel):
    name: str
    componentType: str
    properties: Dict[str, ComponentPropertyUnion]
    variants: List[ComponentVariantUnion]
    overrides: Dict[str, Dict[str, str]]
    bindingProperties: Dict[str, ComponentBindingPropertiesValueUnion]
    sourceId: Optional[str] = None
    children: Optional[List[ComponentChildUnion]] = None
    collectionProperties: Optional[Dict[str, ComponentDataConfigurationUnion]] = None
    tags: Optional[Dict[str, str]] = None
    events: Optional[Dict[str, ComponentEventUnion]] = None
    schemaVersion: Optional[str] = None


class UpdateComponentData(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    sourceId: Optional[str] = None
    componentType: Optional[str] = None
    properties: Optional[Dict[str, ComponentPropertyUnion]] = None
    children: Optional[List[ComponentChildUnion]] = None
    variants: Optional[List[ComponentVariantUnion]] = None
    overrides: Optional[Dict[str, Dict[str, str]]] = None
    bindingProperties: Optional[Dict[str, ComponentBindingPropertiesValueUnion]] = None
    collectionProperties: Optional[Dict[str, ComponentDataConfigurationUnion]] = None
    events: Optional[Dict[str, ComponentEventUnion]] = None
    schemaVersion: Optional[str] = None


class CreateFormData(BaseValidatorModel):
    name: str
    dataType: FormDataTypeConfig
    formActionType: FormActionTypeType
    fields: Dict[str, FieldConfigUnion]
    style: FormStyle
    sectionalElements: Dict[str, SectionalElement]
    schemaVersion: str
    cta: Optional[FormCTA] = None
    tags: Optional[Dict[str, str]] = None
    labelDecorator: Optional[LabelDecoratorType] = None


class UpdateFormData(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[FormDataTypeConfig] = None
    formActionType: Optional[FormActionTypeType] = None
    fields: Optional[Dict[str, FieldConfigUnion]] = None
    style: Optional[FormStyle] = None
    sectionalElements: Optional[Dict[str, SectionalElement]] = None
    schemaVersion: Optional[str] = None
    cta: Optional[FormCTA] = None
    labelDecorator: Optional[LabelDecoratorType] = None


# This class is the input for the 'create_component' function.
class CreateComponentRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    componentToCreate: CreateComponentData
    clientToken: Optional[str] = None


# This class is the input for the 'update_component' function.
class UpdateComponentRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    updatedComponent: UpdateComponentData
    clientToken: Optional[str] = None


# This class is the input for the 'create_form' function.
class CreateFormRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    formToCreate: CreateFormData
    clientToken: Optional[str] = None


# This class is the input for the 'update_form' function.
class UpdateFormRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    updatedForm: UpdateFormData
    clientToken: Optional[str] = None