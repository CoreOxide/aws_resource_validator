# Elastictranscoder Service

### AccessControl
- **Type**: string
- **Pattern**: `(^FullControl$)|(^Read$)|(^ReadAcp$)|(^WriteAcp$)`

### Ascending
- **Type**: string
- **Pattern**: `(^true$)|(^false$)`

### AspectRatio
- **Type**: string
- **Pattern**: `(^auto$)|(^1:1$)|(^4:3$)|(^3:2$)|(^16:9$)`

### AudioBitDepth
- **Type**: string
- **Pattern**: `(^8$)|(^16$)|(^24$)|(^32$)`

### AudioBitOrder
- **Type**: string
- **Pattern**: `(^LittleEndian$)`

### AudioBitRate
- **Type**: string
- **Pattern**: `^\d{1,3}$`

### AudioChannels
- **Type**: string
- **Pattern**: `(^auto$)|(^0$)|(^1$)|(^2$)`

### AudioCodec
- **Type**: string
- **Pattern**: `(^AAC$)|(^vorbis$)|(^mp3$)|(^mp2$)|(^pcm$)|(^flac$)`

### AudioCodecProfile
- **Type**: string
- **Pattern**: `(^auto$)|(^AAC-LC$)|(^HE-AAC$)|(^HE-AACv2$)`

### AudioPackingMode
- **Type**: string
- **Pattern**: `(^SingleTrack$)|(^OneChannelPerTrack$)|(^OneChannelPerTrackWithMosTo8Tracks$)`

### AudioSampleRate
- **Type**: string
- **Pattern**: `(^auto$)|(^22050$)|(^32000$)|(^44100$)|(^48000$)|(^96000$)|(^192000$)`

### AudioSigned
- **Type**: string
- **Pattern**: `(^Unsigned$)|(^Signed$)`

### Base64EncodedString
- **Type**: string
- **Pattern**: `^$|(^(?:[A-Za-z0-9\+/]{4})*(?:[A-Za-z0-9\+/]{2}==|[A-Za-z0-9\+/]{3}=)?$)`

### BucketName
- **Type**: string
- **Pattern**: `^(\w|\.|-){1,255}$`

### CaptionFormatFormat
- **Type**: string
- **Pattern**: `(^mov-text$)|(^srt$)|(^scc$)|(^webvtt$)|(^dfxp$)|(^cea-708$)`

### CaptionFormatPattern
- **Type**: string
- **Pattern**: `(^$)|(^.*\{language\}.*$)`

### CaptionMergePolicy
- **Type**: string
- **Pattern**: `(^MergeOverride$)|(^MergeRetain$)|(^Override$)`

### Digits
- **Type**: string
- **Pattern**: `^\d{1,5}$`

### DigitsOrAuto
- **Type**: string
- **Pattern**: `(^auto$)|(^\d{2,4}$)`

### EncryptionMode
- **Type**: string
- **Pattern**: `(^s3$)|(^s3-aws-kms$)|(^aes-cbc-pkcs7$)|(^aes-ctr$)|(^aes-gcm$)`

### FixedGOP
- **Type**: string
- **Pattern**: `(^true$)|(^false$)`

### FloatString
- **Type**: string
- **Pattern**: `^\d{1,5}(\.\d{0,5})?$`

### FrameRate
- **Type**: string
- **Pattern**: `(^auto$)|(^10$)|(^15$)|(^23.97$)|(^24$)|(^25$)|(^29.97$)|(^30$)|(^50$)|(^60$)`

### GranteeType
- **Type**: string
- **Pattern**: `(^Canonical$)|(^Email$)|(^Group$)`

### HlsContentProtectionMethod
- **Type**: string
- **Pattern**: `(^aes-128$)`

### HorizontalAlign
- **Type**: string
- **Pattern**: `(^Left$)|(^Right$)|(^Center$)`

### Id
- **Type**: string
- **Pattern**: `^\d{13}-\w{6}$`

### Interlaced
- **Type**: string
- **Pattern**: `(^auto$)|(^true$)|(^false$)`

### JobContainer
- **Type**: string
- **Pattern**: `(^auto$)|(^3gp$)|(^asf$)|(^avi$)|(^divx$)|(^flv$)|(^mkv$)|(^mov$)|(^mp4$)|(^mpeg$)|(^mpeg-ps$)|(^mpeg-ts$)|(^mxf$)|(^ogg$)|(^ts$)|(^vob$)|(^wav$)|(^webm$)|(^mp3$)|(^m4a$)|(^aac$)`

### JobStatus
- **Type**: string
- **Pattern**: `(^Submitted$)|(^Progressing$)|(^Complete$)|(^Canceled$)|(^Error$)`

### JpgOrPng
- **Type**: string
- **Pattern**: `(^jpg$)|(^png$)`

### KeyIdGuid
- **Type**: string
- **Pattern**: `(^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$)|(^[0-9A-Fa-f]{32}$)`

### KeyStoragePolicy
- **Type**: string
- **Pattern**: `(^NoStore$)|(^WithVariantPlaylists$)`

### KeyframesMaxDist
- **Type**: string
- **Pattern**: `^\d{1,6}$`

### MaxFrameRate
- **Type**: string
- **Pattern**: `(^10$)|(^15$)|(^23.97$)|(^24$)|(^25$)|(^29.97$)|(^30$)|(^50$)|(^60$)`

### MergePolicy
- **Type**: string
- **Pattern**: `(^Replace$)|(^Prepend$)|(^Append$)|(^Fallback$)`

### NonEmptyBase64EncodedString
- **Type**: string
- **Pattern**: `(^(?:[A-Za-z0-9\+/]{4})*(?:[A-Za-z0-9\+/]{2}==|[A-Za-z0-9\+/]{3}=)?$)`

### Opacity
- **Type**: string
- **Pattern**: `^\d{1,3}(\.\d{0,20})?$`

### PaddingPolicy
- **Type**: string
- **Pattern**: `(^Pad$)|(^NoPad$)`

### PipelineStatus
- **Type**: string
- **Pattern**: `(^Active$)|(^Paused$)`

### PixelsOrPercent
- **Type**: string
- **Pattern**: `(^\d{1,3}(\.\d{0,5})?%$)|(^\d{1,4}?px$)`

### PlayReadyDrmFormatString
- **Type**: string
- **Pattern**: `(^microsoft$)|(^discretix-3.0$)`

### PlaylistFormat
- **Type**: string
- **Pattern**: `(^HLSv3$)|(^HLSv4$)|(^Smooth$)|(^MPEG-DASH$)`

### PresetContainer
- **Type**: string
- **Pattern**: `(^mp4$)|(^ts$)|(^webm$)|(^mp3$)|(^flac$)|(^oga$)|(^ogg$)|(^fmp4$)|(^mpg$)|(^flv$)|(^gif$)|(^mxf$)|(^wav$)|(^mp2$)`

### PresetType
- **Type**: string
- **Pattern**: `(^System$)|(^Custom$)`

### Resolution
- **Type**: string
- **Pattern**: `(^auto$)|(^\d{1,5}x\d{1,5}$)`

### Role
- **Type**: string
- **Pattern**: `^arn:aws:iam::\w{12}:role/.+$`

### Rotate
- **Type**: string
- **Pattern**: `(^auto$)|(^0$)|(^90$)|(^180$)|(^270$)`

### SizingPolicy
- **Type**: string
- **Pattern**: `(^Fit$)|(^Fill$)|(^Stretch$)|(^Keep$)|(^ShrinkToFit$)|(^ShrinkToFill$)`

### SnsTopic
- **Type**: string
- **Pattern**: `(^$)|(^arn:aws:sns:.*:\w{12}:.+$)`

### StorageClass
- **Type**: string
- **Pattern**: `(^ReducedRedundancy$)|(^Standard$)`

### Success
- **Type**: string
- **Pattern**: `(^true$)|(^false$)`

### Target
- **Type**: string
- **Pattern**: `(^Content$)|(^Frame$)`

### ThumbnailPattern
- **Type**: string
- **Pattern**: `(^$)|(^.*\{count\}.*$)`

### ThumbnailResolution
- **Type**: string
- **Pattern**: `^\d{1,5}x\d{1,5}$`

### Time
- **Type**: string
- **Pattern**: `(^\d{1,5}(\.\d{0,3})?$)|(^([0-1]?[0-9]:|2[0-3]:)?([0-5]?[0-9]:)?[0-5]?[0-9](\.\d{0,3})?$)`

### TimeOffset
- **Type**: string
- **Pattern**: `(^[+-]?\d{1,5}(\.\d{0,3})?$)|(^[+-]?([0-1]?[0-9]:|2[0-3]:)?([0-5]?[0-9]:)?[0-5]?[0-9](\.\d{0,3})?$)`

### VerticalAlign
- **Type**: string
- **Pattern**: `(^Top$)|(^Bottom$)|(^Center$)`

### VideoBitRate
- **Type**: string
- **Pattern**: `(^\d{2,5}$)|(^auto$)`

### VideoCodec
- **Type**: string
- **Pattern**: `(^H\.264$)|(^vp8$)|(^vp9$)|(^mpeg2$)|(^gif$)`

### WatermarkKey
- **Type**: string
- **Pattern**: `(^.{1,1020}.jpg$)|(^.{1,1019}.jpeg$)|(^.{1,1020}.png$)`
- **Min Length**: 1
- **Max Length**: 1024

### WatermarkSizingPolicy
- **Type**: string
- **Pattern**: `(^Fit$)|(^Stretch$)|(^ShrinkToFit$)`

