# Licensemanager Service

### Arn
- **Type**: string
- **Pattern**: `^arn:aws(-(cn|us-gov|iso-b|iso-c|iso-d))?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
- **Max Length**: 2048

### ClientToken
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 2048

### ISO8601DateTime
- **Type**: string
- **Pattern**: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`
- **Max Length**: 50

### LicenseConversionTaskId
- **Type**: string
- **Pattern**: `^lct-[a-zA-Z0-9]*`
- **Max Length**: 50

### StatusReasonMessage
- **Type**: string
- **Pattern**: `[\s\S]+`
- **Max Length**: 400

### TokenString
- **Type**: string
- **Pattern**: `\S+`
- **Max Length**: 4096

