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

class AggregateColumnOutputTypeDef(BaseValidatorModel):
    columnNames: List[str]
    function: AggregateFunctionNameType


class AggregateColumnTypeDef(BaseValidatorModel):
    columnNames: Sequence[str]
    function: AggregateFunctionNameType


class AnalysisRuleListOutputTypeDef(BaseValidatorModel):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisRuleListTypeDef(BaseValidatorModel):
    joinColumns: Sequence[str]
    listColumns: Sequence[str]
    allowedJoinOperators: Optional[Sequence[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisSchemaTypeDef(BaseValidatorModel):
    referencedTables: Optional[List[str]] = None


class AnalysisSourceTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class AnalysisTemplateValidationStatusReasonTypeDef(BaseValidatorModel):
    message: str


class AthenaTableReferenceTypeDef(BaseValidatorModel):
    workGroup: str
    databaseName: str
    tableName: str
    outputLocation: Optional[str] = None


class BatchGetCollaborationAnalysisTemplateErrorTypeDef(BaseValidatorModel):
    arn: str
    code: str
    message: str


class BatchGetCollaborationAnalysisTemplateInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArns: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetSchemaErrorTypeDef(BaseValidatorModel):
    name: str
    code: str
    message: str


class BatchGetSchemaInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    names: Sequence[str]


class BilledResourceUtilizationTypeDef(BaseValidatorModel):
    units: float


class IdNamespaceAssociationInputReferenceConfigTypeDef(BaseValidatorModel):
    inputReferenceArn: str
    manageResourcePolicies: bool


class IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef(BaseValidatorModel):
    idNamespaceType: IdNamespaceTypeType


class IdMappingConfigTypeDef(BaseValidatorModel):
    allowUseAsDimensionColumn: bool


class IdNamespaceAssociationInputReferencePropertiesTypeDef(BaseValidatorModel):
    idNamespaceType: IdNamespaceTypeType
    idMappingWorkflowsSupported: List[Dict[str, Any]]


class DataEncryptionMetadataTypeDef(BaseValidatorModel):
    allowCleartext: bool
    allowDuplicates: bool
    allowJoinsOnColumnsWithDifferentNames: bool
    preserveNulls: bool


class DirectAnalysisConfigurationDetailsTypeDef(BaseValidatorModel):
    receiverAccountIds: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleAggregationTypeDef(BaseValidatorModel):
    allowedResultReceivers: Optional[Sequence[str]] = None
    allowedAdditionalAnalyses: Optional[Sequence[str]] = None


class ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleCustomTypeDef(BaseValidatorModel):
    allowedResultReceivers: Optional[Sequence[str]] = None
    allowedAdditionalAnalyses: Optional[Sequence[str]] = None


class ConfiguredTableAssociationAnalysisRuleListOutputTypeDef(BaseValidatorModel):
    allowedResultReceivers: Optional[List[str]] = None
    allowedAdditionalAnalyses: Optional[List[str]] = None


class ConfiguredTableAssociationAnalysisRuleListTypeDef(BaseValidatorModel):
    allowedResultReceivers: Optional[Sequence[str]] = None
    allowedAdditionalAnalyses: Optional[Sequence[str]] = None


class CreateConfiguredAudienceModelAssociationInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredAudienceModelArn: str
    configuredAudienceModelAssociationName: str
    manageResourcePolicies: bool
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None


class CreateConfiguredTableAssociationInputTypeDef(BaseValidatorModel):
    name: str
    membershipIdentifier: str
    configuredTableIdentifier: str
    roleArn: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class IdMappingTableInputReferenceConfigTypeDef(BaseValidatorModel):
    inputReferenceArn: str
    manageResourcePolicies: bool


class DeleteAnalysisTemplateInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str


class DeleteCollaborationInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str


class DeleteConfiguredAudienceModelAssociationInputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str


class DeleteConfiguredTableAnalysisRuleInputTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType


class DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType


class DeleteConfiguredTableAssociationInputTypeDef(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str


class DeleteConfiguredTableInputTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str


class DeleteIdMappingTableInputTypeDef(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str


class DeleteIdNamespaceAssociationInputTypeDef(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str


class DeleteMemberInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    accountId: str


class DeleteMembershipInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str


class DeletePrivacyBudgetTemplateInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str


class DifferentialPrivacyColumnTypeDef(BaseValidatorModel):
    name: str


class DifferentialPrivacySensitivityParametersTypeDef(BaseValidatorModel):
    aggregationType: DifferentialPrivacyAggregationTypeType
    aggregationExpression: str
    userContributionLimit: int
    minColumnValue: Optional[float] = None
    maxColumnValue: Optional[float] = None


class DifferentialPrivacyPreviewParametersInputTypeDef(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateParametersInputTypeDef(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateParametersOutputTypeDef(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int


class DifferentialPrivacyTemplateUpdateParametersTypeDef(BaseValidatorModel):
    epsilon: Optional[int] = None
    usersNoisePerQuery: Optional[int] = None


class GetAnalysisTemplateInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str


class GetCollaborationAnalysisTemplateInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArn: str


class GetCollaborationConfiguredAudienceModelAssociationInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    configuredAudienceModelAssociationIdentifier: str


class GetCollaborationIdNamespaceAssociationInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    idNamespaceAssociationIdentifier: str


class GetCollaborationInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str


class GetCollaborationPrivacyBudgetTemplateInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetTemplateIdentifier: str


class GetConfiguredAudienceModelAssociationInputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str


class GetConfiguredTableAnalysisRuleInputTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType


class GetConfiguredTableAssociationAnalysisRuleInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType


class GetConfiguredTableAssociationInputTypeDef(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str


class GetConfiguredTableInputTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str


class GetIdMappingTableInputTypeDef(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str


class GetIdNamespaceAssociationInputTypeDef(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str


class GetMembershipInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str


class GetPrivacyBudgetTemplateInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str


class GetProtectedQueryInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str


class GetSchemaInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    name: str


class GlueTableReferenceTypeDef(BaseValidatorModel):
    tableName: str
    databaseName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAnalysisTemplatesInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationAnalysisTemplatesInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationIdNamespaceAssociationsInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationPrivacyBudgetTemplatesInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationPrivacyBudgetsInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCollaborationsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    memberStatus: Optional[FilterableMemberStatusType] = None


class ListConfiguredAudienceModelAssociationsInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredTableAssociationsInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredTablesInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListIdMappingTablesInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListIdNamespaceAssociationsInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMembersInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMembershipsInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[MembershipStatusType] = None


class ListPrivacyBudgetTemplatesInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPrivacyBudgetsInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProtectedQueriesInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSchemasInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[SchemaTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class MLMemberAbilitiesOutputTypeDef(BaseValidatorModel):
    customMLMemberAbilities: List[CustomMLMemberAbilityType]


class MLMemberAbilitiesTypeDef(BaseValidatorModel):
    customMLMemberAbilities: Sequence[CustomMLMemberAbilityType]


class ModelInferencePaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool


class ModelTrainingPaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool


class MembershipModelInferencePaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool


class MembershipModelTrainingPaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool


class MembershipQueryComputePaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool


class ProtectedQueryS3OutputConfigurationTypeDef(BaseValidatorModel):
    resultFormat: ResultFormatType
    bucket: str
    keyPrefix: Optional[str] = None
    singleFileOutput: Optional[bool] = None


class QueryComputePaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool


class PopulateIdMappingTableInputTypeDef(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str


class ProtectedQueryErrorTypeDef(BaseValidatorModel):
    message: str
    code: str


class ProtectedQueryMemberOutputConfigurationTypeDef(BaseValidatorModel):
    accountId: str


class ProtectedQueryS3OutputTypeDef(BaseValidatorModel):
    location: str


class ProtectedQuerySingleMemberOutputTypeDef(BaseValidatorModel):
    accountId: str


class ProtectedQuerySQLParametersOutputTypeDef(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class ProtectedQuerySQLParametersTypeDef(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None


class QueryConstraintRequireOverlapTypeDef(BaseValidatorModel):
    columns: Optional[List[str]] = None


class SchemaStatusReasonTypeDef(BaseValidatorModel):
    code: SchemaStatusReasonCodeType
    message: str


class SnowflakeTableSchemaV1TypeDef(BaseValidatorModel):
    columnName: str
    columnType: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAnalysisTemplateInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str
    description: Optional[str] = None


class UpdateCollaborationInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None


class UpdateConfiguredAudienceModelAssociationInputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    name: Optional[str] = None


class UpdateConfiguredTableAssociationInputTypeDef(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    roleArn: Optional[str] = None


class UpdateConfiguredTableInputTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None


class UpdateIdMappingTableInputTypeDef(BaseValidatorModel):
    idMappingTableIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None


class UpdateProtectedQueryInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str
    targetStatus: Literal["CANCELLED"]


class AggregationConstraintTypeDef(BaseValidatorModel):
    pass


class AnalysisRuleAggregationOutputTypeDef(BaseValidatorModel):
    aggregateColumns: List[AggregateColumnOutputTypeDef]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraintTypeDef]
    joinRequired: Optional[Literal["QUERY_RUNNER"]] = None
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisRuleAggregationTypeDef(BaseValidatorModel):
    aggregateColumns: Sequence[AggregateColumnTypeDef]
    joinColumns: Sequence[str]
    dimensionColumns: Sequence[str]
    scalarFunctions: Sequence[ScalarFunctionsType]
    outputConstraints: Sequence[AggregationConstraintTypeDef]
    joinRequired: Optional[Literal["QUERY_RUNNER"]] = None
    allowedJoinOperators: Optional[Sequence[JoinOperatorType]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None


class AnalysisTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListAnalysisTemplatesOutputTypeDef(BaseValidatorModel):
    analysisTemplateSummaries: List[AnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PopulateIdMappingTableOutputTypeDef(BaseValidatorModel):
    idMappingJobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class SchemaAnalysisRuleRequestTypeDef(BaseValidatorModel):
    pass


class BatchGetSchemaAnalysisRuleInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    schemaAnalysisRuleRequests: Sequence[SchemaAnalysisRuleRequestTypeDef]


class ProtectedQueryStatisticsTypeDef(BaseValidatorModel):
    totalDurationInMillis: Optional[int] = None
    billedResourceUtilization: Optional[BilledResourceUtilizationTypeDef] = None


class CollaborationAnalysisTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListCollaborationAnalysisTemplatesOutputTypeDef(BaseValidatorModel):
    collaborationAnalysisTemplateSummaries: List[CollaborationAnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CollaborationConfiguredAudienceModelAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociationSummaries: List[ CollaborationConfiguredAudienceModelAssociationSummaryTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CollaborationConfiguredAudienceModelAssociationTypeDef(BaseValidatorModel):
    pass


class GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociation: ( CollaborationConfiguredAudienceModelAssociationTypeDef )
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIdNamespaceAssociationInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    inputReferenceConfig: IdNamespaceAssociationInputReferenceConfigTypeDef
    name: str
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfigTypeDef] = None


class UpdateIdNamespaceAssociationInputTypeDef(BaseValidatorModel):
    idNamespaceAssociationIdentifier: str
    membershipIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None
    idMappingConfig: Optional[IdMappingConfigTypeDef] = None


class CollaborationPrivacyBudgetTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListCollaborationPrivacyBudgetTemplatesOutputTypeDef(BaseValidatorModel):
    collaborationPrivacyBudgetTemplateSummaries: List[ CollaborationPrivacyBudgetTemplateSummaryTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CollaborationSummaryTypeDef(BaseValidatorModel):
    pass


class ListCollaborationsOutputTypeDef(BaseValidatorModel):
    collaborationList: List[CollaborationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkerComputeConfigurationTypeDef(BaseValidatorModel):
    pass


class ComputeConfigurationTypeDef(BaseValidatorModel):
    worker: Optional[WorkerComputeConfigurationTypeDef] = None


class ConfigurationDetailsTypeDef(BaseValidatorModel):
    directAnalysisConfigurationDetails: Optional[DirectAnalysisConfigurationDetailsTypeDef] = None


class ConfiguredAudienceModelAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListConfiguredAudienceModelAssociationsOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationSummaries: List[ ConfiguredAudienceModelAssociationSummaryTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConfiguredAudienceModelAssociationTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConfiguredTableAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListConfiguredTableAssociationsOutputTypeDef(BaseValidatorModel):
    configuredTableAssociationSummaries: List[ConfiguredTableAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConfiguredTableAssociationTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredTableAssociationOutputTypeDef(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfiguredTableAssociationOutputTypeDef(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfiguredTableAssociationOutputTypeDef(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConfiguredTableSummaryTypeDef(BaseValidatorModel):
    pass


class ListConfiguredTablesOutputTypeDef(BaseValidatorModel):
    configuredTableSummaries: List[ConfiguredTableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateIdMappingTableInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    inputReferenceConfig: IdMappingTableInputReferenceConfigTypeDef
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None


class DifferentialPrivacyConfigurationOutputTypeDef(BaseValidatorModel):
    columns: List[DifferentialPrivacyColumnTypeDef]


class DifferentialPrivacyConfigurationTypeDef(BaseValidatorModel):
    columns: Sequence[DifferentialPrivacyColumnTypeDef]


class DifferentialPrivacyParametersTypeDef(BaseValidatorModel):
    sensitivityParameters: List[DifferentialPrivacySensitivityParametersTypeDef]


class DifferentialPrivacyPreviewAggregationTypeDef(BaseValidatorModel):
    pass


class DifferentialPrivacyPrivacyImpactTypeDef(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPreviewAggregationTypeDef]


class PreviewPrivacyImpactParametersInputTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPreviewParametersInputTypeDef] = None


class DifferentialPrivacyPrivacyBudgetAggregationTypeDef(BaseValidatorModel):
    pass


class DifferentialPrivacyPrivacyBudgetTypeDef(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPrivacyBudgetAggregationTypeDef]
    epsilon: int


class PrivacyBudgetTemplateParametersInputTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersInputTypeDef] = None


class PrivacyBudgetTemplateParametersOutputTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersOutputTypeDef] = None


class PrivacyBudgetTemplateUpdateParametersTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateUpdateParametersTypeDef] = None


class IdMappingTableInputSourceTypeDef(BaseValidatorModel):
    pass


class IdMappingTableInputReferencePropertiesTypeDef(BaseValidatorModel):
    idMappingTableInputSource: List[IdMappingTableInputSourceTypeDef]


class IdMappingTableSchemaTypePropertiesTypeDef(BaseValidatorModel):
    idMappingTableInputSource: List[IdMappingTableInputSourceTypeDef]


class ListAnalysisTemplatesInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationAnalysisTemplatesInputPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationPrivacyBudgetsInputPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationsInputPaginateTypeDef(BaseValidatorModel):
    memberStatus: Optional[FilterableMemberStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfiguredAudienceModelAssociationsInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfiguredTableAssociationsInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfiguredTablesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIdMappingTablesInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIdNamespaceAssociationsInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembersInputPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMembershipsInputPaginateTypeDef(BaseValidatorModel):
    status: Optional[MembershipStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrivacyBudgetTemplatesInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrivacyBudgetsInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProtectedQueriesInputPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemasInputPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[SchemaTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PrivacyBudgetTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListPrivacyBudgetTemplatesOutputTypeDef(BaseValidatorModel):
    privacyBudgetTemplateSummaries: List[PrivacyBudgetTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SchemaSummaryTypeDef(BaseValidatorModel):
    pass


class ListSchemasOutputTypeDef(BaseValidatorModel):
    schemaSummaries: List[SchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MLPaymentConfigTypeDef(BaseValidatorModel):
    modelTraining: Optional[ModelTrainingPaymentConfigTypeDef] = None
    modelInference: Optional[ModelInferencePaymentConfigTypeDef] = None


class MembershipMLPaymentConfigTypeDef(BaseValidatorModel):
    modelTraining: Optional[MembershipModelTrainingPaymentConfigTypeDef] = None
    modelInference: Optional[MembershipModelInferencePaymentConfigTypeDef] = None


class MembershipProtectedQueryOutputConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputConfigurationTypeDef] = None


class ProtectedQueryOutputConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputConfigurationTypeDef] = None
    member: Optional[ProtectedQueryMemberOutputConfigurationTypeDef] = None


class ProtectedQueryOutputTypeDef(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputTypeDef] = None
    memberList: Optional[List[ProtectedQuerySingleMemberOutputTypeDef]] = None


class QueryConstraintTypeDef(BaseValidatorModel):
    requireOverlap: Optional[QueryConstraintRequireOverlapTypeDef] = None


class SchemaStatusDetailTypeDef(BaseValidatorModel):
    status: SchemaStatusType
    analysisType: AnalysisTypeType
    reasons: Optional[List[SchemaStatusReasonTypeDef]] = None
    analysisRuleType: Optional[AnalysisRuleTypeType] = None
    configurations: Optional[List[Literal["DIFFERENTIAL_PRIVACY"]]] = None


class SnowflakeTableSchemaOutputTypeDef(BaseValidatorModel):
    v1: Optional[List[SnowflakeTableSchemaV1TypeDef]] = None


class SnowflakeTableSchemaTypeDef(BaseValidatorModel):
    v1: Optional[Sequence[SnowflakeTableSchemaV1TypeDef]] = None


class CollaborationIdNamespaceAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListCollaborationIdNamespaceAssociationsOutputTypeDef(BaseValidatorModel):
    collaborationIdNamespaceAssociationSummaries: List[ CollaborationIdNamespaceAssociationSummaryTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IdNamespaceAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListIdNamespaceAssociationsOutputTypeDef(BaseValidatorModel):
    idNamespaceAssociationSummaries: List[IdNamespaceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CollaborationIdNamespaceAssociationTypeDef(BaseValidatorModel):
    pass


class GetCollaborationIdNamespaceAssociationOutputTypeDef(BaseValidatorModel):
    collaborationIdNamespaceAssociation: CollaborationIdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IdNamespaceAssociationTypeDef(BaseValidatorModel):
    pass


class CreateIdNamespaceAssociationOutputTypeDef(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIdNamespaceAssociationOutputTypeDef(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIdNamespaceAssociationOutputTypeDef(BaseValidatorModel):
    idNamespaceAssociation: IdNamespaceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CollaborationTypeDef(BaseValidatorModel):
    pass


class CreateCollaborationOutputTypeDef(BaseValidatorModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCollaborationOutputTypeDef(BaseValidatorModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCollaborationOutputTypeDef(BaseValidatorModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReceiverConfigurationTypeDef(BaseValidatorModel):
    analysisType: AnalysisTypeType
    configurationDetails: Optional[ConfigurationDetailsTypeDef] = None


class ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef(BaseValidatorModel):
    pass


class ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef(BaseValidatorModel):
    v1: Optional[ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef] = None


class ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef(BaseValidatorModel):
    pass


class ConfiguredTableAssociationAnalysisRulePolicyTypeDef(BaseValidatorModel):
    v1: Optional[ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef] = None


class IdMappingTableSummaryTypeDef(BaseValidatorModel):
    pass


class ListIdMappingTablesOutputTypeDef(BaseValidatorModel):
    idMappingTableSummaries: List[IdMappingTableSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AnalysisRuleCustomOutputTypeDef(BaseValidatorModel):
    allowedAnalyses: List[str]
    allowedAnalysisProviders: Optional[List[str]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None
    disallowedOutputColumns: Optional[List[str]] = None
    differentialPrivacy: Optional[DifferentialPrivacyConfigurationOutputTypeDef] = None


class AnalysisRuleCustomTypeDef(BaseValidatorModel):
    allowedAnalyses: Sequence[str]
    allowedAnalysisProviders: Optional[Sequence[str]] = None
    additionalAnalyses: Optional[AdditionalAnalysesType] = None
    disallowedOutputColumns: Optional[Sequence[str]] = None
    differentialPrivacy: Optional[DifferentialPrivacyConfigurationTypeDef] = None


class PrivacyImpactTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyImpactTypeDef] = None


class PreviewPrivacyImpactInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    parameters: PreviewPrivacyImpactParametersInputTypeDef


class PrivacyBudgetTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyBudgetTypeDef] = None


class CreatePrivacyBudgetTemplateInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: PrivacyBudgetTemplateParametersInputTypeDef
    tags: Optional[Mapping[str, str]] = None


class UpdatePrivacyBudgetTemplateInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: Optional[PrivacyBudgetTemplateUpdateParametersTypeDef] = None


class SchemaTypePropertiesTypeDef(BaseValidatorModel):
    idMappingTable: Optional[IdMappingTableSchemaTypePropertiesTypeDef] = None


class PaymentConfigurationTypeDef(BaseValidatorModel):
    queryCompute: QueryComputePaymentConfigTypeDef
    machineLearning: Optional[MLPaymentConfigTypeDef] = None


class MembershipPaymentConfigurationTypeDef(BaseValidatorModel):
    queryCompute: MembershipQueryComputePaymentConfigTypeDef
    machineLearning: Optional[MembershipMLPaymentConfigTypeDef] = None


class MembershipProtectedQueryResultConfigurationTypeDef(BaseValidatorModel):
    outputConfiguration: MembershipProtectedQueryOutputConfigurationTypeDef
    roleArn: Optional[str] = None


class ProtectedQueryResultConfigurationTypeDef(BaseValidatorModel):
    outputConfiguration: ProtectedQueryOutputConfigurationTypeDef


class ProtectedQueryResultTypeDef(BaseValidatorModel):
    output: ProtectedQueryOutputTypeDef


class AnalysisRuleIdMappingTableTypeDef(BaseValidatorModel):
    joinColumns: List[str]
    queryConstraints: List[QueryConstraintTypeDef]
    dimensionColumns: Optional[List[str]] = None


class SnowflakeTableReferenceOutputTypeDef(BaseValidatorModel):
    secretArn: str
    accountIdentifier: str
    databaseName: str
    tableName: str
    schemaName: str
    tableSchema: SnowflakeTableSchemaOutputTypeDef


class SnowflakeTableReferenceTypeDef(BaseValidatorModel):
    secretArn: str
    accountIdentifier: str
    databaseName: str
    tableName: str
    schemaName: str
    tableSchema: SnowflakeTableSchemaTypeDef


class AnalysisTemplateTypeDef(BaseValidatorModel):
    pass


class CreateAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CollaborationAnalysisTemplateTypeDef(BaseValidatorModel):
    pass


class BatchGetCollaborationAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    collaborationAnalysisTemplates: List[CollaborationAnalysisTemplateTypeDef]
    errors: List[BatchGetCollaborationAnalysisTemplateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetCollaborationAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    collaborationAnalysisTemplate: CollaborationAnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PreviewPrivacyImpactOutputTypeDef(BaseValidatorModel):
    privacyImpact: PrivacyImpactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CollaborationPrivacyBudgetTemplateTypeDef(BaseValidatorModel):
    pass


class GetCollaborationPrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    collaborationPrivacyBudgetTemplate: CollaborationPrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PrivacyBudgetTemplateTypeDef(BaseValidatorModel):
    pass


class CreatePrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IdMappingTableTypeDef(BaseValidatorModel):
    pass


class CreateIdMappingTableOutputTypeDef(BaseValidatorModel):
    idMappingTable: IdMappingTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIdMappingTableOutputTypeDef(BaseValidatorModel):
    idMappingTable: IdMappingTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIdMappingTableOutputTypeDef(BaseValidatorModel):
    idMappingTable: IdMappingTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MLMemberAbilitiesUnionTypeDef(BaseValidatorModel):
    pass


class MemberSpecificationTypeDef(BaseValidatorModel):
    accountId: str
    memberAbilities: Sequence[MemberAbilityType]
    displayName: str
    mlMemberAbilities: Optional[MLMemberAbilitiesUnionTypeDef] = None
    paymentConfiguration: Optional[PaymentConfigurationTypeDef] = None


class MemberSummaryTypeDef(BaseValidatorModel):
    accountId: str
    status: MemberStatusType
    displayName: str
    abilities: List[MemberAbilityType]
    createTime: datetime
    updateTime: datetime
    paymentConfiguration: PaymentConfigurationTypeDef
    mlAbilities: Optional[MLMemberAbilitiesOutputTypeDef] = None
    membershipId: Optional[str] = None
    membershipArn: Optional[str] = None


class CreateMembershipInputTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    queryLogStatus: MembershipQueryLogStatusType
    tags: Optional[Mapping[str, str]] = None
    defaultResultConfiguration: Optional[MembershipProtectedQueryResultConfigurationTypeDef] = None
    paymentConfiguration: Optional[MembershipPaymentConfigurationTypeDef] = None


class UpdateMembershipInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    queryLogStatus: Optional[MembershipQueryLogStatusType] = None
    defaultResultConfiguration: Optional[MembershipProtectedQueryResultConfigurationTypeDef] = None


class TableReferenceOutputTypeDef(BaseValidatorModel):
    glue: Optional[GlueTableReferenceTypeDef] = None
    snowflake: Optional[SnowflakeTableReferenceOutputTypeDef] = None
    athena: Optional[AthenaTableReferenceTypeDef] = None


class TableReferenceTypeDef(BaseValidatorModel):
    glue: Optional[GlueTableReferenceTypeDef] = None
    snowflake: Optional[SnowflakeTableReferenceTypeDef] = None
    athena: Optional[AthenaTableReferenceTypeDef] = None


class ProtectedQuerySummaryTypeDef(BaseValidatorModel):
    pass


class ListProtectedQueriesOutputTypeDef(BaseValidatorModel):
    protectedQueries: List[ProtectedQuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConfiguredTableAssociationAnalysisRuleTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfiguredTableAssociationAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAssociationAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredTableAssociationAnalysisRuleInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef


class UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredTableAssociationIdentifier: str
    analysisRuleType: ConfiguredTableAssociationAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAssociationAnalysisRulePolicyUnionTypeDef


class ConfiguredTableAnalysisRulePolicyV1OutputTypeDef(BaseValidatorModel):
    pass


class ConfiguredTableAnalysisRulePolicyOutputTypeDef(BaseValidatorModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1OutputTypeDef] = None


class ConfiguredTableAnalysisRulePolicyV1TypeDef(BaseValidatorModel):
    pass


class ConfiguredTableAnalysisRulePolicyTypeDef(BaseValidatorModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1TypeDef] = None


class CollaborationPrivacyBudgetSummaryTypeDef(BaseValidatorModel):
    pass


class ListCollaborationPrivacyBudgetsOutputTypeDef(BaseValidatorModel):
    collaborationPrivacyBudgetSummaries: List[CollaborationPrivacyBudgetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PrivacyBudgetSummaryTypeDef(BaseValidatorModel):
    pass


class ListPrivacyBudgetsOutputTypeDef(BaseValidatorModel):
    privacyBudgetSummaries: List[PrivacyBudgetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SchemaTypeDef(BaseValidatorModel):
    pass


class BatchGetSchemaOutputTypeDef(BaseValidatorModel):
    schemas: List[SchemaTypeDef]
    errors: List[BatchGetSchemaErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaOutputTypeDef(BaseValidatorModel):
    schema: SchemaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCollaborationInputTypeDef(BaseValidatorModel):
    members: Sequence[MemberSpecificationTypeDef]
    name: str
    description: str
    creatorMemberAbilities: Sequence[MemberAbilityType]
    creatorDisplayName: str
    queryLogStatus: CollaborationQueryLogStatusType
    creatorMLMemberAbilities: Optional[MLMemberAbilitiesUnionTypeDef] = None
    dataEncryptionMetadata: Optional[DataEncryptionMetadataTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    creatorPaymentConfiguration: Optional[PaymentConfigurationTypeDef] = None
    analyticsEngine: Optional[AnalyticsEngineType] = None


class ListMembersOutputTypeDef(BaseValidatorModel):
    memberSummaries: List[MemberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MembershipSummaryTypeDef(BaseValidatorModel):
    pass


class ListMembershipsOutputTypeDef(BaseValidatorModel):
    membershipSummaries: List[MembershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MembershipTypeDef(BaseValidatorModel):
    pass


class CreateMembershipOutputTypeDef(BaseValidatorModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMembershipOutputTypeDef(BaseValidatorModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMembershipOutputTypeDef(BaseValidatorModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ProtectedQueryTypeDef(BaseValidatorModel):
    pass


class GetProtectedQueryOutputTypeDef(BaseValidatorModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartProtectedQueryOutputTypeDef(BaseValidatorModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProtectedQueryOutputTypeDef(BaseValidatorModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AnalysisRulePolicyV1TypeDef(BaseValidatorModel):
    pass


class AnalysisRulePolicyTypeDef(BaseValidatorModel):
    v1: Optional[AnalysisRulePolicyV1TypeDef] = None


class ConfiguredTableTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredTableOutputTypeDef(BaseValidatorModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfiguredTableOutputTypeDef(BaseValidatorModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfiguredTableOutputTypeDef(BaseValidatorModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TableReferenceUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredTableInputTypeDef(BaseValidatorModel):
    name: str
    tableReference: TableReferenceUnionTypeDef
    allowedColumns: Sequence[str]
    analysisMethod: Literal["DIRECT_QUERY"]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ConfiguredTableAnalysisRuleTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredTableAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfiguredTableAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfiguredTableAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConfiguredTableAnalysisRulePolicyUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredTableAnalysisRuleInputTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnionTypeDef


class UpdateConfiguredTableAnalysisRuleInputTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyUnionTypeDef


class BatchGetSchemaAnalysisRuleErrorTypeDef(BaseValidatorModel):
    pass


class AnalysisRuleTypeDef(BaseValidatorModel):
    pass


class BatchGetSchemaAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRules: List[AnalysisRuleTypeDef]
    errors: List[BatchGetSchemaAnalysisRuleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: AnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


