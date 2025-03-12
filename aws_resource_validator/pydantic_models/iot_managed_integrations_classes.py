from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.iot_managed_integrations_constants import *

class AbortConfigCriteriaTypeDef(BaseValidatorModel):
    Action: Optional[Literal["CANCEL"]] = None
    FailureType: Optional[AbortCriteriaFailureTypeType] = None
    MinNumberOfExecutedThings: Optional[int] = None
    ThresholdPercentage: Optional[float] = None


class CapabilityActionTypeDef(BaseValidatorModel):
    name: str
    ref: Optional[str] = None
    actionTraceId: Optional[str] = None
    parameters: Optional[Mapping[str, Any]] = None


class ConfigurationErrorTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class CreateCredentialLockerRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateDestinationRequestTypeDef(BaseValidatorModel):
    DeliveryDestinationArn: str
    DeliveryDestinationType: Literal["KINESIS"]
    Name: str
    RoleArn: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateEventLogConfigurationRequestTypeDef(BaseValidatorModel):
    ResourceType: str
    EventLogLevel: LogLevelType
    ResourceId: Optional[str] = None
    ClientToken: Optional[str] = None


class CreateNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateProvisioningProfileRequestTypeDef(BaseValidatorModel):
    ProvisioningType: ProvisioningTypeType
    CaCertificate: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CredentialLockerSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class DeleteCredentialLockerRequestTypeDef(BaseValidatorModel):
    Identifier: str


class DeleteDestinationRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteEventLogConfigurationRequestTypeDef(BaseValidatorModel):
    Id: str


class DeleteManagedThingRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Force: Optional[bool] = None


class DeleteNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    EventType: EventTypeType


class DeleteOtaTaskConfigurationRequestTypeDef(BaseValidatorModel):
    Identifier: str


class DeleteOtaTaskRequestTypeDef(BaseValidatorModel):
    Identifier: str


class DeleteProvisioningProfileRequestTypeDef(BaseValidatorModel):
    Identifier: str


class DestinationSummaryTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    DeliveryDestinationArn: Optional[str] = None
    DeliveryDestinationType: Optional[Literal["KINESIS"]] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None


class EventLogConfigurationSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    EventLogLevel: Optional[LogLevelType] = None


class RolloutRateIncreaseCriteriaTypeDef(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None


class GetCredentialLockerRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetDestinationRequestTypeDef(BaseValidatorModel):
    Name: str


class GetDeviceDiscoveryRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetEventLogConfigurationRequestTypeDef(BaseValidatorModel):
    Id: str


class GetManagedThingCapabilitiesRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetManagedThingConnectivityDataRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetManagedThingMetaDataRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetManagedThingRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetManagedThingStateRequestTypeDef(BaseValidatorModel):
    ManagedThingId: str


class GetNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    EventType: EventTypeType


class GetOtaTaskConfigurationRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetOtaTaskRequestTypeDef(BaseValidatorModel):
    Identifier: str


class TaskProcessingDetailsTypeDef(BaseValidatorModel):
    NumberOfCanceledThings: Optional[int] = None
    NumberOfFailedThings: Optional[int] = None
    NumberOfInProgressThings: Optional[int] = None
    numberOfQueuedThings: Optional[int] = None
    numberOfRejectedThings: Optional[int] = None
    numberOfRemovedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None
    numberOfTimedOutThings: Optional[int] = None
    processingTargets: Optional[List[str]] = None


class GetProvisioningProfileRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetRuntimeLogConfigurationRequestTypeDef(BaseValidatorModel):
    ManagedThingId: str


class RuntimeLogConfigurationsTypeDef(BaseValidatorModel):
    LogLevel: Optional[LogLevelType] = None
    LogFlushLevel: Optional[LogLevelType] = None
    LocalStoreLocation: Optional[str] = None
    LocalStoreFileRotationMaxFiles: Optional[int] = None
    LocalStoreFileRotationMaxBytes: Optional[int] = None
    UploadLog: Optional[bool] = None
    UploadPeriodMinutes: Optional[int] = None
    DeleteLocalStoreAfterUpload: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCredentialLockersRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDestinationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventLogConfigurationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListManagedThingSchemasRequestTypeDef(BaseValidatorModel):
    Identifier: str
    EndpointIdFilter: Optional[str] = None
    CapabilityIdFilter: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ManagedThingSchemaListItemTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    CapabilityId: Optional[str] = None
    Schema: Optional[Dict[str, Any]] = None


class ListManagedThingsRequestTypeDef(BaseValidatorModel):
    OwnerFilter: Optional[str] = None
    CredentialLockerFilter: Optional[str] = None
    RoleFilter: Optional[RoleType] = None
    ParentControllerIdentifierFilter: Optional[str] = None
    ConnectorPolicyIdFilter: Optional[str] = None
    SerialNumberFilter: Optional[str] = None
    ProvisioningStatusFilter: Optional[ProvisioningStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ManagedThingSummaryTypeDef(BaseValidatorModel):
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


class ListNotificationConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NotificationConfigurationSummaryTypeDef(BaseValidatorModel):
    EventType: Optional[EventTypeType] = None
    DestinationName: Optional[str] = None


class ListOtaTaskConfigurationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OtaTaskConfigurationSummaryTypeDef(BaseValidatorModel):
    TaskConfigurationId: Optional[str] = None
    Name: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class ListOtaTaskExecutionsRequestTypeDef(BaseValidatorModel):
    Identifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListOtaTasksRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OtaTaskSummaryTypeDef(BaseValidatorModel):
    TaskId: Optional[str] = None
    TaskArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    TaskConfigurationId: Optional[str] = None
    Status: Optional[OtaStatusType] = None


class ListProvisioningProfilesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProvisioningProfileSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    Arn: Optional[str] = None
    ProvisioningType: Optional[ProvisioningTypeType] = None


class RetryConfigCriteriaTypeDef(BaseValidatorModel):
    FailureType: Optional[RetryCriteriaFailureTypeType] = None
    MinNumberOfRetries: Optional[int] = None


class OtaTaskExecutionSummaryTypeDef(BaseValidatorModel):
    ExecutionNumber: Optional[int] = None
    LastUpdatedAt: Optional[datetime] = None
    QueuedAt: Optional[datetime] = None
    RetryAttempt: Optional[int] = None
    StartedAt: Optional[datetime] = None
    Status: Optional[OtaTaskExecutionStatusType] = None


class ScheduleMaintenanceWindowTypeDef(BaseValidatorModel):
    DurationInMinutes: Optional[int] = None
    StartTime: Optional[str] = None


class OtaTaskTimeoutConfigTypeDef(BaseValidatorModel):
    InProgressTimeoutInMinutes: Optional[int] = None


class PutDefaultEncryptionConfigurationRequestTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyArn: Optional[str] = None


class PutHubConfigurationRequestTypeDef(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int


class ResetRuntimeLogConfigurationRequestTypeDef(BaseValidatorModel):
    ManagedThingId: str


class StartDeviceDiscoveryRequestTypeDef(BaseValidatorModel):
    DiscoveryType: DiscoveryTypeType
    ControllerIdentifier: Optional[str] = None
    ConnectorAssociationIdentifier: Optional[str] = None
    AuthenticationMaterial: Optional[str] = None
    AuthenticationMaterialType: Optional[Literal["ZWAVE_INSTALL_CODE"]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateDestinationRequestTypeDef(BaseValidatorModel):
    Name: str
    DeliveryDestinationArn: Optional[str] = None
    DeliveryDestinationType: Optional[Literal["KINESIS"]] = None
    RoleArn: Optional[str] = None
    Description: Optional[str] = None


class UpdateEventLogConfigurationRequestTypeDef(BaseValidatorModel):
    Id: str
    EventLogLevel: LogLevelType


class UpdateNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str


class UpdateOtaTaskRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None
    TaskConfigurationId: Optional[str] = None


class OtaTaskAbortConfigOutputTypeDef(BaseValidatorModel):
    AbortConfigCriteriaList: Optional[List[AbortConfigCriteriaTypeDef]] = None


class OtaTaskAbortConfigTypeDef(BaseValidatorModel):
    AbortConfigCriteriaList: Optional[Sequence[AbortConfigCriteriaTypeDef]] = None


class ConfigurationStatusTypeDef(BaseValidatorModel):
    state: ConfigurationStateType
    error: Optional[ConfigurationErrorTypeDef] = None


class CreateCredentialLockerResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDestinationResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEventLogConfigurationResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateManagedThingResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    EventType: EventTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOtaTaskConfigurationResponseTypeDef(BaseValidatorModel):
    TaskConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOtaTaskResponseTypeDef(BaseValidatorModel):
    TaskId: str
    TaskArn: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProvisioningProfileResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    ClaimCertificatePrivateKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetCredentialLockerResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    Name: str
    CreatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetCustomEndpointResponseTypeDef(BaseValidatorModel):
    EndpointAddress: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDestinationResponseTypeDef(BaseValidatorModel):
    Description: str
    DeliveryDestinationArn: str
    DeliveryDestinationType: Literal["KINESIS"]
    Name: str
    RoleArn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeviceDiscoveryResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    DiscoveryType: DiscoveryTypeType
    Status: DeviceDiscoveryStatusType
    StartedAt: datetime
    ControllerId: str
    ConnectorAssociationId: str
    FinishedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetEventLogConfigurationResponseTypeDef(BaseValidatorModel):
    Id: str
    ResourceType: str
    ResourceId: str
    EventLogLevel: LogLevelType
    ResponseMetadata: ResponseMetadataTypeDef


class GetHubConfigurationResponseTypeDef(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetManagedThingConnectivityDataResponseTypeDef(BaseValidatorModel):
    ManagedThingId: str
    Connected: bool
    Timestamp: datetime
    DisconnectReason: DisconnectReasonValueType
    ResponseMetadata: ResponseMetadataTypeDef


class GetManagedThingMetaDataResponseTypeDef(BaseValidatorModel):
    ManagedThingId: str
    MetaData: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetManagedThingResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    EventType: EventTypeType
    DestinationName: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetProvisioningProfileResponseTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutHubConfigurationResponseTypeDef(BaseValidatorModel):
    HubTokenTimerExpirySettingInSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterCustomEndpointResponseTypeDef(BaseValidatorModel):
    EndpointAddress: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendManagedThingCommandResponseTypeDef(BaseValidatorModel):
    TraceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDeviceDiscoveryResponseTypeDef(BaseValidatorModel):
    Id: str
    StartedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListCredentialLockersResponseTypeDef(BaseValidatorModel):
    Items: List[CredentialLockerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDestinationsResponseTypeDef(BaseValidatorModel):
    DestinationList: List[DestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEventLogConfigurationsResponseTypeDef(BaseValidatorModel):
    EventLogConfigurationList: List[EventLogConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExponentialRolloutRateTypeDef(BaseValidatorModel):
    BaseRatePerMinute: Optional[int] = None
    IncrementFactor: Optional[float] = None
    RateIncreaseCriteria: Optional[RolloutRateIncreaseCriteriaTypeDef] = None


class GetRuntimeLogConfigurationResponseTypeDef(BaseValidatorModel):
    ManagedThingId: str
    RuntimeLogConfigurations: RuntimeLogConfigurationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutRuntimeLogConfigurationRequestTypeDef(BaseValidatorModel):
    ManagedThingId: str
    RuntimeLogConfigurations: RuntimeLogConfigurationsTypeDef


class ListCredentialLockersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDestinationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventLogConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedThingSchemasRequestPaginateTypeDef(BaseValidatorModel):
    Identifier: str
    EndpointIdFilter: Optional[str] = None
    CapabilityIdFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedThingsRequestPaginateTypeDef(BaseValidatorModel):
    OwnerFilter: Optional[str] = None
    CredentialLockerFilter: Optional[str] = None
    RoleFilter: Optional[RoleType] = None
    ParentControllerIdentifierFilter: Optional[str] = None
    ConnectorPolicyIdFilter: Optional[str] = None
    SerialNumberFilter: Optional[str] = None
    ProvisioningStatusFilter: Optional[ProvisioningStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNotificationConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOtaTaskConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOtaTaskExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    Identifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOtaTasksRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisioningProfilesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedThingSchemasResponseTypeDef(BaseValidatorModel):
    Items: List[ManagedThingSchemaListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListManagedThingsResponseTypeDef(BaseValidatorModel):
    Items: List[ManagedThingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListNotificationConfigurationsResponseTypeDef(BaseValidatorModel):
    NotificationConfigurationList: List[NotificationConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListOtaTaskConfigurationsResponseTypeDef(BaseValidatorModel):
    Items: List[OtaTaskConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListOtaTasksResponseTypeDef(BaseValidatorModel):
    Tasks: List[OtaTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProvisioningProfilesResponseTypeDef(BaseValidatorModel):
    Items: List[ProvisioningProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SchemaVersionListItemTypeDef(BaseValidatorModel):
    pass


class ListSchemaVersionsResponseTypeDef(BaseValidatorModel):
    Items: List[SchemaVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class OtaTaskExecutionRetryConfigOutputTypeDef(BaseValidatorModel):
    RetryConfigCriteria: Optional[List[RetryConfigCriteriaTypeDef]] = None


class OtaTaskExecutionRetryConfigTypeDef(BaseValidatorModel):
    RetryConfigCriteria: Optional[Sequence[RetryConfigCriteriaTypeDef]] = None


class OtaTaskExecutionSummariesTypeDef(BaseValidatorModel):
    TaskExecutionSummary: Optional[OtaTaskExecutionSummaryTypeDef] = None
    ManagedThingId: Optional[str] = None


class OtaTaskSchedulingConfigOutputTypeDef(BaseValidatorModel):
    EndBehavior: Optional[SchedulingConfigEndBehaviorType] = None
    EndTime: Optional[str] = None
    MaintenanceWindows: Optional[List[ScheduleMaintenanceWindowTypeDef]] = None
    StartTime: Optional[str] = None


class OtaTaskSchedulingConfigTypeDef(BaseValidatorModel):
    EndBehavior: Optional[SchedulingConfigEndBehaviorType] = None
    EndTime: Optional[str] = None
    MaintenanceWindows: Optional[Sequence[ScheduleMaintenanceWindowTypeDef]] = None
    StartTime: Optional[str] = None


class StateCapabilityTypeDef(BaseValidatorModel):
    pass


class StateEndpointTypeDef(BaseValidatorModel):
    endpointId: str
    capabilities: List[StateCapabilityTypeDef]


class CommandCapabilityTypeDef(BaseValidatorModel):
    pass


class CommandEndpointTypeDef(BaseValidatorModel):
    endpointId: str
    capabilities: Sequence[CommandCapabilityTypeDef]


class CapabilityReportEndpointOutputTypeDef(BaseValidatorModel):
    pass


class CapabilityReportOutputTypeDef(BaseValidatorModel):
    version: str
    endpoints: List[CapabilityReportEndpointOutputTypeDef]
    nodeId: Optional[str] = None


class CapabilityReportEndpointTypeDef(BaseValidatorModel):
    pass


class CapabilityReportTypeDef(BaseValidatorModel):
    version: str
    endpoints: Sequence[CapabilityReportEndpointTypeDef]
    nodeId: Optional[str] = None


class GetDefaultEncryptionConfigurationResponseTypeDef(BaseValidatorModel):
    configurationStatus: ConfigurationStatusTypeDef
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutDefaultEncryptionConfigurationResponseTypeDef(BaseValidatorModel):
    configurationStatus: ConfigurationStatusTypeDef
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class OtaTaskExecutionRolloutConfigTypeDef(BaseValidatorModel):
    ExponentialRolloutRate: Optional[ExponentialRolloutRateTypeDef] = None
    MaximumPerMinute: Optional[int] = None


class ListOtaTaskExecutionsResponseTypeDef(BaseValidatorModel):
    ExecutionSummaries: List[OtaTaskExecutionSummariesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetManagedThingStateResponseTypeDef(BaseValidatorModel):
    Endpoints: List[StateEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SendManagedThingCommandRequestTypeDef(BaseValidatorModel):
    ManagedThingId: str
    Endpoints: Sequence[CommandEndpointTypeDef]
    ConnectorAssociationId: Optional[str] = None


class GetManagedThingCapabilitiesResponseTypeDef(BaseValidatorModel):
    ManagedThingId: str
    Capabilities: str
    CapabilityReport: CapabilityReportOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PushConfigOutputTypeDef(BaseValidatorModel):
    AbortConfig: Optional[OtaTaskAbortConfigOutputTypeDef] = None
    RolloutConfig: Optional[OtaTaskExecutionRolloutConfigTypeDef] = None
    TimeoutConfig: Optional[OtaTaskTimeoutConfigTypeDef] = None


class PushConfigTypeDef(BaseValidatorModel):
    AbortConfig: Optional[OtaTaskAbortConfigTypeDef] = None
    RolloutConfig: Optional[OtaTaskExecutionRolloutConfigTypeDef] = None
    TimeoutConfig: Optional[OtaTaskTimeoutConfigTypeDef] = None


class CapabilityReportUnionTypeDef(BaseValidatorModel):
    pass


class CreateManagedThingRequestTypeDef(BaseValidatorModel):
    Role: RoleType
    AuthenticationMaterial: str
    AuthenticationMaterialType: AuthMaterialTypeType
    Owner: Optional[str] = None
    CredentialLockerId: Optional[str] = None
    SerialNumber: Optional[str] = None
    Brand: Optional[str] = None
    Model: Optional[str] = None
    Name: Optional[str] = None
    CapabilityReport: Optional[CapabilityReportUnionTypeDef] = None
    Capabilities: Optional[str] = None
    ClientToken: Optional[str] = None
    Classification: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    MetaData: Optional[Mapping[str, str]] = None


class UpdateManagedThingRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Owner: Optional[str] = None
    CredentialLockerId: Optional[str] = None
    SerialNumber: Optional[str] = None
    Brand: Optional[str] = None
    Model: Optional[str] = None
    Name: Optional[str] = None
    CapabilityReport: Optional[CapabilityReportUnionTypeDef] = None
    Capabilities: Optional[str] = None
    Classification: Optional[str] = None
    HubNetworkMode: Optional[HubNetworkModeType] = None
    MetaData: Optional[Mapping[str, str]] = None


class GetOtaTaskConfigurationResponseTypeDef(BaseValidatorModel):
    TaskConfigurationId: str
    Name: str
    PushConfig: PushConfigOutputTypeDef
    Description: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PushConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateOtaTaskConfigurationRequestTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    PushConfig: Optional[PushConfigUnionTypeDef] = None
    ClientToken: Optional[str] = None


