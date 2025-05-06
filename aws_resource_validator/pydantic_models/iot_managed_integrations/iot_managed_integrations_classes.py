from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iot_managed_integrations.iot_managed_integrations_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AbortConfigCriteria(BaseValidatorModel):
    Action: Optional[Literal['CANCEL']] = None
    FailureType: Optional[AbortCriteriaFailureTypeType] = None
    MinNumberOfExecutedThings: Optional[int] = None
    ThresholdPercentage: Optional[float] = None


class CapabilityAction(BaseValidatorModel):
    name: str
    ref: Optional[str] = None
    actionTraceId: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None


class CapabilityReportCapabilityOutput(BaseValidatorModel):
    id: str
    name: str
    version: str
    properties: List[str]
    actions: List[str]
    events: List[str]


class CapabilityReportCapability(BaseValidatorModel):
    id: str
    name: str
    version: str
    properties: List[str]
    actions: List[str]
    events: List[str]


class ConfigurationError(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class CreateCredentialLockerRequest(BaseValidatorModel):
    Name: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDestinationRequest(BaseValidatorModel):
    DeliveryDestinationArn: str
    DeliveryDestinationType: Literal['KINESIS']
    Name: str
    RoleArn: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CreateEventLogConfigurationRequest(BaseValidatorModel):
    ResourceType: str
    EventLogLevel: LogLevelType
    ResourceId: Optional[str] = None
    ClientToken: Optional[str] = None


class CreateNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CreateProvisioningProfileRequest(BaseValidatorModel):
    ProvisioningType: ProvisioningTypeType
    CaCertificate: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CredentialLockerSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class DeleteCredentialLockerRequest(BaseValidatorModel):
    Identifier: str


class DeleteDestinationRequest(BaseValidatorModel):
    Name: str


class DeleteEventLogConfigurationRequest(BaseValidatorModel):
    Id: str


class DeleteManagedThingRequest(BaseValidatorModel):
    Identifier: str
    Force: Optional[bool] = None


class DeleteNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType


class DeleteOtaTaskConfigurationRequest(BaseValidatorModel):
    Identifier: str


class DeleteOtaTaskRequest(BaseValidatorModel):
    Identifier: str


class DeleteProvisioningProfileRequest(BaseValidatorModel):
    Identifier: str


class DestinationSummary(BaseValidatorModel):
    Description: Optional[str] = None
    DeliveryDestinationArn: Optional[str] = None
    DeliveryDestinationType: Optional[Literal['KINESIS']] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None


class EventLogConfigurationSummary(BaseValidatorModel):
    Id: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    EventLogLevel: Optional[LogLevelType] = None


class RolloutRateIncreaseCriteria(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None


class GetCredentialLockerRequest(BaseValidatorModel):
    Identifier: str


class GetDestinationRequest(BaseValidatorModel):
    Name: str


class GetDeviceDiscoveryRequest(BaseValidatorModel):
    Identifier: str


class GetEventLogConfigurationRequest(BaseValidatorModel):
    Id: str


class GetManagedThingCapabilitiesRequest(BaseValidatorModel):
    Identifier: str


class GetManagedThingConnectivityDataRequest(BaseValidatorModel):
    Identifier: str


class GetManagedThingMetaDataRequest(BaseValidatorModel):
    Identifier: str


class GetManagedThingRequest(BaseValidatorModel):
    Identifier: str


class GetManagedThingStateRequest(BaseValidatorModel):
    ManagedThingId: str


class GetNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType


class GetOtaTaskConfigurationRequest(BaseValidatorModel):
    Identifier: str


class GetOtaTaskRequest(BaseValidatorModel):
    Identifier: str


class TaskProcessingDetails(BaseValidatorModel):
    NumberOfCanceledThings: Optional[int] = None
    NumberOfFailedThings: Optional[int] = None
    NumberOfInProgressThings: Optional[int] = None
    numberOfQueuedThings: Optional[int] = None
    numberOfRejectedThings: Optional[int] = None
    numberOfRemovedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None
    numberOfTimedOutThings: Optional[int] = None
    processingTargets: Optional[List[str]] = None


class GetProvisioningProfileRequest(BaseValidatorModel):
    Identifier: str


class GetRuntimeLogConfigurationRequest(BaseValidatorModel):
    ManagedThingId: str


class RuntimeLogConfigurations(BaseValidatorModel):
    LogLevel: Optional[LogLevelType] = None
    LogFlushLevel: Optional[LogLevelType] = None
    LocalStoreLocation: Optional[str] = None
    LocalStoreFileRotationMaxFiles: Optional[int] = None
    LocalStoreFileRotationMaxBytes: Optional[int] = None
    UploadLog: Optional[bool] = None
    UploadPeriodMinutes: Optional[int] = None
    DeleteLocalStoreAfterUpload: Optional[bool] = None


class GetSchemaVersionRequest(BaseValidatorModel):
    Type: SchemaVersionTypeType
    SchemaVersionedId: str
    Format: Optional[SchemaVersionFormatType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCredentialLockersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDestinationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventLogConfigurationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListManagedThingSchemasRequest(BaseValidatorModel):
    Identifier: str
    EndpointIdFilter: Optional[str] = None
    CapabilityIdFilter: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ManagedThingSchemaListItem(BaseValidatorModel):
    EndpointId: Optional[str] = None
    CapabilityId: Optional[str] = None
    Schema: Optional[Dict[str, Any]] = None


class ListManagedThingsRequest(BaseValidatorModel):
    OwnerFilter: Optional[str] = None
    CredentialLockerFilter: Optional[str] = None
    RoleFilter: Optional[RoleType] = None
    ParentControllerIdentifierFilter: Optional[str] = None
    ConnectorPolicyIdFilter: Optional[str] = None
    SerialNumberFilter: Optional[str] = None
    ProvisioningStatusFilter: Optional[ProvisioningStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ManagedThingSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    AdvertisedProductId: Optional[str] = None
    Brand: Optional[str] = None
    Classification: Optional[str] = None
    ConnectorDeviceId: Optional[str] = None
    ConnectorPolicyId: Optional[str] = None
    Model: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    CredentialLockerId: Optional[str] = None
    ParentControllerId: Optional[str] = None
    ProvisioningStatus: Optional[ProvisioningStatusType] = None
    Role: Optional[RoleType] = None
    SerialNumber: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    ActivatedAt: Optional[datetime] = None


class ListNotificationConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NotificationConfigurationSummary(BaseValidatorModel):
    EventType: Optional[EventTypeType] = None
    DestinationName: Optional[str] = None


class ListOtaTaskConfigurationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OtaTaskConfigurationSummary(BaseValidatorModel):
    TaskConfigurationId: Optional[str] = None
    Name: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class ListOtaTaskExecutionsRequest(BaseValidatorModel):
    Identifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOtaTasksRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OtaTaskSummary(BaseValidatorModel):
    TaskId: Optional[str] = None
    TaskArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    TaskConfigurationId: Optional[str] = None
    Status: Optional[OtaStatusType] = None


class ListProvisioningProfilesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProvisioningProfileSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Arn: Optional[str] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None


class ListSchemaVersionsRequest(BaseValidatorModel):
    Type: SchemaVersionTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SchemaId: Optional[str] = None
    Namespace: Optional[str] = None
    Visibility: Optional[SchemaVersionVisibilityType] = None
    SemanticVersion: Optional[str] = None


class SchemaVersionListItem(BaseValidatorModel):
    SchemaId: Optional[str] = None
    Type: Optional[SchemaVersionTypeType] = None
    Description: Optional[str] = None
    Namespace: Optional[str] = None
    SemanticVersion: Optional[str] = None
    Visibility: Optional[SchemaVersionVisibilityType] = None


class RetryConfigCriteria(BaseValidatorModel):
    FailureType: Optional[RetryCriteriaFailureTypeType] = None
    MinNumberOfRetries: Optional[int] = None


class OtaTaskExecutionSummary(BaseValidatorModel):
    ExecutionNumber: Optional[int] = None
    LastUpdatedAt: Optional[datetime] = None
    QueuedAt: Optional[datetime] = None
    RetryAttempt: Optional[int] = None
    StartedAt: Optional[datetime] = None
    Status: Optional[OtaTaskExecutionStatusType] = None


class ScheduleMaintenanceWindow(BaseValidatorModel):
    DurationInMinutes: Optional[int] = None
    StartTime: Optional[str] = None


class OtaTaskTimeoutConfig(BaseValidatorModel):
    InProgressTimeoutInMinutes: Optional[int] = None


class PutDefaultEncryptionConfigurationRequest(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: Optional[str] = None


class PutHubConfigurationRequest(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int


class ResetRuntimeLogConfigurationRequest(BaseValidatorModel):
    ManagedThingId: str


class StartDeviceDiscoveryRequest(BaseValidatorModel):
    DiscoveryType: DiscoveryTypeType
    ControllerIdentifier: Optional[str] = None
    ConnectorAssociationIdentifier: Optional[str] = None
    AuthenticationMaterial: Optional[str] = None
    AuthenticationMaterialType: Optional[Literal['ZWAVE_INSTALL_CODE']] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class StateCapability(BaseValidatorModel):
    id: str
    name: str
    version: str
    properties: Optional[Dict[str, Any]] = None


class UpdateDestinationRequest(BaseValidatorModel):
    Name: str
    DeliveryDestinationArn: Optional[str] = None
    DeliveryDestinationType: Optional[Literal['KINESIS']] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None


class UpdateEventLogConfigurationRequest(BaseValidatorModel):
    Id: str
    EventLogLevel: LogLevelType


class UpdateNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str


class UpdateOtaTaskRequest(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None
    TaskConfigurationId: Optional[str] = None


class OtaTaskAbortConfigOutput(BaseValidatorModel):
    AbortConfigCriteriaList: Optional[List[AbortConfigCriteria]] = None


class OtaTaskAbortConfig(BaseValidatorModel):
    AbortConfigCriteriaList: Optional[List[AbortConfigCriteria]] = None


class CommandCapability(BaseValidatorModel):
    id: str
    name: str
    version: str
    actions: List[CapabilityAction]


class CapabilityReportEndpointOutput(BaseValidatorModel):
    id: str
    deviceTypes: List[str]
    capabilities: List[CapabilityReportCapabilityOutput]


class CapabilityReportEndpoint(BaseValidatorModel):
    id: str
    deviceTypes: List[str]
    capabilities: List[CapabilityReportCapability]


class ConfigurationStatus(BaseValidatorModel):
    state: ConfigurationStateType
    error: Optional[ConfigurationError] = None


class CreateCredentialLockerResponse(BaseValidatorModel):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class CreateDestinationResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateEventLogConfigurationResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateManagedThingResponse(BaseValidatorModel):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class CreateNotificationConfigurationResponse(BaseValidatorModel):
    EventType: EventTypeType
    ResponseMetadata: ResponseMetadata


class CreateOtaTaskConfigurationResponse(BaseValidatorModel):
    TaskConfigurationId: str
    ResponseMetadata: ResponseMetadata


class CreateOtaTaskResponse(BaseValidatorModel):
    TaskId: str
    TaskArn: str
    Description: str
    ResponseMetadata: ResponseMetadata


class CreateProvisioningProfileResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    ClaimCertificatePrivateKey: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetCredentialLockerResponse(BaseValidatorModel):
    Id: str
    Arn: str
    Name: str
    CreatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetCustomEndpointResponse(BaseValidatorModel):
    EndpointAddress: str
    ResponseMetadata: ResponseMetadata


class GetDestinationResponse(BaseValidatorModel):
    Description: str
    DeliveryDestinationArn: str
    DeliveryDestinationType: Literal['KINESIS']
    Name: str
    RoleArn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetDeviceDiscoveryResponse(BaseValidatorModel):
    Id: str
    Arn: str
    DiscoveryType: DiscoveryTypeType
    Status: DeviceDiscoveryStatusType
    StartedAt: datetime
    ControllerId: str
    ConnectorAssociationId: str
    FinishedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetEventLogConfigurationResponse(BaseValidatorModel):
    Id: str
    ResourceType: str
    ResourceId: str
    EventLogLevel: LogLevelType
    ResponseMetadata: ResponseMetadata


class GetHubConfigurationResponse(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetManagedThingConnectivityDataResponse(BaseValidatorModel):
    ManagedThingId: str
    Connected: bool
    Timestamp: datetime
    DisconnectReason: DisconnectReasonValueType
    ResponseMetadata: ResponseMetadata


class GetManagedThingMetaDataResponse(BaseValidatorModel):
    ManagedThingId: str
    MetaData: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetManagedThingResponse(BaseValidatorModel):
    Id: str
    Arn: str
    Owner: str
    CredentialLockerId: str
    AdvertisedProductId: str
    Role: RoleType
    ProvisioningStatus: ProvisioningStatusType
    Name: str
    Model: str
    Brand: str
    SerialNumber: str
    UniversalProductCode: str
    InternationalArticleNumber: str
    ConnectorPolicyId: str
    ConnectorDeviceId: str
    DeviceSpecificKey: str
    MacAddress: str
    ParentControllerId: str
    Classification: str
    CreatedAt: datetime
    UpdatedAt: datetime
    ActivatedAt: datetime
    HubNetworkMode: HubNetworkModeType
    MetaData: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetNotificationConfigurationResponse(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetProvisioningProfileResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetSchemaVersionResponse(BaseValidatorModel):
    SchemaId: str
    Type: SchemaVersionTypeType
    Description: str
    Namespace: str
    SemanticVersion: str
    Visibility: SchemaVersionVisibilityType
    Schema: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


class PutHubConfigurationResponse(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int
    ResponseMetadata: ResponseMetadata


class RegisterCustomEndpointResponse(BaseValidatorModel):
    EndpointAddress: str
    ResponseMetadata: ResponseMetadata


class SendManagedThingCommandResponse(BaseValidatorModel):
    TraceId: str
    ResponseMetadata: ResponseMetadata


class StartDeviceDiscoveryResponse(BaseValidatorModel):
    Id: str
    StartedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListCredentialLockersResponse(BaseValidatorModel):
    Items: List[CredentialLockerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDestinationsResponse(BaseValidatorModel):
    DestinationList: List[DestinationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEventLogConfigurationsResponse(BaseValidatorModel):
    EventLogConfigurationList: List[EventLogConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExponentialRolloutRate(BaseValidatorModel):
    BaseRatePerMinute: Optional[int] = None
    IncrementFactor: Optional[float] = None
    RateIncreaseCriteria: Optional[RolloutRateIncreaseCriteria] = None


class GetRuntimeLogConfigurationResponse(BaseValidatorModel):
    ManagedThingId: str
    RuntimeLogConfigurations: RuntimeLogConfigurations
    ResponseMetadata: ResponseMetadata


class PutRuntimeLogConfigurationRequest(BaseValidatorModel):
    ManagedThingId: str
    RuntimeLogConfigurations: RuntimeLogConfigurations


class ListCredentialLockersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDestinationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventLogConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedThingSchemasRequestPaginate(BaseValidatorModel):
    Identifier: str
    EndpointIdFilter: Optional[str] = None
    CapabilityIdFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedThingsRequestPaginate(BaseValidatorModel):
    OwnerFilter: Optional[str] = None
    CredentialLockerFilter: Optional[str] = None
    RoleFilter: Optional[RoleType] = None
    ParentControllerIdentifierFilter: Optional[str] = None
    ConnectorPolicyIdFilter: Optional[str] = None
    SerialNumberFilter: Optional[str] = None
    ProvisioningStatusFilter: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOtaTaskConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOtaTaskExecutionsRequestPaginate(BaseValidatorModel):
    Identifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOtaTasksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisioningProfilesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemaVersionsRequestPaginate(BaseValidatorModel):
    Type: SchemaVersionTypeType
    SchemaId: Optional[str] = None
    Namespace: Optional[str] = None
    Visibility: Optional[SchemaVersionVisibilityType] = None
    SemanticVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedThingSchemasResponse(BaseValidatorModel):
    Items: List[ManagedThingSchemaListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListManagedThingsResponse(BaseValidatorModel):
    Items: List[ManagedThingSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListNotificationConfigurationsResponse(BaseValidatorModel):
    NotificationConfigurationList: List[NotificationConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOtaTaskConfigurationsResponse(BaseValidatorModel):
    Items: List[OtaTaskConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOtaTasksResponse(BaseValidatorModel):
    Tasks: List[OtaTaskSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProvisioningProfilesResponse(BaseValidatorModel):
    Items: List[ProvisioningProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSchemaVersionsResponse(BaseValidatorModel):
    Items: List[SchemaVersionListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OtaTaskExecutionRetryConfigOutput(BaseValidatorModel):
    RetryConfigCriteria: Optional[List[RetryConfigCriteria]] = None


class OtaTaskExecutionRetryConfig(BaseValidatorModel):
    RetryConfigCriteria: Optional[List[RetryConfigCriteria]] = None


class OtaTaskExecutionSummaries(BaseValidatorModel):
    TaskExecutionSummary: Optional[OtaTaskExecutionSummary] = None
    ManagedThingId: Optional[str] = None


class OtaTaskSchedulingConfigOutput(BaseValidatorModel):
    EndBehavior: Optional[SchedulingConfigEndBehaviorType] = None
    EndTime: Optional[str] = None
    MaintenanceWindows: Optional[List[ScheduleMaintenanceWindow]] = None
    StartTime: Optional[str] = None


class OtaTaskSchedulingConfig(BaseValidatorModel):
    EndBehavior: Optional[SchedulingConfigEndBehaviorType] = None
    EndTime: Optional[str] = None
    MaintenanceWindows: Optional[List[ScheduleMaintenanceWindow]] = None
    StartTime: Optional[str] = None


class StateEndpoint(BaseValidatorModel):
    endpointId: str
    capabilities: List[StateCapability]


class CommandEndpoint(BaseValidatorModel):
    endpointId: str
    capabilities: List[CommandCapability]


class CapabilityReportOutput(BaseValidatorModel):
    version: str
    endpoints: List[CapabilityReportEndpointOutput]
    nodeId: Optional[str] = None


class CapabilityReport(BaseValidatorModel):
    version: str
    endpoints: List[CapabilityReportEndpoint]
    nodeId: Optional[str] = None


class GetDefaultEncryptionConfigurationResponse(BaseValidatorModel):
    configurationStatus: ConfigurationStatus
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadata


class PutDefaultEncryptionConfigurationResponse(BaseValidatorModel):
    configurationStatus: ConfigurationStatus
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadata


class OtaTaskExecutionRolloutConfig(BaseValidatorModel):
    ExponentialRolloutRate: Optional[ExponentialRolloutRate] = None
    MaximumPerMinute: Optional[int] = None

OtaTaskExecutionRetryConfigUnion = Union[OtaTaskExecutionRetryConfig, OtaTaskExecutionRetryConfigOutput]


class ListOtaTaskExecutionsResponse(BaseValidatorModel):
    ExecutionSummaries: List[OtaTaskExecutionSummaries]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetOtaTaskResponse(BaseValidatorModel):
    TaskId: str
    TaskArn: str
    Description: str
    S3Url: str
    Protocol: Literal['HTTP']
    OtaType: OtaTypeType
    OtaTargetQueryString: str
    OtaMechanism: Literal['PUSH']
    Target: List[str]
    CreatedAt: datetime
    LastUpdatedAt: datetime
    TaskConfigurationId: str
    TaskProcessingDetails: TaskProcessingDetails
    OtaSchedulingConfig: OtaTaskSchedulingConfigOutput
    OtaTaskExecutionRetryConfig: OtaTaskExecutionRetryConfigOutput
    Status: OtaStatusType
    ResponseMetadata: ResponseMetadata

OtaTaskSchedulingConfigUnion = Union[OtaTaskSchedulingConfig, OtaTaskSchedulingConfigOutput]


class GetManagedThingStateResponse(BaseValidatorModel):
    Endpoints: List[StateEndpoint]
    ResponseMetadata: ResponseMetadata


class SendManagedThingCommandRequest(BaseValidatorModel):
    ManagedThingId: str
    Endpoints: List[CommandEndpoint]
    ConnectorAssociationId: Optional[str] = None


class GetManagedThingCapabilitiesResponse(BaseValidatorModel):
    ManagedThingId: str
    Capabilities: str
    CapabilityReport: CapabilityReportOutput
    ResponseMetadata: ResponseMetadata

CapabilityReportUnion = Union[CapabilityReport, CapabilityReportOutput]


class PushConfigOutput(BaseValidatorModel):
    AbortConfig: Optional[OtaTaskAbortConfigOutput] = None
    RolloutConfig: Optional[OtaTaskExecutionRolloutConfig] = None
    TimeoutConfig: Optional[OtaTaskTimeoutConfig] = None


class PushConfig(BaseValidatorModel):
    AbortConfig: Optional[OtaTaskAbortConfig] = None
    RolloutConfig: Optional[OtaTaskExecutionRolloutConfig] = None
    TimeoutConfig: Optional[OtaTaskTimeoutConfig] = None


class CreateOtaTaskRequest(BaseValidatorModel):
    S3Url: str
    OtaType: OtaTypeType
    Description: Optional[str] = None
    Protocol: Optional[Literal['HTTP']] = None
    Target: Optional[List[str]] = None
    TaskConfigurationId: Optional[str] = None
    OtaMechanism: Optional[Literal['PUSH']] = None
    OtaTargetQueryString: Optional[str] = None
    ClientToken: Optional[str] = None
    OtaSchedulingConfig: Optional[OtaTaskSchedulingConfigUnion] = None
    OtaTaskExecutionRetryConfig: Optional[OtaTaskExecutionRetryConfigUnion] = None
    Tags: Optional[Dict[str, str]] = None


class CreateManagedThingRequest(BaseValidatorModel):
    Role: RoleType
    AuthenticationMaterial: str
    AuthenticationMaterialType: AuthMaterialTypeType
    Owner: Optional[str] = None
    CredentialLockerId: Optional[str] = None
    SerialNumber: Optional[str] = None
    Brand: Optional[str] = None
    Model: Optional[str] = None
    Name: Optional[str] = None
    CapabilityReport: Optional[CapabilityReportUnion] = None
    Capabilities: Optional[str] = None
    ClientToken: Optional[str] = None
    Classification: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    MetaData: Optional[Dict[str, str]] = None


class UpdateManagedThingRequest(BaseValidatorModel):
    Identifier: str
    Owner: Optional[str] = None
    CredentialLockerId: Optional[str] = None
    SerialNumber: Optional[str] = None
    Brand: Optional[str] = None
    Model: Optional[str] = None
    Name: Optional[str] = None
    CapabilityReport: Optional[CapabilityReportUnion] = None
    Capabilities: Optional[str] = None
    Classification: Optional[str] = None
    HubNetworkMode: Optional[HubNetworkModeType] = None
    MetaData: Optional[Dict[str, str]] = None


class GetOtaTaskConfigurationResponse(BaseValidatorModel):
    TaskConfigurationId: str
    Name: str
    PushConfig: PushConfigOutput
    Description: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata

PushConfigUnion = Union[PushConfig, PushConfigOutput]


class CreateOtaTaskConfigurationRequest(BaseValidatorModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    PushConfig: Optional[PushConfigUnion] = None
    ClientToken: Optional[str] = None