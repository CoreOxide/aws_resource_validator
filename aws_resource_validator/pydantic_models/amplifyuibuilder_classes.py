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
from aws_resource_validator.pydantic_models.amplifyuibuilder_constants import *

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
    values: Sequence[str]


class CodegenJobAsset(BaseValidatorModel):
    downloadUrl: Optional[str] = None


class SortProperty(BaseValidatorModel):
    field: str
    direction: SortDirectionType


class ComponentVariantOutput(BaseValidatorModel):
    variantValues: Optional[Dict[str, str]] = None
    overrides: Optional[Dict[str, Dict[str, str]]] = None


class ComponentVariant(BaseValidatorModel):
    variantValues: Optional[Mapping[str, str]] = None
    overrides: Optional[Mapping[str, Mapping[str, str]]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FormDataTypeConfig(BaseValidatorModel):
    dataSourceType: FormDataSourceTypeType
    dataTypeName: str


class ExchangeCodeForTokenRequestBody(BaseValidatorModel):
    code: str
    redirectUri: str
    clientId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ExportComponentsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


class ExportFormsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


class ExportThemesRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


class FieldPosition(BaseValidatorModel):
    fixed: Optional[Literal["first"]] = None
    rightOf: Optional[str] = None
    below: Optional[str] = None


class FileUploaderFieldConfigOutput(BaseValidatorModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: List[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None


class FileUploaderFieldConfig(BaseValidatorModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: Sequence[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None


class FormInputBindingPropertiesValueProperties(BaseValidatorModel):
    model: Optional[str] = None


class FormStyleConfig(BaseValidatorModel):
    tokenReference: Optional[str] = None
    value: Optional[str] = None


class GetMetadataRequest(BaseValidatorModel):
    appId: str
    environmentName: str


class ListCodegenJobsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListComponentsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFormsRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListThemesRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PutMetadataFlagBody(BaseValidatorModel):
    newValue: str


class RefreshTokenRequestBody(BaseValidatorModel):
    token: str
    clientId: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class ThemeValueOutput(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List[Dict[str, Any]]] = None


class ThemeValuePaginator(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List[Dict[str, Any]]] = None


class ThemeValue(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[Sequence[Mapping[str, Any]]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ApiConfigurationOutput(BaseValidatorModel):
    graphQLConfig: Optional[GraphQLRenderConfig] = None
    dataStoreConfig: Optional[Dict[str, Any]] = None
    noApiConfig: Optional[Dict[str, Any]] = None


class ApiConfiguration(BaseValidatorModel):
    graphQLConfig: Optional[GraphQLRenderConfig] = None
    dataStoreConfig: Optional[Mapping[str, Any]] = None
    noApiConfig: Optional[Mapping[str, Any]] = None


class CodegenGenericDataRelationshipTypeOutput(BaseValidatorModel):
    pass


class CodegenGenericDataFieldOutput(BaseValidatorModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeOutput] = None


class PredicateOutput(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValuePropertiesOutput(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List[PredicateOutput]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


class PredicatePaginator(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValuePropertiesPaginator(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List[PredicatePaginator]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


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


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ExchangeCodeForTokenResponse(BaseValidatorModel):
    accessToken: str
    expiresIn: int
    refreshToken: str
    ResponseMetadata: ResponseMetadata


class GetMetadataResponse(BaseValidatorModel):
    features: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CodegenJobSummary(BaseValidatorModel):
    pass


class ListCodegenJobsResponse(BaseValidatorModel):
    entities: List[CodegenJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ComponentSummary(BaseValidatorModel):
    pass


class ListComponentsResponse(BaseValidatorModel):
    entities: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RefreshTokenResponse(BaseValidatorModel):
    accessToken: str
    expiresIn: int
    ResponseMetadata: ResponseMetadata


class ExchangeCodeForTokenRequest(BaseValidatorModel):
    provider: Literal["figma"]
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


class FormInputValuePropertyBindingProperties(BaseValidatorModel):
    pass


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
    concat: Optional[Sequence[Mapping[str, Any]]] = None


class FormStyle(BaseValidatorModel):
    horizontalGap: Optional[FormStyleConfig] = None
    verticalGap: Optional[FormStyleConfig] = None
    outerPadding: Optional[FormStyleConfig] = None


class ThemeSummary(BaseValidatorModel):
    pass


class ListThemesResponse(BaseValidatorModel):
    entities: List[ThemeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutMetadataFlagRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    featureName: str
    body: PutMetadataFlagBody


class RefreshTokenRequest(BaseValidatorModel):
    provider: Literal["figma"]
    refreshTokenBody: RefreshTokenRequestBody


class ThemeValuesOutput(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValueOutput] = None


class ThemeValuesPaginator(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValuePaginator] = None


class ReactStartCodegenJobDataOutput(BaseValidatorModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationOutput] = None
    dependencies: Optional[Dict[str, str]] = None


class CodegenGenericDataModelOutput(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldOutput]
    primaryKeys: List[str]
    isJoinTable: Optional[bool] = None


class CodegenGenericDataNonModelOutput(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldOutput]


class CodegenGenericDataRelationshipTypeUnion(BaseValidatorModel):
    pass


class CodegenGenericDataField(BaseValidatorModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeUnion] = None


class FormSummary(BaseValidatorModel):
    pass


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


class PredicateUnion(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValueProperties(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[Sequence[PredicateUnion]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


class ComponentDataConfiguration(BaseValidatorModel):
    model: str
    sort: Optional[Sequence[SortProperty]] = None
    predicate: Optional[PredicateUnion] = None
    identifiers: Optional[Sequence[str]] = None


class ThemeValueUnion(BaseValidatorModel):
    pass


class ThemeValues(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValueUnion] = None


class CodegenJobRenderConfigOutput(BaseValidatorModel):
    react: Optional[ReactStartCodegenJobDataOutput] = None


class ApiConfigurationUnion(BaseValidatorModel):
    pass


class ReactStartCodegenJobData(BaseValidatorModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationUnion] = None
    dependencies: Optional[Mapping[str, str]] = None


class CodegenJobGenericDataSchemaOutput(BaseValidatorModel):
    dataSourceType: Literal["DataStore"]
    models: Dict[str, CodegenGenericDataModelOutput]
    enums: Dict[str, CodegenGenericDataEnumOutput]
    nonModels: Dict[str, CodegenGenericDataNonModelOutput]


class CodegenGenericDataModel(BaseValidatorModel):
    fields: Mapping[str, CodegenGenericDataField]
    primaryKeys: Sequence[str]
    isJoinTable: Optional[bool] = None


class FormInputBindingPropertiesValue(BaseValidatorModel):
    pass


class ValueMappingsOutput(BaseValidatorModel):
    values: List[ValueMappingOutput]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValue]] = None


class ValueMappingsPaginator(BaseValidatorModel):
    values: List[ValueMappingPaginator]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValue]] = None


class FormInputValuePropertyUnion(BaseValidatorModel):
    pass


class ValueMapping(BaseValidatorModel):
    value: FormInputValuePropertyUnion
    displayValue: Optional[FormInputValuePropertyUnion] = None


class Theme(BaseValidatorModel):
    pass


class CreateThemeResponse(BaseValidatorModel):
    entity: Theme
    ResponseMetadata: ResponseMetadata


class ExportThemesResponse(BaseValidatorModel):
    entities: List[Theme]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetThemeResponse(BaseValidatorModel):
    theme: Theme
    ResponseMetadata: ResponseMetadata


class UpdateThemeResponse(BaseValidatorModel):
    entity: Theme
    ResponseMetadata: ResponseMetadata


class ThemePaginator(BaseValidatorModel):
    pass


class ExportThemesResponsePaginator(BaseValidatorModel):
    entities: List[ThemePaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CodegenGenericDataFieldUnion(BaseValidatorModel):
    pass


class CodegenGenericDataNonModel(BaseValidatorModel):
    fields: Mapping[str, CodegenGenericDataFieldUnion]


class ActionParametersOutput(BaseValidatorModel):
    pass


class ComponentEventOutput(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersOutput] = None
    bindingEvent: Optional[str] = None


class ActionParametersPaginator(BaseValidatorModel):
    pass


class ComponentEventPaginator(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersPaginator] = None
    bindingEvent: Optional[str] = None


class ThemeValuesUnion(BaseValidatorModel):
    pass


class CreateThemeData(BaseValidatorModel):
    name: str
    values: Sequence[ThemeValuesUnion]
    overrides: Optional[Sequence[ThemeValues]] = None
    tags: Optional[Mapping[str, str]] = None


class ReactStartCodegenJobDataUnion(BaseValidatorModel):
    pass


class CodegenJobRenderConfig(BaseValidatorModel):
    react: Optional[ReactStartCodegenJobDataUnion] = None


class CodegenJob(BaseValidatorModel):
    pass


class GetCodegenJobResponse(BaseValidatorModel):
    job: CodegenJob
    ResponseMetadata: ResponseMetadata


class StartCodegenJobResponse(BaseValidatorModel):
    entity: CodegenJob
    ResponseMetadata: ResponseMetadata


class ComponentPropertyOutput(BaseValidatorModel):
    pass


class ComponentChildOutput(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, ComponentPropertyOutput]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventOutput]] = None
    sourceId: Optional[str] = None


class ComponentPropertyPaginator(BaseValidatorModel):
    pass


class ComponentChildPaginator(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, ComponentPropertyPaginator]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventPaginator]] = None
    sourceId: Optional[str] = None


class FieldInputConfigOutput(BaseValidatorModel):
    pass


class FieldValidationConfigurationOutput(BaseValidatorModel):
    pass


class FieldConfigOutput(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPosition] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigOutput] = None
    validations: Optional[List[FieldValidationConfigurationOutput]] = None


class FieldInputConfigPaginator(BaseValidatorModel):
    pass


class FieldConfigPaginator(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPosition] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigPaginator] = None
    validations: Optional[List[FieldValidationConfigurationOutput]] = None


class ValueMappingUnion(BaseValidatorModel):
    pass


class ValueMappings(BaseValidatorModel):
    values: Sequence[ValueMappingUnion]
    bindingProperties: Optional[Mapping[str, FormInputBindingPropertiesValue]] = None


class CreateThemeRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    themeToCreate: CreateThemeData
    clientToken: Optional[str] = None


class CodegenGenericDataModelUnion(BaseValidatorModel):
    pass


class CodegenGenericDataEnumUnion(BaseValidatorModel):
    pass


class CodegenGenericDataNonModelUnion(BaseValidatorModel):
    pass


class CodegenJobGenericDataSchema(BaseValidatorModel):
    dataSourceType: Literal["DataStore"]
    models: Mapping[str, CodegenGenericDataModelUnion]
    enums: Mapping[str, CodegenGenericDataEnumUnion]
    nonModels: Mapping[str, CodegenGenericDataNonModelUnion]


class Component(BaseValidatorModel):
    pass


class CreateComponentResponse(BaseValidatorModel):
    entity: Component
    ResponseMetadata: ResponseMetadata


class ExportComponentsResponse(BaseValidatorModel):
    entities: List[Component]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetComponentResponse(BaseValidatorModel):
    component: Component
    ResponseMetadata: ResponseMetadata


class UpdateComponentResponse(BaseValidatorModel):
    entity: Component
    ResponseMetadata: ResponseMetadata


class ComponentPaginator(BaseValidatorModel):
    pass


class ExportComponentsResponsePaginator(BaseValidatorModel):
    entities: List[ComponentPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Form(BaseValidatorModel):
    pass


class CreateFormResponse(BaseValidatorModel):
    entity: Form
    ResponseMetadata: ResponseMetadata


class ExportFormsResponse(BaseValidatorModel):
    entities: List[Form]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetFormResponse(BaseValidatorModel):
    form: Form
    ResponseMetadata: ResponseMetadata


class UpdateFormResponse(BaseValidatorModel):
    entity: Form
    ResponseMetadata: ResponseMetadata


class FormPaginator(BaseValidatorModel):
    pass


class ExportFormsResponsePaginator(BaseValidatorModel):
    entities: List[FormPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CodegenJobGenericDataSchemaUnion(BaseValidatorModel):
    pass


class CodegenJobRenderConfigUnion(BaseValidatorModel):
    pass


class StartCodegenJobData(BaseValidatorModel):
    renderConfig: CodegenJobRenderConfigUnion
    genericDataSchema: Optional[CodegenJobGenericDataSchemaUnion] = None
    autoGenerateForms: Optional[bool] = None
    features: Optional[CodegenFeatureFlags] = None
    tags: Optional[Mapping[str, str]] = None


class ActionParametersUnion(BaseValidatorModel):
    pass


class ComponentEvent(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersUnion] = None
    bindingEvent: Optional[str] = None


class StartCodegenJobRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    codegenJobToCreate: StartCodegenJobData
    clientToken: Optional[str] = None


class ComponentProperty(BaseValidatorModel):
    pass


class ComponentChild(BaseValidatorModel):
    componentType: str
    name: str
    properties: Mapping[str, ComponentProperty]
    children: Optional[Sequence[Mapping[str, Any]]] = None
    events: Optional[Mapping[str, ComponentEvent]] = None
    sourceId: Optional[str] = None


class FieldInputConfigUnion(BaseValidatorModel):
    pass


class FieldValidationConfigurationUnion(BaseValidatorModel):
    pass


class FieldConfig(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPosition] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigUnion] = None
    validations: Optional[Sequence[FieldValidationConfigurationUnion]] = None


class ComponentEventUnion(BaseValidatorModel):
    pass


class ComponentVariantUnion(BaseValidatorModel):
    pass


class ComponentPropertyUnion(BaseValidatorModel):
    pass


class ComponentDataConfigurationUnion(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValueUnion(BaseValidatorModel):
    pass


class ComponentChildUnion(BaseValidatorModel):
    pass


class CreateComponentData(BaseValidatorModel):
    name: str
    componentType: str
    properties: Mapping[str, ComponentPropertyUnion]
    variants: Sequence[ComponentVariantUnion]
    overrides: Mapping[str, Mapping[str, str]]
    bindingProperties: Mapping[str, ComponentBindingPropertiesValueUnion]
    sourceId: Optional[str] = None
    children: Optional[Sequence[ComponentChildUnion]] = None
    collectionProperties: Optional[Mapping[str, ComponentDataConfigurationUnion]] = None
    tags: Optional[Mapping[str, str]] = None
    events: Optional[Mapping[str, ComponentEventUnion]] = None
    schemaVersion: Optional[str] = None


class FieldConfigUnion(BaseValidatorModel):
    pass


class SectionalElement(BaseValidatorModel):
    pass


class CreateFormData(BaseValidatorModel):
    name: str
    dataType: FormDataTypeConfig
    formActionType: FormActionTypeType
    fields: Mapping[str, FieldConfigUnion]
    style: FormStyle
    sectionalElements: Mapping[str, SectionalElement]
    schemaVersion: str
    cta: Optional[FormCTA] = None
    tags: Optional[Mapping[str, str]] = None
    labelDecorator: Optional[LabelDecoratorType] = None


class UpdateFormData(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[FormDataTypeConfig] = None
    formActionType: Optional[FormActionTypeType] = None
    fields: Optional[Mapping[str, FieldConfigUnion]] = None
    style: Optional[FormStyle] = None
    sectionalElements: Optional[Mapping[str, SectionalElement]] = None
    schemaVersion: Optional[str] = None
    cta: Optional[FormCTA] = None
    labelDecorator: Optional[LabelDecoratorType] = None


class CreateComponentRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    componentToCreate: CreateComponentData
    clientToken: Optional[str] = None


class CreateFormRequest(BaseValidatorModel):
    appId: str
    environmentName: str
    formToCreate: CreateFormData
    clientToken: Optional[str] = None


