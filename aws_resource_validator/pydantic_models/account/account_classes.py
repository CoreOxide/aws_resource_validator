from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.account.account_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceptPrimaryEmailUpdateRequest(BaseValidatorModel):
    AccountId: str
    Otp: str
    PrimaryEmail: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AlternateContact(BaseValidatorModel):
    AlternateContactType: Optional[AlternateContactTypeType] = None
    EmailAddress: Optional[str] = None
    Name: Optional[str] = None
    PhoneNumber: Optional[str] = None
    Title: Optional[str] = None


class ContactInformation(BaseValidatorModel):
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


class DeleteAlternateContactRequest(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None


class DisableRegionRequest(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


class EnableRegionRequest(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


class GetAlternateContactRequest(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None


class GetContactInformationRequest(BaseValidatorModel):
    AccountId: Optional[str] = None


class GetPrimaryEmailRequest(BaseValidatorModel):
    AccountId: str


class GetRegionOptStatusRequest(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRegionsRequest(BaseValidatorModel):
    AccountId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RegionOptStatusContains: Optional[List[RegionOptStatusType]] = None


class Region(BaseValidatorModel):
    RegionName: Optional[str] = None
    RegionOptStatus: Optional[RegionOptStatusType] = None


class PutAlternateContactRequest(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    EmailAddress: str
    Name: str
    PhoneNumber: str
    Title: str
    AccountId: Optional[str] = None


class StartPrimaryEmailUpdateRequest(BaseValidatorModel):
    AccountId: str
    PrimaryEmail: str


class AcceptPrimaryEmailUpdateResponse(BaseValidatorModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetPrimaryEmailResponse(BaseValidatorModel):
    PrimaryEmail: str
    ResponseMetadata: ResponseMetadata


class GetRegionOptStatusResponse(BaseValidatorModel):
    RegionName: str
    RegionOptStatus: RegionOptStatusType
    ResponseMetadata: ResponseMetadata


class StartPrimaryEmailUpdateResponse(BaseValidatorModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadata


class GetAlternateContactResponse(BaseValidatorModel):
    AlternateContact: AlternateContact
    ResponseMetadata: ResponseMetadata


class GetContactInformationResponse(BaseValidatorModel):
    ContactInformation: ContactInformation
    ResponseMetadata: ResponseMetadata


class PutContactInformationRequest(BaseValidatorModel):
    ContactInformation: ContactInformation
    AccountId: Optional[str] = None


class ListRegionsRequestPaginate(BaseValidatorModel):
    AccountId: Optional[str] = None
    RegionOptStatusContains: Optional[List[RegionOptStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegionsResponse(BaseValidatorModel):
    Regions: List[Region]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None