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
from aws_resource_validator.pydantic_models.appflow_constants import *

class AggregationConfigTypeDef(BaseModel):
    aggregationType: Optional[AggregationTypeType] = None
    targetFileSize: Optional[int] = None

class AmplitudeConnectorProfileCredentialsTypeDef(BaseModel):
    apiKey: str
    secretKey: str

class AmplitudeSourcePropertiesTypeDef(BaseModel):
    object: str

class ApiKeyCredentialsTypeDef(BaseModel):
    apiKey: str
    apiSecretKey: Optional[str] = None

class AuthParameterTypeDef(BaseModel):
    key: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    isSensitiveField: Optional[bool] = None
    connectorSuppliedValues: Optional[List[str]] = None

class BasicAuthCredentialsTypeDef(BaseModel):
    username: str
    password: str

class CancelFlowExecutionsRequestRequestTypeDef(BaseModel):
    flowName: str
    executionIds: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ConnectorRuntimeSettingTypeDef(BaseModel):
    key: Optional[str] = None
    dataType: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    scope: Optional[str] = None
    connectorSuppliedValueOptions: Optional[List[str]] = None

class DataTransferApiTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional[DataTransferApiTypeType] = None

class ConnectorDetailTypeDef(BaseModel):
    connectorDescription: Optional[str] = None
    connectorName: Optional[str] = None
    connectorOwner: Optional[str] = None
    connectorVersion: Optional[str] = None
    applicationType: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    registeredAt: Optional[datetime] = None
    registeredBy: Optional[str] = None
    connectorProvisioningType: Optional[Literal["LAMBDA"]] = None
    connectorModes: Optional[List[str]] = None
    supportedDataTransferTypes: Optional[List[SupportedDataTransferTypeType]] = None

class DestinationFieldPropertiesTypeDef(BaseModel):
    isCreatable: Optional[bool] = None
    isNullable: Optional[bool] = None
    isUpsertable: Optional[bool] = None
    isUpdatable: Optional[bool] = None
    isDefaultedOnCreate: Optional[bool] = None
    supportedWriteOperations: Optional[List[WriteOperationTypeType]] = None

class SourceFieldPropertiesTypeDef(BaseModel):
    isRetrievable: Optional[bool] = None
    isQueryable: Optional[bool] = None
    isTimestampFieldForIncrementalQueries: Optional[bool] = None

class ConnectorEntityTypeDef(BaseModel):
    name: str
    label: Optional[str] = None
    hasNestedEntities: Optional[bool] = None

class GoogleAnalyticsMetadataTypeDef(BaseModel):
    oAuthScopes: Optional[List[str]] = None

class HoneycodeMetadataTypeDef(BaseModel):
    oAuthScopes: Optional[List[str]] = None

class SalesforceMetadataTypeDef(BaseModel):
    oAuthScopes: Optional[List[str]] = None
    dataTransferApis: Optional[List[SalesforceDataTransferApiType]] = None
    oauth2GrantTypesSupported: Optional[List[OAuth2GrantTypeType]] = None

class SlackMetadataTypeDef(BaseModel):
    oAuthScopes: Optional[List[str]] = None

class SnowflakeMetadataTypeDef(BaseModel):
    supportedRegions: Optional[List[str]] = None

class ZendeskMetadataTypeDef(BaseModel):
    oAuthScopes: Optional[List[str]] = None

class ConnectorOAuthRequestTypeDef(BaseModel):
    authCode: Optional[str] = None
    redirectUri: Optional[str] = None

class ConnectorOperatorTypeDef(BaseModel):
    Amplitude: Optional[Literal["BETWEEN"]] = None
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

class DatadogConnectorProfileCredentialsTypeDef(BaseModel):
    apiKey: str
    applicationKey: str

class DynatraceConnectorProfileCredentialsTypeDef(BaseModel):
    apiToken: str

class InforNexusConnectorProfileCredentialsTypeDef(BaseModel):
    accessKeyId: str
    userId: str
    secretAccessKey: str
    datakey: str

class RedshiftConnectorProfileCredentialsTypeDef(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

class SingularConnectorProfileCredentialsTypeDef(BaseModel):
    apiKey: str

class SnowflakeConnectorProfileCredentialsTypeDef(BaseModel):
    username: str
    password: str

class TrendmicroConnectorProfileCredentialsTypeDef(BaseModel):
    apiSecretKey: str

class VeevaConnectorProfileCredentialsTypeDef(BaseModel):
    username: str
    password: str

class DatadogConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class DynatraceConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class InforNexusConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class MarketoConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class PardotConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: Optional[str] = None
    isSandboxEnvironment: Optional[bool] = None
    businessUnitId: Optional[str] = None

class RedshiftConnectorProfilePropertiesTypeDef(BaseModel):
    bucketName: str
    roleArn: str
    databaseUrl: Optional[str] = None
    bucketPrefix: Optional[str] = None
    dataApiRoleArn: Optional[str] = None
    isRedshiftServerless: Optional[bool] = None
    clusterIdentifier: Optional[str] = None
    workgroupName: Optional[str] = None
    databaseName: Optional[str] = None

class SalesforceConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: Optional[str] = None
    isSandboxEnvironment: Optional[bool] = None
    usePrivateLinkForMetadataAndAuthorization: Optional[bool] = None

class ServiceNowConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class SlackConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class SnowflakeConnectorProfilePropertiesTypeDef(BaseModel):
    warehouse: str
    stage: str
    bucketName: str
    bucketPrefix: Optional[str] = None
    privateLinkServiceName: Optional[str] = None
    accountName: Optional[str] = None
    region: Optional[str] = None

class VeevaConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class ZendeskConnectorProfilePropertiesTypeDef(BaseModel):
    instanceUrl: str

class PrivateConnectionProvisioningStateTypeDef(BaseModel):
    status: Optional[PrivateConnectionProvisioningStatusType] = None
    failureMessage: Optional[str] = None
    failureCause: Optional[PrivateConnectionProvisioningFailureCauseType] = None

class LambdaConnectorProvisioningConfigTypeDef(BaseModel):
    lambdaArn: str

class CustomAuthCredentialsTypeDef(BaseModel):
    customAuthenticationType: str
    credentialsMap: Optional[Mapping[str, str]] = None

class ErrorHandlingConfigTypeDef(BaseModel):
    failOnFirstDestinationError: Optional[bool] = None
    bucketPrefix: Optional[str] = None
    bucketName: Optional[str] = None

class OAuth2PropertiesTypeDef(BaseModel):
    tokenUrl: str
    oAuth2GrantType: OAuth2GrantTypeType
    tokenUrlCustomProperties: Optional[Mapping[str, str]] = None

class CustomerProfilesDestinationPropertiesTypeDef(BaseModel):
    domainName: str
    objectTypeName: Optional[str] = None

class DatadogSourcePropertiesTypeDef(BaseModel):
    object: str

class DeleteConnectorProfileRequestRequestTypeDef(BaseModel):
    connectorProfileName: str
    forceDelete: Optional[bool] = None

class DeleteFlowRequestRequestTypeDef(BaseModel):
    flowName: str
    forceDelete: Optional[bool] = None

class DescribeConnectorEntityRequestRequestTypeDef(BaseModel):
    connectorEntityName: str
    connectorType: Optional[ConnectorTypeType] = None
    connectorProfileName: Optional[str] = None
    apiVersion: Optional[str] = None

class DescribeConnectorProfilesRequestRequestTypeDef(BaseModel):
    connectorProfileNames: Optional[Sequence[str]] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeConnectorRequestRequestTypeDef(BaseModel):
    connectorType: ConnectorTypeType
    connectorLabel: Optional[str] = None

class DescribeConnectorsRequestRequestTypeDef(BaseModel):
    connectorTypes: Optional[Sequence[ConnectorTypeType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeFlowExecutionRecordsRequestRequestTypeDef(BaseModel):
    flowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeFlowRequestRequestTypeDef(BaseModel):
    flowName: str

class ExecutionDetailsTypeDef(BaseModel):
    mostRecentExecutionMessage: Optional[str] = None
    mostRecentExecutionTime: Optional[datetime] = None
    mostRecentExecutionStatus: Optional[ExecutionStatusType] = None

class DynatraceSourcePropertiesTypeDef(BaseModel):
    object: str

class ErrorInfoTypeDef(BaseModel):
    putFailuresCount: Optional[int] = None
    executionMessage: Optional[str] = None

class RangeTypeDef(BaseModel):
    maximum: Optional[float] = None
    minimum: Optional[float] = None

class GlueDataCatalogConfigTypeDef(BaseModel):
    roleArn: str
    databaseName: str
    tablePrefix: str

class GoogleAnalyticsSourcePropertiesTypeDef(BaseModel):
    object: str

class IncrementalPullConfigTypeDef(BaseModel):
    datetimeTypeFieldName: Optional[str] = None

class InforNexusSourcePropertiesTypeDef(BaseModel):
    object: str

class ListConnectorEntitiesRequestRequestTypeDef(BaseModel):
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    entitiesPath: Optional[str] = None
    apiVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MarketoSourcePropertiesTypeDef(BaseModel):
    object: str

class RegistrationOutputTypeDef(BaseModel):
    message: Optional[str] = None
    result: Optional[str] = None
    status: Optional[ExecutionStatusType] = None

class OAuth2CustomParameterTypeDef(BaseModel):
    key: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    isSensitiveField: Optional[bool] = None
    connectorSuppliedValues: Optional[List[str]] = None
    type: Optional[OAuth2CustomPropTypeType] = None

class OAuthPropertiesTypeDef(BaseModel):
    tokenUrl: str
    authCodeUrl: str
    oAuthScopes: Sequence[str]

class PardotSourcePropertiesTypeDef(BaseModel):
    object: str

class PrefixConfigTypeDef(BaseModel):
    prefixType: Optional[PrefixTypeType] = None
    prefixFormat: Optional[PrefixFormatType] = None
    pathPrefixHierarchy: Optional[Sequence[PathPrefixType]] = None

class ResetConnectorMetadataCacheRequestRequestTypeDef(BaseModel):
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorEntityName: Optional[str] = None
    entitiesPath: Optional[str] = None
    apiVersion: Optional[str] = None

class S3InputFormatConfigTypeDef(BaseModel):
    s3InputFileType: Optional[S3InputFileTypeType] = None

class SuccessResponseHandlingConfigTypeDef(BaseModel):
    bucketPrefix: Optional[str] = None
    bucketName: Optional[str] = None

class SAPODataPaginationConfigTypeDef(BaseModel):
    maxPageSize: int

class SAPODataParallelismConfigTypeDef(BaseModel):
    maxParallelism: int

class SalesforceSourcePropertiesTypeDef(BaseModel):
    object: str
    enableDynamicFieldUpdate: Optional[bool] = None
    includeDeletedRecords: Optional[bool] = None
    dataTransferApi: Optional[SalesforceDataTransferApiType] = None

class ServiceNowSourcePropertiesTypeDef(BaseModel):
    object: str

class SingularSourcePropertiesTypeDef(BaseModel):
    object: str

class SlackSourcePropertiesTypeDef(BaseModel):
    object: str

class TrendmicroSourcePropertiesTypeDef(BaseModel):
    object: str

class VeevaSourcePropertiesTypeDef(BaseModel):
    object: str
    documentType: Optional[str] = None
    includeSourceFiles: Optional[bool] = None
    includeRenditions: Optional[bool] = None
    includeAllVersions: Optional[bool] = None

class ZendeskSourcePropertiesTypeDef(BaseModel):
    object: str

class StartFlowRequestRequestTypeDef(BaseModel):
    flowName: str
    clientToken: Optional[str] = None

class StopFlowRequestRequestTypeDef(BaseModel):
    flowName: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UnregisterConnectorRequestRequestTypeDef(BaseModel):
    connectorLabel: str
    forceDelete: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CustomAuthConfigTypeDef(BaseModel):
    customAuthenticationType: Optional[str] = None
    authParameters: Optional[List[AuthParameterTypeDef]] = None

class CancelFlowExecutionsResponseTypeDef(BaseModel):
    invalidExecutions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorProfileResponseTypeDef(BaseModel):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowResponseTypeDef(BaseModel):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterConnectorResponseTypeDef(BaseModel):
    connectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlowResponseTypeDef(BaseModel):
    flowArn: str
    flowStatus: FlowStatusType
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopFlowResponseTypeDef(BaseModel):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorProfileResponseTypeDef(BaseModel):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorRegistrationResponseTypeDef(BaseModel):
    connectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowResponseTypeDef(BaseModel):
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CustomConnectorSourcePropertiesTypeDef(BaseModel):
    entityName: str
    customProperties: Optional[Mapping[str, str]] = None
    dataTransferApi: Optional[DataTransferApiTypeDef] = None

class ListConnectorsResponseTypeDef(BaseModel):
    connectors: List[ConnectorDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorEntitiesResponseTypeDef(BaseModel):
    connectorEntityMap: Dict[str, List[ConnectorEntityTypeDef]]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorMetadataTypeDef(BaseModel):
    Amplitude: Optional[Dict[str, Any]] = None
    Datadog: Optional[Dict[str, Any]] = None
    Dynatrace: Optional[Dict[str, Any]] = None
    GoogleAnalytics: Optional[GoogleAnalyticsMetadataTypeDef] = None
    InforNexus: Optional[Dict[str, Any]] = None
    Marketo: Optional[Dict[str, Any]] = None
    Redshift: Optional[Dict[str, Any]] = None
    S3: Optional[Dict[str, Any]] = None
    Salesforce: Optional[SalesforceMetadataTypeDef] = None
    ServiceNow: Optional[Dict[str, Any]] = None
    Singular: Optional[Dict[str, Any]] = None
    Slack: Optional[SlackMetadataTypeDef] = None
    Snowflake: Optional[SnowflakeMetadataTypeDef] = None
    Trendmicro: Optional[Dict[str, Any]] = None
    Veeva: Optional[Dict[str, Any]] = None
    Zendesk: Optional[ZendeskMetadataTypeDef] = None
    EventBridge: Optional[Dict[str, Any]] = None
    Upsolver: Optional[Dict[str, Any]] = None
    CustomerProfiles: Optional[Dict[str, Any]] = None
    Honeycode: Optional[HoneycodeMetadataTypeDef] = None
    SAPOData: Optional[Dict[str, Any]] = None
    Pardot: Optional[Dict[str, Any]] = None

class GoogleAnalyticsConnectorProfileCredentialsTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class HoneycodeConnectorProfileCredentialsTypeDef(BaseModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class MarketoConnectorProfileCredentialsTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class OAuth2CredentialsTypeDef(BaseModel):
    clientId: Optional[str] = None
    clientSecret: Optional[str] = None
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class OAuthCredentialsTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class PardotConnectorProfileCredentialsTypeDef(BaseModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None
    clientCredentialsArn: Optional[str] = None

class SalesforceConnectorProfileCredentialsTypeDef(BaseModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None
    clientCredentialsArn: Optional[str] = None
    oAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    jwtToken: Optional[str] = None

class SlackConnectorProfileCredentialsTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class ZendeskConnectorProfileCredentialsTypeDef(BaseModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class TaskTypeDef(BaseModel):
    sourceFields: Sequence[str]
    taskType: TaskTypeType
    connectorOperator: Optional[ConnectorOperatorTypeDef] = None
    destinationField: Optional[str] = None
    taskProperties: Optional[Mapping[OperatorPropertiesKeysType, str]] = None

class ConnectorProvisioningConfigTypeDef(BaseModel):
    lambda: Optional[LambdaConnectorProvisioningConfigTypeDef] = None

class CustomConnectorDestinationPropertiesTypeDef(BaseModel):
    entityName: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    idFieldNames: Optional[Sequence[str]] = None
    customProperties: Optional[Mapping[str, str]] = None

class EventBridgeDestinationPropertiesTypeDef(BaseModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class HoneycodeDestinationPropertiesTypeDef(BaseModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class MarketoDestinationPropertiesTypeDef(BaseModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class RedshiftDestinationPropertiesTypeDef(BaseModel):
    object: str
    intermediateBucketName: str
    bucketPrefix: Optional[str] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class SalesforceDestinationPropertiesTypeDef(BaseModel):
    object: str
    idFieldNames: Optional[Sequence[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    dataTransferApi: Optional[SalesforceDataTransferApiType] = None

class SnowflakeDestinationPropertiesTypeDef(BaseModel):
    object: str
    intermediateBucketName: str
    bucketPrefix: Optional[str] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class ZendeskDestinationPropertiesTypeDef(BaseModel):
    object: str
    idFieldNames: Optional[Sequence[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None

class CustomConnectorProfilePropertiesTypeDef(BaseModel):
    profileProperties: Optional[Mapping[str, str]] = None
    oAuth2Properties: Optional[OAuth2PropertiesTypeDef] = None

class FlowDefinitionTypeDef(BaseModel):
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
    lastRunExecutionDetails: Optional[ExecutionDetailsTypeDef] = None

class ExecutionResultTypeDef(BaseModel):
    errorInfo: Optional[ErrorInfoTypeDef] = None
    bytesProcessed: Optional[int] = None
    bytesWritten: Optional[int] = None
    recordsProcessed: Optional[int] = None
    numParallelProcesses: Optional[int] = None
    maxPageSize: Optional[int] = None

class FieldTypeDetailsTypeDef(BaseModel):
    fieldType: str
    filterOperators: List[OperatorType]
    supportedValues: Optional[List[str]] = None
    valueRegexPattern: Optional[str] = None
    supportedDateFormat: Optional[str] = None
    fieldValueRange: Optional[RangeTypeDef] = None
    fieldLengthRange: Optional[RangeTypeDef] = None

class MetadataCatalogConfigTypeDef(BaseModel):
    glueDataCatalog: Optional[GlueDataCatalogConfigTypeDef] = None

class MetadataCatalogDetailTypeDef(BaseModel):
    catalogType: Optional[Literal["GLUE"]] = None
    tableName: Optional[str] = None
    tableRegistrationOutput: Optional[RegistrationOutputTypeDef] = None
    partitionRegistrationOutput: Optional[RegistrationOutputTypeDef] = None

class OAuth2DefaultsTypeDef(BaseModel):
    oauthScopes: Optional[List[str]] = None
    tokenUrls: Optional[List[str]] = None
    authCodeUrls: Optional[List[str]] = None
    oauth2GrantTypesSupported: Optional[List[OAuth2GrantTypeType]] = None
    oauth2CustomProperties: Optional[List[OAuth2CustomParameterTypeDef]] = None

class SAPODataConnectorProfilePropertiesTypeDef(BaseModel):
    applicationHostUrl: str
    applicationServicePath: str
    portNumber: int
    clientNumber: str
    logonLanguage: Optional[str] = None
    privateLinkServiceName: Optional[str] = None
    oAuthProperties: Optional[OAuthPropertiesTypeDef] = None
    disableSSO: Optional[bool] = None

class S3OutputFormatConfigTypeDef(BaseModel):
    fileType: Optional[FileTypeType] = None
    prefixConfig: Optional[PrefixConfigTypeDef] = None
    aggregationConfig: Optional[AggregationConfigTypeDef] = None
    preserveSourceDataTyping: Optional[bool] = None

class UpsolverS3OutputFormatConfigTypeDef(BaseModel):
    prefixConfig: PrefixConfigTypeDef
    fileType: Optional[FileTypeType] = None
    aggregationConfig: Optional[AggregationConfigTypeDef] = None

class S3SourcePropertiesTypeDef(BaseModel):
    bucketName: str
    bucketPrefix: Optional[str] = None
    s3InputFormatConfig: Optional[S3InputFormatConfigTypeDef] = None

class SAPODataDestinationPropertiesTypeDef(BaseModel):
    objectPath: str
    successResponseHandlingConfig: Optional[SuccessResponseHandlingConfigTypeDef] = None
    idFieldNames: Optional[Sequence[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None

class SAPODataSourcePropertiesTypeDef(BaseModel):
    objectPath: Optional[str] = None
    parallelismConfig: Optional[SAPODataParallelismConfigTypeDef] = None
    paginationConfig: Optional[SAPODataPaginationConfigTypeDef] = None

class ScheduledTriggerPropertiesTypeDef(BaseModel):
    scheduleExpression: str
    dataPullMode: Optional[DataPullModeType] = None
    scheduleStartTime: Optional[TimestampTypeDef] = None
    scheduleEndTime: Optional[TimestampTypeDef] = None
    timezone: Optional[str] = None
    scheduleOffset: Optional[int] = None
    firstExecutionFrom: Optional[TimestampTypeDef] = None
    flowErrorDeactivationThreshold: Optional[int] = None

class CustomConnectorProfileCredentialsTypeDef(BaseModel):
    authenticationType: AuthenticationTypeType
    basic: Optional[BasicAuthCredentialsTypeDef] = None
    oauth2: Optional[OAuth2CredentialsTypeDef] = None
    apiKey: Optional[ApiKeyCredentialsTypeDef] = None
    custom: Optional[CustomAuthCredentialsTypeDef] = None

class ServiceNowConnectorProfileCredentialsTypeDef(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    oAuth2Credentials: Optional[OAuth2CredentialsTypeDef] = None

class SAPODataConnectorProfileCredentialsTypeDef(BaseModel):
    basicAuthCredentials: Optional[BasicAuthCredentialsTypeDef] = None
    oAuthCredentials: Optional[OAuthCredentialsTypeDef] = None

class RegisterConnectorRequestRequestTypeDef(BaseModel):
    connectorLabel: Optional[str] = None
    description: Optional[str] = None
    connectorProvisioningType: Optional[Literal["LAMBDA"]] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfigTypeDef] = None
    clientToken: Optional[str] = None

class UpdateConnectorRegistrationRequestRequestTypeDef(BaseModel):
    connectorLabel: str
    description: Optional[str] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfigTypeDef] = None
    clientToken: Optional[str] = None

class ListFlowsResponseTypeDef(BaseModel):
    flows: List[FlowDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SupportedFieldTypeDetailsTypeDef(BaseModel):
    v1: FieldTypeDetailsTypeDef

class ExecutionRecordTypeDef(BaseModel):
    executionId: Optional[str] = None
    executionStatus: Optional[ExecutionStatusType] = None
    executionResult: Optional[ExecutionResultTypeDef] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    dataPullStartTime: Optional[datetime] = None
    dataPullEndTime: Optional[datetime] = None
    metadataCatalogDetails: Optional[List[MetadataCatalogDetailTypeDef]] = None

class AuthenticationConfigTypeDef(BaseModel):
    isBasicAuthSupported: Optional[bool] = None
    isApiKeyAuthSupported: Optional[bool] = None
    isOAuth2Supported: Optional[bool] = None
    isCustomAuthSupported: Optional[bool] = None
    oAuth2Defaults: Optional[OAuth2DefaultsTypeDef] = None
    customAuthConfigs: Optional[List[CustomAuthConfigTypeDef]] = None

class ConnectorProfilePropertiesTypeDef(BaseModel):
    Amplitude: Optional[Mapping[str, Any]] = None
    Datadog: Optional[DatadogConnectorProfilePropertiesTypeDef] = None
    Dynatrace: Optional[DynatraceConnectorProfilePropertiesTypeDef] = None
    GoogleAnalytics: Optional[Mapping[str, Any]] = None
    Honeycode: Optional[Mapping[str, Any]] = None
    InforNexus: Optional[InforNexusConnectorProfilePropertiesTypeDef] = None
    Marketo: Optional[MarketoConnectorProfilePropertiesTypeDef] = None
    Redshift: Optional[RedshiftConnectorProfilePropertiesTypeDef] = None
    Salesforce: Optional[SalesforceConnectorProfilePropertiesTypeDef] = None
    ServiceNow: Optional[ServiceNowConnectorProfilePropertiesTypeDef] = None
    Singular: Optional[Mapping[str, Any]] = None
    Slack: Optional[SlackConnectorProfilePropertiesTypeDef] = None
    Snowflake: Optional[SnowflakeConnectorProfilePropertiesTypeDef] = None
    Trendmicro: Optional[Mapping[str, Any]] = None
    Veeva: Optional[VeevaConnectorProfilePropertiesTypeDef] = None
    Zendesk: Optional[ZendeskConnectorProfilePropertiesTypeDef] = None
    SAPOData: Optional[SAPODataConnectorProfilePropertiesTypeDef] = None
    CustomConnector: Optional[CustomConnectorProfilePropertiesTypeDef] = None
    Pardot: Optional[PardotConnectorProfilePropertiesTypeDef] = None

class S3DestinationPropertiesTypeDef(BaseModel):
    bucketName: str
    bucketPrefix: Optional[str] = None
    s3OutputFormatConfig: Optional[S3OutputFormatConfigTypeDef] = None

class UpsolverDestinationPropertiesTypeDef(BaseModel):
    bucketName: str
    s3OutputFormatConfig: UpsolverS3OutputFormatConfigTypeDef
    bucketPrefix: Optional[str] = None

class SourceConnectorPropertiesTypeDef(BaseModel):
    Amplitude: Optional[AmplitudeSourcePropertiesTypeDef] = None
    Datadog: Optional[DatadogSourcePropertiesTypeDef] = None
    Dynatrace: Optional[DynatraceSourcePropertiesTypeDef] = None
    GoogleAnalytics: Optional[GoogleAnalyticsSourcePropertiesTypeDef] = None
    InforNexus: Optional[InforNexusSourcePropertiesTypeDef] = None
    Marketo: Optional[MarketoSourcePropertiesTypeDef] = None
    S3: Optional[S3SourcePropertiesTypeDef] = None
    Salesforce: Optional[SalesforceSourcePropertiesTypeDef] = None
    ServiceNow: Optional[ServiceNowSourcePropertiesTypeDef] = None
    Singular: Optional[SingularSourcePropertiesTypeDef] = None
    Slack: Optional[SlackSourcePropertiesTypeDef] = None
    Trendmicro: Optional[TrendmicroSourcePropertiesTypeDef] = None
    Veeva: Optional[VeevaSourcePropertiesTypeDef] = None
    Zendesk: Optional[ZendeskSourcePropertiesTypeDef] = None
    SAPOData: Optional[SAPODataSourcePropertiesTypeDef] = None
    CustomConnector: Optional[CustomConnectorSourcePropertiesTypeDef] = None
    Pardot: Optional[PardotSourcePropertiesTypeDef] = None

class TriggerPropertiesTypeDef(BaseModel):
    Scheduled: Optional[ScheduledTriggerPropertiesTypeDef] = None

class ConnectorProfileCredentialsTypeDef(BaseModel):
    Amplitude: Optional[AmplitudeConnectorProfileCredentialsTypeDef] = None
    Datadog: Optional[DatadogConnectorProfileCredentialsTypeDef] = None
    Dynatrace: Optional[DynatraceConnectorProfileCredentialsTypeDef] = None
    GoogleAnalytics: Optional[GoogleAnalyticsConnectorProfileCredentialsTypeDef] = None
    Honeycode: Optional[HoneycodeConnectorProfileCredentialsTypeDef] = None
    InforNexus: Optional[InforNexusConnectorProfileCredentialsTypeDef] = None
    Marketo: Optional[MarketoConnectorProfileCredentialsTypeDef] = None
    Redshift: Optional[RedshiftConnectorProfileCredentialsTypeDef] = None
    Salesforce: Optional[SalesforceConnectorProfileCredentialsTypeDef] = None
    ServiceNow: Optional[ServiceNowConnectorProfileCredentialsTypeDef] = None
    Singular: Optional[SingularConnectorProfileCredentialsTypeDef] = None
    Slack: Optional[SlackConnectorProfileCredentialsTypeDef] = None
    Snowflake: Optional[SnowflakeConnectorProfileCredentialsTypeDef] = None
    Trendmicro: Optional[TrendmicroConnectorProfileCredentialsTypeDef] = None
    Veeva: Optional[VeevaConnectorProfileCredentialsTypeDef] = None
    Zendesk: Optional[ZendeskConnectorProfileCredentialsTypeDef] = None
    SAPOData: Optional[SAPODataConnectorProfileCredentialsTypeDef] = None
    CustomConnector: Optional[CustomConnectorProfileCredentialsTypeDef] = None
    Pardot: Optional[PardotConnectorProfileCredentialsTypeDef] = None

class ConnectorEntityFieldTypeDef(BaseModel):
    identifier: str
    parentIdentifier: Optional[str] = None
    label: Optional[str] = None
    isPrimaryKey: Optional[bool] = None
    defaultValue: Optional[str] = None
    isDeprecated: Optional[bool] = None
    supportedFieldTypeDetails: Optional[SupportedFieldTypeDetailsTypeDef] = None
    description: Optional[str] = None
    sourceProperties: Optional[SourceFieldPropertiesTypeDef] = None
    destinationProperties: Optional[DestinationFieldPropertiesTypeDef] = None
    customProperties: Optional[Dict[str, str]] = None

class DescribeFlowExecutionRecordsResponseTypeDef(BaseModel):
    flowExecutions: List[ExecutionRecordTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorConfigurationTypeDef(BaseModel):
    canUseAsSource: Optional[bool] = None
    canUseAsDestination: Optional[bool] = None
    supportedDestinationConnectors: Optional[List[ConnectorTypeType]] = None
    supportedSchedulingFrequencies: Optional[List[ScheduleFrequencyTypeType]] = None
    isPrivateLinkEnabled: Optional[bool] = None
    isPrivateLinkEndpointUrlRequired: Optional[bool] = None
    supportedTriggerTypes: Optional[List[TriggerTypeType]] = None
    connectorMetadata: Optional[ConnectorMetadataTypeDef] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    connectorDescription: Optional[str] = None
    connectorOwner: Optional[str] = None
    connectorName: Optional[str] = None
    connectorVersion: Optional[str] = None
    connectorArn: Optional[str] = None
    connectorModes: Optional[List[str]] = None
    authenticationConfig: Optional[AuthenticationConfigTypeDef] = None
    connectorRuntimeSettings: Optional[List[ConnectorRuntimeSettingTypeDef]] = None
    supportedApiVersions: Optional[List[str]] = None
    supportedOperators: Optional[List[OperatorsType]] = None
    supportedWriteOperations: Optional[List[WriteOperationTypeType]] = None
    connectorProvisioningType: Optional[Literal["LAMBDA"]] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfigTypeDef] = None
    logoURL: Optional[str] = None
    registeredAt: Optional[datetime] = None
    registeredBy: Optional[str] = None
    supportedDataTransferTypes: Optional[List[SupportedDataTransferTypeType]] = None
    supportedDataTransferApis: Optional[List[DataTransferApiTypeDef]] = None

class ConnectorProfileTypeDef(BaseModel):
    connectorProfileArn: Optional[str] = None
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    connectionMode: Optional[ConnectionModeType] = None
    credentialsArn: Optional[str] = None
    connectorProfileProperties: Optional[ConnectorProfilePropertiesTypeDef] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    privateConnectionProvisioningState: Optional[       PrivateConnectionProvisioningStateTypeDef     ] = None

class DestinationConnectorPropertiesTypeDef(BaseModel):
    Redshift: Optional[RedshiftDestinationPropertiesTypeDef] = None
    S3: Optional[S3DestinationPropertiesTypeDef] = None
    Salesforce: Optional[SalesforceDestinationPropertiesTypeDef] = None
    Snowflake: Optional[SnowflakeDestinationPropertiesTypeDef] = None
    EventBridge: Optional[EventBridgeDestinationPropertiesTypeDef] = None
    LookoutMetrics: Optional[Mapping[str, Any]] = None
    Upsolver: Optional[UpsolverDestinationPropertiesTypeDef] = None
    Honeycode: Optional[HoneycodeDestinationPropertiesTypeDef] = None
    CustomerProfiles: Optional[CustomerProfilesDestinationPropertiesTypeDef] = None
    Zendesk: Optional[ZendeskDestinationPropertiesTypeDef] = None
    Marketo: Optional[MarketoDestinationPropertiesTypeDef] = None
    CustomConnector: Optional[CustomConnectorDestinationPropertiesTypeDef] = None
    SAPOData: Optional[SAPODataDestinationPropertiesTypeDef] = None

class SourceFlowConfigTypeDef(BaseModel):
    connectorType: ConnectorTypeType
    sourceConnectorProperties: SourceConnectorPropertiesTypeDef
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None
    incrementalPullConfig: Optional[IncrementalPullConfigTypeDef] = None

class TriggerConfigTypeDef(BaseModel):
    triggerType: TriggerTypeType
    triggerProperties: Optional[TriggerPropertiesTypeDef] = None

class ConnectorProfileConfigTypeDef(BaseModel):
    connectorProfileProperties: ConnectorProfilePropertiesTypeDef
    connectorProfileCredentials: Optional[ConnectorProfileCredentialsTypeDef] = None

class DescribeConnectorEntityResponseTypeDef(BaseModel):
    connectorEntityFields: List[ConnectorEntityFieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorResponseTypeDef(BaseModel):
    connectorConfiguration: ConnectorConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorsResponseTypeDef(BaseModel):
    connectorConfigurations: Dict[ConnectorTypeType, ConnectorConfigurationTypeDef]
    connectors: List[ConnectorDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorProfilesResponseTypeDef(BaseModel):
    connectorProfileDetails: List[ConnectorProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationFlowConfigTypeDef(BaseModel):
    connectorType: ConnectorTypeType
    destinationConnectorProperties: DestinationConnectorPropertiesTypeDef
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None

class CreateConnectorProfileRequestRequestTypeDef(BaseModel):
    connectorProfileName: str
    connectorType: ConnectorTypeType
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfigTypeDef
    kmsArn: Optional[str] = None
    connectorLabel: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateConnectorProfileRequestRequestTypeDef(BaseModel):
    connectorProfileName: str
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfigTypeDef
    clientToken: Optional[str] = None

class CreateFlowRequestRequestTypeDef(BaseModel):
    flowName: str
    triggerConfig: TriggerConfigTypeDef
    sourceFlowConfig: SourceFlowConfigTypeDef
    destinationFlowConfigList: Sequence[DestinationFlowConfigTypeDef]
    tasks: Sequence[TaskTypeDef]
    description: Optional[str] = None
    kmsArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    metadataCatalogConfig: Optional[MetadataCatalogConfigTypeDef] = None
    clientToken: Optional[str] = None

class DescribeFlowResponseTypeDef(BaseModel):
    flowArn: str
    description: str
    flowName: str
    kmsArn: str
    flowStatus: FlowStatusType
    flowStatusMessage: str
    sourceFlowConfig: SourceFlowConfigTypeDef
    destinationFlowConfigList: List[DestinationFlowConfigTypeDef]
    lastRunExecutionDetails: ExecutionDetailsTypeDef
    triggerConfig: TriggerConfigTypeDef
    tasks: List[TaskTypeDef]
    createdAt: datetime
    lastUpdatedAt: datetime
    createdBy: str
    lastUpdatedBy: str
    tags: Dict[str, str]
    metadataCatalogConfig: MetadataCatalogConfigTypeDef
    lastRunMetadataCatalogDetails: List[MetadataCatalogDetailTypeDef]
    schemaVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowRequestRequestTypeDef(BaseModel):
    flowName: str
    triggerConfig: TriggerConfigTypeDef
    sourceFlowConfig: SourceFlowConfigTypeDef
    destinationFlowConfigList: Sequence[DestinationFlowConfigTypeDef]
    tasks: Sequence[TaskTypeDef]
    description: Optional[str] = None
    metadataCatalogConfig: Optional[MetadataCatalogConfigTypeDef] = None
    clientToken: Optional[str] = None

