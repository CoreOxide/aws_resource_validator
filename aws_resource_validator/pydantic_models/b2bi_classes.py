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
from aws_resource_validator.pydantic_models.b2bi_constants import *

class CapabilitySummaryTypeDef(BaseModel):
    capabilityId: str
    name: str
    type: Literal["edi"]
    createdAt: datetime
    modifiedAt: Optional[datetime] = None

class S3LocationTypeDef(BaseModel):
    bucketName: Optional[str] = None
    key: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteCapabilityRequestRequestTypeDef(BaseModel):
    capabilityId: str

class DeletePartnershipRequestRequestTypeDef(BaseModel):
    partnershipId: str

class DeleteProfileRequestRequestTypeDef(BaseModel):
    profileId: str

class DeleteTransformerRequestRequestTypeDef(BaseModel):
    transformerId: str

class X12DetailsTypeDef(BaseModel):
    transactionSet: Optional[X12TransactionSetType] = None
    version: Optional[X12VersionType] = None

class GetCapabilityRequestRequestTypeDef(BaseModel):
    capabilityId: str

class GetPartnershipRequestRequestTypeDef(BaseModel):
    partnershipId: str

class GetProfileRequestRequestTypeDef(BaseModel):
    profileId: str

class GetTransformerJobRequestRequestTypeDef(BaseModel):
    transformerJobId: str
    transformerId: str

class GetTransformerRequestRequestTypeDef(BaseModel):
    transformerId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListCapabilitiesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPartnershipsRequestRequestTypeDef(BaseModel):
    profileId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PartnershipSummaryTypeDef(BaseModel):
    profileId: str
    partnershipId: str
    createdAt: datetime
    name: Optional[str] = None
    capabilities: Optional[List[str]] = None
    tradingPartnerId: Optional[str] = None
    modifiedAt: Optional[datetime] = None

class ListProfilesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ProfileSummaryTypeDef(BaseModel):
    profileId: str
    name: str
    businessName: str
    createdAt: datetime
    logging: Optional[LoggingType] = None
    logGroupName: Optional[str] = None
    modifiedAt: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListTransformersRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TestMappingRequestRequestTypeDef(BaseModel):
    inputFileContent: str
    mappingTemplate: str
    fileFormat: FileFormatType

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdatePartnershipRequestRequestTypeDef(BaseModel):
    partnershipId: str
    name: Optional[str] = None
    capabilities: Optional[Sequence[str]] = None

class UpdateProfileRequestRequestTypeDef(BaseModel):
    profileId: str
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    businessName: Optional[str] = None

class StartTransformerJobRequestRequestTypeDef(BaseModel):
    inputFile: S3LocationTypeDef
    outputLocation: S3LocationTypeDef
    transformerId: str
    clientToken: Optional[str] = None

class CreatePartnershipRequestRequestTypeDef(BaseModel):
    profileId: str
    name: str
    email: str
    capabilities: Sequence[str]
    phone: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateProfileRequestRequestTypeDef(BaseModel):
    name: str
    phone: str
    businessName: str
    logging: LoggingType
    email: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreatePartnershipResponseTypeDef(BaseModel):
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

class CreateProfileResponseTypeDef(BaseModel):
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

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartnershipResponseTypeDef(BaseModel):
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

class GetProfileResponseTypeDef(BaseModel):
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

class GetTransformerJobResponseTypeDef(BaseModel):
    status: TransformerJobStatusType
    outputFiles: List[S3LocationTypeDef]
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapabilitiesResponseTypeDef(BaseModel):
    capabilities: List[CapabilitySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTransformerJobResponseTypeDef(BaseModel):
    transformerJobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestMappingResponseTypeDef(BaseModel):
    mappedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestParsingResponseTypeDef(BaseModel):
    parsedFileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePartnershipResponseTypeDef(BaseModel):
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

class UpdateProfileResponseTypeDef(BaseModel):
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

class EdiTypeTypeDef(BaseModel):
    x12Details: Optional[X12DetailsTypeDef] = None

class ListCapabilitiesRequestListCapabilitiesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPartnershipsRequestListPartnershipsPaginateTypeDef(BaseModel):
    profileId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesRequestListProfilesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTransformersRequestListTransformersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPartnershipsResponseTypeDef(BaseModel):
    partnerships: List[PartnershipSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfilesResponseTypeDef(BaseModel):
    profiles: List[ProfileSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransformerRequestRequestTypeDef(BaseModel):
    name: str
    fileFormat: FileFormatType
    mappingTemplate: str
    ediType: EdiTypeTypeDef
    sampleDocument: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateTransformerResponseTypeDef(BaseModel):
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

class EdiConfigurationTypeDef(BaseModel):
    type: EdiTypeTypeDef
    inputLocation: S3LocationTypeDef
    outputLocation: S3LocationTypeDef
    transformerId: str

class GetTransformerResponseTypeDef(BaseModel):
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

class TestParsingRequestRequestTypeDef(BaseModel):
    inputFile: S3LocationTypeDef
    fileFormat: FileFormatType
    ediType: EdiTypeTypeDef

class TransformerSummaryTypeDef(BaseModel):
    transformerId: str
    name: str
    fileFormat: FileFormatType
    mappingTemplate: str
    status: TransformerStatusType
    ediType: EdiTypeTypeDef
    createdAt: datetime
    sampleDocument: Optional[str] = None
    modifiedAt: Optional[datetime] = None

class UpdateTransformerRequestRequestTypeDef(BaseModel):
    transformerId: str
    name: Optional[str] = None
    fileFormat: Optional[FileFormatType] = None
    mappingTemplate: Optional[str] = None
    status: Optional[TransformerStatusType] = None
    ediType: Optional[EdiTypeTypeDef] = None
    sampleDocument: Optional[str] = None

class UpdateTransformerResponseTypeDef(BaseModel):
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

class CapabilityConfigurationTypeDef(BaseModel):
    edi: Optional[EdiConfigurationTypeDef] = None

class ListTransformersResponseTypeDef(BaseModel):
    transformers: List[TransformerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCapabilityRequestRequestTypeDef(BaseModel):
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: Optional[Sequence[S3LocationTypeDef]] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateCapabilityResponseTypeDef(BaseModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: List[S3LocationTypeDef]
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetCapabilityResponseTypeDef(BaseModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: List[S3LocationTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCapabilityRequestRequestTypeDef(BaseModel):
    capabilityId: str
    name: Optional[str] = None
    configuration: Optional[CapabilityConfigurationTypeDef] = None
    instructionsDocuments: Optional[Sequence[S3LocationTypeDef]] = None

class UpdateCapabilityResponseTypeDef(BaseModel):
    capabilityId: str
    capabilityArn: str
    name: str
    type: Literal["edi"]
    configuration: CapabilityConfigurationTypeDef
    instructionsDocuments: List[S3LocationTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

