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


# This class is the input for the 'create_credential_locker' function.
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


# This class is the input for the 'create_destination' function.
class CreateDestinationRequest(BaseValidatorModel):
    DeliveryDestinationArn: str
    DeliveryDestinationType: Literal['KINESIS']
    Name: str
    RoleArn: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_event_log_configuration' function.
class CreateEventLogConfigurationRequest(BaseValidatorModel):
    ResourceType: str
    EventLogLevel: LogLevelType
    ResourceId: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_notification_configuration' function.
class CreateNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_provisioning_profile' function.
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


# This class is the input for the 'delete_credential_locker' function.
class DeleteCredentialLockerRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'delete_destination' function.
class DeleteDestinationRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_event_log_configuration' function.
class DeleteEventLogConfigurationRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'delete_managed_thing' function.
class DeleteManagedThingRequest(BaseValidatorModel):
    Identifier: str
    Force: Optional[bool] = None


# This class is the input for the 'delete_notification_configuration' function.
class DeleteNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType


# This class is the input for the 'delete_ota_task_configuration' function.
class DeleteOtaTaskConfigurationRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'delete_ota_task' function.
class DeleteOtaTaskRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'delete_provisioning_profile' function.
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


# This class is the input for the 'get_credential_locker' function.
class GetCredentialLockerRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_destination' function.
class GetDestinationRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'get_device_discovery' function.
class GetDeviceDiscoveryRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_event_log_configuration' function.
class GetEventLogConfigurationRequest(BaseValidatorModel):
    Id: str


# This class is the input for the 'get_managed_thing_capabilities' function.
class GetManagedThingCapabilitiesRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_managed_thing_connectivity_data' function.
class GetManagedThingConnectivityDataRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_managed_thing_meta_data' function.
class GetManagedThingMetaDataRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_managed_thing' function.
class GetManagedThingRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_managed_thing_state' function.
class GetManagedThingStateRequest(BaseValidatorModel):
    ManagedThingId: str


# This class is the input for the 'get_notification_configuration' function.
class GetNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType


# This class is the input for the 'get_ota_task_configuration' function.
class GetOtaTaskConfigurationRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_ota_task' function.
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


# This class is the input for the 'get_provisioning_profile' function.
class GetProvisioningProfileRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_runtime_log_configuration' function.
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


# This class is the input for the 'get_schema_version' function.
class GetSchemaVersionRequest(BaseValidatorModel):
    Type: SchemaVersionTypeType
    SchemaVersionedId: str
    Format: Optional[SchemaVersionFormatType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_credential_lockers' function.
class ListCredentialLockersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_destinations' function.
class ListDestinationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_event_log_configurations' function.
class ListEventLogConfigurationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_managed_thing_schemas' function.
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


# This class is the input for the 'list_managed_things' function.
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


# This class is the input for the 'list_notification_configurations' function.
class ListNotificationConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NotificationConfigurationSummary(BaseValidatorModel):
    EventType: Optional[EventTypeType] = None
    DestinationName: Optional[str] = None


# This class is the input for the 'list_ota_task_configurations' function.
class ListOtaTaskConfigurationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OtaTaskConfigurationSummary(BaseValidatorModel):
    TaskConfigurationId: Optional[str] = None
    Name: Optional[str] = None
    CreatedAt: Optional[datetime] = None


# This class is the input for the 'list_ota_task_executions' function.
class ListOtaTaskExecutionsRequest(BaseValidatorModel):
    Identifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_ota_tasks' function.
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


# This class is the input for the 'list_provisioning_profiles' function.
class ListProvisioningProfilesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProvisioningProfileSummary(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Arn: Optional[str] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None


# This class is the input for the 'list_schema_versions' function.
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


# This class is the input for the 'put_default_encryption_configuration' function.
class PutDefaultEncryptionConfigurationRequest(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: Optional[str] = None


# This class is the input for the 'put_hub_configuration' function.
class PutHubConfigurationRequest(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int


# This class is the input for the 'reset_runtime_log_configuration' function.
class ResetRuntimeLogConfigurationRequest(BaseValidatorModel):
    ManagedThingId: str


# This class is the input for the 'start_device_discovery' function.
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


# This class is the input for the 'update_destination' function.
class UpdateDestinationRequest(BaseValidatorModel):
    Name: str
    DeliveryDestinationArn: Optional[str] = None
    DeliveryDestinationType: Optional[Literal['KINESIS']] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_event_log_configuration' function.
class UpdateEventLogConfigurationRequest(BaseValidatorModel):
    Id: str
    EventLogLevel: LogLevelType


# This class is the input for the 'update_notification_configuration' function.
class UpdateNotificationConfigurationRequest(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str


# This class is the input for the 'update_ota_task' function.
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


# This class is the output for the 'create_credential_locker' function.
class CreateCredentialLockerResponse(BaseValidatorModel):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_destination' function.
class CreateDestinationResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_event_log_configuration' function.
class CreateEventLogConfigurationResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_managed_thing' function.
class CreateManagedThingResponse(BaseValidatorModel):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_notification_configuration' function.
class CreateNotificationConfigurationResponse(BaseValidatorModel):
    EventType: EventTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ota_task_configuration' function.
class CreateOtaTaskConfigurationResponse(BaseValidatorModel):
    TaskConfigurationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ota_task' function.
class CreateOtaTaskResponse(BaseValidatorModel):
    TaskId: str
    TaskArn: str
    Description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_provisioning_profile' function.
class CreateProvisioningProfileResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    ClaimCertificatePrivateKey: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ota_task' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_credential_locker' function.
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


# This class is the output for the 'get_destination' function.
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


# This class is the output for the 'get_device_discovery' function.
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


# This class is the output for the 'get_event_log_configuration' function.
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


# This class is the output for the 'get_managed_thing_connectivity_data' function.
class GetManagedThingConnectivityDataResponse(BaseValidatorModel):
    ManagedThingId: str
    Connected: bool
    Timestamp: datetime
    DisconnectReason: DisconnectReasonValueType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_managed_thing_meta_data' function.
class GetManagedThingMetaDataResponse(BaseValidatorModel):
    ManagedThingId: str
    MetaData: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_managed_thing' function.
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


# This class is the output for the 'get_notification_configuration' function.
class GetNotificationConfigurationResponse(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_provisioning_profile' function.
class GetProvisioningProfileResponse(BaseValidatorModel):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_schema_version' function.
class GetSchemaVersionResponse(BaseValidatorModel):
    SchemaId: str
    Type: SchemaVersionTypeType
    Description: str
    Namespace: str
    SemanticVersion: str
    Visibility: SchemaVersionVisibilityType
    Schema: Dict[str, Any]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_hub_configuration' function.
class PutHubConfigurationResponse(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int
    ResponseMetadata: ResponseMetadata


class RegisterCustomEndpointResponse(BaseValidatorModel):
    EndpointAddress: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_managed_thing_command' function.
class SendManagedThingCommandResponse(BaseValidatorModel):
    TraceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_device_discovery' function.
class StartDeviceDiscoveryResponse(BaseValidatorModel):
    Id: str
    StartedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_credential_lockers' function.
class ListCredentialLockersResponse(BaseValidatorModel):
    Items: List[CredentialLockerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_destinations' function.
class ListDestinationsResponse(BaseValidatorModel):
    DestinationList: List[DestinationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_event_log_configurations' function.
class ListEventLogConfigurationsResponse(BaseValidatorModel):
    EventLogConfigurationList: List[EventLogConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExponentialRolloutRate(BaseValidatorModel):
    BaseRatePerMinute: Optional[int] = None
    IncrementFactor: Optional[float] = None
    RateIncreaseCriteria: Optional[RolloutRateIncreaseCriteria] = None


# This class is the output for the 'get_runtime_log_configuration' function.
class GetRuntimeLogConfigurationResponse(BaseValidatorModel):
    ManagedThingId: str
    RuntimeLogConfigurations: RuntimeLogConfigurations
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_runtime_log_configuration' function.
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


# This class is the output for the 'list_managed_thing_schemas' function.
class ListManagedThingSchemasResponse(BaseValidatorModel):
    Items: List[ManagedThingSchemaListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_managed_things' function.
class ListManagedThingsResponse(BaseValidatorModel):
    Items: List[ManagedThingSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_notification_configurations' function.
class ListNotificationConfigurationsResponse(BaseValidatorModel):
    NotificationConfigurationList: List[NotificationConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_ota_task_configurations' function.
class ListOtaTaskConfigurationsResponse(BaseValidatorModel):
    Items: List[OtaTaskConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_ota_tasks' function.
class ListOtaTasksResponse(BaseValidatorModel):
    Tasks: List[OtaTaskSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_provisioning_profiles' function.
class ListProvisioningProfilesResponse(BaseValidatorModel):
    Items: List[ProvisioningProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_schema_versions' function.
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


# This class is the output for the 'put_default_encryption_configuration' function.
class PutDefaultEncryptionConfigurationResponse(BaseValidatorModel):
    configurationStatus: ConfigurationStatus
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadata


class OtaTaskExecutionRolloutConfig(BaseValidatorModel):
    ExponentialRolloutRate: Optional[ExponentialRolloutRate] = None
    MaximumPerMinute: Optional[int] = None

OtaTaskExecutionRetryConfigUnion = Union[OtaTaskExecutionRetryConfig, OtaTaskExecutionRetryConfigOutput]


# This class is the output for the 'list_ota_task_executions' function.
class ListOtaTaskExecutionsResponse(BaseValidatorModel):
    ExecutionSummaries: List[OtaTaskExecutionSummaries]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_ota_task' function.
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


# This class is the output for the 'get_managed_thing_state' function.
class GetManagedThingStateResponse(BaseValidatorModel):
    Endpoints: List[StateEndpoint]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'send_managed_thing_command' function.
class SendManagedThingCommandRequest(BaseValidatorModel):
    ManagedThingId: str
    Endpoints: List[CommandEndpoint]
    ConnectorAssociationId: Optional[str] = None


# This class is the output for the 'get_managed_thing_capabilities' function.
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


# This class is the input for the 'create_ota_task' function.
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


# This class is the input for the 'create_managed_thing' function.
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


# This class is the input for the 'update_managed_thing' function.
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


# This class is the output for the 'get_ota_task_configuration' function.
class GetOtaTaskConfigurationResponse(BaseValidatorModel):
    TaskConfigurationId: str
    Name: str
    PushConfig: PushConfigOutput
    Description: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata

PushConfigUnion = Union[PushConfig, PushConfigOutput]


# This class is the input for the 'create_ota_task_configuration' function.
class CreateOtaTaskConfigurationRequest(BaseValidatorModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    PushConfig: Optional[PushConfigUnion] = None
    ClientToken: Optional[str] = None