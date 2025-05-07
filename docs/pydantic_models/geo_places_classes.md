# Geo Places Classes

# AccessPoint

### Position
- **Type**: typing.Optional[typing.List[float]]


# AccessRestriction

### Restricted
- **Type**: typing.Optional[bool]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]


# Address

### Label
- **Type**: typing.Optional[str]

### Country
- **Type**: <class 'NoneType'>

### Region
- **Type**: <class 'NoneType'>

### SubRegion
- **Type**: <class 'NoneType'>

### Locality
- **Type**: typing.Optional[str]

### District
- **Type**: typing.Optional[str]

### SubDistrict
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]

### Block
- **Type**: typing.Optional[str]

### SubBlock
- **Type**: typing.Optional[str]

### Intersection
- **Type**: typing.Optional[typing.List[str]]

### Street
- **Type**: typing.Optional[str]

### StreetComponents
- **Type**: typing.Optional[typing.List[NoneType]]

### AddressNumber
- **Type**: typing.Optional[str]

### Building
- **Type**: typing.Optional[str]


# AddressComponentMatchScores

### Country
- **Type**: typing.Optional[float]

### Region
- **Type**: typing.Optional[float]

### SubRegion
- **Type**: typing.Optional[float]

### Locality
- **Type**: typing.Optional[float]

### District
- **Type**: typing.Optional[float]

### SubDistrict
- **Type**: typing.Optional[float]

### PostalCode
- **Type**: typing.Optional[float]

### Block
- **Type**: typing.Optional[float]

### SubBlock
- **Type**: typing.Optional[float]

### Intersection
- **Type**: typing.Optional[typing.List[float]]

### AddressNumber
- **Type**: typing.Optional[float]

### Building
- **Type**: typing.Optional[float]


# AddressComponentPhonemes

### Country
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### Region
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### SubRegion
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### Locality
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### District
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### SubDistrict
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### Block
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### SubBlock
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### Street
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]


# AutocompleteAddressHighlights

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.CountryHighlights]

### Region
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.RegionHighlights]

### SubRegion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SubRegionHighlights]

### Locality
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### District
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### SubDistrict
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Street
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Block
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### SubBlock
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Intersection
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]]

### PostalCode
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### AddressNumber
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Building
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]


# AutocompleteFilter

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FilterCircle]

### IncludeCountries
- **Type**: typing.Optional[typing.List[str]]

### IncludePlaceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Locality', 'PostalCode']]]


# AutocompleteHighlights

### Title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AutocompleteAddressHighlights]


# AutocompleteRequest

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### BiasPosition
- **Type**: typing.Optional[typing.List[float]]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AutocompleteFilter]

### PostalCodeMode
- **Type**: typing.Optional[typing.Literal['EnumerateSpannedLocalities', 'MergeAllSpannedLocalities']]

### AdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Core']]]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse']]

### Key
- **Type**: typing.Optional[str]


# AutocompleteResponse

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AutocompleteResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ResponseMetadata'>
- **Required**: Yes


# AutocompleteResultItem

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceType
- **Type**: typing.Literal['Block', 'Country', 'District', 'InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PointOfInterest', 'PostalCode', 'Region', 'Street', 'SubBlock', 'SubDistrict', 'SubRegion']
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'NoneType'>

### Distance
- **Type**: typing.Optional[int]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### Highlights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AutocompleteHighlights]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BusinessChain

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]


# Category

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LocalizedName
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]


# ComponentMatchScores

### Title
- **Type**: typing.Optional[float]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AddressComponentMatchScores]


# ContactDetails

### Label
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]


# Contacts

### Phones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ContactDetails]]

### Faxes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ContactDetails]]

### Websites
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ContactDetails]]

### Emails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ContactDetails]]


# Country

### Code2
- **Type**: typing.Optional[str]

### Code3
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# CountryHighlights

### Code
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Name
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]


# FilterCircle

### Center
- **Type**: typing.List[float]
- **Required**: Yes

### Radius
- **Type**: <class 'int'>
- **Required**: Yes


# FoodType

### LocalizedName
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Primary
- **Type**: typing.Optional[bool]


# GeocodeFilter

### IncludeCountries
- **Type**: typing.Optional[typing.List[str]]

### IncludePlaceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PostalCode', 'Street']]]


# GeocodeQueryComponents

### Country
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### SubRegion
- **Type**: typing.Optional[str]

### Locality
- **Type**: typing.Optional[str]

### District
- **Type**: typing.Optional[str]

### Street
- **Type**: typing.Optional[str]

### AddressNumber
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]


# GeocodeRequest

### QueryText
- **Type**: typing.Optional[str]

### QueryComponents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.GeocodeQueryComponents]

### MaxResults
- **Type**: typing.Optional[int]

### BiasPosition
- **Type**: typing.Optional[typing.List[float]]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.GeocodeFilter]

### AdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Access', 'TimeZone']]]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse', 'Storage']]

### Key
- **Type**: typing.Optional[str]


# GeocodeResponse

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.GeocodeResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ResponseMetadata'>
- **Required**: Yes


# GeocodeResultItem

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceType
- **Type**: typing.Literal['Block', 'Country', 'District', 'InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PointOfInterest', 'PostalCode', 'Region', 'Street', 'SubBlock', 'SubDistrict', 'SubRegion']
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'NoneType'>

### AddressNumberCorrected
- **Type**: typing.Optional[bool]

### PostalCodeDetails
- **Type**: typing.Optional[typing.List[NoneType]]

### Position
- **Type**: typing.Optional[typing.List[float]]

### Distance
- **Type**: typing.Optional[int]

### MapView
- **Type**: typing.Optional[typing.List[float]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]

### FoodTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FoodType]]

### AccessPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessPoint]]

### TimeZone
- **Type**: <class 'NoneType'>

### PoliticalView
- **Type**: typing.Optional[str]

### MatchScores
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.MatchScoreDetails]


# GetPlaceRequest

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Access', 'Contact', 'Phonemes', 'TimeZone']]]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse', 'Storage']]

### Key
- **Type**: typing.Optional[str]


# GetPlaceResponse

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceType
- **Type**: typing.Literal['Block', 'Country', 'District', 'InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PointOfInterest', 'PostalCode', 'Region', 'Street', 'SubBlock', 'SubDistrict', 'SubRegion']
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Address'>
- **Required**: Yes

### AddressNumberCorrected
- **Type**: <class 'bool'>
- **Required**: Yes

### PostalCodeDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PostalCodeDetails]
- **Required**: Yes

### Position
- **Type**: typing.List[float]
- **Required**: Yes

### MapView
- **Type**: typing.List[float]
- **Required**: Yes

### Categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]
- **Required**: Yes

### FoodTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FoodType]
- **Required**: Yes

### BusinessChains
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.BusinessChain]
- **Required**: Yes

### Contacts
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Contacts'>
- **Required**: Yes

### OpeningHours
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.OpeningHours]
- **Required**: Yes

### AccessPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessPoint]
- **Required**: Yes

### AccessRestrictions
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessRestriction]
- **Required**: Yes

### TimeZone
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.TimeZone'>
- **Required**: Yes

### PoliticalView
- **Type**: <class 'str'>
- **Required**: Yes

### Phonemes
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ResponseMetadata'>
- **Required**: Yes


# Highlight

### StartIndex
- **Type**: typing.Optional[int]

### EndIndex
- **Type**: typing.Optional[int]

### Value
- **Type**: typing.Optional[str]


# MatchScoreDetails

### Overall
- **Type**: typing.Optional[float]

### Components
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ComponentMatchScores]


# OpeningHours

### Display
- **Type**: typing.Optional[typing.List[str]]

### OpenNow
- **Type**: typing.Optional[bool]

### Components
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.OpeningHoursComponents]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]


# OpeningHoursComponents

### OpenTime
- **Type**: typing.Optional[str]

### OpenDuration
- **Type**: typing.Optional[str]

### Recurrence
- **Type**: typing.Optional[str]


# PhonemeDetails

### Title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeTranscription]]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AddressComponentPhonemes]


# PhonemeTranscription

### Value
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]

### Preferred
- **Type**: typing.Optional[bool]


# PostalCodeDetails

### PostalCode
- **Type**: typing.Optional[str]

### PostalAuthority
- **Type**: typing.Optional[typing.Literal['Usps']]

### PostalCodeType
- **Type**: typing.Optional[typing.Literal['UspsZip', 'UspsZipPlus4']]

### UspsZip
- **Type**: <class 'NoneType'>

### UspsZipPlus4
- **Type**: <class 'NoneType'>


# QueryRefinement

### RefinedTerm
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalTerm
- **Type**: <class 'str'>
- **Required**: Yes

### StartIndex
- **Type**: <class 'int'>
- **Required**: Yes

### EndIndex
- **Type**: <class 'int'>
- **Required**: Yes


# Region

### Code
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# RegionHighlights

### Code
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Name
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# ReverseGeocodeFilter

### IncludePlaceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'Street']]]


# ReverseGeocodeRequest

### QueryPosition
- **Type**: typing.List[float]
- **Required**: Yes

### QueryRadius
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ReverseGeocodeFilter]

### AdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Access', 'TimeZone']]]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse', 'Storage']]

### Key
- **Type**: typing.Optional[str]


# ReverseGeocodeResponse

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ReverseGeocodeResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ResponseMetadata'>
- **Required**: Yes


# ReverseGeocodeResultItem

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceType
- **Type**: typing.Literal['Block', 'Country', 'District', 'InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PointOfInterest', 'PostalCode', 'Region', 'Street', 'SubBlock', 'SubDistrict', 'SubRegion']
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'NoneType'>

### AddressNumberCorrected
- **Type**: typing.Optional[bool]

### PostalCodeDetails
- **Type**: typing.Optional[typing.List[NoneType]]

### Position
- **Type**: typing.Optional[typing.List[float]]

### Distance
- **Type**: typing.Optional[int]

### MapView
- **Type**: typing.Optional[typing.List[float]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]

### FoodTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FoodType]]

### AccessPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessPoint]]

### TimeZone
- **Type**: <class 'NoneType'>

### PoliticalView
- **Type**: typing.Optional[str]


# SearchNearbyFilter

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### IncludeCountries
- **Type**: typing.Optional[typing.List[str]]

### IncludeCategories
- **Type**: typing.Optional[typing.List[str]]

### ExcludeCategories
- **Type**: typing.Optional[typing.List[str]]

### IncludeBusinessChains
- **Type**: typing.Optional[typing.List[str]]

### ExcludeBusinessChains
- **Type**: typing.Optional[typing.List[str]]

### IncludeFoodTypes
- **Type**: typing.Optional[typing.List[str]]

### ExcludeFoodTypes
- **Type**: typing.Optional[typing.List[str]]


# SearchNearbyRequest

### QueryPosition
- **Type**: typing.List[float]
- **Required**: Yes

### QueryRadius
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SearchNearbyFilter]

### AdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Access', 'Contact', 'Phonemes', 'TimeZone']]]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse', 'Storage']]

### NextToken
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# SearchNearbyResponse

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SearchNearbyResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchNearbyResultItem

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceType
- **Type**: typing.Literal['Block', 'Country', 'District', 'InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PointOfInterest', 'PostalCode', 'Region', 'Street', 'SubBlock', 'SubDistrict', 'SubRegion']
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'NoneType'>

### AddressNumberCorrected
- **Type**: typing.Optional[bool]

### Position
- **Type**: typing.Optional[typing.List[float]]

### Distance
- **Type**: typing.Optional[int]

### MapView
- **Type**: typing.Optional[typing.List[float]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]

### FoodTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FoodType]]

### BusinessChains
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.BusinessChain]]

### Contacts
- **Type**: <class 'NoneType'>

### OpeningHours
- **Type**: typing.Optional[typing.List[NoneType]]

### AccessPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessPoint]]

### AccessRestrictions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessRestriction]]

### TimeZone
- **Type**: <class 'NoneType'>

### PoliticalView
- **Type**: typing.Optional[str]

### Phonemes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeDetails]


# SearchTextFilter

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FilterCircle]

### IncludeCountries
- **Type**: typing.Optional[typing.List[str]]


# SearchTextRequest

### QueryText
- **Type**: typing.Optional[str]

### QueryId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### BiasPosition
- **Type**: typing.Optional[typing.List[float]]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SearchTextFilter]

### AdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Access', 'Contact', 'Phonemes', 'TimeZone']]]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse', 'Storage']]

### NextToken
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# SearchTextResponse

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SearchTextResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTextResultItem

### PlaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PlaceType
- **Type**: typing.Literal['Block', 'Country', 'District', 'InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PointOfInterest', 'PostalCode', 'Region', 'Street', 'SubBlock', 'SubDistrict', 'SubRegion']
- **Required**: Yes

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'NoneType'>

### AddressNumberCorrected
- **Type**: typing.Optional[bool]

### Position
- **Type**: typing.Optional[typing.List[float]]

### Distance
- **Type**: typing.Optional[int]

### MapView
- **Type**: typing.Optional[typing.List[float]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]

### FoodTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FoodType]]

### BusinessChains
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.BusinessChain]]

### Contacts
- **Type**: <class 'NoneType'>

### OpeningHours
- **Type**: typing.Optional[typing.List[NoneType]]

### AccessPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessPoint]]

### AccessRestrictions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessRestriction]]

### TimeZone
- **Type**: <class 'NoneType'>

### PoliticalView
- **Type**: typing.Optional[str]

### Phonemes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeDetails]


# StreetComponents

### BaseName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### TypePlacement
- **Type**: typing.Optional[typing.Literal['AfterBaseName', 'BeforeBaseName']]

### TypeSeparator
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### Suffix
- **Type**: typing.Optional[str]

### Direction
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]


# SubRegion

### Code
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# SubRegionHighlights

### Code
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Name
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]


# SuggestAddressHighlights

### Label
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]


# SuggestFilter

### BoundingBox
- **Type**: typing.Optional[typing.List[float]]

### Circle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FilterCircle]

### IncludeCountries
- **Type**: typing.Optional[typing.List[str]]


# SuggestHighlights

### Title
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Highlight]]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SuggestAddressHighlights]


# SuggestPlaceResult

### PlaceId
- **Type**: typing.Optional[str]

### PlaceType
- **Type**: typing.Optional[typing.Literal['Block', 'Country', 'District', 'InterpolatedAddress', 'Intersection', 'Locality', 'PointAddress', 'PointOfInterest', 'PostalCode', 'Region', 'Street', 'SubBlock', 'SubDistrict', 'SubRegion']]

### Address
- **Type**: <class 'NoneType'>

### Position
- **Type**: typing.Optional[typing.List[float]]

### Distance
- **Type**: typing.Optional[int]

### MapView
- **Type**: typing.Optional[typing.List[float]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.Category]]

### FoodTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.FoodType]]

### BusinessChains
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.BusinessChain]]

### AccessPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessPoint]]

### AccessRestrictions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.AccessRestriction]]

### TimeZone
- **Type**: <class 'NoneType'>

### PoliticalView
- **Type**: typing.Optional[str]

### Phonemes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.PhonemeDetails]


# SuggestQueryResult

### QueryId
- **Type**: typing.Optional[str]

### QueryType
- **Type**: typing.Optional[typing.Literal['BusinessChain', 'Category']]


# SuggestRequest

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### MaxQueryRefinements
- **Type**: typing.Optional[int]

### BiasPosition
- **Type**: typing.Optional[typing.List[float]]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SuggestFilter]

### AdditionalFeatures
- **Type**: typing.Optional[typing.List[typing.Literal['Access', 'Core', 'Phonemes', 'TimeZone']]]

### Language
- **Type**: typing.Optional[str]

### PoliticalView
- **Type**: typing.Optional[str]

### IntendedUse
- **Type**: typing.Optional[typing.Literal['SingleUse']]

### Key
- **Type**: typing.Optional[str]


# SuggestResponse

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SuggestResultItem]
- **Required**: Yes

### QueryRefinements
- **Type**: typing.List[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.QueryRefinement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_places.geo_places_classes.ResponseMetadata'>
- **Required**: Yes


# SuggestResultItem

### Title
- **Type**: <class 'str'>
- **Required**: Yes

### SuggestResultItemType
- **Type**: typing.Literal['Place', 'Query']
- **Required**: Yes

### Place
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SuggestPlaceResult]

### Query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SuggestQueryResult]

### Highlights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.geo_places.geo_places_classes.SuggestHighlights]


# TimeZone

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Offset
- **Type**: typing.Optional[str]

### OffsetSeconds
- **Type**: typing.Optional[int]


# UspsZip

### ZipClassificationCode
- **Type**: typing.Optional[typing.Literal['Military', 'PostOfficeBoxes', 'Unique']]


# UspsZipPlus4

### RecordTypeCode
- **Type**: typing.Optional[typing.Literal['Firm', 'General', 'HighRise', 'PostOfficeBox', 'Rural', 'Street']]


