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
from aws_resource_validator.pydantic_models.entityresolution_constants import *

class AddPolicyStatementInputTypeDef(BaseValidatorModel):
    action: Sequence[str]
    arn: str
    effect: StatementEffectType
    principal: Sequence[str]
    statementId: str
    condition: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteUniqueIdInputTypeDef(BaseValidatorModel):
    uniqueIds: Sequence[str]
    workflowName: str
    inputSource: Optional[str] = None


class DeleteUniqueIdErrorTypeDef(BaseValidatorModel):
    errorType: DeleteUniqueIdErrorTypeType
    uniqueId: str


class DeletedUniqueIdTypeDef(BaseValidatorModel):
    uniqueId: str


class IdMappingWorkflowOutputSourceTypeDef(BaseValidatorModel):
    outputS3Path: str
    KMSArn: Optional[str] = None


class IdNamespaceInputSourceTypeDef(BaseValidatorModel):
    inputSourceARN: str
    schemaName: Optional[str] = None


class IncrementalRunConfigTypeDef(BaseValidatorModel):
    incrementalRunType: Optional[Literal["IMMEDIATE"]] = None


class InputSourceTypeDef(BaseValidatorModel):
    inputSourceARN: str
    schemaName: str
    applyNormalization: Optional[bool] = None


class DeleteIdMappingWorkflowInputTypeDef(BaseValidatorModel):
    workflowName: str


class DeleteIdNamespaceInputTypeDef(BaseValidatorModel):
    idNamespaceName: str


class DeleteMatchingWorkflowInputTypeDef(BaseValidatorModel):
    workflowName: str


class DeletePolicyStatementInputTypeDef(BaseValidatorModel):
    arn: str
    statementId: str


class DeleteSchemaMappingInputTypeDef(BaseValidatorModel):
    schemaName: str


class ErrorDetailsTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None


class GetIdMappingJobInputTypeDef(BaseValidatorModel):
    jobId: str
    workflowName: str


class IdMappingJobMetricsTypeDef(BaseValidatorModel):
    inputRecords: Optional[int] = None
    recordsNotProcessed: Optional[int] = None
    totalMappedRecords: Optional[int] = None
    totalMappedSourceRecords: Optional[int] = None
    totalMappedTargetRecords: Optional[int] = None
    totalRecordsProcessed: Optional[int] = None


class IdMappingJobOutputSourceTypeDef(BaseValidatorModel):
    outputS3Path: str
    roleArn: str
    KMSArn: Optional[str] = None


class GetIdMappingWorkflowInputTypeDef(BaseValidatorModel):
    workflowName: str


class GetIdNamespaceInputTypeDef(BaseValidatorModel):
    idNamespaceName: str


class GetMatchIdInputTypeDef(BaseValidatorModel):
    record: Mapping[str, str]
    workflowName: str
    applyNormalization: Optional[bool] = None


class GetMatchingJobInputTypeDef(BaseValidatorModel):
    jobId: str
    workflowName: str


class JobMetricsTypeDef(BaseValidatorModel):
    inputRecords: Optional[int] = None
    matchIDs: Optional[int] = None
    recordsNotProcessed: Optional[int] = None
    totalRecordsProcessed: Optional[int] = None


class JobOutputSourceTypeDef(BaseValidatorModel):
    outputS3Path: str
    roleArn: str
    KMSArn: Optional[str] = None


class GetMatchingWorkflowInputTypeDef(BaseValidatorModel):
    workflowName: str


class GetPolicyInputTypeDef(BaseValidatorModel):
    arn: str


class GetProviderServiceInputTypeDef(BaseValidatorModel):
    providerName: str
    providerServiceName: str


class ProviderIdNameSpaceConfigurationTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    providerSourceConfigurationDefinition: Optional[Dict[str, Any]] = None
    providerTargetConfigurationDefinition: Optional[Dict[str, Any]] = None


class ProviderIntermediateDataAccessConfigurationTypeDef(BaseValidatorModel):
    awsAccountIds: Optional[List[str]] = None
    requiredBucketActions: Optional[List[str]] = None


class GetSchemaMappingInputTypeDef(BaseValidatorModel):
    schemaName: str


class RuleOutputTypeDef(BaseValidatorModel):
    matchingKeys: List[str]
    ruleName: str


class RuleTypeDef(BaseValidatorModel):
    matchingKeys: Sequence[str]
    ruleName: str


class IdMappingWorkflowSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    updatedAt: datetime
    workflowArn: str
    workflowName: str


class IdNamespaceIdMappingWorkflowMetadataTypeDef(BaseValidatorModel):
    idMappingType: IdMappingTypeType


class NamespaceProviderPropertiesOutputTypeDef(BaseValidatorModel):
    providerServiceArn: str
    providerConfiguration: Optional[Dict[str, Any]] = None


class IntermediateSourceConfigurationTypeDef(BaseValidatorModel):
    intermediateS3Path: str


class JobSummaryTypeDef(BaseValidatorModel):
    jobId: str
    startTime: datetime
    status: JobStatusType
    endTime: Optional[datetime] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIdMappingJobsInputTypeDef(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdMappingWorkflowsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdNamespacesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListMatchingJobsInputTypeDef(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListMatchingWorkflowsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MatchingWorkflowSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    resolutionType: ResolutionTypeType
    updatedAt: datetime
    workflowArn: str
    workflowName: str


class ListProviderServicesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    providerName: Optional[str] = None


class ProviderServiceSummaryTypeDef(BaseValidatorModel):
    providerName: str
    providerServiceArn: str
    providerServiceDisplayName: str
    providerServiceName: str
    providerServiceType: ServiceTypeType


class ListSchemaMappingsInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SchemaMappingSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    hasWorkflows: bool
    schemaArn: str
    schemaName: str
    updatedAt: datetime


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class NamespaceProviderPropertiesTypeDef(BaseValidatorModel):
    providerServiceArn: str
    providerConfiguration: Optional[Mapping[str, Any]] = None


class OutputAttributeTypeDef(BaseValidatorModel):
    name: str
    hashed: Optional[bool] = None


class ProviderMarketplaceConfigurationTypeDef(BaseValidatorModel):
    assetId: str
    dataSetId: str
    listingId: str
    revisionId: str


class PutPolicyInputTypeDef(BaseValidatorModel):
    arn: str
    policy: str
    token: Optional[str] = None


class StartMatchingJobInputTypeDef(BaseValidatorModel):
    workflowName: str


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AddPolicyStatementOutputTypeDef(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteIdMappingWorkflowOutputTypeDef(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteIdNamespaceOutputTypeDef(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMatchingWorkflowOutputTypeDef(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePolicyStatementOutputTypeDef(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSchemaMappingOutputTypeDef(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMatchIdOutputTypeDef(BaseValidatorModel):
    matchId: str
    matchRule: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPolicyOutputTypeDef(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutPolicyOutputTypeDef(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMatchingJobOutputTypeDef(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteUniqueIdOutputTypeDef(BaseValidatorModel):
    deleted: List[DeletedUniqueIdTypeDef]
    disconnectedUniqueIds: List[str]
    errors: List[DeleteUniqueIdErrorTypeDef]
    status: DeleteUniqueIdStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class SchemaInputAttributeTypeDef(BaseValidatorModel):
    pass


class CreateSchemaMappingInputTypeDef(BaseValidatorModel):
    mappedInputFields: Sequence[SchemaInputAttributeTypeDef]
    schemaName: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateSchemaMappingOutputTypeDef(BaseValidatorModel):
    description: str
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaMappingOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    hasWorkflows: bool
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    schemaArn: str
    schemaName: str
    tags: Dict[str, str]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSchemaMappingInputTypeDef(BaseValidatorModel):
    mappedInputFields: Sequence[SchemaInputAttributeTypeDef]
    schemaName: str
    description: Optional[str] = None


class UpdateSchemaMappingOutputTypeDef(BaseValidatorModel):
    description: str
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetIdMappingJobOutputTypeDef(BaseValidatorModel):
    endTime: datetime
    errorDetails: ErrorDetailsTypeDef
    jobId: str
    metrics: IdMappingJobMetricsTypeDef
    outputSourceConfig: List[IdMappingJobOutputSourceTypeDef]
    startTime: datetime
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StartIdMappingJobInputTypeDef(BaseValidatorModel):
    workflowName: str
    outputSourceConfig: Optional[Sequence[IdMappingJobOutputSourceTypeDef]] = None


class StartIdMappingJobOutputTypeDef(BaseValidatorModel):
    jobId: str
    outputSourceConfig: List[IdMappingJobOutputSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetMatchingJobOutputTypeDef(BaseValidatorModel):
    endTime: datetime
    errorDetails: ErrorDetailsTypeDef
    jobId: str
    metrics: JobMetricsTypeDef
    outputSourceConfig: List[JobOutputSourceTypeDef]
    startTime: datetime
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class IdMappingRuleBasedPropertiesOutputTypeDef(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    recordMatchingModel: RecordMatchingModelType
    ruleDefinitionType: IdMappingWorkflowRuleDefinitionTypeType
    rules: Optional[List[RuleOutputTypeDef]] = None


class NamespaceRuleBasedPropertiesOutputTypeDef(BaseValidatorModel):
    attributeMatchingModel: Optional[AttributeMatchingModelType] = None
    recordMatchingModels: Optional[List[RecordMatchingModelType]] = None
    ruleDefinitionTypes: Optional[List[IdMappingWorkflowRuleDefinitionTypeType]] = None
    rules: Optional[List[RuleOutputTypeDef]] = None


class RuleBasedPropertiesOutputTypeDef(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    rules: List[RuleOutputTypeDef]
    matchPurpose: Optional[MatchPurposeType] = None


class IdMappingRuleBasedPropertiesTypeDef(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    recordMatchingModel: RecordMatchingModelType
    ruleDefinitionType: IdMappingWorkflowRuleDefinitionTypeType
    rules: Optional[Sequence[RuleTypeDef]] = None


class RuleBasedPropertiesTypeDef(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    rules: Sequence[RuleTypeDef]
    matchPurpose: Optional[MatchPurposeType] = None


class ListIdMappingWorkflowsOutputTypeDef(BaseValidatorModel):
    workflowSummaries: List[IdMappingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ProviderPropertiesOutputTypeDef(BaseValidatorModel):
    providerServiceArn: str
    intermediateSourceConfiguration: Optional[IntermediateSourceConfigurationTypeDef] = None
    providerConfiguration: Optional[Dict[str, Any]] = None


class ProviderPropertiesTypeDef(BaseValidatorModel):
    providerServiceArn: str
    intermediateSourceConfiguration: Optional[IntermediateSourceConfigurationTypeDef] = None
    providerConfiguration: Optional[Mapping[str, Any]] = None


class ListIdMappingJobsOutputTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMatchingJobsOutputTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListIdMappingJobsInputPaginateTypeDef(BaseValidatorModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIdMappingWorkflowsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIdNamespacesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMatchingJobsInputPaginateTypeDef(BaseValidatorModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMatchingWorkflowsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProviderServicesInputPaginateTypeDef(BaseValidatorModel):
    providerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemaMappingsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMatchingWorkflowsOutputTypeDef(BaseValidatorModel):
    workflowSummaries: List[MatchingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListProviderServicesOutputTypeDef(BaseValidatorModel):
    providerServiceSummaries: List[ProviderServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSchemaMappingsOutputTypeDef(BaseValidatorModel):
    schemaList: List[SchemaMappingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class OutputSourceOutputTypeDef(BaseValidatorModel):
    output: List[OutputAttributeTypeDef]
    outputS3Path: str
    KMSArn: Optional[str] = None
    applyNormalization: Optional[bool] = None


class OutputSourceTypeDef(BaseValidatorModel):
    output: Sequence[OutputAttributeTypeDef]
    outputS3Path: str
    KMSArn: Optional[str] = None
    applyNormalization: Optional[bool] = None


class ProviderSchemaAttributeTypeDef(BaseValidatorModel):
    pass


class ProviderComponentSchemaTypeDef(BaseValidatorModel):
    providerSchemaAttributes: Optional[List[ProviderSchemaAttributeTypeDef]] = None
    schemas: Optional[List[List[str]]] = None


class ProviderEndpointConfigurationTypeDef(BaseValidatorModel):
    marketplaceConfiguration: Optional[ProviderMarketplaceConfigurationTypeDef] = None


class IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[NamespaceProviderPropertiesOutputTypeDef] = None
    ruleBasedProperties: Optional[NamespaceRuleBasedPropertiesOutputTypeDef] = None


class RuleUnionTypeDef(BaseValidatorModel):
    pass


class NamespaceRuleBasedPropertiesTypeDef(BaseValidatorModel):
    attributeMatchingModel: Optional[AttributeMatchingModelType] = None
    recordMatchingModels: Optional[Sequence[RecordMatchingModelType]] = None
    ruleDefinitionTypes: Optional[Sequence[IdMappingWorkflowRuleDefinitionTypeType]] = None
    rules: Optional[Sequence[RuleUnionTypeDef]] = None


class IdNamespaceSummaryTypeDef(BaseValidatorModel):
    pass


class ListIdNamespacesOutputTypeDef(BaseValidatorModel):
    idNamespaceSummaries: List[IdNamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IdMappingTechniquesOutputTypeDef(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[ProviderPropertiesOutputTypeDef] = None
    ruleBasedProperties: Optional[IdMappingRuleBasedPropertiesOutputTypeDef] = None


class ResolutionTechniquesOutputTypeDef(BaseValidatorModel):
    resolutionType: ResolutionTypeType
    providerProperties: Optional[ProviderPropertiesOutputTypeDef] = None
    ruleBasedProperties: Optional[RuleBasedPropertiesOutputTypeDef] = None


class IdMappingTechniquesTypeDef(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[ProviderPropertiesTypeDef] = None
    ruleBasedProperties: Optional[IdMappingRuleBasedPropertiesTypeDef] = None


class ResolutionTechniquesTypeDef(BaseValidatorModel):
    resolutionType: ResolutionTypeType
    providerProperties: Optional[ProviderPropertiesTypeDef] = None
    ruleBasedProperties: Optional[RuleBasedPropertiesTypeDef] = None


class GetProviderServiceOutputTypeDef(BaseValidatorModel):
    anonymizedOutput: bool
    providerComponentSchema: ProviderComponentSchemaTypeDef
    providerConfigurationDefinition: Dict[str, Any]
    providerEndpointConfiguration: ProviderEndpointConfigurationTypeDef
    providerEntityOutputDefinition: Dict[str, Any]
    providerIdNameSpaceConfiguration: ProviderIdNameSpaceConfigurationTypeDef
    providerIntermediateDataAccessConfiguration: ProviderIntermediateDataAccessConfigurationTypeDef
    providerJobConfiguration: Dict[str, Any]
    providerName: str
    providerServiceArn: str
    providerServiceDisplayName: str
    providerServiceName: str
    providerServiceType: ServiceTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class IdMappingWorkflowInputSourceTypeDef(BaseValidatorModel):
    pass


class CreateIdMappingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesOutputTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetIdMappingWorkflowOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingTechniques: IdMappingTechniquesOutputTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    tags: Dict[str, str]
    updatedAt: datetime
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIdMappingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesOutputTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMatchingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceOutputTypeDef]
    resolutionTechniques: ResolutionTechniquesOutputTypeDef
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMatchingWorkflowOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceOutputTypeDef]
    resolutionTechniques: ResolutionTechniquesOutputTypeDef
    roleArn: str
    tags: Dict[str, str]
    updatedAt: datetime
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMatchingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceOutputTypeDef]
    resolutionTechniques: ResolutionTechniquesOutputTypeDef
    roleArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef


class NamespaceRuleBasedPropertiesUnionTypeDef(BaseValidatorModel):
    pass


class NamespaceProviderPropertiesUnionTypeDef(BaseValidatorModel):
    pass


class IdNamespaceIdMappingWorkflowPropertiesTypeDef(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[NamespaceProviderPropertiesUnionTypeDef] = None
    ruleBasedProperties: Optional[NamespaceRuleBasedPropertiesUnionTypeDef] = None


class IdMappingTechniquesUnionTypeDef(BaseValidatorModel):
    pass


class CreateIdMappingWorkflowInputTypeDef(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesUnionTypeDef
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[Sequence[IdMappingWorkflowOutputSourceTypeDef]] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateIdMappingWorkflowInputTypeDef(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesUnionTypeDef
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[Sequence[IdMappingWorkflowOutputSourceTypeDef]] = None
    roleArn: Optional[str] = None


class ResolutionTechniquesUnionTypeDef(BaseValidatorModel):
    pass


class OutputSourceUnionTypeDef(BaseValidatorModel):
    pass


class CreateMatchingWorkflowInputTypeDef(BaseValidatorModel):
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceUnionTypeDef]
    resolutionTechniques: ResolutionTechniquesUnionTypeDef
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateMatchingWorkflowInputTypeDef(BaseValidatorModel):
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceUnionTypeDef]
    resolutionTechniques: ResolutionTechniquesUnionTypeDef
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfigTypeDef] = None


class IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef(BaseValidatorModel):
    pass


class UpdateIdNamespaceInputTypeDef(BaseValidatorModel):
    idNamespaceName: str
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[ Sequence[IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef] ] = None
    inputSourceConfig: Optional[Sequence[IdNamespaceInputSourceTypeDef]] = None
    roleArn: Optional[str] = None


