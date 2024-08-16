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
from aws_resource_validator.pydantic_models.entityresolution_constants import *

class AddPolicyStatementInputRequestTypeDef(BaseValidatorModel):
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

class BatchDeleteUniqueIdInputRequestTypeDef(BaseValidatorModel):
    uniqueIds: Sequence[str]
    workflowName: str
    inputSource: Optional[str] = None

class DeleteUniqueIdErrorTypeDef(BaseValidatorModel):
    errorType: DeleteUniqueIdErrorTypeType
    uniqueId: str

class DeletedUniqueIdTypeDef(BaseValidatorModel):
    uniqueId: str

class IdMappingWorkflowInputSourceTypeDef(BaseValidatorModel):
    inputSourceARN: str
    schemaName: Optional[str] = None
    type: Optional[IdNamespaceTypeType] = None

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

class SchemaInputAttributeTypeDef(BaseValidatorModel):
    fieldName: str
    type: SchemaAttributeTypeType
    groupName: Optional[str] = None
    matchKey: Optional[str] = None
    subType: Optional[str] = None

class DeleteIdMappingWorkflowInputRequestTypeDef(BaseValidatorModel):
    workflowName: str

class DeleteIdNamespaceInputRequestTypeDef(BaseValidatorModel):
    idNamespaceName: str

class DeleteMatchingWorkflowInputRequestTypeDef(BaseValidatorModel):
    workflowName: str

class DeletePolicyStatementInputRequestTypeDef(BaseValidatorModel):
    arn: str
    statementId: str

class DeleteSchemaMappingInputRequestTypeDef(BaseValidatorModel):
    schemaName: str

class ErrorDetailsTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None

class GetIdMappingJobInputRequestTypeDef(BaseValidatorModel):
    jobId: str
    workflowName: str

class IdMappingJobMetricsTypeDef(BaseValidatorModel):
    inputRecords: Optional[int] = None
    recordsNotProcessed: Optional[int] = None
    totalRecordsProcessed: Optional[int] = None

class IdMappingJobOutputSourceTypeDef(BaseValidatorModel):
    outputS3Path: str
    roleArn: str
    KMSArn: Optional[str] = None

class GetIdMappingWorkflowInputRequestTypeDef(BaseValidatorModel):
    workflowName: str

class GetIdNamespaceInputRequestTypeDef(BaseValidatorModel):
    idNamespaceName: str

class GetMatchIdInputRequestTypeDef(BaseValidatorModel):
    record: Mapping[str, str]
    workflowName: str
    applyNormalization: Optional[bool] = None

class GetMatchingJobInputRequestTypeDef(BaseValidatorModel):
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

class GetMatchingWorkflowInputRequestTypeDef(BaseValidatorModel):
    workflowName: str

class GetPolicyInputRequestTypeDef(BaseValidatorModel):
    arn: str

class GetProviderServiceInputRequestTypeDef(BaseValidatorModel):
    providerName: str
    providerServiceName: str

class ProviderIdNameSpaceConfigurationTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    providerSourceConfigurationDefinition: Optional[Dict[str, Any]] = None
    providerTargetConfigurationDefinition: Optional[Dict[str, Any]] = None

class ProviderIntermediateDataAccessConfigurationTypeDef(BaseValidatorModel):
    awsAccountIds: Optional[List[str]] = None
    requiredBucketActions: Optional[List[str]] = None

class GetSchemaMappingInputRequestTypeDef(BaseValidatorModel):
    schemaName: str

class IdMappingWorkflowSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    updatedAt: datetime
    workflowArn: str
    workflowName: str

class NamespaceProviderPropertiesTypeDef(BaseValidatorModel):
    providerServiceArn: str
    providerConfiguration: Optional[Mapping[str, Any]] = None

class IdNamespaceSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    idNamespaceArn: str
    idNamespaceName: str
    type: IdNamespaceTypeType
    updatedAt: datetime
    description: Optional[str] = None

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

class ListIdMappingJobsInputRequestTypeDef(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdMappingWorkflowsInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdNamespacesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMatchingJobsInputRequestTypeDef(BaseValidatorModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMatchingWorkflowsInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MatchingWorkflowSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    resolutionType: ResolutionTypeType
    updatedAt: datetime
    workflowArn: str
    workflowName: str

class ListProviderServicesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    providerName: Optional[str] = None

class ProviderServiceSummaryTypeDef(BaseValidatorModel):
    providerName: str
    providerServiceArn: str
    providerServiceDisplayName: str
    providerServiceName: str
    providerServiceType: ServiceTypeType

class ListSchemaMappingsInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SchemaMappingSummaryTypeDef(BaseValidatorModel):
    createdAt: datetime
    hasWorkflows: bool
    schemaArn: str
    schemaName: str
    updatedAt: datetime

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class OutputAttributeTypeDef(BaseValidatorModel):
    name: str
    hashed: Optional[bool] = None

class ProviderSchemaAttributeTypeDef(BaseValidatorModel):
    fieldName: str
    type: SchemaAttributeTypeType
    hashing: Optional[bool] = None
    subType: Optional[str] = None

class ProviderMarketplaceConfigurationTypeDef(BaseValidatorModel):
    assetId: str
    dataSetId: str
    listingId: str
    revisionId: str

class PutPolicyInputRequestTypeDef(BaseValidatorModel):
    arn: str
    policy: str
    token: Optional[str] = None

class RuleTypeDef(BaseValidatorModel):
    matchingKeys: Sequence[str]
    ruleName: str

class StartMatchingJobInputRequestTypeDef(BaseValidatorModel):
    workflowName: str

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
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

class CreateSchemaMappingInputRequestTypeDef(BaseValidatorModel):
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

class UpdateSchemaMappingInputRequestTypeDef(BaseValidatorModel):
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

class StartIdMappingJobInputRequestTypeDef(BaseValidatorModel):
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

class ListIdMappingWorkflowsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    workflowSummaries: List[IdMappingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IdNamespaceIdMappingWorkflowPropertiesTypeDef(BaseValidatorModel):
    idMappingType: Literal["PROVIDER"]
    providerProperties: Optional[NamespaceProviderPropertiesTypeDef] = None

class ListIdNamespacesOutputTypeDef(BaseValidatorModel):
    idNamespaceSummaries: List[IdNamespaceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProviderPropertiesTypeDef(BaseValidatorModel):
    providerServiceArn: str
    intermediateSourceConfiguration: Optional[IntermediateSourceConfigurationTypeDef] = None
    providerConfiguration: Optional[Mapping[str, Any]] = None

class ListIdMappingJobsOutputTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMatchingJobsOutputTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdMappingJobsInputListIdMappingJobsPaginateTypeDef(BaseValidatorModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdMappingWorkflowsInputListIdMappingWorkflowsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdNamespacesInputListIdNamespacesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMatchingJobsInputListMatchingJobsPaginateTypeDef(BaseValidatorModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProviderServicesInputListProviderServicesPaginateTypeDef(BaseValidatorModel):
    providerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMatchingWorkflowsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    workflowSummaries: List[MatchingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProviderServicesOutputTypeDef(BaseValidatorModel):
    nextToken: str
    providerServiceSummaries: List[ProviderServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemaMappingsOutputTypeDef(BaseValidatorModel):
    nextToken: str
    schemaList: List[SchemaMappingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OutputSourceTypeDef(BaseValidatorModel):
    output: Sequence[OutputAttributeTypeDef]
    outputS3Path: str
    KMSArn: Optional[str] = None
    applyNormalization: Optional[bool] = None

class ProviderComponentSchemaTypeDef(BaseValidatorModel):
    providerSchemaAttributes: Optional[List[ProviderSchemaAttributeTypeDef]] = None
    schemas: Optional[List[List[str]]] = None

class ProviderEndpointConfigurationTypeDef(BaseValidatorModel):
    marketplaceConfiguration: Optional[ProviderMarketplaceConfigurationTypeDef] = None

class RuleBasedPropertiesTypeDef(BaseValidatorModel):
    attributeMatchingModel: AttributeMatchingModelType
    rules: Sequence[RuleTypeDef]

class CreateIdNamespaceInputRequestTypeDef(BaseValidatorModel):
    idNamespaceName: str
    type: IdNamespaceTypeType
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[       Sequence[IdNamespaceIdMappingWorkflowPropertiesTypeDef]     ] = None
    inputSourceConfig: Optional[Sequence[IdNamespaceInputSourceTypeDef]] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateIdNamespaceOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingWorkflowProperties: List[IdNamespaceIdMappingWorkflowPropertiesTypeDef]
    idNamespaceArn: str
    idNamespaceName: str
    inputSourceConfig: List[IdNamespaceInputSourceTypeDef]
    roleArn: str
    tags: Dict[str, str]
    type: IdNamespaceTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdNamespaceOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingWorkflowProperties: List[IdNamespaceIdMappingWorkflowPropertiesTypeDef]
    idNamespaceArn: str
    idNamespaceName: str
    inputSourceConfig: List[IdNamespaceInputSourceTypeDef]
    roleArn: str
    tags: Dict[str, str]
    type: IdNamespaceTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdNamespaceInputRequestTypeDef(BaseValidatorModel):
    idNamespaceName: str
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[       Sequence[IdNamespaceIdMappingWorkflowPropertiesTypeDef]     ] = None
    inputSourceConfig: Optional[Sequence[IdNamespaceInputSourceTypeDef]] = None
    roleArn: Optional[str] = None

class UpdateIdNamespaceOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingWorkflowProperties: List[IdNamespaceIdMappingWorkflowPropertiesTypeDef]
    idNamespaceArn: str
    idNamespaceName: str
    inputSourceConfig: List[IdNamespaceInputSourceTypeDef]
    roleArn: str
    type: IdNamespaceTypeType
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class IdMappingTechniquesTypeDef(BaseValidatorModel):
    idMappingType: Literal["PROVIDER"]
    providerProperties: Optional[ProviderPropertiesTypeDef] = None

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

class ResolutionTechniquesTypeDef(BaseValidatorModel):
    resolutionType: ResolutionTypeType
    providerProperties: Optional[ProviderPropertiesTypeDef] = None
    ruleBasedProperties: Optional[RuleBasedPropertiesTypeDef] = None

class CreateIdMappingWorkflowInputRequestTypeDef(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[Sequence[IdMappingWorkflowOutputSourceTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class CreateIdMappingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdMappingWorkflowOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    tags: Dict[str, str]
    updatedAt: datetime
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdMappingWorkflowInputRequestTypeDef(BaseValidatorModel):
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[Sequence[IdMappingWorkflowOutputSourceTypeDef]] = None

class UpdateIdMappingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMatchingWorkflowInputRequestTypeDef(BaseValidatorModel):
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateMatchingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMatchingWorkflowOutputTypeDef(BaseValidatorModel):
    createdAt: datetime
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    tags: Dict[str, str]
    updatedAt: datetime
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMatchingWorkflowInputRequestTypeDef(BaseValidatorModel):
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfigTypeDef] = None

class UpdateMatchingWorkflowOutputTypeDef(BaseValidatorModel):
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

