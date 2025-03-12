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

class AccessPointTypeDef(BaseValidatorModel):
    Position: Optional[List[float]] = None


class CategoryTypeDef(BaseValidatorModel):
    Id: str
    Name: str
    LocalizedName: Optional[str] = None
    Primary: Optional[bool] = None


class AddressComponentMatchScoresTypeDef(BaseValidatorModel):
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


class PhonemeTranscriptionTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Language: Optional[str] = None
    Preferred: Optional[bool] = None


class CountryTypeDef(BaseValidatorModel):
    Code2: Optional[str] = None
    Code3: Optional[str] = None
    Name: Optional[str] = None


class RegionTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Name: Optional[str] = None


class SubRegionTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Name: Optional[str] = None


class HighlightTypeDef(BaseValidatorModel):
    StartIndex: Optional[int] = None
    EndIndex: Optional[int] = None
    Value: Optional[str] = None


class FilterCircleTypeDef(BaseValidatorModel):
    Center: Sequence[float]
    Radius: int


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BusinessChainTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Id: Optional[str] = None


class FoodTypeTypeDef(BaseValidatorModel):
    LocalizedName: str
    Id: Optional[str] = None
    Primary: Optional[bool] = None


class GeocodeFilterTypeDef(BaseValidatorModel):
    IncludeCountries: Optional[Sequence[str]] = None
    IncludePlaceTypes: Optional[Sequence[GeocodeFilterPlaceTypeType]] = None


class GeocodeQueryComponentsTypeDef(BaseValidatorModel):
    Country: Optional[str] = None
    Region: Optional[str] = None
    SubRegion: Optional[str] = None
    Locality: Optional[str] = None
    District: Optional[str] = None
    Street: Optional[str] = None
    AddressNumber: Optional[str] = None
    PostalCode: Optional[str] = None


class TimeZoneTypeDef(BaseValidatorModel):
    Name: str
    Offset: Optional[str] = None
    OffsetSeconds: Optional[int] = None


class GetPlaceRequestTypeDef(BaseValidatorModel):
    PlaceId: str
    AdditionalFeatures: Optional[Sequence[GetPlaceAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[GetPlaceIntendedUseType] = None
    Key: Optional[str] = None


class OpeningHoursComponentsTypeDef(BaseValidatorModel):
    OpenTime: Optional[str] = None
    OpenDuration: Optional[str] = None
    Recurrence: Optional[str] = None


class UspsZipPlus4TypeDef(BaseValidatorModel):
    RecordTypeCode: Optional[RecordTypeCodeType] = None


class UspsZipTypeDef(BaseValidatorModel):
    ZipClassificationCode: Optional[ZipClassificationCodeType] = None


class QueryRefinementTypeDef(BaseValidatorModel):
    RefinedTerm: str
    OriginalTerm: str
    StartIndex: int
    EndIndex: int


class ReverseGeocodeFilterTypeDef(BaseValidatorModel):
    IncludePlaceTypes: Optional[Sequence[ReverseGeocodeFilterPlaceTypeType]] = None


class SearchNearbyFilterTypeDef(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    IncludeCountries: Optional[Sequence[str]] = None
    IncludeCategories: Optional[Sequence[str]] = None
    ExcludeCategories: Optional[Sequence[str]] = None
    IncludeBusinessChains: Optional[Sequence[str]] = None
    ExcludeBusinessChains: Optional[Sequence[str]] = None
    IncludeFoodTypes: Optional[Sequence[str]] = None
    ExcludeFoodTypes: Optional[Sequence[str]] = None


class SuggestQueryResultTypeDef(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryType: Optional[QueryTypeType] = None


class AccessRestrictionTypeDef(BaseValidatorModel):
    Restricted: Optional[bool] = None
    Categories: Optional[List[CategoryTypeDef]] = None


class ContactDetailsTypeDef(BaseValidatorModel):
    Label: Optional[str] = None
    Value: Optional[str] = None
    Categories: Optional[List[CategoryTypeDef]] = None


class ComponentMatchScoresTypeDef(BaseValidatorModel):
    Title: Optional[float] = None
    Address: Optional[AddressComponentMatchScoresTypeDef] = None


class AddressComponentPhonemesTypeDef(BaseValidatorModel):
    Country: Optional[List[PhonemeTranscriptionTypeDef]] = None
    Region: Optional[List[PhonemeTranscriptionTypeDef]] = None
    SubRegion: Optional[List[PhonemeTranscriptionTypeDef]] = None
    Locality: Optional[List[PhonemeTranscriptionTypeDef]] = None
    District: Optional[List[PhonemeTranscriptionTypeDef]] = None
    SubDistrict: Optional[List[PhonemeTranscriptionTypeDef]] = None
    Block: Optional[List[PhonemeTranscriptionTypeDef]] = None
    SubBlock: Optional[List[PhonemeTranscriptionTypeDef]] = None
    Street: Optional[List[PhonemeTranscriptionTypeDef]] = None


class StreetComponentsTypeDef(BaseValidatorModel):
    pass


class AddressTypeDef(BaseValidatorModel):
    Label: Optional[str] = None
    Country: Optional[CountryTypeDef] = None
    Region: Optional[RegionTypeDef] = None
    SubRegion: Optional[SubRegionTypeDef] = None
    Locality: Optional[str] = None
    District: Optional[str] = None
    SubDistrict: Optional[str] = None
    PostalCode: Optional[str] = None
    Block: Optional[str] = None
    SubBlock: Optional[str] = None
    Intersection: Optional[List[str]] = None
    Street: Optional[str] = None
    StreetComponents: Optional[List[StreetComponentsTypeDef]] = None
    AddressNumber: Optional[str] = None
    Building: Optional[str] = None


class CountryHighlightsTypeDef(BaseValidatorModel):
    Code: Optional[List[HighlightTypeDef]] = None
    Name: Optional[List[HighlightTypeDef]] = None


class RegionHighlightsTypeDef(BaseValidatorModel):
    Code: Optional[List[HighlightTypeDef]] = None
    Name: Optional[List[HighlightTypeDef]] = None


class SubRegionHighlightsTypeDef(BaseValidatorModel):
    Code: Optional[List[HighlightTypeDef]] = None
    Name: Optional[List[HighlightTypeDef]] = None


class SuggestAddressHighlightsTypeDef(BaseValidatorModel):
    Label: Optional[List[HighlightTypeDef]] = None


class AutocompleteFilterTypeDef(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Circle: Optional[FilterCircleTypeDef] = None
    IncludeCountries: Optional[Sequence[str]] = None
    IncludePlaceTypes: Optional[Sequence[AutocompleteFilterPlaceTypeType]] = None


class SearchTextFilterTypeDef(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Circle: Optional[FilterCircleTypeDef] = None
    IncludeCountries: Optional[Sequence[str]] = None


class SuggestFilterTypeDef(BaseValidatorModel):
    BoundingBox: Optional[Sequence[float]] = None
    Circle: Optional[FilterCircleTypeDef] = None
    IncludeCountries: Optional[Sequence[str]] = None


class GeocodeRequestTypeDef(BaseValidatorModel):
    QueryText: Optional[str] = None
    QueryComponents: Optional[GeocodeQueryComponentsTypeDef] = None
    MaxResults: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[GeocodeFilterTypeDef] = None
    AdditionalFeatures: Optional[Sequence[GeocodeAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[GeocodeIntendedUseType] = None
    Key: Optional[str] = None


class OpeningHoursTypeDef(BaseValidatorModel):
    Display: Optional[List[str]] = None
    OpenNow: Optional[bool] = None
    Components: Optional[List[OpeningHoursComponentsTypeDef]] = None
    Categories: Optional[List[CategoryTypeDef]] = None


class PostalCodeDetailsTypeDef(BaseValidatorModel):
    PostalCode: Optional[str] = None
    PostalAuthority: Optional[Literal["Usps"]] = None
    PostalCodeType: Optional[PostalCodeTypeType] = None
    UspsZip: Optional[UspsZipTypeDef] = None
    UspsZipPlus4: Optional[UspsZipPlus4TypeDef] = None


class ReverseGeocodeRequestTypeDef(BaseValidatorModel):
    QueryPosition: Sequence[float]
    QueryRadius: Optional[int] = None
    MaxResults: Optional[int] = None
    Filter: Optional[ReverseGeocodeFilterTypeDef] = None
    AdditionalFeatures: Optional[Sequence[ReverseGeocodeAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[ReverseGeocodeIntendedUseType] = None
    Key: Optional[str] = None


class SearchNearbyRequestTypeDef(BaseValidatorModel):
    QueryPosition: Sequence[float]
    QueryRadius: Optional[int] = None
    MaxResults: Optional[int] = None
    Filter: Optional[SearchNearbyFilterTypeDef] = None
    AdditionalFeatures: Optional[Sequence[SearchNearbyAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[SearchNearbyIntendedUseType] = None
    NextToken: Optional[str] = None
    Key: Optional[str] = None


class ContactsTypeDef(BaseValidatorModel):
    Phones: Optional[List[ContactDetailsTypeDef]] = None
    Faxes: Optional[List[ContactDetailsTypeDef]] = None
    Websites: Optional[List[ContactDetailsTypeDef]] = None
    Emails: Optional[List[ContactDetailsTypeDef]] = None


class MatchScoreDetailsTypeDef(BaseValidatorModel):
    Overall: Optional[float] = None
    Components: Optional[ComponentMatchScoresTypeDef] = None


class PhonemeDetailsTypeDef(BaseValidatorModel):
    Title: Optional[List[PhonemeTranscriptionTypeDef]] = None
    Address: Optional[AddressComponentPhonemesTypeDef] = None


class AutocompleteAddressHighlightsTypeDef(BaseValidatorModel):
    Label: Optional[List[HighlightTypeDef]] = None
    Country: Optional[CountryHighlightsTypeDef] = None
    Region: Optional[RegionHighlightsTypeDef] = None
    SubRegion: Optional[SubRegionHighlightsTypeDef] = None
    Locality: Optional[List[HighlightTypeDef]] = None
    District: Optional[List[HighlightTypeDef]] = None
    SubDistrict: Optional[List[HighlightTypeDef]] = None
    Street: Optional[List[HighlightTypeDef]] = None
    Block: Optional[List[HighlightTypeDef]] = None
    SubBlock: Optional[List[HighlightTypeDef]] = None
    Intersection: Optional[List[List[HighlightTypeDef]]] = None
    PostalCode: Optional[List[HighlightTypeDef]] = None
    AddressNumber: Optional[List[HighlightTypeDef]] = None
    Building: Optional[List[HighlightTypeDef]] = None


class SuggestHighlightsTypeDef(BaseValidatorModel):
    Title: Optional[List[HighlightTypeDef]] = None
    Address: Optional[SuggestAddressHighlightsTypeDef] = None


class AutocompleteRequestTypeDef(BaseValidatorModel):
    QueryText: str
    MaxResults: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[AutocompleteFilterTypeDef] = None
    PostalCodeMode: Optional[PostalCodeModeType] = None
    AdditionalFeatures: Optional[Sequence[Literal["Core"]]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[Literal["SingleUse"]] = None
    Key: Optional[str] = None


class SearchTextRequestTypeDef(BaseValidatorModel):
    QueryText: Optional[str] = None
    QueryId: Optional[str] = None
    MaxResults: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[SearchTextFilterTypeDef] = None
    AdditionalFeatures: Optional[Sequence[SearchTextAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[SearchTextIntendedUseType] = None
    NextToken: Optional[str] = None
    Key: Optional[str] = None


class SuggestRequestTypeDef(BaseValidatorModel):
    QueryText: str
    MaxResults: Optional[int] = None
    MaxQueryRefinements: Optional[int] = None
    BiasPosition: Optional[Sequence[float]] = None
    Filter: Optional[SuggestFilterTypeDef] = None
    AdditionalFeatures: Optional[Sequence[SuggestAdditionalFeatureType]] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    IntendedUse: Optional[Literal["SingleUse"]] = None
    Key: Optional[str] = None


class ReverseGeocodeResultItemTypeDef(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[AddressTypeDef] = None
    AddressNumberCorrected: Optional[bool] = None
    PostalCodeDetails: Optional[List[PostalCodeDetailsTypeDef]] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[CategoryTypeDef]] = None
    FoodTypes: Optional[List[FoodTypeTypeDef]] = None
    AccessPoints: Optional[List[AccessPointTypeDef]] = None
    TimeZone: Optional[TimeZoneTypeDef] = None
    PoliticalView: Optional[str] = None


class GeocodeResultItemTypeDef(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[AddressTypeDef] = None
    AddressNumberCorrected: Optional[bool] = None
    PostalCodeDetails: Optional[List[PostalCodeDetailsTypeDef]] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[CategoryTypeDef]] = None
    FoodTypes: Optional[List[FoodTypeTypeDef]] = None
    AccessPoints: Optional[List[AccessPointTypeDef]] = None
    TimeZone: Optional[TimeZoneTypeDef] = None
    PoliticalView: Optional[str] = None
    MatchScores: Optional[MatchScoreDetailsTypeDef] = None


class GetPlaceResponseTypeDef(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    PricingBucket: str
    Address: AddressTypeDef
    AddressNumberCorrected: bool
    PostalCodeDetails: List[PostalCodeDetailsTypeDef]
    Position: List[float]
    MapView: List[float]
    Categories: List[CategoryTypeDef]
    FoodTypes: List[FoodTypeTypeDef]
    BusinessChains: List[BusinessChainTypeDef]
    Contacts: ContactsTypeDef
    OpeningHours: List[OpeningHoursTypeDef]
    AccessPoints: List[AccessPointTypeDef]
    AccessRestrictions: List[AccessRestrictionTypeDef]
    TimeZone: TimeZoneTypeDef
    PoliticalView: str
    Phonemes: PhonemeDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchNearbyResultItemTypeDef(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[AddressTypeDef] = None
    AddressNumberCorrected: Optional[bool] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[CategoryTypeDef]] = None
    FoodTypes: Optional[List[FoodTypeTypeDef]] = None
    BusinessChains: Optional[List[BusinessChainTypeDef]] = None
    Contacts: Optional[ContactsTypeDef] = None
    OpeningHours: Optional[List[OpeningHoursTypeDef]] = None
    AccessPoints: Optional[List[AccessPointTypeDef]] = None
    AccessRestrictions: Optional[List[AccessRestrictionTypeDef]] = None
    TimeZone: Optional[TimeZoneTypeDef] = None
    PoliticalView: Optional[str] = None
    Phonemes: Optional[PhonemeDetailsTypeDef] = None


class SearchTextResultItemTypeDef(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[AddressTypeDef] = None
    AddressNumberCorrected: Optional[bool] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[CategoryTypeDef]] = None
    FoodTypes: Optional[List[FoodTypeTypeDef]] = None
    BusinessChains: Optional[List[BusinessChainTypeDef]] = None
    Contacts: Optional[ContactsTypeDef] = None
    OpeningHours: Optional[List[OpeningHoursTypeDef]] = None
    AccessPoints: Optional[List[AccessPointTypeDef]] = None
    AccessRestrictions: Optional[List[AccessRestrictionTypeDef]] = None
    TimeZone: Optional[TimeZoneTypeDef] = None
    PoliticalView: Optional[str] = None
    Phonemes: Optional[PhonemeDetailsTypeDef] = None


class SuggestPlaceResultTypeDef(BaseValidatorModel):
    PlaceId: Optional[str] = None
    PlaceType: Optional[PlaceTypeType] = None
    Address: Optional[AddressTypeDef] = None
    Position: Optional[List[float]] = None
    Distance: Optional[int] = None
    MapView: Optional[List[float]] = None
    Categories: Optional[List[CategoryTypeDef]] = None
    FoodTypes: Optional[List[FoodTypeTypeDef]] = None
    BusinessChains: Optional[List[BusinessChainTypeDef]] = None
    AccessPoints: Optional[List[AccessPointTypeDef]] = None
    AccessRestrictions: Optional[List[AccessRestrictionTypeDef]] = None
    TimeZone: Optional[TimeZoneTypeDef] = None
    PoliticalView: Optional[str] = None
    Phonemes: Optional[PhonemeDetailsTypeDef] = None


class AutocompleteHighlightsTypeDef(BaseValidatorModel):
    Title: Optional[List[HighlightTypeDef]] = None
    Address: Optional[AutocompleteAddressHighlightsTypeDef] = None


class ReverseGeocodeResponseTypeDef(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[ReverseGeocodeResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GeocodeResponseTypeDef(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[GeocodeResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SearchNearbyResponseTypeDef(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SearchNearbyResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchTextResponseTypeDef(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SearchTextResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SuggestResultItemTypeDef(BaseValidatorModel):
    Title: str
    SuggestResultItemType: SuggestResultItemTypeType
    Place: Optional[SuggestPlaceResultTypeDef] = None
    Query: Optional[SuggestQueryResultTypeDef] = None
    Highlights: Optional[SuggestHighlightsTypeDef] = None


class AutocompleteResultItemTypeDef(BaseValidatorModel):
    PlaceId: str
    PlaceType: PlaceTypeType
    Title: str
    Address: Optional[AddressTypeDef] = None
    Distance: Optional[int] = None
    Language: Optional[str] = None
    PoliticalView: Optional[str] = None
    Highlights: Optional[AutocompleteHighlightsTypeDef] = None


class SuggestResponseTypeDef(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[SuggestResultItemTypeDef]
    QueryRefinements: List[QueryRefinementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AutocompleteResponseTypeDef(BaseValidatorModel):
    PricingBucket: str
    ResultItems: List[AutocompleteResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


