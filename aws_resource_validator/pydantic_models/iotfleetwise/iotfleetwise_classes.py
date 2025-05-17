from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iotfleetwise.iotfleetwise_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActuatorOutput(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[List[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    assignedValue: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None


class Actuator(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[List[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    assignedValue: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None


class AssociateVehicleFleetRequest(BaseValidatorModel):
    vehicleName: str
    fleetId: str


class AttributeOutput(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[List[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    assignedValue: Optional[str] = None
    defaultValue: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None


class Attribute(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[List[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    assignedValue: Optional[str] = None
    defaultValue: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None


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

Blob = Union[str, bytes, IO[Any], StreamingBody]


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

Timestamp = Union[datetime, str]


class CustomDecodingInterface(BaseValidatorModel):
    name: str


class CustomDecodingSignal(BaseValidatorModel):
    id: str


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


# This class is the input for the 'delete_campaign' function.
class DeleteCampaignRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_decoder_manifest' function.
class DeleteDecoderManifestRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_fleet' function.
class DeleteFleetRequest(BaseValidatorModel):
    fleetId: str


# This class is the input for the 'delete_model_manifest' function.
class DeleteModelManifestRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_signal_catalog' function.
class DeleteSignalCatalogRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_state_template' function.
class DeleteStateTemplateRequest(BaseValidatorModel):
    identifier: str


# This class is the input for the 'delete_vehicle' function.
class DeleteVehicleRequest(BaseValidatorModel):
    vehicleName: str


class DisassociateVehicleFleetRequest(BaseValidatorModel):
    vehicleName: str
    fleetId: str


class FleetSummary(BaseValidatorModel):
    id: str
    arn: str
    signalCatalogArn: str
    creationTime: datetime
    description: Optional[str] = None
    lastModificationTime: Optional[datetime] = None


class FormattedVss(BaseValidatorModel):
    vssJson: Optional[str] = None


# This class is the input for the 'get_campaign' function.
class GetCampaignRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'get_decoder_manifest' function.
class GetDecoderManifestRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'get_fleet' function.
class GetFleetRequest(BaseValidatorModel):
    fleetId: str


# This class is the input for the 'get_model_manifest' function.
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


# This class is the input for the 'get_signal_catalog' function.
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


# This class is the input for the 'get_state_template' function.
class GetStateTemplateRequest(BaseValidatorModel):
    identifier: str


# This class is the input for the 'get_vehicle' function.
class GetVehicleRequest(BaseValidatorModel):
    vehicleName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_vehicle_status' function.
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


# This class is the input for the 'list_campaigns' function.
class ListCampaignsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[str] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None


# This class is the input for the 'list_decoder_manifest_network_interfaces' function.
class ListDecoderManifestNetworkInterfacesRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_decoder_manifest_signals' function.
class ListDecoderManifestSignalsRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_decoder_manifests' function.
class ListDecoderManifestsRequest(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None


# This class is the input for the 'list_fleets_for_vehicle' function.
class ListFleetsForVehicleRequest(BaseValidatorModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_fleets' function.
class ListFleetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None


# This class is the input for the 'list_model_manifest_nodes' function.
class ListModelManifestNodesRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_model_manifests' function.
class ListModelManifestsRequest(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None


class ModelManifestSummary(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None


# This class is the input for the 'list_signal_catalog_nodes' function.
class ListSignalCatalogNodesRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    signalNodeType: Optional[SignalNodeTypeType] = None


# This class is the input for the 'list_signal_catalogs' function.
class ListSignalCatalogsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SignalCatalogSummary(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastModificationTime: Optional[datetime] = None


# This class is the input for the 'list_state_templates' function.
class ListStateTemplatesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None


class StateTemplateSummary(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastModificationTime: Optional[datetime] = None
    id: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'list_vehicles_in_fleet' function.
class ListVehiclesInFleetRequest(BaseValidatorModel):
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_vehicles' function.
class ListVehiclesRequest(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[List[str]] = None
    attributeValues: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None


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
    protocolName: Literal['ROS_2']


class SensorOutput(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[List[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None


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


# This class is the input for the 'put_encryption_configuration' function.
class PutEncryptionConfigurationRequest(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None


class TimestreamResources(BaseValidatorModel):
    timestreamDatabaseName: str
    timestreamTableName: str


class Sensor(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[List[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None


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
    dataType: Dict[str, Any]


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
    memberType: Dict[str, Any]
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_campaign' function.
class UpdateCampaignRequest(BaseValidatorModel):
    name: str
    action: UpdateCampaignActionType
    description: Optional[str] = None
    dataExtraDimensions: Optional[List[str]] = None


# This class is the input for the 'update_fleet' function.
class UpdateFleetRequest(BaseValidatorModel):
    fleetId: str
    description: Optional[str] = None


# This class is the input for the 'update_model_manifest' function.
class UpdateModelManifestRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[List[str]] = None
    nodesToRemove: Optional[List[str]] = None
    status: Optional[ManifestStatusType] = None


# This class is the input for the 'update_state_template' function.
class UpdateStateTemplateRequest(BaseValidatorModel):
    identifier: str
    description: Optional[str] = None
    stateTemplatePropertiesToAdd: Optional[List[str]] = None
    stateTemplatePropertiesToRemove: Optional[List[str]] = None
    dataExtraDimensions: Optional[List[str]] = None
    metadataExtraDimensions: Optional[List[str]] = None

ActuatorUnion = Union[Actuator, ActuatorOutput]

AttributeUnion = Union[Attribute, AttributeOutput]


# This class is the output for the 'batch_create_vehicle' function.
class BatchCreateVehicleResponse(BaseValidatorModel):
    vehicles: List[CreateVehicleResponseItem]
    errors: List[CreateVehicleError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_campaign' function.
class CreateCampaignResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_decoder_manifest' function.
class CreateDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_fleet' function.
class CreateFleetResponse(BaseValidatorModel):
    id: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_manifest' function.
class CreateModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_signal_catalog' function.
class CreateSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_state_template' function.
class CreateStateTemplateResponse(BaseValidatorModel):
    name: str
    arn: str
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vehicle' function.
class CreateVehicleResponse(BaseValidatorModel):
    vehicleName: str
    arn: str
    thingArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_campaign' function.
class DeleteCampaignResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_decoder_manifest' function.
class DeleteDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_fleet' function.
class DeleteFleetResponse(BaseValidatorModel):
    id: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_model_manifest' function.
class DeleteModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_signal_catalog' function.
class DeleteSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_state_template' function.
class DeleteStateTemplateResponse(BaseValidatorModel):
    name: str
    arn: str
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vehicle' function.
class DeleteVehicleResponse(BaseValidatorModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_decoder_manifest' function.
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


# This class is the output for the 'get_fleet' function.
class GetFleetResponse(BaseValidatorModel):
    id: str
    arn: str
    description: str
    signalCatalogArn: str
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_model_manifest' function.
class GetModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_state_template' function.
class GetStateTemplateResponse(BaseValidatorModel):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    stateTemplateProperties: List[str]
    dataExtraDimensions: List[str]
    metadataExtraDimensions: List[str]
    creationTime: datetime
    lastModificationTime: datetime
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_decoder_manifest' function.
class ImportDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_signal_catalog' function.
class ImportSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_fleets_for_vehicle' function.
class ListFleetsForVehicleResponse(BaseValidatorModel):
    fleets: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_vehicles_in_fleet' function.
class ListVehiclesInFleetResponse(BaseValidatorModel):
    vehicles: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_encryption_configuration' function.
class PutEncryptionConfigurationResponse(BaseValidatorModel):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_campaign' function.
class UpdateCampaignResponse(BaseValidatorModel):
    arn: str
    name: str
    status: CampaignStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_decoder_manifest' function.
class UpdateDecoderManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_fleet' function.
class UpdateFleetResponse(BaseValidatorModel):
    id: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_model_manifest' function.
class UpdateModelManifestResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_signal_catalog' function.
class UpdateSignalCatalogResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_state_template' function.
class UpdateStateTemplateResponse(BaseValidatorModel):
    name: str
    arn: str
    id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vehicle' function.
class UpdateVehicleResponse(BaseValidatorModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_update_vehicle' function.
class BatchUpdateVehicleResponse(BaseValidatorModel):
    vehicles: List[UpdateVehicleResponseItem]
    errors: List[UpdateVehicleError]
    ResponseMetadata: ResponseMetadata


class CanDbcDefinition(BaseValidatorModel):
    networkInterface: str
    canDbcFiles: List[Blob]
    signalsMap: Optional[Dict[str, str]] = None


# This class is the output for the 'list_campaigns' function.
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


# This class is the input for the 'create_fleet' function.
class CreateFleetRequest(BaseValidatorModel):
    fleetId: str
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_model_manifest' function.
class CreateModelManifestRequest(BaseValidatorModel):
    name: str
    nodes: List[str]
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_state_template' function.
class CreateStateTemplateRequest(BaseValidatorModel):
    name: str
    signalCatalogArn: str
    stateTemplateProperties: List[str]
    description: Optional[str] = None
    dataExtraDimensions: Optional[List[str]] = None
    metadataExtraDimensions: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


class DataDestinationConfig(BaseValidatorModel):
    s3Config: Optional[S3Config] = None
    timestreamConfig: Optional[TimestreamConfig] = None
    mqttTopicConfig: Optional[MqttTopicConfig] = None


class DataPartitionStorageOptions(BaseValidatorModel):
    maximumSize: StorageMaximumSize
    storageLocation: str
    minimumTimeToLive: StorageMinimumTimeToLive


# This class is the output for the 'list_decoder_manifests' function.
class ListDecoderManifestsResponse(BaseValidatorModel):
    summaries: List[DecoderManifestSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_fleets' function.
class ListFleetsResponse(BaseValidatorModel):
    fleetSummaries: List[FleetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'import_signal_catalog' function.
class ImportSignalCatalogRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    vss: Optional[FormattedVss] = None
    tags: Optional[List[Tag]] = None


class GetRegisterAccountStatusResponse(BaseValidatorModel):
    customerAccountId: str
    accountStatus: RegistrationStatusType
    timestreamRegistrationResponse: TimestreamRegistrationResponse
    iamRegistrationResponse: IamRegistrationResponse
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_signal_catalog' function.
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
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDecoderManifestNetworkInterfacesRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDecoderManifestSignalsRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDecoderManifestsRequestPaginate(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetsForVehicleRequestPaginate(BaseValidatorModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetsRequestPaginate(BaseValidatorModel):
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelManifestNodesRequestPaginate(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelManifestsRequestPaginate(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSignalCatalogNodesRequestPaginate(BaseValidatorModel):
    name: str
    signalNodeType: Optional[SignalNodeTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSignalCatalogsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStateTemplatesRequestPaginate(BaseValidatorModel):
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVehiclesInFleetRequestPaginate(BaseValidatorModel):
    fleetId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVehiclesRequestPaginate(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[List[str]] = None
    attributeValues: Optional[List[str]] = None
    listResponseScope: Optional[Literal['METADATA_ONLY']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_vehicle_status' function.
class GetVehicleStatusResponse(BaseValidatorModel):
    campaigns: List[VehicleStatus]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_model_manifests' function.
class ListModelManifestsResponse(BaseValidatorModel):
    summaries: List[ModelManifestSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_signal_catalogs' function.
class ListSignalCatalogsResponse(BaseValidatorModel):
    summaries: List[SignalCatalogSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_state_templates' function.
class ListStateTemplatesResponse(BaseValidatorModel):
    summaries: List[StateTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_vehicles' function.
class ListVehiclesResponse(BaseValidatorModel):
    vehicleSummaries: List[VehicleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    interfaceId: str
    type: NetworkInterfaceTypeType
    canInterface: Optional[CanInterface] = None
    obdInterface: Optional[ObdInterface] = None
    vehicleMiddleware: Optional[VehicleMiddleware] = None
    customDecodingInterface: Optional[CustomDecodingInterface] = None


class NodeOutput(BaseValidatorModel):
    branch: Optional[Branch] = None
    sensor: Optional[SensorOutput] = None
    actuator: Optional[ActuatorOutput] = None
    attribute: Optional[AttributeOutput] = None
    struct: Optional[CustomStruct] = None
    property: Optional[CustomProperty] = None


class PeriodicStateTemplateUpdateStrategy(BaseValidatorModel):
    stateTemplateUpdateRate: TimePeriod


class PrimitiveMessageDefinition(BaseValidatorModel):
    ros2PrimitiveMessageDefinition: Optional[ROS2PrimitiveMessageDefinition] = None


# This class is the input for the 'register_account' function.
class RegisterAccountRequest(BaseValidatorModel):
    timestreamResources: Optional[TimestreamResources] = None
    iamResources: Optional[IamResources] = None


# This class is the output for the 'register_account' function.
class RegisterAccountResponse(BaseValidatorModel):
    registerAccountStatus: RegistrationStatusType
    timestreamResources: TimestreamResources
    iamResources: IamResources
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadata

SensorUnion = Union[Sensor, SensorOutput]


class SignalFetchConfig(BaseValidatorModel):
    timeBased: Optional[TimeBasedSignalFetchConfig] = None
    conditionBased: Optional[ConditionBasedSignalFetchConfig] = None

StructuredMessageFieldNameAndDataTypePairUnion = Union[StructuredMessageFieldNameAndDataTypePair, StructuredMessageFieldNameAndDataTypePairOutput]

StructuredMessageListDefinitionUnion = Union[StructuredMessageListDefinition, StructuredMessageListDefinitionOutput]


class NetworkFileDefinition(BaseValidatorModel):
    canDbc: Optional[CanDbcDefinition] = None


class DataPartition(BaseValidatorModel):
    id: str
    storageOptions: DataPartitionStorageOptions
    uploadOptions: Optional[DataPartitionUploadOptions] = None


# This class is the output for the 'list_decoder_manifest_network_interfaces' function.
class ListDecoderManifestNetworkInterfacesResponse(BaseValidatorModel):
    networkInterfaces: List[NetworkInterface]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_model_manifest_nodes' function.
class ListModelManifestNodesResponse(BaseValidatorModel):
    nodes: List[NodeOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_signal_catalog_nodes' function.
class ListSignalCatalogNodesResponse(BaseValidatorModel):
    nodes: List[NodeOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StateTemplateUpdateStrategyOutput(BaseValidatorModel):
    periodic: Optional[PeriodicStateTemplateUpdateStrategy] = None
    onChange: Optional[Dict[str, Any]] = None


class StateTemplateUpdateStrategy(BaseValidatorModel):
    periodic: Optional[PeriodicStateTemplateUpdateStrategy] = None
    onChange: Optional[Dict[str, Any]] = None


class StructuredMessageOutput(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinition] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionOutput] = None
    structuredMessageDefinition: Optional[List[StructuredMessageFieldNameAndDataTypePairOutput]] = None


class StructuredMessagePaginator(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinition] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionPaginator] = None
    structuredMessageDefinition: Optional[List[StructuredMessageFieldNameAndDataTypePairPaginator]] = None


class Node(BaseValidatorModel):
    branch: Optional[Branch] = None
    sensor: Optional[SensorUnion] = None
    actuator: Optional[ActuatorUnion] = None
    attribute: Optional[AttributeUnion] = None
    struct: Optional[CustomStruct] = None
    property: Optional[CustomProperty] = None


class SignalFetchInformationOutput(BaseValidatorModel):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfig
    actions: List[str]
    conditionLanguageVersion: Optional[int] = None


class SignalFetchInformation(BaseValidatorModel):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfig
    actions: List[str]
    conditionLanguageVersion: Optional[int] = None


class StructuredMessage(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinition] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionUnion] = None
    structuredMessageDefinition: Optional[List[StructuredMessageFieldNameAndDataTypePairUnion]] = None


# This class is the input for the 'import_decoder_manifest' function.
class ImportDecoderManifestRequest(BaseValidatorModel):
    name: str
    networkFileDefinitions: List[NetworkFileDefinition]


class StateTemplateAssociationOutput(BaseValidatorModel):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyOutput

StateTemplateUpdateStrategyUnion = Union[StateTemplateUpdateStrategy, StateTemplateUpdateStrategyOutput]


class MessageSignalOutput(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessageOutput


class MessageSignalPaginator(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessagePaginator

NodeUnion = Union[Node, NodeOutput]


# This class is the output for the 'get_campaign' function.
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

SignalFetchInformationUnion = Union[SignalFetchInformation, SignalFetchInformationOutput]

StructuredMessageUnion = Union[StructuredMessage, StructuredMessageOutput]


# This class is the output for the 'get_vehicle' function.
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


class StateTemplateAssociation(BaseValidatorModel):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyUnion


class SignalDecoderOutput(BaseValidatorModel):
    fullyQualifiedName: str
    type: SignalDecoderTypeType
    interfaceId: str
    canSignal: Optional[CanSignal] = None
    obdSignal: Optional[ObdSignal] = None
    messageSignal: Optional[MessageSignalOutput] = None
    customDecodingSignal: Optional[CustomDecodingSignal] = None


class SignalDecoderPaginator(BaseValidatorModel):
    fullyQualifiedName: str
    type: SignalDecoderTypeType
    interfaceId: str
    canSignal: Optional[CanSignal] = None
    obdSignal: Optional[ObdSignal] = None
    messageSignal: Optional[MessageSignalPaginator] = None
    customDecodingSignal: Optional[CustomDecodingSignal] = None


# This class is the input for the 'create_signal_catalog' function.
class CreateSignalCatalogRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodes: Optional[List[NodeUnion]] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_signal_catalog' function.
class UpdateSignalCatalogRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[List[NodeUnion]] = None
    nodesToUpdate: Optional[List[NodeUnion]] = None
    nodesToRemove: Optional[List[str]] = None


# This class is the input for the 'create_campaign' function.
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
    signalsToCollect: Optional[List[SignalInformation]] = None
    dataExtraDimensions: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None
    dataDestinationConfigs: Optional[List[DataDestinationConfig]] = None
    dataPartitions: Optional[List[DataPartition]] = None
    signalsToFetch: Optional[List[SignalFetchInformationUnion]] = None


class MessageSignal(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessageUnion

StateTemplateAssociationUnion = Union[StateTemplateAssociation, StateTemplateAssociationOutput]


# This class is the output for the 'list_decoder_manifest_signals' function.
class ListDecoderManifestSignalsResponse(BaseValidatorModel):
    signalDecoders: List[SignalDecoderOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDecoderManifestSignalsResponsePaginator(BaseValidatorModel):
    signalDecoders: List[SignalDecoderPaginator]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

MessageSignalUnion = Union[MessageSignal, MessageSignalOutput]


class CreateVehicleRequestItem(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Dict[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[List[Tag]] = None
    stateTemplates: Optional[List[StateTemplateAssociationUnion]] = None


# This class is the input for the 'create_vehicle' function.
class CreateVehicleRequest(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Dict[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[List[Tag]] = None
    stateTemplates: Optional[List[StateTemplateAssociationUnion]] = None


class UpdateVehicleRequestItem(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None
    stateTemplatesToAdd: Optional[List[StateTemplateAssociationUnion]] = None
    stateTemplatesToRemove: Optional[List[str]] = None


# This class is the input for the 'update_vehicle' function.
class UpdateVehicleRequest(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None
    stateTemplatesToAdd: Optional[List[StateTemplateAssociationUnion]] = None
    stateTemplatesToRemove: Optional[List[str]] = None


class SignalDecoder(BaseValidatorModel):
    fullyQualifiedName: str
    type: SignalDecoderTypeType
    interfaceId: str
    canSignal: Optional[CanSignal] = None
    obdSignal: Optional[ObdSignal] = None
    messageSignal: Optional[MessageSignalUnion] = None
    customDecodingSignal: Optional[CustomDecodingSignal] = None


# This class is the input for the 'batch_create_vehicle' function.
class BatchCreateVehicleRequest(BaseValidatorModel):
    vehicles: List[CreateVehicleRequestItem]


# This class is the input for the 'batch_update_vehicle' function.
class BatchUpdateVehicleRequest(BaseValidatorModel):
    vehicles: List[UpdateVehicleRequestItem]

SignalDecoderUnion = Union[SignalDecoder, SignalDecoderOutput]


# This class is the input for the 'create_decoder_manifest' function.
class CreateDecoderManifestRequest(BaseValidatorModel):
    name: str
    modelManifestArn: str
    description: Optional[str] = None
    signalDecoders: Optional[List[SignalDecoderUnion]] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None
    defaultForUnmappedSignals: Optional[Literal['CUSTOM_DECODING']] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_decoder_manifest' function.
class UpdateDecoderManifestRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    signalDecodersToAdd: Optional[List[SignalDecoderUnion]] = None
    signalDecodersToUpdate: Optional[List[SignalDecoderUnion]] = None
    signalDecodersToRemove: Optional[List[str]] = None
    networkInterfacesToAdd: Optional[List[NetworkInterface]] = None
    networkInterfacesToUpdate: Optional[List[NetworkInterface]] = None
    networkInterfacesToRemove: Optional[List[str]] = None
    status: Optional[ManifestStatusType] = None
    defaultForUnmappedSignals: Optional[Literal['CUSTOM_DECODING']] = None