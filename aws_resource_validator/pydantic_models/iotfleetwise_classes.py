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
from aws_resource_validator.pydantic_models.iotfleetwise_constants import *

class AssociateVehicleFleetRequest(BaseValidatorModel):
    vehicleName: str
    fleetId: str


class CreateVehicleError(BaseValidatorModel):
    vehicleName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None


class CreateVehicleResponseItem(BaseValidatorModel):
    vehicleName: Optional[str] = None
    arn: Optional[str] = None
    thingArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UpdateVehicleError(BaseValidatorModel):
    vehicleName: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None


class UpdateVehicleResponseItem(BaseValidatorModel):
    vehicleName: Optional[str] = None
    arn: Optional[str] = None


class Branch(BaseValidatorModel):
    fullyQualifiedName: str
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None


class CampaignSummary(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[CampaignStatusType] = None


class CanInterface(BaseValidatorModel):
    name: str
    protocolName: Optional[str] = None
    protocolVersion: Optional[str] = None


class CanSignal(BaseValidatorModel):
    messageId: int
    isBigEndian: bool
    isSigned: bool
    startBit: int
    offset: float
    factor: float
    length: int
    name: Optional[str] = None
    signalValueType: Optional[SignalValueTypeType] = None


class CloudWatchLogDeliveryOptions(BaseValidatorModel):
    logType: LogTypeType
    logGroupName: Optional[str] = None


class ConditionBasedCollectionScheme(BaseValidatorModel):
    expression: str
    minimumTriggerIntervalMs: Optional[int] = None
    triggerMode: Optional[TriggerModeType] = None
    conditionLanguageVersion: Optional[int] = None


class TimeBasedCollectionScheme(BaseValidatorModel):
    periodMs: int


class ConditionBasedSignalFetchConfig(BaseValidatorModel):
    conditionExpression: str
    triggerMode: TriggerModeType


class SignalInformation(BaseValidatorModel):
    name: str
    maxSampleCount: Optional[int] = None
    minimumSamplingIntervalMs: Optional[int] = None
    dataPartitionId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CustomDecodingInterface(BaseValidatorModel):
    name: str


class CustomProperty(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    dataEncoding: Optional[NodeDataEncodingType] = None
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None


class CustomStruct(BaseValidatorModel):
    fullyQualifiedName: str
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None


class MqttTopicConfig(BaseValidatorModel):
    mqttTopicArn: str
    executionRoleArn: str


class S3Config(BaseValidatorModel):
    bucketArn: str
    dataFormat: Optional[DataFormatType] = None
    storageCompressionFormat: Optional[StorageCompressionFormatType] = None
    prefix: Optional[str] = None


class TimestreamConfig(BaseValidatorModel):
    timestreamTableArn: str
    executionRoleArn: str


class StorageMaximumSize(BaseValidatorModel):
    unit: StorageMaximumSizeUnitType
    value: int


class StorageMinimumTimeToLive(BaseValidatorModel):
    unit: StorageMinimumTimeToLiveUnitType
    value: int


class DataPartitionUploadOptions(BaseValidatorModel):
    expression: str
    conditionLanguageVersion: Optional[int] = None


class DecoderManifestSummary(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    modelManifestArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None
    message: Optional[str] = None


class DeleteCampaignRequest(BaseValidatorModel):
    name: str


class DeleteDecoderManifestRequest(BaseValidatorModel):
    name: str


class DeleteFleetRequest(BaseValidatorModel):
    fleetId: str


class DeleteModelManifestRequest(BaseValidatorModel):
    name: str


class DeleteSignalCatalogRequest(BaseValidatorModel):
    name: str


class DeleteStateTemplateRequest(BaseValidatorModel):
    identifier: str


class DeleteVehicleRequest(BaseValidatorModel):
    vehicleName: str


class DisassociateVehicleFleetRequest(BaseValidatorModel):
    vehicleName: str
    fleetId: str


class FormattedVss(BaseValidatorModel):
    vssJson: Optional[str] = None


class GetCampaignRequest(BaseValidatorModel):
    name: str


class GetDecoderManifestRequest(BaseValidatorModel):
    name: str


class GetFleetRequest(BaseValidatorModel):
    fleetId: str


class GetModelManifestRequest(BaseValidatorModel):
    name: str


class IamRegistrationResponse(BaseValidatorModel):
    roleArn: str
    registrationStatus: RegistrationStatusType
    errorMessage: Optional[str] = None


class TimestreamRegistrationResponse(BaseValidatorModel):
    timestreamDatabaseName: str
    timestreamTableName: str
    registrationStatus: RegistrationStatusType
    timestreamDatabaseArn: Optional[str] = None
    timestreamTableArn: Optional[str] = None
    errorMessage: Optional[str] = None


class GetSignalCatalogRequest(BaseValidatorModel):
    name: str


class NodeCounts(BaseValidatorModel):
    totalNodes: Optional[int] = None
    totalBranches: Optional[int] = None
    totalSensors: Optional[int] = None
    totalAttributes: Optional[int] = None
    totalActuators: Optional[int] = None
    totalStructs: Optional[int] = None
    totalProperties: Optional[int] = None


class GetStateTemplateRequest(BaseValidatorModel):
    identifier: str


class GetVehicleRequest(BaseValidatorModel):
    vehicleName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetVehicleStatusRequest(BaseValidatorModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VehicleStatus(BaseValidatorModel):
    campaignName: Optional[str] = None
    vehicleName: Optional[str] = None
    status: Optional[VehicleStateType] = None


class IamResources(BaseValidatorModel):
    roleArn: str


class ListCampaignsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListDecoderManifestNetworkInterfacesRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDecoderManifestSignalsRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDecoderManifestsRequest(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListFleetsForVehicleRequest(BaseValidatorModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFleetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListModelManifestNodesRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListModelManifestsRequest(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ModelManifestSummary(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None


class ListSignalCatalogNodesRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    signalNodeType: Optional[SignalNodeTypeType] = None


class ListSignalCatalogsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SignalCatalogSummary(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastModificationTime: Optional[datetime] = None


class ListStateTemplatesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class ListVehiclesInFleetRequest(BaseValidatorModel):
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListVehiclesRequest(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class VehicleSummary(BaseValidatorModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    creationTime: datetime
    lastModificationTime: datetime
    attributes: Optional[Dict[str, str]] = None


class ObdInterface(BaseValidatorModel):
    name: str
    requestMessageId: int
    obdStandard: Optional[str] = None
    pidRequestIntervalSeconds: Optional[int] = None
    dtcRequestIntervalSeconds: Optional[int] = None
    useExtendedIds: Optional[bool] = None
    hasTransmissionEcu: Optional[bool] = None


class VehicleMiddleware(BaseValidatorModel):
    name: str
    protocolName: Literal["ROS_2"]


class ObdSignal(BaseValidatorModel):
    pidResponseLength: int
    serviceMode: int
    pid: int
    scaling: float
    offset: float
    startByte: int
    byteLength: int
    bitRightShift: Optional[int] = None
    bitMaskLength: Optional[int] = None
    isSigned: Optional[bool] = None
    signalValueType: Optional[SignalValueTypeType] = None


class TimePeriod(BaseValidatorModel):
    unit: TimeUnitType
    value: int


class ROS2PrimitiveMessageDefinition(BaseValidatorModel):
    primitiveType: ROS2PrimitiveTypeType
    offset: Optional[float] = None
    scaling: Optional[float] = None
    upperBound: Optional[int] = None


class PutEncryptionConfigurationRequest(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None


class TimestreamResources(BaseValidatorModel):
    timestreamDatabaseName: str
    timestreamTableName: str


class TimeBasedSignalFetchConfig(BaseValidatorModel):
    executionFrequencyMs: int


class StructuredMessageFieldNameAndDataTypePairOutput(BaseValidatorModel):
    fieldName: str
    dataType: Dict[str, Any]


class StructuredMessageFieldNameAndDataTypePairPaginator(BaseValidatorModel):
    fieldName: str
    dataType: Dict[str, Any]


class StructuredMessageFieldNameAndDataTypePair(BaseValidatorModel):
    fieldName: str
    dataType: Mapping[str, Any]


class StructuredMessageListDefinitionOutput(BaseValidatorModel):
    name: str
    memberType: Dict[str, Any]
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None


class StructuredMessageListDefinitionPaginator(BaseValidatorModel):
    name: str
    memberType: Dict[str, Any]
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None


class StructuredMessageListDefinition(BaseValidatorModel):
    name: str
    memberType: Mapping[str, Any]
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateCampaignRequest(BaseValidatorModel):
    name: str
    action: UpdateCampaignActionType
    description: Optional[str] = None
    dataExtraDimensions: Optional[Sequence[str]] = None


class UpdateFleetRequest(BaseValidatorModel):
    fleetId: str
    description: Optional[str] = None


class UpdateModelManifestRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[str]] = None
    nodesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None


class UpdateStateTemplateRequest(BaseValidatorModel):
    identifier: str
    description: Optional[str] = None
    stateTemplatePropertiesToAdd: Optional[Sequence[str]] = None
    stateTemplatePropertiesToRemove: Optional[Sequence[str]] = None
    dataExtraDimensions: Optional[Sequence[str]] = None
    metadataExtraDimensions: Optional[Sequence[str]] = None


class BatchCreateVehicleResponse(BaseValidatorModel):
    vehicles: List[CreateVehicleResponseItem]
    errors: List[CreateVehicleError]
    ResponseMetadata: ResponseMetadata


class CreateCampaignResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class CreateVehicleResponse(BaseValidatorModel):
    vehicleName: str
    arn: str
    thingArn: str
    ResponseMetadata: ResponseMetadata


class DeleteCampaignResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class DeleteDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class DeleteModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class DeleteSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class DeleteVehicleResponse(BaseValidatorModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadata


class GetDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    description: str
    modelManifestArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    message: str
    ResponseMetadata: ResponseMetadata


class GetEncryptionConfigurationResponse(BaseValidatorModel):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    errorMessage: str
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class GetModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class ImportDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class ImportSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class ListFleetsForVehicleResponse(BaseValidatorModel):
    fleets: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListVehiclesInFleetResponse(BaseValidatorModel):
    vehicles: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutEncryptionConfigurationResponse(BaseValidatorModel):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadata


class UpdateCampaignResponse(BaseValidatorModel):
    arn: str
    name: str
    status: CampaignStatusType
    ResponseMetadata: ResponseMetadata


class UpdateDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class UpdateModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class UpdateSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class UpdateVehicleResponse(BaseValidatorModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadata


class BatchUpdateVehicleResponse(BaseValidatorModel):
    vehicles: List[UpdateVehicleResponseItem]
    errors: List[UpdateVehicleError]
    ResponseMetadata: ResponseMetadata


class Blob(BaseValidatorModel):
    pass


class CanDbcDefinition(BaseValidatorModel):
    networkInterface: str
    canDbcFiles: Sequence[Blob]
    signalsMap: Optional[Mapping[str, str]] = None


class ListCampaignsResponse(BaseValidatorModel):
    campaignSummaries: List[CampaignSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetLoggingOptionsResponse(BaseValidatorModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptions
    ResponseMetadata: ResponseMetadata


class PutLoggingOptionsRequest(BaseValidatorModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptions


class CollectionScheme(BaseValidatorModel):
    timeBasedCollectionScheme: Optional[TimeBasedCollectionScheme] = None
    conditionBasedCollectionScheme: Optional[ConditionBasedCollectionScheme] = None


class CreateFleetRequest(BaseValidatorModel):
    fleetId: str
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class CreateModelManifestRequest(BaseValidatorModel):
    name: str
    nodes: Sequence[str]
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class CreateStateTemplateRequest(BaseValidatorModel):
    name: str
    signalCatalogArn: str
    stateTemplateProperties: Sequence[str]
    description: Optional[str] = None
    dataExtraDimensions: Optional[Sequence[str]] = None
    metadataExtraDimensions: Optional[Sequence[str]] = None
    tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class DataDestinationConfig(BaseValidatorModel):
    s3Config: Optional[S3Config] = None
    timestreamConfig: Optional[TimestreamConfig] = None
    mqttTopicConfig: Optional[MqttTopicConfig] = None


class DataPartitionStorageOptions(BaseValidatorModel):
    maximumSize: StorageMaximumSize
    storageLocation: str
    minimumTimeToLive: StorageMinimumTimeToLive


class ListDecoderManifestsResponse(BaseValidatorModel):
    summaries: List[DecoderManifestSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FleetSummary(BaseValidatorModel):
    pass


class ListFleetsResponse(BaseValidatorModel):
    fleetSummaries: List[FleetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImportSignalCatalogRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    vss: Optional[FormattedVss] = None
    tags: Optional[Sequence[Tag]] = None


class GetRegisterAccountStatusResponse(BaseValidatorModel):
    customerAccountId: str
    accountStatus: RegistrationStatusType
    timestreamRegistrationResponse: TimestreamRegistrationResponse
    iamRegistrationResponse: IamRegistrationResponse
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class GetSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    description: str
    nodeCounts: NodeCounts
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class GetVehicleStatusRequestPaginate(BaseValidatorModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCampaignsRequestPaginate(BaseValidatorModel):
    status: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDecoderManifestNetworkInterfacesRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDecoderManifestSignalsRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDecoderManifestsRequestPaginate(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetsForVehicleRequestPaginate(BaseValidatorModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetsRequestPaginate(BaseValidatorModel):
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelManifestNodesRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelManifestsRequestPaginate(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSignalCatalogNodesRequestPaginate(BaseValidatorModel):
    name: str
    signalNodeType: Optional[SignalNodeTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSignalCatalogsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStateTemplatesRequestPaginate(BaseValidatorModel):
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVehiclesInFleetRequestPaginate(BaseValidatorModel):
    fleetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVehiclesRequestPaginate(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetVehicleStatusResponse(BaseValidatorModel):
    campaigns: List[VehicleStatus]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListModelManifestsResponse(BaseValidatorModel):
    summaries: List[ModelManifestSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSignalCatalogsResponse(BaseValidatorModel):
    summaries: List[SignalCatalogSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StateTemplateSummary(BaseValidatorModel):
    pass


class ListStateTemplatesResponse(BaseValidatorModel):
    summaries: List[StateTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListVehiclesResponse(BaseValidatorModel):
    vehicleSummaries: List[VehicleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PeriodicStateTemplateUpdateStrategy(BaseValidatorModel):
    stateTemplateUpdateRate: TimePeriod


class PrimitiveMessageDefinition(BaseValidatorModel):
    ros2PrimitiveMessageDefinition: Optional[ROS2PrimitiveMessageDefinition] = None


class RegisterAccountRequest(BaseValidatorModel):
    timestreamResources: Optional[TimestreamResources] = None
    iamResources: Optional[IamResources] = None


class RegisterAccountResponse(BaseValidatorModel):
    registerAccountStatus: RegistrationStatusType
    timestreamResources: TimestreamResources
    iamResources: IamResources
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class SignalFetchConfig(BaseValidatorModel):
    timeBased: Optional[TimeBasedSignalFetchConfig] = None
    conditionBased: Optional[ConditionBasedSignalFetchConfig] = None


class NetworkFileDefinition(BaseValidatorModel):
    canDbc: Optional[CanDbcDefinition] = None


class NetworkInterface(BaseValidatorModel):
    pass


class ListDecoderManifestNetworkInterfacesResponse(BaseValidatorModel):
    networkInterfaces: List[NetworkInterface]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NodeOutput(BaseValidatorModel):
    pass


class ListModelManifestNodesResponse(BaseValidatorModel):
    nodes: List[NodeOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSignalCatalogNodesResponse(BaseValidatorModel):
    nodes: List[NodeOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StateTemplateUpdateStrategyOutput(BaseValidatorModel):
    periodic: Optional[PeriodicStateTemplateUpdateStrategy] = None
    onChange: Optional[Dict[str, Any]] = None


class StateTemplateUpdateStrategy(BaseValidatorModel):
    periodic: Optional[PeriodicStateTemplateUpdateStrategy] = None
    onChange: Optional[Mapping[str, Any]] = None


class StructuredMessageOutput(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinition] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionOutput] = None
    structuredMessageDefinition: Optional[ List[StructuredMessageFieldNameAndDataTypePairOutput] ] = None


class StructuredMessagePaginator(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinition] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionPaginator] = None
    structuredMessageDefinition: Optional[ List[StructuredMessageFieldNameAndDataTypePairPaginator] ] = None


class SignalFetchInformationOutput(BaseValidatorModel):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfig
    actions: List[str]
    conditionLanguageVersion: Optional[int] = None


class SignalFetchInformation(BaseValidatorModel):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfig
    actions: Sequence[str]
    conditionLanguageVersion: Optional[int] = None


class StructuredMessageFieldNameAndDataTypePairUnion(BaseValidatorModel):
    pass


class StructuredMessageListDefinitionUnion(BaseValidatorModel):
    pass


class StructuredMessage(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinition] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionUnion] = None
    structuredMessageDefinition: Optional[ Sequence[StructuredMessageFieldNameAndDataTypePairUnion] ] = None


class ImportDecoderManifestRequest(BaseValidatorModel):
    name: str
    networkFileDefinitions: Sequence[NetworkFileDefinition]


class StateTemplateAssociationOutput(BaseValidatorModel):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyOutput


class MessageSignalOutput(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessageOutput


class MessageSignalPaginator(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessagePaginator


class DataPartition(BaseValidatorModel):
    pass


class GetCampaignResponse(BaseValidatorModel):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    targetArn: str
    status: CampaignStatusType
    startTime: datetime
    expiryTime: datetime
    postTriggerCollectionDuration: int
    diagnosticsMode: DiagnosticsModeType
    spoolingMode: SpoolingModeType
    compression: CompressionType
    priority: int
    signalsToCollect: List[SignalInformation]
    collectionScheme: CollectionScheme
    dataExtraDimensions: List[str]
    creationTime: datetime
    lastModificationTime: datetime
    dataDestinationConfigs: List[DataDestinationConfig]
    dataPartitions: List[DataPartition]
    signalsToFetch: List[SignalFetchInformationOutput]
    ResponseMetadata: ResponseMetadata


class GetVehicleResponse(BaseValidatorModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Dict[str, str]
    stateTemplates: List[StateTemplateAssociationOutput]
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


class StateTemplateUpdateStrategyUnion(BaseValidatorModel):
    pass


class StateTemplateAssociation(BaseValidatorModel):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyUnion


class NodeUnion(BaseValidatorModel):
    pass


class CreateSignalCatalogRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodes: Optional[Sequence[NodeUnion]] = None
    tags: Optional[Sequence[Tag]] = None


class UpdateSignalCatalogRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[NodeUnion]] = None
    nodesToUpdate: Optional[Sequence[NodeUnion]] = None
    nodesToRemove: Optional[Sequence[str]] = None


class Timestamp(BaseValidatorModel):
    pass


class SignalFetchInformationUnion(BaseValidatorModel):
    pass


class CreateCampaignRequest(BaseValidatorModel):
    name: str
    signalCatalogArn: str
    targetArn: str
    collectionScheme: CollectionScheme
    description: Optional[str] = None
    startTime: Optional[Timestamp] = None
    expiryTime: Optional[Timestamp] = None
    postTriggerCollectionDuration: Optional[int] = None
    diagnosticsMode: Optional[DiagnosticsModeType] = None
    spoolingMode: Optional[SpoolingModeType] = None
    compression: Optional[CompressionType] = None
    priority: Optional[int] = None
    signalsToCollect: Optional[Sequence[SignalInformation]] = None
    dataExtraDimensions: Optional[Sequence[str]] = None
    tags: Optional[Sequence[Tag]] = None
    dataDestinationConfigs: Optional[Sequence[DataDestinationConfig]] = None
    dataPartitions: Optional[Sequence[DataPartition]] = None
    signalsToFetch: Optional[Sequence[SignalFetchInformationUnion]] = None


class StructuredMessageUnion(BaseValidatorModel):
    pass


class MessageSignal(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessageUnion


class SignalDecoderOutput(BaseValidatorModel):
    pass


class ListDecoderManifestSignalsResponse(BaseValidatorModel):
    signalDecoders: List[SignalDecoderOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SignalDecoderPaginator(BaseValidatorModel):
    pass


class ListDecoderManifestSignalsResponsePaginator(BaseValidatorModel):
    signalDecoders: List[SignalDecoderPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StateTemplateAssociationUnion(BaseValidatorModel):
    pass


class CreateVehicleRequestItem(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[Tag]] = None
    stateTemplates: Optional[Sequence[StateTemplateAssociationUnion]] = None


class CreateVehicleRequest(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[Tag]] = None
    stateTemplates: Optional[Sequence[StateTemplateAssociationUnion]] = None


class UpdateVehicleRequestItem(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None
    stateTemplatesToAdd: Optional[Sequence[StateTemplateAssociationUnion]] = None
    stateTemplatesToRemove: Optional[Sequence[str]] = None


class UpdateVehicleRequest(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None
    stateTemplatesToAdd: Optional[Sequence[StateTemplateAssociationUnion]] = None
    stateTemplatesToRemove: Optional[Sequence[str]] = None


class BatchCreateVehicleRequest(BaseValidatorModel):
    vehicles: Sequence[CreateVehicleRequestItem]


class BatchUpdateVehicleRequest(BaseValidatorModel):
    vehicles: Sequence[UpdateVehicleRequestItem]


class SignalDecoderUnion(BaseValidatorModel):
    pass


class CreateDecoderManifestRequest(BaseValidatorModel):
    name: str
    modelManifestArn: str
    description: Optional[str] = None
    signalDecoders: Optional[Sequence[SignalDecoderUnion]] = None
    networkInterfaces: Optional[Sequence[NetworkInterface]] = None
    defaultForUnmappedSignals: Optional[Literal["CUSTOM_DECODING"]] = None
    tags: Optional[Sequence[Tag]] = None


class UpdateDecoderManifestRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    signalDecodersToAdd: Optional[Sequence[SignalDecoderUnion]] = None
    signalDecodersToUpdate: Optional[Sequence[SignalDecoderUnion]] = None
    signalDecodersToRemove: Optional[Sequence[str]] = None
    networkInterfacesToAdd: Optional[Sequence[NetworkInterface]] = None
    networkInterfacesToUpdate: Optional[Sequence[NetworkInterface]] = None
    networkInterfacesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None
    defaultForUnmappedSignals: Optional[Literal["CUSTOM_DECODING"]] = None


