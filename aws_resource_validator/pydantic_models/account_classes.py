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
from aws_resource_validator.pydantic_models.account_constants import *

class AcceptPrimaryEmailUpdateRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Otp: str
    PrimaryEmail: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AlternateContactTypeDef(BaseValidatorModel):
    AlternateContactType: Optional[AlternateContactTypeType] = None
    EmailAddress: Optional[str] = None
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Title: Optional[str] = None


class ContactInformationTypeDef(BaseValidatorModel):
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


class DeleteAlternateContactRequestTypeDef(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None


class DisableRegionRequestTypeDef(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


class EnableRegionRequestTypeDef(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


class GetAlternateContactRequestTypeDef(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None


class GetContactInformationRequestTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None


class GetPrimaryEmailRequestTypeDef(BaseValidatorModel):
    AccountId: str


class GetRegionOptStatusRequestTypeDef(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRegionsRequestTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RegionOptStatusContains: Optional[Sequence[RegionOptStatusType]] = None


class RegionTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None
    RegionOptStatus: Optional[RegionOptStatusType] = None


class PutAlternateContactRequestTypeDef(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    EmailAddress: str
    Name: str
    PhoneNumber: str
    Title: str
    AccountId: Optional[str] = None


class StartPrimaryEmailUpdateRequestTypeDef(BaseValidatorModel):
    AccountId: str
    PrimaryEmail: str


class AcceptPrimaryEmailUpdateResponseTypeDef(BaseValidatorModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetPrimaryEmailResponseTypeDef(BaseValidatorModel):
    PrimaryEmail: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRegionOptStatusResponseTypeDef(BaseValidatorModel):
    RegionName: str
    RegionOptStatus: RegionOptStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class StartPrimaryEmailUpdateResponseTypeDef(BaseValidatorModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetAlternateContactResponseTypeDef(BaseValidatorModel):
    AlternateContact: AlternateContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetContactInformationResponseTypeDef(BaseValidatorModel):
    ContactInformation: ContactInformationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutContactInformationRequestTypeDef(BaseValidatorModel):
    ContactInformation: ContactInformationTypeDef
    AccountId: Optional[str] = None


class ListRegionsRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    RegionOptStatusContains: Optional[Sequence[RegionOptStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRegionsResponseTypeDef(BaseValidatorModel):
    Regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


