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
from aws_resource_validator.pydantic_models.cleanrooms_constants import *

class AggregateColumnOutput(BaseValidatorModel):
    columnNames: List[str]
    function: AggregateFunctionNameType


class AggregateColumn(BaseValidatorModel):
    columnNames: Sequence[str]
    function: AggregateFunctionNameType


class AnalysisRuleListOutput(BaseValidatorModel):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisRuleList(BaseValidatorModel):
    joinColumns: Sequence[str]
    listColumns: Sequence[str]
    allowedJoinOperators: Optional[Sequence[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisSchema(BaseValidatorModel):
    referencedTables: Optional[List[str]] = None


class AnalysisSource(BaseValidatorModel):
    text: Optional[str] = None


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


class BatchGetCollaborationAnalysisTemplateInput(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArns: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetSchemaError(BaseValidatorModel):
    name: str
    code: str
    message: str


class BatchGetSchemaInput(BaseValidatorModel):
    collaborationIdentifier: str
    names: Sequence[str]


class BilledResourceUtilization(BaseValidatorModel):
    units: float


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


class DataEncryptionMetadata(BaseValidatorModel):
    allowCleartext: bool
    allowDuplicates: bool
    allowJoinsOnColumnsWithDifferentNames: bool
    preserveNulls: bool


class DirectAnalysisConfigurationDetails(BaseValidatorModel):
    receiverAccountIds: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleAggregationOutput(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleAggregation(BaseValidatorModel):
    allowedResultReceivers: Optional[Sequence[str]] = None
    allowedAdditionalAnalyses: Optional[Sequence[str]] = None


class ConfiguredTableAssociationAnalysisRuleCustomOutput(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleCustom(BaseValidatorModel):
    allowedResultReceivers: Optional[Sequence[str]] = None
    allowedAdditionalAnalyses: Optional[Sequence[str]] = None


class ConfiguredTableAssociationAnalysisRuleListOutput(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleList(BaseValidatorModel):
    allowedResultReceivers: Optional[Sequence[str]] = None
    allowedAdditionalAnalyses: Optional[Sequence[str]] = None


class CreateConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredAudienceModelArn: str
    configuredAudienceModelAssociationName: str
    manageResourcePolicies: bool
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None


class CreateConfiguredTableAssociationInput(BaseValidatorModel):
    name: str
    membershipIdentifier: str
    configuredTableIdentifier: str
    roleArn: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


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


class DifferentialPrivacyPreviewParametersInput(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateParametersInput(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateParametersOutput(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateUpdateParameters(BaseValidatorModel):
    epsilon: Optional[int] = None
    usersNoisePerQuery: Optional[int] = None


class GetAnalysisTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str


class GetCollaborationAnalysisTemplateInput(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArn: str


class GetCollaborationConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    collaborationIdentifier: str
    configuredAudienceModelAssociationIdentifier: str


class GetCollaborationIdNamespaceAssociationInput(BaseValidatorModel):
    collaborationIdentifier: str
    idNamespaceAssociationIdentifier: str


class GetCollaborationInput(BaseValidatorModel):
    collaborationIdentifier: str


class GetCollaborationPrivacyBudgetTemplateInput(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetTemplateIdentifier: str


class GetConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str


class GetConfiguredTableAnalysisRuleInput(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType


class GetConfiguredTableAssociationAnalysisRuleInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType


class GetConfiguredTableAssociationInput(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str


class GetConfiguredTableInput(BaseValidatorModel):
    configuredTableIdentifier: str


class GetIdMappingTableInput(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str


class GetIdNamespaceAssociationInput(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str


class GetMembershipInput(BaseValidatorModel):
    membershipIdentifier: str


class GetPrivacyBudgetTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str


class GetProtectedQueryInput(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str


class GetSchemaInput(BaseValidatorModel):
    collaborationIdentifier: str
    name: str


class GlueTableReference(BaseValidatorModel):
    tableName: str
    databaseName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAnalysisTemplatesInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationAnalysisTemplatesInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationConfiguredAudienceModelAssociationsInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationIdNamespaceAssociationsInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationPrivacyBudgetTemplatesInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationPrivacyBudgetsInput(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCollaborationsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    memberStatus: Optional[FilterableMemberStatusType] = None


class ListConfiguredAudienceModelAssociationsInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredTableAssociationsInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredTablesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListIdMappingTablesInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListIdNamespaceAssociationsInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMembersInput(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMembershipsInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[MembershipStatusType] = None


class ListPrivacyBudgetTemplatesInput(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPrivacyBudgetsInput(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProtectedQueriesInput(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSchemasInput(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[SchemaTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class MLMemberAbilitiesOutput(BaseValidatorModel):
    customMLMemberAbilities: List[CustomMLMemberAbilityType]


class MLMemberAbilities(BaseValidatorModel):
    customMLMemberAbilities: Sequence[CustomMLMemberAbilityType]


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
    parameters: Optional[Mapping[str, str]] = None


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
    tags: Mapping[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAnalysisTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str
    description: Optional[str] = None


class UpdateCollaborationInput(BaseValidatorModel):
    collaborationIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None


class UpdateConfiguredAudienceModelAssociationInput(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    name: Optional[str] = None


class UpdateConfiguredTableAssociationInput(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    roleArn: Optional[str] = None


class UpdateConfiguredTableInput(BaseValidatorModel):
    configuredTableIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None


class UpdateIdMappingTableInput(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None


class UpdateProtectedQueryInput(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str
    targetStatus: Literal["CANCELLED"]


class AggregationConstraint(BaseValidatorModel):
    pass


class AnalysisRuleAggregationOutput(BaseValidatorModel):
    aggregateColumns: List[AggregateColumnOutput]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraint]
    joinRequired: Optional[Literal["QUERY_RUNNER"]] = None
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisRuleAggregation(BaseValidatorModel):
    aggregateColumns: Sequence[AggregateColumn]
    joinColumns: Sequence[str]
    dimensionColumns: Sequence[str]
    scalarFunctions: Sequence[ScalarFunctionsType]
    outputConstraints: Sequence[AggregationConstraint]
    joinRequired: Optional[Literal["QUERY_RUNNER"]] = None
    allowedJoinOperators: Optional[Sequence[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisTemplateSummary(BaseValidatorModel):
    pass


class ListAnalysisTemplatesOutput(BaseValidatorModel):
    analysisTemplateSummaries: List[AnalysisTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PopulateIdMappingTableOutput(BaseValidatorModel):
    idMappingJobId: str
    ResponseMetadata: ResponseMetadata


class SchemaAnalysisRuleRequest(BaseValidatorModel):
    pass


class BatchGetSchemaAnalysisRuleInput(BaseValidatorModel):
    collaborationIdentifier: str
    schemaAnalysisRuleRequests: Sequence[SchemaAnalysisRuleRequest]


class ProtectedQueryStatistics(BaseValidatorModel):
    totalDurationInMillis: Optional[int] = None
    billedResourceUtilization: Optional[BilledResourceUtilization] = None


class CollaborationAnalysisTemplateSummary(BaseValidatorModel):
    pass


class ListCollaborationAnalysisTemplatesOutput(BaseValidatorModel):
    collaborationAnalysisTemplateSummaries: List[CollaborationAnalysisTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CollaborationConfiguredAudienceModelAssociationSummary(BaseValidatorModel):
    pass


class ListCollaborationConfiguredAudienceModelAssociationsOutput(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociationSummaries: List[ CollaborationConfiguredAudienceModelAssociationSummary ]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CollaborationConfiguredAudienceModelAssociation(BaseValidatorModel):
    pass


class GetCollaborationConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociation: ( CollaborationConfiguredAudienceModelAssociation )
    ResponseMetadata: ResponseMetadata


class CreateIdNamespaceAssociationInput(BaseValidatorModel):
    membershipIdentifier: str
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfig
    name: str
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfig] = None


class UpdateIdNamespaceAssociationInput(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfig] = None


class CollaborationPrivacyBudgetTemplateSummary(BaseValidatorModel):
    pass


class ListCollaborationPrivacyBudgetTemplatesOutput(BaseValidatorModel):
    collaborationPrivacyBudgetTemplateSummaries: List[ CollaborationPrivacyBudgetTemplateSummary ]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CollaborationSummary(BaseValidatorModel):
    pass


class ListCollaborationsOutput(BaseValidatorModel):
    collaborationList: List[CollaborationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class WorkerComputeConfiguration(BaseValidatorModel):
    pass


class ComputeConfiguration(BaseValidatorModel):
    worker: Optional[WorkerComputeConfiguration] = None


class ConfigurationDetails(BaseValidatorModel):
    directAnalysisConfigurationDetails: Optional[DirectAnalysisConfigurationDetails] = None


class ConfiguredAudienceModelAssociationSummary(BaseValidatorModel):
    pass


class ListConfiguredAudienceModelAssociationsOutput(BaseValidatorModel):
    configuredAudienceModelAssociationSummaries: List[ ConfiguredAudienceModelAssociationSummary ]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConfiguredAudienceModelAssociation(BaseValidatorModel):
    pass


class CreateConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociation
    ResponseMetadata: ResponseMetadata


class GetConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociation
    ResponseMetadata: ResponseMetadata


class UpdateConfiguredAudienceModelAssociationOutput(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociation
    ResponseMetadata: ResponseMetadata


class ConfiguredTableAssociationSummary(BaseValidatorModel):
    pass


class ListConfiguredTableAssociationsOutput(BaseValidatorModel):
    configuredTableAssociationSummaries: List[ConfiguredTableAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConfiguredTableAssociation(BaseValidatorModel):
    pass


class CreateConfiguredTableAssociationOutput(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociation
    ResponseMetadata: ResponseMetadata


class GetConfiguredTableAssociationOutput(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociation
    ResponseMetadata: ResponseMetadata


class UpdateConfiguredTableAssociationOutput(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociation
    ResponseMetadata: ResponseMetadata


class ConfiguredTableSummary(BaseValidatorModel):
    pass


class ListConfiguredTablesOutput(BaseValidatorModel):
    configuredTableSummaries: List[ConfiguredTableSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateIdMappingTableInput(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    inputReferenceConfig: IdMappingTableInputReferenceConfig
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None


class DifferentialPrivacyConfigurationOutput(BaseValidatorModel):
    columns: List[DifferentialPrivacyColumn]


class DifferentialPrivacyConfiguration(BaseValidatorModel):
    columns: Sequence[DifferentialPrivacyColumn]


class DifferentialPrivacyParameters(BaseValidatorModel):
    sensitivityParameters: List[DifferentialPrivacySensitivityParameters]


class DifferentialPrivacyPreviewAggregation(BaseValidatorModel):
    pass


class DifferentialPrivacyPrivacyImpact(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPreviewAggregation]


class PreviewPrivacyImpactParametersInput(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPreviewParametersInput] = None


class DifferentialPrivacyPrivacyBudgetAggregation(BaseValidatorModel):
    pass


class DifferentialPrivacyPrivacyBudget(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPrivacyBudgetAggregation]
    epsilon: int


class PrivacyBudgetTemplateParametersInput(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersInput] = None


class PrivacyBudgetTemplateParametersOutput(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersOutput] = None


class PrivacyBudgetTemplateUpdateParameters(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateUpdateParameters] = None


class IdMappingTableInputSource(BaseValidatorModel):
    pass


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
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
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
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProtectedQueriesInputPaginate(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemasInputPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[SchemaTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class PrivacyBudgetTemplateSummary(BaseValidatorModel):
    pass


class ListPrivacyBudgetTemplatesOutput(BaseValidatorModel):
    privacyBudgetTemplateSummaries: List[PrivacyBudgetTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SchemaSummary(BaseValidatorModel):
    pass


class ListSchemasOutput(BaseValidatorModel):
    schemaSummaries: List[SchemaSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class QueryConstraint(BaseValidatorModel):
    requireOverlap: Optional[QueryConstraintRequireOverlap] = None


class SchemaStatusDetail(BaseValidatorModel):
    status: SchemaStatusType
    analysisType: AnalysisTypeType
    reasons: Optional[List[SchemaStatusReason]] = None
    analysisRuleType: Optional[AnalysisRuleTypeType] = None
    configurations: Optional[List[Literal["DIFFERENTIAL_PRIVACY"]]] = None


class SnowflakeTableSchemaOutput(BaseValidatorModel):
    v1: Optional[List[SnowflakeTableSchemaV1]] = None


class SnowflakeTableSchema(BaseValidatorModel):
    v1: Optional[Sequence[SnowflakeTableSchemaV1]] = None


class CollaborationIdNamespaceAssociationSummary(BaseValidatorModel):
    pass


class ListCollaborationIdNamespaceAssociationsOutput(BaseValidatorModel):
    collaborationIdNamespaceAssociationSummaries: List[ CollaborationIdNamespaceAssociationSummary ]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IdNamespaceAssociationSummary(BaseValidatorModel):
    pass


class ListIdNamespaceAssociationsOutput(BaseValidatorModel):
    idNamespaceAssociationSummaries: List[IdNamespaceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CollaborationIdNamespaceAssociation(BaseValidatorModel):
    pass


class GetCollaborationIdNamespaceAssociationOutput(BaseValidatorModel):
    collaborationIdNamespaceAssociation: CollaborationIdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


class IdNamespaceAssociation(BaseValidatorModel):
    pass


class CreateIdNamespaceAssociationOutput(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


class GetIdNamespaceAssociationOutput(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


class UpdateIdNamespaceAssociationOutput(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociation
    ResponseMetadata: ResponseMetadata


class Collaboration(BaseValidatorModel):
    pass


class CreateCollaborationOutput(BaseValidatorModel):
    collaboration: Collaboration
    ResponseMetadata: ResponseMetadata


class GetCollaborationOutput(BaseValidatorModel):
    collaboration: Collaboration
    ResponseMetadata: ResponseMetadata


class UpdateCollaborationOutput(BaseValidatorModel):
    collaboration: Collaboration
    ResponseMetadata: ResponseMetadata


class ReceiverConfiguration(BaseValidatorModel):
    analysisType: AnalysisTypeType
    configurationDetails: Optional[ConfigurationDetails] = None


class ConfiguredTableAssociationAnalysisRulePolicyV1Output(BaseValidatorModel):
    pass


class ConfiguredTableAssociationAnalysisRulePolicyOutput(BaseValidatorModel):
    v1: Optional[ConfiguredTableAssociationAnalysisRulePolicyV1Output] = None


class ConfiguredTableAssociationAnalysisRulePolicyV1(BaseValidatorModel):
    pass


class ConfiguredTableAssociationAnalysisRulePolicy(BaseValidatorModel):
    v1: Optional[ConfiguredTableAssociationAnalysisRulePolicyV1] = None


class IdMappingTableSummary(BaseValidatorModel):
    pass


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
    allowedAnalyses: Sequence[str]
    allowedAnalysisProviders: Optional[Sequence[str]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None
    disallowedOutputColumns: Optional[Sequence[str]] = None
    differentialPrivacy: Optional[DifferentialPrivacyConfiguration] = None


class PrivacyImpact(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyImpact] = None


class PreviewPrivacyImpactInput(BaseValidatorModel):
    membershipIdentifier: str
    parameters: PreviewPrivacyImpactParametersInput


class PrivacyBudget(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyBudget] = None


class CreatePrivacyBudgetTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: PrivacyBudgetTemplateParametersInput
    tags: Optional[Mapping[str, str]] = None


class UpdatePrivacyBudgetTemplateInput(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: Optional[PrivacyBudgetTemplateUpdateParameters] = None


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


class AnalysisTemplate(BaseValidatorModel):
    pass


class CreateAnalysisTemplateOutput(BaseValidatorModel):
    analysisTemplate: AnalysisTemplate
    ResponseMetadata: ResponseMetadata


class GetAnalysisTemplateOutput(BaseValidatorModel):
    analysisTemplate: AnalysisTemplate
    ResponseMetadata: ResponseMetadata


class UpdateAnalysisTemplateOutput(BaseValidatorModel):
    analysisTemplate: AnalysisTemplate
    ResponseMetadata: ResponseMetadata


class CollaborationAnalysisTemplate(BaseValidatorModel):
    pass


class BatchGetCollaborationAnalysisTemplateOutput(BaseValidatorModel):
    collaborationAnalysisTemplates: List[CollaborationAnalysisTemplate]
    errors: List[BatchGetCollaborationAnalysisTemplateError]
    ResponseMetadata: ResponseMetadata


class GetCollaborationAnalysisTemplateOutput(BaseValidatorModel):
    collaborationAnalysisTemplate: CollaborationAnalysisTemplate
    ResponseMetadata: ResponseMetadata


class PreviewPrivacyImpactOutput(BaseValidatorModel):
    privacyImpact: PrivacyImpact
    ResponseMetadata: ResponseMetadata


class CollaborationPrivacyBudgetTemplate(BaseValidatorModel):
    pass


class GetCollaborationPrivacyBudgetTemplateOutput(BaseValidatorModel):
    collaborationPrivacyBudgetTemplate: CollaborationPrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


class PrivacyBudgetTemplate(BaseValidatorModel):
    pass


class CreatePrivacyBudgetTemplateOutput(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


class GetPrivacyBudgetTemplateOutput(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


class UpdatePrivacyBudgetTemplateOutput(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplate
    ResponseMetadata: ResponseMetadata


class IdMappingTable(BaseValidatorModel):
    pass


class CreateIdMappingTableOutput(BaseValidatorModel):
    idMappingTable: IdMappingTable
    ResponseMetadata: ResponseMetadata


class GetIdMappingTableOutput(BaseValidatorModel):
    idMappingTable: IdMappingTable
    ResponseMetadata: ResponseMetadata


class UpdateIdMappingTableOutput(BaseValidatorModel):
    idMappingTable: IdMappingTable
    ResponseMetadata: ResponseMetadata


class MLMemberAbilitiesUnion(BaseValidatorModel):
    pass


class MemberSpecification(BaseValidatorModel):
    accountId: str
    memberAbilities: Sequence[MemberAbilityType]
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


class CreateMembershipInput(BaseValidatorModel):
    collaborationIdentifier: str
    queryLogStatus: MembershipQueryLogStatusType
    tags: Optional[Mapping[str, str]] = None
    defaultResultConfiguration: Optional[MembershipProtectedQueryResultConfiguration] = None
    paymentConfiguration: Optional[MembershipPaymentConfiguration] = None


class UpdateMembershipInput(BaseValidatorModel):
    membershipIdentifier: str
    queryLogStatus: Optional[MembershipQueryLogStatusType] = None
    defaultResultConfiguration: Optional[MembershipProtectedQueryResultConfiguration] = None


class TableReferenceOutput(BaseValidatorModel):
    glue: Optional[GlueTableReference] = None
    snowflake: Optional[SnowflakeTableReferenceOutput] = None
    athena: Optional[AthenaTableReference] = None


class TableReference(BaseValidatorModel):
    glue: Optional[GlueTableReference] = None
    snowflake: Optional[SnowflakeTableReference] = None
    athena: Optional[AthenaTableReference] = None


class ProtectedQuerySummary(BaseValidatorModel):
    pass


class ListProtectedQueriesOutput(BaseValidatorModel):
    protectedQueries: List[ProtectedQuerySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConfiguredTableAssociationAnalysisRule(BaseValidatorModel):
    pass


class CreateConfiguredTableAssociationAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRule
    ResponseMetadata: ResponseMetadata


class GetConfiguredTableAssociationAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRule
    ResponseMetadata: ResponseMetadata


class UpdateConfiguredTableAssociationAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRule
    ResponseMetadata: ResponseMetadata


class ConfiguredTableAssociationAnalysisRulePolicyUnion(BaseValidatorModel):
    pass


class CreateConfiguredTableAssociationAnalysisRuleInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnion


class UpdateConfiguredTableAssociationAnalysisRuleInput(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnion


class ConfiguredTableAnalysisRulePolicyV1Output(BaseValidatorModel):
    pass


class ConfiguredTableAnalysisRulePolicyOutput(BaseValidatorModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1Output] = None


class ConfiguredTableAnalysisRulePolicyV1(BaseValidatorModel):
    pass


class ConfiguredTableAnalysisRulePolicy(BaseValidatorModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1] = None


class CollaborationPrivacyBudgetSummary(BaseValidatorModel):
    pass


class ListCollaborationPrivacyBudgetsOutput(BaseValidatorModel):
    collaborationPrivacyBudgetSummaries: List[CollaborationPrivacyBudgetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PrivacyBudgetSummary(BaseValidatorModel):
    pass


class ListPrivacyBudgetsOutput(BaseValidatorModel):
    privacyBudgetSummaries: List[PrivacyBudgetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Schema(BaseValidatorModel):
    pass


class BatchGetSchemaOutput(BaseValidatorModel):
    schemas: List[Schema]
    errors: List[BatchGetSchemaError]
    ResponseMetadata: ResponseMetadata


class GetSchemaOutput(BaseValidatorModel):
    schema: Schema
    ResponseMetadata: ResponseMetadata


class CreateCollaborationInput(BaseValidatorModel):
    members: Sequence[MemberSpecification]
    name: str
    description: str
    creatorMemberAbilities: Sequence[MemberAbilityType]
    creatorDisplayName: str
    queryLogStatus: CollaborationQueryLogStatusType
    creatorMLMemberAbilities: Optional[MLMemberAbilitiesUnion] = None
    dataEncryptionMetadata: Optional[DataEncryptionMetadata] = None
    tags: Optional[Mapping[str, str]] = None
    creatorPaymentConfiguration: Optional[PaymentConfiguration] = None
    analyticsEngine: Optional[AnalyticsEngineType] = None


class ListMembersOutput(BaseValidatorModel):
    memberSummaries: List[MemberSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MembershipSummary(BaseValidatorModel):
    pass


class ListMembershipsOutput(BaseValidatorModel):
    membershipSummaries: List[MembershipSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Membership(BaseValidatorModel):
    pass


class CreateMembershipOutput(BaseValidatorModel):
    membership: Membership
    ResponseMetadata: ResponseMetadata


class GetMembershipOutput(BaseValidatorModel):
    membership: Membership
    ResponseMetadata: ResponseMetadata


class UpdateMembershipOutput(BaseValidatorModel):
    membership: Membership
    ResponseMetadata: ResponseMetadata


class ProtectedQuery(BaseValidatorModel):
    pass


class GetProtectedQueryOutput(BaseValidatorModel):
    protectedQuery: ProtectedQuery
    ResponseMetadata: ResponseMetadata


class StartProtectedQueryOutput(BaseValidatorModel):
    protectedQuery: ProtectedQuery
    ResponseMetadata: ResponseMetadata


class UpdateProtectedQueryOutput(BaseValidatorModel):
    protectedQuery: ProtectedQuery
    ResponseMetadata: ResponseMetadata


class AnalysisRulePolicyV1(BaseValidatorModel):
    pass


class AnalysisRulePolicy(BaseValidatorModel):
    v1: Optional[AnalysisRulePolicyV1] = None


class ConfiguredTable(BaseValidatorModel):
    pass


class CreateConfiguredTableOutput(BaseValidatorModel):
    configuredTable: ConfiguredTable
    ResponseMetadata: ResponseMetadata


class GetConfiguredTableOutput(BaseValidatorModel):
    configuredTable: ConfiguredTable
    ResponseMetadata: ResponseMetadata


class UpdateConfiguredTableOutput(BaseValidatorModel):
    configuredTable: ConfiguredTable
    ResponseMetadata: ResponseMetadata


class TableReferenceUnion(BaseValidatorModel):
    pass


class CreateConfiguredTableInput(BaseValidatorModel):
    name: str
    tableReference: TableReferenceUnion
    allowedColumns: Sequence[str]
    analysisMethod: Literal["DIRECT_QUERY"]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ConfiguredTableAnalysisRule(BaseValidatorModel):
    pass


class CreateConfiguredTableAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRule
    ResponseMetadata: ResponseMetadata


class GetConfiguredTableAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRule
    ResponseMetadata: ResponseMetadata


class UpdateConfiguredTableAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRule
    ResponseMetadata: ResponseMetadata


class ConfiguredTableAnalysisRulePolicyUnion(BaseValidatorModel):
    pass


class CreateConfiguredTableAnalysisRuleInput(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnion


class UpdateConfiguredTableAnalysisRuleInput(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnion


class BatchGetSchemaAnalysisRuleError(BaseValidatorModel):
    pass


class AnalysisRule(BaseValidatorModel):
    pass


class BatchGetSchemaAnalysisRuleOutput(BaseValidatorModel):
    analysisRules: List[AnalysisRule]
    errors: List[BatchGetSchemaAnalysisRuleError]
    ResponseMetadata: ResponseMetadata


class GetSchemaAnalysisRuleOutput(BaseValidatorModel):
    analysisRule: AnalysisRule
    ResponseMetadata: ResponseMetadata


