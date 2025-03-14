# Mediaconvert Service

### __stringMax2048PatternS3Https
- **Type**: string
- **Pattern**: `^s3://([^\/]+\/+)+((([^\/]*)))|^https?://[^\/].*[^&]$`
- **Max Length**: 2048

### __stringMin11Max11Pattern01D20305D205D
- **Type**: string
- **Pattern**: `^((([0-1]\d)|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$`
- **Min Length**: 11
- **Max Length**: 11

### __stringMin14PatternS3BmpBMPPngPNGHttpsBmpBMPPngPNG
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(bmp|BMP|png|PNG))|(https?://(.*?)\.(bmp|BMP|png|PNG)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### __stringMin14PatternS3BmpBMPPngPNGTgaTGAHttpsBmpBMPPngPNGTgaTGA
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(bmp|BMP|png|PNG|tga|TGA))|(https?://(.*?)\.(bmp|BMP|png|PNG|tga|TGA)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### __stringMin14PatternS3CubeCUBEHttpsCubeCUBE
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(cube|CUBE))|(https?://(.*?)\.(cube|CUBE)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### __stringMin14PatternS3Mov09PngHttpsMov09Png
- **Type**: string
- **Pattern**: `^((s3://(.*)(\.mov|[0-9]+\.png))|(https?://(.*)(\.mov|[0-9]+\.png)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### __stringMin14PatternS3SccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTTHttpsSccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTT
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(scc|SCC|ttml|TTML|dfxp|DFXP|stl|STL|srt|SRT|xml|XML|smi|SMI|vtt|VTT|webvtt|WEBVTT))|(https?://(.*?)\.(scc|SCC|ttml|TTML|dfxp|DFXP|stl|STL|srt|SRT|xml|XML|smi|SMI|vtt|VTT|webvtt|WEBVTT)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### __stringMin14PatternS3XmlXMLHttpsXmlXML
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(xml|XML))|(https?://(.*?)\.(xml|XML)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### __stringMin16Max24PatternAZaZ0922AZaZ0916
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+\/]{22}==$|^[A-Za-z0-9+\/]{16}$`
- **Min Length**: 16
- **Max Length**: 24

### __stringMin1Max2048PatternArnAZSecretsmanagerWD12SecretAZAZ09
- **Type**: string
- **Pattern**: `^(arn:[a-z-]+:secretsmanager:[\w-]+:\d{12}:secret:)?[a-zA-Z0-9_\/_+=.@-]*$`
- **Min Length**: 1
- **Max Length**: 2048

### __stringMin1Max50PatternAZAZ09
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\/_+=.@-]*$`
- **Min Length**: 1
- **Max Length**: 50

### __stringMin24Max512PatternAZaZ0902
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+\/]+={0,2}$`
- **Min Length**: 24
- **Max Length**: 512

### __stringMin32Max32Pattern09aFAF32
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{32}$`
- **Min Length**: 32
- **Max Length**: 32

### __stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### __stringMin3Max3Pattern1809aFAF09aEAE
- **Type**: string
- **Pattern**: `^[1-8][0-9a-fA-F][0-9a-eA-E]$`
- **Min Length**: 3
- **Max Length**: 3

### __stringMin3Max3PatternAZaZ3
- **Type**: string
- **Pattern**: `^[A-Za-z]{3}$`
- **Min Length**: 3
- **Max Length**: 3

### __stringMin6Max8Pattern09aFAF609aFAF2
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$`
- **Min Length**: 6
- **Max Length**: 8

### __stringMin9Max19PatternAZ26EastWestCentralNorthSouthEastWest1912
- **Type**: string
- **Pattern**: `^[a-z-]{2,6}-(east|west|central|((north|south)(east|west)?))-[1-9]{1,2}$`
- **Min Length**: 9
- **Max Length**: 19

### __stringPattern
- **Type**: string
- **Pattern**: `^[ -~]+$`

### __stringPattern010920405090509092
- **Type**: string
- **Pattern**: `^([01][0-9]|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$`

### __stringPattern010920405090509092090909
- **Type**: string
- **Pattern**: `^([01][0-9]|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}(@[0-9]+(\.[0-9]+)?(:[0-9]+)?)?$`

### __stringPattern01D20305D205D
- **Type**: string
- **Pattern**: `^((([0-1]\d)|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$`

### __stringPattern0940191020191209301
- **Type**: string
- **Pattern**: `^([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$`

### __stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### __stringPattern0xAFaF0908190908
- **Type**: string
- **Pattern**: `(^0x[A-Fa-f0-9]{0,8}$|^[1-9][0-9]{0,8}$)`

### __stringPatternAZaZ0902
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+\/]+={0,2}$`

### __stringPatternAZaZ0932
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]{32}$`

### __stringPatternAZaZ23AZaZ
- **Type**: string
- **Pattern**: `^[A-Za-z]{2,3}(-[A-Za-z-]+)?$`

### __stringPatternAZaZ23AZaZ09
- **Type**: string
- **Pattern**: `^[A-Za-z]{2,3}(-[A-Za-z0-9-]+)?$`

### __stringPatternArnAwsUsGovAcm
- **Type**: string
- **Pattern**: `^arn:aws(-us-gov)?:acm:`

### __stringPatternArnAwsUsGovCnKmsAZ26EastWestCentralNorthSouthEastWest1912D12KeyAFAF098AFAF094AFAF094AFAF094AFAF0912MrkAFAF0932
- **Type**: string
- **Pattern**: `^arn:aws(-us-gov|-cn)?:kms:[a-z-]{2,6}-(east|west|central|((north|south)(east|west)?))-[1-9]{1,2}:\d{12}:key/([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}|mrk-[a-fA-F0-9]{32})$`

### __stringPatternDD
- **Type**: string
- **Pattern**: `^(\d+(\/\d+)*)$`

### __stringPatternHttps
- **Type**: string
- **Pattern**: `^https:\/\/`

### __stringPatternHttpsD
- **Type**: string
- **Pattern**: `^https:\/\/[^:@\/]*(:\d*)?(\/.*)?$`

### __stringPatternHttpsKantarmedia
- **Type**: string
- **Pattern**: `^https:\/\/.*.kantarmedia.*$`

### __stringPatternIdentityAZaZ26AZaZ09163
- **Type**: string
- **Pattern**: `^(identity|[A-Za-z]{2,6}(\.[A-Za-z0-9-]{1,63})+)$`

### __stringPatternS3
- **Type**: string
- **Pattern**: `^s3:\/\/`

### __stringPatternS3ASSETMAPXml
- **Type**: string
- **Pattern**: `^s3:\/\/.*\/(ASSETMAP.xml)?$`

### __stringPatternS3Https
- **Type**: string
- **Pattern**: `^s3://([^\/]+\/+)+((([^\/]*)))|^https?://[^\/].*[^&]$`

### __stringPatternS3TtfHttpsTtf
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(ttf))|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`

### __stringPatternSNManifestConfirmConditionNotificationNS
- **Type**: string
- **Pattern**: `^\s*<(.|\n)*ManifestConfirmConditionNotification(.|\n)*>\s*$`

### __stringPatternSNSignalProcessingNotificationNS
- **Type**: string
- **Pattern**: `^\s*<(.|\n)*SignalProcessingNotification(.|\n)*>\s*$`

### __stringPatternW
- **Type**: string
- **Pattern**: `^[\w-]+$`

### __stringPatternWS
- **Type**: string
- **Pattern**: `^[\w\s]*$`

