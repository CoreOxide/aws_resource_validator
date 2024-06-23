# Location Service

### ApiKeyAction
- **Type**: string
- **Pattern**: `^geo:\w*\*?$`
- **Min Length**: 5
- **Max Length**: 200

### Arn
- **Type**: string
- **Pattern**: `^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?$`
- **Min Length**: 0
- **Max Length**: 1600

### BatchGetDevicePositionRequestTrackerNameString
- **Type**: string
- **Pattern**: `^[-._\w]+$`
- **Min Length**: 1

### CountryCode
- **Type**: string
- **Pattern**: `^[A-Z]{3}$`

### CountryCode3
- **Type**: string
- **Pattern**: `^[A-Z]{3}$`
- **Min Length**: 3
- **Max Length**: 3

### CountryCode3OrEmpty
- **Type**: string
- **Pattern**: `^[A-Z]{3}$|^$`
- **Min Length**: 0
- **Max Length**: 3

### CustomLayer
- **Type**: string
- **Pattern**: `^[-._\w]+$`
- **Min Length**: 1
- **Max Length**: 100

### GeoArn
- **Type**: string
- **Pattern**: `^arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))$`
- **Min Length**: 0
- **Max Length**: 1600

### GetMapGlyphsRequestFontUnicodeRangeString
- **Type**: string
- **Pattern**: `^[0-9]+-[0-9]+\.pbf$`

### GetMapSpritesRequestFileNameString
- **Type**: string
- **Pattern**: `^sprites(@2x)?\.(png|json)$`

### GetMapTileRequestXString
- **Type**: string
- **Pattern**: `\d+`

### GetMapTileRequestYString
- **Type**: string
- **Pattern**: `\d+`

### GetMapTileRequestZString
- **Type**: string
- **Pattern**: `\d+`

### Id
- **Type**: string
- **Pattern**: `^[-._\p{L}\p{N}]+$`
- **Min Length**: 1
- **Max Length**: 100

### MapStyle
- **Type**: string
- **Pattern**: `^[-._\w]+$`
- **Min Length**: 1
- **Max Length**: 100

### RefererPattern
- **Type**: string
- **Pattern**: `^([$\-._+!*\x{60}(),;/?:@=&\w]|%([0-9a-fA-F?]{2}|[0-9a-fA-F?]?[*]))+$`
- **Min Length**: 0
- **Max Length**: 253

### ResourceName
- **Type**: string
- **Pattern**: `^[-._\w]+$`
- **Min Length**: 1
- **Max Length**: 100

### TagKey
- **Type**: string
- **Pattern**: `^[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[A-Za-z0-9 _=@:.+-/]*$`
- **Min Length**: 0
- **Max Length**: 256

