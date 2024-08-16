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
from aws_resource_validator.pydantic_models.bedrock_agent_runtime_constants import *

class AccessDeniedExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ParameterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

class ActionGroupInvocationOutputTypeDef(BaseValidatorModel):
    text: Optional[str] = None

class ApiParameterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

class ContentBodyTypeDef(BaseValidatorModel):
    body: Optional[str] = None

class BadGatewayExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None

class CodeInterpreterInvocationInputTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    files: Optional[List[str]] = None

class CodeInterpreterInvocationOutputTypeDef(BaseValidatorModel):
    executionError: Optional[str] = None
    executionOutput: Optional[str] = None
    executionTimeout: Optional[bool] = None
    files: Optional[List[str]] = None

class ConflictExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class DeleteAgentMemoryRequestRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: Optional[str] = None

class DependencyFailedExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    resourceName: Optional[str] = None

class S3ObjectDocTypeDef(BaseValidatorModel):
    uri: str

class GuardrailConfigurationTypeDef(BaseValidatorModel):
    guardrailId: str
    guardrailVersion: str

class PromptTemplateTypeDef(BaseValidatorModel):
    textPromptTemplate: Optional[str] = None

class FailureTraceTypeDef(BaseValidatorModel):
    failureReason: Optional[str] = None
    traceId: Optional[str] = None

class OutputFileTypeDef(BaseValidatorModel):
    bytes: Optional[bytes] = None
    name: Optional[str] = None
    type: Optional[str] = None

class S3ObjectFileTypeDef(BaseValidatorModel):
    uri: str

class FilterAttributeTypeDef(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]

class FinalResponseTypeDef(BaseValidatorModel):
    text: Optional[str] = None

class FlowCompletionEventTypeDef(BaseValidatorModel):
    completionReason: Literal["SUCCESS"]

class FlowInputContentTypeDef(BaseValidatorModel):
    document: Optional[Mapping[str, Any]] = None

class FlowOutputContentTypeDef(BaseValidatorModel):
    document: Optional[Dict[str, Any]] = None

class InternalServerExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ResourceNotFoundExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ServiceQuotaExceededExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ThrottlingExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class ValidationExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class FunctionParameterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetAgentMemoryRequestRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    maxItems: Optional[int] = None
    nextToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GuardrailContentFilterTypeDef(BaseValidatorModel):
    action: Optional[Literal["BLOCKED"]] = None
    confidence: Optional[GuardrailContentFilterConfidenceType] = None
    type: Optional[GuardrailContentFilterTypeType] = None

class GuardrailCustomWordTypeDef(BaseValidatorModel):
    action: Optional[Literal["BLOCKED"]] = None
    match: Optional[str] = None

class GuardrailManagedWordTypeDef(BaseValidatorModel):
    action: Optional[Literal["BLOCKED"]] = None
    match: Optional[str] = None
    type: Optional[Literal["PROFANITY"]] = None

class GuardrailPiiEntityFilterTypeDef(BaseValidatorModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    type: Optional[GuardrailPiiEntityTypeType] = None

class GuardrailRegexFilterTypeDef(BaseValidatorModel):
    action: Optional[GuardrailSensitiveInformationPolicyActionType] = None
    match: Optional[str] = None
    name: Optional[str] = None
    regex: Optional[str] = None

class GuardrailTopicTypeDef(BaseValidatorModel):
    action: Optional[Literal["BLOCKED"]] = None
    name: Optional[str] = None
    type: Optional[Literal["DENY"]] = None

class TextInferenceConfigTypeDef(BaseValidatorModel):
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None
    temperature: Optional[float] = None
    topP: Optional[float] = None

class InferenceConfigurationTypeDef(BaseValidatorModel):
    maximumLength: Optional[int] = None
    stopSequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    topK: Optional[int] = None
    topP: Optional[float] = None

class KnowledgeBaseLookupInputTypeDef(BaseValidatorModel):
    knowledgeBaseId: Optional[str] = None
    text: Optional[str] = None

class KnowledgeBaseQueryTypeDef(BaseValidatorModel):
    text: str

class KnowledgeBaseVectorSearchConfigurationTypeDef(BaseValidatorModel):
    filter: Optional["RetrievalFilterTypeDef"] = None
    numberOfResults: Optional[int] = None
    overrideSearchType: Optional[SearchTypeType] = None

class RetrievalResultContentTypeDef(BaseValidatorModel):
    text: str

class MemorySessionSummaryTypeDef(BaseValidatorModel):
    memoryId: Optional[str] = None
    sessionExpiryTime: Optional[datetime] = None
    sessionId: Optional[str] = None
    sessionStartTime: Optional[datetime] = None
    summaryText: Optional[str] = None

class RepromptResponseTypeDef(BaseValidatorModel):
    source: Optional[SourceType] = None
    text: Optional[str] = None

class QueryTransformationConfigurationTypeDef(BaseValidatorModel):
    type: Literal["QUERY_DECOMPOSITION"]

class RationaleTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    traceId: Optional[str] = None

class PostProcessingParsedResponseTypeDef(BaseValidatorModel):
    text: Optional[str] = None

class PreProcessingParsedResponseTypeDef(BaseValidatorModel):
    isValid: Optional[bool] = None
    rationale: Optional[str] = None

class RetrievalResultConfluenceLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None

class RetrievalResultS3LocationTypeDef(BaseValidatorModel):
    uri: Optional[str] = None

class RetrievalResultSalesforceLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None

class RetrievalResultSharePointLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None

class RetrievalResultWebLocationTypeDef(BaseValidatorModel):
    url: Optional[str] = None

class RetrieveAndGenerateInputTypeDef(BaseValidatorModel):
    text: str

class RetrieveAndGenerateOutputTypeDef(BaseValidatorModel):
    text: str

class RetrieveAndGenerateSessionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyArn: str

class SpanTypeDef(BaseValidatorModel):
    end: Optional[int] = None
    start: Optional[int] = None

class PropertyParametersTypeDef(BaseValidatorModel):
    properties: Optional[List[ParameterTypeDef]] = None

class RequestBodyTypeDef(BaseValidatorModel):
    content: Optional[Dict[str, List[ParameterTypeDef]]] = None

class ApiResultTypeDef(BaseValidatorModel):
    actionGroup: str
    apiPath: Optional[str] = None
    httpMethod: Optional[str] = None
    httpStatusCode: Optional[int] = None
    responseBody: Optional[Mapping[str, ContentBodyTypeDef]] = None
    responseState: Optional[ResponseStateType] = None

class FunctionResultTypeDef(BaseValidatorModel):
    actionGroup: str
    function: Optional[str] = None
    responseBody: Optional[Mapping[str, ContentBodyTypeDef]] = None
    responseState: Optional[ResponseStateType] = None

class ByteContentDocTypeDef(BaseValidatorModel):
    contentType: str
    data: BlobTypeDef
    identifier: str

class ByteContentFileTypeDef(BaseValidatorModel):
    data: BlobTypeDef
    mediaType: str

class FilePartTypeDef(BaseValidatorModel):
    files: Optional[List[OutputFileTypeDef]] = None

class RetrievalFilterTypeDef(BaseValidatorModel):
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

class FlowInputTypeDef(BaseValidatorModel):
    content: FlowInputContentTypeDef
    nodeName: str
    nodeOutputName: str

class FlowOutputEventTypeDef(BaseValidatorModel):
    content: FlowOutputContentTypeDef
    nodeName: str
    nodeType: NodeTypeType

class FunctionInvocationInputTypeDef(BaseValidatorModel):
    actionGroup: str
    function: Optional[str] = None
    parameters: Optional[List[FunctionParameterTypeDef]] = None

class GetAgentMemoryRequestGetAgentMemoryPaginateTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    memoryId: str
    memoryType: Literal["SESSION_SUMMARY"]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GuardrailContentPolicyAssessmentTypeDef(BaseValidatorModel):
    filters: Optional[List[GuardrailContentFilterTypeDef]] = None

class GuardrailWordPolicyAssessmentTypeDef(BaseValidatorModel):
    customWords: Optional[List[GuardrailCustomWordTypeDef]] = None
    managedWordLists: Optional[List[GuardrailManagedWordTypeDef]] = None

class GuardrailSensitiveInformationPolicyAssessmentTypeDef(BaseValidatorModel):
    piiEntities: Optional[List[GuardrailPiiEntityFilterTypeDef]] = None
    regexes: Optional[List[GuardrailRegexFilterTypeDef]] = None

class GuardrailTopicPolicyAssessmentTypeDef(BaseValidatorModel):
    topics: Optional[List[GuardrailTopicTypeDef]] = None

class InferenceConfigTypeDef(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfigTypeDef] = None

class ModelInvocationInputTypeDef(BaseValidatorModel):
    inferenceConfiguration: Optional[InferenceConfigurationTypeDef] = None
    overrideLambda: Optional[str] = None
    parserMode: Optional[CreationModeType] = None
    promptCreationMode: Optional[CreationModeType] = None
    text: Optional[str] = None
    traceId: Optional[str] = None
    type: Optional[PromptTypeType] = None

class KnowledgeBaseRetrievalConfigurationTypeDef(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationTypeDef

class MemoryTypeDef(BaseValidatorModel):
    sessionSummary: Optional[MemorySessionSummaryTypeDef] = None

class OrchestrationConfigurationTypeDef(BaseValidatorModel):
    queryTransformationConfiguration: QueryTransformationConfigurationTypeDef

class PostProcessingModelInvocationOutputTypeDef(BaseValidatorModel):
    parsedResponse: Optional[PostProcessingParsedResponseTypeDef] = None
    traceId: Optional[str] = None

class PreProcessingModelInvocationOutputTypeDef(BaseValidatorModel):
    parsedResponse: Optional[PreProcessingParsedResponseTypeDef] = None
    traceId: Optional[str] = None

class RetrievalResultLocationTypeDef(BaseValidatorModel):
    type: RetrievalResultLocationTypeType
    confluenceLocation: Optional[RetrievalResultConfluenceLocationTypeDef] = None
    s3Location: Optional[RetrievalResultS3LocationTypeDef] = None
    salesforceLocation: Optional[RetrievalResultSalesforceLocationTypeDef] = None
    sharePointLocation: Optional[RetrievalResultSharePointLocationTypeDef] = None
    webLocation: Optional[RetrievalResultWebLocationTypeDef] = None

class TextResponsePartTypeDef(BaseValidatorModel):
    span: Optional[SpanTypeDef] = None
    text: Optional[str] = None

class ApiRequestBodyTypeDef(BaseValidatorModel):
    content: Optional[Dict[str, PropertyParametersTypeDef]] = None

class ActionGroupInvocationInputTypeDef(BaseValidatorModel):
    actionGroupName: Optional[str] = None
    apiPath: Optional[str] = None
    executionType: Optional[ExecutionTypeType] = None
    function: Optional[str] = None
    invocationId: Optional[str] = None
    parameters: Optional[List[ParameterTypeDef]] = None
    requestBody: Optional[RequestBodyTypeDef] = None
    verb: Optional[str] = None

class InvocationResultMemberTypeDef(BaseValidatorModel):
    apiResult: Optional[ApiResultTypeDef] = None
    functionResult: Optional[FunctionResultTypeDef] = None

class ExternalSourceTypeDef(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    byteContent: Optional[ByteContentDocTypeDef] = None
    s3Location: Optional[S3ObjectDocTypeDef] = None

class FileSourceTypeDef(BaseValidatorModel):
    sourceType: FileSourceTypeType
    byteContent: Optional[ByteContentFileTypeDef] = None
    s3Location: Optional[S3ObjectFileTypeDef] = None

class InvokeFlowRequestRequestTypeDef(BaseValidatorModel):
    flowAliasIdentifier: str
    flowIdentifier: str
    inputs: Sequence[FlowInputTypeDef]

class FlowResponseStreamTypeDef(BaseValidatorModel):
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

class GuardrailAssessmentTypeDef(BaseValidatorModel):
    contentPolicy: Optional[GuardrailContentPolicyAssessmentTypeDef] = None
    sensitiveInformationPolicy: Optional[       GuardrailSensitiveInformationPolicyAssessmentTypeDef     ] = None
    topicPolicy: Optional[GuardrailTopicPolicyAssessmentTypeDef] = None
    wordPolicy: Optional[GuardrailWordPolicyAssessmentTypeDef] = None

class ExternalSourcesGenerationConfigurationTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    inferenceConfig: Optional[InferenceConfigTypeDef] = None
    promptTemplate: Optional[PromptTemplateTypeDef] = None

class GenerationConfigurationTypeDef(BaseValidatorModel):
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    inferenceConfig: Optional[InferenceConfigTypeDef] = None
    promptTemplate: Optional[PromptTemplateTypeDef] = None

class KnowledgeBaseConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalConfiguration: KnowledgeBaseRetrievalConfigurationTypeDef

class RetrieveRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQueryTypeDef
    nextToken: Optional[str] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None

class RetrieveRequestRetrievePaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    retrievalQuery: KnowledgeBaseQueryTypeDef
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAgentMemoryResponseTypeDef(BaseValidatorModel):
    memoryContents: List[MemoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PostProcessingTraceTypeDef(BaseValidatorModel):
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[PostProcessingModelInvocationOutputTypeDef] = None

class PreProcessingTraceTypeDef(BaseValidatorModel):
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    modelInvocationOutput: Optional[PreProcessingModelInvocationOutputTypeDef] = None

class KnowledgeBaseRetrievalResultTypeDef(BaseValidatorModel):
    content: RetrievalResultContentTypeDef
    location: Optional[RetrievalResultLocationTypeDef] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None
    score: Optional[float] = None

class RetrievedReferenceTypeDef(BaseValidatorModel):
    content: Optional[RetrievalResultContentTypeDef] = None
    location: Optional[RetrievalResultLocationTypeDef] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = None

class GeneratedResponsePartTypeDef(BaseValidatorModel):
    textResponsePart: Optional[TextResponsePartTypeDef] = None

class ApiInvocationInputTypeDef(BaseValidatorModel):
    actionGroup: str
    apiPath: Optional[str] = None
    httpMethod: Optional[str] = None
    parameters: Optional[List[ApiParameterTypeDef]] = None
    requestBody: Optional[ApiRequestBodyTypeDef] = None

class InvocationInputTypeDef(BaseValidatorModel):
    actionGroupInvocationInput: Optional[ActionGroupInvocationInputTypeDef] = None
    codeInterpreterInvocationInput: Optional[CodeInterpreterInvocationInputTypeDef] = None
    invocationType: Optional[InvocationTypeType] = None
    knowledgeBaseLookupInput: Optional[KnowledgeBaseLookupInputTypeDef] = None
    traceId: Optional[str] = None

class InputFileTypeDef(BaseValidatorModel):
    name: str
    source: FileSourceTypeDef
    useCase: FileUseCaseType

class InvokeFlowResponseTypeDef(BaseValidatorModel):
    responseStream: "EventStream[FlowResponseStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

class GuardrailTraceTypeDef(BaseValidatorModel):
    action: Optional[GuardrailActionType] = None
    inputAssessments: Optional[List[GuardrailAssessmentTypeDef]] = None
    outputAssessments: Optional[List[GuardrailAssessmentTypeDef]] = None
    traceId: Optional[str] = None

class ExternalSourcesRetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    modelArn: str
    sources: Sequence[ExternalSourceTypeDef]
    generationConfiguration: Optional[ExternalSourcesGenerationConfigurationTypeDef] = None

class KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    modelArn: str
    generationConfiguration: Optional[GenerationConfigurationTypeDef] = None
    orchestrationConfiguration: Optional[OrchestrationConfigurationTypeDef] = None
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None

class RetrieveResponseTypeDef(BaseValidatorModel):
    nextToken: str
    retrievalResults: List[KnowledgeBaseRetrievalResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class KnowledgeBaseLookupOutputTypeDef(BaseValidatorModel):
    retrievedReferences: Optional[List[RetrievedReferenceTypeDef]] = None

class CitationTypeDef(BaseValidatorModel):
    generatedResponsePart: Optional[GeneratedResponsePartTypeDef] = None
    retrievedReferences: Optional[List[RetrievedReferenceTypeDef]] = None

class InvocationInputMemberTypeDef(BaseValidatorModel):
    apiInvocationInput: Optional[ApiInvocationInputTypeDef] = None
    functionInvocationInput: Optional[FunctionInvocationInputTypeDef] = None

class SessionStateTypeDef(BaseValidatorModel):
    files: Optional[Sequence[InputFileTypeDef]] = None
    invocationId: Optional[str] = None
    knowledgeBaseConfigurations: Optional[Sequence[KnowledgeBaseConfigurationTypeDef]] = None
    promptSessionAttributes: Optional[Mapping[str, str]] = None
    returnControlInvocationResults: Optional[Sequence[InvocationResultMemberTypeDef]] = None
    sessionAttributes: Optional[Mapping[str, str]] = None

class RetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    type: RetrieveAndGenerateTypeType
    externalSourcesConfiguration: Optional[       ExternalSourcesRetrieveAndGenerateConfigurationTypeDef     ] = None
    knowledgeBaseConfiguration: Optional[       KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef     ] = None

class ObservationTypeDef(BaseValidatorModel):
    actionGroupInvocationOutput: Optional[ActionGroupInvocationOutputTypeDef] = None
    codeInterpreterInvocationOutput: Optional[CodeInterpreterInvocationOutputTypeDef] = None
    finalResponse: Optional[FinalResponseTypeDef] = None
    knowledgeBaseLookupOutput: Optional[KnowledgeBaseLookupOutputTypeDef] = None
    repromptResponse: Optional[RepromptResponseTypeDef] = None
    traceId: Optional[str] = None
    type: Optional[TypeType] = None

class AttributionTypeDef(BaseValidatorModel):
    citations: Optional[List[CitationTypeDef]] = None

class RetrieveAndGenerateResponseTypeDef(BaseValidatorModel):
    citations: List[CitationTypeDef]
    guardrailAction: GuadrailActionType
    output: RetrieveAndGenerateOutputTypeDef
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReturnControlPayloadTypeDef(BaseValidatorModel):
    invocationId: Optional[str] = None
    invocationInputs: Optional[List[InvocationInputMemberTypeDef]] = None

class InvokeAgentRequestRequestTypeDef(BaseValidatorModel):
    agentAliasId: str
    agentId: str
    sessionId: str
    enableTrace: Optional[bool] = None
    endSession: Optional[bool] = None
    inputText: Optional[str] = None
    memoryId: Optional[str] = None
    sessionState: Optional[SessionStateTypeDef] = None

class RetrieveAndGenerateRequestRequestTypeDef(BaseValidatorModel):
    input: RetrieveAndGenerateInputTypeDef
    retrieveAndGenerateConfiguration: Optional[RetrieveAndGenerateConfigurationTypeDef] = None
    sessionConfiguration: Optional[RetrieveAndGenerateSessionConfigurationTypeDef] = None
    sessionId: Optional[str] = None

class OrchestrationTraceTypeDef(BaseValidatorModel):
    invocationInput: Optional[InvocationInputTypeDef] = None
    modelInvocationInput: Optional[ModelInvocationInputTypeDef] = None
    observation: Optional[ObservationTypeDef] = None
    rationale: Optional[RationaleTypeDef] = None

class PayloadPartTypeDef(BaseValidatorModel):
    attribution: Optional[AttributionTypeDef] = None
    bytes: Optional[bytes] = None

class TraceTypeDef(BaseValidatorModel):
    failureTrace: Optional[FailureTraceTypeDef] = None
    guardrailTrace: Optional[GuardrailTraceTypeDef] = None
    orchestrationTrace: Optional[OrchestrationTraceTypeDef] = None
    postProcessingTrace: Optional[PostProcessingTraceTypeDef] = None
    preProcessingTrace: Optional[PreProcessingTraceTypeDef] = None

class TracePartTypeDef(BaseValidatorModel):
    agentAliasId: Optional[str] = None
    agentId: Optional[str] = None
    agentVersion: Optional[str] = None
    sessionId: Optional[str] = None
    trace: Optional[TraceTypeDef] = None

class ResponseStreamTypeDef(BaseValidatorModel):
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

class InvokeAgentResponseTypeDef(BaseValidatorModel):
    completion: "EventStream[ResponseStreamTypeDef]"
    contentType: str
    memoryId: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

