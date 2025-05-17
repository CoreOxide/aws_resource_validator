from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.appflow.appflow_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AggregationConfig(BaseValidatorModel):
    aggregationType: Optional[AggregationTypeType] = None
    targetFileSize: Optional[int] = None


class AmplitudeConnectorProfileCredentials(BaseValidatorModel):
    apiKey: str
    secretKey: str


class AmplitudeSourceProperties(BaseValidatorModel):
    object: str


class ApiKeyCredentials(BaseValidatorModel):
    apiKey: str
    apiSecretKey: Optional[str] = None


class AuthParameter(BaseValidatorModel):
    key: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    isSensitiveField: Optional[bool] = None
    connectorSuppliedValues: Optional[List[str]] = None


class BasicAuthCredentials(BaseValidatorModel):
    username: str
    password: str


# This class is the input for the 'cancel_flow_executions' function.
class CancelFlowExecutionsRequest(BaseValidatorModel):
    flowName: str
    executionIds: Optional[List[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConnectorRuntimeSetting(BaseValidatorModel):
    key: Optional[str] = None
    dataType: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    scope: Optional[str] = None
    connectorSuppliedValueOptions: Optional[List[str]] = None


class DataTransferApi(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[DataTransferApiTypeType] = None


class ConnectorDetail(BaseValidatorModel):
    connectorDescription: Optional[str] = None
    connectorName: Optional[str] = None
    connectorOwner: Optional[str] = None
    connectorVersion: Optional[str] = None
    applicationType: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    registeredAt: Optional[datetime] = None
    registeredBy: Optional[str] = None
    connectorProvisioningType: Optional[Literal['LAMBDA']] = None
    connectorModes: Optional[List[str]] = None
    supportedDataTransferTypes: Optional[List[SupportedDataTransferTypeType]] = None


class DestinationFieldProperties(BaseValidatorModel):
    isCreatable: Optional[bool] = None
    isNullable: Optional[bool] = None
    isUpsertable: Optional[bool] = None
    isUpdatable: Optional[bool] = None
    isDefaultedOnCreate: Optional[bool] = None
    supportedWriteOperations: Optional[List[WriteOperationTypeType]] = None


class SourceFieldProperties(BaseValidatorModel):
    isRetrievable: Optional[bool] = None
    isQueryable: Optional[bool] = None
    isTimestampFieldForIncrementalQueries: Optional[bool] = None


class ConnectorEntity(BaseValidatorModel):
    name: str
    label: Optional[str] = None
    hasNestedEntities: Optional[bool] = None


class GoogleAnalyticsMetadata(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None


class HoneycodeMetadata(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None


class SalesforceMetadata(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None
    dataTransferApis: Optional[List[SalesforceDataTransferApiType]] = None
    oauth2GrantTypesSupported: Optional[List[OAuth2GrantTypeType]] = None


class SlackMetadata(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None


class SnowflakeMetadata(BaseValidatorModel):
    supportedRegions: Optional[List[str]] = None


class ZendeskMetadata(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None


class ConnectorOAuthRequest(BaseValidatorModel):
    authCode: Optional[str] = None
    redirectUri: Optional[str] = None


class ConnectorOperator(BaseValidatorModel):
    Amplitude: Optional[Literal['BETWEEN']] = None
    Datadog: Optional[DatadogConnectorOperatorType] = None
    Dynatrace: Optional[DynatraceConnectorOperatorType] = None
    GoogleAnalytics: Optional[GoogleAnalyticsConnectorOperatorType] = None
    InforNexus: Optional[InforNexusConnectorOperatorType] = None
    Marketo: Optional[MarketoConnectorOperatorType] = None
    S3: Optional[S3ConnectorOperatorType] = None
    Salesforce: Optional[SalesforceConnectorOperatorType] = None
    ServiceNow: Optional[ServiceNowConnectorOperatorType] = None
    Singular: Optional[SingularConnectorOperatorType] = None
    Slack: Optional[SlackConnectorOperatorType] = None
    Trendmicro: Optional[TrendmicroConnectorOperatorType] = None
    Veeva: Optional[VeevaConnectorOperatorType] = None
    Zendesk: Optional[ZendeskConnectorOperatorType] = None
    SAPOData: Optional[SAPODataConnectorOperatorType] = None
    CustomConnector: Optional[OperatorType] = None
    Pardot: Optional[PardotConnectorOperatorType] = None


class DatadogConnectorProfileCredentials(BaseValidatorModel):
    apiKey: str
    applicationKey: str


class DynatraceConnectorProfileCredentials(BaseValidatorModel):
    apiToken: str


class InforNexusConnectorProfileCredentials(BaseValidatorModel):
    accessKeyId: str
    userId: str
    secretAccessKey: str
    datakey: str


class RedshiftConnectorProfileCredentials(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[str] = None


class SingularConnectorProfileCredentials(BaseValidatorModel):
    apiKey: str


class SnowflakeConnectorProfileCredentials(BaseValidatorModel):
    username: str
    password: str


class TrendmicroConnectorProfileCredentials(BaseValidatorModel):
    apiSecretKey: str


class VeevaConnectorProfileCredentials(BaseValidatorModel):
    username: str
    password: str


class DatadogConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class DynatraceConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class InforNexusConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class MarketoConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class PardotConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: Optional[str] = None
    isSandboxEnvironment: Optional[bool] = None
    businessUnitId: Optional[str] = None


class RedshiftConnectorProfileProperties(BaseValidatorModel):
    bucketName: str
    roleArn: str
    databaseUrl: Optional[str] = None
    bucketPrefix: Optional[str] = None
    dataApiRoleArn: Optional[str] = None
    isRedshiftServerless: Optional[bool] = None
    clusterIdentifier: Optional[str] = None
    workgroupName: Optional[str] = None
    databaseName: Optional[str] = None


class SalesforceConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: Optional[str] = None
    isSandboxEnvironment: Optional[bool] = None
    usePrivateLinkForMetadataAndAuthorization: Optional[bool] = None


class ServiceNowConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class SlackConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class SnowflakeConnectorProfileProperties(BaseValidatorModel):
    warehouse: str
    stage: str
    bucketName: str
    bucketPrefix: Optional[str] = None
    privateLinkServiceName: Optional[str] = None
    accountName: Optional[str] = None
    region: Optional[str] = None


class VeevaConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class ZendeskConnectorProfileProperties(BaseValidatorModel):
    instanceUrl: str


class PrivateConnectionProvisioningState(BaseValidatorModel):
    status: Optional[PrivateConnectionProvisioningStatusType] = None
    failureMessage: Optional[str] = None
    failureCause: Optional[PrivateConnectionProvisioningFailureCauseType] = None


class LambdaConnectorProvisioningConfig(BaseValidatorModel):
    lambdaArn: str


class CustomAuthCredentials(BaseValidatorModel):
    customAuthenticationType: str
    credentialsMap: Optional[Dict[str, str]] = None


class ErrorHandlingConfig(BaseValidatorModel):
    failOnFirstDestinationError: Optional[bool] = None
    bucketPrefix: Optional[str] = None
    bucketName: Optional[str] = None


class OAuth2PropertiesOutput(BaseValidatorModel):
    tokenUrl: str
    oAuth2GrantType: OAuth2GrantTypeType
    tokenUrlCustomProperties: Optional[Dict[str, str]] = None


class CustomerProfilesDestinationProperties(BaseValidatorModel):
    domainName: str
    objectTypeName: Optional[str] = None


class DatadogSourceProperties(BaseValidatorModel):
    object: str


class DeleteConnectorProfileRequest(BaseValidatorModel):
    connectorProfileName: str
    forceDelete: Optional[bool] = None


class DeleteFlowRequest(BaseValidatorModel):
    flowName: str
    forceDelete: Optional[bool] = None


# This class is the input for the 'describe_connector_entity' function.
class DescribeConnectorEntityRequest(BaseValidatorModel):
    connectorEntityName: str
    connectorType: Optional[ConnectorTypeType] = None
    connectorProfileName: Optional[str] = None
    apiVersion: Optional[str] = None


# This class is the input for the 'describe_connector_profiles' function.
class DescribeConnectorProfilesRequest(BaseValidatorModel):
    connectorProfileNames: Optional[List[str]] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'describe_connector' function.
class DescribeConnectorRequest(BaseValidatorModel):
    connectorType: ConnectorTypeType
    connectorLabel: Optional[str] = None


# This class is the input for the 'describe_connectors' function.
class DescribeConnectorsRequest(BaseValidatorModel):
    connectorTypes: Optional[List[ConnectorTypeType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'describe_flow_execution_records' function.
class DescribeFlowExecutionRecordsRequest(BaseValidatorModel):
    flowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'describe_flow' function.
class DescribeFlowRequest(BaseValidatorModel):
    flowName: str


class ExecutionDetails(BaseValidatorModel):
    mostRecentExecutionMessage: Optional[str] = None
    mostRecentExecutionTime: Optional[datetime] = None
    mostRecentExecutionStatus: Optional[ExecutionStatusType] = None


class DynatraceSourceProperties(BaseValidatorModel):
    object: str


class ErrorInfo(BaseValidatorModel):
    putFailuresCount: Optional[int] = None
    executionMessage: Optional[str] = None


class Range(BaseValidatorModel):
    maximum: Optional[float] = None
    minimum: Optional[float] = None


class GlueDataCatalogConfig(BaseValidatorModel):
    roleArn: str
    databaseName: str
    tablePrefix: str


class GoogleAnalyticsSourceProperties(BaseValidatorModel):
    object: str


class IncrementalPullConfig(BaseValidatorModel):
    datetimeTypeFieldName: Optional[str] = None


class InforNexusSourceProperties(BaseValidatorModel):
    object: str


# This class is the input for the 'list_connector_entities' function.
class ListConnectorEntitiesRequest(BaseValidatorModel):
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    entitiesPath: Optional[str] = None
    apiVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_connectors' function.
class ListConnectorsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_flows' function.
class ListFlowsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class MarketoSourceProperties(BaseValidatorModel):
    object: str


class RegistrationOutput(BaseValidatorModel):
    message: Optional[str] = None
    result: Optional[str] = None
    status: Optional[ExecutionStatusType] = None


class OAuth2CustomParameter(BaseValidatorModel):
    key: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    isSensitiveField: Optional[bool] = None
    connectorSuppliedValues: Optional[List[str]] = None
    type: Optional[OAuth2CustomPropTypeType] = None


class OAuth2Properties(BaseValidatorModel):
    tokenUrl: str
    oAuth2GrantType: OAuth2GrantTypeType
    tokenUrlCustomProperties: Optional[Dict[str, str]] = None


class OAuthPropertiesOutput(BaseValidatorModel):
    tokenUrl: str
    authCodeUrl: str
    oAuthScopes: List[str]


class OAuthProperties(BaseValidatorModel):
    tokenUrl: str
    authCodeUrl: str
    oAuthScopes: List[str]


class PardotSourceProperties(BaseValidatorModel):
    object: str


class PrefixConfigOutput(BaseValidatorModel):
    prefixType: Optional[PrefixTypeType] = None
    prefixFormat: Optional[PrefixFormatType] = None
    pathPrefixHierarchy: Optional[List[PathPrefixType]] = None


class PrefixConfig(BaseValidatorModel):
    prefixType: Optional[PrefixTypeType] = None
    prefixFormat: Optional[PrefixFormatType] = None
    pathPrefixHierarchy: Optional[List[PathPrefixType]] = None


class ResetConnectorMetadataCacheRequest(BaseValidatorModel):
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorEntityName: Optional[str] = None
    entitiesPath: Optional[str] = None
    apiVersion: Optional[str] = None


class S3InputFormatConfig(BaseValidatorModel):
    s3InputFileType: Optional[S3InputFileTypeType] = None


class SuccessResponseHandlingConfig(BaseValidatorModel):
    bucketPrefix: Optional[str] = None
    bucketName: Optional[str] = None


class SAPODataPaginationConfig(BaseValidatorModel):
    maxPageSize: int


class SAPODataParallelismConfig(BaseValidatorModel):
    maxParallelism: int


class SalesforceSourceProperties(BaseValidatorModel):
    object: str
    enableDynamicFieldUpdate: Optional[bool] = None
    includeDeletedRecords: Optional[bool] = None
    dataTransferApi: Optional[SalesforceDataTransferApiType] = None


class ScheduledTriggerPropertiesOutput(BaseValidatorModel):
    scheduleExpression: str
    dataPullMode: Optional[DataPullModeType] = None
    scheduleStartTime: Optional[datetime] = None
    scheduleEndTime: Optional[datetime] = None
    timezone: Optional[str] = None
    scheduleOffset: Optional[int] = None
    firstExecutionFrom: Optional[datetime] = None
    flowErrorDeactivationThreshold: Optional[int] = None

Timestamp = Union[datetime, str]


class ServiceNowSourceProperties(BaseValidatorModel):
    object: str


class SingularSourceProperties(BaseValidatorModel):
    object: str


class SlackSourceProperties(BaseValidatorModel):
    object: str


class TrendmicroSourceProperties(BaseValidatorModel):
    object: str


class VeevaSourceProperties(BaseValidatorModel):
    object: str
    documentType: Optional[str] = None
    includeSourceFiles: Optional[bool] = None
    includeRenditions: Optional[bool] = None
    includeAllVersions: Optional[bool] = None


class ZendeskSourceProperties(BaseValidatorModel):
    object: str


# This class is the input for the 'start_flow' function.
class StartFlowRequest(BaseValidatorModel):
    flowName: str
    clientToken: Optional[str] = None


# This class is the input for the 'stop_flow' function.
class StopFlowRequest(BaseValidatorModel):
    flowName: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UnregisterConnectorRequest(BaseValidatorModel):
    connectorLabel: str
    forceDelete: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class CustomAuthConfig(BaseValidatorModel):
    customAuthenticationType: Optional[str] = None
    authParameters: Optional[List[AuthParameter]] = None


# This class is the output for the 'cancel_flow_executions' function.
class CancelFlowExecutionsResponse(BaseValidatorModel):
    invalidExecutions: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_connector_profile' function.
class CreateConnectorProfileResponse(BaseValidatorModel):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_flow' function.
class CreateFlowResponse(BaseValidatorModel):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_connector' function.
class RegisterConnectorResponse(BaseValidatorModel):
    connectorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_flow' function.
class StartFlowResponse(BaseValidatorModel):
    flowArn: str
    flowStatus: FlowStatusType
    executionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_flow' function.
class StopFlowResponse(BaseValidatorModel):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_connector_profile' function.
class UpdateConnectorProfileResponse(BaseValidatorModel):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_connector_registration' function.
class UpdateConnectorRegistrationResponse(BaseValidatorModel):
    connectorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_flow' function.
class UpdateFlowResponse(BaseValidatorModel):
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadata


class CustomConnectorSourcePropertiesOutput(BaseValidatorModel):
    entityName: str
    customProperties: Optional[Dict[str, str]] = None
    dataTransferApi: Optional[DataTransferApi] = None


class CustomConnectorSourceProperties(BaseValidatorModel):
    entityName: str
    customProperties: Optional[Dict[str, str]] = None
    dataTransferApi: Optional[DataTransferApi] = None


# This class is the output for the 'list_connectors' function.
class ListConnectorsResponse(BaseValidatorModel):
    connectors: List[ConnectorDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_connector_entities' function.
class ListConnectorEntitiesResponse(BaseValidatorModel):
    connectorEntityMap: Dict[str, List[ConnectorEntity]]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectorMetadata(BaseValidatorModel):
    Amplitude: Optional[Dict[str, Any]] = None
    Datadog: Optional[Dict[str, Any]] = None
    Dynatrace: Optional[Dict[str, Any]] = None
    GoogleAnalytics: Optional[GoogleAnalyticsMetadata] = None
    InforNexus: Optional[Dict[str, Any]] = None
    Marketo: Optional[Dict[str, Any]] = None
    Redshift: Optional[Dict[str, Any]] = None
    S3: Optional[Dict[str, Any]] = None
    Salesforce: Optional[SalesforceMetadata] = None
    ServiceNow: Optional[Dict[str, Any]] = None
    Singular: Optional[Dict[str, Any]] = None
    Slack: Optional[SlackMetadata] = None
    Snowflake: Optional[SnowflakeMetadata] = None
    Trendmicro: Optional[Dict[str, Any]] = None
    Veeva: Optional[Dict[str, Any]] = None
    Zendesk: Optional[ZendeskMetadata] = None
    EventBridge: Optional[Dict[str, Any]] = None
    Upsolver: Optional[Dict[str, Any]] = None
    CustomerProfiles: Optional[Dict[str, Any]] = None
    Honeycode: Optional[HoneycodeMetadata] = None
    SAPOData: Optional[Dict[str, Any]] = None
    Pardot: Optional[Dict[str, Any]] = None


class GoogleAnalyticsConnectorProfileCredentials(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None


class HoneycodeConnectorProfileCredentials(BaseValidatorModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None


class MarketoConnectorProfileCredentials(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None


class OAuth2Credentials(BaseValidatorModel):
    clientId: Optional[str] = None
    clientSecret: Optional[str] = None
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None


class OAuthCredentials(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None


class PardotConnectorProfileCredentials(BaseValidatorModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None
    clientCredentialsArn: Optional[str] = None


class SalesforceConnectorProfileCredentials(BaseValidatorModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None
    clientCredentialsArn: Optional[str] = None
    oAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    jwtToken: Optional[str] = None


class SlackConnectorProfileCredentials(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None


class ZendeskConnectorProfileCredentials(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequest] = None


class TaskOutput(BaseValidatorModel):
    sourceFields: List[str]
    taskType: TaskTypeType
    connectorOperator: Optional[ConnectorOperator] = None
    destinationField: Optional[str] = None
    taskProperties: Optional[Dict[OperatorPropertiesKeysType, str]] = None


class Task(BaseValidatorModel):
    sourceFields: List[str]
    taskType: TaskTypeType
    connectorOperator: Optional[ConnectorOperator] = None
    destinationField: Optional[str] = None
    taskProperties: Optional[Dict[OperatorPropertiesKeysType, str]] = None


class ConnectorProvisioningConfig(BaseValidatorModel):
    lambda_:Optional[LambdaConnectorProvisioningConfig] = None


class CustomConnectorDestinationPropertiesOutput(BaseValidatorModel):
    entityName: str
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    idFieldNames: Optional[List[str]] = None
    customProperties: Optional[Dict[str, str]] = None


class CustomConnectorDestinationProperties(BaseValidatorModel):
    entityName: str
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    idFieldNames: Optional[List[str]] = None
    customProperties: Optional[Dict[str, str]] = None


class EventBridgeDestinationProperties(BaseValidatorModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None


class HoneycodeDestinationProperties(BaseValidatorModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None


class MarketoDestinationProperties(BaseValidatorModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None


class RedshiftDestinationProperties(BaseValidatorModel):
    object: str
    intermediateBucketName: str
    bucketPrefix: Optional[str] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None


class SalesforceDestinationPropertiesOutput(BaseValidatorModel):
    object: str
    idFieldNames: Optional[List[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    dataTransferApi: Optional[SalesforceDataTransferApiType] = None


class SalesforceDestinationProperties(BaseValidatorModel):
    object: str
    idFieldNames: Optional[List[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    dataTransferApi: Optional[SalesforceDataTransferApiType] = None


class SnowflakeDestinationProperties(BaseValidatorModel):
    object: str
    intermediateBucketName: str
    bucketPrefix: Optional[str] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None


class ZendeskDestinationPropertiesOutput(BaseValidatorModel):
    object: str
    idFieldNames: Optional[List[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None


class ZendeskDestinationProperties(BaseValidatorModel):
    object: str
    idFieldNames: Optional[List[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None


class CustomConnectorProfilePropertiesOutput(BaseValidatorModel):
    profileProperties: Optional[Dict[str, str]] = None
    oAuth2Properties: Optional[OAuth2PropertiesOutput] = None


class FlowDefinition(BaseValidatorModel):
    flowArn: Optional[str] = None
    description: Optional[str] = None
    flowName: Optional[str] = None
    flowStatus: Optional[FlowStatusType] = None
    sourceConnectorType: Optional[ConnectorTypeType] = None
    sourceConnectorLabel: Optional[str] = None
    destinationConnectorType: Optional[ConnectorTypeType] = None
    destinationConnectorLabel: Optional[str] = None
    triggerType: Optional[TriggerTypeType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    lastRunExecutionDetails: Optional[ExecutionDetails] = None


class ExecutionResult(BaseValidatorModel):
    errorInfo: Optional[ErrorInfo] = None
    bytesProcessed: Optional[int] = None
    bytesWritten: Optional[int] = None
    recordsProcessed: Optional[int] = None
    numParallelProcesses: Optional[int] = None
    maxPageSize: Optional[int] = None


class FieldTypeDetails(BaseValidatorModel):
    fieldType: str
    filterOperators: List[OperatorType]
    supportedValues: Optional[List[str]] = None
    valueRegexPattern: Optional[str] = None
    supportedDateFormat: Optional[str] = None
    fieldValueRange: Optional[Range] = None
    fieldLengthRange: Optional[Range] = None


class MetadataCatalogConfig(BaseValidatorModel):
    glueDataCatalog: Optional[GlueDataCatalogConfig] = None


class MetadataCatalogDetail(BaseValidatorModel):
    catalogType: Optional[Literal['GLUE']] = None
    tableName: Optional[str] = None
    tableRegistrationOutput: Optional[RegistrationOutput] = None
    partitionRegistrationOutput: Optional[RegistrationOutput] = None


class OAuth2Defaults(BaseValidatorModel):
    oauthScopes: Optional[List[str]] = None
    tokenUrls: Optional[List[str]] = None
    authCodeUrls: Optional[List[str]] = None
    oauth2GrantTypesSupported: Optional[List[OAuth2GrantTypeType]] = None
    oauth2CustomProperties: Optional[List[OAuth2CustomParameter]] = None

OAuth2PropertiesUnion = Union[OAuth2Properties, OAuth2PropertiesOutput]


class SAPODataConnectorProfilePropertiesOutput(BaseValidatorModel):
    applicationHostUrl: str
    applicationServicePath: str
    portNumber: int
    clientNumber: str
    logonLanguage: Optional[str] = None
    privateLinkServiceName: Optional[str] = None
    oAuthProperties: Optional[OAuthPropertiesOutput] = None
    disableSSO: Optional[bool] = None

OAuthPropertiesUnion = Union[OAuthProperties, OAuthPropertiesOutput]


class S3OutputFormatConfigOutput(BaseValidatorModel):
    fileType: Optional[FileTypeType] = None
    prefixConfig: Optional[PrefixConfigOutput] = None
    aggregationConfig: Optional[AggregationConfig] = None
    preserveSourceDataTyping: Optional[bool] = None


class UpsolverS3OutputFormatConfigOutput(BaseValidatorModel):
    prefixConfig: PrefixConfigOutput
    fileType: Optional[FileTypeType] = None
    aggregationConfig: Optional[AggregationConfig] = None

PrefixConfigUnion = Union[PrefixConfig, PrefixConfigOutput]


class S3SourceProperties(BaseValidatorModel):
    bucketName: str
    bucketPrefix: Optional[str] = None
    s3InputFormatConfig: Optional[S3InputFormatConfig] = None


class SAPODataDestinationPropertiesOutput(BaseValidatorModel):
    objectPath: str
    successResponseHandlingConfig: Optional[SuccessResponseHandlingConfig] = None
    idFieldNames: Optional[List[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None


class SAPODataDestinationProperties(BaseValidatorModel):
    objectPath: str
    successResponseHandlingConfig: Optional[SuccessResponseHandlingConfig] = None
    idFieldNames: Optional[List[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfig] = None
    writeOperationType: Optional[WriteOperationTypeType] = None


class SAPODataSourceProperties(BaseValidatorModel):
    objectPath: Optional[str] = None
    parallelismConfig: Optional[SAPODataParallelismConfig] = None
    paginationConfig: Optional[SAPODataPaginationConfig] = None


class TriggerPropertiesOutput(BaseValidatorModel):
    Scheduled: Optional[ScheduledTriggerPropertiesOutput] = None


class ScheduledTriggerProperties(BaseValidatorModel):
    scheduleExpression: str
    dataPullMode: Optional[DataPullModeType] = None
    scheduleStartTime: Optional[Timestamp] = None
    scheduleEndTime: Optional[Timestamp] = None
    timezone: Optional[str] = None
    scheduleOffset: Optional[int] = None
    firstExecutionFrom: Optional[Timestamp] = None
    flowErrorDeactivationThreshold: Optional[int] = None


class CustomConnectorProfileCredentials(BaseValidatorModel):
    authenticationType: AuthenticationTypeType
    basic: Optional[BasicAuthCredentials] = None
    oauth2: Optional[OAuth2Credentials] = None
    apiKey: Optional[ApiKeyCredentials] = None
    custom: Optional[CustomAuthCredentials] = None


class ServiceNowConnectorProfileCredentials(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[str] = None
    oAuth2Credentials: Optional[OAuth2Credentials] = None


class SAPODataConnectorProfileCredentials(BaseValidatorModel):
    basicAuthCredentials: Optional[BasicAuthCredentials] = None
    oAuthCredentials: Optional[OAuthCredentials] = None

TaskUnion = Union[Task, TaskOutput]


# This class is the input for the 'register_connector' function.
class RegisterConnectorRequest(BaseValidatorModel):
    connectorLabel: Optional[str] = None
    description: Optional[str] = None
    connectorProvisioningType: Optional[Literal['LAMBDA']] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfig] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_connector_registration' function.
class UpdateConnectorRegistrationRequest(BaseValidatorModel):
    connectorLabel: str
    description: Optional[str] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfig] = None
    clientToken: Optional[str] = None

CustomConnectorDestinationPropertiesUnion = Union[CustomConnectorDestinationProperties, CustomConnectorDestinationPropertiesOutput]

SalesforceDestinationPropertiesUnion = Union[SalesforceDestinationProperties, SalesforceDestinationPropertiesOutput]

ZendeskDestinationPropertiesUnion = Union[ZendeskDestinationProperties, ZendeskDestinationPropertiesOutput]


# This class is the output for the 'list_flows' function.
class ListFlowsResponse(BaseValidatorModel):
    flows: List[FlowDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SupportedFieldTypeDetails(BaseValidatorModel):
    v1: FieldTypeDetails


class ExecutionRecord(BaseValidatorModel):
    executionId: Optional[str] = None
    executionStatus: Optional[ExecutionStatusType] = None
    executionResult: Optional[ExecutionResult] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    dataPullStartTime: Optional[datetime] = None
    dataPullEndTime: Optional[datetime] = None
    metadataCatalogDetails: Optional[List[MetadataCatalogDetail]] = None


class AuthenticationConfig(BaseValidatorModel):
    isBasicAuthSupported: Optional[bool] = None
    isApiKeyAuthSupported: Optional[bool] = None
    isOAuth2Supported: Optional[bool] = None
    isCustomAuthSupported: Optional[bool] = None
    oAuth2Defaults: Optional[OAuth2Defaults] = None
    customAuthConfigs: Optional[List[CustomAuthConfig]] = None


class CustomConnectorProfileProperties(BaseValidatorModel):
    profileProperties: Optional[Dict[str, str]] = None
    oAuth2Properties: Optional[OAuth2PropertiesUnion] = None


class ConnectorProfilePropertiesOutput(BaseValidatorModel):
    Amplitude: Optional[Dict[str, Any]] = None
    Datadog: Optional[DatadogConnectorProfileProperties] = None
    Dynatrace: Optional[DynatraceConnectorProfileProperties] = None
    GoogleAnalytics: Optional[Dict[str, Any]] = None
    Honeycode: Optional[Dict[str, Any]] = None
    InforNexus: Optional[InforNexusConnectorProfileProperties] = None
    Marketo: Optional[MarketoConnectorProfileProperties] = None
    Redshift: Optional[RedshiftConnectorProfileProperties] = None
    Salesforce: Optional[SalesforceConnectorProfileProperties] = None
    ServiceNow: Optional[ServiceNowConnectorProfileProperties] = None
    Singular: Optional[Dict[str, Any]] = None
    Slack: Optional[SlackConnectorProfileProperties] = None
    Snowflake: Optional[SnowflakeConnectorProfileProperties] = None
    Trendmicro: Optional[Dict[str, Any]] = None
    Veeva: Optional[VeevaConnectorProfileProperties] = None
    Zendesk: Optional[ZendeskConnectorProfileProperties] = None
    SAPOData: Optional[SAPODataConnectorProfilePropertiesOutput] = None
    CustomConnector: Optional[CustomConnectorProfilePropertiesOutput] = None
    Pardot: Optional[PardotConnectorProfileProperties] = None


class SAPODataConnectorProfileProperties(BaseValidatorModel):
    applicationHostUrl: str
    applicationServicePath: str
    portNumber: int
    clientNumber: str
    logonLanguage: Optional[str] = None
    privateLinkServiceName: Optional[str] = None
    oAuthProperties: Optional[OAuthPropertiesUnion] = None
    disableSSO: Optional[bool] = None


class S3DestinationPropertiesOutput(BaseValidatorModel):
    bucketName: str
    bucketPrefix: Optional[str] = None
    s3OutputFormatConfig: Optional[S3OutputFormatConfigOutput] = None


class UpsolverDestinationPropertiesOutput(BaseValidatorModel):
    bucketName: str
    s3OutputFormatConfig: UpsolverS3OutputFormatConfigOutput
    bucketPrefix: Optional[str] = None


class S3OutputFormatConfig(BaseValidatorModel):
    fileType: Optional[FileTypeType] = None
    prefixConfig: Optional[PrefixConfigUnion] = None
    aggregationConfig: Optional[AggregationConfig] = None
    preserveSourceDataTyping: Optional[bool] = None


class UpsolverS3OutputFormatConfig(BaseValidatorModel):
    prefixConfig: PrefixConfigUnion
    fileType: Optional[FileTypeType] = None
    aggregationConfig: Optional[AggregationConfig] = None

SAPODataDestinationPropertiesUnion = Union[SAPODataDestinationProperties, SAPODataDestinationPropertiesOutput]


class SourceConnectorPropertiesOutput(BaseValidatorModel):
    Amplitude: Optional[AmplitudeSourceProperties] = None
    Datadog: Optional[DatadogSourceProperties] = None
    Dynatrace: Optional[DynatraceSourceProperties] = None
    GoogleAnalytics: Optional[GoogleAnalyticsSourceProperties] = None
    InforNexus: Optional[InforNexusSourceProperties] = None
    Marketo: Optional[MarketoSourceProperties] = None
    S3: Optional[S3SourceProperties] = None
    Salesforce: Optional[SalesforceSourceProperties] = None
    ServiceNow: Optional[ServiceNowSourceProperties] = None
    Singular: Optional[SingularSourceProperties] = None
    Slack: Optional[SlackSourceProperties] = None
    Trendmicro: Optional[TrendmicroSourceProperties] = None
    Veeva: Optional[VeevaSourceProperties] = None
    Zendesk: Optional[ZendeskSourceProperties] = None
    SAPOData: Optional[SAPODataSourceProperties] = None
    CustomConnector: Optional[CustomConnectorSourcePropertiesOutput] = None
    Pardot: Optional[PardotSourceProperties] = None


class SourceConnectorProperties(BaseValidatorModel):
    Amplitude: Optional[AmplitudeSourceProperties] = None
    Datadog: Optional[DatadogSourceProperties] = None
    Dynatrace: Optional[DynatraceSourceProperties] = None
    GoogleAnalytics: Optional[GoogleAnalyticsSourceProperties] = None
    InforNexus: Optional[InforNexusSourceProperties] = None
    Marketo: Optional[MarketoSourceProperties] = None
    S3: Optional[S3SourceProperties] = None
    Salesforce: Optional[SalesforceSourceProperties] = None
    ServiceNow: Optional[ServiceNowSourceProperties] = None
    Singular: Optional[SingularSourceProperties] = None
    Slack: Optional[SlackSourceProperties] = None
    Trendmicro: Optional[TrendmicroSourceProperties] = None
    Veeva: Optional[VeevaSourceProperties] = None
    Zendesk: Optional[ZendeskSourceProperties] = None
    SAPOData: Optional[SAPODataSourceProperties] = None
    CustomConnector: Optional[CustomConnectorSourceProperties] = None
    Pardot: Optional[PardotSourceProperties] = None


class TriggerConfigOutput(BaseValidatorModel):
    triggerType: TriggerTypeType
    triggerProperties: Optional[TriggerPropertiesOutput] = None


class TriggerProperties(BaseValidatorModel):
    Scheduled: Optional[ScheduledTriggerProperties] = None


class ConnectorProfileCredentials(BaseValidatorModel):
    Amplitude: Optional[AmplitudeConnectorProfileCredentials] = None
    Datadog: Optional[DatadogConnectorProfileCredentials] = None
    Dynatrace: Optional[DynatraceConnectorProfileCredentials] = None
    GoogleAnalytics: Optional[GoogleAnalyticsConnectorProfileCredentials] = None
    Honeycode: Optional[HoneycodeConnectorProfileCredentials] = None
    InforNexus: Optional[InforNexusConnectorProfileCredentials] = None
    Marketo: Optional[MarketoConnectorProfileCredentials] = None
    Redshift: Optional[RedshiftConnectorProfileCredentials] = None
    Salesforce: Optional[SalesforceConnectorProfileCredentials] = None
    ServiceNow: Optional[ServiceNowConnectorProfileCredentials] = None
    Singular: Optional[SingularConnectorProfileCredentials] = None
    Slack: Optional[SlackConnectorProfileCredentials] = None
    Snowflake: Optional[SnowflakeConnectorProfileCredentials] = None
    Trendmicro: Optional[TrendmicroConnectorProfileCredentials] = None
    Veeva: Optional[VeevaConnectorProfileCredentials] = None
    Zendesk: Optional[ZendeskConnectorProfileCredentials] = None
    SAPOData: Optional[SAPODataConnectorProfileCredentials] = None
    CustomConnector: Optional[CustomConnectorProfileCredentials] = None
    Pardot: Optional[PardotConnectorProfileCredentials] = None


class ConnectorEntityField(BaseValidatorModel):
    identifier: str
    parentIdentifier: Optional[str] = None
    label: Optional[str] = None
    isPrimaryKey: Optional[bool] = None
    defaultValue: Optional[str] = None
    isDeprecated: Optional[bool] = None
    supportedFieldTypeDetails: Optional[SupportedFieldTypeDetails] = None
    description: Optional[str] = None
    sourceProperties: Optional[SourceFieldProperties] = None
    destinationProperties: Optional[DestinationFieldProperties] = None
    customProperties: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_flow_execution_records' function.
class DescribeFlowExecutionRecordsResponse(BaseValidatorModel):
    flowExecutions: List[ExecutionRecord]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectorConfiguration(BaseValidatorModel):
    canUseAsSource: Optional[bool] = None
    canUseAsDestination: Optional[bool] = None
    supportedDestinationConnectors: Optional[List[ConnectorTypeType]] = None
    supportedSchedulingFrequencies: Optional[List[ScheduleFrequencyTypeType]] = None
    isPrivateLinkEnabled: Optional[bool] = None
    isPrivateLinkEndpointUrlRequired: Optional[bool] = None
    supportedTriggerTypes: Optional[List[TriggerTypeType]] = None
    connectorMetadata: Optional[ConnectorMetadata] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    connectorDescription: Optional[str] = None
    connectorOwner: Optional[str] = None
    connectorName: Optional[str] = None
    connectorVersion: Optional[str] = None
    connectorArn: Optional[str] = None
    connectorModes: Optional[List[str]] = None
    authenticationConfig: Optional[AuthenticationConfig] = None
    connectorRuntimeSettings: Optional[List[ConnectorRuntimeSetting]] = None
    supportedApiVersions: Optional[List[str]] = None
    supportedOperators: Optional[List[OperatorsType]] = None
    supportedWriteOperations: Optional[List[WriteOperationTypeType]] = None
    connectorProvisioningType: Optional[Literal['LAMBDA']] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfig] = None
    logoURL: Optional[str] = None
    registeredAt: Optional[datetime] = None
    registeredBy: Optional[str] = None
    supportedDataTransferTypes: Optional[List[SupportedDataTransferTypeType]] = None
    supportedDataTransferApis: Optional[List[DataTransferApi]] = None

CustomConnectorProfilePropertiesUnion = Union[CustomConnectorProfileProperties, CustomConnectorProfilePropertiesOutput]


class ConnectorProfile(BaseValidatorModel):
    connectorProfileArn: Optional[str] = None
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    connectionMode: Optional[ConnectionModeType] = None
    credentialsArn: Optional[str] = None
    connectorProfileProperties: Optional[ConnectorProfilePropertiesOutput] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    privateConnectionProvisioningState: Optional[PrivateConnectionProvisioningState] = None

SAPODataConnectorProfilePropertiesUnion = Union[SAPODataConnectorProfileProperties, SAPODataConnectorProfilePropertiesOutput]


class DestinationConnectorPropertiesOutput(BaseValidatorModel):
    Redshift: Optional[RedshiftDestinationProperties] = None
    S3: Optional[S3DestinationPropertiesOutput] = None
    Salesforce: Optional[SalesforceDestinationPropertiesOutput] = None
    Snowflake: Optional[SnowflakeDestinationProperties] = None
    EventBridge: Optional[EventBridgeDestinationProperties] = None
    LookoutMetrics: Optional[Dict[str, Any]] = None
    Upsolver: Optional[UpsolverDestinationPropertiesOutput] = None
    Honeycode: Optional[HoneycodeDestinationProperties] = None
    CustomerProfiles: Optional[CustomerProfilesDestinationProperties] = None
    Zendesk: Optional[ZendeskDestinationPropertiesOutput] = None
    Marketo: Optional[MarketoDestinationProperties] = None
    CustomConnector: Optional[CustomConnectorDestinationPropertiesOutput] = None
    SAPOData: Optional[SAPODataDestinationPropertiesOutput] = None

S3OutputFormatConfigUnion = Union[S3OutputFormatConfig, S3OutputFormatConfigOutput]

UpsolverS3OutputFormatConfigUnion = Union[UpsolverS3OutputFormatConfig, UpsolverS3OutputFormatConfigOutput]


class SourceFlowConfigOutput(BaseValidatorModel):
    connectorType: ConnectorTypeType
    sourceConnectorProperties: SourceConnectorPropertiesOutput
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None
    incrementalPullConfig: Optional[IncrementalPullConfig] = None


class SourceFlowConfig(BaseValidatorModel):
    connectorType: ConnectorTypeType
    sourceConnectorProperties: SourceConnectorProperties
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None
    incrementalPullConfig: Optional[IncrementalPullConfig] = None


class TriggerConfig(BaseValidatorModel):
    triggerType: TriggerTypeType
    triggerProperties: Optional[TriggerProperties] = None


# This class is the output for the 'describe_connector_entity' function.
class DescribeConnectorEntityResponse(BaseValidatorModel):
    connectorEntityFields: List[ConnectorEntityField]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_connector' function.
class DescribeConnectorResponse(BaseValidatorModel):
    connectorConfiguration: ConnectorConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_connectors' function.
class DescribeConnectorsResponse(BaseValidatorModel):
    connectorConfigurations: Dict[ConnectorTypeType, ConnectorConfiguration]
    connectors: List[ConnectorDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_connector_profiles' function.
class DescribeConnectorProfilesResponse(BaseValidatorModel):
    connectorProfileDetails: List[ConnectorProfile]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectorProfileProperties(BaseValidatorModel):
    Amplitude: Optional[Dict[str, Any]] = None
    Datadog: Optional[DatadogConnectorProfileProperties] = None
    Dynatrace: Optional[DynatraceConnectorProfileProperties] = None
    GoogleAnalytics: Optional[Dict[str, Any]] = None
    Honeycode: Optional[Dict[str, Any]] = None
    InforNexus: Optional[InforNexusConnectorProfileProperties] = None
    Marketo: Optional[MarketoConnectorProfileProperties] = None
    Redshift: Optional[RedshiftConnectorProfileProperties] = None
    Salesforce: Optional[SalesforceConnectorProfileProperties] = None
    ServiceNow: Optional[ServiceNowConnectorProfileProperties] = None
    Singular: Optional[Dict[str, Any]] = None
    Slack: Optional[SlackConnectorProfileProperties] = None
    Snowflake: Optional[SnowflakeConnectorProfileProperties] = None
    Trendmicro: Optional[Dict[str, Any]] = None
    Veeva: Optional[VeevaConnectorProfileProperties] = None
    Zendesk: Optional[ZendeskConnectorProfileProperties] = None
    SAPOData: Optional[SAPODataConnectorProfilePropertiesUnion] = None
    CustomConnector: Optional[CustomConnectorProfilePropertiesUnion] = None
    Pardot: Optional[PardotConnectorProfileProperties] = None


class DestinationFlowConfigOutput(BaseValidatorModel):
    connectorType: ConnectorTypeType
    destinationConnectorProperties: DestinationConnectorPropertiesOutput
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None


class S3DestinationProperties(BaseValidatorModel):
    bucketName: str
    bucketPrefix: Optional[str] = None
    s3OutputFormatConfig: Optional[S3OutputFormatConfigUnion] = None


class UpsolverDestinationProperties(BaseValidatorModel):
    bucketName: str
    s3OutputFormatConfig: UpsolverS3OutputFormatConfigUnion
    bucketPrefix: Optional[str] = None

SourceFlowConfigUnion = Union[SourceFlowConfig, SourceFlowConfigOutput]

TriggerConfigUnion = Union[TriggerConfig, TriggerConfigOutput]

ConnectorProfilePropertiesUnion = Union[ConnectorProfileProperties, ConnectorProfilePropertiesOutput]


# This class is the output for the 'describe_flow' function.
class DescribeFlowResponse(BaseValidatorModel):
    flowArn: str
    description: str
    flowName: str
    kmsArn: str
    flowStatus: FlowStatusType
    flowStatusMessage: str
    sourceFlowConfig: SourceFlowConfigOutput
    destinationFlowConfigList: List[DestinationFlowConfigOutput]
    lastRunExecutionDetails: ExecutionDetails
    triggerConfig: TriggerConfigOutput
    tasks: List[TaskOutput]
    createdAt: datetime
    lastUpdatedAt: datetime
    createdBy: str
    lastUpdatedBy: str
    tags: Dict[str, str]
    metadataCatalogConfig: MetadataCatalogConfig
    lastRunMetadataCatalogDetails: List[MetadataCatalogDetail]
    schemaVersion: int
    ResponseMetadata: ResponseMetadata

S3DestinationPropertiesUnion = Union[S3DestinationProperties, S3DestinationPropertiesOutput]

UpsolverDestinationPropertiesUnion = Union[UpsolverDestinationProperties, UpsolverDestinationPropertiesOutput]


class ConnectorProfileConfig(BaseValidatorModel):
    connectorProfileProperties: ConnectorProfilePropertiesUnion
    connectorProfileCredentials: Optional[ConnectorProfileCredentials] = None


class DestinationConnectorProperties(BaseValidatorModel):
    Redshift: Optional[RedshiftDestinationProperties] = None
    S3: Optional[S3DestinationPropertiesUnion] = None
    Salesforce: Optional[SalesforceDestinationPropertiesUnion] = None
    Snowflake: Optional[SnowflakeDestinationProperties] = None
    EventBridge: Optional[EventBridgeDestinationProperties] = None
    LookoutMetrics: Optional[Dict[str, Any]] = None
    Upsolver: Optional[UpsolverDestinationPropertiesUnion] = None
    Honeycode: Optional[HoneycodeDestinationProperties] = None
    CustomerProfiles: Optional[CustomerProfilesDestinationProperties] = None
    Zendesk: Optional[ZendeskDestinationPropertiesUnion] = None
    Marketo: Optional[MarketoDestinationProperties] = None
    CustomConnector: Optional[CustomConnectorDestinationPropertiesUnion] = None
    SAPOData: Optional[SAPODataDestinationPropertiesUnion] = None


# This class is the input for the 'create_connector_profile' function.
class CreateConnectorProfileRequest(BaseValidatorModel):
    connectorProfileName: str
    connectorType: ConnectorTypeType
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfig
    kmsArn: Optional[str] = None
    connectorLabel: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_connector_profile' function.
class UpdateConnectorProfileRequest(BaseValidatorModel):
    connectorProfileName: str
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfig
    clientToken: Optional[str] = None

DestinationConnectorPropertiesUnion = Union[DestinationConnectorProperties, DestinationConnectorPropertiesOutput]


class DestinationFlowConfig(BaseValidatorModel):
    connectorType: ConnectorTypeType
    destinationConnectorProperties: DestinationConnectorPropertiesUnion
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None

DestinationFlowConfigUnion = Union[DestinationFlowConfig, DestinationFlowConfigOutput]


# This class is the input for the 'create_flow' function.
class CreateFlowRequest(BaseValidatorModel):
    flowName: str
    triggerConfig: TriggerConfigUnion
    sourceFlowConfig: SourceFlowConfigUnion
    destinationFlowConfigList: List[DestinationFlowConfigUnion]
    tasks: List[TaskUnion]
    description: Optional[str] = None
    kmsArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    metadataCatalogConfig: Optional[MetadataCatalogConfig] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_flow' function.
class UpdateFlowRequest(BaseValidatorModel):
    flowName: str
    triggerConfig: TriggerConfigUnion
    sourceFlowConfig: SourceFlowConfigUnion
    destinationFlowConfigList: List[DestinationFlowConfigUnion]
    tasks: List[TaskUnion]
    description: Optional[str] = None
    metadataCatalogConfig: Optional[MetadataCatalogConfig] = None
    clientToken: Optional[str] = None