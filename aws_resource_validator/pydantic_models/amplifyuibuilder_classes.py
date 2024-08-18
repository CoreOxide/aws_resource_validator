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
from aws_resource_validator.pydantic_models.amplifyuibuilder_constants import *

class MutationActionSetStateParameterPaginatorTypeDef(BaseValidatorModel):
    componentName: str
    property: str
    set: "ComponentPropertyPaginatorTypeDef"

class MutationActionSetStateParameterTypeDef(BaseValidatorModel):
    componentName: str
    property: str
    set: "ComponentPropertyTypeDef"

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

class CodegenGenericDataEnumTypeDef(BaseValidatorModel):
    values: List[str]

class CodegenGenericDataRelationshipTypeTypeDef(BaseValidatorModel):
    type: GenericDataRelationshipTypeType
    relatedModelName: str
    relatedModelFields: Optional[List[str]] = None
    canUnlinkAssociatedModel: Optional[bool] = None
    relatedJoinFieldName: Optional[str] = None
    relatedJoinTableName: Optional[str] = None
    belongsToFieldOnRelatedModel: Optional[str] = None
    associatedFields: Optional[List[str]] = None
    isHasManyIndex: Optional[bool] = None

class CodegenJobAssetTypeDef(BaseValidatorModel):
    downloadUrl: Optional[str] = None

class CodegenJobSummaryTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    createdAt: Optional[datetime] = None
    modifiedAt: Optional[datetime] = None

class ComponentBindingPropertiesValuePropertiesPaginatorTypeDef(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[List["PredicatePaginatorTypeDef"]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None

class ComponentBindingPropertiesValuePropertiesTypeDef(BaseValidatorModel):
    model: Optional[str] = None
    field: Optional[str] = None
    predicates: Optional[Sequence["PredicateTypeDef"]] = None
    userAttribute: Optional[str] = None
    bucket: Optional[str] = None
    key: Optional[str] = None
    defaultValue: Optional[str] = None
    slotName: Optional[str] = None

class ComponentConditionPropertyTypeDef(BaseValidatorModel):
    property: Optional[str] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    then: Optional["ComponentPropertyTypeDef"] = None
    else: Optional["ComponentPropertyTypeDef"] = None
    operandType: Optional[str] = None

class SortPropertyTypeDef(BaseValidatorModel):
    field: str
    direction: SortDirectionType

class ComponentVariantPaginatorTypeDef(BaseValidatorModel):
    variantValues: Optional[Dict[str, str]] = None
    overrides: Optional[Dict[str, Dict[str, str]]] = None

class ComponentPropertyBindingPropertiesTypeDef(BaseValidatorModel):
    property: str
    field: Optional[str] = None

class FormBindingElementTypeDef(BaseValidatorModel):
    element: str
    property: str

class ComponentSummaryTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    componentType: str

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

class CreateThemeDataTypeDef(BaseValidatorModel):
    name: str
    values: Sequence["ThemeValuesTypeDef"]
    overrides: Optional[Sequence["ThemeValuesTypeDef"]] = None
    tags: Optional[Mapping[str, str]] = None

class ThemeTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    createdAt: datetime
    values: List["ThemeValuesTypeDef"]
    modifiedAt: Optional[datetime] = None
    overrides: Optional[List["ThemeValuesTypeDef"]] = None
    tags: Optional[Dict[str, str]] = None

class DeleteComponentRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str

class DeleteFormRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str

class DeleteThemeRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str

class ExchangeCodeForTokenRequestBodyTypeDef(BaseValidatorModel):
    code: str
    redirectUri: str
    clientId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ExportComponentsRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None

class ExportFormsRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None

class ExportThemesRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None

class ThemePaginatorTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str
    createdAt: datetime
    values: List["ThemeValuesPaginatorTypeDef"]
    modifiedAt: Optional[datetime] = None
    overrides: Optional[List["ThemeValuesPaginatorTypeDef"]] = None
    tags: Optional[Dict[str, str]] = None

class FieldPositionTypeDef(BaseValidatorModel):
    fixed: Optional[Literal["first"]] = None
    rightOf: Optional[str] = None
    below: Optional[str] = None

class FieldValidationConfigurationPaginatorTypeDef(BaseValidatorModel):
    type: str
    strValues: Optional[List[str]] = None
    numValues: Optional[List[int]] = None
    validationMessage: Optional[str] = None

class FieldValidationConfigurationTypeDef(BaseValidatorModel):
    type: str
    strValues: Optional[Sequence[str]] = None
    numValues: Optional[Sequence[int]] = None
    validationMessage: Optional[str] = None

class FileUploaderFieldConfigPaginatorTypeDef(BaseValidatorModel):
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

class FormInputValuePropertyBindingPropertiesTypeDef(BaseValidatorModel):
    property: str
    field: Optional[str] = None

class FormStyleConfigTypeDef(BaseValidatorModel):
    tokenReference: Optional[str] = None
    value: Optional[str] = None

class GetCodegenJobRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str

class GetComponentRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str

class GetFormRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str

class GetMetadataRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str

class GetThemeRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str

class ListCodegenJobsRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListComponentsRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFormsRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListThemesRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ThemeSummaryTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    name: str

class PredicatePaginatorTypeDef(BaseValidatorModel):
    or: Optional[List[Dict[str, Any]]] = None
    and: Optional[List[Dict[str, Any]]] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    operandType: Optional[str] = None

class PredicateTypeDef(BaseValidatorModel):
    or: Optional[Sequence[Dict[str, Any]]] = None
    and: Optional[Sequence[Dict[str, Any]]] = None
    field: Optional[str] = None
    operator: Optional[str] = None
    operand: Optional[str] = None
    operandType: Optional[str] = None

class PutMetadataFlagBodyTypeDef(BaseValidatorModel):
    newValue: str

class RefreshTokenRequestBodyTypeDef(BaseValidatorModel):
    token: str
    clientId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class ThemeValuePaginatorTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[List["ThemeValuesPaginatorTypeDef"]] = None

class ThemeValueTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    children: Optional[Sequence["ThemeValuesTypeDef"]] = None

class ThemeValuesPaginatorTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[Dict[str, Any]] = None

class ThemeValuesTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[Dict[str, Any]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateThemeDataTypeDef(BaseValidatorModel):
    values: Sequence["ThemeValuesTypeDef"]
    id: Optional[str] = None
    name: Optional[str] = None
    overrides: Optional[Sequence["ThemeValuesTypeDef"]] = None

class ValueMappingPaginatorTypeDef(BaseValidatorModel):
    value: "FormInputValuePropertyPaginatorTypeDef"
    displayValue: Optional["FormInputValuePropertyPaginatorTypeDef"] = None

class ValueMappingTypeDef(BaseValidatorModel):
    value: "FormInputValuePropertyTypeDef"
    displayValue: Optional["FormInputValuePropertyTypeDef"] = None

class ActionParametersPaginatorTypeDef(BaseValidatorModel):
    type: Optional["ComponentPropertyPaginatorTypeDef"] = None
    url: Optional["ComponentPropertyPaginatorTypeDef"] = None
    anchor: Optional["ComponentPropertyPaginatorTypeDef"] = None
    target: Optional["ComponentPropertyPaginatorTypeDef"] = None
    global: Optional["ComponentPropertyPaginatorTypeDef"] = None
    model: Optional[str] = None
    id: Optional["ComponentPropertyPaginatorTypeDef"] = None
    fields: Optional[Dict[str, "ComponentPropertyPaginatorTypeDef"]] = None
    state: Optional[MutationActionSetStateParameterPaginatorTypeDef] = None

class ActionParametersTypeDef(BaseValidatorModel):
    type: Optional["ComponentPropertyTypeDef"] = None
    url: Optional["ComponentPropertyTypeDef"] = None
    anchor: Optional["ComponentPropertyTypeDef"] = None
    target: Optional["ComponentPropertyTypeDef"] = None
    global: Optional["ComponentPropertyTypeDef"] = None
    model: Optional[str] = None
    id: Optional["ComponentPropertyTypeDef"] = None
    fields: Optional[Mapping[str, "ComponentPropertyTypeDef"]] = None
    state: Optional[MutationActionSetStateParameterTypeDef] = None

class ApiConfigurationTypeDef(BaseValidatorModel):
    graphQLConfig: Optional[GraphQLRenderConfigTypeDef] = None
    dataStoreConfig: Optional[Dict[str, Any]] = None
    noApiConfig: Optional[Dict[str, Any]] = None

class CodegenGenericDataFieldTypeDef(BaseValidatorModel):
    dataType: CodegenGenericDataFieldDataTypeType
    dataTypeValue: str
    required: bool
    readOnly: bool
    isArray: bool
    relationship: Optional[CodegenGenericDataRelationshipTypeTypeDef] = None

class ComponentBindingPropertiesValuePaginatorTypeDef(BaseValidatorModel):
    type: Optional[str] = None
    bindingProperties: Optional[ComponentBindingPropertiesValuePropertiesPaginatorTypeDef] = None
    defaultValue: Optional[str] = None

class ComponentBindingPropertiesValueTypeDef(BaseValidatorModel):
    type: Optional[str] = None
    bindingProperties: Optional[ComponentBindingPropertiesValuePropertiesTypeDef] = None
    defaultValue: Optional[str] = None

class ComponentDataConfigurationPaginatorTypeDef(BaseValidatorModel):
    model: str
    sort: Optional[List[SortPropertyTypeDef]] = None
    predicate: Optional["PredicatePaginatorTypeDef"] = None
    identifiers: Optional[List[str]] = None

class ComponentDataConfigurationTypeDef(BaseValidatorModel):
    model: str
    sort: Optional[Sequence[SortPropertyTypeDef]] = None
    predicate: Optional["PredicateTypeDef"] = None
    identifiers: Optional[Sequence[str]] = None

class ComponentPropertyPaginatorTypeDef(BaseValidatorModel):
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

class ComponentPropertyTypeDef(BaseValidatorModel):
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

class ListCodegenJobsResponseTypeDef(BaseValidatorModel):
    entities: List[CodegenJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListComponentsResponseTypeDef(BaseValidatorModel):
    entities: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshTokenResponseTypeDef(BaseValidatorModel):
    accessToken: str
    expiresIn: int
    ResponseMetadata: ResponseMetadataTypeDef

class FormSummaryTypeDef(BaseValidatorModel):
    appId: str
    dataType: FormDataTypeConfigTypeDef
    environmentName: str
    formActionType: FormActionTypeType
    id: str
    name: str

class CreateThemeRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    themeToCreate: CreateThemeDataTypeDef
    clientToken: Optional[str] = None

class CreateThemeResponseTypeDef(BaseValidatorModel):
    entity: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportThemesResponseTypeDef(BaseValidatorModel):
    entities: List[ThemeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetThemeResponseTypeDef(BaseValidatorModel):
    theme: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThemeResponseTypeDef(BaseValidatorModel):
    entity: ThemeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExchangeCodeForTokenRequestRequestTypeDef(BaseValidatorModel):
    provider: Literal["figma"]
    request: ExchangeCodeForTokenRequestBodyTypeDef

class ExportComponentsRequestExportComponentsPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ExportFormsRequestExportFormsPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ExportThemesRequestExportThemesPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCodegenJobsRequestListCodegenJobsPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsRequestListComponentsPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFormsRequestListFormsPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThemesRequestListThemesPaginateTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ExportThemesResponsePaginatorTypeDef(BaseValidatorModel):
    entities: List[ThemePaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FormButtonTypeDef(BaseValidatorModel):
    excluded: Optional[bool] = None
    children: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None

class SectionalElementTypeDef(BaseValidatorModel):
    type: str
    position: Optional[FieldPositionTypeDef] = None
    text: Optional[str] = None
    level: Optional[int] = None
    orientation: Optional[str] = None
    excluded: Optional[bool] = None

class FormInputBindingPropertiesValueTypeDef(BaseValidatorModel):
    type: Optional[str] = None
    bindingProperties: Optional[FormInputBindingPropertiesValuePropertiesTypeDef] = None

class FormInputValuePropertyPaginatorTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingPropertiesTypeDef] = None
    concat: Optional[List[Dict[str, Any]]] = None

class FormInputValuePropertyTypeDef(BaseValidatorModel):
    value: Optional[str] = None
    bindingProperties: Optional[FormInputValuePropertyBindingPropertiesTypeDef] = None
    concat: Optional[Sequence[Dict[str, Any]]] = None

class FormStyleTypeDef(BaseValidatorModel):
    horizontalGap: Optional[FormStyleConfigTypeDef] = None
    verticalGap: Optional[FormStyleConfigTypeDef] = None
    outerPadding: Optional[FormStyleConfigTypeDef] = None

class ListThemesResponseTypeDef(BaseValidatorModel):
    entities: List[ThemeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutMetadataFlagRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    featureName: str
    body: PutMetadataFlagBodyTypeDef

class RefreshTokenRequestRequestTypeDef(BaseValidatorModel):
    provider: Literal["figma"]
    refreshTokenBody: RefreshTokenRequestBodyTypeDef

class UpdateThemeRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    updatedTheme: UpdateThemeDataTypeDef
    clientToken: Optional[str] = None

class ComponentEventPaginatorTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersPaginatorTypeDef] = None
    bindingEvent: Optional[str] = None

class ComponentEventTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    parameters: Optional[ActionParametersTypeDef] = None
    bindingEvent: Optional[str] = None

class ReactStartCodegenJobDataTypeDef(BaseValidatorModel):
    module: Optional[JSModuleType] = None
    target: Optional[JSTargetType] = None
    script: Optional[JSScriptType] = None
    renderTypeDeclarations: Optional[bool] = None
    inlineSourceMap: Optional[bool] = None
    apiConfiguration: Optional[ApiConfigurationTypeDef] = None
    dependencies: Optional[Dict[str, str]] = None

class CodegenGenericDataModelTypeDef(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldTypeDef]
    primaryKeys: List[str]
    isJoinTable: Optional[bool] = None

class CodegenGenericDataNonModelTypeDef(BaseValidatorModel):
    fields: Dict[str, CodegenGenericDataFieldTypeDef]

class ListFormsResponseTypeDef(BaseValidatorModel):
    entities: List[FormSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FormCTATypeDef(BaseValidatorModel):
    position: Optional[FormButtonsPositionType] = None
    clear: Optional[FormButtonTypeDef] = None
    cancel: Optional[FormButtonTypeDef] = None
    submit: Optional[FormButtonTypeDef] = None

class ValueMappingsPaginatorTypeDef(BaseValidatorModel):
    values: List[ValueMappingPaginatorTypeDef]
    bindingProperties: Optional[Dict[str, FormInputBindingPropertiesValueTypeDef]] = None

class ValueMappingsTypeDef(BaseValidatorModel):
    values: Sequence[ValueMappingTypeDef]
    bindingProperties: Optional[Mapping[str, FormInputBindingPropertiesValueTypeDef]] = None

class ComponentChildPaginatorTypeDef(BaseValidatorModel):
    componentType: str
    name: str
    properties: Dict[str, "ComponentPropertyPaginatorTypeDef"]
    children: Optional[List[Dict[str, Any]]] = None
    events: Optional[Dict[str, ComponentEventPaginatorTypeDef]] = None
    sourceId: Optional[str] = None

class ComponentPaginatorTypeDef(BaseValidatorModel):
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

class ComponentChildTypeDef(BaseValidatorModel):
    componentType: str
    name: str
    properties: Mapping[str, "ComponentPropertyTypeDef"]
    children: Optional[Sequence[Dict[str, Any]]] = None
    events: Optional[Mapping[str, ComponentEventTypeDef]] = None
    sourceId: Optional[str] = None

class ComponentTypeDef(BaseValidatorModel):
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

class CreateComponentDataTypeDef(BaseValidatorModel):
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

class UpdateComponentDataTypeDef(BaseValidatorModel):
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

class CodegenJobRenderConfigTypeDef(BaseValidatorModel):
    react: Optional[ReactStartCodegenJobDataTypeDef] = None

class CodegenJobGenericDataSchemaTypeDef(BaseValidatorModel):
    dataSourceType: Literal["DataStore"]
    models: Dict[str, CodegenGenericDataModelTypeDef]
    enums: Dict[str, CodegenGenericDataEnumTypeDef]
    nonModels: Dict[str, CodegenGenericDataNonModelTypeDef]

class FieldInputConfigPaginatorTypeDef(BaseValidatorModel):
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

class FieldInputConfigTypeDef(BaseValidatorModel):
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

class ExportComponentsResponsePaginatorTypeDef(BaseValidatorModel):
    entities: List[ComponentPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentResponseTypeDef(BaseValidatorModel):
    entity: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportComponentsResponseTypeDef(BaseValidatorModel):
    entities: List[ComponentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentResponseTypeDef(BaseValidatorModel):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComponentResponseTypeDef(BaseValidatorModel):
    entity: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    componentToCreate: CreateComponentDataTypeDef
    clientToken: Optional[str] = None

class UpdateComponentRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    updatedComponent: UpdateComponentDataTypeDef
    clientToken: Optional[str] = None

class CodegenJobTypeDef(BaseValidatorModel):
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

class StartCodegenJobDataTypeDef(BaseValidatorModel):
    renderConfig: CodegenJobRenderConfigTypeDef
    genericDataSchema: Optional[CodegenJobGenericDataSchemaTypeDef] = None
    autoGenerateForms: Optional[bool] = None
    features: Optional[CodegenFeatureFlagsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class FieldConfigPaginatorTypeDef(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigPaginatorTypeDef] = None
    validations: Optional[List[FieldValidationConfigurationPaginatorTypeDef]] = None

class FieldConfigTypeDef(BaseValidatorModel):
    label: Optional[str] = None
    position: Optional[FieldPositionTypeDef] = None
    excluded: Optional[bool] = None
    inputType: Optional[FieldInputConfigTypeDef] = None
    validations: Optional[Sequence[FieldValidationConfigurationTypeDef]] = None

class GetCodegenJobResponseTypeDef(BaseValidatorModel):
    job: CodegenJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCodegenJobResponseTypeDef(BaseValidatorModel):
    entity: CodegenJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCodegenJobRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    codegenJobToCreate: StartCodegenJobDataTypeDef
    clientToken: Optional[str] = None

class FormPaginatorTypeDef(BaseValidatorModel):
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

class CreateFormDataTypeDef(BaseValidatorModel):
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

class FormTypeDef(BaseValidatorModel):
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

class UpdateFormDataTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[FormDataTypeConfigTypeDef] = None
    formActionType: Optional[FormActionTypeType] = None
    fields: Optional[Mapping[str, FieldConfigTypeDef]] = None
    style: Optional[FormStyleTypeDef] = None
    sectionalElements: Optional[Mapping[str, SectionalElementTypeDef]] = None
    schemaVersion: Optional[str] = None
    cta: Optional[FormCTATypeDef] = None
    labelDecorator: Optional[LabelDecoratorType] = None

class ExportFormsResponsePaginatorTypeDef(BaseValidatorModel):
    entities: List[FormPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFormRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    formToCreate: CreateFormDataTypeDef
    clientToken: Optional[str] = None

class CreateFormResponseTypeDef(BaseValidatorModel):
    entity: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportFormsResponseTypeDef(BaseValidatorModel):
    entities: List[FormTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFormResponseTypeDef(BaseValidatorModel):
    form: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFormResponseTypeDef(BaseValidatorModel):
    entity: FormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFormRequestRequestTypeDef(BaseValidatorModel):
    appId: str
    environmentName: str
    id: str
    updatedForm: UpdateFormDataTypeDef
    clientToken: Optional[str] = None

