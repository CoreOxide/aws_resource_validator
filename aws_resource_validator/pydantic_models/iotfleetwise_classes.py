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
from aws_resource_validator.pydantic_models.iotfleetwise_constants import *

class ActuatorExtraOutputTypeDef(BaseModel):
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

class ActuatorOutputTypeDef(BaseModel):
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

class ActuatorTypeDef(BaseModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[Sequence[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    assignedValue: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None

class AssociateVehicleFleetRequestRequestTypeDef(BaseModel):
    vehicleName: str
    fleetId: str

class AttributeExtraOutputTypeDef(BaseModel):
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

class AttributeOutputTypeDef(BaseModel):
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

class AttributeTypeDef(BaseModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[Sequence[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    assignedValue: Optional[str] = None
    defaultValue: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None

class CreateVehicleErrorTypeDef(BaseModel):
    vehicleName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class CreateVehicleResponseItemTypeDef(BaseModel):
    vehicleName: Optional[str] = None
    arn: Optional[str] = None
    thingArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UpdateVehicleRequestItemTypeDef(BaseModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None

class UpdateVehicleErrorTypeDef(BaseModel):
    vehicleName: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None

class UpdateVehicleResponseItemTypeDef(BaseModel):
    vehicleName: Optional[str] = None
    arn: Optional[str] = None

class BranchTypeDef(BaseModel):
    fullyQualifiedName: str
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None

class CampaignSummaryTypeDef(BaseModel):
    creationTime: datetime
    lastModificationTime: datetime
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[CampaignStatusType] = None

class CanInterfaceTypeDef(BaseModel):
    name: str
    protocolName: Optional[str] = None
    protocolVersion: Optional[str] = None

class CanSignalTypeDef(BaseModel):
    messageId: int
    isBigEndian: bool
    isSigned: bool
    startBit: int
    offset: float
    factor: float
    length: int
    name: Optional[str] = None

class CloudWatchLogDeliveryOptionsTypeDef(BaseModel):
    logType: LogTypeType
    logGroupName: Optional[str] = None

class ConditionBasedCollectionSchemeTypeDef(BaseModel):
    expression: str
    minimumTriggerIntervalMs: Optional[int] = None
    triggerMode: Optional[TriggerModeType] = None
    conditionLanguageVersion: Optional[int] = None

class TimeBasedCollectionSchemeTypeDef(BaseModel):
    periodMs: int

class SignalInformationTypeDef(BaseModel):
    name: str
    maxSampleCount: Optional[int] = None
    minimumSamplingIntervalMs: Optional[int] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CustomPropertyTypeDef(BaseModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    dataEncoding: Optional[NodeDataEncodingType] = None
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None

class CustomStructTypeDef(BaseModel):
    fullyQualifiedName: str
    description: Optional[str] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None

class S3ConfigTypeDef(BaseModel):
    bucketArn: str
    dataFormat: Optional[DataFormatType] = None
    storageCompressionFormat: Optional[StorageCompressionFormatType] = None
    prefix: Optional[str] = None

class TimestreamConfigTypeDef(BaseModel):
    timestreamTableArn: str
    executionRoleArn: str

class DecoderManifestSummaryTypeDef(BaseModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    modelManifestArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None
    message: Optional[str] = None

class DeleteCampaignRequestRequestTypeDef(BaseModel):
    name: str

class DeleteDecoderManifestRequestRequestTypeDef(BaseModel):
    name: str

class DeleteFleetRequestRequestTypeDef(BaseModel):
    fleetId: str

class DeleteModelManifestRequestRequestTypeDef(BaseModel):
    name: str

class DeleteSignalCatalogRequestRequestTypeDef(BaseModel):
    name: str

class DeleteVehicleRequestRequestTypeDef(BaseModel):
    vehicleName: str

class DisassociateVehicleFleetRequestRequestTypeDef(BaseModel):
    vehicleName: str
    fleetId: str

class FleetSummaryTypeDef(BaseModel):
    id: str
    arn: str
    signalCatalogArn: str
    creationTime: datetime
    description: Optional[str] = None
    lastModificationTime: Optional[datetime] = None

class FormattedVssTypeDef(BaseModel):
    vssJson: Optional[str] = None

class GetCampaignRequestRequestTypeDef(BaseModel):
    name: str

class GetDecoderManifestRequestRequestTypeDef(BaseModel):
    name: str

class GetFleetRequestRequestTypeDef(BaseModel):
    fleetId: str

class GetModelManifestRequestRequestTypeDef(BaseModel):
    name: str

class IamRegistrationResponseTypeDef(BaseModel):
    roleArn: str
    registrationStatus: RegistrationStatusType
    errorMessage: Optional[str] = None

class TimestreamRegistrationResponseTypeDef(BaseModel):
    timestreamDatabaseName: str
    timestreamTableName: str
    registrationStatus: RegistrationStatusType
    timestreamDatabaseArn: Optional[str] = None
    timestreamTableArn: Optional[str] = None
    errorMessage: Optional[str] = None

class GetSignalCatalogRequestRequestTypeDef(BaseModel):
    name: str

class NodeCountsTypeDef(BaseModel):
    totalNodes: Optional[int] = None
    totalBranches: Optional[int] = None
    totalSensors: Optional[int] = None
    totalAttributes: Optional[int] = None
    totalActuators: Optional[int] = None
    totalStructs: Optional[int] = None
    totalProperties: Optional[int] = None

class GetVehicleRequestRequestTypeDef(BaseModel):
    vehicleName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetVehicleStatusRequestRequestTypeDef(BaseModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class VehicleStatusTypeDef(BaseModel):
    campaignName: Optional[str] = None
    vehicleName: Optional[str] = None
    status: Optional[VehicleStateType] = None

class IamResourcesTypeDef(BaseModel):
    roleArn: str

class ListCampaignsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[str] = None

class ListDecoderManifestNetworkInterfacesRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDecoderManifestSignalsRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDecoderManifestsRequestRequestTypeDef(BaseModel):
    modelManifestArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFleetsForVehicleRequestRequestTypeDef(BaseModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFleetsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListModelManifestNodesRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListModelManifestsRequestRequestTypeDef(BaseModel):
    signalCatalogArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ModelManifestSummaryTypeDef(BaseModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None

class ListSignalCatalogNodesRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    signalNodeType: Optional[SignalNodeTypeType] = None

class ListSignalCatalogsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SignalCatalogSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastModificationTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListVehiclesInFleetRequestRequestTypeDef(BaseModel):
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListVehiclesRequestRequestTypeDef(BaseModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class VehicleSummaryTypeDef(BaseModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    creationTime: datetime
    lastModificationTime: datetime
    attributes: Optional[Dict[str, str]] = None

class MessageSignalTypeDef(BaseModel):
    topicName: str
    structuredMessage: "StructuredMessageTypeDef"

class ObdInterfaceTypeDef(BaseModel):
    name: str
    requestMessageId: int
    obdStandard: Optional[str] = None
    pidRequestIntervalSeconds: Optional[int] = None
    dtcRequestIntervalSeconds: Optional[int] = None
    useExtendedIds: Optional[bool] = None
    hasTransmissionEcu: Optional[bool] = None

class VehicleMiddlewareTypeDef(BaseModel):
    name: str
    protocolName: Literal["ROS_2"]

class SensorExtraOutputTypeDef(BaseModel):
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

class SensorOutputTypeDef(BaseModel):
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

class SensorTypeDef(BaseModel):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    description: Optional[str] = None
    unit: Optional[str] = None
    allowedValues: Optional[Sequence[str]] = None
    min: Optional[float] = None
    max: Optional[float] = None
    deprecationMessage: Optional[str] = None
    comment: Optional[str] = None
    structFullyQualifiedName: Optional[str] = None

class ObdSignalTypeDef(BaseModel):
    pidResponseLength: int
    serviceMode: int
    pid: int
    scaling: float
    offset: float
    startByte: int
    byteLength: int
    bitRightShift: Optional[int] = None
    bitMaskLength: Optional[int] = None

class ROS2PrimitiveMessageDefinitionTypeDef(BaseModel):
    primitiveType: ROS2PrimitiveTypeType
    offset: Optional[float] = None
    scaling: Optional[float] = None
    upperBound: Optional[int] = None

class PutEncryptionConfigurationRequestRequestTypeDef(BaseModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None

class TimestreamResourcesTypeDef(BaseModel):
    timestreamDatabaseName: str
    timestreamTableName: str

class StructuredMessageFieldNameAndDataTypePairTypeDef(BaseModel):
    fieldName: str
    dataType: "StructuredMessageTypeDef"

class StructuredMessageListDefinitionTypeDef(BaseModel):
    name: str
    memberType: "StructuredMessageTypeDef"
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateCampaignRequestRequestTypeDef(BaseModel):
    name: str
    action: UpdateCampaignActionType
    description: Optional[str] = None
    dataExtraDimensions: Optional[Sequence[str]] = None

class UpdateFleetRequestRequestTypeDef(BaseModel):
    fleetId: str
    description: Optional[str] = None

class UpdateModelManifestRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[str]] = None
    nodesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None

class UpdateVehicleRequestRequestTypeDef(BaseModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None

class BatchCreateVehicleResponseTypeDef(BaseModel):
    vehicles: List[CreateVehicleResponseItemTypeDef]
    errors: List[CreateVehicleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCampaignResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDecoderManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResponseTypeDef(BaseModel):
    id: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSignalCatalogResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVehicleResponseTypeDef(BaseModel):
    vehicleName: str
    arn: str
    thingArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCampaignResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDecoderManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFleetResponseTypeDef(BaseModel):
    id: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteModelManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSignalCatalogResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVehicleResponseTypeDef(BaseModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDecoderManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    description: str
    modelManifestArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncryptionConfigurationResponseTypeDef(BaseModel):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    errorMessage: str
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetFleetResponseTypeDef(BaseModel):
    id: str
    arn: str
    description: str
    signalCatalogArn: str
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetVehicleResponseTypeDef(BaseModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Dict[str, str]
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ImportDecoderManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSignalCatalogResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsForVehicleResponseTypeDef(BaseModel):
    fleets: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVehiclesInFleetResponseTypeDef(BaseModel):
    vehicles: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutEncryptionConfigurationResponseTypeDef(BaseModel):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCampaignResponseTypeDef(BaseModel):
    arn: str
    name: str
    status: CampaignStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDecoderManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetResponseTypeDef(BaseModel):
    id: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelManifestResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSignalCatalogResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVehicleResponseTypeDef(BaseModel):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateVehicleRequestRequestTypeDef(BaseModel):
    vehicles: Sequence[UpdateVehicleRequestItemTypeDef]

class BatchUpdateVehicleResponseTypeDef(BaseModel):
    vehicles: List[UpdateVehicleResponseItemTypeDef]
    errors: List[UpdateVehicleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CanDbcDefinitionTypeDef(BaseModel):
    networkInterface: str
    canDbcFiles: Sequence[BlobTypeDef]
    signalsMap: Optional[Mapping[str, str]] = None

class ListCampaignsResponseTypeDef(BaseModel):
    campaignSummaries: List[CampaignSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggingOptionsResponseTypeDef(BaseModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef

class CollectionSchemeTypeDef(BaseModel):
    timeBasedCollectionScheme: Optional[TimeBasedCollectionSchemeTypeDef] = None
    conditionBasedCollectionScheme: Optional[ConditionBasedCollectionSchemeTypeDef] = None

class CreateFleetRequestRequestTypeDef(BaseModel):
    fleetId: str
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelManifestRequestRequestTypeDef(BaseModel):
    name: str
    nodes: Sequence[str]
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateVehicleRequestItemTypeDef(BaseModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateVehicleRequestRequestTypeDef(BaseModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DataDestinationConfigTypeDef(BaseModel):
    s3Config: Optional[S3ConfigTypeDef] = None
    timestreamConfig: Optional[TimestreamConfigTypeDef] = None

class ListDecoderManifestsResponseTypeDef(BaseModel):
    summaries: List[DecoderManifestSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponseTypeDef(BaseModel):
    fleetSummaries: List[FleetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSignalCatalogRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    vss: Optional[FormattedVssTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class GetRegisterAccountStatusResponseTypeDef(BaseModel):
    customerAccountId: str
    accountStatus: RegistrationStatusType
    timestreamRegistrationResponse: TimestreamRegistrationResponseTypeDef
    iamRegistrationResponse: IamRegistrationResponseTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSignalCatalogResponseTypeDef(BaseModel):
    name: str
    arn: str
    description: str
    nodeCounts: NodeCountsTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef(BaseModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCampaignsRequestListCampaignsPaginateTypeDef(BaseModel):
    status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef(BaseModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef(BaseModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef(BaseModel):
    modelManifestArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef(BaseModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsRequestListFleetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef(BaseModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelManifestsRequestListModelManifestsPaginateTypeDef(BaseModel):
    signalCatalogArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef(BaseModel):
    name: str
    signalNodeType: Optional[SignalNodeTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef(BaseModel):
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVehiclesRequestListVehiclesPaginateTypeDef(BaseModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetVehicleStatusResponseTypeDef(BaseModel):
    campaigns: List[VehicleStatusTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelManifestsResponseTypeDef(BaseModel):
    summaries: List[ModelManifestSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSignalCatalogsResponseTypeDef(BaseModel):
    summaries: List[SignalCatalogSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVehiclesResponseTypeDef(BaseModel):
    vehicleSummaries: List[VehicleSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInterfaceTypeDef(BaseModel):
    interfaceId: str
    type: NetworkInterfaceTypeType
    canInterface: Optional[CanInterfaceTypeDef] = None
    obdInterface: Optional[ObdInterfaceTypeDef] = None
    vehicleMiddleware: Optional[VehicleMiddlewareTypeDef] = None

class NodeExtraOutputTypeDef(BaseModel):
    branch: Optional[BranchTypeDef] = None
    sensor: Optional[SensorExtraOutputTypeDef] = None
    actuator: Optional[ActuatorExtraOutputTypeDef] = None
    attribute: Optional[AttributeExtraOutputTypeDef] = None
    struct: Optional[CustomStructTypeDef] = None
    property: Optional[CustomPropertyTypeDef] = None

class NodeOutputTypeDef(BaseModel):
    branch: Optional[BranchTypeDef] = None
    sensor: Optional[SensorOutputTypeDef] = None
    actuator: Optional[ActuatorOutputTypeDef] = None
    attribute: Optional[AttributeOutputTypeDef] = None
    struct: Optional[CustomStructTypeDef] = None
    property: Optional[CustomPropertyTypeDef] = None

class NodeTypeDef(BaseModel):
    branch: Optional[BranchTypeDef] = None
    sensor: Optional[SensorTypeDef] = None
    actuator: Optional[ActuatorTypeDef] = None
    attribute: Optional[AttributeTypeDef] = None
    struct: Optional[CustomStructTypeDef] = None
    property: Optional[CustomPropertyTypeDef] = None

class SignalDecoderTypeDef(BaseModel):
    fullyQualifiedName: str
    type: SignalDecoderTypeType
    interfaceId: str
    canSignal: Optional[CanSignalTypeDef] = None
    obdSignal: Optional[ObdSignalTypeDef] = None
    messageSignal: Optional[MessageSignalTypeDef] = None

class PrimitiveMessageDefinitionTypeDef(BaseModel):
    ros2PrimitiveMessageDefinition: Optional[ROS2PrimitiveMessageDefinitionTypeDef] = None

class RegisterAccountRequestRequestTypeDef(BaseModel):
    timestreamResources: Optional[TimestreamResourcesTypeDef] = None
    iamResources: Optional[IamResourcesTypeDef] = None

class RegisterAccountResponseTypeDef(BaseModel):
    registerAccountStatus: RegistrationStatusType
    timestreamResources: TimestreamResourcesTypeDef
    iamResources: IamResourcesTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkFileDefinitionTypeDef(BaseModel):
    canDbc: Optional[CanDbcDefinitionTypeDef] = None

class BatchCreateVehicleRequestRequestTypeDef(BaseModel):
    vehicles: Sequence[CreateVehicleRequestItemTypeDef]

class CreateCampaignRequestRequestTypeDef(BaseModel):
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

class GetCampaignResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListDecoderManifestNetworkInterfacesResponseTypeDef(BaseModel):
    networkInterfaces: List[NetworkInterfaceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSignalCatalogNodesResponseTypeDef(BaseModel):
    nodes: List[NodeExtraOutputTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelManifestNodesResponseTypeDef(BaseModel):
    nodes: List[NodeOutputTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDecoderManifestRequestRequestTypeDef(BaseModel):
    name: str
    modelManifestArn: str
    description: Optional[str] = None
    signalDecoders: Optional[Sequence[SignalDecoderTypeDef]] = None
    networkInterfaces: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListDecoderManifestSignalsResponseTypeDef(BaseModel):
    signalDecoders: List[SignalDecoderTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDecoderManifestRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    signalDecodersToAdd: Optional[Sequence[SignalDecoderTypeDef]] = None
    signalDecodersToUpdate: Optional[Sequence[SignalDecoderTypeDef]] = None
    signalDecodersToRemove: Optional[Sequence[str]] = None
    networkInterfacesToAdd: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    networkInterfacesToUpdate: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    networkInterfacesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None

class StructuredMessageTypeDef(BaseModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinitionTypeDef] = None
    structuredMessageListDefinition: Optional[Dict[str, Any]] = None
    structuredMessageDefinition: Optional[Sequence[Dict[str, Any]]] = None

class ImportDecoderManifestRequestRequestTypeDef(BaseModel):
    name: str
    networkFileDefinitions: Sequence[NetworkFileDefinitionTypeDef]

class CreateSignalCatalogRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    nodes: Optional[Sequence[NodeUnionTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateSignalCatalogRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[NodeUnionTypeDef]] = None
    nodesToUpdate: Optional[Sequence[NodeUnionTypeDef]] = None
    nodesToRemove: Optional[Sequence[str]] = None

