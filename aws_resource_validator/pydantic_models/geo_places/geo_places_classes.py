from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.geo_places.geo_places_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


class StreetComponents(BaseValidatorModel):
    BaseName: Optional[str] = None
    Type: Optional[str] = None
    TypePlacement: Optional[TypePlacementType] = None
    TypeSeparator: Optional[str] = None
    Prefix: Optional[str] = None
    Suffix: Optional[str] = None
    Direction: Optional[str] = None
    Language: Optional[str] = None


class SubRegion(BaseValidatorModel):
    Code: Optional[str] = None
    Name: Optional[str] = None


class Highlight(BaseValidatorModel):
    StartIndex: Optional[int] = None
    EndIndex: Optional[int] = None
    Value: Optional[str] = None


class FilterCircle(BaseValidatorModel):
    Center: List[float]
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
    IncludeCountries: Optional[List[str]] = None
    IncludePlaceTypes: Optional[List[GeocodeFilterPlaceTypeType]] = None


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


# This class is the input for the 'get_place' function.
class GetPlaceRequest(BaseValidatorModel):
    PlaceId: str
    AdditionalFeatures: Optional[List[GetPlaceAdditionalFeatureType]] = None
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
    IncludePlaceTypes: Optional[List[ReverseGeocodeFilterPlaceTypeType]] = None


class SearchNearbyFilter(BaseValidatorModel):
    BoundingBox: Optional[List[float]] = None
    IncludeCountries: Optional[List[str]] = None
    IncludeCategories: Optional[List[str]] = None
    ExcludeCategories: Optional[List[str]] = None
    IncludeBusinessChains: Optional[List[str]] = None
    ExcludeBusinessChains: Optional[List[str]] = None
    IncludeFoodTypes: Optional[List[str]] = None
    ExcludeFoodTypes: Optional[List[str]] = None


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
    BoundingBox: Optional[List[float]] = None
    Circle: Optional[FilterCircle] = None
    IncludeCountries: Optional[List[str]] = None
    IncludePlaceTypes: Optional[List[AutocompleteFilterPlaceTypeType]] = None


class SearchTextFilter(BaseValidatorModel):
    BoundingBox: Optional[List[float]] = None
    Circle: Optional[FilterCircle] = None
    IncludeCountries: Optional[List[str]] = None


class SuggestFilter(BaseValidatorModel):
    BoundingBox: Optional[List[float]] = None
    Circle: Optional[FilterCircle] = None
    IncludeCountries: Optional[List[str]] = None


# This class is the input for the 'geocode' function.
class GeocodeRequest(BaseValidatorModel):
    QueryText: Optional[str] = None
    QueryComponents: Optional[GeocodeQueryComponents] = None
    MaxResults: Optional[int] = None
    BiasPosition: Optional[List[float]] = None
    Filter: Optional[GeocodeFilter] = None
    AdditionalFeatures: Optional[List[GeocodeAdditionalFeatureType]] = None
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
    PostalAuthority: Optional[Literal['Usps']] = None
    PostalCodeType: Optional[PostalCodeTypeType] = None
    UspsZip: Optional[UspsZip] = None
    UspsZipPlus4: Optional[UspsZipPlus4] = None


# This class is the input for the 'reverse_geocode' function.
class ReverseGeocodeRequest(BaseValidatorModel):
    QueryPosition: List[float]
    QueryRadius: Optional[int] = None
    MaxResults: Optional[int] = None
    Filter: Optional[ReverseGeocodeFilter] = None
    AdditionalFeatures: Optional[List[ReverseGeocodeAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[ReverseGeocodeIntendedUseType] = None
    Key: Optional[str] = None


# This class is the input for the 'search_nearby' function.
class SearchNearbyRequest(BaseValidatorModel):
    QueryPosition: List[float]
    QueryRadius: Optional[int] = None
    MaxResults: Optional[int] = None
    Filter: Optional[SearchNearbyFilter] = None
    AdditionalFeatures: Optional[List[SearchNearbyAdditionalFeatureType]] = None
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


# This class is the input for the 'autocomplete' function.
class AutocompleteRequest(BaseValidatorModel):
    QueryText: str
    MaxResults: Optional[int] = None
    BiasPosition: Optional[List[float]] = None
    Filter: Optional[AutocompleteFilter] = None
    PostalCodeMode: Optional[PostalCodeModeType] = None
    AdditionalFeatures: Optional[List[Literal['Core']]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[Literal['SingleUse']] = None
    Key: Optional[str] = None


# This class is the input for the 'search_text' function.
class SearchTextRequest(BaseValidatorModel):
    QueryText: Optional[str] = None
    QueryId: Optional[str] = None
    MaxResults: Optional[int] = None
    BiasPosition: Optional[List[float]] = None
    Filter: Optional[SearchTextFilter] = None
    AdditionalFeatures: Optional[List[SearchTextAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[SearchTextIntendedUseType] = None
    NextToken: Optional[str] = None
    Key: Optional[str] = None


# This class is the input for the 'suggest' function.
class SuggestRequest(BaseValidatorModel):
    QueryText: str
    MaxResults: Optional[int] = None
    MaxQueryRefinements: Optional[int] = None
    BiasPosition: Optional[List[float]] = None
    Filter: Optional[SuggestFilter] = None
    AdditionalFeatures: Optional[List[SuggestAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[Literal['SingleUse']] = None
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


# This class is the output for the 'get_place' function.
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


# This class is the output for the 'reverse_geocode' function.
class ReverseGeocodeResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[ReverseGeocodeResultItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'geocode' function.
class GeocodeResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[GeocodeResultItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_nearby' function.
class SearchNearbyResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SearchNearbyResultItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'search_text' function.
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


# This class is the output for the 'suggest' function.
class SuggestResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SuggestResultItem]
    QueryRefinements: List[QueryRefinement]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'autocomplete' function.
class AutocompleteResponse(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[AutocompleteResultItem]
    ResponseMetadata: ResponseMetadata