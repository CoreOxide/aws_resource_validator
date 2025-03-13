# Account Service

### AccountId
- **Type**: string
- **Pattern**: `^\d{12}$`

### ContactInformationPhoneNumber
- **Type**: string
- **Pattern**: `^[+][\s0-9()-]+$`
- **Min Length**: 1
- **Max Length**: 20

### EmailAddress
- **Type**: string
- **Pattern**: `^[\s]*[\w+=.#|!&-]+@[\w.-]+\.[\w]+[\s]*$`
- **Min Length**: 1
- **Max Length**: 254

### Otp
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{6}$`

### PhoneNumber
- **Type**: string
- **Pattern**: `^[\s0-9()+-]+$`
- **Min Length**: 1
- **Max Length**: 25

