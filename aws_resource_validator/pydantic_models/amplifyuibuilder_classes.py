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

class GraphQLRenderConfigTypeDef(BaseValidatorModel):
    typesFilePath: str
    queriesFilePath: str
    mutationsFilePath: str
    subscriptionsFilePath: str
    fragmentsFilePath: str


class CodegenDependencyTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    supportedVersion: Optional[str] = None
    isSemVer: Optional[bool] = None
    reason: Optional[str] = None


class CodegenFeatureFlagsTypeDef(BaseValidatorModel):
    isRelationshipSupported: Optional[bool] = None
    isNonModelSupported: Optional[bool] = None


class CodegenGenericDataEnumOutputTypeDef(BaseValidatorModel):
    values: List[str]


class CodegenGenericDataEnumTypeDef(BaseValidatorModel):
    values: Sequence[str]


class CodegenJobAssetTypeDef(BaseValidatorModel):
    downloadUrl: Optional[str] = None


class SortPropertyTypeDef(BaseValidatorModel):
    field: str
    direction: SortDirectionType


class ComponentVariantOutputTypeDef(BaseValidatorModel):
    variantValues: Optional[Dict[str, str]] = None
    overrides: Optional[Dict[str, Dict[str, str]]] = None


class ComponentVariantTypeDef(BaseValidatorModel):
    variantValues: Optional[Mapping[str, str]] = None
    overrides: Optional[Mapping[str, Mapping[str, str]]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FormDataTypeConfigTypeDef(BaseValidatorModel):
    dataSourceType: FormDataSourceTypeType
    dataTypeName: str


class ExchangeCodeForTokenRequestBodyTypeDef(BaseValidatorModel):
    code: str
    redirectUri: str
    clientId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ExportComponentsRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


class ExportFormsRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


class ExportThemesRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None


class FieldPositionTypeDef(BaseValidatorModel):
    fixed: Optional[Literal["first"]] = None
    rightOf: Optional[str] = None
    below: Optional[str] = None


class FileUploaderFieldConfigOutputTypeDef(BaseValidatorModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: List[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None


class FileUploaderFieldConfigTypeDef(BaseValidatorModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: Sequence[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None


class FormInputBindingPropertiesValuePropertiesTypeDef(BaseValidatorModel):
    model: Optional[str] = None


class FormStyleConfigTypeDef(BaseValidatorModel):
    tokenReference: Optional[str] = None
    value: Optional[str] = None


class GetMetadataRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str


class ListCodegenJobsRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListComponentsRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFormsRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListThemesRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PutMetadataFlagBodyTypeDef(BaseValidatorModel):
    newValue: str


class RefreshTokenRequestBodyTypeDef(BaseValidatorModel):
    token: str
    clientId: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class ThemeValueOutputTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List[Dict[str, Any]]] = None


class ThemeValuePaginatorTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List[Dict[str, Any]]] = None


class ThemeValueTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[Sequence[Mapping[str, Any]]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ApiConfigurationOutputTypeDef(BaseValidatorModel):
    graphQLConfig: Optional[GraphQLRenderConfigTypeDef] = None
    dataStoreConfig: Optional[Dict[str, Any]] = None
    noApiConfig: Optional[Dict[str, Any]] = None


class ApiConfigurationTypeDef(BaseValidatorModel):
    graphQLConfig: Optional[GraphQLRenderConfigTypeDef] = None
    dataStoreConfig: Optional[Mapping[str, Any]] = None
    noApiConfig: Optional[Mapping[str, Any]] = None


class CodegenGenericDataRelationshipTypeOutputTypeDef(BaseValidatorModel):
    pass


class CodegenGenericDataFieldOutputTypeDef(BaseValidatorModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeOutputTypeDef] = None


class PredicateOutputTypeDef(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValuePropertiesOutputTypeDef(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List[PredicateOutputTypeDef]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


class PredicatePaginatorTypeDef(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValuePropertiesPaginatorTypeDef(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List[PredicatePaginatorTypeDef]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


class ComponentDataConfigurationOutputTypeDef(BaseValidatorModel):
    model: str
    sort: Optional[List[SortPropertyTypeDef]] = None
    predicate: Optional[PredicateOutputTypeDef] = None
    identifiers: Optional[List[str]] = None


class ComponentDataConfigurationPaginatorTypeDef(BaseValidatorModel):
    model: str
    sort: Optional[List[SortPropertyTypeDef]] = None
    predicate: Optional[PredicatePaginatorTypeDef] = None
    identifiers: Optional[List[str]] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ExchangeCodeForTokenResponseTypeDef(BaseValidatorModel):
    accessToken: str
    expiresIn: int
    refreshToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMetadataResponseTypeDef(BaseValidatorModel):
    features: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CodegenJobSummaryTypeDef(BaseValidatorModel):
    pass


class ListCodegenJobsResponseTypeDef(BaseValidatorModel):
    entities: List[CodegenJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ComponentSummaryTypeDef(BaseValidatorModel):
    pass


class ListComponentsResponseTypeDef(BaseValidatorModel):
    entities: List[ComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class RefreshTokenResponseTypeDef(BaseValidatorModel):
    accessToken: str
    expiresIn: int
    ResponseMetadata: ResponseMetadataTypeDef


class ExchangeCodeForTokenRequestTypeDef(BaseValidatorModel):
    provider: Literal["figma"]
    request: ExchangeCodeForTokenRequestBodyTypeDef


class ExportComponentsRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ExportFormsRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ExportThemesRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCodegenJobsRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComponentsRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFormsRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThemesRequestPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class FormButtonTypeDef(BaseValidatorModel):
    excluded: Optional[bool] = None
    children: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None


class FormInputValuePropertyBindingPropertiesTypeDef(BaseValidatorModel):
    pass


class FormInputValuePropertyOutputTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingPropertiesTypeDef] = None
    concat: Optional[List[Dict[str, Any]]] = None


class FormInputValuePropertyPaginatorTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingPropertiesTypeDef] = None
    concat: Optional[List[Dict[str, Any]]] = None


class FormInputValuePropertyTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingPropertiesTypeDef] = None
    concat: Optional[Sequence[Mapping[str, Any]]] = None


class FormStyleTypeDef(BaseValidatorModel):
    horizontalGap: Optional[FormStyleConfigTypeDef] = None
    verticalGap: Optional[FormStyleConfigTypeDef] = None
    outerPadding: Optional[FormStyleConfigTypeDef] = None


class ThemeSummaryTypeDef(BaseValidatorModel):
    pass


class ListThemesResponseTypeDef(BaseValidatorModel):
    entities: List[ThemeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutMetadataFlagRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    featureName: str
    body: PutMetadataFlagBodyTypeDef


class RefreshTokenRequestTypeDef(BaseValidatorModel):
    provider: Literal["figma"]
    refreshTokenBody: RefreshTokenRequestBodyTypeDef


class ThemeValuesOutputTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValueOutputTypeDef] = None


class ThemeValuesPaginatorTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValuePaginatorTypeDef] = None


class ReactStartCodegenJobDataOutputTypeDef(BaseValidatorModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationOutputTypeDef] = None
    dependencies: Optional[Dict[str, str]] = None


class CodegenGenericDataModelOutputTypeDef(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldOutputTypeDef]
    primaryKeys: List[str]
    isJoinTable: Optional[bool] = None


class CodegenGenericDataNonModelOutputTypeDef(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldOutputTypeDef]


class CodegenGenericDataRelationshipTypeUnionTypeDef(BaseValidatorModel):
    pass


class CodegenGenericDataFieldTypeDef(BaseValidatorModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeUnionTypeDef] = None


class FormSummaryTypeDef(BaseValidatorModel):
    pass


class ListFormsResponseTypeDef(BaseValidatorModel):
    entities: List[FormSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FormCTATypeDef(BaseValidatorModel):
    position: Optional[FormButtonsPositionType] = None
    clear: Optional[FormButtonTypeDef] = None
    cancel: Optional[FormButtonTypeDef] = None
    submit: Optional[FormButtonTypeDef] = None


class ValueMappingOutputTypeDef(BaseValidatorModel):
    value: FormInputValuePropertyOutputTypeDef
    displayValue: Optional[FormInputValuePropertyOutputTypeDef] = None


class ValueMappingPaginatorTypeDef(BaseValidatorModel):
    value: FormInputValuePropertyPaginatorTypeDef
    displayValue: Optional[FormInputValuePropertyPaginatorTypeDef] = None


class PredicateUnionTypeDef(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValuePropertiesTypeDef(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[Sequence[PredicateUnionTypeDef]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None


class ComponentDataConfigurationTypeDef(BaseValidatorModel):
    model: str
    sort: Optional[Sequence[SortPropertyTypeDef]] = None
    predicate: Optional[PredicateUnionTypeDef] = None
    identifiers: Optional[Sequence[str]] = None


class ThemeValueUnionTypeDef(BaseValidatorModel):
    pass


class ThemeValuesTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[ThemeValueUnionTypeDef] = None


class CodegenJobRenderConfigOutputTypeDef(BaseValidatorModel):
    react: Optional[ReactStartCodegenJobDataOutputTypeDef] = None


class ApiConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ReactStartCodegenJobDataTypeDef(BaseValidatorModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationUnionTypeDef] = None
    dependencies: Optional[Mapping[str, str]] = None


class CodegenJobGenericDataSchemaOutputTypeDef(BaseValidatorModel):
    dataSourceType: Literal["DataStore"]
    models: Dict[str, CodegenGenericDataModelOutputTypeDef]
    enums: Dict[str, CodegenGenericDataEnumOutputTypeDef]
    nonModels: Dict[str, CodegenGenericDataNonModelOutputTypeDef]


class CodegenGenericDataModelTypeDef(BaseValidatorModel):
    fields: Mapping[str, CodegenGenericDataFieldTypeDef]
    primaryKeys: Sequence[str]
    isJoinTable: Optional[bool] = None


class FormInputBindingPropertiesValueTypeDef(BaseValidatorModel):
    pass


class ValueMappingsOutputTypeDef(BaseValidatorModel):
    values: List[ValueMappingOutputTypeDef]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValueTypeDef]] = None


class ValueMappingsPaginatorTypeDef(BaseValidatorModel):
    values: List[ValueMappingPaginatorTypeDef]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValueTypeDef]] = None


class FormInputValuePropertyUnionTypeDef(BaseValidatorModel):
    pass


class ValueMappingTypeDef(BaseValidatorModel):
    value: FormInputValuePropertyUnionTypeDef
    displayValue: Optional[FormInputValuePropertyUnionTypeDef] = None


class ThemeTypeDef(BaseValidatorModel):
    pass


class CreateThemeResponseTypeDef(BaseValidatorModel):
    entity: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportThemesResponseTypeDef(BaseValidatorModel):
    entities: List[ThemeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetThemeResponseTypeDef(BaseValidatorModel):
    theme: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateThemeResponseTypeDef(BaseValidatorModel):
    entity: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ThemePaginatorTypeDef(BaseValidatorModel):
    pass


class ExportThemesResponsePaginatorTypeDef(BaseValidatorModel):
    entities: List[ThemePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CodegenGenericDataFieldUnionTypeDef(BaseValidatorModel):
    pass


class CodegenGenericDataNonModelTypeDef(BaseValidatorModel):
    fields: Mapping[str, CodegenGenericDataFieldUnionTypeDef]


class ActionParametersOutputTypeDef(BaseValidatorModel):
    pass


class ComponentEventOutputTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersOutputTypeDef] = None
    bindingEvent: Optional[str] = None


class ActionParametersPaginatorTypeDef(BaseValidatorModel):
    pass


class ComponentEventPaginatorTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersPaginatorTypeDef] = None
    bindingEvent: Optional[str] = None


class ThemeValuesUnionTypeDef(BaseValidatorModel):
    pass


class CreateThemeDataTypeDef(BaseValidatorModel):
    name: str
    values: Sequence[ThemeValuesUnionTypeDef]
    overrides: Optional[Sequence[ThemeValuesTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None


class ReactStartCodegenJobDataUnionTypeDef(BaseValidatorModel):
    pass


class CodegenJobRenderConfigTypeDef(BaseValidatorModel):
    react: Optional[ReactStartCodegenJobDataUnionTypeDef] = None


class CodegenJobTypeDef(BaseValidatorModel):
    pass


class GetCodegenJobResponseTypeDef(BaseValidatorModel):
    job: CodegenJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartCodegenJobResponseTypeDef(BaseValidatorModel):
    entity: CodegenJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ComponentPropertyOutputTypeDef(BaseValidatorModel):
    pass


class ComponentChildOutputTypeDef(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, ComponentPropertyOutputTypeDef]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventOutputTypeDef]] = None
    sourceId: Optional[str] = None


class ComponentPropertyPaginatorTypeDef(BaseValidatorModel):
    pass


class ComponentChildPaginatorTypeDef(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, ComponentPropertyPaginatorTypeDef]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventPaginatorTypeDef]] = None
    sourceId: Optional[str] = None


class FieldInputConfigOutputTypeDef(BaseValidatorModel):
    pass


class FieldValidationConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class FieldConfigOutputTypeDef(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigOutputTypeDef] = None
    validations: Optional[List[FieldValidationConfigurationOutputTypeDef]] = None


class FieldInputConfigPaginatorTypeDef(BaseValidatorModel):
    pass


class FieldConfigPaginatorTypeDef(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigPaginatorTypeDef] = None
    validations: Optional[List[FieldValidationConfigurationOutputTypeDef]] = None


class ValueMappingUnionTypeDef(BaseValidatorModel):
    pass


class ValueMappingsTypeDef(BaseValidatorModel):
    values: Sequence[ValueMappingUnionTypeDef]
    bindingProperties: Optional[Mapping[str, FormInputBindingPropertiesValueTypeDef]] = None


class CreateThemeRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    themeToCreate: CreateThemeDataTypeDef
    clientToken: Optional[str] = None


class CodegenGenericDataModelUnionTypeDef(BaseValidatorModel):
    pass


class CodegenGenericDataEnumUnionTypeDef(BaseValidatorModel):
    pass


class CodegenGenericDataNonModelUnionTypeDef(BaseValidatorModel):
    pass


class CodegenJobGenericDataSchemaTypeDef(BaseValidatorModel):
    dataSourceType: Literal["DataStore"]
    models: Mapping[str, CodegenGenericDataModelUnionTypeDef]
    enums: Mapping[str, CodegenGenericDataEnumUnionTypeDef]
    nonModels: Mapping[str, CodegenGenericDataNonModelUnionTypeDef]


class ComponentTypeDef(BaseValidatorModel):
    pass


class CreateComponentResponseTypeDef(BaseValidatorModel):
    entity: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportComponentsResponseTypeDef(BaseValidatorModel):
    entities: List[ComponentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetComponentResponseTypeDef(BaseValidatorModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateComponentResponseTypeDef(BaseValidatorModel):
    entity: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ComponentPaginatorTypeDef(BaseValidatorModel):
    pass


class ExportComponentsResponsePaginatorTypeDef(BaseValidatorModel):
    entities: List[ComponentPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FormTypeDef(BaseValidatorModel):
    pass


class CreateFormResponseTypeDef(BaseValidatorModel):
    entity: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportFormsResponseTypeDef(BaseValidatorModel):
    entities: List[FormTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetFormResponseTypeDef(BaseValidatorModel):
    form: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFormResponseTypeDef(BaseValidatorModel):
    entity: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FormPaginatorTypeDef(BaseValidatorModel):
    pass


class ExportFormsResponsePaginatorTypeDef(BaseValidatorModel):
    entities: List[FormPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CodegenJobGenericDataSchemaUnionTypeDef(BaseValidatorModel):
    pass


class CodegenJobRenderConfigUnionTypeDef(BaseValidatorModel):
    pass


class StartCodegenJobDataTypeDef(BaseValidatorModel):
    renderConfig: CodegenJobRenderConfigUnionTypeDef
    genericDataSchema: Optional[CodegenJobGenericDataSchemaUnionTypeDef] = None
    autoGenerateForms: Optional[bool] = None
    features: Optional[CodegenFeatureFlagsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class ActionParametersUnionTypeDef(BaseValidatorModel):
    pass


class ComponentEventTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersUnionTypeDef] = None
    bindingEvent: Optional[str] = None


class StartCodegenJobRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    codegenJobToCreate: StartCodegenJobDataTypeDef
    clientToken: Optional[str] = None


class ComponentPropertyTypeDef(BaseValidatorModel):
    pass


class ComponentChildTypeDef(BaseValidatorModel):
    componentType: str
    name: str
    properties: Mapping[str, ComponentPropertyTypeDef]
    children: Optional[Sequence[Mapping[str, Any]]] = None
    events: Optional[Mapping[str, ComponentEventTypeDef]] = None
    sourceId: Optional[str] = None


class FieldInputConfigUnionTypeDef(BaseValidatorModel):
    pass


class FieldValidationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class FieldConfigTypeDef(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigUnionTypeDef] = None
    validations: Optional[Sequence[FieldValidationConfigurationUnionTypeDef]] = None


class ComponentEventUnionTypeDef(BaseValidatorModel):
    pass


class ComponentVariantUnionTypeDef(BaseValidatorModel):
    pass


class ComponentPropertyUnionTypeDef(BaseValidatorModel):
    pass


class ComponentDataConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ComponentBindingPropertiesValueUnionTypeDef(BaseValidatorModel):
    pass


class ComponentChildUnionTypeDef(BaseValidatorModel):
    pass


class CreateComponentDataTypeDef(BaseValidatorModel):
    name: str
    componentType: str
    properties: Mapping[str, ComponentPropertyUnionTypeDef]
    variants: Sequence[ComponentVariantUnionTypeDef]
    overrides: Mapping[str, Mapping[str, str]]
    bindingProperties: Mapping[str, ComponentBindingPropertiesValueUnionTypeDef]
    sourceId: Optional[str] = None
    children: Optional[Sequence[ComponentChildUnionTypeDef]] = None
    collectionProperties: Optional[Mapping[str, ComponentDataConfigurationUnionTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    events: Optional[Mapping[str, ComponentEventUnionTypeDef]] = None
    schemaVersion: Optional[str] = None


class FieldConfigUnionTypeDef(BaseValidatorModel):
    pass


class SectionalElementTypeDef(BaseValidatorModel):
    pass


class CreateFormDataTypeDef(BaseValidatorModel):
    name: str
    dataType: FormDataTypeConfigTypeDef
    formActionType: FormActionTypeType
    fields: Mapping[str, FieldConfigUnionTypeDef]
    style: FormStyleTypeDef
    sectionalElements: Mapping[str, SectionalElementTypeDef]
    schemaVersion: str
    cta: Optional[FormCTATypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    labelDecorator: Optional[LabelDecoratorType] = None


class UpdateFormDataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[FormDataTypeConfigTypeDef] = None
    formActionType: Optional[FormActionTypeType] = None
    fields: Optional[Mapping[str, FieldConfigUnionTypeDef]] = None
    style: Optional[FormStyleTypeDef] = None
    sectionalElements: Optional[Mapping[str, SectionalElementTypeDef]] = None
    schemaVersion: Optional[str] = None
    cta: Optional[FormCTATypeDef] = None
    labelDecorator: Optional[LabelDecoratorType] = None


class CreateComponentRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    componentToCreate: CreateComponentDataTypeDef
    clientToken: Optional[str] = None


class CreateFormRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    formToCreate: CreateFormDataTypeDef
    clientToken: Optional[str] = None


