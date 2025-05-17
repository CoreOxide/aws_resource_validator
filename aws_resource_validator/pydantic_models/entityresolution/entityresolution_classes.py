from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.entityresolution.entityresolution_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'add_policy_statement' function.
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


# This class is the input for the 'batch_delete_unique_id' function.
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


# This class is the input for the 'delete_id_mapping_workflow' function.
class DeleteIdMappingWorkflowInput(BaseValidatorModel):
    workflowName: str


# This class is the input for the 'delete_id_namespace' function.
class DeleteIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str


# This class is the input for the 'delete_matching_workflow' function.
class DeleteMatchingWorkflowInput(BaseValidatorModel):
    workflowName: str


# This class is the input for the 'delete_policy_statement' function.
class DeletePolicyStatementInput(BaseValidatorModel):
    arn: str
    statementId: str


# This class is the input for the 'delete_schema_mapping' function.
class DeleteSchemaMappingInput(BaseValidatorModel):
    schemaName: str


class ErrorDetails(BaseValidatorModel):
    errorMessage: Optional[str] = None


# This class is the input for the 'get_id_mapping_job' function.
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


# This class is the input for the 'get_id_mapping_workflow' function.
class GetIdMappingWorkflowInput(BaseValidatorModel):
    workflowName: str


# This class is the input for the 'get_id_namespace' function.
class GetIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str


# This class is the input for the 'get_match_id' function.
class GetMatchIdInput(BaseValidatorModel):
    record: Dict[str, str]
    workflowName: str
    applyNormalization: Optional[bool] = None


# This class is the input for the 'get_matching_job' function.
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


# This class is the input for the 'get_matching_workflow' function.
class GetMatchingWorkflowInput(BaseValidatorModel):
    workflowName: str


# This class is the input for the 'get_policy' function.
class GetPolicyInput(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_provider_service' function.
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


# This class is the input for the 'get_schema_mapping' function.
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


# This class is the input for the 'list_id_mapping_jobs' function.
class ListIdMappingJobsInput(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_id_mapping_workflows' function.
class ListIdMappingWorkflowsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_id_namespaces' function.
class ListIdNamespacesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_matching_jobs' function.
class ListMatchingJobsInput(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_matching_workflows' function.
class ListMatchingWorkflowsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MatchingWorkflowSummary(BaseValidatorModel):
    createdAt: datetime
    resolutionType: ResolutionTypeType
    updatedAt: datetime
    workflowArn: str
    workflowName: str


# This class is the input for the 'list_provider_services' function.
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


# This class is the input for the 'list_schema_mappings' function.
class ListSchemaMappingsInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SchemaMappingSummary(BaseValidatorModel):
    createdAt: datetime
    hasWorkflows: bool
    schemaArn: str
    schemaName: str
    updatedAt: datetime


# This class is the input for the 'list_tags_for_resource' function.
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


# This class is the input for the 'put_policy' function.
class PutPolicyInput(BaseValidatorModel):
    arn: str
    policy: str
    token: Optional[str] = None


# This class is the input for the 'start_matching_job' function.
class StartMatchingJobInput(BaseValidatorModel):
    workflowName: str


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the output for the 'add_policy_statement' function.
class AddPolicyStatementOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_id_mapping_workflow' function.
class DeleteIdMappingWorkflowOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_id_namespace' function.
class DeleteIdNamespaceOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_matching_workflow' function.
class DeleteMatchingWorkflowOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_policy_statement' function.
class DeletePolicyStatementOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_schema_mapping' function.
class DeleteSchemaMappingOutput(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_match_id' function.
class GetMatchIdOutput(BaseValidatorModel):
    matchId: str
    matchRule: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_policy' function.
class GetPolicyOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_policy' function.
class PutPolicyOutput(BaseValidatorModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_matching_job' function.
class StartMatchingJobOutput(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_delete_unique_id' function.
class BatchDeleteUniqueIdOutput(BaseValidatorModel):
    deleted: List[DeletedUniqueId]
    disconnectedUniqueIds: List[str]
    errors: List[DeleteUniqueIdError]
    status: DeleteUniqueIdStatusType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_schema_mapping' function.
class CreateSchemaMappingInput(BaseValidatorModel):
    mappedInputFields: List[SchemaInputAttribute]
    schemaName: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_schema_mapping' function.
class CreateSchemaMappingOutput(BaseValidatorModel):
    description: str
    mappedInputFields: List[SchemaInputAttribute]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_schema_mapping' function.
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


# This class is the input for the 'update_schema_mapping' function.
class UpdateSchemaMappingInput(BaseValidatorModel):
    mappedInputFields: List[SchemaInputAttribute]
    schemaName: str
    description: Optional[str] = None


# This class is the output for the 'update_schema_mapping' function.
class UpdateSchemaMappingOutput(BaseValidatorModel):
    description: str
    mappedInputFields: List[SchemaInputAttribute]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_id_mapping_job' function.
class GetIdMappingJobOutput(BaseValidatorModel):
    endTime: datetime
    errorDetails: ErrorDetails
    jobId: str
    metrics: IdMappingJobMetrics
    outputSourceConfig: List[IdMappingJobOutputSource]
    startTime: datetime
    status: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_id_mapping_job' function.
class StartIdMappingJobInput(BaseValidatorModel):
    workflowName: str
    outputSourceConfig: Optional[List[IdMappingJobOutputSource]] = None


# This class is the output for the 'start_id_mapping_job' function.
class StartIdMappingJobOutput(BaseValidatorModel):
    jobId: str
    outputSourceConfig: List[IdMappingJobOutputSource]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_matching_job' function.
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


# This class is the output for the 'list_id_mapping_workflows' function.
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


# This class is the output for the 'list_id_mapping_jobs' function.
class ListIdMappingJobsOutput(BaseValidatorModel):
    jobs: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_matching_jobs' function.
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


# This class is the output for the 'list_matching_workflows' function.
class ListMatchingWorkflowsOutput(BaseValidatorModel):
    workflowSummaries: List[MatchingWorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_provider_services' function.
class ListProviderServicesOutput(BaseValidatorModel):
    providerServiceSummaries: List[ProviderServiceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_schema_mappings' function.
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


# This class is the output for the 'list_id_namespaces' function.
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


# This class is the output for the 'get_provider_service' function.
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


# This class is the output for the 'create_id_namespace' function.
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


# This class is the output for the 'get_id_namespace' function.
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


# This class is the output for the 'update_id_namespace' function.
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


# This class is the output for the 'create_id_mapping_workflow' function.
class CreateIdMappingWorkflowOutput(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesOutput
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    outputSourceConfig: List[IdMappingWorkflowOutputSource]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_id_mapping_workflow' function.
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


# This class is the output for the 'update_id_mapping_workflow' function.
class UpdateIdMappingWorkflowOutput(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesOutput
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    outputSourceConfig: List[IdMappingWorkflowOutputSource]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_matching_workflow' function.
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


# This class is the output for the 'get_matching_workflow' function.
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


# This class is the output for the 'update_matching_workflow' function.
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


# This class is the input for the 'create_id_mapping_workflow' function.
class CreateIdMappingWorkflowInput(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesUnion
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[List[IdMappingWorkflowOutputSource]] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_id_mapping_workflow' function.
class UpdateIdMappingWorkflowInput(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesUnion
    inputSourceConfig: List[IdMappingWorkflowInputSource]
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[List[IdMappingWorkflowOutputSource]] = None
    roleArn: Optional[str] = None


# This class is the input for the 'create_matching_workflow' function.
class CreateMatchingWorkflowInput(BaseValidatorModel):
    inputSourceConfig: List[InputSource]
    outputSourceConfig: List[OutputSourceUnion]
    resolutionTechniques: ResolutionTechniquesUnion
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfig] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_matching_workflow' function.
class UpdateMatchingWorkflowInput(BaseValidatorModel):
    inputSourceConfig: List[InputSource]
    outputSourceConfig: List[OutputSourceUnion]
    resolutionTechniques: ResolutionTechniquesUnion
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfig] = None

IdNamespaceIdMappingWorkflowPropertiesUnion = Union[IdNamespaceIdMappingWorkflowProperties, IdNamespaceIdMappingWorkflowPropertiesOutput]


# This class is the input for the 'create_id_namespace' function.
class CreateIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str
    type: IdNamespaceTypeType
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[List[IdNamespaceIdMappingWorkflowPropertiesUnion]] = None
    inputSourceConfig: Optional[List[IdNamespaceInputSource]] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_id_namespace' function.
class UpdateIdNamespaceInput(BaseValidatorModel):
    idNamespaceName: str
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[List[IdNamespaceIdMappingWorkflowPropertiesUnion]] = None
    inputSourceConfig: Optional[List[IdNamespaceInputSource]] = None
    roleArn: Optional[str] = None