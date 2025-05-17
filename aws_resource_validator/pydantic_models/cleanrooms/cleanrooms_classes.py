from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cleanrooms.cleanrooms_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AggregateColumnOutput(BaseValidatorModel):
    columnNames: List[str]
    function: AggregateFunctionNameType


class AggregateColumn(BaseValidatorModel):
    columnNames: List[str]
    function: AggregateFunctionNameType


class AggregationConstraint(BaseValidatorModel):
    columnName: str
    minimum: int
    type: Literal['COUNT_DISTINCT']


class AnalysisParameter(BaseValidatorModel):
    name: str
    type: ParameterTypeType
    defaultValue: Optional[str] = None


class AnalysisRuleListOutput(BaseValidatorModel):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisRuleList(BaseValidatorModel):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisSchema(BaseValidatorModel):
    referencedTables: Optional[List[str]] = None


class AnalysisSource(BaseValidatorModel):
    text: Optional[str] = None


class AnalysisTemplateSummary(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    name: str
    updateTime: datetime
    membershipArn: str
    membershipId: str
    collaborationArn: str
    collaborationId: str
    description: Optional[str] = None


class AnalysisTemplateValidationStatusReason(BaseValidatorModel):
    message: str


class AthenaTableReference(BaseValidatorModel):
    workGroup: str
    databaseName: str
    tableName: str
    outputLocation: Optional[str] = None


class BatchGetCollaborationAnalysisTemplateError(BaseValidatorModel):
    arn: str
    code: str
    message: str


# This class is the input for the 'batch_get_collaboration_analysis_template' function.
class BatchGetCollaborationAnalysisTemplateInput(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArns: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetSchemaAnalysisRuleError(BaseValidatorModel):
    name: str
    type: AnalysisRuleTypeType
    code: str
    message: str


class SchemaAnalysisRuleRequest(BaseValidatorModel):
    name: str
    type: AnalysisRuleTypeType


class BatchGetSchemaError(BaseValidatorModel):
    name: str
    code: str
    message: str


# This class is the input for the 'batch_get_schema' function.
class BatchGetSchemaInput(BaseValidatorModel):
    collaborationIdentifier: str
    names: List[str]


class BilledResourceUtilization(BaseValidatorModel):
    units: float


class CollaborationAnalysisTemplateSummary(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    name: str
    updateTime: datetime
    collaborationArn: str
    collaborationId: str
    creatorAccountId: str
    description: Optional[str] = None


class CollaborationConfiguredAudienceModelAssociationSummary(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    name: str
    updateTime: datetime
    collaborationArn: str
    collaborationId: str
    creatorAccountId: str
    description: Optional[str] = None


class CollaborationConfiguredAudienceModelAssociation(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    configuredAudienceModelArn: str
    name: str
    creatorAccountId: str
    createTime: datetime
    updateTime: datetime
    description: Optional[str] = None


class IdNamespaceAssociationInputReferenceConfig(BaseValidatorModel):
    inputReferenceArn: str
    manageResourcePolicies: bool


class IdNamespaceAssociationInputReferencePropertiesSummary(BaseValidatorModel):
    idNamespaceType: IdNamespaceTypeType


class IdMappingConfig(BaseValidatorModel):
    allowUseAsDimensionColumn: bool


class IdNamespaceAssociationInputReferenceProperties(BaseValidatorModel):
    idNamespaceType: IdNamespaceTypeType
    idMappingWorkflowsSupported: List[Dict[str, Any]]


class CollaborationPrivacyBudgetTemplateSummary(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    createTime: datetime
    updateTime: datetime


class CollaborationSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    creatorAccountId: str
    creatorDisplayName: str
    createTime: datetime
    updateTime: datetime
    memberStatus: MemberStatusType
    membershipId: Optional[str] = None
    membershipArn: Optional[str] = None
    analyticsEngine: Optional[AnalyticsEngineType] = None


class DataEncryptionMetadata(BaseValidatorModel):
    allowCleartext: bool
    allowDuplicates: bool
    allowJoinsOnColumnsWithDifferentNames: bool
    preserveNulls: bool


class Column(BaseValidatorModel):
    name: str
    type: str


class WorkerComputeConfiguration(BaseValidatorModel):
    type: Optional[WorkerComputeTypeType] = None
    number: Optional[int] = None


class DirectAnalysisConfigurationDetails(BaseValidatorModel):
    receiverAccountIds: Optional[List[str]] = None


class ConfiguredAudienceModelAssociationSummary(BaseValidatorModel):
    membershipId: str
    membershipArn: str
    collaborationArn: str
    collaborationId: str
    createTime: datetime
    updateTime: datetime
    id: str
    arn: str
    name: str
    configuredAudienceModelArn: str
    description: Optional[str] = None


class ConfiguredAudienceModelAssociation(BaseValidatorModel):
    id: str
    arn: str
    configuredAudienceModelArn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    name: str
    manageResourcePolicies: bool
    createTime: datetime
    updateTime: datetime
    description: Optional[str] = None


class ConfiguredTableAssociationAnalysisRuleAggregationOutput(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleAggregation(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleCustomOutput(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleCustom(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleListOutput(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleList(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationSummary(BaseValidatorModel):
    configuredTableId: str
    membershipId: str
    membershipArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    id: str
    arn: str


class ConfiguredTableAssociation(BaseValidatorModel):
    arn: str
    id: str
    configuredTableId: str
    configuredTableArn: str
    membershipId: str
    membershipArn: str
    roleArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    description: Optional[str] = None
    analysisRuleTypes: Optional[List[ConfiguredTableAssociationAnalysisRuleTypeType]] = None


class ConfiguredTableSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    createTime: datetime
    updateTime: datetime
    analysisRuleTypes: List[ConfiguredTableAnalysisRuleTypeType]
    analysisMethod: Literal['DIRECT_QUERY']


# This class is the input for the 'create_configured_audience_model_association' function.
class CreateConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredAudienceModelArn: str
    configuredAudienceModelAssociationName: str
    manageResourcePolicies: bool
    tags: Optional[Dict[str, str]] = None
    description: Optional[str] = None


# This class is the input for the 'create_configured_table_association' function.
class CreateConfiguredTableAssociationInput(BaseValidatorModel):
    name: str
    membershipIdentifier: str
    configuredTableIdentifier: str
    roleArn: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class IdMappingTableInputReferenceConfig(BaseValidatorModel):
    inputReferenceArn: str
    manageResourcePolicies: bool


class DeleteAnalysisTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str


class DeleteCollaborationInput(BaseValidatorModel):
    collaborationIdentifier: str


class DeleteConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str


class DeleteConfiguredTableAnalysisRuleInput(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType


class DeleteConfiguredTableAssociationAnalysisRuleInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType


class DeleteConfiguredTableAssociationInput(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str


class DeleteConfiguredTableInput(BaseValidatorModel):
    configuredTableIdentifier: str


class DeleteIdMappingTableInput(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str


class DeleteIdNamespaceAssociationInput(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str


class DeleteMemberInput(BaseValidatorModel):
    collaborationIdentifier: str
    accountId: str


class DeleteMembershipInput(BaseValidatorModel):
    membershipIdentifier: str


class DeletePrivacyBudgetTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str


class DifferentialPrivacyColumn(BaseValidatorModel):
    name: str


class DifferentialPrivacySensitivityParameters(BaseValidatorModel):
    aggregationType: DifferentialPrivacyAggregationTypeType
    aggregationExpression: str
    userContributionLimit: int
    minColumnValue: Optional[float] = None
    maxColumnValue: Optional[float] = None


class DifferentialPrivacyPreviewAggregation(BaseValidatorModel):
    type: DifferentialPrivacyAggregationTypeType
    maxCount: int


class DifferentialPrivacyPreviewParametersInput(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyPrivacyBudgetAggregation(BaseValidatorModel):
    type: DifferentialPrivacyAggregationTypeType
    maxCount: int
    remainingCount: int


class DifferentialPrivacyTemplateParametersInput(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateParametersOutput(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateUpdateParameters(BaseValidatorModel):
    epsilon: Optional[int] = None
    usersNoisePerQuery: Optional[int] = None


# This class is the input for the 'get_analysis_template' function.
class GetAnalysisTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str


# This class is the input for the 'get_collaboration_analysis_template' function.
class GetCollaborationAnalysisTemplateInput(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArn: str


# This class is the input for the 'get_collaboration_configured_audience_model_association' function.
class GetCollaborationConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    collaborationIdentifier: str
    configuredAudienceModelAssociationIdentifier: str


# This class is the input for the 'get_collaboration_id_namespace_association' function.
class GetCollaborationIdNamespaceAssociationInput(BaseValidatorModel):
    collaborationIdentifier: str
    idNamespaceAssociationIdentifier: str


# This class is the input for the 'get_collaboration' function.
class GetCollaborationInput(BaseValidatorModel):
    collaborationIdentifier: str


# This class is the input for the 'get_collaboration_privacy_budget_template' function.
class GetCollaborationPrivacyBudgetTemplateInput(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetTemplateIdentifier: str


# This class is the input for the 'get_configured_audience_model_association' function.
class GetConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str


# This class is the input for the 'get_configured_table_analysis_rule' function.
class GetConfiguredTableAnalysisRuleInput(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType


# This class is the input for the 'get_configured_table_association_analysis_rule' function.
class GetConfiguredTableAssociationAnalysisRuleInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType


# This class is the input for the 'get_configured_table_association' function.
class GetConfiguredTableAssociationInput(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str


# This class is the input for the 'get_configured_table' function.
class GetConfiguredTableInput(BaseValidatorModel):
    configuredTableIdentifier: str


# This class is the input for the 'get_id_mapping_table' function.
class GetIdMappingTableInput(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str


# This class is the input for the 'get_id_namespace_association' function.
class GetIdNamespaceAssociationInput(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str


# This class is the input for the 'get_membership' function.
class GetMembershipInput(BaseValidatorModel):
    membershipIdentifier: str


# This class is the input for the 'get_privacy_budget_template' function.
class GetPrivacyBudgetTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str


# This class is the input for the 'get_protected_query' function.
class GetProtectedQueryInput(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str


# This class is the input for the 'get_schema_analysis_rule' function.
class GetSchemaAnalysisRuleInput(BaseValidatorModel):
    collaborationIdentifier: str
    name: str
    type: AnalysisRuleTypeType


# This class is the input for the 'get_schema' function.
class GetSchemaInput(BaseValidatorModel):
    collaborationIdentifier: str
    name: str


class GlueTableReference(BaseValidatorModel):
    tableName: str
    databaseName: str


class IdMappingTableInputSource(BaseValidatorModel):
    idNamespaceAssociationId: str
    type: IdNamespaceTypeType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_analysis_templates' function.
class ListAnalysisTemplatesInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_analysis_templates' function.
class ListCollaborationAnalysisTemplatesInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_configured_audience_model_associations' function.
class ListCollaborationConfiguredAudienceModelAssociationsInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_id_namespace_associations' function.
class ListCollaborationIdNamespaceAssociationsInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_privacy_budget_templates' function.
class ListCollaborationPrivacyBudgetTemplatesInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_privacy_budgets' function.
class ListCollaborationPrivacyBudgetsInput(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_collaborations' function.
class ListCollaborationsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    memberStatus: Optional[FilterableMemberStatusType] = None


# This class is the input for the 'list_configured_audience_model_associations' function.
class ListConfiguredAudienceModelAssociationsInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_configured_table_associations' function.
class ListConfiguredTableAssociationsInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_configured_tables' function.
class ListConfiguredTablesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_id_mapping_tables' function.
class ListIdMappingTablesInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_id_namespace_associations' function.
class ListIdNamespaceAssociationsInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_members' function.
class ListMembersInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_memberships' function.
class ListMembershipsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[MembershipStatusType] = None


# This class is the input for the 'list_privacy_budget_templates' function.
class ListPrivacyBudgetTemplatesInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PrivacyBudgetTemplateSummary(BaseValidatorModel):
    id: str
    arn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    createTime: datetime
    updateTime: datetime


# This class is the input for the 'list_privacy_budgets' function.
class ListPrivacyBudgetsInput(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_protected_queries' function.
class ListProtectedQueriesInput(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_schemas' function.
class ListSchemasInput(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[SchemaTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SchemaSummary(BaseValidatorModel):
    name: str
    type: SchemaTypeType
    creatorAccountId: str
    createTime: datetime
    updateTime: datetime
    collaborationId: str
    collaborationArn: str
    analysisRuleTypes: List[AnalysisRuleTypeType]
    analysisMethod: Optional[Literal['DIRECT_QUERY']] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class MLMemberAbilitiesOutput(BaseValidatorModel):
    customMLMemberAbilities: List[CustomMLMemberAbilityType]


class MLMemberAbilities(BaseValidatorModel):
    customMLMemberAbilities: List[CustomMLMemberAbilityType]


class ModelInferencePaymentConfig(BaseValidatorModel):
    isResponsible: bool


class ModelTrainingPaymentConfig(BaseValidatorModel):
    isResponsible: bool


class MembershipModelInferencePaymentConfig(BaseValidatorModel):
    isResponsible: bool


class MembershipModelTrainingPaymentConfig(BaseValidatorModel):
    isResponsible: bool


class MembershipQueryComputePaymentConfig(BaseValidatorModel):
    isResponsible: bool


class ProtectedQueryS3OutputConfiguration(BaseValidatorModel):
    resultFormat: ResultFormatType
    bucket: str
    keyPrefix: Optional[str] = None
    singleFileOutput: Optional[bool] = None


class QueryComputePaymentConfig(BaseValidatorModel):
    isResponsible: bool


# This class is the input for the 'populate_id_mapping_table' function.
class PopulateIdMappingTableInput(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str


class ProtectedQueryError(BaseValidatorModel):
    message: str
    code: str


class ProtectedQueryMemberOutputConfiguration(BaseValidatorModel):
    accountId: str


class ProtectedQueryS3Output(BaseValidatorModel):
    location: str


class ProtectedQuerySingleMemberOutput(BaseValidatorModel):
    accountId: str


class ProtectedQuerySQLParametersOutput(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class ProtectedQuerySQLParameters(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class QueryConstraintRequireOverlap(BaseValidatorModel):
    columns: Optional[List[str]] = None


class SchemaStatusReason(BaseValidatorModel):
    code: SchemaStatusReasonCodeType
    message: str


class SnowflakeTableSchemaV1(BaseValidatorModel):
    columnName: str
    columnType: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_analysis_template' function.
class UpdateAnalysisTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str
    description: Optional[str] = None


# This class is the input for the 'update_collaboration' function.
class UpdateCollaborationInput(BaseValidatorModel):
    collaborationIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'update_configured_audience_model_association' function.
class UpdateConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    name: Optional[str] = None


# This class is the input for the 'update_configured_table_association' function.
class UpdateConfiguredTableAssociationInput(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    roleArn: Optional[str] = None


# This class is the input for the 'update_configured_table' function.
class UpdateConfiguredTableInput(BaseValidatorModel):
    configuredTableIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'update_id_mapping_table' function.
class UpdateIdMappingTableInput(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None


# This class is the input for the 'update_protected_query' function.
class UpdateProtectedQueryInput(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str
    targetStatus: Literal['CANCELLED']


class AnalysisRuleAggregationOutput(BaseValidatorModel):
    aggregateColumns: List[AggregateColumnOutput]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraint]
    joinRequired: Optional[Literal['QUERY_RUNNER']] = None
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisRuleAggregation(BaseValidatorModel):
    aggregateColumns: List[AggregateColumn]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraint]
    joinRequired: Optional[Literal['QUERY_RUNNER']] = None
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


# This class is the input for the 'create_analysis_template' function.
class CreateAnalysisTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    format: Literal['SQL']
    source: AnalysisSource
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    analysisParameters: Optional[List[AnalysisParameter]] = None


class AnalysisTemplateValidationStatusDetail(BaseValidatorModel):
    type: Literal['DIFFERENTIAL_PRIVACY']
    status: AnalysisTemplateValidationStatusType
    reasons: Optional[List[AnalysisTemplateValidationStatusReason]] = None


# This class is the output for the 'list_analysis_templates' function.
class ListAnalysisTemplatesOutput(BaseValidatorModel):
    analysisTemplateSummaries: List[AnalysisTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'populate_id_mapping_table' function.
class PopulateIdMappingTableOutput(BaseValidatorModel):
    idMappingJobId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_get_schema_analysis_rule' function.
class BatchGetSchemaAnalysisRuleInput(BaseValidatorModel):
    collaborationIdentifier: str
    schemaAnalysisRuleRequests: List[SchemaAnalysisRuleRequest]


class ProtectedQueryStatistics(BaseValidatorModel):
    totalDurationInMillis: Optional[int] = None
    billedResourceUtilization: Optional[BilledResourceUtilization] = None


# This class is the output for the 'list_collaboration_analysis_templates' function.
class ListCollaborationAnalysisTemplatesOutput(BaseValidatorModel):
    collaborationAnalysisTemplateSummaries: List[CollaborationAnalysisTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_collaboration_configured_audience_model_associations' function.
class ListCollaborationConfiguredAudienceModelAssociationsOutput(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociationSummaries: List[CollaborationConfiguredAudienceModelAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_collaboration_configured_audience_model_association' function.
class GetCollaborationConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociation: CollaborationConfiguredAudienceModelAssociation
    ResponseMetadata: ResponseMetadata


class CollaborationIdNamespaceAssociationSummary(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    updateTime: datetime
    collaborationArn: str
    collaborationId: str
    creatorAccountId: str
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfig
    name: str
    inputReferenceProperties: IdNamespaceAssociationInputReferencePropertiesSummary
    description: Optional[str] = None


class IdNamespaceAssociationSummary(BaseValidatorModel):
    membershipId: str
    membershipArn: str
    collaborationArn: str
    collaborationId: str
    createTime: datetime
    updateTime: datetime
    id: str
    arn: str
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfig
    name: str
    inputReferenceProperties: IdNamespaceAssociationInputReferencePropertiesSummary
    description: Optional[str] = None


# This class is the input for the 'create_id_namespace_association' function.
class CreateIdNamespaceAssociationInput(BaseValidatorModel):
    membershipIdentifier: str
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfig
    name: str
    tags: Optional[Dict[str, str]] = None
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfig] = None


# This class is the input for the 'update_id_namespace_association' function.
class UpdateIdNamespaceAssociationInput(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfig] = None


class CollaborationIdNamespaceAssociation(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    name: str
    creatorAccountId: str
    createTime: datetime
    updateTime: datetime
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfig
    inputReferenceProperties: IdNamespaceAssociationInputReferenceProperties
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfig] = None


class IdNamespaceAssociation(BaseValidatorModel):
    id: str
    arn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfig
    inputReferenceProperties: IdNamespaceAssociationInputReferenceProperties
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfig] = None


# This class is the output for the 'list_collaboration_privacy_budget_templates' function.
class ListCollaborationPrivacyBudgetTemplatesOutput(BaseValidatorModel):
    collaborationPrivacyBudgetTemplateSummaries: List[CollaborationPrivacyBudgetTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_collaborations' function.
class ListCollaborationsOutput(BaseValidatorModel):
    collaborationList: List[CollaborationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Collaboration(BaseValidatorModel):
    id: str
    arn: str
    name: str
    creatorAccountId: str
    creatorDisplayName: str
    createTime: datetime
    updateTime: datetime
    memberStatus: MemberStatusType
    queryLogStatus: CollaborationQueryLogStatusType
    description: Optional[str] = None
    membershipId: Optional[str] = None
    membershipArn: Optional[str] = None
    dataEncryptionMetadata: Optional[DataEncryptionMetadata] = None
    analyticsEngine: Optional[AnalyticsEngineType] = None


class ComputeConfiguration(BaseValidatorModel):
    worker: Optional[WorkerComputeConfiguration] = None


class ConfigurationDetails(BaseValidatorModel):
    directAnalysisConfigurationDetails: Optional[DirectAnalysisConfigurationDetails] = None


# This class is the output for the 'list_configured_audience_model_associations' function.
class ListConfiguredAudienceModelAssociationsOutput(BaseValidatorModel):
    configuredAudienceModelAssociationSummaries: List[ConfiguredAudienceModelAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_configured_audience_model_association' function.
class CreateConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_configured_audience_model_association' function.
class GetConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_configured_audience_model_association' function.
class UpdateConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociation
    ResponseMetadata: ResponseMetadata


class ConfiguredTableAssociationAnalysisRulePolicyV1Output(BaseValidatorModel):
    list: Optional[ConfiguredTableAssociationAnalysisRuleListOutput] = None
    aggregation: Optional[ConfiguredTableAssociationAnalysisRuleAggregationOutput] = None
    custom: Optional[ConfiguredTableAssociationAnalysisRuleCustomOutput] = None


class ConfiguredTableAssociationAnalysisRulePolicyV1(BaseValidatorModel):
    list: Optional[ConfiguredTableAssociationAnalysisRuleList] = None
    aggregation: Optional[ConfiguredTableAssociationAnalysisRuleAggregation] = None
    custom: Optional[ConfiguredTableAssociationAnalysisRuleCustom] = None


# This class is the output for the 'list_configured_table_associations' function.
class ListConfiguredTableAssociationsOutput(BaseValidatorModel):
    configuredTableAssociationSummaries: List[ConfiguredTableAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_configured_table_association' function.
class CreateConfiguredTableAssociationOutput(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_configured_table_association' function.
class GetConfiguredTableAssociationOutput(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_configured_table_association' function.
class UpdateConfiguredTableAssociationOutput(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_configured_tables' function.
class ListConfiguredTablesOutput(BaseValidatorModel):
    configuredTableSummaries: List[ConfiguredTableSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_id_mapping_table' function.
class CreateIdMappingTableInput(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    inputReferenceConfig: IdMappingTableInputReferenceConfig
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None


class IdMappingTableSummary(BaseValidatorModel):
    collaborationArn: str
    collaborationId: str
    membershipId: str
    membershipArn: str
    createTime: datetime
    updateTime: datetime
    id: str
    arn: str
    inputReferenceConfig: IdMappingTableInputReferenceConfig
    name: str
    description: Optional[str] = None


class DifferentialPrivacyConfigurationOutput(BaseValidatorModel):
    columns: List[DifferentialPrivacyColumn]


class DifferentialPrivacyConfiguration(BaseValidatorModel):
    columns: List[DifferentialPrivacyColumn]


class DifferentialPrivacyParameters(BaseValidatorModel):
    sensitivityParameters: List[DifferentialPrivacySensitivityParameters]


class DifferentialPrivacyPrivacyImpact(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPreviewAggregation]


class PreviewPrivacyImpactParametersInput(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPreviewParametersInput] = None


class DifferentialPrivacyPrivacyBudget(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPrivacyBudgetAggregation]
    epsilon: int


class PrivacyBudgetTemplateParametersInput(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersInput] = None


class PrivacyBudgetTemplateParametersOutput(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersOutput] = None


class PrivacyBudgetTemplateUpdateParameters(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateUpdateParameters] = None


class IdMappingTableInputReferenceProperties(BaseValidatorModel):
    idMappingTableInputSource: List[IdMappingTableInputSource]


class IdMappingTableSchemaTypeProperties(BaseValidatorModel):
    idMappingTableInputSource: List[IdMappingTableInputSource]


class ListAnalysisTemplatesInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationAnalysisTemplatesInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationConfiguredAudienceModelAssociationsInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationIdNamespaceAssociationsInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationPrivacyBudgetTemplatesInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationPrivacyBudgetsInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationsInputPaginate(BaseValidatorModel):
    memberStatus: Optional[FilterableMemberStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfiguredAudienceModelAssociationsInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfiguredTableAssociationsInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfiguredTablesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIdMappingTablesInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIdNamespaceAssociationsInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembershipsInputPaginate(BaseValidatorModel):
    status: Optional[MembershipStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrivacyBudgetTemplatesInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrivacyBudgetsInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProtectedQueriesInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemasInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[SchemaTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_privacy_budget_templates' function.
class ListPrivacyBudgetTemplatesOutput(BaseValidatorModel):
    privacyBudgetTemplateSummaries: List[PrivacyBudgetTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_schemas' function.
class ListSchemasOutput(BaseValidatorModel):
    schemaSummaries: List[SchemaSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

MLMemberAbilitiesUnion = Union[MLMemberAbilities, MLMemberAbilitiesOutput]


class MLPaymentConfig(BaseValidatorModel):
    modelTraining: Optional[ModelTrainingPaymentConfig] = None
    modelInference: Optional[ModelInferencePaymentConfig] = None


class MembershipMLPaymentConfig(BaseValidatorModel):
    modelTraining: Optional[MembershipModelTrainingPaymentConfig] = None
    modelInference: Optional[MembershipModelInferencePaymentConfig] = None


class MembershipProtectedQueryOutputConfiguration(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputConfiguration] = None


class ProtectedQueryOutputConfiguration(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputConfiguration] = None
    member: Optional[ProtectedQueryMemberOutputConfiguration] = None


class ProtectedQueryOutput(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3Output] = None
    memberList: Optional[List[ProtectedQuerySingleMemberOutput]] = None

ProtectedQuerySQLParametersUnion = Union[ProtectedQuerySQLParameters, ProtectedQuerySQLParametersOutput]


class QueryConstraint(BaseValidatorModel):
    requireOverlap: Optional[QueryConstraintRequireOverlap] = None


class SchemaStatusDetail(BaseValidatorModel):
    status: SchemaStatusType
    analysisType: AnalysisTypeType
    reasons: Optional[List[SchemaStatusReason]] = None
    analysisRuleType: Optional[AnalysisRuleTypeType] = None
    configurations: Optional[List[Literal['DIFFERENTIAL_PRIVACY']]] = None


class SnowflakeTableSchemaOutput(BaseValidatorModel):
    v1: Optional[List[SnowflakeTableSchemaV1]] = None


class SnowflakeTableSchema(BaseValidatorModel):
    v1: Optional[List[SnowflakeTableSchemaV1]] = None


class AnalysisTemplate(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    membershipId: str
    membershipArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    schema: AnalysisSchema
    format: Literal['SQL']
    source: AnalysisSource
    description: Optional[str] = None
    analysisParameters: Optional[List[AnalysisParameter]] = None
    validations: Optional[List[AnalysisTemplateValidationStatusDetail]] = None


class CollaborationAnalysisTemplate(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    name: str
    createTime: datetime
    updateTime: datetime
    schema: AnalysisSchema
    format: Literal['SQL']
    source: AnalysisSource
    description: Optional[str] = None
    analysisParameters: Optional[List[AnalysisParameter]] = None
    validations: Optional[List[AnalysisTemplateValidationStatusDetail]] = None


# This class is the output for the 'list_collaboration_id_namespace_associations' function.
class ListCollaborationIdNamespaceAssociationsOutput(BaseValidatorModel):
    collaborationIdNamespaceAssociationSummaries: List[CollaborationIdNamespaceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_id_namespace_associations' function.
class ListIdNamespaceAssociationsOutput(BaseValidatorModel):
    idNamespaceAssociationSummaries: List[IdNamespaceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_collaboration_id_namespace_association' function.
class GetCollaborationIdNamespaceAssociationOutput(BaseValidatorModel):
    collaborationIdNamespaceAssociation: CollaborationIdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_id_namespace_association' function.
class CreateIdNamespaceAssociationOutput(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_id_namespace_association' function.
class GetIdNamespaceAssociationOutput(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_id_namespace_association' function.
class UpdateIdNamespaceAssociationOutput(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_collaboration' function.
class CreateCollaborationOutput(BaseValidatorModel):
    collaboration: Collaboration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_collaboration' function.
class GetCollaborationOutput(BaseValidatorModel):
    collaboration: Collaboration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_collaboration' function.
class UpdateCollaborationOutput(BaseValidatorModel):
    collaboration: Collaboration
    ResponseMetadata: ResponseMetadata


class ReceiverConfiguration(BaseValidatorModel):
    analysisType: AnalysisTypeType
    configurationDetails: Optional[ConfigurationDetails] = None


class ConfiguredTableAssociationAnalysisRulePolicyOutput(BaseValidatorModel):
    v1: Optional[ConfiguredTableAssociationAnalysisRulePolicyV1Output] = None


class ConfiguredTableAssociationAnalysisRulePolicy(BaseValidatorModel):
    v1: Optional[ConfiguredTableAssociationAnalysisRulePolicyV1] = None


# This class is the output for the 'list_id_mapping_tables' function.
class ListIdMappingTablesOutput(BaseValidatorModel):
    idMappingTableSummaries: List[IdMappingTableSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AnalysisRuleCustomOutput(BaseValidatorModel):
    allowedAnalyses: List[str]
    allowedAnalysisProviders: Optional[List[str]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None
    disallowedOutputColumns: Optional[List[str]] = None
    differentialPrivacy: Optional[DifferentialPrivacyConfigurationOutput] = None


class AnalysisRuleCustom(BaseValidatorModel):
    allowedAnalyses: List[str]
    allowedAnalysisProviders: Optional[List[str]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None
    disallowedOutputColumns: Optional[List[str]] = None
    differentialPrivacy: Optional[DifferentialPrivacyConfiguration] = None


class PrivacyImpact(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyImpact] = None


# This class is the input for the 'preview_privacy_impact' function.
class PreviewPrivacyImpactInput(BaseValidatorModel):
    membershipIdentifier: str
    parameters: PreviewPrivacyImpactParametersInput


class PrivacyBudget(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyBudget] = None


# This class is the input for the 'create_privacy_budget_template' function.
class CreatePrivacyBudgetTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    parameters: PrivacyBudgetTemplateParametersInput
    tags: Optional[Dict[str, str]] = None


class CollaborationPrivacyBudgetTemplate(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    createTime: datetime
    updateTime: datetime
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    parameters: PrivacyBudgetTemplateParametersOutput


class PrivacyBudgetTemplate(BaseValidatorModel):
    id: str
    arn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    createTime: datetime
    updateTime: datetime
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    parameters: PrivacyBudgetTemplateParametersOutput


# This class is the input for the 'update_privacy_budget_template' function.
class UpdatePrivacyBudgetTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str
    privacyBudgetType: Literal['DIFFERENTIAL_PRIVACY']
    parameters: Optional[PrivacyBudgetTemplateUpdateParameters] = None


class IdMappingTable(BaseValidatorModel):
    id: str
    arn: str
    inputReferenceConfig: IdMappingTableInputReferenceConfig
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    inputReferenceProperties: IdMappingTableInputReferenceProperties
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None


class SchemaTypeProperties(BaseValidatorModel):
    idMappingTable: Optional[IdMappingTableSchemaTypeProperties] = None


class PaymentConfiguration(BaseValidatorModel):
    queryCompute: QueryComputePaymentConfig
    machineLearning: Optional[MLPaymentConfig] = None


class MembershipPaymentConfiguration(BaseValidatorModel):
    queryCompute: MembershipQueryComputePaymentConfig
    machineLearning: Optional[MembershipMLPaymentConfig] = None


class MembershipProtectedQueryResultConfiguration(BaseValidatorModel):
    outputConfiguration: MembershipProtectedQueryOutputConfiguration
    roleArn: Optional[str] = None


class ProtectedQueryResultConfiguration(BaseValidatorModel):
    outputConfiguration: ProtectedQueryOutputConfiguration


class ProtectedQueryResult(BaseValidatorModel):
    output: ProtectedQueryOutput


class AnalysisRuleIdMappingTable(BaseValidatorModel):
    joinColumns: List[str]
    queryConstraints: List[QueryConstraint]
    dimensionColumns: Optional[List[str]] = None


class SnowflakeTableReferenceOutput(BaseValidatorModel):
    secretArn: str
    accountIdentifier: str
    databaseName: str
    tableName: str
    schemaName: str
    tableSchema: SnowflakeTableSchemaOutput


class SnowflakeTableReference(BaseValidatorModel):
    secretArn: str
    accountIdentifier: str
    databaseName: str
    tableName: str
    schemaName: str
    tableSchema: SnowflakeTableSchema


# This class is the output for the 'create_analysis_template' function.
class CreateAnalysisTemplateOutput(BaseValidatorModel):
    analysisTemplate: AnalysisTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_analysis_template' function.
class GetAnalysisTemplateOutput(BaseValidatorModel):
    analysisTemplate: AnalysisTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_analysis_template' function.
class UpdateAnalysisTemplateOutput(BaseValidatorModel):
    analysisTemplate: AnalysisTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_collaboration_analysis_template' function.
class BatchGetCollaborationAnalysisTemplateOutput(BaseValidatorModel):
    collaborationAnalysisTemplates: List[CollaborationAnalysisTemplate]
    errors: List[BatchGetCollaborationAnalysisTemplateError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_collaboration_analysis_template' function.
class GetCollaborationAnalysisTemplateOutput(BaseValidatorModel):
    collaborationAnalysisTemplate: CollaborationAnalysisTemplate
    ResponseMetadata: ResponseMetadata


class ProtectedQuerySummary(BaseValidatorModel):
    id: str
    membershipId: str
    membershipArn: str
    createTime: datetime
    status: ProtectedQueryStatusType
    receiverConfigurations: List[ReceiverConfiguration]


class ConfiguredTableAssociationAnalysisRule(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationId: str
    configuredTableAssociationArn: str
    policy: ConfiguredTableAssociationAnalysisRulePolicyOutput
    type: ConfiguredTableAssociationAnalysisRuleTypeType
    createTime: datetime
    updateTime: datetime

ConfiguredTableAssociationAnalysisRulePolicyUnion = Union[ConfiguredTableAssociationAnalysisRulePolicy, ConfiguredTableAssociationAnalysisRulePolicyOutput]


class ConfiguredTableAnalysisRulePolicyV1Output(BaseValidatorModel):
    list: Optional[AnalysisRuleListOutput] = None
    aggregation: Optional[AnalysisRuleAggregationOutput] = None
    custom: Optional[AnalysisRuleCustomOutput] = None


class ConfiguredTableAnalysisRulePolicyV1(BaseValidatorModel):
    list: Optional[AnalysisRuleList] = None
    aggregation: Optional[AnalysisRuleAggregation] = None
    custom: Optional[AnalysisRuleCustom] = None


# This class is the output for the 'preview_privacy_impact' function.
class PreviewPrivacyImpactOutput(BaseValidatorModel):
    privacyImpact: PrivacyImpact
    ResponseMetadata: ResponseMetadata


class CollaborationPrivacyBudgetSummary(BaseValidatorModel):
    id: str
    privacyBudgetTemplateId: str
    privacyBudgetTemplateArn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    type: Literal['DIFFERENTIAL_PRIVACY']
    createTime: datetime
    updateTime: datetime
    budget: PrivacyBudget


class PrivacyBudgetSummary(BaseValidatorModel):
    id: str
    privacyBudgetTemplateId: str
    privacyBudgetTemplateArn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    type: Literal['DIFFERENTIAL_PRIVACY']
    createTime: datetime
    updateTime: datetime
    budget: PrivacyBudget


# This class is the output for the 'get_collaboration_privacy_budget_template' function.
class GetCollaborationPrivacyBudgetTemplateOutput(BaseValidatorModel):
    collaborationPrivacyBudgetTemplate: CollaborationPrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_privacy_budget_template' function.
class CreatePrivacyBudgetTemplateOutput(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_privacy_budget_template' function.
class GetPrivacyBudgetTemplateOutput(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_privacy_budget_template' function.
class UpdatePrivacyBudgetTemplateOutput(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_id_mapping_table' function.
class CreateIdMappingTableOutput(BaseValidatorModel):
    idMappingTable: IdMappingTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_id_mapping_table' function.
class GetIdMappingTableOutput(BaseValidatorModel):
    idMappingTable: IdMappingTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_id_mapping_table' function.
class UpdateIdMappingTableOutput(BaseValidatorModel):
    idMappingTable: IdMappingTable
    ResponseMetadata: ResponseMetadata


class Schema(BaseValidatorModel):
    columns: List[Column]
    partitionKeys: List[Column]
    analysisRuleTypes: List[AnalysisRuleTypeType]
    creatorAccountId: str
    name: str
    collaborationId: str
    collaborationArn: str
    description: str
    createTime: datetime
    updateTime: datetime
    type: SchemaTypeType
    schemaStatusDetails: List[SchemaStatusDetail]
    analysisMethod: Optional[Literal['DIRECT_QUERY']] = None
    schemaTypeProperties: Optional[SchemaTypeProperties] = None


class MemberSpecification(BaseValidatorModel):
    accountId: str
    memberAbilities: List[MemberAbilityType]
    displayName: str
    mlMemberAbilities: Optional[MLMemberAbilitiesUnion] = None
    paymentConfiguration: Optional[PaymentConfiguration] = None


class MemberSummary(BaseValidatorModel):
    accountId: str
    status: MemberStatusType
    displayName: str
    abilities: List[MemberAbilityType]
    createTime: datetime
    updateTime: datetime
    paymentConfiguration: PaymentConfiguration
    mlAbilities: Optional[MLMemberAbilitiesOutput] = None
    membershipId: Optional[str] = None
    membershipArn: Optional[str] = None


class MembershipSummary(BaseValidatorModel):
    id: str
    arn: str
    collaborationArn: str
    collaborationId: str
    collaborationCreatorAccountId: str
    collaborationCreatorDisplayName: str
    collaborationName: str
    createTime: datetime
    updateTime: datetime
    status: MembershipStatusType
    memberAbilities: List[MemberAbilityType]
    paymentConfiguration: MembershipPaymentConfiguration
    mlMemberAbilities: Optional[MLMemberAbilitiesOutput] = None


# This class is the input for the 'create_membership' function.
class CreateMembershipInput(BaseValidatorModel):
    collaborationIdentifier: str
    queryLogStatus: MembershipQueryLogStatusType
    tags: Optional[Dict[str, str]] = None
    defaultResultConfiguration: Optional[MembershipProtectedQueryResultConfiguration] = None
    paymentConfiguration: Optional[MembershipPaymentConfiguration] = None


class Membership(BaseValidatorModel):
    id: str
    arn: str
    collaborationArn: str
    collaborationId: str
    collaborationCreatorAccountId: str
    collaborationCreatorDisplayName: str
    collaborationName: str
    createTime: datetime
    updateTime: datetime
    status: MembershipStatusType
    memberAbilities: List[MemberAbilityType]
    queryLogStatus: MembershipQueryLogStatusType
    paymentConfiguration: MembershipPaymentConfiguration
    mlMemberAbilities: Optional[MLMemberAbilitiesOutput] = None
    defaultResultConfiguration: Optional[MembershipProtectedQueryResultConfiguration] = None


# This class is the input for the 'update_membership' function.
class UpdateMembershipInput(BaseValidatorModel):
    membershipIdentifier: str
    queryLogStatus: Optional[MembershipQueryLogStatusType] = None
    defaultResultConfiguration: Optional[MembershipProtectedQueryResultConfiguration] = None


# This class is the input for the 'start_protected_query' function.
class StartProtectedQueryInput(BaseValidatorModel):
    type: Literal['SQL']
    membershipIdentifier: str
    sqlParameters: ProtectedQuerySQLParametersUnion
    resultConfiguration: Optional[ProtectedQueryResultConfiguration] = None
    computeConfiguration: Optional[ComputeConfiguration] = None


class ProtectedQuery(BaseValidatorModel):
    id: str
    membershipId: str
    membershipArn: str
    createTime: datetime
    status: ProtectedQueryStatusType
    sqlParameters: Optional[ProtectedQuerySQLParametersOutput] = None
    resultConfiguration: Optional[ProtectedQueryResultConfiguration] = None
    statistics: Optional[ProtectedQueryStatistics] = None
    result: Optional[ProtectedQueryResult] = None
    error: Optional[ProtectedQueryError] = None
    differentialPrivacy: Optional[DifferentialPrivacyParameters] = None
    computeConfiguration: Optional[ComputeConfiguration] = None


class AnalysisRulePolicyV1(BaseValidatorModel):
    list: Optional[AnalysisRuleListOutput] = None
    aggregation: Optional[AnalysisRuleAggregationOutput] = None
    custom: Optional[AnalysisRuleCustomOutput] = None
    idMappingTable: Optional[AnalysisRuleIdMappingTable] = None


class TableReferenceOutput(BaseValidatorModel):
    glue: Optional[GlueTableReference] = None
    snowflake: Optional[SnowflakeTableReferenceOutput] = None
    athena: Optional[AthenaTableReference] = None


class TableReference(BaseValidatorModel):
    glue: Optional[GlueTableReference] = None
    snowflake: Optional[SnowflakeTableReference] = None
    athena: Optional[AthenaTableReference] = None


# This class is the output for the 'list_protected_queries' function.
class ListProtectedQueriesOutput(BaseValidatorModel):
    protectedQueries: List[ProtectedQuerySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_configured_table_association_analysis_rule' function.
class CreateConfiguredTableAssociationAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_configured_table_association_analysis_rule' function.
class GetConfiguredTableAssociationAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_configured_table_association_analysis_rule' function.
class UpdateConfiguredTableAssociationAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRule
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_configured_table_association_analysis_rule' function.
class CreateConfiguredTableAssociationAnalysisRuleInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnion


# This class is the input for the 'update_configured_table_association_analysis_rule' function.
class UpdateConfiguredTableAssociationAnalysisRuleInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnion


class ConfiguredTableAnalysisRulePolicyOutput(BaseValidatorModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1Output] = None


class ConfiguredTableAnalysisRulePolicy(BaseValidatorModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1] = None


# This class is the output for the 'list_collaboration_privacy_budgets' function.
class ListCollaborationPrivacyBudgetsOutput(BaseValidatorModel):
    collaborationPrivacyBudgetSummaries: List[CollaborationPrivacyBudgetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_privacy_budgets' function.
class ListPrivacyBudgetsOutput(BaseValidatorModel):
    privacyBudgetSummaries: List[PrivacyBudgetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'batch_get_schema' function.
class BatchGetSchemaOutput(BaseValidatorModel):
    schemas: List[Schema]
    errors: List[BatchGetSchemaError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_schema' function.
class GetSchemaOutput(BaseValidatorModel):
    schema: Schema
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_collaboration' function.
class CreateCollaborationInput(BaseValidatorModel):
    members: List[MemberSpecification]
    name: str
    description: str
    creatorMemberAbilities: List[MemberAbilityType]
    creatorDisplayName: str
    queryLogStatus: CollaborationQueryLogStatusType
    creatorMLMemberAbilities: Optional[MLMemberAbilitiesUnion] = None
    dataEncryptionMetadata: Optional[DataEncryptionMetadata] = None
    tags: Optional[Dict[str, str]] = None
    creatorPaymentConfiguration: Optional[PaymentConfiguration] = None
    analyticsEngine: Optional[AnalyticsEngineType] = None


# This class is the output for the 'list_members' function.
class ListMembersOutput(BaseValidatorModel):
    memberSummaries: List[MemberSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_memberships' function.
class ListMembershipsOutput(BaseValidatorModel):
    membershipSummaries: List[MembershipSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_membership' function.
class CreateMembershipOutput(BaseValidatorModel):
    membership: Membership
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_membership' function.
class GetMembershipOutput(BaseValidatorModel):
    membership: Membership
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_membership' function.
class UpdateMembershipOutput(BaseValidatorModel):
    membership: Membership
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_protected_query' function.
class GetProtectedQueryOutput(BaseValidatorModel):
    protectedQuery: ProtectedQuery
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_protected_query' function.
class StartProtectedQueryOutput(BaseValidatorModel):
    protectedQuery: ProtectedQuery
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_protected_query' function.
class UpdateProtectedQueryOutput(BaseValidatorModel):
    protectedQuery: ProtectedQuery
    ResponseMetadata: ResponseMetadata


class AnalysisRulePolicy(BaseValidatorModel):
    v1: Optional[AnalysisRulePolicyV1] = None


class ConfiguredTable(BaseValidatorModel):
    id: str
    arn: str
    name: str
    tableReference: TableReferenceOutput
    createTime: datetime
    updateTime: datetime
    analysisRuleTypes: List[ConfiguredTableAnalysisRuleTypeType]
    analysisMethod: Literal['DIRECT_QUERY']
    allowedColumns: List[str]
    description: Optional[str] = None

TableReferenceUnion = Union[TableReference, TableReferenceOutput]


class ConfiguredTableAnalysisRule(BaseValidatorModel):
    configuredTableId: str
    configuredTableArn: str
    policy: ConfiguredTableAnalysisRulePolicyOutput
    type: ConfiguredTableAnalysisRuleTypeType
    createTime: datetime
    updateTime: datetime

ConfiguredTableAnalysisRulePolicyUnion = Union[ConfiguredTableAnalysisRulePolicy, ConfiguredTableAnalysisRulePolicyOutput]


class AnalysisRule(BaseValidatorModel):
    collaborationId: str
    type: AnalysisRuleTypeType
    name: str
    createTime: datetime
    updateTime: datetime
    policy: AnalysisRulePolicy


# This class is the output for the 'create_configured_table' function.
class CreateConfiguredTableOutput(BaseValidatorModel):
    configuredTable: ConfiguredTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_configured_table' function.
class GetConfiguredTableOutput(BaseValidatorModel):
    configuredTable: ConfiguredTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_configured_table' function.
class UpdateConfiguredTableOutput(BaseValidatorModel):
    configuredTable: ConfiguredTable
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_configured_table' function.
class CreateConfiguredTableInput(BaseValidatorModel):
    name: str
    tableReference: TableReferenceUnion
    allowedColumns: List[str]
    analysisMethod: Literal['DIRECT_QUERY']
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_configured_table_analysis_rule' function.
class CreateConfiguredTableAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_configured_table_analysis_rule' function.
class GetConfiguredTableAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_configured_table_analysis_rule' function.
class UpdateConfiguredTableAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRule
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_configured_table_analysis_rule' function.
class CreateConfiguredTableAnalysisRuleInput(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnion


# This class is the input for the 'update_configured_table_analysis_rule' function.
class UpdateConfiguredTableAnalysisRuleInput(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnion


# This class is the output for the 'batch_get_schema_analysis_rule' function.
class BatchGetSchemaAnalysisRuleOutput(BaseValidatorModel):
    analysisRules: List[AnalysisRule]
    errors: List[BatchGetSchemaAnalysisRuleError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_schema_analysis_rule' function.
class GetSchemaAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: AnalysisRule
    ResponseMetadata: ResponseMetadata