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
from aws_resource_validator.pydantic_models.amplifyuibuilder_constants import *

class MutationActionSetStateParameterPaginatorTypeDef(BaseModel):
    componentName: str
    property: str
    set: "ComponentPropertyPaginatorTypeDef"

class MutationActionSetStateParameterTypeDef(BaseModel):
    componentName: str
    property: str
    set: "ComponentPropertyTypeDef"

class GraphQLRenderConfigTypeDef(BaseModel):
    typesFilePath: str
    queriesFilePath: str
    mutationsFilePath: str
    subscriptionsFilePath: str
    fragmentsFilePath: str

class CodegenDependencyTypeDef(BaseModel):
    name: Optional[str] = None
    supportedVersion: Optional[str] = None
    isSemVer: Optional[bool] = None
    reason: Optional[str] = None

class CodegenFeatureFlagsTypeDef(BaseModel):
    isRelationshipSupported: Optional[bool] = None
    isNonModelSupported: Optional[bool] = None

class CodegenGenericDataEnumTypeDef(BaseModel):
    values: List[str]

class CodegenGenericDataRelationshipTypeTypeDef(BaseModel):
    type: GenericDataRelationshipTypeType
    relatedModelName: str
    relatedModelFields: Optional[List[str]] = None
    canUnlinkAssociatedModel: Optional[bool] = None
    relatedJoinFieldName: Optional[str] = None
    relatedJoinTableName: Optional[str] = None
    belongsToFieldOnRelatedModel: Optional[str] = None
    associatedFields: Optional[List[str]] = None
    isHasManyIndex: Optional[bool] = None

class CodegenJobAssetTypeDef(BaseModel):
    downloadUrl: Optional[str] = None

class CodegenJobSummaryTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None

class ComponentBindingPropertiesValuePropertiesPaginatorTypeDef(BaseModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List["PredicatePaginatorTypeDef"]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None

class ComponentBindingPropertiesValuePropertiesTypeDef(BaseModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[Sequence["PredicateTypeDef"]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None

class ComponentConditionPropertyTypeDef(BaseModel):
    property: Optional[str] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    then: Optional["ComponentPropertyTypeDef"] = None
    else: Optional["ComponentPropertyTypeDef"] = None
    operandType: Optional[str] = None

class SortPropertyTypeDef(BaseModel):
    field: str
    direction: SortDirectionType

class ComponentVariantPaginatorTypeDef(BaseModel):
    variantValues: Optional[Dict[str, str]] = None
    overrides: Optional[Dict[str, Dict[str, str]]] = None

class ComponentPropertyBindingPropertiesTypeDef(BaseModel):
    property: str
    field: Optional[str] = None

class FormBindingElementTypeDef(BaseModel):
    element: str
    property: str

class ComponentSummaryTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str
    componentType: str

class ComponentVariantTypeDef(BaseModel):
    variantValues: Optional[Mapping[str, str]] = None
    overrides: Optional[Mapping[str, Mapping[str, str]]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class FormDataTypeConfigTypeDef(BaseModel):
    dataSourceType: FormDataSourceTypeType
    dataTypeName: str

class CreateThemeDataTypeDef(BaseModel):
    name: str
    values: Sequence["ThemeValuesTypeDef"]
    overrides: Optional[Sequence["ThemeValuesTypeDef"]] = None
    tags: Optional[Mapping[str, str]] = None

class ThemeTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str
    createdAt: datetime
    values: List["ThemeValuesTypeDef"]
    modifiedAt: Optional[datetime] = None
    overrides: Optional[List["ThemeValuesTypeDef"]] = None
    tags: Optional[Dict[str, str]] = None

class DeleteComponentRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str

class DeleteFormRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str

class DeleteThemeRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str

class ExchangeCodeForTokenRequestBodyTypeDef(BaseModel):
    code: str
    redirectUri: str
    clientId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ExportComponentsRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None

class ExportFormsRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None

class ExportThemesRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None

class ThemePaginatorTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str
    createdAt: datetime
    values: List["ThemeValuesPaginatorTypeDef"]
    modifiedAt: Optional[datetime] = None
    overrides: Optional[List["ThemeValuesPaginatorTypeDef"]] = None
    tags: Optional[Dict[str, str]] = None

class FieldPositionTypeDef(BaseModel):
    fixed: Optional[Literal["first"]] = None
    rightOf: Optional[str] = None
    below: Optional[str] = None

class FieldValidationConfigurationPaginatorTypeDef(BaseModel):
    type: str
    strValues: Optional[List[str]] = None
    numValues: Optional[List[int]] = None
    validationMessage: Optional[str] = None

class FieldValidationConfigurationTypeDef(BaseModel):
    type: str
    strValues: Optional[Sequence[str]] = None
    numValues: Optional[Sequence[int]] = None
    validationMessage: Optional[str] = None

class FileUploaderFieldConfigPaginatorTypeDef(BaseModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: List[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None

class FileUploaderFieldConfigTypeDef(BaseModel):
    accessLevel: StorageAccessLevelType
    acceptedFileTypes: Sequence[str]
    showThumbnails: Optional[bool] = None
    isResumable: Optional[bool] = None
    maxFileCount: Optional[int] = None
    maxSize: Optional[int] = None

class FormInputBindingPropertiesValuePropertiesTypeDef(BaseModel):
    model: Optional[str] = None

class FormInputValuePropertyBindingPropertiesTypeDef(BaseModel):
    property: str
    field: Optional[str] = None

class FormStyleConfigTypeDef(BaseModel):
    tokenReference: Optional[str] = None
    value: Optional[str] = None

class GetCodegenJobRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str

class GetComponentRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str

class GetFormRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str

class GetMetadataRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str

class GetThemeRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str

class ListCodegenJobsRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListComponentsRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFormsRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListThemesRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ThemeSummaryTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str

class PredicatePaginatorTypeDef(BaseModel):
    or: Optional[List[Dict[str, Any]]] = None
    and: Optional[List[Dict[str, Any]]] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    operandType: Optional[str] = None

class PredicateTypeDef(BaseModel):
    or: Optional[Sequence[Dict[str, Any]]] = None
    and: Optional[Sequence[Dict[str, Any]]] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    operandType: Optional[str] = None

class PutMetadataFlagBodyTypeDef(BaseModel):
    newValue: str

class RefreshTokenRequestBodyTypeDef(BaseModel):
    token: str
    clientId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class ThemeValuePaginatorTypeDef(BaseModel):
    value: Optional[str] = None
    children: Optional[List["ThemeValuesPaginatorTypeDef"]] = None

class ThemeValueTypeDef(BaseModel):
    value: Optional[str] = None
    children: Optional[Sequence["ThemeValuesTypeDef"]] = None

class ThemeValuesPaginatorTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[Dict[str, Any]] = None

class ThemeValuesTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[Dict[str, Any]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateThemeDataTypeDef(BaseModel):
    values: Sequence["ThemeValuesTypeDef"]
    id: Optional[str] = None
    name: Optional[str] = None
    overrides: Optional[Sequence["ThemeValuesTypeDef"]] = None

class ValueMappingPaginatorTypeDef(BaseModel):
    value: "FormInputValuePropertyPaginatorTypeDef"
    displayValue: Optional["FormInputValuePropertyPaginatorTypeDef"] = None

class ValueMappingTypeDef(BaseModel):
    value: "FormInputValuePropertyTypeDef"
    displayValue: Optional["FormInputValuePropertyTypeDef"] = None

class ActionParametersPaginatorTypeDef(BaseModel):
    type: Optional["ComponentPropertyPaginatorTypeDef"] = None
    url: Optional["ComponentPropertyPaginatorTypeDef"] = None
    anchor: Optional["ComponentPropertyPaginatorTypeDef"] = None
    target: Optional["ComponentPropertyPaginatorTypeDef"] = None
    global: Optional["ComponentPropertyPaginatorTypeDef"] = None
    model: Optional[str] = None
    id: Optional["ComponentPropertyPaginatorTypeDef"] = None
    fields: Optional[Dict[str, "ComponentPropertyPaginatorTypeDef"]] = None
    state: Optional[MutationActionSetStateParameterPaginatorTypeDef] = None

class ActionParametersTypeDef(BaseModel):
    type: Optional["ComponentPropertyTypeDef"] = None
    url: Optional["ComponentPropertyTypeDef"] = None
    anchor: Optional["ComponentPropertyTypeDef"] = None
    target: Optional["ComponentPropertyTypeDef"] = None
    global: Optional["ComponentPropertyTypeDef"] = None
    model: Optional[str] = None
    id: Optional["ComponentPropertyTypeDef"] = None
    fields: Optional[Mapping[str, "ComponentPropertyTypeDef"]] = None
    state: Optional[MutationActionSetStateParameterTypeDef] = None

class ApiConfigurationTypeDef(BaseModel):
    graphQLConfig: Optional[GraphQLRenderConfigTypeDef] = None
    dataStoreConfig: Optional[Dict[str, Any]] = None
    noApiConfig: Optional[Dict[str, Any]] = None

class CodegenGenericDataFieldTypeDef(BaseModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeTypeDef] = None

class ComponentBindingPropertiesValuePaginatorTypeDef(BaseModel):
    type: Optional[str] = None
    bindingProperties: Optional[ComponentBindingPropertiesValuePropertiesPaginatorTypeDef] = None
    defaultValue: Optional[str] = None

class ComponentBindingPropertiesValueTypeDef(BaseModel):
    type: Optional[str] = None
    bindingProperties: Optional[ComponentBindingPropertiesValuePropertiesTypeDef] = None
    defaultValue: Optional[str] = None

class ComponentDataConfigurationPaginatorTypeDef(BaseModel):
    model: str
    sort: Optional[List[SortPropertyTypeDef]] = None
    predicate: Optional["PredicatePaginatorTypeDef"] = None
    identifiers: Optional[List[str]] = None

class ComponentDataConfigurationTypeDef(BaseModel):
    model: str
    sort: Optional[Sequence[SortPropertyTypeDef]] = None
    predicate: Optional["PredicateTypeDef"] = None
    identifiers: Optional[Sequence[str]] = None

class ComponentPropertyPaginatorTypeDef(BaseModel):
    value: Optional[str] = None
    bindingProperties: Optional[ComponentPropertyBindingPropertiesTypeDef] = None
    collectionBindingProperties: Optional[ComponentPropertyBindingPropertiesTypeDef] = None
    defaultValue: Optional[str] = None
    model: Optional[str] = None
    bindings: Optional[Dict[str, FormBindingElementTypeDef]] = None
    event: Optional[str] = None
    userAttribute: Optional[str] = None
    concat: Optional[List[Dict[str, Any]]] = None
    condition: Optional[ComponentConditionPropertyTypeDef] = None
    configured: Optional[bool] = None
    type: Optional[str] = None
    importedValue: Optional[str] = None
    componentName: Optional[str] = None
    property: Optional[str] = None

class ComponentPropertyTypeDef(BaseModel):
    value: Optional[str] = None
    bindingProperties: Optional[ComponentPropertyBindingPropertiesTypeDef] = None
    collectionBindingProperties: Optional[ComponentPropertyBindingPropertiesTypeDef] = None
    defaultValue: Optional[str] = None
    model: Optional[str] = None
    bindings: Optional[Mapping[str, FormBindingElementTypeDef]] = None
    event: Optional[str] = None
    userAttribute: Optional[str] = None
    concat: Optional[Sequence[Dict[str, Any]]] = None
    condition: Optional[Dict[str, Any]] = None
    configured: Optional[bool] = None
    type: Optional[str] = None
    importedValue: Optional[str] = None
    componentName: Optional[str] = None
    property: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ExchangeCodeForTokenResponseTypeDef(BaseModel):
    accessToken: str
    expiresIn: int
    refreshToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMetadataResponseTypeDef(BaseModel):
    features: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCodegenJobsResponseTypeDef(BaseModel):
    entities: List[CodegenJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentsResponseTypeDef(BaseModel):
    entities: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshTokenResponseTypeDef(BaseModel):
    accessToken: str
    expiresIn: int
    ResponseMetadata: ResponseMetadataTypeDef

class FormSummaryTypeDef(BaseModel):
    appId: str
    dataType: FormDataTypeConfigTypeDef
    environmentName: str
    formActionType: FormActionTypeType
    id: str
    name: str

class CreateThemeRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    themeToCreate: CreateThemeDataTypeDef
    clientToken: Optional[str] = None

class CreateThemeResponseTypeDef(BaseModel):
    entity: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportThemesResponseTypeDef(BaseModel):
    entities: List[ThemeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetThemeResponseTypeDef(BaseModel):
    theme: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThemeResponseTypeDef(BaseModel):
    entity: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExchangeCodeForTokenRequestRequestTypeDef(BaseModel):
    provider: Literal["figma"]
    request: ExchangeCodeForTokenRequestBodyTypeDef

class ExportComponentsRequestExportComponentsPaginateTypeDef(BaseModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ExportFormsRequestExportFormsPaginateTypeDef(BaseModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ExportThemesRequestExportThemesPaginateTypeDef(BaseModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCodegenJobsRequestListCodegenJobsPaginateTypeDef(BaseModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsRequestListComponentsPaginateTypeDef(BaseModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFormsRequestListFormsPaginateTypeDef(BaseModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThemesRequestListThemesPaginateTypeDef(BaseModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ExportThemesResponsePaginatorTypeDef(BaseModel):
    entities: List[ThemePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FormButtonTypeDef(BaseModel):
    excluded: Optional[bool] = None
    children: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None

class SectionalElementTypeDef(BaseModel):
    type: str
    position: Optional[FieldPositionTypeDef] = None
    text: Optional[str] = None
    level: Optional[int] = None
    orientation: Optional[str] = None
    excluded: Optional[bool] = None

class FormInputBindingPropertiesValueTypeDef(BaseModel):
    type: Optional[str] = None
    bindingProperties: Optional[FormInputBindingPropertiesValuePropertiesTypeDef] = None

class FormInputValuePropertyPaginatorTypeDef(BaseModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingPropertiesTypeDef] = None
    concat: Optional[List[Dict[str, Any]]] = None

class FormInputValuePropertyTypeDef(BaseModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingPropertiesTypeDef] = None
    concat: Optional[Sequence[Dict[str, Any]]] = None

class FormStyleTypeDef(BaseModel):
    horizontalGap: Optional[FormStyleConfigTypeDef] = None
    verticalGap: Optional[FormStyleConfigTypeDef] = None
    outerPadding: Optional[FormStyleConfigTypeDef] = None

class ListThemesResponseTypeDef(BaseModel):
    entities: List[ThemeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetadataFlagRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    featureName: str
    body: PutMetadataFlagBodyTypeDef

class RefreshTokenRequestRequestTypeDef(BaseModel):
    provider: Literal["figma"]
    refreshTokenBody: RefreshTokenRequestBodyTypeDef

class UpdateThemeRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    updatedTheme: UpdateThemeDataTypeDef
    clientToken: Optional[str] = None

class ComponentEventPaginatorTypeDef(BaseModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersPaginatorTypeDef] = None
    bindingEvent: Optional[str] = None

class ComponentEventTypeDef(BaseModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersTypeDef] = None
    bindingEvent: Optional[str] = None

class ReactStartCodegenJobDataTypeDef(BaseModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationTypeDef] = None
    dependencies: Optional[Dict[str, str]] = None

class CodegenGenericDataModelTypeDef(BaseModel):
    fields: Dict[str, CodegenGenericDataFieldTypeDef]
    primaryKeys: List[str]
    isJoinTable: Optional[bool] = None

class CodegenGenericDataNonModelTypeDef(BaseModel):
    fields: Dict[str, CodegenGenericDataFieldTypeDef]

class ListFormsResponseTypeDef(BaseModel):
    entities: List[FormSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FormCTATypeDef(BaseModel):
    position: Optional[FormButtonsPositionType] = None
    clear: Optional[FormButtonTypeDef] = None
    cancel: Optional[FormButtonTypeDef] = None
    submit: Optional[FormButtonTypeDef] = None

class ValueMappingsPaginatorTypeDef(BaseModel):
    values: List[ValueMappingPaginatorTypeDef]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValueTypeDef]] = None

class ValueMappingsTypeDef(BaseModel):
    values: Sequence[ValueMappingTypeDef]
    bindingProperties: Optional[Mapping[str, FormInputBindingPropertiesValueTypeDef]] = None

class ComponentChildPaginatorTypeDef(BaseModel):
    componentType: str
    name: str
    properties: Dict[str, "ComponentPropertyPaginatorTypeDef"]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventPaginatorTypeDef]] = None
    sourceId: Optional[str] = None

class ComponentPaginatorTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str
    componentType: str
    properties: Dict[str, "ComponentPropertyPaginatorTypeDef"]
    variants: List[ComponentVariantPaginatorTypeDef]
    overrides: Dict[str, Dict[str, str]]
    bindingProperties: Dict[str, ComponentBindingPropertiesValuePaginatorTypeDef]
    createdAt: datetime
    sourceId: Optional[str] = None
    children: Optional[List["ComponentChildPaginatorTypeDef"]] = None
    collectionProperties: Optional[Dict[str, ComponentDataConfigurationPaginatorTypeDef]] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    events: Optional[Dict[str, ComponentEventPaginatorTypeDef]] = None
    schemaVersion: Optional[str] = None

class ComponentChildTypeDef(BaseModel):
    componentType: str
    name: str
    properties: Mapping[str, "ComponentPropertyTypeDef"]
    children: Optional[Sequence[Dict[str, Any]]] = None
    events: Optional[Mapping[str, ComponentEventTypeDef]] = None
    sourceId: Optional[str] = None

class ComponentTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str
    componentType: str
    properties: Dict[str, "ComponentPropertyTypeDef"]
    variants: List[ComponentVariantTypeDef]
    overrides: Dict[str, Dict[str, str]]
    bindingProperties: Dict[str, ComponentBindingPropertiesValueTypeDef]
    createdAt: datetime
    sourceId: Optional[str] = None
    children: Optional[List["ComponentChildTypeDef"]] = None
    collectionProperties: Optional[Dict[str, ComponentDataConfigurationTypeDef]] = None
    modifiedAt: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    events: Optional[Dict[str, ComponentEventTypeDef]] = None
    schemaVersion: Optional[str] = None

class CreateComponentDataTypeDef(BaseModel):
    name: str
    componentType: str
    properties: Mapping[str, "ComponentPropertyTypeDef"]
    variants: Sequence[ComponentVariantTypeDef]
    overrides: Mapping[str, Mapping[str, str]]
    bindingProperties: Mapping[str, ComponentBindingPropertiesValueTypeDef]
    sourceId: Optional[str] = None
    children: Optional[Sequence["ComponentChildTypeDef"]] = None
    collectionProperties: Optional[Mapping[str, ComponentDataConfigurationTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    events: Optional[Mapping[str, ComponentEventTypeDef]] = None
    schemaVersion: Optional[str] = None

class UpdateComponentDataTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    sourceId: Optional[str] = None
    componentType: Optional[str] = None
    properties: Optional[Mapping[str, "ComponentPropertyTypeDef"]] = None
    children: Optional[Sequence["ComponentChildTypeDef"]] = None
    variants: Optional[Sequence[ComponentVariantTypeDef]] = None
    overrides: Optional[Mapping[str, Mapping[str, str]]] = None
    bindingProperties: Optional[Mapping[str, ComponentBindingPropertiesValueTypeDef]] = None
    collectionProperties: Optional[Mapping[str, ComponentDataConfigurationTypeDef]] = None
    events: Optional[Mapping[str, ComponentEventTypeDef]] = None
    schemaVersion: Optional[str] = None

class CodegenJobRenderConfigTypeDef(BaseModel):
    react: Optional[ReactStartCodegenJobDataTypeDef] = None

class CodegenJobGenericDataSchemaTypeDef(BaseModel):
    dataSourceType: Literal["DataStore"]
    models: Dict[str, CodegenGenericDataModelTypeDef]
    enums: Dict[str, CodegenGenericDataEnumTypeDef]
    nonModels: Dict[str, CodegenGenericDataNonModelTypeDef]

class FieldInputConfigPaginatorTypeDef(BaseModel):
    type: str
    required: Optional[bool] = None
    readOnly: Optional[bool] = None
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None
    descriptiveText: Optional[str] = None
    defaultChecked: Optional[bool] = None
    defaultCountryCode: Optional[str] = None
    valueMappings: Optional[ValueMappingsPaginatorTypeDef] = None
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    step: Optional[float] = None
    value: Optional[str] = None
    isArray: Optional[bool] = None
    fileUploaderConfig: Optional[FileUploaderFieldConfigPaginatorTypeDef] = None

class FieldInputConfigTypeDef(BaseModel):
    type: str
    required: Optional[bool] = None
    readOnly: Optional[bool] = None
    placeholder: Optional[str] = None
    defaultValue: Optional[str] = None
    descriptiveText: Optional[str] = None
    defaultChecked: Optional[bool] = None
    defaultCountryCode: Optional[str] = None
    valueMappings: Optional[ValueMappingsTypeDef] = None
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    step: Optional[float] = None
    value: Optional[str] = None
    isArray: Optional[bool] = None
    fileUploaderConfig: Optional[FileUploaderFieldConfigTypeDef] = None

class ExportComponentsResponsePaginatorTypeDef(BaseModel):
    entities: List[ComponentPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentResponseTypeDef(BaseModel):
    entity: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportComponentsResponseTypeDef(BaseModel):
    entities: List[ComponentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentResponseTypeDef(BaseModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComponentResponseTypeDef(BaseModel):
    entity: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    componentToCreate: CreateComponentDataTypeDef
    clientToken: Optional[str] = None

class UpdateComponentRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    updatedComponent: UpdateComponentDataTypeDef
    clientToken: Optional[str] = None

class CodegenJobTypeDef(BaseModel):
    id: str
    appId: str
    environmentName: str
    renderConfig: Optional[CodegenJobRenderConfigTypeDef] = None
    genericDataSchema: Optional[CodegenJobGenericDataSchemaTypeDef] = None
    autoGenerateForms: Optional[bool] = None
    features: Optional[CodegenFeatureFlagsTypeDef] = None
    status: Optional[CodegenJobStatusType] = None
    statusMessage: Optional[str] = None
    asset: Optional[CodegenJobAssetTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None
    dependencies: Optional[List[CodegenDependencyTypeDef]] = None

class StartCodegenJobDataTypeDef(BaseModel):
    renderConfig: CodegenJobRenderConfigTypeDef
    genericDataSchema: Optional[CodegenJobGenericDataSchemaTypeDef] = None
    autoGenerateForms: Optional[bool] = None
    features: Optional[CodegenFeatureFlagsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class FieldConfigPaginatorTypeDef(BaseModel):
    label: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigPaginatorTypeDef] = None
    validations: Optional[List[FieldValidationConfigurationPaginatorTypeDef]] = None

class FieldConfigTypeDef(BaseModel):
    label: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigTypeDef] = None
    validations: Optional[Sequence[FieldValidationConfigurationTypeDef]] = None

class GetCodegenJobResponseTypeDef(BaseModel):
    job: CodegenJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCodegenJobResponseTypeDef(BaseModel):
    entity: CodegenJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCodegenJobRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    codegenJobToCreate: StartCodegenJobDataTypeDef
    clientToken: Optional[str] = None

class FormPaginatorTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str
    formActionType: FormActionTypeType
    style: FormStyleTypeDef
    dataType: FormDataTypeConfigTypeDef
    fields: Dict[str, FieldConfigPaginatorTypeDef]
    sectionalElements: Dict[str, SectionalElementTypeDef]
    schemaVersion: str
    tags: Optional[Dict[str, str]] = None
    cta: Optional[FormCTATypeDef] = None
    labelDecorator: Optional[LabelDecoratorType] = None

class CreateFormDataTypeDef(BaseModel):
    name: str
    dataType: FormDataTypeConfigTypeDef
    formActionType: FormActionTypeType
    fields: Mapping[str, FieldConfigTypeDef]
    style: FormStyleTypeDef
    sectionalElements: Mapping[str, SectionalElementTypeDef]
    schemaVersion: str
    cta: Optional[FormCTATypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    labelDecorator: Optional[LabelDecoratorType] = None

class FormTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    name: str
    formActionType: FormActionTypeType
    style: FormStyleTypeDef
    dataType: FormDataTypeConfigTypeDef
    fields: Dict[str, FieldConfigTypeDef]
    sectionalElements: Dict[str, SectionalElementTypeDef]
    schemaVersion: str
    tags: Optional[Dict[str, str]] = None
    cta: Optional[FormCTATypeDef] = None
    labelDecorator: Optional[LabelDecoratorType] = None

class UpdateFormDataTypeDef(BaseModel):
    name: Optional[str] = None
    dataType: Optional[FormDataTypeConfigTypeDef] = None
    formActionType: Optional[FormActionTypeType] = None
    fields: Optional[Mapping[str, FieldConfigTypeDef]] = None
    style: Optional[FormStyleTypeDef] = None
    sectionalElements: Optional[Mapping[str, SectionalElementTypeDef]] = None
    schemaVersion: Optional[str] = None
    cta: Optional[FormCTATypeDef] = None
    labelDecorator: Optional[LabelDecoratorType] = None

class ExportFormsResponsePaginatorTypeDef(BaseModel):
    entities: List[FormPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFormRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    formToCreate: CreateFormDataTypeDef
    clientToken: Optional[str] = None

class CreateFormResponseTypeDef(BaseModel):
    entity: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportFormsResponseTypeDef(BaseModel):
    entities: List[FormTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFormResponseTypeDef(BaseModel):
    form: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFormResponseTypeDef(BaseModel):
    entity: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFormRequestRequestTypeDef(BaseModel):
    appId: str
    environmentName: str
    id: str
    updatedForm: UpdateFormDataTypeDef
    clientToken: Optional[str] = None

