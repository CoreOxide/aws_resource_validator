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
from aws_resource_validator.pydantic_models.bedrock_agent_runtime_constants import *

class AccessDeniedExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ParameterTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

class ActionGroupInvocationOutputTypeDef(BaseModel):
    text: Optional[str] = None

class ApiParameterTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

class ContentBodyTypeDef(BaseModel):
    body: Optional[str] = None

class BadGatewayExceptionTypeDef(BaseModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None

class CodeInterpreterInvocationInputTypeDef(BaseModel):
    code: Optional[str] = None
    files: Optional[List[str]] = None

class CodeInterpreterInvocationOutputTypeDef(BaseModel):
    executionError: Optional[str] = None
    executionOutput: Optional[str] = None
    executionTimeout: Optional[bool] = None
    files: Optional[List[str]] = None

class ConflictExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class DeleteAgentMemoryRequestRequestTypeDef(BaseModel):
    agentAliasId: str
    agentId: str
    memoryId: Optional[str] = None

class DependencyFailedExceptionTypeDef(BaseModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None

class S3ObjectDocTypeDef(BaseModel):
    uri: str

class GuardrailConfigurationTypeDef(BaseModel):
    guardrailId: str
    guardrailVersion: str

class PromptTemplateTypeDef(BaseModel):
    textPromptTemplate: Optional[str] = None

class FailureTraceTypeDef(BaseModel):
    failureReason: Optional[str] = None
    traceId: Optional[str] = None

class OutputFileTypeDef(BaseModel):
    bytes: Optional[bytes] = None
    name: Optional[str] = None
    type: Optional[str] = None

class S3ObjectFileTypeDef(BaseModel):
    uri: str

class FilterAttributeTypeDef(BaseModel):
    key: str
    value: Mapping[str, Any]

class FinalResponseTypeDef(BaseModel):
    text: Optional[str] = None

class FlowCompletionEventTypeDef(BaseModel):
    completionReason: Literal["SUCCESS"]

class FlowInputContentTypeDef(BaseModel):
    document: Optional[Mapping[str, Any]] = None

class FlowOutputContentTypeDef(BaseModel):
    document: Optional[Dict[str, Any]] = None

class InternalServerExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ResourceNotFoundExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ServiceQuotaExceededExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ThrottlingExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class ValidationExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class FunctionParameterTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetAgentMemoryRequestRequestTypeDef(BaseModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    maxItems: Optional[int] = None
    nextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GuardrailContentFilterTypeDef(BaseModel):
    action: Optional[Literal["BLOCKED"]] = None
    confidence: Optional[GuardrailContentFilterConfidenceType] = None
    type: Optional[GuardrailContentFilterTypeType] = None

class GuardrailCustomWordTypeDef(BaseModel):
    action: Optional[Literal["BLOCKED"]] = None
    match: Optional[str] = None

class GuardrailManagedWordTypeDef(BaseModel):
    action: Optional[Literal["BLOCKED"]] = None
    match: Optional[str] = None
    type: Optional[Literal["PROFANITY"]] = None

class GuardrailPiiEntityFilterTypeDef(BaseModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    type: Optional[GuardrailPiiEntityTypeType] = None

class GuardrailRegexFilterTypeDef(BaseModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    name: Optional[str] = None
    regex: Optional[str] = None

class GuardrailTopicTypeDef(BaseModel):
    action: Optional[Literal["BLOCKED"]] = None
    name: Optional[str] = None
    type: Optional[Literal["DENY"]] = None

class TextInferenceConfigTypeDef(BaseModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None

class InferenceConfigurationTypeDef(BaseModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class KnowledgeBaseLookupInputTypeDef(BaseModel):
    knowledgeBaseId: Optional[str] = None
    text: Optional[str] = None

class KnowledgeBaseQueryTypeDef(BaseModel):
    text: str

class KnowledgeBaseVectorSearchConfigurationTypeDef(BaseModel):
    filter: Optional["RetrievalFilterTypeDef"] = None
    numberOfResults: Optional[int] = None
    overrideSearchType: Optional[SearchTypeType] = None

class RetrievalResultContentTypeDef(BaseModel):
    text: str

class MemorySessionSummaryTypeDef(BaseModel):
    memoryId: Optional[str] = None
    sessionExpiryTime: Optional[datetime] = None
    sessionId: Optional[str] = None
    sessionStartTime: Optional[datetime] = None
    summaryText: Optional[str] = None

class RepromptResponseTypeDef(BaseModel):
    source: Optional[SourceType] = None
    text: Optional[str] = None

class QueryTransformationConfigurationTypeDef(BaseModel):
    type: Literal["QUERY_DECOMPOSITION"]

class RationaleTypeDef(BaseModel):
    text: Optional[str] = None
    traceId: Optional[str] = None

class PostProcessingParsedResponseTypeDef(BaseModel):
    text: Optional[str] = None

class PreProcessingParsedResponseTypeDef(BaseModel):
    isValid: Optional[bool] = None
    rationale: Optional[str] = None

class RetrievalResultConfluenceLocationTypeDef(BaseModel):
    url: Optional[str] = None

class RetrievalResultS3LocationTypeDef(BaseModel):
    uri: Optional[str] = None

class RetrievalResultSalesforceLocationTypeDef(BaseModel):
    url: Optional[str] = None

class RetrievalResultSharePointLocationTypeDef(BaseModel):
    url: Optional[str] = None

class RetrievalResultWebLocationTypeDef(BaseModel):
    url: Optional[str] = None

class RetrieveAndGenerateInputTypeDef(BaseModel):
    text: str

class RetrieveAndGenerateOutputTypeDef(BaseModel):
    text: str

class RetrieveAndGenerateSessionConfigurationTypeDef(BaseModel):
    kmsKeyArn: str

class SpanTypeDef(BaseModel):
    end: Optional[int] = None
    start: Optional[int] = None

class PropertyParametersTypeDef(BaseModel):
    properties: Optional[List[ParameterTypeDef]] = None

class RequestBodyTypeDef(BaseModel):
    content: Optional[Dict[str, List[ParameterTypeDef]]] = None

class ApiResultTypeDef(BaseModel):
    actionGroup: str
    apiPath: Optional[str] = None
    httpMethod: Optional[str] = None
    httpStatusCode: Optional[int] = None
    responseBody: Optional[Mapping[str, ContentBodyTypeDef]] = None
    responseState: Optional[ResponseStateType] = None

class FunctionResultTypeDef(BaseModel):
    actionGroup: str
    function: Optional[str] = None
    responseBody: Optional[Mapping[str, ContentBodyTypeDef]] = None
    responseState: Optional[ResponseStateType] = None

class ByteContentDocTypeDef(BaseModel):
    contentType: str
    data: BlobTypeDef
    identifier: str

class ByteContentFileTypeDef(BaseModel):
    data: BlobTypeDef
    mediaType: str

class FilePartTypeDef(BaseModel):
    files: Optional[List[OutputFileTypeDef]] = None

class RetrievalFilterTypeDef(BaseModel):
    andAll: Optional[Sequence[Dict[str, Any]]] = None
    equals: Optional[FilterAttributeTypeDef] = None
    greaterThan: Optional[FilterAttributeTypeDef] = None
    greaterThanOrEquals: Optional[FilterAttributeTypeDef] = None
    _in: Optional[FilterAttributeTypeDef] = None
    lessThan: Optional[FilterAttributeTypeDef] = None
    lessThanOrEquals: Optional[FilterAttributeTypeDef] = None
    listContains: Optional[FilterAttributeTypeDef] = None
    notEquals: Optional[FilterAttributeTypeDef] = None
    notIn: Optional[FilterAttributeTypeDef] = None
    orAll: Optional[Sequence[Dict[str, Any]]] = None
    startsWith: Optional[FilterAttributeTypeDef] = None
    stringContains: Optional[FilterAttributeTypeDef] = None

class FlowInputTypeDef(BaseModel):
    content: FlowInputContentTypeDef
    nodeName: str
    nodeOutputName: str

class FlowOutputEventTypeDef(BaseModel):
    content: FlowOutputContentTypeDef
    nodeName: str
    nodeType: NodeTypeType

class FunctionInvocationInputTypeDef(BaseModel):
    actionGroup: str
    function: Optional[str] = None
    parameters: Optional[List[FunctionParameterTypeDef]] = None

class GetAgentMemoryRequestGetAgentMemoryPaginateTypeDef(BaseModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GuardrailContentPolicyAssessmentTypeDef(BaseModel):
    filters: Optional[List[GuardrailContentFilterTypeDef]] = None

class GuardrailWordPolicyAssessmentTypeDef(BaseModel):
    customWords: Optional[List[GuardrailCustomWordTypeDef]] = None
    managedWordLists: Optional[List[GuardrailManagedWordTypeDef]] = None

class GuardrailSensitiveInformationPolicyAssessmentTypeDef(BaseModel):
    piiEntities: Optional[List[GuardrailPiiEntityFilterTypeDef]] = None
    regexes: Optional[List[GuardrailRegexFilterTypeDef]] = None

class GuardrailTopicPolicyAssessmentTypeDef(BaseModel):
    topics: Optional[List[GuardrailTopicTypeDef]] = None

class InferenceConfigTypeDef(BaseModel):
    textInferenceConfig: Optional[TextInferenceConfigTypeDef] = None

class ModelInvocationInputTypeDef(BaseModel):
    inferenceConfiguration: Optional[InferenceConfigurationTypeDef] = None
    overrideLambda: Optional[str] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    text: Optional[str] = None
    traceId: Optional[str] = None
    type: Optional[PromptTypeType] = None

class KnowledgeBaseRetrievalConfigurationTypeDef(BaseModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationTypeDef

class MemoryTypeDef(BaseModel):
    sessionSummary: Optional[MemorySessionSummaryTypeDef] = None

class OrchestrationConfigurationTypeDef(BaseModel):
    queryTransformationConfiguration: QueryTransformationConfigurationTypeDef

class PostProcessingModelInvocationOutputTypeDef(BaseModel):
    parsedResponse: Optional[PostProcessingParsedResponseTypeDef] = None
    traceId: Optional[str] = None

class PreProcessingModelInvocationOutputTypeDef(BaseModel):
    parsedResponse: Optional[PreProcessingParsedResponseTypeDef] = None
    traceId: Optional[str] = None

class RetrievalResultLocationTypeDef(BaseModel):
    type: RetrievalResultLocationTypeType
    confluenceLocation: Optional[RetrievalResultConfluenceLocationTypeDef] = None
    s3Location: Optional[RetrievalResultS3LocationTypeDef] = None
    salesforceLocation: Optional[RetrievalResultSalesforceLocationTypeDef] = None
    sharePointLocation: Optional[RetrievalResultSharePointLocationTypeDef] = None
    webLocation: Optional[RetrievalResultWebLocationTypeDef] = None

class TextResponsePartTypeDef(BaseModel):
    span: Optional[SpanTypeDef] = None
    text: Optional[str] = None

class ApiRequestBodyTypeDef(BaseModel):
    content: Optional[Dict[str, PropertyParametersTypeDef]] = None

class ActionGroupInvocationInputTypeDef(BaseModel):
    actionGroupName: Optional[str] = None
    apiPath: Optional[str] = None
    executionType: Optional[ExecutionTypeType] = None
    function: Optional[str] = None
    invocationId: Optional[str] = None
    parameters: Optional[List[ParameterTypeDef]] = None
    requestBody: Optional[RequestBodyTypeDef] = None
    verb: Optional[str] = None

class InvocationResultMemberTypeDef(BaseModel):
    apiResult: Optional[ApiResultTypeDef] = None
    functionResult: Optional[FunctionResultTypeDef] = None

class ExternalSourceTypeDef(BaseModel):
    sourceType: ExternalSourceTypeType
    byteContent: Optional[ByteContentDocTypeDef] = None
    s3Location: Optional[S3ObjectDocTypeDef] = None

class FileSourceTypeDef(BaseModel):
    sourceType: FileSourceTypeType
    byteContent: Optional[ByteContentFileTypeDef] = None
    s3Location: Optional[S3ObjectFileTypeDef] = None

class InvokeFlowRequestRequestTypeDef(BaseModel):
    flowAliasIdentifier: str
    flowIdentifier: str
    inputs: Sequence[FlowInputTypeDef]

class FlowResponseStreamTypeDef(BaseModel):
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    badGatewayException: Optional[BadGatewayExceptionTypeDef] = None
    conflictException: Optional[ConflictExceptionTypeDef] = None
    dependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    flowCompletionEvent: Optional[FlowCompletionEventTypeDef] = None
    flowOutputEvent: Optional[FlowOutputEventTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    resourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None

class GuardrailAssessmentTypeDef(BaseModel):
    contentPolicy: Optional[GuardrailContentPolicyAssessmentTypeDef] = None
    sensitiveInformationPolicy: Optional[       GuardrailSensitiveInformationPolicyAssessmentTypeDef     ] = None
    topicPolicy: Optional[GuardrailTopicPolicyAssessmentTypeDef] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessmentTypeDef] = None

class ExternalSourcesGenerationConfigurationTypeDef(BaseModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    inferenceConfig: Optional[InferenceConfigTypeDef] = None
    promptTemplate: Optional[PromptTemplateTypeDef] = None

class GenerationConfigurationTypeDef(BaseModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    inferenceConfig: Optional[InferenceConfigTypeDef] = None
    promptTemplate: Optional[PromptTemplateTypeDef] = None

class KnowledgeBaseConfigurationTypeDef(BaseModel):
    knowledgeBaseId: str
    retrievalConfiguration: KnowledgeBaseRetrievalConfigurationTypeDef

class RetrieveRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQueryTypeDef
    nextToken: Optional[str] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None

class RetrieveRequestRetrievePaginateTypeDef(BaseModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQueryTypeDef
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAgentMemoryResponseTypeDef(BaseModel):
    memoryContents: List[MemoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PostProcessingTraceTypeDef(BaseModel):
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[PostProcessingModelInvocationOutputTypeDef] = None

class PreProcessingTraceTypeDef(BaseModel):
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[PreProcessingModelInvocationOutputTypeDef] = None

class KnowledgeBaseRetrievalResultTypeDef(BaseModel):
    content: RetrievalResultContentTypeDef
    location: Optional[RetrievalResultLocationTypeDef] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    score: Optional[float] = None

class RetrievedReferenceTypeDef(BaseModel):
    content: Optional[RetrievalResultContentTypeDef] = None
    location: Optional[RetrievalResultLocationTypeDef] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None

class GeneratedResponsePartTypeDef(BaseModel):
    textResponsePart: Optional[TextResponsePartTypeDef] = None

class ApiInvocationInputTypeDef(BaseModel):
    actionGroup: str
    apiPath: Optional[str] = None
    httpMethod: Optional[str] = None
    parameters: Optional[List[ApiParameterTypeDef]] = None
    requestBody: Optional[ApiRequestBodyTypeDef] = None

class InvocationInputTypeDef(BaseModel):
    actionGroupInvocationInput: Optional[ActionGroupInvocationInputTypeDef] = None
    codeInterpreterInvocationInput: Optional[CodeInterpreterInvocationInputTypeDef] = None
    invocationType: Optional[InvocationTypeType] = None
    knowledgeBaseLookupInput: Optional[KnowledgeBaseLookupInputTypeDef] = None
    traceId: Optional[str] = None

class InputFileTypeDef(BaseModel):
    name: str
    source: FileSourceTypeDef
    useCase: FileUseCaseType

class InvokeFlowResponseTypeDef(BaseModel):
    responseStream: "EventStream[FlowResponseStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

class GuardrailTraceTypeDef(BaseModel):
    action: Optional[GuardrailActionType] = None
    inputAssessments: Optional[List[GuardrailAssessmentTypeDef]] = None
    outputAssessments: Optional[List[GuardrailAssessmentTypeDef]] = None
    traceId: Optional[str] = None

class ExternalSourcesRetrieveAndGenerateConfigurationTypeDef(BaseModel):
    modelArn: str
    sources: Sequence[ExternalSourceTypeDef]
    generationConfiguration: Optional[ExternalSourcesGenerationConfigurationTypeDef] = None

class KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef(BaseModel):
    knowledgeBaseId: str
    modelArn: str
    generationConfiguration: Optional[GenerationConfigurationTypeDef] = None
    orchestrationConfiguration: Optional[OrchestrationConfigurationTypeDef] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None

class RetrieveResponseTypeDef(BaseModel):
    nextToken: str
    retrievalResults: List[KnowledgeBaseRetrievalResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class KnowledgeBaseLookupOutputTypeDef(BaseModel):
    retrievedReferences: Optional[List[RetrievedReferenceTypeDef]] = None

class CitationTypeDef(BaseModel):
    generatedResponsePart: Optional[GeneratedResponsePartTypeDef] = None
    retrievedReferences: Optional[List[RetrievedReferenceTypeDef]] = None

class InvocationInputMemberTypeDef(BaseModel):
    apiInvocationInput: Optional[ApiInvocationInputTypeDef] = None
    functionInvocationInput: Optional[FunctionInvocationInputTypeDef] = None

class SessionStateTypeDef(BaseModel):
    files: Optional[Sequence[InputFileTypeDef]] = None
    invocationId: Optional[str] = None
    knowledgeBaseConfigurations: Optional[Sequence[KnowledgeBaseConfigurationTypeDef]] = None
    promptSessionAttributes: Optional[Mapping[str, str]] = None
    returnControlInvocationResults: Optional[Sequence[InvocationResultMemberTypeDef]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None

class RetrieveAndGenerateConfigurationTypeDef(BaseModel):
    type: RetrieveAndGenerateTypeType
    externalSourcesConfiguration: Optional[       ExternalSourcesRetrieveAndGenerateConfigurationTypeDef     ] = None
    knowledgeBaseConfiguration: Optional[       KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef     ] = None

class ObservationTypeDef(BaseModel):
    actionGroupInvocationOutput: Optional[ActionGroupInvocationOutputTypeDef] = None
    codeInterpreterInvocationOutput: Optional[CodeInterpreterInvocationOutputTypeDef] = None
    finalResponse: Optional[FinalResponseTypeDef] = None
    knowledgeBaseLookupOutput: Optional[KnowledgeBaseLookupOutputTypeDef] = None
    repromptResponse: Optional[RepromptResponseTypeDef] = None
    traceId: Optional[str] = None
    type: Optional[TypeType] = None

class AttributionTypeDef(BaseModel):
    citations: Optional[List[CitationTypeDef]] = None

class RetrieveAndGenerateResponseTypeDef(BaseModel):
    citations: List[CitationTypeDef]
    guardrailAction: GuadrailActionType
    output: RetrieveAndGenerateOutputTypeDef
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReturnControlPayloadTypeDef(BaseModel):
    invocationId: Optional[str] = None
    invocationInputs: Optional[List[InvocationInputMemberTypeDef]] = None

class InvokeAgentRequestRequestTypeDef(BaseModel):
    agentAliasId: str
    agentId: str
    sessionId: str
    enableTrace: Optional[bool] = None
    endSession: Optional[bool] = None
    inputText: Optional[str] = None
    memoryId: Optional[str] = None
    sessionState: Optional[SessionStateTypeDef] = None

class RetrieveAndGenerateRequestRequestTypeDef(BaseModel):
    input: RetrieveAndGenerateInputTypeDef
    retrieveAndGenerateConfiguration: Optional[RetrieveAndGenerateConfigurationTypeDef] = None
    sessionConfiguration: Optional[RetrieveAndGenerateSessionConfigurationTypeDef] = None
    sessionId: Optional[str] = None

class OrchestrationTraceTypeDef(BaseModel):
    invocationInput: Optional[InvocationInputTypeDef] = None
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    observation: Optional[ObservationTypeDef] = None
    rationale: Optional[RationaleTypeDef] = None

class PayloadPartTypeDef(BaseModel):
    attribution: Optional[AttributionTypeDef] = None
    bytes: Optional[bytes] = None

class TraceTypeDef(BaseModel):
    failureTrace: Optional[FailureTraceTypeDef] = None
    guardrailTrace: Optional[GuardrailTraceTypeDef] = None
    orchestrationTrace: Optional[OrchestrationTraceTypeDef] = None
    postProcessingTrace: Optional[PostProcessingTraceTypeDef] = None
    preProcessingTrace: Optional[PreProcessingTraceTypeDef] = None

class TracePartTypeDef(BaseModel):
    agentAliasId: Optional[str] = None
    agentId: Optional[str] = None
    agentVersion: Optional[str] = None
    sessionId: Optional[str] = None
    trace: Optional[TraceTypeDef] = None

class ResponseStreamTypeDef(BaseModel):
    accessDeniedException: Optional[AccessDeniedExceptionTypeDef] = None
    badGatewayException: Optional[BadGatewayExceptionTypeDef] = None
    chunk: Optional[PayloadPartTypeDef] = None
    conflictException: Optional[ConflictExceptionTypeDef] = None
    dependencyFailedException: Optional[DependencyFailedExceptionTypeDef] = None
    files: Optional[FilePartTypeDef] = None
    internalServerException: Optional[InternalServerExceptionTypeDef] = None
    resourceNotFoundException: Optional[ResourceNotFoundExceptionTypeDef] = None
    returnControl: Optional[ReturnControlPayloadTypeDef] = None
    serviceQuotaExceededException: Optional[ServiceQuotaExceededExceptionTypeDef] = None
    throttlingException: Optional[ThrottlingExceptionTypeDef] = None
    trace: Optional[TracePartTypeDef] = None
    validationException: Optional[ValidationExceptionTypeDef] = None

class InvokeAgentResponseTypeDef(BaseModel):
    completion: "EventStream[ResponseStreamTypeDef]"
    contentType: str
    memoryId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

