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
from aws_resource_validator.pydantic_models.b2bi_constants import *

class CapabilitySummaryTypeDef(BaseValidatorModel):
    capabilityId: str
    name: str
    type: Literal["edi"]
    createdAt: datetime
    modifiedAt: Optional[datetime] = None

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

class DeleteCapabilityRequestRequestTypeDef(BaseValidatorModel):
    capabilityId: str

class DeletePartnershipRequestRequestTypeDef(BaseValidatorModel):
    partnershipId: str

class DeleteProfileRequestRequestTypeDef(BaseValidatorModel):
    profileId: str

class DeleteTransformerRequestRequestTypeDef(BaseValidatorModel):
    transformerId: str

class X12DetailsTypeDef(BaseValidatorModel):
    transactionSet: Optional[X12TransactionSetType] = None
    version: Optional[X12VersionType] = None

class GetCapabilityRequestRequestTypeDef(BaseValidatorModel):
    capabilityId: str

class GetPartnershipRequestRequestTypeDef(BaseValidatorModel):
    partnershipId: str

class GetProfileRequestRequestTypeDef(BaseValidatorModel):
    profileId: str

class GetTransformerJobRequestRequestTypeDef(BaseValidatorModel):
    transformerJobId: str
    transformerId: str

class GetTransformerRequestRequestTypeDef(BaseValidatorModel):
    transformerId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCapabilitiesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPartnershipsRequestRequestTypeDef(BaseValidatorModel):
    profileId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PartnershipSummaryTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    createdAt: datetime
    name: Optional[str] = None
    capabilities: Optional[List[str]] = None
    tradingPartnerId: Optional[str] = None
    modifiedAt: Optional[datetime] = None

class ListProfilesRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class ListTransformersRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestMappingRequestRequestTypeDef(BaseValidatorModel):
    inputFileContent: str
    mappingTemplate: str
    fileFormat: FileFormatType

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdatePartnershipRequestRequestTypeDef(BaseValidatorModel):
    partnershipId: str
    name: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None

class UpdateProfileRequestRequestTypeDef(BaseValidatorModel):
    profileId: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    businessName: Optional[str] = None

class StartTransformerJobRequestRequestTypeDef(BaseValidatorModel):
    inputFile: S3LocationTypeDef
    outputLocation: S3LocationTypeDef
    transformerId: str
    clientToken: Optional[str] = None

class CreatePartnershipRequestRequestTypeDef(BaseValidatorModel):
    profileId: str
    name: str
    email: str
    capabilities: Sequence[str]
    phone: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateProfileRequestRequestTypeDef(BaseValidatorModel):
    name: str
    phone: str
    businessName: str
    logging: LoggingType
    email: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreatePartnershipResponseTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    tradingPartnerId: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

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

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartnershipResponseTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
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

class ListCapabilitiesResponseTypeDef(BaseValidatorModel):
    capabilities: List[CapabilitySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTransformerJobResponseTypeDef(BaseValidatorModel):
    transformerJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestMappingResponseTypeDef(BaseValidatorModel):
    mappedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestParsingResponseTypeDef(BaseValidatorModel):
    parsedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePartnershipResponseTypeDef(BaseValidatorModel):
    profileId: str
    partnershipId: str
    partnershipArn: str
    name: str
    email: str
    phone: str
    capabilities: List[str]
    tradingPartnerId: str
    createdAt: datetime
    modifiedAt: datetime
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

class EdiTypeTypeDef(BaseValidatorModel):
    x12Details: Optional[X12DetailsTypeDef] = None

class ListCapabilitiesRequestListCapabilitiesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPartnershipsRequestListPartnershipsPaginateTypeDef(BaseValidatorModel):
    profileId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesRequestListProfilesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTransformersRequestListTransformersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPartnershipsResponseTypeDef(BaseValidatorModel):
    partnerships: List[PartnershipSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilesResponseTypeDef(BaseValidatorModel):
    profiles: List[ProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransformerRequestRequestTypeDef(BaseValidatorModel):
    name: str
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateTransformerResponseTypeDef(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    fileFormat: FileFormatType
    mappingTemplate: str
    status: TransformerStatusType
    ediType: EdiTypeTypeDef
    sampleDocument: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EdiConfigurationTypeDef(BaseValidatorModel):
    type: EdiTypeTypeDef
    inputLocation: S3LocationTypeDef
    outputLocation: S3LocationTypeDef
    transformerId: str

class GetTransformerResponseTypeDef(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    fileFormat: FileFormatType
    mappingTemplate: str
    status: TransformerStatusType
    ediType: EdiTypeTypeDef
    sampleDocument: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TestParsingRequestRequestTypeDef(BaseValidatorModel):
    inputFile: S3LocationTypeDef
    fileFormat: FileFormatType
    ediType: EdiTypeTypeDef

class TransformerSummaryTypeDef(BaseValidatorModel):
    transformerId: str
    name: str
    fileFormat: FileFormatType
    mappingTemplate: str
    status: TransformerStatusType
    ediType: EdiTypeTypeDef
    createdAt: datetime
    sampleDocument: Optional[str] = None
    modifiedAt: Optional[datetime] = None

class UpdateTransformerRequestRequestTypeDef(BaseValidatorModel):
    transformerId: str
    name: Optional[str] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    status: Optional[TransformerStatusType] = None
    ediType: Optional[EdiTypeTypeDef] = None
    sampleDocument: Optional[str] = None

class UpdateTransformerResponseTypeDef(BaseValidatorModel):
    transformerId: str
    transformerArn: str
    name: str
    fileFormat: FileFormatType
    mappingTemplate: str
    status: TransformerStatusType
    ediType: EdiTypeTypeDef
    sampleDocument: str
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CapabilityConfigurationTypeDef(BaseValidatorModel):
    edi: Optional[EdiConfigurationTypeDef] = None

class ListTransformersResponseTypeDef(BaseValidatorModel):
    transformers: List[TransformerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCapabilityRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: Optional[Sequence[S3LocationTypeDef]] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateCapabilityResponseTypeDef(BaseValidatorModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: List[S3LocationTypeDef]
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetCapabilityResponseTypeDef(BaseValidatorModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: List[S3LocationTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCapabilityRequestRequestTypeDef(BaseValidatorModel):
    capabilityId: str
    name: Optional[str] = None
    configuration: Optional[CapabilityConfigurationTypeDef] = None
    instructionsDocuments: Optional[Sequence[S3LocationTypeDef]] = None

class UpdateCapabilityResponseTypeDef(BaseValidatorModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: List[S3LocationTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

