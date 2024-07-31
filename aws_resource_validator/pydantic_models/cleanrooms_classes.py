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
from aws_resource_validator.pydantic_models.cleanrooms_constants import *

class AggregateColumnTypeDef(BaseModel):
    columnNames: List[str]
    function: AggregateFunctionNameType

class AggregationConstraintTypeDef(BaseModel):
    columnName: str
    minimum: int
    type: Literal["COUNT_DISTINCT"]

class AnalysisParameterTypeDef(BaseModel):
    name: str
    type: ParameterTypeType
    defaultValue: Optional[str] = None

class AnalysisRuleListTypeDef(BaseModel):
    joinColumns: List[str]
    listColumns: List[str]
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None

class AnalysisSchemaTypeDef(BaseModel):
    referencedTables: Optional[List[str]] = None

class AnalysisSourceTypeDef(BaseModel):
    text: Optional[str] = None

class AnalysisTemplateSummaryTypeDef(BaseModel):
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

class AnalysisTemplateValidationStatusReasonTypeDef(BaseModel):
    message: str

class BatchGetCollaborationAnalysisTemplateErrorTypeDef(BaseModel):
    arn: str
    code: str
    message: str

class BatchGetCollaborationAnalysisTemplateInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    analysisTemplateArns: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetSchemaAnalysisRuleErrorTypeDef(BaseModel):
    name: str
    type: AnalysisRuleTypeType
    code: str
    message: str

class SchemaAnalysisRuleRequestTypeDef(BaseModel):
    name: str
    type: AnalysisRuleTypeType

class BatchGetSchemaErrorTypeDef(BaseModel):
    name: str
    code: str
    message: str

class BatchGetSchemaInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    names: Sequence[str]

class CollaborationAnalysisTemplateSummaryTypeDef(BaseModel):
    arn: str
    createTime: datetime
    id: str
    name: str
    updateTime: datetime
    collaborationArn: str
    collaborationId: str
    creatorAccountId: str
    description: Optional[str] = None

class CollaborationConfiguredAudienceModelAssociationSummaryTypeDef(BaseModel):
    arn: str
    createTime: datetime
    id: str
    name: str
    updateTime: datetime
    collaborationArn: str
    collaborationId: str
    creatorAccountId: str
    description: Optional[str] = None

class CollaborationConfiguredAudienceModelAssociationTypeDef(BaseModel):
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

class CollaborationPrivacyBudgetTemplateSummaryTypeDef(BaseModel):
    id: str
    arn: str
    collaborationId: str
    collaborationArn: str
    creatorAccountId: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    createTime: datetime
    updateTime: datetime

class CollaborationSummaryTypeDef(BaseModel):
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

class DataEncryptionMetadataTypeDef(BaseModel):
    allowCleartext: bool
    allowDuplicates: bool
    allowJoinsOnColumnsWithDifferentNames: bool
    preserveNulls: bool

class ColumnTypeDef(BaseModel):
    name: str
    type: str

class ConfiguredAudienceModelAssociationSummaryTypeDef(BaseModel):
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

class ConfiguredAudienceModelAssociationTypeDef(BaseModel):
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

class ConfiguredTableAssociationSummaryTypeDef(BaseModel):
    configuredTableId: str
    membershipId: str
    membershipArn: str
    name: str
    createTime: datetime
    updateTime: datetime
    id: str
    arn: str

class ConfiguredTableAssociationTypeDef(BaseModel):
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

class ConfiguredTableSummaryTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    createTime: datetime
    updateTime: datetime
    analysisRuleTypes: List[ConfiguredTableAnalysisRuleTypeType]
    analysisMethod: Literal["DIRECT_QUERY"]

class CreateConfiguredAudienceModelAssociationInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    configuredAudienceModelArn: str
    configuredAudienceModelAssociationName: str
    manageResourcePolicies: bool
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None

class CreateConfiguredTableAssociationInputRequestTypeDef(BaseModel):
    name: str
    membershipIdentifier: str
    configuredTableIdentifier: str
    roleArn: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteAnalysisTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str

class DeleteCollaborationInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str

class DeleteConfiguredAudienceModelAssociationInputRequestTypeDef(BaseModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str

class DeleteConfiguredTableAnalysisRuleInputRequestTypeDef(BaseModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType

class DeleteConfiguredTableAssociationInputRequestTypeDef(BaseModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str

class DeleteConfiguredTableInputRequestTypeDef(BaseModel):
    configuredTableIdentifier: str

class DeleteMemberInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    accountId: str

class DeleteMembershipInputRequestTypeDef(BaseModel):
    membershipIdentifier: str

class DeletePrivacyBudgetTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str

class DifferentialPrivacyColumnTypeDef(BaseModel):
    name: str

class DifferentialPrivacySensitivityParametersTypeDef(BaseModel):
    aggregationType: DifferentialPrivacyAggregationTypeType
    aggregationExpression: str
    userContributionLimit: int
    minColumnValue: Optional[float] = None
    maxColumnValue: Optional[float] = None

class DifferentialPrivacyPreviewAggregationTypeDef(BaseModel):
    type: DifferentialPrivacyAggregationTypeType
    maxCount: int

class DifferentialPrivacyPreviewParametersInputTypeDef(BaseModel):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyPrivacyBudgetAggregationTypeDef(BaseModel):
    type: DifferentialPrivacyAggregationTypeType
    maxCount: int
    remainingCount: int

class DifferentialPrivacyTemplateParametersInputTypeDef(BaseModel):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyTemplateParametersOutputTypeDef(BaseModel):
    epsilon: int
    usersNoisePerQuery: int

class DifferentialPrivacyTemplateUpdateParametersTypeDef(BaseModel):
    epsilon: Optional[int] = None
    usersNoisePerQuery: Optional[int] = None

class GetAnalysisTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str

class GetCollaborationAnalysisTemplateInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    analysisTemplateArn: str

class GetCollaborationConfiguredAudienceModelAssociationInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    configuredAudienceModelAssociationIdentifier: str

class GetCollaborationInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str

class GetCollaborationPrivacyBudgetTemplateInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    privacyBudgetTemplateIdentifier: str

class GetConfiguredAudienceModelAssociationInputRequestTypeDef(BaseModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str

class GetConfiguredTableAnalysisRuleInputRequestTypeDef(BaseModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType

class GetConfiguredTableAssociationInputRequestTypeDef(BaseModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str

class GetConfiguredTableInputRequestTypeDef(BaseModel):
    configuredTableIdentifier: str

class GetMembershipInputRequestTypeDef(BaseModel):
    membershipIdentifier: str

class GetPrivacyBudgetTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str

class GetProtectedQueryInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str

class GetSchemaAnalysisRuleInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    name: str
    type: AnalysisRuleTypeType

class GetSchemaInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    name: str

class GlueTableReferenceTypeDef(BaseModel):
    tableName: str
    databaseName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAnalysisTemplatesInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationAnalysisTemplatesInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationConfiguredAudienceModelAssociationsInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationPrivacyBudgetTemplatesInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCollaborationPrivacyBudgetsInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCollaborationsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    memberStatus: Optional[FilterableMemberStatusType] = None

class ListConfiguredAudienceModelAssociationsInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListConfiguredTableAssociationsInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListConfiguredTablesInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMembersInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMembershipsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[MembershipStatusType] = None

class ListPrivacyBudgetTemplatesInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PrivacyBudgetTemplateSummaryTypeDef(BaseModel):
    id: str
    arn: str
    membershipId: str
    membershipArn: str
    collaborationId: str
    collaborationArn: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    createTime: datetime
    updateTime: datetime

class ListPrivacyBudgetsInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProtectedQueriesInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProtectedQuerySummaryTypeDef(BaseModel):
    id: str
    membershipId: str
    membershipArn: str
    createTime: datetime
    status: ProtectedQueryStatusType

class ListSchemasInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    schemaType: Optional[Literal["TABLE"]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SchemaSummaryTypeDef(BaseModel):
    name: str
    type: Literal["TABLE"]
    creatorAccountId: str
    createTime: datetime
    updateTime: datetime
    collaborationId: str
    collaborationArn: str
    analysisRuleTypes: List[AnalysisRuleTypeType]
    analysisMethod: Optional[Literal["DIRECT_QUERY"]] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class MembershipQueryComputePaymentConfigTypeDef(BaseModel):
    isResponsible: bool

class ProtectedQueryS3OutputConfigurationTypeDef(BaseModel):
    resultFormat: ResultFormatType
    bucket: str
    keyPrefix: Optional[str] = None

class QueryComputePaymentConfigTypeDef(BaseModel):
    isResponsible: bool

class ProtectedQueryErrorTypeDef(BaseModel):
    message: str
    code: str

class ProtectedQueryS3OutputTypeDef(BaseModel):
    location: str

class ProtectedQuerySingleMemberOutputTypeDef(BaseModel):
    accountId: str

class ProtectedQuerySQLParametersTypeDef(BaseModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None

class ProtectedQueryStatisticsTypeDef(BaseModel):
    totalDurationInMillis: Optional[int] = None

class SchemaStatusReasonTypeDef(BaseModel):
    code: SchemaStatusReasonCodeType
    message: str

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAnalysisTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    analysisTemplateIdentifier: str
    description: Optional[str] = None

class UpdateCollaborationInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateConfiguredAudienceModelAssociationInputRequestTypeDef(BaseModel):
    configuredAudienceModelAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    name: Optional[str] = None

class UpdateConfiguredTableAssociationInputRequestTypeDef(BaseModel):
    configuredTableAssociationIdentifier: str
    membershipIdentifier: str
    description: Optional[str] = None
    roleArn: Optional[str] = None

class UpdateConfiguredTableInputRequestTypeDef(BaseModel):
    configuredTableIdentifier: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateProtectedQueryInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    protectedQueryIdentifier: str
    targetStatus: Literal["CANCELLED"]

class AnalysisRuleAggregationTypeDef(BaseModel):
    aggregateColumns: List[AggregateColumnTypeDef]
    joinColumns: List[str]
    dimensionColumns: List[str]
    scalarFunctions: List[ScalarFunctionsType]
    outputConstraints: List[AggregationConstraintTypeDef]
    joinRequired: Optional[Literal["QUERY_RUNNER"]] = None
    allowedJoinOperators: Optional[List[JoinOperatorType]] = None

class CreateAnalysisTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    name: str
    format: Literal["SQL"]
    source: AnalysisSourceTypeDef
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    analysisParameters: Optional[Sequence[AnalysisParameterTypeDef]] = None

class AnalysisTemplateValidationStatusDetailTypeDef(BaseModel):
    type: Literal["DIFFERENTIAL_PRIVACY"]
    status: AnalysisTemplateValidationStatusType
    reasons: Optional[List[AnalysisTemplateValidationStatusReasonTypeDef]] = None

class ListAnalysisTemplatesOutputTypeDef(BaseModel):
    nextToken: str
    analysisTemplateSummaries: List[AnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetSchemaAnalysisRuleInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    schemaAnalysisRuleRequests: Sequence[SchemaAnalysisRuleRequestTypeDef]

class ListCollaborationAnalysisTemplatesOutputTypeDef(BaseModel):
    nextToken: str
    collaborationAnalysisTemplateSummaries: List[CollaborationAnalysisTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef(BaseModel):
    collaborationConfiguredAudienceModelAssociationSummaries: List[       CollaborationConfiguredAudienceModelAssociationSummaryTypeDef     ]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef(BaseModel):
    collaborationConfiguredAudienceModelAssociation: CollaborationConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollaborationPrivacyBudgetTemplatesOutputTypeDef(BaseModel):
    nextToken: str
    collaborationPrivacyBudgetTemplateSummaries: List[       CollaborationPrivacyBudgetTemplateSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCollaborationsOutputTypeDef(BaseModel):
    nextToken: str
    collaborationList: List[CollaborationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CollaborationTypeDef(BaseModel):
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

class ListConfiguredAudienceModelAssociationsOutputTypeDef(BaseModel):
    configuredAudienceModelAssociationSummaries: List[       ConfiguredAudienceModelAssociationSummaryTypeDef     ]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredAudienceModelAssociationOutputTypeDef(BaseModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredAudienceModelAssociationOutputTypeDef(BaseModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelAssociationOutputTypeDef(BaseModel):
    configuredAudienceModelAssociation: ConfiguredAudienceModelAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfiguredTableAssociationsOutputTypeDef(BaseModel):
    configuredTableAssociationSummaries: List[ConfiguredTableAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableAssociationOutputTypeDef(BaseModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableAssociationOutputTypeDef(BaseModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableAssociationOutputTypeDef(BaseModel):
    configuredTableAssociation: ConfiguredTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfiguredTablesOutputTypeDef(BaseModel):
    configuredTableSummaries: List[ConfiguredTableSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DifferentialPrivacyConfigurationTypeDef(BaseModel):
    columns: List[DifferentialPrivacyColumnTypeDef]

class DifferentialPrivacyParametersTypeDef(BaseModel):
    sensitivityParameters: List[DifferentialPrivacySensitivityParametersTypeDef]

class DifferentialPrivacyPrivacyImpactTypeDef(BaseModel):
    aggregations: List[DifferentialPrivacyPreviewAggregationTypeDef]

class PreviewPrivacyImpactParametersInputTypeDef(BaseModel):
    differentialPrivacy: Optional[DifferentialPrivacyPreviewParametersInputTypeDef] = None

class DifferentialPrivacyPrivacyBudgetTypeDef(BaseModel):
    aggregations: List[DifferentialPrivacyPrivacyBudgetAggregationTypeDef]
    epsilon: int

class PrivacyBudgetTemplateParametersInputTypeDef(BaseModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersInputTypeDef] = None

class PrivacyBudgetTemplateParametersOutputTypeDef(BaseModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateParametersOutputTypeDef] = None

class PrivacyBudgetTemplateUpdateParametersTypeDef(BaseModel):
    differentialPrivacy: Optional[DifferentialPrivacyTemplateUpdateParametersTypeDef] = None

class TableReferenceTypeDef(BaseModel):
    glue: Optional[GlueTableReferenceTypeDef] = None

class ListAnalysisTemplatesInputListAnalysisTemplatesPaginateTypeDef(BaseModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationConfiguredAudienceModelAssociationsInputListCollaborationConfiguredAudienceModelAssociationsPaginateTypeDef(BaseModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationPrivacyBudgetTemplatesInputListCollaborationPrivacyBudgetTemplatesPaginateTypeDef(BaseModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationPrivacyBudgetsInputListCollaborationPrivacyBudgetsPaginateTypeDef(BaseModel):
    collaborationIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCollaborationsInputListCollaborationsPaginateTypeDef(BaseModel):
    memberStatus: Optional[FilterableMemberStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredAudienceModelAssociationsInputListConfiguredAudienceModelAssociationsPaginateTypeDef(BaseModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredTableAssociationsInputListConfiguredTableAssociationsPaginateTypeDef(BaseModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredTablesInputListConfiguredTablesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersInputListMembersPaginateTypeDef(BaseModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembershipsInputListMembershipsPaginateTypeDef(BaseModel):
    status: Optional[MembershipStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivacyBudgetTemplatesInputListPrivacyBudgetTemplatesPaginateTypeDef(BaseModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivacyBudgetsInputListPrivacyBudgetsPaginateTypeDef(BaseModel):
    membershipIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProtectedQueriesInputListProtectedQueriesPaginateTypeDef(BaseModel):
    membershipIdentifier: str
    status: Optional[ProtectedQueryStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasInputListSchemasPaginateTypeDef(BaseModel):
    collaborationIdentifier: str
    schemaType: Optional[Literal["TABLE"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrivacyBudgetTemplatesOutputTypeDef(BaseModel):
    nextToken: str
    privacyBudgetTemplateSummaries: List[PrivacyBudgetTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectedQueriesOutputTypeDef(BaseModel):
    nextToken: str
    protectedQueries: List[ProtectedQuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemasOutputTypeDef(BaseModel):
    schemaSummaries: List[SchemaSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MembershipPaymentConfigurationTypeDef(BaseModel):
    queryCompute: MembershipQueryComputePaymentConfigTypeDef

class MembershipProtectedQueryOutputConfigurationTypeDef(BaseModel):
    s3: Optional[ProtectedQueryS3OutputConfigurationTypeDef] = None

class ProtectedQueryOutputConfigurationTypeDef(BaseModel):
    s3: Optional[ProtectedQueryS3OutputConfigurationTypeDef] = None

class PaymentConfigurationTypeDef(BaseModel):
    queryCompute: QueryComputePaymentConfigTypeDef

class ProtectedQueryOutputTypeDef(BaseModel):
    s3: Optional[ProtectedQueryS3OutputTypeDef] = None
    memberList: Optional[List[ProtectedQuerySingleMemberOutputTypeDef]] = None

class SchemaStatusDetailTypeDef(BaseModel):
    status: SchemaStatusType
    reasons: Optional[List[SchemaStatusReasonTypeDef]] = None
    analysisRuleType: Optional[AnalysisRuleTypeType] = None
    configurations: Optional[List[Literal["DIFFERENTIAL_PRIVACY"]]] = None

class AnalysisTemplateTypeDef(BaseModel):
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

class CollaborationAnalysisTemplateTypeDef(BaseModel):
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

class CreateCollaborationOutputTypeDef(BaseModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationOutputTypeDef(BaseModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCollaborationOutputTypeDef(BaseModel):
    collaboration: CollaborationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRuleCustomTypeDef(BaseModel):
    allowedAnalyses: List[str]
    allowedAnalysisProviders: Optional[List[str]] = None
    differentialPrivacy: Optional[DifferentialPrivacyConfigurationTypeDef] = None

class PrivacyImpactTypeDef(BaseModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyImpactTypeDef] = None

class PreviewPrivacyImpactInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    parameters: PreviewPrivacyImpactParametersInputTypeDef

class PrivacyBudgetTypeDef(BaseModel):
    differentialPrivacy: Optional[DifferentialPrivacyPrivacyBudgetTypeDef] = None

class CreatePrivacyBudgetTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    autoRefresh: PrivacyBudgetTemplateAutoRefreshType
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: PrivacyBudgetTemplateParametersInputTypeDef
    tags: Optional[Mapping[str, str]] = None

class CollaborationPrivacyBudgetTemplateTypeDef(BaseModel):
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

class PrivacyBudgetTemplateTypeDef(BaseModel):
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

class UpdatePrivacyBudgetTemplateInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    privacyBudgetTemplateIdentifier: str
    privacyBudgetType: Literal["DIFFERENTIAL_PRIVACY"]
    parameters: Optional[PrivacyBudgetTemplateUpdateParametersTypeDef] = None

class ConfiguredTableTypeDef(BaseModel):
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

class CreateConfiguredTableInputRequestTypeDef(BaseModel):
    name: str
    tableReference: TableReferenceTypeDef
    allowedColumns: Sequence[str]
    analysisMethod: Literal["DIRECT_QUERY"]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class MembershipSummaryTypeDef(BaseModel):
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

class MembershipProtectedQueryResultConfigurationTypeDef(BaseModel):
    outputConfiguration: MembershipProtectedQueryOutputConfigurationTypeDef
    roleArn: Optional[str] = None

class ProtectedQueryResultConfigurationTypeDef(BaseModel):
    outputConfiguration: ProtectedQueryOutputConfigurationTypeDef

class MemberSpecificationTypeDef(BaseModel):
    accountId: str
    memberAbilities: Sequence[MemberAbilityType]
    displayName: str
    paymentConfiguration: Optional[PaymentConfigurationTypeDef] = None

class MemberSummaryTypeDef(BaseModel):
    accountId: str
    status: MemberStatusType
    displayName: str
    abilities: List[MemberAbilityType]
    createTime: datetime
    updateTime: datetime
    paymentConfiguration: PaymentConfigurationTypeDef
    membershipId: Optional[str] = None
    membershipArn: Optional[str] = None

class ProtectedQueryResultTypeDef(BaseModel):
    output: ProtectedQueryOutputTypeDef

class SchemaTypeDef(BaseModel):
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

class CreateAnalysisTemplateOutputTypeDef(BaseModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAnalysisTemplateOutputTypeDef(BaseModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnalysisTemplateOutputTypeDef(BaseModel):
    analysisTemplate: AnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetCollaborationAnalysisTemplateOutputTypeDef(BaseModel):
    collaborationAnalysisTemplates: List[CollaborationAnalysisTemplateTypeDef]
    errors: List[BatchGetCollaborationAnalysisTemplateErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCollaborationAnalysisTemplateOutputTypeDef(BaseModel):
    collaborationAnalysisTemplate: CollaborationAnalysisTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRulePolicyV1TypeDef(BaseModel):
    list: Optional[AnalysisRuleListTypeDef] = None
    aggregation: Optional[AnalysisRuleAggregationTypeDef] = None
    custom: Optional[AnalysisRuleCustomTypeDef] = None

class ConfiguredTableAnalysisRulePolicyV1TypeDef(BaseModel):
    list: Optional[AnalysisRuleListTypeDef] = None
    aggregation: Optional[AnalysisRuleAggregationTypeDef] = None
    custom: Optional[AnalysisRuleCustomTypeDef] = None

class PreviewPrivacyImpactOutputTypeDef(BaseModel):
    privacyImpact: PrivacyImpactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CollaborationPrivacyBudgetSummaryTypeDef(BaseModel):
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

class PrivacyBudgetSummaryTypeDef(BaseModel):
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

class GetCollaborationPrivacyBudgetTemplateOutputTypeDef(BaseModel):
    collaborationPrivacyBudgetTemplate: CollaborationPrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrivacyBudgetTemplateOutputTypeDef(BaseModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrivacyBudgetTemplateOutputTypeDef(BaseModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivacyBudgetTemplateOutputTypeDef(BaseModel):
    privacyBudgetTemplate: PrivacyBudgetTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableOutputTypeDef(BaseModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableOutputTypeDef(BaseModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableOutputTypeDef(BaseModel):
    configuredTable: ConfiguredTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembershipsOutputTypeDef(BaseModel):
    nextToken: str
    membershipSummaries: List[MembershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembershipInputRequestTypeDef(BaseModel):
    collaborationIdentifier: str
    queryLogStatus: MembershipQueryLogStatusType
    tags: Optional[Mapping[str, str]] = None
    defaultResultConfiguration: Optional[       MembershipProtectedQueryResultConfigurationTypeDef     ] = None
    paymentConfiguration: Optional[MembershipPaymentConfigurationTypeDef] = None

class MembershipTypeDef(BaseModel):
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

class UpdateMembershipInputRequestTypeDef(BaseModel):
    membershipIdentifier: str
    queryLogStatus: Optional[MembershipQueryLogStatusType] = None
    defaultResultConfiguration: Optional[       MembershipProtectedQueryResultConfigurationTypeDef     ] = None

class StartProtectedQueryInputRequestTypeDef(BaseModel):
    type: Literal["SQL"]
    membershipIdentifier: str
    sqlParameters: ProtectedQuerySQLParametersTypeDef
    resultConfiguration: Optional[ProtectedQueryResultConfigurationTypeDef] = None

class CreateCollaborationInputRequestTypeDef(BaseModel):
    members: Sequence[MemberSpecificationTypeDef]
    name: str
    description: str
    creatorMemberAbilities: Sequence[MemberAbilityType]
    creatorDisplayName: str
    queryLogStatus: CollaborationQueryLogStatusType
    dataEncryptionMetadata: Optional[DataEncryptionMetadataTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    creatorPaymentConfiguration: Optional[PaymentConfigurationTypeDef] = None

class ListMembersOutputTypeDef(BaseModel):
    nextToken: str
    memberSummaries: List[MemberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProtectedQueryTypeDef(BaseModel):
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

class BatchGetSchemaOutputTypeDef(BaseModel):
    schemas: List[SchemaTypeDef]
    errors: List[BatchGetSchemaErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaOutputTypeDef(BaseModel):
    schema: SchemaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRulePolicyTypeDef(BaseModel):
    v1: Optional[AnalysisRulePolicyV1TypeDef] = None

class ConfiguredTableAnalysisRulePolicyTypeDef(BaseModel):
    v1: Optional[ConfiguredTableAnalysisRulePolicyV1TypeDef] = None

class ListCollaborationPrivacyBudgetsOutputTypeDef(BaseModel):
    collaborationPrivacyBudgetSummaries: List[CollaborationPrivacyBudgetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrivacyBudgetsOutputTypeDef(BaseModel):
    privacyBudgetSummaries: List[PrivacyBudgetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMembershipOutputTypeDef(BaseModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMembershipOutputTypeDef(BaseModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMembershipOutputTypeDef(BaseModel):
    membership: MembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProtectedQueryOutputTypeDef(BaseModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartProtectedQueryOutputTypeDef(BaseModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProtectedQueryOutputTypeDef(BaseModel):
    protectedQuery: ProtectedQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisRuleTypeDef(BaseModel):
    collaborationId: str
    type: AnalysisRuleTypeType
    name: str
    createTime: datetime
    updateTime: datetime
    policy: AnalysisRulePolicyTypeDef

class ConfiguredTableAnalysisRuleTypeDef(BaseModel):
    configuredTableId: str
    configuredTableArn: str
    policy: ConfiguredTableAnalysisRulePolicyTypeDef
    type: ConfiguredTableAnalysisRuleTypeType
    createTime: datetime
    updateTime: datetime

class CreateConfiguredTableAnalysisRuleInputRequestTypeDef(BaseModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyTypeDef

class UpdateConfiguredTableAnalysisRuleInputRequestTypeDef(BaseModel):
    configuredTableIdentifier: str
    analysisRuleType: ConfiguredTableAnalysisRuleTypeType
    analysisRulePolicy: ConfiguredTableAnalysisRulePolicyTypeDef

class BatchGetSchemaAnalysisRuleOutputTypeDef(BaseModel):
    analysisRules: List[AnalysisRuleTypeDef]
    errors: List[BatchGetSchemaAnalysisRuleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaAnalysisRuleOutputTypeDef(BaseModel):
    analysisRule: AnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredTableAnalysisRuleOutputTypeDef(BaseModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredTableAnalysisRuleOutputTypeDef(BaseModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredTableAnalysisRuleOutputTypeDef(BaseModel):
    analysisRule: ConfiguredTableAnalysisRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

