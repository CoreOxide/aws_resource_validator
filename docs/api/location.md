# Location Service

### ApiKeyAction
- **Type**: string
- **Pattern**: `(geo|geo-routes|geo-places|geo-maps):\w*\*?`
- **Min Length**: 5
- **Max Length**: 200

### Arn
- **Type**: string
- **Pattern**: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
- **Min Length**: 0
- **Max Length**: 1600

### BatchGetDevicePositionRequestTrackerNameString
- **Type**: string
- **Pattern**: `[-._\w]+`
- **Min Length**: 1

### CountryCode3
- **Type**: string
- **Pattern**: `[A-Z]{3}`
- **Min Length**: 3
- **Max Length**: 3

### CountryCode3OrEmpty
- **Type**: string
- **Pattern**: `[A-Z]{3}$|^`
- **Min Length**: 0
- **Max Length**: 3

### CustomLayer
- **Type**: string
- **Pattern**: `[-._\w]+`
- **Min Length**: 1
- **Max Length**: 100

### DeviceStateIpv4AddressString
- **Type**: string
- **Pattern**: `(?:(?:25[0-5]|(?:2[0-4]|1\d|[0-9]|)\d)\.?\b){4}`

### GeoArn
- **Type**: string
- **Pattern**: `arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))`
- **Min Length**: 0
- **Max Length**: 1600

### GeoArnV2
- **Type**: string
- **Pattern**: `.*(^arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\*)|([-a-z]+[/][*-._\w]+))$)|(^arn(:[a-z0-9]+([.-][a-z0-9]+)*):(geo-routes|geo-places|geo-maps)(:((\*)|([a-z0-9]+([.-][a-z0-9]+)*)))::((provider[\/][*-._\w]+))$).*`
- **Min Length**: 0
- **Max Length**: 1600

### GetMapGlyphsRequestFontUnicodeRangeString
- **Type**: string
- **Pattern**: `[0-9]+-[0-9]+\.pbf`

### GetMapSpritesRequestFileNameString
- **Type**: string
- **Pattern**: `sprites(@2x)?\.(png|json)`

### GetMapTileRequestXString
- **Type**: string
- **Pattern**: `.*\d+.*`

### GetMapTileRequestYString
- **Type**: string
- **Pattern**: `.*\d+.*`

### GetMapTileRequestZString
- **Type**: string
- **Pattern**: `.*\d+.*`

### Id
- **Type**: string
- **Pattern**: `[-._\p{L}\p{N}]+`
- **Min Length**: 1
- **Max Length**: 100

### MapStyle
- **Type**: string
- **Pattern**: `[-._\w]+`
- **Min Length**: 1
- **Max Length**: 100

### RefererPattern
- **Type**: string
- **Pattern**: `([$\-._+!*\x{60}(),;/?:@=&\w]|%([0-9a-fA-F?]{2}|[0-9a-fA-F?]?[*]))+`
- **Min Length**: 0
- **Max Length**: 253

### ResourceName
- **Type**: string
- **Pattern**: `[-._\w]+`
- **Min Length**: 1
- **Max Length**: 100

### TagKey
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `([\p{L}\p{Z}\p{N}_.,:/=+\-@]*)`
- **Min Length**: 0
- **Max Length**: 256

### Uuid
- **Type**: string
- **Pattern**: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

### WiFiAccessPointMacAddressString
- **Type**: string
- **Pattern**: `([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})`
- **Min Length**: 12
- **Max Length**: 17

