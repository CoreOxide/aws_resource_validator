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
from aws_resource_validator.pydantic_models.geo_places_constants import *

class AccessPoint(BaseValidatorModel):
    Position: Optional[List[float]] = None


class Category(BaseValidatorModel):
    Id: str
    Name: str
    LocalizedName: Optional[str] = None
    Primary: Optional[bool] = None


class AddressComponentMatchScores(BaseValidatorModel):
    Country: Optional[float] = None
    Region: Optional[float] = None
    SubRegion: Optional[float] = None
    Locality: Optional[float] = None
    District: Optional[float] = None
    SubDistrict: Optional[float] = None
    PostalCode: Optional[float] = None
    Block: Optional[float] = None
    SubBlock: Optional[float] = None
    Intersection: Optional[List[float]] = None
    AddressNumber: Optional[float] = None
    Building: Optional[float] = None


class PhonemeTranscription(BaseValidatorModel):
    Value: Optional[str] = None
    Language: Optional[str] = None
    Preferred: Optional[bool] = None


class Country(BaseValidatorModel):
    Code2: Optional[str] = None
    Code3: Optional[str] = None
    Name: Optional[str] = None


class Region(BaseValidatorModel):
    Code: Optional[str] = None
    Name: Optional[str] = None


class SubRegion(BaseValidatorModel):
    Code: Optional[str] = None
    Name: Optional[str] = None


class Highlight(BaseValidatorModel):
    StartIndex: Optional[int] = None
    EndIndex: Optional[int] = None
    Value: Optional[str] = None


class FilterCircle(BaseValidatorModel):
    Center: Sequence[float]
    Radius: int


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BusinessChain(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None


class FoodType(BaseValidatorModel):
    LocalizedName: str
    Id: Optional[str] = None
    Primary: Optional[bool] = None


class GeocodeFilter(BaseValidatorModel):
    IncludeCountries: Optional[Sequence[str]] = None
    IncludePlaceTypes: Optional[Sequence[GeocodeFilterPlaceTypeType]] = None


class GeocodeQueryComponents(BaseValidatorModel):
    Country: Optional[str] = None
    Region: Optional[str] = None
    SubRegion: Optional[str] = None
    Locality: Optional[str] = None
    District: Optional[str] = None
    Street: Optional[str] = None
    AddressNumber: Optional[str] = None
    PostalCode: Optional[str] = None


class TimeZone(BaseValidatorModel):
    Name: str
    Offset: Optional[str] = None
    OffsetSeconds: Optional[int] = None


class GetPlaceRequest(BaseValidatorModel):
    PlaceId: str
    AdditionalFeatures: Optional[Sequence[GetPlaceAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[GetPlaceIntendedUseType] = None
    Key: Optional[str] = None


class OpeningHoursComponents(BaseValidatorModel):
    OpenTime: Optional[str] = None
    OpenDuration: Optional[str] = None
    Recurrence: Optional[str] = None


class UspsZipPlus4(BaseValidatorModel):
    RecordTypeCode: Optional[RecordTypeCodeType] = None


class UspsZip(BaseValidatorModel):
    ZipClassificationCode: Optional[ZipClassificationCodeType] = None


class QueryRefinement(BaseValidatorModel):
    RefinedTerm: str
    OriginalTerm: str
    StartIndex: int
    EndIndex: int


class ReverseGeocodeFilter(BaseValidatorModel):
    IncludePlaceTypes: Optional[Sequence[ReverseGeocodeFilterPlaceTypeType]] = None


class SearchNearbyFilter(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    IncludeCountries: Optional[Sequence[str]] = None
    IncludeCategories: Optional[Sequence[str]] = None
    ExcludeCategories: Optional[Sequence[str]] = None
    IncludeBusinessChains: Optional[Sequence[str]] = None
    ExcludeBusinessChains: Optional[Sequence[str]] = None
    IncludeFoodTypes: Optional[Sequence[str]] = None
    ExcludeFoodTypes: Optional[Sequence[str]] = None


class SuggestQueryResult(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryType: Optional[QueryTypeType] = None


class AccessRestriction(BaseValidatorModel):
    Restricted: Optional[bool] = None
    Categories: Optional[List[Category]] = None


class ContactDetails(BaseValidatorModel):
    Label: Optional[str] = None
    Value: Optional[str] = None
    Categories: Optional[List[Category]] = None


class ComponentMatchScores(BaseValidatorModel):
    Title: Optional[float] = None
    Address: Optional[AddressComponentMatchScores] = None


class AddressComponentPhonemes(BaseValidatorModel):
    Country: Optional[List[PhonemeTranscription]] = None
    Region: Optional[List[PhonemeTranscription]] = None
    SubRegion: Optional[List[PhonemeTranscription]] = None
    Locality: Optional[List[PhonemeTranscription]] = None
    District: Optional[List[PhonemeTranscription]] = None
    SubDistrict: Optional[List[PhonemeTranscription]] = None
    Block: Optional[List[PhonemeTranscription]] = None
    SubBlock: Optional[List[PhonemeTranscription]] = None
    Street: Optional[List[PhonemeTranscription]] = None


class StreetComponents(BaseValidatorModel):
    pass


class Address(BaseValidatorModel):
    Label: Optional[str] = None
    Country: Optional[Country] = None
    Region: Optional[Region] = None
    SubRegion: Optional[SubRegion] = None
    Locality: Optional[str] = None
    District: Optional[str] = None
    SubDistrict: Optional[str] = None
    PostalCode: Optional[str] = None
    Block: Optional[str] = None
    SubBlock: Optional[str] = None
    Intersection: Optional[List[str]] = None
    Street: Optional[str] = None
    StreetComponents: Optional[List[StreetComponents]] = None
    AddressNumber: Optional[str] = None
    Building: Optional[str] = None


class CountryHighlights(BaseValidatorModel):
    Code: Optional[List[Highlight]] = None
    Name: Optional[List[Highlight]] = None


class RegionHighlights(BaseValidatorModel):
    Code: Optional[List[Highlight]] = None
    Name: Optional[List[Highlight]] = None


class SubRegionHighlights(BaseValidatorModel):
    Code: Optional[List[Highlight]] = None
    Name: Optional[List[Highlight]] = None


class SuggestAddressHighlights(BaseValidatorModel):
    Label: Optional[List[Highlight]] = None


class AutocompleteFilter(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Circle: Optional[FilterCircle] = None
    IncludeCountries: Optional[Sequence[str]] = None
    IncludePlaceTypes: Optional[Sequence[AutocompleteFilterPlaceTypeType]] = None


class SearchTextFilter(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Circle: Optional[FilterCircle] = None
    IncludeCountries: Optional[Sequence[str]] = None


class SuggestFilter(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Circle: Optional[FilterCircle] = None
    IncludeCountries: Optional[Sequence[str]] = None


class GeocodeRequest(BaseValidatorModel):
    QueryText: Optional[str] = None
    QueryComponents: Optional[GeocodeQueryComponents] = None
    MaxResults: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[GeocodeFilter] = None
    AdditionalFeatures: Optional[Sequence[GeocodeAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[GeocodeIntendedUseType] = None
    Key: Optional[str] = None


class OpeningHours(BaseValidatorModel):
    Display: Optional[List[str]] = None
    OpenNow: Optional[bool] = None
    Components: Optional[List[OpeningHoursComponents]] = None
    Categories: Optional[List[Category]] = None


class PostalCodeDetails(BaseValidatorModel):
    PostalCode: Optional[str] = None
    PostalAuthority: Optional[Literal["Usps"]] = None
    PostalCodeType: Optional[PostalCodeTypeType] = None
    UspsZip: Optional[UspsZip] = None
    UspsZipPlus4: Optional[UspsZipPlus4] = None


class ReverseGeocodeRequest(BaseValidatorModel):
    QueryPosition: Sequence[float]
    QueryRadius: Optional[int] = None
    MaxResults: Optional[int] = None
    Filter: Optional[ReverseGeocodeFilter] = None
    AdditionalFeatures: Optional[Sequence[ReverseGeocodeAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[ReverseGeocodeIntendedUseType] = None
    Key: Optional[str] = None


class SearchNearbyRequest(BaseValidatorModel):
    QueryPosition: Sequence[float]
    QueryRadius: Optional[int] = None
    MaxResults: Optional[int] = None
    Filter: Optional[SearchNearbyFilter] = None
    AdditionalFeatures: Optional[Sequence[SearchNearbyAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[SearchNearbyIntendedUseType] = None
    NextToken: Optional[str] = None
    Key: Optional[str] = None


class Contacts(BaseValidatorModel):
    Phones: Optional[List[ContactDetails]] = None
    Faxes: Optional[List[ContactDetails]] = None
    Websites: Optional[List[ContactDetails]] = None
    Emails: Optional[List[ContactDetails]] = None


class MatchScoreDetails(BaseValidatorModel):
    Overall: Optional[float] = None
    Components: Optional[ComponentMatchScores] = None


class PhonemeDetails(BaseValidatorModel):
    Title: Optional[List[PhonemeTranscription]] = None
    Address: Optional[AddressComponentPhonemes] = None


class AutocompleteAddressHighlights(BaseValidatorModel):
    Label: Optional[List[Highlight]] = None
    Country: Optional[CountryHighlights] = None
    Region: Optional[RegionHighlights] = None
    SubRegion: Optional[SubRegionHighlights] = None
    Locality: Optional[List[Highlight]] = None
    District: Optional[List[Highlight]] = None
    SubDistrict: Optional[List[Highlight]] = None
    Street: Optional[List[Highlight]] = None
    Block: Optional[List[Highlight]] = None
    SubBlock: Optional[List[Highlight]] = None
    Intersection: Optional[List[List[Highlight]]] = None
    PostalCode: Optional[List[Highlight]] = None
    AddressNumber: Optional[List[Highlight]] = None
    Building: Optional[List[Highlight]] = None


class SuggestHighlights(BaseValidatorModel):
    Title: Optional[List[Highlight]] = None
    Address: Optional[SuggestAddressHighlights] = None


class AutocompleteRequest(BaseValidatorModel):
    QueryText: str
    MaxResults: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[AutocompleteFilter] = None
    PostalCodeMode: Optional[PostalCodeModeType] = None
    AdditionalFeatures: Optional[Sequence[Literal["Core"]]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[Literal["SingleUse"]] = None
    Key: Optional[str] = None


class SearchTextRequest(BaseValidatorModel):
    QueryText: Optional[str] = None
    QueryId: Optional[str] = None
    MaxResults: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[SearchTextFilter] = None
    AdditionalFeatures: Optional[Sequence[SearchTextAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[SearchTextIntendedUseType] = None
    NextToken: Optional[str] = None
    Key: Optional[str] = None


class SuggestRequest(BaseValidatorModel):
    QueryText: str
    MaxResults: Optional[int] = None
    MaxQueryRefinements: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[SuggestFilter] = None
    AdditionalFeatures: Optional[Sequence[SuggestAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[Literal["SingleUse"]] = None
    Key: Optional[str] = None


class ReverseGeocodeResultItem(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[Address] = None
    AddressNumberCorrected: Optional[bool] = None
    PostalCodeDetails: Optional[List[PostalCodeDetails]] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[Category]] = None
    FoodTypes: Optional[List[FoodType]] = None
    AccessPoints: Optional[List[AccessPoint]] = None
    TimeZone: Optional[TimeZone] = None
    PoliticalView: Optional[str] = None


class GeocodeResultItem(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[Address] = None
    AddressNumberCorrected: Optional[bool] = None
    PostalCodeDetails: Optional[List[PostalCodeDetails]] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[Category]] = None
    FoodTypes: Optional[List[FoodType]] = None
    AccessPoints: Optional[List[AccessPoint]] = None
    TimeZone: Optional[TimeZone] = None
    PoliticalView: Optional[str] = None
    MatchScores: Optional[MatchScoreDetails] = None


class GetPlaceResponse(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    PricingBucket: str
    Address: Address
    AddressNumberCorrected: bool
    PostalCodeDetails: List[PostalCodeDetails]
    Position: List[float]
    MapView: List[float]
    Categories: List[Category]
    FoodTypes: List[FoodType]
    BusinessChains: List[BusinessChain]
    Contacts: Contacts
    OpeningHours: List[OpeningHours]
    AccessPoints: List[AccessPoint]
    AccessRestrictions: List[AccessRestriction]
    TimeZone: TimeZone
    PoliticalView: str
    Phonemes: PhonemeDetails
    ResponseMetadata: ResponseMetadata


class SearchNearbyResultItem(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[Address] = None
    AddressNumberCorrected: Optional[bool] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[Category]] = None
    FoodTypes: Optional[List[FoodType]] = None
    BusinessChains: Optional[List[BusinessChain]] = None
    Contacts: Optional[Contacts] = None
    OpeningHours: Optional[List[OpeningHours]] = None
    AccessPoints: Optional[List[AccessPoint]] = None
    AccessRestrictions: Optional[List[AccessRestriction]] = None
    TimeZone: Optional[TimeZone] = None
    PoliticalView: Optional[str] = None
    Phonemes: Optional[PhonemeDetails] = None


class SearchTextResultItem(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[Address] = None
    AddressNumberCorrected: Optional[bool] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[Category]] = None
    FoodTypes: Optional[List[FoodType]] = None
    BusinessChains: Optional[List[BusinessChain]] = None
    Contacts: Optional[Contacts] = None
    OpeningHours: Optional[List[OpeningHours]] = None
    AccessPoints: Optional[List[AccessPoint]] = None
    AccessRestrictions: Optional[List[AccessRestriction]] = None
    TimeZone: Optional[TimeZone] = None
    PoliticalView: Optional[str] = None
    Phonemes: Optional[PhonemeDetails] = None


class SuggestPlaceResult(BaseValidatorModel):
    PlaceId: Optional[str] = None
    PlaceType: Optional[PlaceTypeType] = None
    Address: Optional[Address] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[Category]] = None
    FoodTypes: Optional[List[FoodType]] = None
    BusinessChains: Optional[List[BusinessChain]] = None
    AccessPoints: Optional[List[AccessPoint]] = None
    AccessRestrictions: Optional[List[AccessRestriction]] = None
    TimeZone: Optional[TimeZone] = None
    PoliticalView: Optional[str] = None
    Phonemes: Optional[PhonemeDetails] = None


class AutocompleteHighlights(BaseValidatorModel):
    Title: Optional[List[Highlight]] = None
    Address: Optional[AutocompleteAddressHighlights] = None


class ReverseGeocodeResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[ReverseGeocodeResultItem]
    ResponseMetadata: ResponseMetadata


class GeocodeResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[GeocodeResultItem]
    ResponseMetadata: ResponseMetadata


class SearchNearbyResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SearchNearbyResultItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchTextResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SearchTextResultItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SuggestResultItem(BaseValidatorModel):
    Title: str
    SuggestResultItemType: SuggestResultItemTypeType
    Place: Optional[SuggestPlaceResult] = None
    Query: Optional[SuggestQueryResult] = None
    Highlights: Optional[SuggestHighlights] = None


class AutocompleteResultItem(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[Address] = None
    Distance: Optional[int] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    Highlights: Optional[AutocompleteHighlights] = None


class SuggestResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SuggestResultItem]
    QueryRefinements: List[QueryRefinement]
    ResponseMetadata: ResponseMetadata


class AutocompleteResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[AutocompleteResultItem]
    ResponseMetadata: ResponseMetadata


