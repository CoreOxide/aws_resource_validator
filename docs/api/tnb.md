# Tnb Service

### NsInstanceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-instance/ni-[a-f0-9]{17})$`

### NsInstanceId
- **Type**: string
- **Pattern**: `^ni-[a-f0-9]{17}$`

### NsLcmOpOccArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-operation/no-[a-f0-9]{17})$`

### NsLcmOpOccId
- **Type**: string
- **Pattern**: `^no-[a-f0-9]{17}$`

### NsdId
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

### NsdInfoArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-package/np-[a-f0-9]{17})$`

### NsdInfoId
- **Type**: string
- **Pattern**: `^np-[a-f0-9]{17}$`

### TNBResourceArn
- **Type**: string
- **Pattern**: `^arn:aws:tnb:[a-z0-9-]+:[^:]*:.*$`

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:).{1,128}$`

### VnfInstanceArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(function-instance/fi-[a-f0-9]{17})$`

### VnfInstanceId
- **Type**: string
- **Pattern**: `^fi-[a-f0-9]{17}$`

### VnfPkgArn
- **Type**: string
- **Pattern**: `^arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(function-package/fp-[a-f0-9]{17})$`

### VnfPkgId
- **Type**: string
- **Pattern**: `^fp-[a-f0-9]{17}$`

### VnfdId
- **Type**: string
- **Pattern**: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

