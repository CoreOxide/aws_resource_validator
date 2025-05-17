from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.b2bi.b2bi_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CapabilitySummary(BaseValidatorModel):
    capabilityId: str
    name: str
    type: Literal['edi']
    createdAt: datetime
    modifiedAt: Optional[datetime] = None


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


class Mapping(BaseValidatorModel):
    templateLanguage: MappingTemplateLanguageType
    template: Optional[str] = None


# This class is the input for the 'delete_capability' function.
class DeleteCapabilityRequest(BaseValidatorModel):
    capabilityId: str


# This class is the input for the 'delete_partnership' function.
class DeletePartnershipRequest(BaseValidatorModel):
    partnershipId: str


# This class is the input for the 'delete_profile' function.
class DeleteProfileRequest(BaseValidatorModel):
    profileId: str


# This class is the input for the 'delete_transformer' function.
class DeleteTransformerRequest(BaseValidatorModel):
    transformerId: str


# This class is the input for the 'generate_mapping' function.
class GenerateMappingRequest(BaseValidatorModel):
    inputFileContent: str
    outputFileContent: str
    mappingType: MappingTypeType


# This class is the input for the 'get_capability' function.
class GetCapabilityRequest(BaseValidatorModel):
    capabilityId: str


# This class is the input for the 'get_partnership' function.
class GetPartnershipRequest(BaseValidatorModel):
    partnershipId: str


# This class is the input for the 'get_profile' function.
class GetProfileRequest(BaseValidatorModel):
    profileId: str


# This class is the input for the 'get_transformer_job' function.
class GetTransformerJobRequest(BaseValidatorModel):
    transformerJobId: str
    transformerId: str


# This class is the input for the 'get_transformer' function.
class GetTransformerRequest(BaseValidatorModel):
    transformerId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_capabilities' function.
class ListCapabilitiesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_partnerships' function.
class ListPartnershipsRequest(BaseValidatorModel):
    profileId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_profiles' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


# This class is the input for the 'list_transformers' function.
class ListTransformersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SampleDocumentKeys(BaseValidatorModel):
    input: Optional[str] = None
    output: Optional[str] = None


# This class is the input for the 'test_mapping' function.
class TestMappingRequest(BaseValidatorModel):
    inputFileContent: str
    mappingTemplate: str
    fileFormat: FileFormatType


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: List[str]


# This class is the input for the 'update_profile' function.
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


# This class is the input for the 'start_transformer_job' function.
class StartTransformerJobRequest(BaseValidatorModel):
    inputFile: S3Location
    outputLocation: S3Location
    transformerId: str
    clientToken: Optional[str] = None


# This class is the input for the 'create_profile' function.
class CreateProfileRequest(BaseValidatorModel):
    name: str
    phone: str
    businessName: str
    logging: LoggingType
    email: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: List[Tag]


# This class is the output for the 'create_profile' function.
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


# This class is the output for the 'create_starter_mapping_template' function.
class CreateStarterMappingTemplateResponse(BaseValidatorModel):
    mappingTemplate: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'generate_mapping' function.
class GenerateMappingResponse(BaseValidatorModel):
    mappingTemplate: str
    mappingAccuracy: float
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_profile' function.
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


# This class is the output for the 'get_transformer_job' function.
class GetTransformerJobResponse(BaseValidatorModel):
    status: TransformerJobStatusType
    outputFiles: List[S3Location]
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_capabilities' function.
class ListCapabilitiesResponse(BaseValidatorModel):
    capabilities: List[CapabilitySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_transformer_job' function.
class StartTransformerJobResponse(BaseValidatorModel):
    transformerJobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_conversion' function.
class TestConversionResponse(BaseValidatorModel):
    convertedFileContent: str
    validationMessages: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_mapping' function.
class TestMappingResponse(BaseValidatorModel):
    mappedFileContent: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_parsing' function.
class TestParsingResponse(BaseValidatorModel):
    parsedFileContent: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_profile' function.
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


# This class is the output for the 'list_profiles' function.
class ListProfilesResponse(BaseValidatorModel):
    profiles: List[ProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SampleDocumentsOutput(BaseValidatorModel):
    bucketName: str
    keys: List[SampleDocumentKeys]


class SampleDocuments(BaseValidatorModel):
    bucketName: str
    keys: List[SampleDocumentKeys]


class X12OutboundEdiHeaders(BaseValidatorModel):
    interchangeControlHeaders: Optional[X12InterchangeControlHeaders] = None
    functionalGroupHeaders: Optional[X12FunctionalGroupHeaders] = None
    delimiters: Optional[X12Delimiters] = None
    validateEdi: Optional[bool] = None


class EdiConfiguration(BaseValidatorModel):
    type: EdiType
    inputLocation: S3Location
    outputLocation: S3Location
    transformerId: str
    capabilityDirection: Optional[CapabilityDirectionType] = None


# This class is the input for the 'test_parsing' function.
class TestParsingRequest(BaseValidatorModel):
    inputFile: S3Location
    fileFormat: FileFormatType
    ediType: EdiType


class InputConversion(BaseValidatorModel):
    fromFormat: Literal['X12']
    formatOptions: Optional[FormatOptions] = None


class OutputConversion(BaseValidatorModel):
    toFormat: Literal['X12']
    formatOptions: Optional[FormatOptions] = None


# This class is the input for the 'create_starter_mapping_template' function.
class CreateStarterMappingTemplateRequest(BaseValidatorModel):
    mappingType: MappingTypeType
    templateDetails: TemplateDetails
    outputSampleLocation: Optional[S3Location] = None


class ConversionTarget(BaseValidatorModel):
    fileFormat: Literal['X12']
    formatDetails: Optional[ConversionTargetFormatDetails] = None
    outputSampleFile: Optional[OutputSampleFileSource] = None

SampleDocumentsUnion = Union[SampleDocuments, SampleDocumentsOutput]


class X12Envelope(BaseValidatorModel):
    common: Optional[X12OutboundEdiHeaders] = None


class CapabilityConfiguration(BaseValidatorModel):
    edi: Optional[EdiConfiguration] = None


# This class is the output for the 'create_transformer' function.
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
    mapping: Mapping
    outputConversion: OutputConversion
    sampleDocuments: SampleDocumentsOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transformer' function.
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
    mapping: Mapping
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
    mapping: Optional[Mapping] = None
    outputConversion: Optional[OutputConversion] = None
    sampleDocuments: Optional[SampleDocumentsOutput] = None


# This class is the output for the 'update_transformer' function.
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
    mapping: Mapping
    outputConversion: OutputConversion
    sampleDocuments: SampleDocumentsOutput
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'test_conversion' function.
class TestConversionRequest(BaseValidatorModel):
    source: ConversionSource
    target: ConversionTarget


# This class is the input for the 'create_transformer' function.
class CreateTransformerRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiType] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversion] = None
    mapping: Optional[Mapping] = None
    outputConversion: Optional[OutputConversion] = None
    sampleDocuments: Optional[SampleDocumentsUnion] = None


# This class is the input for the 'update_transformer' function.
class UpdateTransformerRequest(BaseValidatorModel):
    transformerId: str
    name: Optional[str] = None
    status: Optional[TransformerStatusType] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    ediType: Optional[EdiType] = None
    sampleDocument: Optional[str] = None
    inputConversion: Optional[InputConversion] = None
    mapping: Optional[Mapping] = None
    outputConversion: Optional[OutputConversion] = None
    sampleDocuments: Optional[SampleDocumentsUnion] = None


class OutboundEdiOptions(BaseValidatorModel):
    x12: Optional[X12Envelope] = None


# This class is the input for the 'create_capability' function.
class CreateCapabilityRequest(BaseValidatorModel):
    name: str
    type: Literal['edi']
    configuration: CapabilityConfiguration
    instructionsDocuments: Optional[List[S3Location]] = None
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'create_capability' function.
class CreateCapabilityResponse(BaseValidatorModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal['edi']
    configuration: CapabilityConfiguration
    instructionsDocuments: List[S3Location]
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_capability' function.
class GetCapabilityResponse(BaseValidatorModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal['edi']
    configuration: CapabilityConfiguration
    instructionsDocuments: List[S3Location]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_capability' function.
class UpdateCapabilityRequest(BaseValidatorModel):
    capabilityId: str
    name: Optional[str] = None
    configuration: Optional[CapabilityConfiguration] = None
    instructionsDocuments: Optional[List[S3Location]] = None


# This class is the output for the 'update_capability' function.
class UpdateCapabilityResponse(BaseValidatorModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal['edi']
    configuration: CapabilityConfiguration
    instructionsDocuments: List[S3Location]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_transformers' function.
class ListTransformersResponse(BaseValidatorModel):
    transformers: List[TransformerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CapabilityOptions(BaseValidatorModel):
    outboundEdi: Optional[OutboundEdiOptions] = None


# This class is the input for the 'create_partnership' function.
class CreatePartnershipRequest(BaseValidatorModel):
    profileId: str
    name: str
    email: str
    capabilities: List[str]
    phone: Optional[str] = None
    capabilityOptions: Optional[CapabilityOptions] = None
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'create_partnership' function.
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


# This class is the output for the 'get_partnership' function.
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


# This class is the input for the 'update_partnership' function.
class UpdatePartnershipRequest(BaseValidatorModel):
    partnershipId: str
    name: Optional[str] = None
    capabilities: Optional[List[str]] = None
    capabilityOptions: Optional[CapabilityOptions] = None


# This class is the output for the 'update_partnership' function.
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


# This class is the output for the 'list_partnerships' function.
class ListPartnershipsResponse(BaseValidatorModel):
    partnerships: List[PartnershipSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None