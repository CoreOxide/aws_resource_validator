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
from aws_resource_validator.pydantic_models.b2bi_constants import *

class InputFileSourceTypeDef(BaseValidatorModel):
    fileContent: Optional[str] = None


class X12DetailsTypeDef(BaseValidatorModel):
    transactionSet: Optional[X12TransactionSetType] = None
    version: Optional[X12VersionType] = None


class S3LocationTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    key: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MappingType(BaseValidatorModel):
    templateLanguage: MappingTemplateLanguageType
    template: Optional[str] = None


class DeleteCapabilityRequestTypeDef(BaseValidatorModel):
    capabilityId: str


class DeletePartnershipRequestTypeDef(BaseValidatorModel):
    partnershipId: str


class DeleteProfileRequestTypeDef(BaseValidatorModel):
    profileId: str


class DeleteTransformerRequestTypeDef(BaseValidatorModel):
    transformerId: str


class GenerateMappingRequestTypeDef(BaseValidatorModel):
    inputFileContent: str
    outputFileContent: str
    mappingType: MappingTypeType


class GetCapabilityRequestTypeDef(BaseValidatorModel):
    capabilityId: str


class GetPartnershipRequestTypeDef(BaseValidatorModel):
    partnershipId: str


class GetProfileRequestTypeDef(BaseValidatorModel):
    profileId: str


class GetTransformerJobRequestTypeDef(BaseValidatorModel):
    transformerJobId: str
    transformerId: str


class GetTransformerRequestTypeDef(BaseValidatorModel):
    transformerId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCapabilitiesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPartnershipsRequestTypeDef(BaseValidatorModel):
    profileId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProfilesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ProfileSummaryTypeDef(BaseValidatorModel):
    profileId: str
    name: str
    businessName: str
    createdAt: datetime
    logging: Optional[LoggingType] = None
    logGroupName: Optional[str] = None
    modifiedAt: Optional[datetime] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class ListTransformersRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestMappingRequestTypeDef(BaseValidatorModel):
    inputFileContent: str
    mappingTemplate: str
    fileFormat: FileFormatType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateProfileRequestTypeDef(BaseValidatorModel):
    profileId: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    businessName: Optional[str] = None


class X12DelimitersTypeDef(BaseValidatorModel):
    componentSeparator: Optional[str] = None
    dataElementSeparator: Optional[str] = None
    segmentTerminator: Optional[str] = None


class X12FunctionalGroupHeadersTypeDef(BaseValidatorModel):
    applicationSenderCode: Optional[str] = None
    applicationReceiverCode: Optional[str] = None
    responsibleAgencyCode: Optional[str] = None


class X12InterchangeControlHeadersTypeDef(BaseValidatorModel):
    senderIdQualifier: Optional[str] = None
    senderId: Optional[str] = None
    receiverIdQualifier: Optional[str] = None
    receiverId: Optional[str] = None
    repetitionSeparator: Optional[str] = None
    acknowledgmentRequestedCode: Optional[str] = None
    usageIndicatorCode: Optional[str] = None


class ConversionSourceTypeDef(BaseValidatorModel):
    fileFormat: ConversionSourceFormatType
    inputFile: InputFileSourceTypeDef


class ConversionTargetFormatDetailsTypeDef(BaseValidatorModel):
    x12: Optional[X12DetailsTypeDef] = None


class EdiTypeTypeDef(BaseValidatorModel):
    x12Details: Optional[X12DetailsTypeDef] = None


class FormatOptionsTypeDef(BaseValidatorModel):
    x12: Optional[X12DetailsTypeDef] = None


class TemplateDetailsTypeDef(BaseValidatorModel):
    x12: Optional[X12DetailsTypeDef] = None


class OutputSampleFileSourceTypeDef(BaseValidatorModel):
    fileLocation: Optional[S3LocationTypeDef] = None


class StartTransformerJobRequestTypeDef(BaseValidatorModel):
    inputFile: S3LocationTypeDef
    outputLocation: S3LocationTypeDef
    transformerId: str
    clientToken: Optional[str] = None


class CreateProfileRequestTypeDef(BaseValidatorModel):
    name: str
    phone: str
    businessName: str
    logging: LoggingType
    email: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class CreateProfileResponseTypeDef(BaseValidatorModel):
    profileId: str
    profileArn: str
    name: str
    businessName: str
    phone: str
    email: str
    logging: LoggingType
    logGroupName: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStarterMappingTemplateResponseTypeDef(BaseValidatorModel):
    mappingTemplate: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GenerateMappingResponseTypeDef(BaseValidatorModel):
    mappingTemplate: str
    mappingAccuracy: float
    ResponseMetadata: ResponseMetadataTypeDef


class GetProfileResponseTypeDef(BaseValidatorModel):
    profileId: str
    profileArn: str
    name: str
    email: str
    phone: str
    businessName: str
    logging: LoggingType
    logGroupName: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetTransformerJobResponseTypeDef(BaseValidatorModel):
    status: TransformerJobStatusType
    outputFiles: List[S3LocationTypeDef]
    message: str
    ResponseMetadata: ResponseMetadataTypeDef


class CapabilitySummaryTypeDef(BaseValidatorModel):
    pass


class ListCapabilitiesResponseTypeDef(BaseValidatorModel):
    capabilities: List[CapabilitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartTransformerJobResponseTypeDef(BaseValidatorModel):
    transformerJobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TestConversionResponseTypeDef(BaseValidatorModel):
    convertedFileContent: str
    validationMessages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class TestMappingResponseTypeDef(BaseValidatorModel):
    mappedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef


class TestParsingResponseTypeDef(BaseValidatorModel):
    parsedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProfileResponseTypeDef(BaseValidatorModel):
    profileId: str
    profileArn: str
    name: str
    email: str
    phone: str
    businessName: str
    logging: LoggingType
    logGroupName: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListCapabilitiesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPartnershipsRequestPaginateTypeDef(BaseValidatorModel):
    profileId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProfilesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTransformersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProfilesResponseTypeDef(BaseValidatorModel):
    profiles: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SampleDocumentKeysTypeDef(BaseValidatorModel):
    pass


class SampleDocumentsOutputTypeDef(BaseValidatorModel):
    bucketName: str
    keys: List[SampleDocumentKeysTypeDef]


class SampleDocumentsTypeDef(BaseValidatorModel):
    bucketName: str
    keys: Sequence[SampleDocumentKeysTypeDef]


class X12OutboundEdiHeadersTypeDef(BaseValidatorModel):
    interchangeControlHeaders: Optional[X12InterchangeControlHeadersTypeDef] = None
    functionalGroupHeaders: Optional[X12FunctionalGroupHeadersTypeDef] = None
    delimiters: Optional[X12DelimitersTypeDef] = None
    validateEdi: Optional[bool] = None


class TestParsingRequestTypeDef(BaseValidatorModel):
    inputFile: S3LocationTypeDef
    fileFormat: FileFormatType
    ediType: EdiTypeTypeDef


class InputConversionTypeDef(BaseValidatorModel):
    fromFormat: Literal["X12"]
    formatOptions: Optional[FormatOptionsTypeDef] = None


class OutputConversionTypeDef(BaseValidatorModel):
    toFormat: Literal["X12"]
    formatOptions: Optional[FormatOptionsTypeDef] = None


class CreateStarterMappingTemplateRequestTypeDef(BaseValidatorModel):
    mappingType: MappingTypeType
    templateDetails: TemplateDetailsTypeDef
    outputSampleLocation: Optional[S3LocationTypeDef] = None


class ConversionTargetTypeDef(BaseValidatorModel):
    fileFormat: Literal["X12"]
    formatDetails: Optional[ConversionTargetFormatDetailsTypeDef] = None
    outputSampleFile: Optional[OutputSampleFileSourceTypeDef] = None


class X12EnvelopeTypeDef(BaseValidatorModel):
    common: Optional[X12OutboundEdiHeadersTypeDef] = None


class EdiConfigurationTypeDef(BaseValidatorModel):
    pass


class CapabilityConfigurationTypeDef(BaseValidatorModel):
    edi: Optional[EdiConfigurationTypeDef] = None


class CreateTransformerResponseTypeDef(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: str
    inputConversion: InputConversionTypeDef
    mapping: MappingType
    outputConversion: OutputConversionTypeDef
    sampleDocuments: SampleDocumentsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTransformerResponseTypeDef(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: str
    inputConversion: InputConversionTypeDef
    mapping: MappingType
    outputConversion: OutputConversionTypeDef
    sampleDocuments: SampleDocumentsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TransformerSummaryTypeDef(BaseValidatorModel):
    transformerId: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: Optional[datetime] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiTypeTypeDef] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversionTypeDef] = None
    mapping: Optional[MappingType] = None
    outputConversion: Optional[OutputConversionTypeDef] = None
    sampleDocuments: Optional[SampleDocumentsOutputTypeDef] = None


class UpdateTransformerResponseTypeDef(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: str
    inputConversion: InputConversionTypeDef
    mapping: MappingType
    outputConversion: OutputConversionTypeDef
    sampleDocuments: SampleDocumentsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TestConversionRequestTypeDef(BaseValidatorModel):
    source: ConversionSourceTypeDef
    target: ConversionTargetTypeDef


class SampleDocumentsUnionTypeDef(BaseValidatorModel):
    pass


class CreateTransformerRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiTypeTypeDef] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversionTypeDef] = None
    mapping: Optional[MappingType] = None
    outputConversion: Optional[OutputConversionTypeDef] = None
    sampleDocuments: Optional[SampleDocumentsUnionTypeDef] = None


class UpdateTransformerRequestTypeDef(BaseValidatorModel):
    transformerId: str
    name: Optional[str] = None
    status: Optional[TransformerStatusType] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiTypeTypeDef] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversionTypeDef] = None
    mapping: Optional[MappingType] = None
    outputConversion: Optional[OutputConversionTypeDef] = None
    sampleDocuments: Optional[SampleDocumentsUnionTypeDef] = None


class OutboundEdiOptionsTypeDef(BaseValidatorModel):
    x12: Optional[X12EnvelopeTypeDef] = None


class UpdateCapabilityRequestTypeDef(BaseValidatorModel):
    capabilityId: str
    name: Optional[str] = None
    configuration: Optional[CapabilityConfigurationTypeDef] = None
    instructionsDocuments: Optional[Sequence[S3LocationTypeDef]] = None


class ListTransformersResponseTypeDef(BaseValidatorModel):
    transformers: List[TransformerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CapabilityOptionsTypeDef(BaseValidatorModel):
    outboundEdi: Optional[OutboundEdiOptionsTypeDef] = None


class CreatePartnershipRequestTypeDef(BaseValidatorModel):
    profileId: str
    name: str
    email: str
    capabilities: Sequence[str]
    phone: Optional[str] = None
    capabilityOptions: Optional[CapabilityOptionsTypeDef] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreatePartnershipResponseTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptionsTypeDef
    tradingPartnerId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetPartnershipResponseTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptionsTypeDef
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PartnershipSummaryTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    createdAt: datetime
    name: Optional[str] = None
    capabilities: Optional[List[str]] = None
    capabilityOptions: Optional[CapabilityOptionsTypeDef] = None
    tradingPartnerId: Optional[str] = None
    modifiedAt: Optional[datetime] = None


class UpdatePartnershipRequestTypeDef(BaseValidatorModel):
    partnershipId: str
    name: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    capabilityOptions: Optional[CapabilityOptionsTypeDef] = None


class UpdatePartnershipResponseTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptionsTypeDef
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListPartnershipsResponseTypeDef(BaseValidatorModel):
    partnerships: List[PartnershipSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


