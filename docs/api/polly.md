# Polly Service

### LexiconName
- **Type**: string
- **Pattern**: `[0-9A-Za-z]{1,20}`

### OutputS3BucketName
- **Type**: string
- **Pattern**: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`

### OutputS3KeyPrefix
- **Type**: string
- **Pattern**: `^[0-9a-zA-Z\/\!\-_\.\*\\'\(\):;\$@=+\,\?&]{0,800}$`

### SnsTopicArn
- **Type**: string
- **Pattern**: `^arn:aws(-(cn|iso(-b)?|us-gov))?:sns:[a-z0-9_-]{1,50}:\d{12}:[a-zA-Z0-9_-]{1,251}([a-zA-Z0-9_-]{0,5}|\.fifo)$`

### TaskId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,100}$`

