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
from aws_resource_validator.pydantic_models.iotfleetwise_constants import *

class ActuatorExtraOutputTypeDef(BaseValidatorModel):
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

class ActuatorOutputTypeDef(BaseValidatorModel):
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

class ActuatorTypeDef(BaseValidatorModel):
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

class AssociateVehicleFleetRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    fleetId: str

class AttributeExtraOutputTypeDef(BaseValidatorModel):
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

class AttributeOutputTypeDef(BaseValidatorModel):
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

class AttributeTypeDef(BaseValidatorModel):
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

class UpdateVehicleRequestItemTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None

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

class SignalInformationTypeDef(BaseValidatorModel):
    name: str
    maxSampleCount: Optional[int] = None
    minimumSamplingIntervalMs: Optional[int] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

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

class S3ConfigTypeDef(BaseValidatorModel):
    bucketArn: str
    dataFormat: Optional[DataFormatType] = None
    storageCompressionFormat: Optional[StorageCompressionFormatType] = None
    prefix: Optional[str] = None

class TimestreamConfigTypeDef(BaseValidatorModel):
    timestreamTableArn: str
    executionRoleArn: str

class DecoderManifestSummaryTypeDef(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    modelManifestArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None
    message: Optional[str] = None

class DeleteCampaignRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteDecoderManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteFleetRequestRequestTypeDef(BaseValidatorModel):
    fleetId: str

class DeleteModelManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteSignalCatalogRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteVehicleRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str

class DisassociateVehicleFleetRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    fleetId: str

class FleetSummaryTypeDef(BaseValidatorModel):
    id: str
    arn: str
    signalCatalogArn: str
    creationTime: datetime
    description: Optional[str] = None
    lastModificationTime: Optional[datetime] = None

class FormattedVssTypeDef(BaseValidatorModel):
    vssJson: Optional[str] = None

class GetCampaignRequestRequestTypeDef(BaseValidatorModel):
    name: str

class GetDecoderManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str

class GetFleetRequestRequestTypeDef(BaseValidatorModel):
    fleetId: str

class GetModelManifestRequestRequestTypeDef(BaseValidatorModel):
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

class GetSignalCatalogRequestRequestTypeDef(BaseValidatorModel):
    name: str

class NodeCountsTypeDef(BaseValidatorModel):
    totalNodes: Optional[int] = None
    totalBranches: Optional[int] = None
    totalSensors: Optional[int] = None
    totalAttributes: Optional[int] = None
    totalActuators: Optional[int] = None
    totalStructs: Optional[int] = None
    totalProperties: Optional[int] = None

class GetVehicleRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetVehicleStatusRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class VehicleStatusTypeDef(BaseValidatorModel):
    campaignName: Optional[str] = None
    vehicleName: Optional[str] = None
    status: Optional[VehicleStateType] = None

class IamResourcesTypeDef(BaseValidatorModel):
    roleArn: str

class ListCampaignsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[str] = None

class ListDecoderManifestNetworkInterfacesRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDecoderManifestSignalsRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDecoderManifestsRequestRequestTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFleetsForVehicleRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFleetsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListModelManifestNodesRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListModelManifestsRequestRequestTypeDef(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ModelManifestSummaryTypeDef(BaseValidatorModel):
    creationTime: datetime
    lastModificationTime: datetime
    name: Optional[str] = None
    arn: Optional[str] = None
    signalCatalogArn: Optional[str] = None
    description: Optional[str] = None
    status: Optional[ManifestStatusType] = None

class ListSignalCatalogNodesRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    signalNodeType: Optional[SignalNodeTypeType] = None

class ListSignalCatalogsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SignalCatalogSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastModificationTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class ListVehiclesInFleetRequestRequestTypeDef(BaseValidatorModel):
    fleetId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListVehiclesRequestRequestTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class VehicleSummaryTypeDef(BaseValidatorModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    creationTime: datetime
    lastModificationTime: datetime
    attributes: Optional[Dict[str, str]] = None

class MessageSignalTypeDef(BaseValidatorModel):
    topicName: str
    structuredMessage: "StructuredMessageTypeDef"

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

class SensorExtraOutputTypeDef(BaseValidatorModel):
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

class SensorOutputTypeDef(BaseValidatorModel):
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

class SensorTypeDef(BaseValidatorModel):
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

class ROS2PrimitiveMessageDefinitionTypeDef(BaseValidatorModel):
    primitiveType: ROS2PrimitiveTypeType
    offset: Optional[float] = None
    scaling: Optional[float] = None
    upperBound: Optional[int] = None

class PutEncryptionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKeyId: Optional[str] = None

class TimestreamResourcesTypeDef(BaseValidatorModel):
    timestreamDatabaseName: str
    timestreamTableName: str

class StructuredMessageFieldNameAndDataTypePairTypeDef(BaseValidatorModel):
    fieldName: str
    dataType: "StructuredMessageTypeDef"

class StructuredMessageListDefinitionTypeDef(BaseValidatorModel):
    name: str
    memberType: "StructuredMessageTypeDef"
    listType: StructuredMessageListTypeType
    capacity: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateCampaignRequestRequestTypeDef(BaseValidatorModel):
    name: str
    action: UpdateCampaignActionType
    description: Optional[str] = None
    dataExtraDimensions: Optional[Sequence[str]] = None

class UpdateFleetRequestRequestTypeDef(BaseValidatorModel):
    fleetId: str
    description: Optional[str] = None

class UpdateModelManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[str]] = None
    nodesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None

class UpdateVehicleRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: Optional[str] = None
    decoderManifestArn: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    attributeUpdateMode: Optional[UpdateModeType] = None

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

class CreateFleetResponseTypeDef(BaseValidatorModel):
    id: str
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

class DeleteFleetResponseTypeDef(BaseValidatorModel):
    id: str
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

class GetFleetResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    description: str
    signalCatalogArn: str
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

class GetVehicleResponseTypeDef(BaseValidatorModel):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Dict[str, str]
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVehiclesInFleetResponseTypeDef(BaseValidatorModel):
    vehicles: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class UpdateFleetResponseTypeDef(BaseValidatorModel):
    id: str
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

class BatchUpdateVehicleRequestRequestTypeDef(BaseValidatorModel):
    vehicles: Sequence[UpdateVehicleRequestItemTypeDef]

class BatchUpdateVehicleResponseTypeDef(BaseValidatorModel):
    vehicles: List[UpdateVehicleResponseItemTypeDef]
    errors: List[UpdateVehicleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CanDbcDefinitionTypeDef(BaseValidatorModel):
    networkInterface: str
    canDbcFiles: Sequence[BlobTypeDef]
    signalsMap: Optional[Mapping[str, str]] = None

class ListCampaignsResponseTypeDef(BaseValidatorModel):
    campaignSummaries: List[CampaignSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggingOptionsResponseTypeDef(BaseValidatorModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestRequestTypeDef(BaseValidatorModel):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef

class CollectionSchemeTypeDef(BaseValidatorModel):
    timeBasedCollectionScheme: Optional[TimeBasedCollectionSchemeTypeDef] = None
    conditionBasedCollectionScheme: Optional[ConditionBasedCollectionSchemeTypeDef] = None

class CreateFleetRequestRequestTypeDef(BaseValidatorModel):
    fleetId: str
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nodes: Sequence[str]
    signalCatalogArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateVehicleRequestItemTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateVehicleRequestRequestTypeDef(BaseValidatorModel):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Optional[Mapping[str, str]] = None
    associationBehavior: Optional[VehicleAssociationBehaviorType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DataDestinationConfigTypeDef(BaseValidatorModel):
    s3Config: Optional[S3ConfigTypeDef] = None
    timestreamConfig: Optional[TimestreamConfigTypeDef] = None

class ListDecoderManifestsResponseTypeDef(BaseValidatorModel):
    summaries: List[DecoderManifestSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsResponseTypeDef(BaseValidatorModel):
    fleetSummaries: List[FleetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSignalCatalogRequestRequestTypeDef(BaseValidatorModel):
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

class GetVehicleStatusRequestGetVehicleStatusPaginateTypeDef(BaseValidatorModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCampaignsRequestListCampaignsPaginateTypeDef(BaseValidatorModel):
    status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDecoderManifestNetworkInterfacesRequestListDecoderManifestNetworkInterfacesPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDecoderManifestSignalsRequestListDecoderManifestSignalsPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDecoderManifestsRequestListDecoderManifestsPaginateTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsForVehicleRequestListFleetsForVehiclePaginateTypeDef(BaseValidatorModel):
    vehicleName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetsRequestListFleetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelManifestNodesRequestListModelManifestNodesPaginateTypeDef(BaseValidatorModel):
    name: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelManifestsRequestListModelManifestsPaginateTypeDef(BaseValidatorModel):
    signalCatalogArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSignalCatalogNodesRequestListSignalCatalogNodesPaginateTypeDef(BaseValidatorModel):
    name: str
    signalNodeType: Optional[SignalNodeTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSignalCatalogsRequestListSignalCatalogsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVehiclesInFleetRequestListVehiclesInFleetPaginateTypeDef(BaseValidatorModel):
    fleetId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVehiclesRequestListVehiclesPaginateTypeDef(BaseValidatorModel):
    modelManifestArn: Optional[str] = None
    attributeNames: Optional[Sequence[str]] = None
    attributeValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetVehicleStatusResponseTypeDef(BaseValidatorModel):
    campaigns: List[VehicleStatusTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelManifestsResponseTypeDef(BaseValidatorModel):
    summaries: List[ModelManifestSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSignalCatalogsResponseTypeDef(BaseValidatorModel):
    summaries: List[SignalCatalogSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVehiclesResponseTypeDef(BaseValidatorModel):
    vehicleSummaries: List[VehicleSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInterfaceTypeDef(BaseValidatorModel):
    interfaceId: str
    type: NetworkInterfaceTypeType
    canInterface: Optional[CanInterfaceTypeDef] = None
    obdInterface: Optional[ObdInterfaceTypeDef] = None
    vehicleMiddleware: Optional[VehicleMiddlewareTypeDef] = None

class NodeExtraOutputTypeDef(BaseValidatorModel):
    branch: Optional[BranchTypeDef] = None
    sensor: Optional[SensorExtraOutputTypeDef] = None
    actuator: Optional[ActuatorExtraOutputTypeDef] = None
    attribute: Optional[AttributeExtraOutputTypeDef] = None
    struct: Optional[CustomStructTypeDef] = None
    property: Optional[CustomPropertyTypeDef] = None

class NodeOutputTypeDef(BaseValidatorModel):
    branch: Optional[BranchTypeDef] = None
    sensor: Optional[SensorOutputTypeDef] = None
    actuator: Optional[ActuatorOutputTypeDef] = None
    attribute: Optional[AttributeOutputTypeDef] = None
    struct: Optional[CustomStructTypeDef] = None
    property: Optional[CustomPropertyTypeDef] = None

class NodeTypeDef(BaseValidatorModel):
    branch: Optional[BranchTypeDef] = None
    sensor: Optional[SensorTypeDef] = None
    actuator: Optional[ActuatorTypeDef] = None
    attribute: Optional[AttributeTypeDef] = None
    struct: Optional[CustomStructTypeDef] = None
    property: Optional[CustomPropertyTypeDef] = None

class SignalDecoderTypeDef(BaseValidatorModel):
    fullyQualifiedName: str
    type: SignalDecoderTypeType
    interfaceId: str
    canSignal: Optional[CanSignalTypeDef] = None
    obdSignal: Optional[ObdSignalTypeDef] = None
    messageSignal: Optional[MessageSignalTypeDef] = None

class PrimitiveMessageDefinitionTypeDef(BaseValidatorModel):
    ros2PrimitiveMessageDefinition: Optional[ROS2PrimitiveMessageDefinitionTypeDef] = None

class RegisterAccountRequestRequestTypeDef(BaseValidatorModel):
    timestreamResources: Optional[TimestreamResourcesTypeDef] = None
    iamResources: Optional[IamResourcesTypeDef] = None

class RegisterAccountResponseTypeDef(BaseValidatorModel):
    registerAccountStatus: RegistrationStatusType
    timestreamResources: TimestreamResourcesTypeDef
    iamResources: IamResourcesTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkFileDefinitionTypeDef(BaseValidatorModel):
    canDbc: Optional[CanDbcDefinitionTypeDef] = None

class BatchCreateVehicleRequestRequestTypeDef(BaseValidatorModel):
    vehicles: Sequence[CreateVehicleRequestItemTypeDef]

class CreateCampaignRequestRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListDecoderManifestNetworkInterfacesResponseTypeDef(BaseValidatorModel):
    networkInterfaces: List[NetworkInterfaceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSignalCatalogNodesResponseTypeDef(BaseValidatorModel):
    nodes: List[NodeExtraOutputTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelManifestNodesResponseTypeDef(BaseValidatorModel):
    nodes: List[NodeOutputTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDecoderManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str
    modelManifestArn: str
    description: Optional[str] = None
    signalDecoders: Optional[Sequence[SignalDecoderTypeDef]] = None
    networkInterfaces: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListDecoderManifestSignalsResponseTypeDef(BaseValidatorModel):
    signalDecoders: List[SignalDecoderTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDecoderManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    signalDecodersToAdd: Optional[Sequence[SignalDecoderTypeDef]] = None
    signalDecodersToUpdate: Optional[Sequence[SignalDecoderTypeDef]] = None
    signalDecodersToRemove: Optional[Sequence[str]] = None
    networkInterfacesToAdd: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    networkInterfacesToUpdate: Optional[Sequence[NetworkInterfaceTypeDef]] = None
    networkInterfacesToRemove: Optional[Sequence[str]] = None
    status: Optional[ManifestStatusType] = None

class StructuredMessageTypeDef(BaseValidatorModel):
    primitiveMessageDefinition: Optional[PrimitiveMessageDefinitionTypeDef] = None
    structuredMessageListDefinition: Optional[Dict[str, Any]] = None
    structuredMessageDefinition: Optional[Sequence[Dict[str, Any]]] = None

class ImportDecoderManifestRequestRequestTypeDef(BaseValidatorModel):
    name: str
    networkFileDefinitions: Sequence[NetworkFileDefinitionTypeDef]

class CreateSignalCatalogRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodes: Optional[Sequence[NodeUnionTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateSignalCatalogRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    nodesToAdd: Optional[Sequence[NodeUnionTypeDef]] = None
    nodesToUpdate: Optional[Sequence[NodeUnionTypeDef]] = None
    nodesToRemove: Optional[Sequence[str]] = None

