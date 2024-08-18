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
from aws_resource_validator.pydantic_models.appflow_constants import *

class AggregationConfigTypeDef(BaseValidatorModel):
    aggregationType: Optional[AggregationTypeType] = None
    targetFileSize: Optional[int] = None

class AmplitudeConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    apiKey: str
    secretKey: str

class AmplitudeSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class ApiKeyCredentialsTypeDef(BaseValidatorModel):
    apiKey: str
    apiSecretKey: Optional[str] = None

class AuthParameterTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    isSensitiveField: Optional[bool] = None
    connectorSuppliedValues: Optional[List[str]] = None

class BasicAuthCredentialsTypeDef(BaseValidatorModel):
    username: str
    password: str

class CancelFlowExecutionsRequestRequestTypeDef(BaseValidatorModel):
    flowName: str
    executionIds: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ConnectorRuntimeSettingTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    dataType: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    scope: Optional[str] = None
    connectorSuppliedValueOptions: Optional[List[str]] = None

class DataTransferApiTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[DataTransferApiTypeType] = None

class ConnectorDetailTypeDef(BaseValidatorModel):
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

class DestinationFieldPropertiesTypeDef(BaseValidatorModel):
    isCreatable: Optional[bool] = None
    isNullable: Optional[bool] = None
    isUpsertable: Optional[bool] = None
    isUpdatable: Optional[bool] = None
    isDefaultedOnCreate: Optional[bool] = None
    supportedWriteOperations: Optional[List[WriteOperationTypeType]] = None

class SourceFieldPropertiesTypeDef(BaseValidatorModel):
    isRetrievable: Optional[bool] = None
    isQueryable: Optional[bool] = None
    isTimestampFieldForIncrementalQueries: Optional[bool] = None

class ConnectorEntityTypeDef(BaseValidatorModel):
    name: str
    label: Optional[str] = None
    hasNestedEntities: Optional[bool] = None

class GoogleAnalyticsMetadataTypeDef(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None

class HoneycodeMetadataTypeDef(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None

class SalesforceMetadataTypeDef(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None
    dataTransferApis: Optional[List[SalesforceDataTransferApiType]] = None
    oauth2GrantTypesSupported: Optional[List[OAuth2GrantTypeType]] = None

class SlackMetadataTypeDef(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None

class SnowflakeMetadataTypeDef(BaseValidatorModel):
    supportedRegions: Optional[List[str]] = None

class ZendeskMetadataTypeDef(BaseValidatorModel):
    oAuthScopes: Optional[List[str]] = None

class ConnectorOAuthRequestTypeDef(BaseValidatorModel):
    authCode: Optional[str] = None
    redirectUri: Optional[str] = None

class ConnectorOperatorTypeDef(BaseValidatorModel):
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

class DatadogConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    apiKey: str
    applicationKey: str

class DynatraceConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    apiToken: str

class InforNexusConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: str
    userId: str
    secretAccessKey: str
    datakey: str

class RedshiftConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[str] = None

class SingularConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    apiKey: str

class SnowflakeConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    username: str
    password: str

class TrendmicroConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    apiSecretKey: str

class VeevaConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    username: str
    password: str

class DatadogConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class DynatraceConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class InforNexusConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class MarketoConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class PardotConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: Optional[str] = None
    isSandboxEnvironment: Optional[bool] = None
    businessUnitId: Optional[str] = None

class RedshiftConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    bucketName: str
    roleArn: str
    databaseUrl: Optional[str] = None
    bucketPrefix: Optional[str] = None
    dataApiRoleArn: Optional[str] = None
    isRedshiftServerless: Optional[bool] = None
    clusterIdentifier: Optional[str] = None
    workgroupName: Optional[str] = None
    databaseName: Optional[str] = None

class SalesforceConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: Optional[str] = None
    isSandboxEnvironment: Optional[bool] = None
    usePrivateLinkForMetadataAndAuthorization: Optional[bool] = None

class ServiceNowConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class SlackConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class SnowflakeConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    warehouse: str
    stage: str
    bucketName: str
    bucketPrefix: Optional[str] = None
    privateLinkServiceName: Optional[str] = None
    accountName: Optional[str] = None
    region: Optional[str] = None

class VeevaConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class ZendeskConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    instanceUrl: str

class PrivateConnectionProvisioningStateTypeDef(BaseValidatorModel):
    status: Optional[PrivateConnectionProvisioningStatusType] = None
    failureMessage: Optional[str] = None
    failureCause: Optional[PrivateConnectionProvisioningFailureCauseType] = None

class LambdaConnectorProvisioningConfigTypeDef(BaseValidatorModel):
    lambdaArn: str

class CustomAuthCredentialsTypeDef(BaseValidatorModel):
    customAuthenticationType: str
    credentialsMap: Optional[Mapping[str, str]] = None

class ErrorHandlingConfigTypeDef(BaseValidatorModel):
    failOnFirstDestinationError: Optional[bool] = None
    bucketPrefix: Optional[str] = None
    bucketName: Optional[str] = None

class OAuth2PropertiesTypeDef(BaseValidatorModel):
    tokenUrl: str
    oAuth2GrantType: OAuth2GrantTypeType
    tokenUrlCustomProperties: Optional[Mapping[str, str]] = None

class CustomerProfilesDestinationPropertiesTypeDef(BaseValidatorModel):
    domainName: str
    objectTypeName: Optional[str] = None

class DatadogSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class DeleteConnectorProfileRequestRequestTypeDef(BaseValidatorModel):
    connectorProfileName: str
    forceDelete: Optional[bool] = None

class DeleteFlowRequestRequestTypeDef(BaseValidatorModel):
    flowName: str
    forceDelete: Optional[bool] = None

class DescribeConnectorEntityRequestRequestTypeDef(BaseValidatorModel):
    connectorEntityName: str
    connectorType: Optional[ConnectorTypeType] = None
    connectorProfileName: Optional[str] = None
    apiVersion: Optional[str] = None

class DescribeConnectorProfilesRequestRequestTypeDef(BaseValidatorModel):
    connectorProfileNames: Optional[Sequence[str]] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorLabel: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeConnectorRequestRequestTypeDef(BaseValidatorModel):
    connectorType: ConnectorTypeType
    connectorLabel: Optional[str] = None

class DescribeConnectorsRequestRequestTypeDef(BaseValidatorModel):
    connectorTypes: Optional[Sequence[ConnectorTypeType]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeFlowExecutionRecordsRequestRequestTypeDef(BaseValidatorModel):
    flowName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeFlowRequestRequestTypeDef(BaseValidatorModel):
    flowName: str

class ExecutionDetailsTypeDef(BaseValidatorModel):
    mostRecentExecutionMessage: Optional[str] = None
    mostRecentExecutionTime: Optional[datetime] = None
    mostRecentExecutionStatus: Optional[ExecutionStatusType] = None

class DynatraceSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class ErrorInfoTypeDef(BaseValidatorModel):
    putFailuresCount: Optional[int] = None
    executionMessage: Optional[str] = None

class RangeTypeDef(BaseValidatorModel):
    maximum: Optional[float] = None
    minimum: Optional[float] = None

class GlueDataCatalogConfigTypeDef(BaseValidatorModel):
    roleArn: str
    databaseName: str
    tablePrefix: str

class GoogleAnalyticsSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class IncrementalPullConfigTypeDef(BaseValidatorModel):
    datetimeTypeFieldName: Optional[str] = None

class InforNexusSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class ListConnectorEntitiesRequestRequestTypeDef(BaseValidatorModel):
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    entitiesPath: Optional[str] = None
    apiVersion: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListFlowsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class MarketoSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class RegistrationOutputTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    result: Optional[str] = None
    status: Optional[ExecutionStatusType] = None

class OAuth2CustomParameterTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    isRequired: Optional[bool] = None
    label: Optional[str] = None
    description: Optional[str] = None
    isSensitiveField: Optional[bool] = None
    connectorSuppliedValues: Optional[List[str]] = None
    type: Optional[OAuth2CustomPropTypeType] = None

class OAuthPropertiesTypeDef(BaseValidatorModel):
    tokenUrl: str
    authCodeUrl: str
    oAuthScopes: Sequence[str]

class PardotSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class PrefixConfigTypeDef(BaseValidatorModel):
    prefixType: Optional[PrefixTypeType] = None
    prefixFormat: Optional[PrefixFormatType] = None
    pathPrefixHierarchy: Optional[Sequence[PathPrefixType]] = None

class ResetConnectorMetadataCacheRequestRequestTypeDef(BaseValidatorModel):
    connectorProfileName: Optional[str] = None
    connectorType: Optional[ConnectorTypeType] = None
    connectorEntityName: Optional[str] = None
    entitiesPath: Optional[str] = None
    apiVersion: Optional[str] = None

class S3InputFormatConfigTypeDef(BaseValidatorModel):
    s3InputFileType: Optional[S3InputFileTypeType] = None

class SuccessResponseHandlingConfigTypeDef(BaseValidatorModel):
    bucketPrefix: Optional[str] = None
    bucketName: Optional[str] = None

class SAPODataPaginationConfigTypeDef(BaseValidatorModel):
    maxPageSize: int

class SAPODataParallelismConfigTypeDef(BaseValidatorModel):
    maxParallelism: int

class SalesforceSourcePropertiesTypeDef(BaseValidatorModel):
    object: str
    enableDynamicFieldUpdate: Optional[bool] = None
    includeDeletedRecords: Optional[bool] = None
    dataTransferApi: Optional[SalesforceDataTransferApiType] = None

class ServiceNowSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class SingularSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class SlackSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class TrendmicroSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class VeevaSourcePropertiesTypeDef(BaseValidatorModel):
    object: str
    documentType: Optional[str] = None
    includeSourceFiles: Optional[bool] = None
    includeRenditions: Optional[bool] = None
    includeAllVersions: Optional[bool] = None

class ZendeskSourcePropertiesTypeDef(BaseValidatorModel):
    object: str

class StartFlowRequestRequestTypeDef(BaseValidatorModel):
    flowName: str
    clientToken: Optional[str] = None

class StopFlowRequestRequestTypeDef(BaseValidatorModel):
    flowName: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UnregisterConnectorRequestRequestTypeDef(BaseValidatorModel):
    connectorLabel: str
    forceDelete: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class CustomAuthConfigTypeDef(BaseValidatorModel):
    customAuthenticationType: Optional[str] = None
    authParameters: Optional[List[AuthParameterTypeDef]] = None

class CancelFlowExecutionsResponseTypeDef(BaseValidatorModel):
    invalidExecutions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorProfileResponseTypeDef(BaseValidatorModel):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowResponseTypeDef(BaseValidatorModel):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterConnectorResponseTypeDef(BaseValidatorModel):
    connectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlowResponseTypeDef(BaseValidatorModel):
    flowArn: str
    flowStatus: FlowStatusType
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopFlowResponseTypeDef(BaseValidatorModel):
    flowArn: str
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorProfileResponseTypeDef(BaseValidatorModel):
    connectorProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorRegistrationResponseTypeDef(BaseValidatorModel):
    connectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlowResponseTypeDef(BaseValidatorModel):
    flowStatus: FlowStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CustomConnectorSourcePropertiesTypeDef(BaseValidatorModel):
    entityName: str
    customProperties: Optional[Mapping[str, str]] = None
    dataTransferApi: Optional[DataTransferApiTypeDef] = None

class ListConnectorsResponseTypeDef(BaseValidatorModel):
    connectors: List[ConnectorDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectorEntitiesResponseTypeDef(BaseValidatorModel):
    connectorEntityMap: Dict[str, List[ConnectorEntityTypeDef]]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorMetadataTypeDef(BaseValidatorModel):
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

class GoogleAnalyticsConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class HoneycodeConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class MarketoConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class OAuth2CredentialsTypeDef(BaseValidatorModel):
    clientId: Optional[str] = None
    clientSecret: Optional[str] = None
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class OAuthCredentialsTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class PardotConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None
    clientCredentialsArn: Optional[str] = None

class SalesforceConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None
    clientCredentialsArn: Optional[str] = None
    oAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    jwtToken: Optional[str] = None

class SlackConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class ZendeskConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    clientId: str
    clientSecret: str
    accessToken: Optional[str] = None
    oAuthRequest: Optional[ConnectorOAuthRequestTypeDef] = None

class TaskTypeDef(BaseValidatorModel):
    sourceFields: Sequence[str]
    taskType: TaskTypeType
    connectorOperator: Optional[ConnectorOperatorTypeDef] = None
    destinationField: Optional[str] = None
    taskProperties: Optional[Mapping[OperatorPropertiesKeysType, str]] = None

class ConnectorProvisioningConfigTypeDef(BaseValidatorModel):
    lambda: Optional[LambdaConnectorProvisioningConfigTypeDef] = None

class CustomConnectorDestinationPropertiesTypeDef(BaseValidatorModel):
    entityName: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    idFieldNames: Optional[Sequence[str]] = None
    customProperties: Optional[Mapping[str, str]] = None

class EventBridgeDestinationPropertiesTypeDef(BaseValidatorModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class HoneycodeDestinationPropertiesTypeDef(BaseValidatorModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class MarketoDestinationPropertiesTypeDef(BaseValidatorModel):
    object: str
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class RedshiftDestinationPropertiesTypeDef(BaseValidatorModel):
    object: str
    intermediateBucketName: str
    bucketPrefix: Optional[str] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class SalesforceDestinationPropertiesTypeDef(BaseValidatorModel):
    object: str
    idFieldNames: Optional[Sequence[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None
    dataTransferApi: Optional[SalesforceDataTransferApiType] = None

class SnowflakeDestinationPropertiesTypeDef(BaseValidatorModel):
    object: str
    intermediateBucketName: str
    bucketPrefix: Optional[str] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None

class ZendeskDestinationPropertiesTypeDef(BaseValidatorModel):
    object: str
    idFieldNames: Optional[Sequence[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None

class CustomConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    profileProperties: Optional[Mapping[str, str]] = None
    oAuth2Properties: Optional[OAuth2PropertiesTypeDef] = None

class FlowDefinitionTypeDef(BaseValidatorModel):
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

class ExecutionResultTypeDef(BaseValidatorModel):
    errorInfo: Optional[ErrorInfoTypeDef] = None
    bytesProcessed: Optional[int] = None
    bytesWritten: Optional[int] = None
    recordsProcessed: Optional[int] = None
    numParallelProcesses: Optional[int] = None
    maxPageSize: Optional[int] = None

class FieldTypeDetailsTypeDef(BaseValidatorModel):
    fieldType: str
    filterOperators: List[OperatorType]
    supportedValues: Optional[List[str]] = None
    valueRegexPattern: Optional[str] = None
    supportedDateFormat: Optional[str] = None
    fieldValueRange: Optional[RangeTypeDef] = None
    fieldLengthRange: Optional[RangeTypeDef] = None

class MetadataCatalogConfigTypeDef(BaseValidatorModel):
    glueDataCatalog: Optional[GlueDataCatalogConfigTypeDef] = None

class MetadataCatalogDetailTypeDef(BaseValidatorModel):
    catalogType: Optional[Literal["GLUE"]] = None
    tableName: Optional[str] = None
    tableRegistrationOutput: Optional[RegistrationOutputTypeDef] = None
    partitionRegistrationOutput: Optional[RegistrationOutputTypeDef] = None

class OAuth2DefaultsTypeDef(BaseValidatorModel):
    oauthScopes: Optional[List[str]] = None
    tokenUrls: Optional[List[str]] = None
    authCodeUrls: Optional[List[str]] = None
    oauth2GrantTypesSupported: Optional[List[OAuth2GrantTypeType]] = None
    oauth2CustomProperties: Optional[List[OAuth2CustomParameterTypeDef]] = None

class SAPODataConnectorProfilePropertiesTypeDef(BaseValidatorModel):
    applicationHostUrl: str
    applicationServicePath: str
    portNumber: int
    clientNumber: str
    logonLanguage: Optional[str] = None
    privateLinkServiceName: Optional[str] = None
    oAuthProperties: Optional[OAuthPropertiesTypeDef] = None
    disableSSO: Optional[bool] = None

class S3OutputFormatConfigTypeDef(BaseValidatorModel):
    fileType: Optional[FileTypeType] = None
    prefixConfig: Optional[PrefixConfigTypeDef] = None
    aggregationConfig: Optional[AggregationConfigTypeDef] = None
    preserveSourceDataTyping: Optional[bool] = None

class UpsolverS3OutputFormatConfigTypeDef(BaseValidatorModel):
    prefixConfig: PrefixConfigTypeDef
    fileType: Optional[FileTypeType] = None
    aggregationConfig: Optional[AggregationConfigTypeDef] = None

class S3SourcePropertiesTypeDef(BaseValidatorModel):
    bucketName: str
    bucketPrefix: Optional[str] = None
    s3InputFormatConfig: Optional[S3InputFormatConfigTypeDef] = None

class SAPODataDestinationPropertiesTypeDef(BaseValidatorModel):
    objectPath: str
    successResponseHandlingConfig: Optional[SuccessResponseHandlingConfigTypeDef] = None
    idFieldNames: Optional[Sequence[str]] = None
    errorHandlingConfig: Optional[ErrorHandlingConfigTypeDef] = None
    writeOperationType: Optional[WriteOperationTypeType] = None

class SAPODataSourcePropertiesTypeDef(BaseValidatorModel):
    objectPath: Optional[str] = None
    parallelismConfig: Optional[SAPODataParallelismConfigTypeDef] = None
    paginationConfig: Optional[SAPODataPaginationConfigTypeDef] = None

class ScheduledTriggerPropertiesTypeDef(BaseValidatorModel):
    scheduleExpression: str
    dataPullMode: Optional[DataPullModeType] = None
    scheduleStartTime: Optional[TimestampTypeDef] = None
    scheduleEndTime: Optional[TimestampTypeDef] = None
    timezone: Optional[str] = None
    scheduleOffset: Optional[int] = None
    firstExecutionFrom: Optional[TimestampTypeDef] = None
    flowErrorDeactivationThreshold: Optional[int] = None

class CustomConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    authenticationType: AuthenticationTypeType
    basic: Optional[BasicAuthCredentialsTypeDef] = None
    oauth2: Optional[OAuth2CredentialsTypeDef] = None
    apiKey: Optional[ApiKeyCredentialsTypeDef] = None
    custom: Optional[CustomAuthCredentialsTypeDef] = None

class ServiceNowConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[str] = None
    oAuth2Credentials: Optional[OAuth2CredentialsTypeDef] = None

class SAPODataConnectorProfileCredentialsTypeDef(BaseValidatorModel):
    basicAuthCredentials: Optional[BasicAuthCredentialsTypeDef] = None
    oAuthCredentials: Optional[OAuthCredentialsTypeDef] = None

class RegisterConnectorRequestRequestTypeDef(BaseValidatorModel):
    connectorLabel: Optional[str] = None
    description: Optional[str] = None
    connectorProvisioningType: Optional[Literal["LAMBDA"]] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfigTypeDef] = None
    clientToken: Optional[str] = None

class UpdateConnectorRegistrationRequestRequestTypeDef(BaseValidatorModel):
    connectorLabel: str
    description: Optional[str] = None
    connectorProvisioningConfig: Optional[ConnectorProvisioningConfigTypeDef] = None
    clientToken: Optional[str] = None

class ListFlowsResponseTypeDef(BaseValidatorModel):
    flows: List[FlowDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SupportedFieldTypeDetailsTypeDef(BaseValidatorModel):
    v1: FieldTypeDetailsTypeDef

class ExecutionRecordTypeDef(BaseValidatorModel):
    executionId: Optional[str] = None
    executionStatus: Optional[ExecutionStatusType] = None
    executionResult: Optional[ExecutionResultTypeDef] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    dataPullStartTime: Optional[datetime] = None
    dataPullEndTime: Optional[datetime] = None
    metadataCatalogDetails: Optional[List[MetadataCatalogDetailTypeDef]] = None

class AuthenticationConfigTypeDef(BaseValidatorModel):
    isBasicAuthSupported: Optional[bool] = None
    isApiKeyAuthSupported: Optional[bool] = None
    isOAuth2Supported: Optional[bool] = None
    isCustomAuthSupported: Optional[bool] = None
    oAuth2Defaults: Optional[OAuth2DefaultsTypeDef] = None
    customAuthConfigs: Optional[List[CustomAuthConfigTypeDef]] = None

class ConnectorProfilePropertiesTypeDef(BaseValidatorModel):
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

class S3DestinationPropertiesTypeDef(BaseValidatorModel):
    bucketName: str
    bucketPrefix: Optional[str] = None
    s3OutputFormatConfig: Optional[S3OutputFormatConfigTypeDef] = None

class UpsolverDestinationPropertiesTypeDef(BaseValidatorModel):
    bucketName: str
    s3OutputFormatConfig: UpsolverS3OutputFormatConfigTypeDef
    bucketPrefix: Optional[str] = None

class SourceConnectorPropertiesTypeDef(BaseValidatorModel):
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

class TriggerPropertiesTypeDef(BaseValidatorModel):
    Scheduled: Optional[ScheduledTriggerPropertiesTypeDef] = None

class ConnectorProfileCredentialsTypeDef(BaseValidatorModel):
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

class ConnectorEntityFieldTypeDef(BaseValidatorModel):
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

class DescribeFlowExecutionRecordsResponseTypeDef(BaseValidatorModel):
    flowExecutions: List[ExecutionRecordTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectorConfigurationTypeDef(BaseValidatorModel):
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

class ConnectorProfileTypeDef(BaseValidatorModel):
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

class DestinationConnectorPropertiesTypeDef(BaseValidatorModel):
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

class SourceFlowConfigTypeDef(BaseValidatorModel):
    connectorType: ConnectorTypeType
    sourceConnectorProperties: SourceConnectorPropertiesTypeDef
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None
    incrementalPullConfig: Optional[IncrementalPullConfigTypeDef] = None

class TriggerConfigTypeDef(BaseValidatorModel):
    triggerType: TriggerTypeType
    triggerProperties: Optional[TriggerPropertiesTypeDef] = None

class ConnectorProfileConfigTypeDef(BaseValidatorModel):
    connectorProfileProperties: ConnectorProfilePropertiesTypeDef
    connectorProfileCredentials: Optional[ConnectorProfileCredentialsTypeDef] = None

class DescribeConnectorEntityResponseTypeDef(BaseValidatorModel):
    connectorEntityFields: List[ConnectorEntityFieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorResponseTypeDef(BaseValidatorModel):
    connectorConfiguration: ConnectorConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorsResponseTypeDef(BaseValidatorModel):
    connectorConfigurations: Dict[ConnectorTypeType, ConnectorConfigurationTypeDef]
    connectors: List[ConnectorDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorProfilesResponseTypeDef(BaseValidatorModel):
    connectorProfileDetails: List[ConnectorProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationFlowConfigTypeDef(BaseValidatorModel):
    connectorType: ConnectorTypeType
    destinationConnectorProperties: DestinationConnectorPropertiesTypeDef
    apiVersion: Optional[str] = None
    connectorProfileName: Optional[str] = None

class CreateConnectorProfileRequestRequestTypeDef(BaseValidatorModel):
    connectorProfileName: str
    connectorType: ConnectorTypeType
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfigTypeDef
    kmsArn: Optional[str] = None
    connectorLabel: Optional[str] = None
    clientToken: Optional[str] = None

class UpdateConnectorProfileRequestRequestTypeDef(BaseValidatorModel):
    connectorProfileName: str
    connectionMode: ConnectionModeType
    connectorProfileConfig: ConnectorProfileConfigTypeDef
    clientToken: Optional[str] = None

class CreateFlowRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeFlowResponseTypeDef(BaseValidatorModel):
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

class UpdateFlowRequestRequestTypeDef(BaseValidatorModel):
    flowName: str
    triggerConfig: TriggerConfigTypeDef
    sourceFlowConfig: SourceFlowConfigTypeDef
    destinationFlowConfigList: Sequence[DestinationFlowConfigTypeDef]
    tasks: Sequence[TaskTypeDef]
    description: Optional[str] = None
    metadataCatalogConfig: Optional[MetadataCatalogConfigTypeDef] = None
    clientToken: Optional[str] = None

