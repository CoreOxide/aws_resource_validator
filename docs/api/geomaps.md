# Geomaps Service

### CountryCode
- **Type**: string
- **Pattern**: `([A-Z]{2}|[A-Z]{3})`
- **Min Length**: 2
- **Max Length**: 3

### GetGlyphsRequestFontUnicodeRangeString
- **Type**: string
- **Pattern**: `[0-9]+-[0-9]+\.pbf`

### GetSpritesRequestFileNameString
- **Type**: string
- **Pattern**: `sprites(@2x)?\.(png|json)`

### GetStaticMapRequestFileNameString
- **Type**: string
- **Pattern**: `map(@2x)?`

### GetTileRequestXString
- **Type**: string
- **Pattern**: `.*\d+.*`

### GetTileRequestYString
- **Type**: string
- **Pattern**: `.*\d+.*`

### GetTileRequestZString
- **Type**: string
- **Pattern**: `.*\d+.*`

### PositionListString
- **Type**: string
- **Pattern**: `(-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?)(,(-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?))*`
- **Min Length**: 7

### PositionString
- **Type**: string
- **Pattern**: `-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?`
- **Min Length**: 3
- **Max Length**: 36

### Tileset
- **Type**: string
- **Pattern**: `[-.\w]+`
- **Min Length**: 1
- **Max Length**: 100

