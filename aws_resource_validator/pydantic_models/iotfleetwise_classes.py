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

class AssociateVehicleFleetRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    fleetId: str


class CreateVehicleErrorTypeDef(BaseValidatorModel):
    vehicleName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None


class CreateVehicleResponseItemTypeDef(BaseValidatorModel):
    vehicleName: Optional[str] = None
    arn: Optional[str] = None
    thingArn: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UpdateVehicleErrorTypeDef(BaseValidatorModel):
    vehicleName: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None


class UpdateVehicleResponseItemTypeDef(BaseValidatorModel):
    vehicleName: Optional[str] = None
    arn: Optional[str] = None


class BranchTypeDef(BaseValidatorModel):
    fullyQualifiedName: str
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None


class CampaignSummaryTypeDef(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[CampaignStatusType] = None


class CanInterfaceTypeDef(BaseValidatorModel):
    name: str
    protocolName: Optional[str] = None
    protocolVersion: Optional[str] = None


class CanSignalTypeDef(BaseValidatorModel):
    messageId: int
    isBigEndian: bool
    isSigned: bool
    startBit: int
    offset: float
    factor: float
    length: int
    name: Optional[str] = None
    signalValueType: Optional[SignalValueTypeType] = None


class CloudWatchLogDeliveryOptionsTypeDef(BaseValidatorModel):
    logType: LogTypeType
    logGroupName: Optional[str] = None


class ConditionBasedCollectionSchemeTypeDef(BaseValidatorModel):
    expression: str
    minimumTriggerIntervalMs: Optional[int] = None
    triggerMode: Optional[TriggerModeType] = None
    conditionLanguageVersion: Optional[int] = None


class TimeBasedCollectionSchemeTypeDef(BaseValidatorModel):
    periodMs: int


class ConditionBasedSignalFetchConfigTypeDef(BaseValidatorModel):
    conditionExpression: str
    triggerMode: TriggerModeType


class SignalInformationTypeDef(BaseValidatorModel):
    name: str
    maxSampleCount: Optional[int] = None
    minimumSamplingIntervalMs: Optional[int] = None
    dataPartitionId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CustomDecodingInterfaceTypeDef(BaseValidatorModel):
    name: str


class CustomPropertyTypeDef(BaseValidatorModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    dataEncoding: Optional[NodeDataEncodingType] = None
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None


class CustomStructTypeDef(BaseValidatorModel):
    fullyQualifiedName: str
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None


class MqttTopicConfigTypeDef(BaseValidatorModel):
    mqttTopicArn: str
    executionRoleArn: str


class S3ConfigTypeDef(BaseValidatorModel):
    bucketArn: str
    dataFormat: Optional[DataFormatType] = None
    storageCompressionFormat: Optional[StorageCompressionFormatType] = None
    prefix: Optional[str] = None


class TimestreamConfigTypeDef(BaseValidatorModel):
    timestreamTableArn: str
    executionRoleArn: str


class StorageMaximumSizeTypeDef(BaseValidatorModel):
    unit: StorageMaximumSizeUnitType
    value: int


class StorageMinimumTimeToLiveTypeDef(BaseValidatorModel):
    unit: StorageMinimumTimeToLiveUnitType
    value: int


class DataPartitionUploadOptionsTypeDef(BaseValidatorModel):
    expression: str
    conditionLanguageVersion: Optional[int] = None


class DecoderManifestSummaryTypeDef(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    modelManifestArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None
    message: Optional[str] = None


class DeleteCampaignRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteDecoderManifestRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteFleetRequestTypeDef(BaseValidatorModel):
    fleetId: str


class DeleteModelManifestRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteSignalCatalogRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteStateTemplateRequestTypeDef(BaseValidatorModel):
    identifier: str


class DeleteVehicleRequestTypeDef(BaseValidatorModel):
    vehicleName: str


class DisassociateVehicleFleetRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    fleetId: str


class FormattedVssTypeDef(BaseValidatorModel):
    vssJson: Optional[str] = None


class GetCampaignRequestTypeDef(BaseValidatorModel):
    name: str


class GetDecoderManifestRequestTypeDef(BaseValidatorModel):
    name: str


class GetFleetRequestTypeDef(BaseValidatorModel):
    fleetId: str


class GetModelManifestRequestTypeDef(BaseValidatorModel):
    name: str


class IamRegistrationResponseTypeDef(BaseValidatorModel):
    roleArn: str
    registrationStatus: RegistrationStatusType
    errorMessage: Optional[str] = None


class TimestreamRegistrationResponseTypeDef(BaseValidatorModel):
    timestreamDatabaseName: str
    timestreamTableName: str
    registrationStatus: RegistrationStatusType
    timestreamDatabaseArn: Optional[str] = None
    timestreamTableArn: Optional[str] = None
    errorMessage: Optional[str] = None


class GetSignalCatalogRequestTypeDef(BaseValidatorModel):
    name: str


class NodeCountsTypeDef(BaseValidatorModel):
    totalNodes: Optional[int] = None
    totalBranches: Optional[int] = None
    totalSensors: Optional[int] = None
    totalAttributes: Optional[int] = None
    totalActuators: Optional[int] = None
    totalStructs: Optional[int] = None
    totalProperties: Optional[int] = None


class GetStateTemplateRequestTypeDef(BaseValidatorModel):
    identifier: str


class GetVehicleRequestTypeDef(BaseValidatorModel):
    vehicleName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetVehicleStatusRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VehicleStatusTypeDef(BaseValidatorModel):
    campaignName: Optional[str] = None
    vehicleName: Optional[str] = None
    status: Optional[VehicleStateType] = None


class IamResourcesTypeDef(BaseValidatorModel):
    roleArn: str


class ListCampaignsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListDecoderManifestNetworkInterfacesRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDecoderManifestSignalsRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDecoderManifestsRequestTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListFleetsForVehicleRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFleetsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListModelManifestNodesRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListModelManifestsRequestTypeDef(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ModelManifestSummaryTypeDef(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None


class ListSignalCatalogNodesRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    signalNodeType: Optional[SignalNodeTypeType] = None


class ListSignalCatalogsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SignalCatalogSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastModificationTime: Optional[datetime] = None


class ListStateTemplatesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class ListVehiclesInFleetRequestTypeDef(BaseValidatorModel):
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListVehiclesRequestTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None


class VehicleSummaryTypeDef(BaseValidatorModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    creationTime: datetime
    lastModificationTime: datetime
    attributes: Optional[Dict[str, str]] = None


class ObdInterfaceTypeDef(BaseValidatorModel):
    name: str
    requestMessageId: int
    obdStandard: Optional[str] = None
    pidRequestIntervalSeconds: Optional[int] = None
    dtcRequestIntervalSeconds: Optional[int] = None
    useExtendedIds: Optional[bool] = None
    hasTransmissionEcu: Optional[bool] = None


class VehicleMiddlewareTypeDef(BaseValidatorModel):
    name: str
    protocolName: Literal["ROS_2"]


class ObdSignalTypeDef(BaseValidatorModel):
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


class TimePeriodTypeDef(BaseValidatorModel):
    unit: TimeUnitType
    value: int


class ROS2PrimitiveMessageDefinitionTypeDef(BaseValidatorModel):
    primitiveType: ROS2PrimitiveTypeType
    offset: Optional[float] = None
    scaling: Optional[float] = None
    upperBound: Optional[int] = None


class PutEncryptionConfigurationRequestTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None


class TimestreamResourcesTypeDef(BaseValidatorModel):
    timestreamDatabaseName: str
    timestreamTableName: str


class TimeBasedSignalFetchConfigTypeDef(BaseValidatorModel):
    executionFrequencyMs: int


class StructuredMessageFieldNameAndDataTypePairOutputTypeDef(BaseValidatorModel):
    fieldName: str
    dataType: Dict[str, Any]


class StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef(BaseValidatorModel):
    fieldName: str
    dataType: Dict[str, Any]


class StructuredMessageFieldNameAndDataTypePairTypeDef(BaseValidatorModel):
    fieldName: str
    dataType: Mapping[str, Any]


class StructuredMessageListDefinitionOutputTypeDef(BaseValidatorModel):
    name: str
    memberType: Dict[str, Any]
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None


class StructuredMessageListDefinitionPaginatorTypeDef(BaseValidatorModel):
    name: str
    memberType: Dict[str, Any]
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None


class StructuredMessageListDefinitionTypeDef(BaseValidatorModel):
    name: str
    memberType: Mapping[str, Any]
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateCampaignRequestTypeDef(BaseValidatorModel):
    name: str
    action: UpdateCampaignActionType
    description: Optional[str] = None
    dataExtraDimensions: Optional[Sequence[str]] = None


class UpdateFleetRequestTypeDef(BaseValidatorModel):
    fleetId: str
    description: Optional[str] = None


class UpdateModelManifestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[str]] = None
    nodesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None


class UpdateStateTemplateRequestTypeDef(BaseValidatorModel):
    identifier: str
    description: Optional[str] = None
    stateTemplatePropertiesToAdd: Optional[Sequence[str]] = None
    stateTemplatePropertiesToRemove: Optional[Sequence[str]] = None
    dataExtraDimensions: Optional[Sequence[str]] = None
    metadataExtraDimensions: Optional[Sequence[str]] = None


class BatchCreateVehicleResponseTypeDef(BaseValidatorModel):
    vehicles: List[CreateVehicleResponseItemTypeDef]
    errors: List[CreateVehicleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCampaignResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDecoderManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSignalCatalogResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVehicleResponseTypeDef(BaseValidatorModel):
    vehicleName: str
    arn: str
    thingArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCampaignResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDecoderManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteModelManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSignalCatalogResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVehicleResponseTypeDef(BaseValidatorModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDecoderManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    description: str
    modelManifestArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    message: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetEncryptionConfigurationResponseTypeDef(BaseValidatorModel):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    errorMessage: str
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetModelManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ImportDecoderManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportSignalCatalogResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListFleetsForVehicleResponseTypeDef(BaseValidatorModel):
    fleets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListVehiclesInFleetResponseTypeDef(BaseValidatorModel):
    vehicles: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutEncryptionConfigurationResponseTypeDef(BaseValidatorModel):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCampaignResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    status: CampaignStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDecoderManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateModelManifestResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSignalCatalogResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVehicleResponseTypeDef(BaseValidatorModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdateVehicleResponseTypeDef(BaseValidatorModel):
    vehicles: List[UpdateVehicleResponseItemTypeDef]
    errors: List[UpdateVehicleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class CanDbcDefinitionTypeDef(BaseValidatorModel):
    networkInterface: str
    canDbcFiles: Sequence[BlobTypeDef]
    signalsMap: Optional[Mapping[str, str]] = None


class ListCampaignsResponseTypeDef(BaseValidatorModel):
    campaignSummaries: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetLoggingOptionsResponseTypeDef(BaseValidatorModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutLoggingOptionsRequestTypeDef(BaseValidatorModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef


class CollectionSchemeTypeDef(BaseValidatorModel):
    timeBasedCollectionScheme: Optional[TimeBasedCollectionSchemeTypeDef] = None
    conditionBasedCollectionScheme: Optional[ConditionBasedCollectionSchemeTypeDef] = None


class CreateFleetRequestTypeDef(BaseValidatorModel):
    fleetId: str
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateModelManifestRequestTypeDef(BaseValidatorModel):
    name: str
    nodes: Sequence[str]
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateStateTemplateRequestTypeDef(BaseValidatorModel):
    name: str
    signalCatalogArn: str
    stateTemplateProperties: Sequence[str]
    description: Optional[str] = None
    dataExtraDimensions: Optional[Sequence[str]] = None
    metadataExtraDimensions: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class DataDestinationConfigTypeDef(BaseValidatorModel):
    s3Config: Optional[S3ConfigTypeDef] = None
    timestreamConfig: Optional[TimestreamConfigTypeDef] = None
    mqttTopicConfig: Optional[MqttTopicConfigTypeDef] = None


class DataPartitionStorageOptionsTypeDef(BaseValidatorModel):
    maximumSize: StorageMaximumSizeTypeDef
    storageLocation: str
    minimumTimeToLive: StorageMinimumTimeToLiveTypeDef


class ListDecoderManifestsResponseTypeDef(BaseValidatorModel):
    summaries: List[DecoderManifestSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FleetSummaryTypeDef(BaseValidatorModel):
    pass


class ListFleetsResponseTypeDef(BaseValidatorModel):
    fleetSummaries: List[FleetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ImportSignalCatalogRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    vss: Optional[FormattedVssTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class GetRegisterAccountStatusResponseTypeDef(BaseValidatorModel):
    customerAccountId: str
    accountStatus: RegistrationStatusType
    timestreamRegistrationResponse: TimestreamRegistrationResponseTypeDef
    iamRegistrationResponse: IamRegistrationResponseTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetSignalCatalogResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    description: str
    nodeCounts: NodeCountsTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetVehicleStatusRequestPaginateTypeDef(BaseValidatorModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCampaignsRequestPaginateTypeDef(BaseValidatorModel):
    status: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDecoderManifestNetworkInterfacesRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDecoderManifestSignalsRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDecoderManifestsRequestPaginateTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFleetsForVehicleRequestPaginateTypeDef(BaseValidatorModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFleetsRequestPaginateTypeDef(BaseValidatorModel):
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListModelManifestNodesRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListModelManifestsRequestPaginateTypeDef(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSignalCatalogNodesRequestPaginateTypeDef(BaseValidatorModel):
    name: str
    signalNodeType: Optional[SignalNodeTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSignalCatalogsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStateTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVehiclesInFleetRequestPaginateTypeDef(BaseValidatorModel):
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVehiclesRequestPaginateTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    listResponseScope: Optional[Literal["METADATA_ONLY"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetVehicleStatusResponseTypeDef(BaseValidatorModel):
    campaigns: List[VehicleStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListModelManifestsResponseTypeDef(BaseValidatorModel):
    summaries: List[ModelManifestSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSignalCatalogsResponseTypeDef(BaseValidatorModel):
    summaries: List[SignalCatalogSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StateTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListStateTemplatesResponseTypeDef(BaseValidatorModel):
    summaries: List[StateTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListVehiclesResponseTypeDef(BaseValidatorModel):
    vehicleSummaries: List[VehicleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PeriodicStateTemplateUpdateStrategyTypeDef(BaseValidatorModel):
    stateTemplateUpdateRate: TimePeriodTypeDef


class PrimitiveMessageDefinitionTypeDef(BaseValidatorModel):
    ros2PrimitiveMessageDefinition: Optional[ROS2PrimitiveMessageDefinitionTypeDef] = None


class RegisterAccountRequestTypeDef(BaseValidatorModel):
    timestreamResources: Optional[TimestreamResourcesTypeDef] = None
    iamResources: Optional[IamResourcesTypeDef] = None


class RegisterAccountResponseTypeDef(BaseValidatorModel):
    registerAccountStatus: RegistrationStatusType
    timestreamResources: TimestreamResourcesTypeDef
    iamResources: IamResourcesTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class SignalFetchConfigTypeDef(BaseValidatorModel):
    timeBased: Optional[TimeBasedSignalFetchConfigTypeDef] = None
    conditionBased: Optional[ConditionBasedSignalFetchConfigTypeDef] = None


class NetworkFileDefinitionTypeDef(BaseValidatorModel):
    canDbc: Optional[CanDbcDefinitionTypeDef] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    pass


class ListDecoderManifestNetworkInterfacesResponseTypeDef(BaseValidatorModel):
    networkInterfaces: List[NetworkInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NodeOutputTypeDef(BaseValidatorModel):
    pass


class ListModelManifestNodesResponseTypeDef(BaseValidatorModel):
    nodes: List[NodeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSignalCatalogNodesResponseTypeDef(BaseValidatorModel):
    nodes: List[NodeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StateTemplateUpdateStrategyOutputTypeDef(BaseValidatorModel):
    periodic: Optional[PeriodicStateTemplateUpdateStrategyTypeDef] = None
    onChange: Optional[Dict[str, Any]] = None


class StateTemplateUpdateStrategyTypeDef(BaseValidatorModel):
    periodic: Optional[PeriodicStateTemplateUpdateStrategyTypeDef] = None
    onChange: Optional[Mapping[str, Any]] = None


class StructuredMessageOutputTypeDef(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinitionTypeDef] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionOutputTypeDef] = None
    structuredMessageDefinition: Optional[ List[StructuredMessageFieldNameAndDataTypePairOutputTypeDef] ] = None


class StructuredMessagePaginatorTypeDef(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinitionTypeDef] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionPaginatorTypeDef] = None
    structuredMessageDefinition: Optional[ List[StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef] ] = None


class SignalFetchInformationOutputTypeDef(BaseValidatorModel):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfigTypeDef
    actions: List[str]
    conditionLanguageVersion: Optional[int] = None


class SignalFetchInformationTypeDef(BaseValidatorModel):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfigTypeDef
    actions: Sequence[str]
    conditionLanguageVersion: Optional[int] = None


class StructuredMessageFieldNameAndDataTypePairUnionTypeDef(BaseValidatorModel):
    pass


class StructuredMessageListDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class StructuredMessageTypeDef(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinitionTypeDef] = None
    structuredMessageListDefinition: Optional[StructuredMessageListDefinitionUnionTypeDef] = None
    structuredMessageDefinition: Optional[ Sequence[StructuredMessageFieldNameAndDataTypePairUnionTypeDef] ] = None


class ImportDecoderManifestRequestTypeDef(BaseValidatorModel):
    name: str
    networkFileDefinitions: Sequence[NetworkFileDefinitionTypeDef]


class StateTemplateAssociationOutputTypeDef(BaseValidatorModel):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyOutputTypeDef


class MessageSignalOutputTypeDef(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessageOutputTypeDef


class MessageSignalPaginatorTypeDef(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessagePaginatorTypeDef


class DataPartitionTypeDef(BaseValidatorModel):
    pass


class GetCampaignResponseTypeDef(BaseValidatorModel):
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
    signalsToCollect: List[SignalInformationTypeDef]
    collectionScheme: CollectionSchemeTypeDef
    dataExtraDimensions: List[str]
    creationTime: datetime
    lastModificationTime: datetime
    dataDestinationConfigs: List[DataDestinationConfigTypeDef]
    dataPartitions: List[DataPartitionTypeDef]
    signalsToFetch: List[SignalFetchInformationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetVehicleResponseTypeDef(BaseValidatorModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Dict[str, str]
    stateTemplates: List[StateTemplateAssociationOutputTypeDef]
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class StateTemplateUpdateStrategyUnionTypeDef(BaseValidatorModel):
    pass


class StateTemplateAssociationTypeDef(BaseValidatorModel):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyUnionTypeDef


class NodeUnionTypeDef(BaseValidatorModel):
    pass


class CreateSignalCatalogRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodes: Optional[Sequence[NodeUnionTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateSignalCatalogRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[NodeUnionTypeDef]] = None
    nodesToUpdate: Optional[Sequence[NodeUnionTypeDef]] = None
    nodesToRemove: Optional[Sequence[str]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class SignalFetchInformationUnionTypeDef(BaseValidatorModel):
    pass


class CreateCampaignRequestTypeDef(BaseValidatorModel):
    name: str
    signalCatalogArn: str
    targetArn: str
    collectionScheme: CollectionSchemeTypeDef
    description: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    expiryTime: Optional[TimestampTypeDef] = None
    postTriggerCollectionDuration: Optional[int] = None
    diagnosticsMode: Optional[DiagnosticsModeType] = None
    spoolingMode: Optional[SpoolingModeType] = None
    compression: Optional[CompressionType] = None
    priority: Optional[int] = None
    signalsToCollect: Optional[Sequence[SignalInformationTypeDef]] = None
    dataExtraDimensions: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    dataDestinationConfigs: Optional[Sequence[DataDestinationConfigTypeDef]] = None
    dataPartitions: Optional[Sequence[DataPartitionTypeDef]] = None
    signalsToFetch: Optional[Sequence[SignalFetchInformationUnionTypeDef]] = None


class StructuredMessageUnionTypeDef(BaseValidatorModel):
    pass


class MessageSignalTypeDef(BaseValidatorModel):
    topicName: str
    structuredMessage: StructuredMessageUnionTypeDef


class SignalDecoderOutputTypeDef(BaseValidatorModel):
    pass


class ListDecoderManifestSignalsResponseTypeDef(BaseValidatorModel):
    signalDecoders: List[SignalDecoderOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SignalDecoderPaginatorTypeDef(BaseValidatorModel):
    pass


class ListDecoderManifestSignalsResponsePaginatorTypeDef(BaseValidatorModel):
    signalDecoders: List[SignalDecoderPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StateTemplateAssociationUnionTypeDef(BaseValidatorModel):
    pass


class CreateVehicleRequestItemTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    stateTemplates: Optional[Sequence[StateTemplateAssociationUnionTypeDef]] = None


class CreateVehicleRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    stateTemplates: Optional[Sequence[StateTemplateAssociationUnionTypeDef]] = None


class UpdateVehicleRequestItemTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None
    stateTemplatesToAdd: Optional[Sequence[StateTemplateAssociationUnionTypeDef]] = None
    stateTemplatesToRemove: Optional[Sequence[str]] = None


class UpdateVehicleRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None
    stateTemplatesToAdd: Optional[Sequence[StateTemplateAssociationUnionTypeDef]] = None
    stateTemplatesToRemove: Optional[Sequence[str]] = None


class BatchCreateVehicleRequestTypeDef(BaseValidatorModel):
    vehicles: Sequence[CreateVehicleRequestItemTypeDef]


class BatchUpdateVehicleRequestTypeDef(BaseValidatorModel):
    vehicles: Sequence[UpdateVehicleRequestItemTypeDef]


class SignalDecoderUnionTypeDef(BaseValidatorModel):
    pass


class CreateDecoderManifestRequestTypeDef(BaseValidatorModel):
    name: str
    modelManifestArn: str
    description: Optional[str] = None
    signalDecoders: Optional[Sequence[SignalDecoderUnionTypeDef]] = None
    networkInterfaces: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    defaultForUnmappedSignals: Optional[Literal["CUSTOM_DECODING"]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateDecoderManifestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    signalDecodersToAdd: Optional[Sequence[SignalDecoderUnionTypeDef]] = None
    signalDecodersToUpdate: Optional[Sequence[SignalDecoderUnionTypeDef]] = None
    signalDecodersToRemove: Optional[Sequence[str]] = None
    networkInterfacesToAdd: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    networkInterfacesToUpdate: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    networkInterfacesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None
    defaultForUnmappedSignals: Optional[Literal["CUSTOM_DECODING"]] = None


