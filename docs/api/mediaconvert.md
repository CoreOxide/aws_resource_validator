# Mediaconvert Service

### stringMin11Max11Pattern01D20305D205D
- **Type**: string
- **Pattern**: `^((([0-1]\d)|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$`
- **Min Length**: 11
- **Max Length**: 11

### stringMin14PatternS3BmpBMPPngPNGHttpsBmpBMPPngPNG
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(bmp|BMP|png|PNG))|(https?://(.*?)\.(bmp|BMP|png|PNG)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### stringMin14PatternS3BmpBMPPngPNGTgaTGAHttpsBmpBMPPngPNGTgaTGA
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(bmp|BMP|png|PNG|tga|TGA))|(https?://(.*?)\.(bmp|BMP|png|PNG|tga|TGA)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### stringMin14PatternS3CubeCUBEHttpsCubeCUBE
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(cube|CUBE))|(https?://(.*?)\.(cube|CUBE)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### stringMin14PatternS3Mov09PngHttpsMov09Png
- **Type**: string
- **Pattern**: `^((s3://(.*)(\.mov|[0-9]+\.png))|(https?://(.*)(\.mov|[0-9]+\.png)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### stringMin14PatternS3SccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTTHttpsSccSCCTtmlTTMLDfxpDFXPStlSTLSrtSRTXmlXMLSmiSMIVttVTTWebvttWEBVTT
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(scc|SCC|ttml|TTML|dfxp|DFXP|stl|STL|srt|SRT|xml|XML|smi|SMI|vtt|VTT|webvtt|WEBVTT))|(https?://(.*?)\.(scc|SCC|ttml|TTML|dfxp|DFXP|stl|STL|srt|SRT|xml|XML|smi|SMI|vtt|VTT|webvtt|WEBVTT)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### stringMin14PatternS3XmlXMLHttpsXmlXML
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(xml|XML))|(https?://(.*?)\.(xml|XML)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`
- **Min Length**: 14

### stringMin16Max24PatternAZaZ0922AZaZ0916
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+\/]{22}==$|^[A-Za-z0-9+\/]{16}$`
- **Min Length**: 16
- **Max Length**: 24

### stringMin1Max50PatternAZAZ09
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\/_+=.@-]*$`
- **Min Length**: 1
- **Max Length**: 50

### stringMin1Max512PatternAZAZ09
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_\/_+=.@-]*$`
- **Min Length**: 1
- **Max Length**: 512

### stringMin24Max512PatternAZaZ0902
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+\/]+={0,2}$`
- **Min Length**: 24
- **Max Length**: 512

### stringMin32Max32Pattern09aFAF32
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{32}$`
- **Min Length**: 32
- **Max Length**: 32

### stringMin36Max36Pattern09aFAF809aFAF409aFAF409aFAF409aFAF12
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
- **Min Length**: 36
- **Max Length**: 36

### stringMin3Max3Pattern1809aFAF09aEAE
- **Type**: string
- **Pattern**: `^[1-8][0-9a-fA-F][0-9a-eA-E]$`
- **Min Length**: 3
- **Max Length**: 3

### stringMin3Max3PatternAZaZ3
- **Type**: string
- **Pattern**: `^[A-Za-z]{3}$`
- **Min Length**: 3
- **Max Length**: 3

### stringMin6Max8Pattern09aFAF609aFAF2
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$`
- **Min Length**: 6
- **Max Length**: 8

### stringMin9Max19PatternAZ26EastWestCentralNorthSouthEastWest1912
- **Type**: string
- **Pattern**: `^[a-z-]{2,6}-(east|west|central|((north|south)(east|west)?))-[1-9]{1,2}$`
- **Min Length**: 9
- **Max Length**: 19

### stringPattern
- **Type**: string
- **Pattern**: `^[ -~]+$`

### stringPattern010920405090509092
- **Type**: string
- **Pattern**: `^([01][0-9]|2[0-4]):[0-5][0-9]:[0-5][0-9][:;][0-9]{2}$`

### stringPattern01D20305D205D
- **Type**: string
- **Pattern**: `^((([0-1]\d)|(2[0-3]))(:[0-5]\d){2}([:;][0-5]\d))$`

### stringPattern0940191020191209301
- **Type**: string
- **Pattern**: `^([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$`

### stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### stringPattern0xAFaF0908190908
- **Type**: string
- **Pattern**: `(^0x[A-Fa-f0-9]{0,8}$|^[1-9][0-9]{0,8}$)`

### stringPatternAZaZ0902
- **Type**: string
- **Pattern**: `^[A-Za-z0-9+\/]+={0,2}$`

### stringPatternAZaZ0932
- **Type**: string
- **Pattern**: `^[A-Za-z0-9]{32}$`

### stringPatternAZaZ23AZaZ
- **Type**: string
- **Pattern**: `^[A-Za-z]{2,3}(-[A-Za-z-]+)?$`

### stringPatternAZaZ23AZaZ09
- **Type**: string
- **Pattern**: `^[A-Za-z]{2,3}(-[A-Za-z0-9-]+)?$`

### stringPatternArnAwsUsGovAcm
- **Type**: string
- **Pattern**: `^arn:aws(-us-gov)?:acm:`

### stringPatternArnAwsUsGovCnKmsAZ26EastWestCentralNorthSouthEastWest1912D12KeyAFAF098AFAF094AFAF094AFAF094AFAF0912MrkAFAF0932
- **Type**: string
- **Pattern**: `^arn:aws(-us-gov|-cn)?:kms:[a-z-]{2,6}-(east|west|central|((north|south)(east|west)?))-[1-9]{1,2}:\d{12}:key/([a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}|mrk-[a-fA-F0-9]{32})$`

### stringPatternDD
- **Type**: string
- **Pattern**: `^(\d+(\/\d+)*)$`

### stringPatternHttps
- **Type**: string
- **Pattern**: `^https:\/\/`

### stringPatternHttpsD
- **Type**: string
- **Pattern**: `^https:\/\/[^:@\/]*(:\d*)?(\/.*)?$`

### stringPatternHttpsKantarmedia
- **Type**: string
- **Pattern**: `^https:\/\/.*.kantarmedia.*$`

### stringPatternIdentityAZaZ26AZaZ09163
- **Type**: string
- **Pattern**: `^(identity|[A-Za-z]{2,6}(\.[A-Za-z0-9-]{1,63})+)$`

### stringPatternS3
- **Type**: string
- **Pattern**: `^s3:\/\/`

### stringPatternS3ASSETMAPXml
- **Type**: string
- **Pattern**: `^s3:\/\/.*\/(ASSETMAP.xml)?$`

### stringPatternS3Https
- **Type**: string
- **Pattern**: `^s3://([^\/]+\/+)+((([^\/]*)))|^https?://[^\/].*[^&]$`

### stringPatternS3TtfHttpsTtf
- **Type**: string
- **Pattern**: `^((s3://(.*?)\.(ttf))|(https?://(.*?)\.(ttf)(\?([^&=]+=[^&]+&)*[^&=]+=[^&]+)?))$`

### stringPatternSNManifestConfirmConditionNotificationNS
- **Type**: string
- **Pattern**: `^\s*<(.|\n)*ManifestConfirmConditionNotification(.|\n)*>\s*$`

### stringPatternSNSignalProcessingNotificationNS
- **Type**: string
- **Pattern**: `^\s*<(.|\n)*SignalProcessingNotification(.|\n)*>\s*$`

### stringPatternW
- **Type**: string
- **Pattern**: `^[\w-]+$`

### stringPatternWS
- **Type**: string
- **Pattern**: `^[\w\s]*$`

