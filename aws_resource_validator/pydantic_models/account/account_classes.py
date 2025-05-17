from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.account.account_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_primary_email_update' function.
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


# This class is the input for the 'delete_alternate_contact' function.
class DeleteAlternateContactRequest(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None


# This class is the input for the 'disable_region' function.
class DisableRegionRequest(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


# This class is the input for the 'enable_region' function.
class EnableRegionRequest(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


# This class is the input for the 'get_alternate_contact' function.
class GetAlternateContactRequest(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    AccountId: Optional[str] = None


# This class is the input for the 'get_contact_information' function.
class GetContactInformationRequest(BaseValidatorModel):
    AccountId: Optional[str] = None


# This class is the input for the 'get_primary_email' function.
class GetPrimaryEmailRequest(BaseValidatorModel):
    AccountId: str


# This class is the input for the 'get_region_opt_status' function.
class GetRegionOptStatusRequest(BaseValidatorModel):
    RegionName: str
    AccountId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_regions' function.
class ListRegionsRequest(BaseValidatorModel):
    AccountId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RegionOptStatusContains: Optional[List[RegionOptStatusType]] = None


class Region(BaseValidatorModel):
    RegionName: Optional[str] = None
    RegionOptStatus: Optional[RegionOptStatusType] = None


# This class is the input for the 'put_alternate_contact' function.
class PutAlternateContactRequest(BaseValidatorModel):
    AlternateContactType: AlternateContactTypeType
    EmailAddress: str
    Name: str
    PhoneNumber: str
    Title: str
    AccountId: Optional[str] = None


# This class is the input for the 'start_primary_email_update' function.
class StartPrimaryEmailUpdateRequest(BaseValidatorModel):
    AccountId: str
    PrimaryEmail: str


# This class is the output for the 'accept_primary_email_update' function.
class AcceptPrimaryEmailUpdateResponse(BaseValidatorModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_contact_information' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_primary_email' function.
class GetPrimaryEmailResponse(BaseValidatorModel):
    PrimaryEmail: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_region_opt_status' function.
class GetRegionOptStatusResponse(BaseValidatorModel):
    RegionName: str
    RegionOptStatus: RegionOptStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_primary_email_update' function.
class StartPrimaryEmailUpdateResponse(BaseValidatorModel):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_alternate_contact' function.
class GetAlternateContactResponse(BaseValidatorModel):
    AlternateContact: AlternateContact
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_contact_information' function.
class GetContactInformationResponse(BaseValidatorModel):
    ContactInformation: ContactInformation
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_contact_information' function.
class PutContactInformationRequest(BaseValidatorModel):
    ContactInformation: ContactInformation
    AccountId: Optional[str] = None


class ListRegionsRequestPaginate(BaseValidatorModel):
    AccountId: Optional[str] = None
    RegionOptStatusContains: Optional[List[RegionOptStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_regions' function.
class ListRegionsResponse(BaseValidatorModel):
    Regions: List[Region]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None