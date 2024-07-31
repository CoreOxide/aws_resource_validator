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
from aws_resource_validator.pydantic_models.account_constants import *

class AcceptPrimaryEmailUpdateRequestRequestTypeDef(BaseModel):
    AccountId: str
    Otp: str
    PrimaryEmail: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AlternateContactTypeDef(BaseModel):
    AlternateContactType: Optional[AlternateContactTypeType] = None
    EmailAddress: Optional[str] = None
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Title: Optional[str] = None

class ContactInformationTypeDef(BaseModel):
    AddressLine1: str
    City: str
    CountryCode: str
    FullName: str
    PhoneNumber: str
    PostalCode: str
    AddressLine2: Optional[str] = None
    AddressLine3: Optional[str] = None
    CompanyName: Optional[str] = None
    DistrictOrCounty: Optional[str] = None
    StateOrRegion: Optional[str] = None
    WebsiteUrl: Optional[str] = None

class DeleteAlternateContactRequestRequestTypeDef(BaseModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None

class DisableRegionRequestRequestTypeDef(BaseModel):
    RegionName: str
    AccountId: Optional[str] = None

class EnableRegionRequestRequestTypeDef(BaseModel):
    RegionName: str
    AccountId: Optional[str] = None

class GetAlternateContactRequestRequestTypeDef(BaseModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None

class GetContactInformationRequestRequestTypeDef(BaseModel):
    AccountId: Optional[str] = None

class GetPrimaryEmailRequestRequestTypeDef(BaseModel):
    AccountId: str

class GetRegionOptStatusRequestRequestTypeDef(BaseModel):
    RegionName: str
    AccountId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRegionsRequestRequestTypeDef(BaseModel):
    AccountId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RegionOptStatusContains: Optional[Sequence[RegionOptStatusType]] = None

class RegionTypeDef(BaseModel):
    RegionName: Optional[str] = None
    RegionOptStatus: Optional[RegionOptStatusType] = None

class PutAlternateContactRequestRequestTypeDef(BaseModel):
    AlternateContactType: AlternateContactTypeType
    EmailAddress: str
    Name: str
    PhoneNumber: str
    Title: str
    AccountId: Optional[str] = None

class StartPrimaryEmailUpdateRequestRequestTypeDef(BaseModel):
    AccountId: str
    PrimaryEmail: str

class AcceptPrimaryEmailUpdateResponseTypeDef(BaseModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrimaryEmailResponseTypeDef(BaseModel):
    PrimaryEmail: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegionOptStatusResponseTypeDef(BaseModel):
    RegionName: str
    RegionOptStatus: RegionOptStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartPrimaryEmailUpdateResponseTypeDef(BaseModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAlternateContactResponseTypeDef(BaseModel):
    AlternateContact: AlternateContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactInformationResponseTypeDef(BaseModel):
    ContactInformation: ContactInformationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutContactInformationRequestRequestTypeDef(BaseModel):
    ContactInformation: ContactInformationTypeDef
    AccountId: Optional[str] = None

class ListRegionsRequestListRegionsPaginateTypeDef(BaseModel):
    AccountId: Optional[str] = None
    RegionOptStatusContains: Optional[Sequence[RegionOptStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegionsResponseTypeDef(BaseModel):
    Regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

