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

class InputFileSource(BaseValidatorModel):
    fileContent: Optional[str] = None


class X12Details(BaseValidatorModel):
    transactionSet: Optional[X12TransactionSetType] = None
    version: Optional[X12VersionType] = None


class S3Location(BaseValidatorModel):
    bucketName: Optional[str] = None
    key: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MappingType(BaseValidatorModel):
    templateLanguage: MappingTemplateLanguageType
    template: Optional[str] = None


class DeleteCapabilityRequest(BaseValidatorModel):
    capabilityId: str


class DeletePartnershipRequest(BaseValidatorModel):
    partnershipId: str


class DeleteProfileRequest(BaseValidatorModel):
    profileId: str


class DeleteTransformerRequest(BaseValidatorModel):
    transformerId: str


class GenerateMappingRequest(BaseValidatorModel):
    inputFileContent: str
    outputFileContent: str
    mappingType: MappingTypeType


class GetCapabilityRequest(BaseValidatorModel):
    capabilityId: str


class GetPartnershipRequest(BaseValidatorModel):
    partnershipId: str


class GetProfileRequest(BaseValidatorModel):
    profileId: str


class GetTransformerJobRequest(BaseValidatorModel):
    transformerJobId: str
    transformerId: str


class GetTransformerRequest(BaseValidatorModel):
    transformerId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListCapabilitiesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPartnershipsRequest(BaseValidatorModel):
    profileId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListProfilesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ProfileSummary(BaseValidatorModel):
    profileId: str
    name: str
    businessName: str
    createdAt: datetime
    logging: Optional[LoggingType] = None
    logGroupName: Optional[str] = None
    modifiedAt: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class ListTransformersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TestMappingRequest(BaseValidatorModel):
    inputFileContent: str
    mappingTemplate: str
    fileFormat: FileFormatType


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateProfileRequest(BaseValidatorModel):
    profileId: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    businessName: Optional[str] = None


class X12Delimiters(BaseValidatorModel):
    componentSeparator: Optional[str] = None
    dataElementSeparator: Optional[str] = None
    segmentTerminator: Optional[str] = None


class X12FunctionalGroupHeaders(BaseValidatorModel):
    applicationSenderCode: Optional[str] = None
    applicationReceiverCode: Optional[str] = None
    responsibleAgencyCode: Optional[str] = None


class X12InterchangeControlHeaders(BaseValidatorModel):
    senderIdQualifier: Optional[str] = None
    senderId: Optional[str] = None
    receiverIdQualifier: Optional[str] = None
    receiverId: Optional[str] = None
    repetitionSeparator: Optional[str] = None
    acknowledgmentRequestedCode: Optional[str] = None
    usageIndicatorCode: Optional[str] = None


class ConversionSource(BaseValidatorModel):
    fileFormat: ConversionSourceFormatType
    inputFile: InputFileSource


class ConversionTargetFormatDetails(BaseValidatorModel):
    x12: Optional[X12Details] = None


class EdiType(BaseValidatorModel):
    x12Details: Optional[X12Details] = None


class FormatOptions(BaseValidatorModel):
    x12: Optional[X12Details] = None


class TemplateDetails(BaseValidatorModel):
    x12: Optional[X12Details] = None


class OutputSampleFileSource(BaseValidatorModel):
    fileLocation: Optional[S3Location] = None


class StartTransformerJobRequest(BaseValidatorModel):
    inputFile: S3Location
    outputLocation: S3Location
    transformerId: str
    clientToken: Optional[str] = None


class CreateProfileRequest(BaseValidatorModel):
    name: str
    phone: str
    businessName: str
    logging: LoggingType
    email: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class CreateProfileResponse(BaseValidatorModel):
    profileId: str
    profileArn: str
    name: str
    businessName: str
    phone: str
    email: str
    logging: LoggingType
    logGroupName: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class CreateStarterMappingTemplateResponse(BaseValidatorModel):
    mappingTemplate: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GenerateMappingResponse(BaseValidatorModel):
    mappingTemplate: str
    mappingAccuracy: float
    ResponseMetadata: ResponseMetadata


class GetProfileResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class GetTransformerJobResponse(BaseValidatorModel):
    status: TransformerJobStatusType
    outputFiles: List[S3Location]
    message: str
    ResponseMetadata: ResponseMetadata


class CapabilitySummary(BaseValidatorModel):
    pass


class ListCapabilitiesResponse(BaseValidatorModel):
    capabilities: List[CapabilitySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class StartTransformerJobResponse(BaseValidatorModel):
    transformerJobId: str
    ResponseMetadata: ResponseMetadata


class TestConversionResponse(BaseValidatorModel):
    convertedFileContent: str
    validationMessages: List[str]
    ResponseMetadata: ResponseMetadata


class TestMappingResponse(BaseValidatorModel):
    mappedFileContent: str
    ResponseMetadata: ResponseMetadata


class TestParsingResponse(BaseValidatorModel):
    parsedFileContent: str
    ResponseMetadata: ResponseMetadata


class UpdateProfileResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


class ListCapabilitiesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPartnershipsRequestPaginate(BaseValidatorModel):
    profileId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProfilesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTransformersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProfilesResponse(BaseValidatorModel):
    profiles: List[ProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SampleDocumentKeys(BaseValidatorModel):
    pass


class SampleDocumentsOutput(BaseValidatorModel):
    bucketName: str
    keys: List[SampleDocumentKeys]


class SampleDocuments(BaseValidatorModel):
    bucketName: str
    keys: Sequence[SampleDocumentKeys]


class X12OutboundEdiHeaders(BaseValidatorModel):
    interchangeControlHeaders: Optional[X12InterchangeControlHeaders] = None
    functionalGroupHeaders: Optional[X12FunctionalGroupHeaders] = None
    delimiters: Optional[X12Delimiters] = None
    validateEdi: Optional[bool] = None


class TestParsingRequest(BaseValidatorModel):
    inputFile: S3Location
    fileFormat: FileFormatType
    ediType: EdiType


class InputConversion(BaseValidatorModel):
    fromFormat: Literal["X12"]
    formatOptions: Optional[FormatOptions] = None


class OutputConversion(BaseValidatorModel):
    toFormat: Literal["X12"]
    formatOptions: Optional[FormatOptions] = None


class CreateStarterMappingTemplateRequest(BaseValidatorModel):
    mappingType: MappingTypeType
    templateDetails: TemplateDetails
    outputSampleLocation: Optional[S3Location] = None


class ConversionTarget(BaseValidatorModel):
    fileFormat: Literal["X12"]
    formatDetails: Optional[ConversionTargetFormatDetails] = None
    outputSampleFile: Optional[OutputSampleFileSource] = None


class X12Envelope(BaseValidatorModel):
    common: Optional[X12OutboundEdiHeaders] = None


class EdiConfiguration(BaseValidatorModel):
    pass


class CapabilityConfiguration(BaseValidatorModel):
    edi: Optional[EdiConfiguration] = None


class CreateTransformerResponse(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiType
    sampleDocument: str
    inputConversion: InputConversion
    mapping: MappingType
    outputConversion: OutputConversion
    sampleDocuments: SampleDocumentsOutput
    ResponseMetadata: ResponseMetadata


class GetTransformerResponse(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiType
    sampleDocument: str
    inputConversion: InputConversion
    mapping: MappingType
    outputConversion: OutputConversion
    sampleDocuments: SampleDocumentsOutput
    ResponseMetadata: ResponseMetadata


class TransformerSummary(BaseValidatorModel):
    transformerId: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: Optional[datetime] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiType] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversion] = None
    mapping: Optional[MappingType] = None
    outputConversion: Optional[OutputConversion] = None
    sampleDocuments: Optional[SampleDocumentsOutput] = None


class UpdateTransformerResponse(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    status: TransformerStatusType
    createdAt: datetime
    modifiedAt: datetime
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiType
    sampleDocument: str
    inputConversion: InputConversion
    mapping: MappingType
    outputConversion: OutputConversion
    sampleDocuments: SampleDocumentsOutput
    ResponseMetadata: ResponseMetadata


class TestConversionRequest(BaseValidatorModel):
    source: ConversionSource
    target: ConversionTarget


class SampleDocumentsUnion(BaseValidatorModel):
    pass


class CreateTransformerRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiType] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversion] = None
    mapping: Optional[MappingType] = None
    outputConversion: Optional[OutputConversion] = None
    sampleDocuments: Optional[SampleDocumentsUnion] = None


class UpdateTransformerRequest(BaseValidatorModel):
    transformerId: str
    name: Optional[str] = None
    status: Optional[TransformerStatusType] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiType] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversion] = None
    mapping: Optional[MappingType] = None
    outputConversion: Optional[OutputConversion] = None
    sampleDocuments: Optional[SampleDocumentsUnion] = None


class OutboundEdiOptions(BaseValidatorModel):
    x12: Optional[X12Envelope] = None


class UpdateCapabilityRequest(BaseValidatorModel):
    capabilityId: str
    name: Optional[str] = None
    configuration: Optional[CapabilityConfiguration] = None
    instructionsDocuments: Optional[Sequence[S3Location]] = None


class ListTransformersResponse(BaseValidatorModel):
    transformers: List[TransformerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CapabilityOptions(BaseValidatorModel):
    outboundEdi: Optional[OutboundEdiOptions] = None


class CreatePartnershipRequest(BaseValidatorModel):
    profileId: str
    name: str
    email: str
    capabilities: Sequence[str]
    phone: Optional[str] = None
    capabilityOptions: Optional[CapabilityOptions] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class CreatePartnershipResponse(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptions
    tradingPartnerId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class GetPartnershipResponse(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptions
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadata


class PartnershipSummary(BaseValidatorModel):
    profileId: str
    partnershipId: str
    createdAt: datetime
    name: Optional[str] = None
    capabilities: Optional[List[str]] = None
    capabilityOptions: Optional[CapabilityOptions] = None
    tradingPartnerId: Optional[str] = None
    modifiedAt: Optional[datetime] = None


class UpdatePartnershipRequest(BaseValidatorModel):
    partnershipId: str
    name: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None
    capabilityOptions: Optional[CapabilityOptions] = None


class UpdatePartnershipResponse(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    capabilityOptions: CapabilityOptions
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadata


class ListPartnershipsResponse(BaseValidatorModel):
    partnerships: List[PartnershipSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


