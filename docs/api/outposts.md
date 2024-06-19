# Outposts Service

### AccountId
- **Type**: string
- **Pattern**: `\d{12}`
- **Min Length**: 12
- **Max Length**: 12

### AddressLine1
- **Type**: string
- **Pattern**: `^\S[\S ]*$`
- **Min Length**: 1
- **Max Length**: 180

### AddressLine2
- **Type**: string
- **Pattern**: `^\S[\S ]*$`
- **Min Length**: 0
- **Max Length**: 60

### AddressLine3
- **Type**: string
- **Pattern**: `^\S[\S ]*$`
- **Min Length**: 0
- **Max Length**: 60

### Arn
- **Type**: string
- **Pattern**: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:([a-z\d-]+)/)[a-z]{2,8}-[a-f0-9]{17}$`
- **Max Length**: 1011

### AssetId
- **Type**: string
- **Pattern**: `^(\w+)$`
- **Min Length**: 1
- **Max Length**: 100

### AvailabilityZone
- **Type**: string
- **Pattern**: `^([a-zA-Z]+-){1,3}([a-zA-Z]+)?(\d+[a-zA-Z]?)?$`
- **Min Length**: 1
- **Max Length**: 1000

### AvailabilityZoneId
- **Type**: string
- **Pattern**: `^[a-zA-Z]+\d-[a-zA-Z]+\d$`
- **Min Length**: 1
- **Max Length**: 255

### CIDR
- **Type**: string
- **Pattern**: `^([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$`
- **Min Length**: 9
- **Max Length**: 18

### CapacityTaskId
- **Type**: string
- **Pattern**: `^cap-[a-f0-9]{17}$`
- **Min Length**: 21
- **Max Length**: 21

### City
- **Type**: string
- **Pattern**: `^\S[\S ]*$`
- **Min Length**: 1
- **Max Length**: 50

### ConnectionId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+/=]{1,1024}$`
- **Min Length**: 1
- **Max Length**: 1024

### ContactName
- **Type**: string
- **Pattern**: `^\S[\S ]*$`
- **Min Length**: 1
- **Max Length**: 255

### ContactPhoneNumber
- **Type**: string
- **Pattern**: `^[\S ]+$`
- **Min Length**: 1
- **Max Length**: 20

### CountryCode
- **Type**: string
- **Pattern**: `^[A-Z]{2}$`
- **Min Length**: 2
- **Max Length**: 2

### DeviceSerialNumber
- **Type**: string
- **Pattern**: `^(\w+)$`
- **Min Length**: 1
- **Max Length**: 100

### DistrictOrCounty
- **Type**: string
- **Pattern**: `^\S[\S ]*`
- **Min Length**: 1
- **Max Length**: 60

### ErrorMessage
- **Type**: string
- **Pattern**: `^[\S \n]+$`
- **Min Length**: 1
- **Max Length**: 1000

### Family
- **Type**: string
- **Pattern**: `[a-z0-9]+`
- **Min Length**: 1
- **Max Length**: 10

### HostId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-]*$`
- **Min Length**: 1
- **Max Length**: 50

### InstanceFamilyName
- **Type**: string
- **Pattern**: `^(?:.{1,200}/)?(?:[a-z0-9-_A-Z])+$`
- **Min Length**: 1
- **Max Length**: 200

### InstanceTypeName
- **Type**: string
- **Pattern**: `^[a-z0-9\-]+\.[a-z0-9\-]+$`
- **Min Length**: 1
- **Max Length**: 64

### LifeCycleStatus
- **Type**: string
- **Pattern**: `^[ A-Za-z]+$`
- **Min Length**: 1
- **Max Length**: 20

### LineItemId
- **Type**: string
- **Pattern**: `ooi-[a-f0-9]{17}`

### MacAddress
- **Type**: string
- **Pattern**: `^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$`
- **Min Length**: 17
- **Max Length**: 17

### Municipality
- **Type**: string
- **Pattern**: `^\S[\S ]*$`
- **Min Length**: 0
- **Max Length**: 180

### OrderId
- **Type**: string
- **Pattern**: `oo-[a-f0-9]{17}$`
- **Min Length**: 1
- **Max Length**: 20

### OutpostArn
- **Type**: string
- **Pattern**: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
- **Min Length**: 1
- **Max Length**: 255

### OutpostDescription
- **Type**: string
- **Pattern**: `^[\S ]*$`
- **Min Length**: 0
- **Max Length**: 1000

### OutpostId
- **Type**: string
- **Pattern**: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
- **Min Length**: 1
- **Max Length**: 180

### OutpostIdOnly
- **Type**: string
- **Pattern**: `^op-[a-f0-9]{17}$`
- **Min Length**: 1
- **Max Length**: 20

### OutpostIdentifier
- **Type**: string
- **Pattern**: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
- **Min Length**: 1
- **Max Length**: 180

### OutpostName
- **Type**: string
- **Pattern**: `^[\S ]+$`
- **Min Length**: 1
- **Max Length**: 255

### OwnerId
- **Type**: string
- **Pattern**: `\d{12}`
- **Min Length**: 12
- **Max Length**: 12

### PostalCode
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9 -]+$`
- **Min Length**: 1
- **Max Length**: 20

### RackId
- **Type**: string
- **Pattern**: `^[\S \n]+$`
- **Min Length**: 5
- **Max Length**: 20

### ServerEndpoint
- **Type**: string
- **Pattern**: `^([0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{1,5}$`
- **Min Length**: 9
- **Max Length**: 21

### SiteArn
- **Type**: string
- **Pattern**: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/(os-[a-f0-9]{17})$`
- **Min Length**: 1
- **Max Length**: 255

### SiteDescription
- **Type**: string
- **Pattern**: `^[\S ]+$`
- **Min Length**: 1
- **Max Length**: 1001

### SiteId
- **Type**: string
- **Pattern**: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
- **Min Length**: 1
- **Max Length**: 255

### SiteName
- **Type**: string
- **Pattern**: `^[\S ]+$`
- **Min Length**: 1
- **Max Length**: 1000

### SiteNotes
- **Type**: string
- **Pattern**: `^[\S \n]+$`
- **Min Length**: 1
- **Max Length**: 2000

### SkuCode
- **Type**: string
- **Pattern**: `OR-[A-Z0-9]{7}`
- **Min Length**: 1
- **Max Length**: 10

### StateOrRegion
- **Type**: string
- **Pattern**: `^\S[\S ]*$`
- **Min Length**: 1
- **Max Length**: 50

### String
- **Type**: string
- **Pattern**: `^[\S \n]+$`
- **Min Length**: 1
- **Max Length**: 1000

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[\S \n]+$`
- **Max Length**: 256

### Token
- **Type**: string
- **Pattern**: `^(\d+)##(\S+)$`
- **Min Length**: 1
- **Max Length**: 2048

### TrackingId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 6
- **Max Length**: 42

### UnderlayIpAddress
- **Type**: string
- **Pattern**: `^([0-9]{1,3}\.){3}[0-9]{1,3}$`
- **Min Length**: 7
- **Max Length**: 15

### WireGuardPublicKey
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9/+]{43}=$`
- **Min Length**: 44
- **Max Length**: 44

