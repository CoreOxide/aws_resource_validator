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
from aws_resource_validator.pydantic_models.entityresolution_constants import *

class AddPolicyStatementInputRequestTypeDef(BaseModel):
    action: Sequence[str]
    arn: str
    effect: StatementEffectType
    principal: Sequence[str]
    statementId: str
    condition: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchDeleteUniqueIdInputRequestTypeDef(BaseModel):
    uniqueIds: Sequence[str]
    workflowName: str
    inputSource: Optional[str] = None

class DeleteUniqueIdErrorTypeDef(BaseModel):
    errorType: DeleteUniqueIdErrorTypeType
    uniqueId: str

class DeletedUniqueIdTypeDef(BaseModel):
    uniqueId: str

class IdMappingWorkflowInputSourceTypeDef(BaseModel):
    inputSourceARN: str
    schemaName: Optional[str] = None
    type: Optional[IdNamespaceTypeType] = None

class IdMappingWorkflowOutputSourceTypeDef(BaseModel):
    outputS3Path: str
    KMSArn: Optional[str] = None

class IdNamespaceInputSourceTypeDef(BaseModel):
    inputSourceARN: str
    schemaName: Optional[str] = None

class IncrementalRunConfigTypeDef(BaseModel):
    incrementalRunType: Optional[Literal["IMMEDIATE"]] = None

class InputSourceTypeDef(BaseModel):
    inputSourceARN: str
    schemaName: str
    applyNormalization: Optional[bool] = None

class SchemaInputAttributeTypeDef(BaseModel):
    fieldName: str
    type: SchemaAttributeTypeType
    groupName: Optional[str] = None
    matchKey: Optional[str] = None
    subType: Optional[str] = None

class DeleteIdMappingWorkflowInputRequestTypeDef(BaseModel):
    workflowName: str

class DeleteIdNamespaceInputRequestTypeDef(BaseModel):
    idNamespaceName: str

class DeleteMatchingWorkflowInputRequestTypeDef(BaseModel):
    workflowName: str

class DeletePolicyStatementInputRequestTypeDef(BaseModel):
    arn: str
    statementId: str

class DeleteSchemaMappingInputRequestTypeDef(BaseModel):
    schemaName: str

class ErrorDetailsTypeDef(BaseModel):
    errorMessage: Optional[str] = None

class GetIdMappingJobInputRequestTypeDef(BaseModel):
    jobId: str
    workflowName: str

class IdMappingJobMetricsTypeDef(BaseModel):
    inputRecords: Optional[int] = None
    recordsNotProcessed: Optional[int] = None
    totalRecordsProcessed: Optional[int] = None

class IdMappingJobOutputSourceTypeDef(BaseModel):
    outputS3Path: str
    roleArn: str
    KMSArn: Optional[str] = None

class GetIdMappingWorkflowInputRequestTypeDef(BaseModel):
    workflowName: str

class GetIdNamespaceInputRequestTypeDef(BaseModel):
    idNamespaceName: str

class GetMatchIdInputRequestTypeDef(BaseModel):
    record: Mapping[str, str]
    workflowName: str
    applyNormalization: Optional[bool] = None

class GetMatchingJobInputRequestTypeDef(BaseModel):
    jobId: str
    workflowName: str

class JobMetricsTypeDef(BaseModel):
    inputRecords: Optional[int] = None
    matchIDs: Optional[int] = None
    recordsNotProcessed: Optional[int] = None
    totalRecordsProcessed: Optional[int] = None

class JobOutputSourceTypeDef(BaseModel):
    outputS3Path: str
    roleArn: str
    KMSArn: Optional[str] = None

class GetMatchingWorkflowInputRequestTypeDef(BaseModel):
    workflowName: str

class GetPolicyInputRequestTypeDef(BaseModel):
    arn: str

class GetProviderServiceInputRequestTypeDef(BaseModel):
    providerName: str
    providerServiceName: str

class ProviderIdNameSpaceConfigurationTypeDef(BaseModel):
    description: Optional[str] = None
    providerSourceConfigurationDefinition: Optional[Dict[str, Any]] = None
    providerTargetConfigurationDefinition: Optional[Dict[str, Any]] = None

class ProviderIntermediateDataAccessConfigurationTypeDef(BaseModel):
    awsAccountIds: Optional[List[str]] = None
    requiredBucketActions: Optional[List[str]] = None

class GetSchemaMappingInputRequestTypeDef(BaseModel):
    schemaName: str

class IdMappingWorkflowSummaryTypeDef(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    workflowArn: str
    workflowName: str

class NamespaceProviderPropertiesTypeDef(BaseModel):
    providerServiceArn: str
    providerConfiguration: Optional[Mapping[str, Any]] = None

class IdNamespaceSummaryTypeDef(BaseModel):
    createdAt: datetime
    idNamespaceArn: str
    idNamespaceName: str
    type: IdNamespaceTypeType
    updatedAt: datetime
    description: Optional[str] = None

class IntermediateSourceConfigurationTypeDef(BaseModel):
    intermediateS3Path: str

class JobSummaryTypeDef(BaseModel):
    jobId: str
    startTime: datetime
    status: JobStatusType
    endTime: Optional[datetime] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListIdMappingJobsInputRequestTypeDef(BaseModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdMappingWorkflowsInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListIdNamespacesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMatchingJobsInputRequestTypeDef(BaseModel):
    workflowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMatchingWorkflowsInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MatchingWorkflowSummaryTypeDef(BaseModel):
    createdAt: datetime
    resolutionType: ResolutionTypeType
    updatedAt: datetime
    workflowArn: str
    workflowName: str

class ListProviderServicesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    providerName: Optional[str] = None

class ProviderServiceSummaryTypeDef(BaseModel):
    providerName: str
    providerServiceArn: str
    providerServiceDisplayName: str
    providerServiceName: str
    providerServiceType: ServiceTypeType

class ListSchemaMappingsInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SchemaMappingSummaryTypeDef(BaseModel):
    createdAt: datetime
    hasWorkflows: bool
    schemaArn: str
    schemaName: str
    updatedAt: datetime

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class OutputAttributeTypeDef(BaseModel):
    name: str
    hashed: Optional[bool] = None

class ProviderSchemaAttributeTypeDef(BaseModel):
    fieldName: str
    type: SchemaAttributeTypeType
    hashing: Optional[bool] = None
    subType: Optional[str] = None

class ProviderMarketplaceConfigurationTypeDef(BaseModel):
    assetId: str
    dataSetId: str
    listingId: str
    revisionId: str

class PutPolicyInputRequestTypeDef(BaseModel):
    arn: str
    policy: str
    token: Optional[str] = None

class RuleTypeDef(BaseModel):
    matchingKeys: Sequence[str]
    ruleName: str

class StartMatchingJobInputRequestTypeDef(BaseModel):
    workflowName: str

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AddPolicyStatementOutputTypeDef(BaseModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIdMappingWorkflowOutputTypeDef(BaseModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIdNamespaceOutputTypeDef(BaseModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMatchingWorkflowOutputTypeDef(BaseModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePolicyStatementOutputTypeDef(BaseModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSchemaMappingOutputTypeDef(BaseModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMatchIdOutputTypeDef(BaseModel):
    matchId: str
    matchRule: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyOutputTypeDef(BaseModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPolicyOutputTypeDef(BaseModel):
    arn: str
    policy: str
    token: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchingJobOutputTypeDef(BaseModel):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteUniqueIdOutputTypeDef(BaseModel):
    deleted: List[DeletedUniqueIdTypeDef]
    disconnectedUniqueIds: List[str]
    errors: List[DeleteUniqueIdErrorTypeDef]
    status: DeleteUniqueIdStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaMappingInputRequestTypeDef(BaseModel):
    mappedInputFields: Sequence[SchemaInputAttributeTypeDef]
    schemaName: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateSchemaMappingOutputTypeDef(BaseModel):
    description: str
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaMappingOutputTypeDef(BaseModel):
    createdAt: datetime
    description: str
    hasWorkflows: bool
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    schemaArn: str
    schemaName: str
    tags: Dict[str, str]
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSchemaMappingInputRequestTypeDef(BaseModel):
    mappedInputFields: Sequence[SchemaInputAttributeTypeDef]
    schemaName: str
    description: Optional[str] = None

class UpdateSchemaMappingOutputTypeDef(BaseModel):
    description: str
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    schemaArn: str
    schemaName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdMappingJobOutputTypeDef(BaseModel):
    endTime: datetime
    errorDetails: ErrorDetailsTypeDef
    jobId: str
    metrics: IdMappingJobMetricsTypeDef
    outputSourceConfig: List[IdMappingJobOutputSourceTypeDef]
    startTime: datetime
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartIdMappingJobInputRequestTypeDef(BaseModel):
    workflowName: str
    outputSourceConfig: Optional[Sequence[IdMappingJobOutputSourceTypeDef]] = None

class StartIdMappingJobOutputTypeDef(BaseModel):
    jobId: str
    outputSourceConfig: List[IdMappingJobOutputSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMatchingJobOutputTypeDef(BaseModel):
    endTime: datetime
    errorDetails: ErrorDetailsTypeDef
    jobId: str
    metrics: JobMetricsTypeDef
    outputSourceConfig: List[JobOutputSourceTypeDef]
    startTime: datetime
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdMappingWorkflowsOutputTypeDef(BaseModel):
    nextToken: str
    workflowSummaries: List[IdMappingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IdNamespaceIdMappingWorkflowPropertiesTypeDef(BaseModel):
    idMappingType: Literal["PROVIDER"]
    providerProperties: Optional[NamespaceProviderPropertiesTypeDef] = None

class ListIdNamespacesOutputTypeDef(BaseModel):
    idNamespaceSummaries: List[IdNamespaceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProviderPropertiesTypeDef(BaseModel):
    providerServiceArn: str
    intermediateSourceConfiguration: Optional[IntermediateSourceConfigurationTypeDef] = None
    providerConfiguration: Optional[Mapping[str, Any]] = None

class ListIdMappingJobsOutputTypeDef(BaseModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMatchingJobsOutputTypeDef(BaseModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIdMappingJobsInputListIdMappingJobsPaginateTypeDef(BaseModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdMappingWorkflowsInputListIdMappingWorkflowsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIdNamespacesInputListIdNamespacesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMatchingJobsInputListMatchingJobsPaginateTypeDef(BaseModel):
    workflowName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMatchingWorkflowsInputListMatchingWorkflowsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProviderServicesInputListProviderServicesPaginateTypeDef(BaseModel):
    providerName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaMappingsInputListSchemaMappingsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMatchingWorkflowsOutputTypeDef(BaseModel):
    nextToken: str
    workflowSummaries: List[MatchingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProviderServicesOutputTypeDef(BaseModel):
    nextToken: str
    providerServiceSummaries: List[ProviderServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemaMappingsOutputTypeDef(BaseModel):
    nextToken: str
    schemaList: List[SchemaMappingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OutputSourceTypeDef(BaseModel):
    output: Sequence[OutputAttributeTypeDef]
    outputS3Path: str
    KMSArn: Optional[str] = None
    applyNormalization: Optional[bool] = None

class ProviderComponentSchemaTypeDef(BaseModel):
    providerSchemaAttributes: Optional[List[ProviderSchemaAttributeTypeDef]] = None
    schemas: Optional[List[List[str]]] = None

class ProviderEndpointConfigurationTypeDef(BaseModel):
    marketplaceConfiguration: Optional[ProviderMarketplaceConfigurationTypeDef] = None

class RuleBasedPropertiesTypeDef(BaseModel):
    attributeMatchingModel: AttributeMatchingModelType
    rules: Sequence[RuleTypeDef]

class CreateIdNamespaceInputRequestTypeDef(BaseModel):
    idNamespaceName: str
    type: IdNamespaceTypeType
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[       Sequence[IdNamespaceIdMappingWorkflowPropertiesTypeDef]     ] = None
    inputSourceConfig: Optional[Sequence[IdNamespaceInputSourceTypeDef]] = None
    roleArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateIdNamespaceOutputTypeDef(BaseModel):
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

class GetIdNamespaceOutputTypeDef(BaseModel):
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

class UpdateIdNamespaceInputRequestTypeDef(BaseModel):
    idNamespaceName: str
    description: Optional[str] = None
    idMappingWorkflowProperties: Optional[       Sequence[IdNamespaceIdMappingWorkflowPropertiesTypeDef]     ] = None
    inputSourceConfig: Optional[Sequence[IdNamespaceInputSourceTypeDef]] = None
    roleArn: Optional[str] = None

class UpdateIdNamespaceOutputTypeDef(BaseModel):
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

class IdMappingTechniquesTypeDef(BaseModel):
    idMappingType: Literal["PROVIDER"]
    providerProperties: Optional[ProviderPropertiesTypeDef] = None

class GetProviderServiceOutputTypeDef(BaseModel):
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

class ResolutionTechniquesTypeDef(BaseModel):
    resolutionType: ResolutionTypeType
    providerProperties: Optional[ProviderPropertiesTypeDef] = None
    ruleBasedProperties: Optional[RuleBasedPropertiesTypeDef] = None

class CreateIdMappingWorkflowInputRequestTypeDef(BaseModel):
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[Sequence[IdMappingWorkflowOutputSourceTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None

class CreateIdMappingWorkflowOutputTypeDef(BaseModel):
    description: str
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdMappingWorkflowOutputTypeDef(BaseModel):
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

class UpdateIdMappingWorkflowInputRequestTypeDef(BaseModel):
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    outputSourceConfig: Optional[Sequence[IdMappingWorkflowOutputSourceTypeDef]] = None

class UpdateIdMappingWorkflowOutputTypeDef(BaseModel):
    description: str
    idMappingTechniques: IdMappingTechniquesTypeDef
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMatchingWorkflowInputRequestTypeDef(BaseModel):
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateMatchingWorkflowOutputTypeDef(BaseModel):
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMatchingWorkflowOutputTypeDef(BaseModel):
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

class UpdateMatchingWorkflowInputRequestTypeDef(BaseModel):
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowName: str
    description: Optional[str] = None
    incrementalRunConfig: Optional[IncrementalRunConfigTypeDef] = None

class UpdateMatchingWorkflowOutputTypeDef(BaseModel):
    description: str
    incrementalRunConfig: IncrementalRunConfigTypeDef
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceTypeDef]
    resolutionTechniques: ResolutionTechniquesTypeDef
    roleArn: str
    workflowName: str
    ResponseMetadata: ResponseMetadataTypeDef

