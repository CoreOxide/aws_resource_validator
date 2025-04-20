from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.entityresolution.entityresolution_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AddPolicyStatementInput(BaseValidatorModel):
    action: List[str]
    arn: str
    effect: StatementEffectType
    principal: List[str]
    statementId: str
    condition: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteUniqueIdInput(BaseValidatorModel):
    uniqueIds: List[str]
    workflowName: str
    inputSource: Optional[str] = None


class DeleteUniqueIdError(BaseValidatorModel):
    errorType: DeleteUniqueIdErrorTypeType
    uniqueId: str


class DeletedUniqueId(BaseValidatorModel):
    uniqueId: str


class IdMappingWorkflowInputSource(BaseValidatorModel):
    inputSourceARN: str
    schemaName: Optional[str] = None
    type: Optional[IdNamespaceTypeType] = None


class IdMappingWorkflowOutputSource(BaseValidatorModel):
    outputS3Path: str
    KMSArn: Optional[str] = None


class IdNamespaceInputSource(BaseValidatorModel):
    inputSourceARN: str
    schemaName: Optional[str] = None


class IncrementalRunConfig(BaseValidatorModel):
    incrementalRunType: Optional[Literal['IMMEDIATE']] = None


class InputSource(BaseValidatorModel):
    inputSourceARN: str
    schemaName: str
    applyNormalization: Optional[bool] = None


class SchemaInputAttribute(BaseValidatorModel):
    fieldName: str
    type: SchemaAttributeTypeType
    groupName: Optional[str] = None
    hashed: Optional[bool] = None
    matchKey: Optional[str] = None
    subType: Optional[str] = None


class DeleteIdMappingWorkflowInput(BaseValidatorModel):
    workflowName: str


class DeleteIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str


class DeleteMatchingWorkflowInput(BaseValidatorModel):
    workflowName: str


class DeletePolicyStatementInput(BaseValidatorModel):
    arn: str
    statementId: str


class DeleteSchemaMappingInput(BaseValidatorModel):
    schemaName: str


class ErrorDetails(BaseValidatorModel):
    errorMessage: Optional[str] = None


class GetIdMappingJobInput(BaseValidatorModel):
    jobId: str
    workflowName: str


class IdMappingJobMetrics(BaseValidatorModel):
    inputRecords: Optional[int] = None
    recordsNotProcessed: Optional[int] = None
    totalMappedRecords: Optional[int] = None
    totalMappedSourceRecords: Optional[int] = None
    totalMappedTargetRecords: Optional[int] = None
    totalRecordsProcessed: Optional[int] = None


class IdMappingJobOutputSource(BaseValidatorModel):
    outputS3Path: str
    roleArn: str
    KMSArn: Optional[str] = None


class GetIdMappingWorkflowInput(BaseValidatorModel):
    workflowName: str


class GetIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str


class GetMatchIdInput(BaseValidatorModel):
    record: Dict[str, str]
    workflowName: str
    applyNormalization: Optional[bool] = None


class GetMatchingJobInput(BaseValidatorModel):
    jobId: str
    workflowName: str


class JobMetrics(BaseValidatorModel):
    inputRecords: Optional[int] = None
    matchIDs: Optional[int] = None
    recordsNotProcessed: Optional[int] = None
    totalRecordsProcessed: Optional[int] = None


class JobOutputSource(BaseValidatorModel):
    outputS3Path: str
    roleArn: str
    KMSArn: Optional[str] = None


class GetMatchingWorkflowInput(BaseValidatorModel):
    workflowName: str


class GetPolicyInput(BaseValidatorModel):
    arn: str


class GetProviderServiceInput(BaseValidatorModel):
    providerName: str
    providerServiceName: str


class ProviderIdNameSpaceConfiguration(BaseValidatorModel):
    description: Optional[str] = None
    providerSourceConfigurationDefinition: Optional[Dict[str, Any]] = None
    providerTargetConfigurationDefinition: Optional[Dict[str, Any]] = None


class ProviderIntermediateDataAccessConfiguration(BaseValidatorModel):
    awsAccountIds: Optional[List[str]] = None
    requiredBucketActions: Optional[List[str]] = None


class GetSchemaMappingInput(BaseValidatorModel):
    schemaName: str


class RuleOutput(BaseValidatorModel):
    matchingKeys: List[str]
    ruleName: str


class Rule(BaseValidatorModel):
    matchingKeys: List[str]
    ruleName: str


class IdMappingWorkflowSummary(BaseValidatorModel):
    createdAt: datetime
    updatedAt: datetime
    workflowArn: str
    workflowName: str


class IdNamespaceIdMappingWorkflowMetadata(BaseValidatorModel):
    idMappingType: IdMappingTypeType


class NamespaceProviderPropertiesOutput(BaseValidatorModel):
    providerServiceArn: str
    providerConfiguration: Optional[Dict[str, Any]] = None


class IntermediateSourceConfiguration(BaseValidatorModel):
    intermediateS3Path: str


class JobSummary(BaseValidatorModel):
    jobId: str
    startTime: datetime
    status: JobStatusType
    endTime: Optional[datetime] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIdMappingJobsInput(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdMappingWorkflowsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListIdNamespacesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListMatchingJobsInput(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListMatchingWorkflowsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MatchingWorkflowSummary(BaseValidatorModel):
    createdAt: datetime
    resolutionType: ResolutionTypeType
    updatedAt: datetime
    workflowArn: str
    workflowName: str


class ListProviderServicesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    providerName: Optional[str] = None


class ProviderServiceSummary(BaseValidatorModel):
    providerName: str
    providerServiceArn: str
    providerServiceDisplayName: str
    providerServiceName: str
    providerServiceType: ServiceTypeType


class ListSchemaMappingsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SchemaMappingSummary(BaseValidatorModel):
    createdAt: datetime
    hasWorkflows: bool
    schemaArn: str
    schemaName: str
    updatedAt: datetime


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class NamespaceProviderProperties(BaseValidatorModel):
    providerServiceArn: str
    providerConfiguration: Optional[Dict[str, Any]] = None


class OutputAttribute(BaseValidatorModel):
    name: str
    hashed: Optional[bool] = None


class ProviderSchemaAttribute(BaseValidatorModel):
    fieldName: str
    type: SchemaAttributeTypeType
    hashing: Optional[bool] = None
    subType: Optional[str] = None


class ProviderMarketplaceConfiguration(BaseValidatorModel):
    assetId: str
    dataSetId: str
    listingId: str
    revisionId: str


class PutPolicyInput(BaseValidatorModel):
    arn: str
    policy: str
    token: Optional[str] = None


class StartMatchingJobInput(BaseValidatorModel):
    workflowName: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class AddPolicyStatementOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


class DeleteIdMappingWorkflowOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


class DeleteIdNamespaceOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


class DeleteMatchingWorkflowOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


class DeletePolicyStatementOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


class DeleteSchemaMappingOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


class GetMatchIdOutput(BaseValidatorModel):
    matchId: str
    matchRule: str
    ResponseMetadata: ResponseMetadata


class GetPolicyOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutPolicyOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


class StartMatchingJobOutput(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


class BatchDeleteUniqueIdOutput(BaseValidatorModel):
    deleted: List[DeletedUniqueId]
    disconnectedUniqueIds: List[str]
    errors: List[DeleteUniqueIdError]
    status: DeleteUniqueIdStatusType
    ResponseMetadata: ResponseMetadata


class CreateSchemaMappingInput(BaseValidatorModel):
    mappedInputFields: List[SchemaInputAttribute]
    schemaName: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateSchemaMappingOutput(BaseValidatorModel):
    description: str
    mappedInputFields: List[SchemaInputAttribute]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadata


class GetSchemaMappingOutput(BaseValidatorModel):
    createdAt: datetime
    description: str
    hasWorkflows: bool
    mappedInputFields: List[SchemaInputAttribute]
    schemaArn: str
    schemaName: str
    tags: Dict[str, str]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateSchemaMappingInput(BaseValidatorModel):
    mappedInputFields: List[SchemaInputAttribute]
    schemaName: str
    description: Optional[str] = None


class UpdateSchemaMappingOutput(BaseValidatorModel):
    description: str
    mappedInputFields: List[SchemaInputAttribute]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadata


class GetIdMappingJobOutput(BaseValidatorModel):
    endTime: datetime
    errorDetails: ErrorDetails
    jobId: str
    metrics: IdMappingJobMetrics
    outputSourceConfig: List[IdMappingJobOutputSource]
    startTime: datetime
    status: JobStatusType
    ResponseMetadata: ResponseMetadata


class StartIdMappingJobInput(BaseValidatorModel):
    workflowName: str
    outputSourceConfig: Optional[List[IdMappingJobOutputSource]] = None


class StartIdMappingJobOutput(BaseValidatorModel):
    jobId: str
    outputSourceConfig: List[IdMappingJobOutputSource]
    ResponseMetadata: ResponseMetadata


class GetMatchingJobOutput(BaseValidatorModel):
    endTime: datetime
    errorDetails: ErrorDetails
    jobId: str
    metrics: JobMetrics
    outputSourceConfig: List[JobOutputSource]
    startTime: datetime
    status: JobStatusType
    ResponseMetadata: ResponseMetadata


class IdMappingRuleBasedPropertiesOutput(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    recordMatchingModel: RecordMatchingModelType
    ruleDefinitionType: IdMappingWorkflowRuleDefinitionTypeType
    rules: Optional[List[RuleOutput]] = None


class NamespaceRuleBasedPropertiesOutput(BaseValidatorModel):
    attributeMatchingModel: Optional[AttributeMatchingModelType] = None
    recordMatchingModels: Optional[List[RecordMatchingModelType]] = None
    ruleDefinitionTypes: Optional[List[IdMappingWorkflowRuleDefinitionTypeType]] = None
    rules: Optional[List[RuleOutput]] = None


class RuleBasedPropertiesOutput(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    rules: List[RuleOutput]
    matchPurpose: Optional[MatchPurposeType] = None


class IdMappingRuleBasedProperties(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    recordMatchingModel: RecordMatchingModelType
    ruleDefinitionType: IdMappingWorkflowRuleDefinitionTypeType
    rules: Optional[List[Rule]] = None


class RuleBasedProperties(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    rules: List[Rule]
    matchPurpose: Optional[MatchPurposeType] = None

RuleUnion = Union[Rule, RuleOutput]


class ListIdMappingWorkflowsOutput(BaseValidatorModel):
    workflowSummaries: List[IdMappingWorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IdNamespaceSummary(BaseValidatorModel):
    createdAt: datetime
    idNamespaceArn: str
    idNamespaceName: str
    type: IdNamespaceTypeType
    updatedAt: datetime
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[List[IdNamespaceIdMappingWorkflowMetadata]] = None


class ProviderPropertiesOutput(BaseValidatorModel):
    providerServiceArn: str
    intermediateSourceConfiguration: Optional[IntermediateSourceConfiguration] = None
    providerConfiguration: Optional[Dict[str, Any]] = None


class ProviderProperties(BaseValidatorModel):
    providerServiceArn: str
    intermediateSourceConfiguration: Optional[IntermediateSourceConfiguration] = None
    providerConfiguration: Optional[Dict[str, Any]] = None


class ListIdMappingJobsOutput(BaseValidatorModel):
    jobs: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMatchingJobsOutput(BaseValidatorModel):
    jobs: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListIdMappingJobsInputPaginate(BaseValidatorModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIdMappingWorkflowsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIdNamespacesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMatchingJobsInputPaginate(BaseValidatorModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMatchingWorkflowsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProviderServicesInputPaginate(BaseValidatorModel):
    providerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemaMappingsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMatchingWorkflowsOutput(BaseValidatorModel):
    workflowSummaries: List[MatchingWorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListProviderServicesOutput(BaseValidatorModel):
    providerServiceSummaries: List[ProviderServiceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSchemaMappingsOutput(BaseValidatorModel):
    schemaList: List[SchemaMappingSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

NamespaceProviderPropertiesUnion = Union[NamespaceProviderProperties, NamespaceProviderPropertiesOutput]


class OutputSourceOutput(BaseValidatorModel):
    output: List[OutputAttribute]
    outputS3Path: str
    KMSArn: Optional[str] = None
    applyNormalization: Optional[bool] = None


class OutputSource(BaseValidatorModel):
    output: List[OutputAttribute]
    outputS3Path: str
    KMSArn: Optional[str] = None
    applyNormalization: Optional[bool] = None


class ProviderComponentSchema(BaseValidatorModel):
    providerSchemaAttributes: Optional[List[ProviderSchemaAttribute]] = None
    schemas: Optional[List[List[str]]] = None


class ProviderEndpointConfiguration(BaseValidatorModel):
    marketplaceConfiguration: Optional[ProviderMarketplaceConfiguration] = None


class IdNamespaceIdMappingWorkflowPropertiesOutput(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[NamespaceProviderPropertiesOutput] = None
    ruleBasedProperties: Optional[NamespaceRuleBasedPropertiesOutput] = None


class NamespaceRuleBasedProperties(BaseValidatorModel):
    attributeMatchingModel: Optional[AttributeMatchingModelType] = None
    recordMatchingModels: Optional[List[RecordMatchingModelType]] = None
    ruleDefinitionTypes: Optional[List[IdMappingWorkflowRuleDefinitionTypeType]] = None
    rules: Optional[List[RuleUnion]] = None


class ListIdNamespacesOutput(BaseValidatorModel):
    idNamespaceSummaries: List[IdNamespaceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IdMappingTechniquesOutput(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[ProviderPropertiesOutput] = None
    ruleBasedProperties: Optional[IdMappingRuleBasedPropertiesOutput] = None


class ResolutionTechniquesOutput(BaseValidatorModel):
    resolutionType: ResolutionTypeType
    providerProperties: Optional[ProviderPropertiesOutput] = None
    ruleBasedProperties: Optional[RuleBasedPropertiesOutput] = None


class IdMappingTechniques(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[ProviderProperties] = None
    ruleBasedProperties: Optional[IdMappingRuleBasedProperties] = None


class ResolutionTechniques(BaseValidatorModel):
    resolutionType: ResolutionTypeType
    providerProperties: Optional[ProviderProperties] = None
    ruleBasedProperties: Optional[RuleBasedProperties] = None

OutputSourceUnion = Union[OutputSource, OutputSourceOutput]


class GetProviderServiceOutput(BaseValidatorModel):
    anonymizedOutput: bool
    providerComponentSchema: ProviderComponentSchema
    providerConfigurationDefinition: Dict[str, Any]
    providerEndpointConfiguration: ProviderEndpointConfiguration
    providerEntityOutputDefinition: Dict[str, Any]
    providerIdNameSpaceConfiguration: ProviderIdNameSpaceConfiguration
    providerIntermediateDataAccessConfiguration: ProviderIntermediateDataAccessConfiguration
    providerJobConfiguration: Dict[str, Any]
    providerName: str
    providerServiceArn: str
    providerServiceDisplayName: str
    providerServiceName: str
    providerServiceType: ServiceTypeType
    ResponseMetadata: ResponseMetadata


class CreateIdNamespaceOutput(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingWorkflowProperties: List[IdNamespaceIdMappingWorkflowPropertiesOutput]
    idNamespaceArn: str
    idNamespaceName: str
    inputSourceConfig: List[IdNamespaceInputSource]
    roleArn: str
    tags: Dict[str, str]
    type: IdNamespaceTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetIdNamespaceOutput(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingWorkflowProperties: List[IdNamespaceIdMappingWorkflowPropertiesOutput]
    idNamespaceArn: str
    idNamespaceName: str
    inputSourceConfig: List[IdNamespaceInputSource]
    roleArn: str
    tags: Dict[str, str]
    type: IdNamespaceTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class UpdateIdNamespaceOutput(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingWorkflowProperties: List[IdNamespaceIdMappingWorkflowPropertiesOutput]
    idNamespaceArn: str
    idNamespaceName: str
    inputSourceConfig: List[IdNamespaceInputSource]
    roleArn: str
    type: IdNamespaceTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata

NamespaceRuleBasedPropertiesUnion = Union[NamespaceRuleBasedProperties, NamespaceRuleBasedPropertiesOutput]


class CreateIdMappingWorkflowOutput(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesOutput
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    outputSourceConfig: List[IdMappingWorkflowOutputSource]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata


class GetIdMappingWorkflowOutput(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingTechniques: IdMappingTechniquesOutput
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    outputSourceConfig: List[IdMappingWorkflowOutputSource]
    roleArn: str
    tags: Dict[str, str]
    updatedAt: datetime
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata


class UpdateIdMappingWorkflowOutput(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesOutput
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    outputSourceConfig: List[IdMappingWorkflowOutputSource]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata


class CreateMatchingWorkflowOutput(BaseValidatorModel):
    description: str
    incrementalRunConfig: IncrementalRunConfig
    inputSourceConfig: List[InputSource]
    outputSourceConfig: List[OutputSourceOutput]
    resolutionTechniques: ResolutionTechniquesOutput
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata


class GetMatchingWorkflowOutput(BaseValidatorModel):
    createdAt: datetime
    description: str
    incrementalRunConfig: IncrementalRunConfig
    inputSourceConfig: List[InputSource]
    outputSourceConfig: List[OutputSourceOutput]
    resolutionTechniques: ResolutionTechniquesOutput
    roleArn: str
    tags: Dict[str, str]
    updatedAt: datetime
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata


class UpdateMatchingWorkflowOutput(BaseValidatorModel):
    description: str
    incrementalRunConfig: IncrementalRunConfig
    inputSourceConfig: List[InputSource]
    outputSourceConfig: List[OutputSourceOutput]
    resolutionTechniques: ResolutionTechniquesOutput
    roleArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata

IdMappingTechniquesUnion = Union[IdMappingTechniques, IdMappingTechniquesOutput]

ResolutionTechniquesUnion = Union[ResolutionTechniques, ResolutionTechniquesOutput]


class IdNamespaceIdMappingWorkflowProperties(BaseValidatorModel):
    idMappingType: IdMappingTypeType
    providerProperties: Optional[NamespaceProviderPropertiesUnion] = None
    ruleBasedProperties: Optional[NamespaceRuleBasedPropertiesUnion] = None


class CreateIdMappingWorkflowInput(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesUnion
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[List[IdMappingWorkflowOutputSource]] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateIdMappingWorkflowInput(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesUnion
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[List[IdMappingWorkflowOutputSource]] = None
    roleArn: Optional[str] = None


class CreateMatchingWorkflowInput(BaseValidatorModel):
    inputSourceConfig: List[InputSource]
    outputSourceConfig: List[OutputSourceUnion]
    resolutionTechniques: ResolutionTechniquesUnion
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfig] = None
    tags: Optional[Dict[str, str]] = None


class UpdateMatchingWorkflowInput(BaseValidatorModel):
    inputSourceConfig: List[InputSource]
    outputSourceConfig: List[OutputSourceUnion]
    resolutionTechniques: ResolutionTechniquesUnion
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfig] = None

IdNamespaceIdMappingWorkflowPropertiesUnion = Union[IdNamespaceIdMappingWorkflowProperties, IdNamespaceIdMappingWorkflowPropertiesOutput]


class CreateIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str
    type: IdNamespaceTypeType
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[List[IdNamespaceIdMappingWorkflowPropertiesUnion]] = None
    inputSourceConfig: Optional[List[IdNamespaceInputSource]] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[List[IdNamespaceIdMappingWorkflowPropertiesUnion]] = None
    inputSourceConfig: Optional[List[IdNamespaceInputSource]] = None
    roleArn: Optional[str] = None