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
from aws_resource_validator.pydantic_models.cleanrooms_constants import *

class AggregateColumnTypeDef(BaseValidatorModel):
    columnNames: List[str]
    function: AggregateFunctionNameType

class AggregationConstraintTypeDef(BaseValidatorModel):
    columnName: str
    minimum: int
    type: Literal["COUNT_DISTINCT"]

class AnalysisParameterTypeDef(BaseValidatorModel):
    name: str
    type: ParameterTypeType
    defaultValue: Optional[str] = None

class AnalysisRuleListTypeDef(BaseValidatorModel):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None

class AnalysisSchemaTypeDef(BaseValidatorModel):
    referencedTables: Optional[List[str]] = None

class AnalysisSourceTypeDef(BaseValidatorModel):
    text: Optional[str] = None

class AnalysisTemplateSummaryTypeDef(BaseValidatorModel):
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

class AnalysisTemplateValidationStatusReasonTypeDef(BaseValidatorModel):
    message: str

class BatchGetCollaborationAnalysisTemplateErrorTypeDef(BaseValidatorModel):
    arn: str
    code: str
    message: str

class BatchGetCollaborationAnalysisTemplateInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArns: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetSchemaAnalysisRuleErrorTypeDef(BaseValidatorModel):
    name: str
    type: AnalysisRuleTypeType
    code: str
    message: str

class SchemaAnalysisRuleRequestTypeDef(BaseValidatorModel):
    name: str
    type: AnalysisRuleTypeType

class BatchGetSchemaErrorTypeDef(BaseValidatorModel):
    name: str
    code: str
    message: str

class BatchGetSchemaInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    names: Sequence[str]

class CollaborationAnalysisTemplateSummaryTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    name: str
    updateTime: datetime
    collaborationArn: str
    collaborationId: str
    creatorAccountId: str
    description: Optional[str] = None

class CollaborationConfiguredAudienceModelAssociationSummaryTypeDef(BaseValidatorModel):
    arn: str
    createTime: datetime
    id: str
    name: str
    updateTime: datetime
    collaborationArn: str
    collaborationId: str
    creatorAccountId: str
    description: Optional[str] = None

class CollaborationConfiguredAudienceModelAssociationTypeDef(BaseValidatorModel):
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

class CollaborationPrivacyBudgetTemplateSummaryTypeDef(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    createTime: datetime
    updateTime: datetime

class CollaborationSummaryTypeDef(BaseValidatorModel):
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

class DataEncryptionMetadataTypeDef(BaseValidatorModel):
    allowCleartext: bool
    allowDuplicates: bool
    allowJoinsOnColumnsWithDifferentNames: bool
    preserveNulls: bool

class ColumnTypeDef(BaseValidatorModel):
    name: str
    type: str

class ConfiguredAudienceModelAssociationSummaryTypeDef(BaseValidatorModel):
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

class ConfiguredAudienceModelAssociationTypeDef(BaseValidatorModel):
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

class ConfiguredTableAssociationSummaryTypeDef(BaseValidatorModel):
    configuredTableId: str
    membershipId: str
    membershipArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    id: str
    arn: str

class ConfiguredTableAssociationTypeDef(BaseValidatorModel):
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

class ConfiguredTableSummaryTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    createTime: datetime
    updateTime: datetime
    analysisRuleTypes: List[ConfiguredTableAnalysisRuleTypeType]
    analysisMethod: Literal["DIRECT_QUERY"]

class CreateConfiguredAudienceModelAssociationInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredAudienceModelArn: str
    configuredAudienceModelAssociationName: str
    manageResourcePolicies: bool
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None

class CreateConfiguredTableAssociationInputRequestTypeDef(BaseValidatorModel):
    name: str
    membershipIdentifier: str
    configuredTableIdentifier: str
    roleArn: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteAnalysisTemplateInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str

class DeleteCollaborationInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str

class DeleteConfiguredAudienceModelAssociationInputRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str

class DeleteConfiguredTableAnalysisRuleInputRequestTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType

class DeleteConfiguredTableAssociationInputRequestTypeDef(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str

class DeleteConfiguredTableInputRequestTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str

class DeleteMemberInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    accountId: str

class DeleteMembershipInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str

class DeletePrivacyBudgetTemplateInputRequestTypeDef(BaseValidatorModel):
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

class DifferentialPrivacyPreviewAggregationTypeDef(BaseValidatorModel):
    type: DifferentialPrivacyAggregationTypeType
    maxCount: int

class DifferentialPrivacyPreviewParametersInputTypeDef(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyPrivacyBudgetAggregationTypeDef(BaseValidatorModel):
    type: DifferentialPrivacyAggregationTypeType
    maxCount: int
    remainingCount: int

class DifferentialPrivacyTemplateParametersInputTypeDef(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyTemplateParametersOutputTypeDef(BaseValidatorModel):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyTemplateUpdateParametersTypeDef(BaseValidatorModel):
    epsilon: Optional[int] = None
    usersNoisePerQuery: Optional[int] = None

class GetAnalysisTemplateInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str

class GetCollaborationAnalysisTemplateInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    analysisTemplateArn: str

class GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    configuredAudienceModelAssociationIdentifier: str

class GetCollaborationInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str

class GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetTemplateIdentifier: str

class GetConfiguredAudienceModelAssociationInputRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str

class GetConfiguredTableAnalysisRuleInputRequestTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType

class GetConfiguredTableAssociationInputRequestTypeDef(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str

class GetConfiguredTableInputRequestTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str

class GetMembershipInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str

class GetPrivacyBudgetTemplateInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str

class GetProtectedQueryInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str

class GetSchemaAnalysisRuleInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    name: str
    type: AnalysisRuleTypeType

class GetSchemaInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    name: str

class GlueTableReferenceTypeDef(BaseValidatorModel):
    tableName: str
    databaseName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAnalysisTemplatesInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationAnalysisTemplatesInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationPrivacyBudgetsInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCollaborationsInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    memberStatus: Optional[FilterableMemberStatusType] = None

class ListConfiguredAudienceModelAssociationsInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListConfiguredTableAssociationsInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListConfiguredTablesInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMembersInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMembershipsInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[MembershipStatusType] = None

class ListPrivacyBudgetTemplatesInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PrivacyBudgetTemplateSummaryTypeDef(BaseValidatorModel):
    id: str
    arn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    createTime: datetime
    updateTime: datetime

class ListPrivacyBudgetsInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProtectedQueriesInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProtectedQuerySummaryTypeDef(BaseValidatorModel):
    id: str
    membershipId: str
    membershipArn: str
    createTime: datetime
    status: ProtectedQueryStatusType

class ListSchemasInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[Literal["TABLE"]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SchemaSummaryTypeDef(BaseValidatorModel):
    name: str
    type: Literal["TABLE"]
    creatorAccountId: str
    createTime: datetime
    updateTime: datetime
    collaborationId: str
    collaborationArn: str
    analysisRuleTypes: List[AnalysisRuleTypeType]
    analysisMethod: Optional[Literal["DIRECT_QUERY"]] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class MembershipQueryComputePaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool

class ProtectedQueryS3OutputConfigurationTypeDef(BaseValidatorModel):
    resultFormat: ResultFormatType
    bucket: str
    keyPrefix: Optional[str] = None

class QueryComputePaymentConfigTypeDef(BaseValidatorModel):
    isResponsible: bool

class ProtectedQueryErrorTypeDef(BaseValidatorModel):
    message: str
    code: str

class ProtectedQueryS3OutputTypeDef(BaseValidatorModel):
    location: str

class ProtectedQuerySingleMemberOutputTypeDef(BaseValidatorModel):
    accountId: str

class ProtectedQuerySQLParametersTypeDef(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None

class ProtectedQueryStatisticsTypeDef(BaseValidatorModel):
    totalDurationInMillis: Optional[int] = None

class SchemaStatusReasonTypeDef(BaseValidatorModel):
    code: SchemaStatusReasonCodeType
    message: str

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAnalysisTemplateInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str
    description: Optional[str] = None

class UpdateCollaborationInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateConfiguredAudienceModelAssociationInputRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    name: Optional[str] = None

class UpdateConfiguredTableAssociationInputRequestTypeDef(BaseValidatorModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    roleArn: Optional[str] = None

class UpdateConfiguredTableInputRequestTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateProtectedQueryInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str
    targetStatus: Literal["CANCELLED"]

class AnalysisRuleAggregationTypeDef(BaseValidatorModel):
    aggregateColumns: List[AggregateColumnTypeDef]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraintTypeDef]
    joinRequired: Optional[Literal["QUERY_RUNNER"]] = None
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None

class CreateAnalysisTemplateInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    format: Literal["SQL"]
    source: AnalysisSourceTypeDef
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    analysisParameters: Optional[Sequence[AnalysisParameterTypeDef]] = None

class AnalysisTemplateValidationStatusDetailTypeDef(BaseValidatorModel):
    type: Literal["DIFFERENTIAL_PRIVACY"]
    status: AnalysisTemplateValidationStatusType
    reasons: Optional[List[AnalysisTemplateValidationStatusReasonTypeDef]] = None

class ListAnalysisTemplatesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    analysisTemplateSummaries: List[AnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetSchemaAnalysisRuleInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    schemaAnalysisRuleRequests: Sequence[SchemaAnalysisRuleRequestTypeDef]

class ListCollaborationAnalysisTemplatesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    collaborationAnalysisTemplateSummaries: List[CollaborationAnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociationSummaries: List[       CollaborationConfiguredAudienceModelAssociationSummaryTypeDef     ]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    collaborationConfiguredAudienceModelAssociation: CollaborationConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollaborationPrivacyBudgetTemplatesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    collaborationPrivacyBudgetTemplateSummaries: List[       CollaborationPrivacyBudgetTemplateSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollaborationsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    collaborationList: List[CollaborationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CollaborationTypeDef(BaseValidatorModel):
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
    dataEncryptionMetadata: Optional[DataEncryptionMetadataTypeDef] = None

class ListConfiguredAudienceModelAssociationsOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociationSummaries: List[       ConfiguredAudienceModelAssociationSummaryTypeDef     ]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelAssociationOutputTypeDef(BaseValidatorModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfiguredTableAssociationsOutputTypeDef(BaseValidatorModel):
    configuredTableAssociationSummaries: List[ConfiguredTableAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableAssociationOutputTypeDef(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableAssociationOutputTypeDef(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableAssociationOutputTypeDef(BaseValidatorModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfiguredTablesOutputTypeDef(BaseValidatorModel):
    configuredTableSummaries: List[ConfiguredTableSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DifferentialPrivacyConfigurationTypeDef(BaseValidatorModel):
    columns: List[DifferentialPrivacyColumnTypeDef]

class DifferentialPrivacyParametersTypeDef(BaseValidatorModel):
    sensitivityParameters: List[DifferentialPrivacySensitivityParametersTypeDef]

class DifferentialPrivacyPrivacyImpactTypeDef(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPreviewAggregationTypeDef]

class PreviewPrivacyImpactParametersInputTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPreviewParametersInputTypeDef] = None

class DifferentialPrivacyPrivacyBudgetTypeDef(BaseValidatorModel):
    aggregations: List[DifferentialPrivacyPrivacyBudgetAggregationTypeDef]
    epsilon: int

class PrivacyBudgetTemplateParametersInputTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersInputTypeDef] = None

class PrivacyBudgetTemplateParametersOutputTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersOutputTypeDef] = None

class PrivacyBudgetTemplateUpdateParametersTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateUpdateParametersTypeDef] = None

class TableReferenceTypeDef(BaseValidatorModel):
    glue: Optional[GlueTableReferenceTypeDef] = None

class ListAnalysisTemplatesInputListAnalysisTemplatesPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationConfiguredAudienceModelAssociationsInputListCollaborationConfiguredAudienceModelAssociationsPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationPrivacyBudgetTemplatesInputListCollaborationPrivacyBudgetTemplatesPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationPrivacyBudgetsInputListCollaborationPrivacyBudgetsPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationsInputListCollaborationsPaginateTypeDef(BaseValidatorModel):
    memberStatus: Optional[FilterableMemberStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredAudienceModelAssociationsInputListConfiguredAudienceModelAssociationsPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredTableAssociationsInputListConfiguredTableAssociationsPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredTablesInputListConfiguredTablesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersInputListMembersPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembershipsInputListMembershipsPaginateTypeDef(BaseValidatorModel):
    status: Optional[MembershipStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivacyBudgetTemplatesInputListPrivacyBudgetTemplatesPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivacyBudgetsInputListPrivacyBudgetsPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedQueriesInputListProtectedQueriesPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasInputListSchemasPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    schemaType: Optional[Literal["TABLE"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivacyBudgetTemplatesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    privacyBudgetTemplateSummaries: List[PrivacyBudgetTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectedQueriesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    protectedQueries: List[ProtectedQuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemasOutputTypeDef(BaseValidatorModel):
    schemaSummaries: List[SchemaSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MembershipPaymentConfigurationTypeDef(BaseValidatorModel):
    queryCompute: MembershipQueryComputePaymentConfigTypeDef

class MembershipProtectedQueryOutputConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputConfigurationTypeDef] = None

class ProtectedQueryOutputConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputConfigurationTypeDef] = None

class PaymentConfigurationTypeDef(BaseValidatorModel):
    queryCompute: QueryComputePaymentConfigTypeDef

class ProtectedQueryOutputTypeDef(BaseValidatorModel):
    s3: Optional[ProtectedQueryS3OutputTypeDef] = None
    memberList: Optional[List[ProtectedQuerySingleMemberOutputTypeDef]] = None

class SchemaStatusDetailTypeDef(BaseValidatorModel):
    status: SchemaStatusType
    reasons: Optional[List[SchemaStatusReasonTypeDef]] = None
    analysisRuleType: Optional[AnalysisRuleTypeType] = None
    configurations: Optional[List[Literal["DIFFERENTIAL_PRIVACY"]]] = None

class AnalysisTemplateTypeDef(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    membershipId: str
    membershipArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    schema: AnalysisSchemaTypeDef
    format: Literal["SQL"]
    source: AnalysisSourceTypeDef
    description: Optional[str] = None
    analysisParameters: Optional[List[AnalysisParameterTypeDef]] = None
    validations: Optional[List[AnalysisTemplateValidationStatusDetailTypeDef]] = None

class CollaborationAnalysisTemplateTypeDef(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    name: str
    createTime: datetime
    updateTime: datetime
    schema: AnalysisSchemaTypeDef
    format: Literal["SQL"]
    source: AnalysisSourceTypeDef
    description: Optional[str] = None
    analysisParameters: Optional[List[AnalysisParameterTypeDef]] = None
    validations: Optional[List[AnalysisTemplateValidationStatusDetailTypeDef]] = None

class CreateCollaborationOutputTypeDef(BaseValidatorModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationOutputTypeDef(BaseValidatorModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCollaborationOutputTypeDef(BaseValidatorModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRuleCustomTypeDef(BaseValidatorModel):
    allowedAnalyses: List[str]
    allowedAnalysisProviders: Optional[List[str]] = None
    differentialPrivacy: Optional[DifferentialPrivacyConfigurationTypeDef] = None

class PrivacyImpactTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyImpactTypeDef] = None

class PreviewPrivacyImpactInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    parameters: PreviewPrivacyImpactParametersInputTypeDef

class PrivacyBudgetTypeDef(BaseValidatorModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyBudgetTypeDef] = None

class CreatePrivacyBudgetTemplateInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: PrivacyBudgetTemplateParametersInputTypeDef
    tags: Optional[Mapping[str, str]] = None

class CollaborationPrivacyBudgetTemplateTypeDef(BaseValidatorModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    createTime: datetime
    updateTime: datetime
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    parameters: PrivacyBudgetTemplateParametersOutputTypeDef

class PrivacyBudgetTemplateTypeDef(BaseValidatorModel):
    id: str
    arn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    createTime: datetime
    updateTime: datetime
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    parameters: PrivacyBudgetTemplateParametersOutputTypeDef

class UpdatePrivacyBudgetTemplateInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: Optional[PrivacyBudgetTemplateUpdateParametersTypeDef] = None

class ConfiguredTableTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    tableReference: TableReferenceTypeDef
    createTime: datetime
    updateTime: datetime
    analysisRuleTypes: List[ConfiguredTableAnalysisRuleTypeType]
    analysisMethod: Literal["DIRECT_QUERY"]
    allowedColumns: List[str]
    description: Optional[str] = None

class CreateConfiguredTableInputRequestTypeDef(BaseValidatorModel):
    name: str
    tableReference: TableReferenceTypeDef
    allowedColumns: Sequence[str]
    analysisMethod: Literal["DIRECT_QUERY"]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class MembershipSummaryTypeDef(BaseValidatorModel):
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
    paymentConfiguration: MembershipPaymentConfigurationTypeDef

class MembershipProtectedQueryResultConfigurationTypeDef(BaseValidatorModel):
    outputConfiguration: MembershipProtectedQueryOutputConfigurationTypeDef
    roleArn: Optional[str] = None

class ProtectedQueryResultConfigurationTypeDef(BaseValidatorModel):
    outputConfiguration: ProtectedQueryOutputConfigurationTypeDef

class MemberSpecificationTypeDef(BaseValidatorModel):
    accountId: str
    memberAbilities: Sequence[MemberAbilityType]
    displayName: str
    paymentConfiguration: Optional[PaymentConfigurationTypeDef] = None

class MemberSummaryTypeDef(BaseValidatorModel):
    accountId: str
    status: MemberStatusType
    displayName: str
    abilities: List[MemberAbilityType]
    createTime: datetime
    updateTime: datetime
    paymentConfiguration: PaymentConfigurationTypeDef
    membershipId: Optional[str] = None
    membershipArn: Optional[str] = None

class ProtectedQueryResultTypeDef(BaseValidatorModel):
    output: ProtectedQueryOutputTypeDef

class SchemaTypeDef(BaseValidatorModel):
    columns: List[ColumnTypeDef]
    partitionKeys: List[ColumnTypeDef]
    analysisRuleTypes: List[AnalysisRuleTypeType]
    creatorAccountId: str
    name: str
    collaborationId: str
    collaborationArn: str
    description: str
    createTime: datetime
    updateTime: datetime
    type: Literal["TABLE"]
    schemaStatusDetails: List[SchemaStatusDetailTypeDef]
    analysisMethod: Optional[Literal["DIRECT_QUERY"]] = None

class CreateAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetCollaborationAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    collaborationAnalysisTemplates: List[CollaborationAnalysisTemplateTypeDef]
    errors: List[BatchGetCollaborationAnalysisTemplateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationAnalysisTemplateOutputTypeDef(BaseValidatorModel):
    collaborationAnalysisTemplate: CollaborationAnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRulePolicyV1TypeDef(BaseValidatorModel):
    list: Optional[AnalysisRuleListTypeDef] = None
    aggregation: Optional[AnalysisRuleAggregationTypeDef] = None
    custom: Optional[AnalysisRuleCustomTypeDef] = None

class ConfiguredTableAnalysisRulePolicyV1TypeDef(BaseValidatorModel):
    list: Optional[AnalysisRuleListTypeDef] = None
    aggregation: Optional[AnalysisRuleAggregationTypeDef] = None
    custom: Optional[AnalysisRuleCustomTypeDef] = None

class PreviewPrivacyImpactOutputTypeDef(BaseValidatorModel):
    privacyImpact: PrivacyImpactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CollaborationPrivacyBudgetSummaryTypeDef(BaseValidatorModel):
    id: str
    privacyBudgetTemplateId: str
    privacyBudgetTemplateArn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    type: Literal["DIFFERENTIAL_PRIVACY"]
    createTime: datetime
    updateTime: datetime
    budget: PrivacyBudgetTypeDef

class PrivacyBudgetSummaryTypeDef(BaseValidatorModel):
    id: str
    privacyBudgetTemplateId: str
    privacyBudgetTemplateArn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    type: Literal["DIFFERENTIAL_PRIVACY"]
    createTime: datetime
    updateTime: datetime
    budget: PrivacyBudgetTypeDef

class GetCollaborationPrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    collaborationPrivacyBudgetTemplate: CollaborationPrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivacyBudgetTemplateOutputTypeDef(BaseValidatorModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableOutputTypeDef(BaseValidatorModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableOutputTypeDef(BaseValidatorModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableOutputTypeDef(BaseValidatorModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembershipsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    membershipSummaries: List[MembershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembershipInputRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    queryLogStatus: MembershipQueryLogStatusType
    tags: Optional[Mapping[str, str]] = None
    defaultResultConfiguration: Optional[       MembershipProtectedQueryResultConfigurationTypeDef     ] = None
    paymentConfiguration: Optional[MembershipPaymentConfigurationTypeDef] = None

class MembershipTypeDef(BaseValidatorModel):
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
    paymentConfiguration: MembershipPaymentConfigurationTypeDef
    defaultResultConfiguration: Optional[       MembershipProtectedQueryResultConfigurationTypeDef     ] = None

class UpdateMembershipInputRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    queryLogStatus: Optional[MembershipQueryLogStatusType] = None
    defaultResultConfiguration: Optional[       MembershipProtectedQueryResultConfigurationTypeDef     ] = None

class StartProtectedQueryInputRequestTypeDef(BaseValidatorModel):
    type: Literal["SQL"]
    membershipIdentifier: str
    sqlParameters: ProtectedQuerySQLParametersTypeDef
    resultConfiguration: Optional[ProtectedQueryResultConfigurationTypeDef] = None

class CreateCollaborationInputRequestTypeDef(BaseValidatorModel):
    members: Sequence[MemberSpecificationTypeDef]
    name: str
    description: str
    creatorMemberAbilities: Sequence[MemberAbilityType]
    creatorDisplayName: str
    queryLogStatus: CollaborationQueryLogStatusType
    dataEncryptionMetadata: Optional[DataEncryptionMetadataTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    creatorPaymentConfiguration: Optional[PaymentConfigurationTypeDef] = None

class ListMembersOutputTypeDef(BaseValidatorModel):
    nextToken: str
    memberSummaries: List[MemberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProtectedQueryTypeDef(BaseValidatorModel):
    id: str
    membershipId: str
    membershipArn: str
    createTime: datetime
    status: ProtectedQueryStatusType
    sqlParameters: Optional[ProtectedQuerySQLParametersTypeDef] = None
    resultConfiguration: Optional[ProtectedQueryResultConfigurationTypeDef] = None
    statistics: Optional[ProtectedQueryStatisticsTypeDef] = None
    result: Optional[ProtectedQueryResultTypeDef] = None
    error: Optional[ProtectedQueryErrorTypeDef] = None
    differentialPrivacy: Optional[DifferentialPrivacyParametersTypeDef] = None

class BatchGetSchemaOutputTypeDef(BaseValidatorModel):
    schemas: List[SchemaTypeDef]
    errors: List[BatchGetSchemaErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaOutputTypeDef(BaseValidatorModel):
    schema: SchemaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRulePolicyTypeDef(BaseValidatorModel):
    v1: Optional[AnalysisRulePolicyV1TypeDef] = None

class ConfiguredTableAnalysisRulePolicyTypeDef(BaseValidatorModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1TypeDef] = None

class ListCollaborationPrivacyBudgetsOutputTypeDef(BaseValidatorModel):
    collaborationPrivacyBudgetSummaries: List[CollaborationPrivacyBudgetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrivacyBudgetsOutputTypeDef(BaseValidatorModel):
    privacyBudgetSummaries: List[PrivacyBudgetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembershipOutputTypeDef(BaseValidatorModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembershipOutputTypeDef(BaseValidatorModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMembershipOutputTypeDef(BaseValidatorModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProtectedQueryOutputTypeDef(BaseValidatorModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartProtectedQueryOutputTypeDef(BaseValidatorModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProtectedQueryOutputTypeDef(BaseValidatorModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRuleTypeDef(BaseValidatorModel):
    collaborationId: str
    type: AnalysisRuleTypeType
    name: str
    createTime: datetime
    updateTime: datetime
    policy: AnalysisRulePolicyTypeDef

class ConfiguredTableAnalysisRuleTypeDef(BaseValidatorModel):
    configuredTableId: str
    configuredTableArn: str
    policy: ConfiguredTableAnalysisRulePolicyTypeDef
    type: ConfiguredTableAnalysisRuleTypeType
    createTime: datetime
    updateTime: datetime

class CreateConfiguredTableAnalysisRuleInputRequestTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyTypeDef

class UpdateConfiguredTableAnalysisRuleInputRequestTypeDef(BaseValidatorModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyTypeDef

class BatchGetSchemaAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRules: List[AnalysisRuleTypeDef]
    errors: List[BatchGetSchemaAnalysisRuleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: AnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableAnalysisRuleOutputTypeDef(BaseValidatorModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

