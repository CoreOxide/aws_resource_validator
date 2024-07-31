from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AnalyticsS3ExportFileFormatType = Literal["CSV"]
ArchiveStatusType = Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
BucketAccelerateStatusType = Literal["Enabled", "Suspended"]
BucketCannedACLType = Literal["authenticated-read", "private", "public-read", "public-read-write"]
BucketExistsWaiterName = Literal["bucket_exists"]
BucketLocationConstraintType = Literal["EU",
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-2",
    "us-gov-east-1",
    "us-gov-west-1",
    "us-west-1",
    "us-west-2",]
BucketLogsPermissionType = Literal["FULL_CONTROL", "READ", "WRITE"]
BucketNotExistsWaiterName = Literal["bucket_not_exists"]
BucketTypeType = Literal["Directory"]
BucketVersioningStatusType = Literal["Enabled", "Suspended"]
ChecksumAlgorithmType = Literal["CRC32", "CRC32C", "SHA1", "SHA256"]
ChecksumModeType = Literal["ENABLED"]
CompressionTypeType = Literal["BZIP2", "GZIP", "NONE"]
DataRedundancyType = Literal["SingleAvailabilityZone"]
DeleteMarkerReplicationStatusType = Literal["Disabled", "Enabled"]
EncodingTypeType = Literal["url"]
EventType = Literal["s3:IntelligentTiering",
    "s3:LifecycleExpiration:*",
    "s3:LifecycleExpiration:Delete",
    "s3:LifecycleExpiration:DeleteMarkerCreated",
    "s3:LifecycleTransition",
    "s3:ObjectAcl:Put",
    "s3:ObjectCreated:*",
    "s3:ObjectCreated:CompleteMultipartUpload",
    "s3:ObjectCreated:Copy",
    "s3:ObjectCreated:Post",
    "s3:ObjectCreated:Put",
    "s3:ObjectRemoved:*",
    "s3:ObjectRemoved:Delete",
    "s3:ObjectRemoved:DeleteMarkerCreated",
    "s3:ObjectRestore:*",
    "s3:ObjectRestore:Completed",
    "s3:ObjectRestore:Delete",
    "s3:ObjectRestore:Post",
    "s3:ObjectTagging:*",
    "s3:ObjectTagging:Delete",
    "s3:ObjectTagging:Put",
    "s3:ReducedRedundancyLostObject",
    "s3:Replication:*",
    "s3:Replication:OperationFailedReplication",
    "s3:Replication:OperationMissedThreshold",
    "s3:Replication:OperationNotTracked",
    "s3:Replication:OperationReplicatedAfterThreshold",]
ExistingObjectReplicationStatusType = Literal["Disabled", "Enabled"]
ExpirationStatusType = Literal["Disabled", "Enabled"]
ExpressionTypeType = Literal["SQL"]
FileHeaderInfoType = Literal["IGNORE", "NONE", "USE"]
FilterRuleNameType = Literal["prefix", "suffix"]
IntelligentTieringAccessTierType = Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
IntelligentTieringStatusType = Literal["Disabled", "Enabled"]
InventoryFormatType = Literal["CSV", "ORC", "Parquet"]
InventoryFrequencyType = Literal["Daily", "Weekly"]
InventoryIncludedObjectVersionsType = Literal["All", "Current"]
InventoryOptionalFieldType = Literal["BucketKeyStatus",
    "ChecksumAlgorithm",
    "ETag",
    "EncryptionStatus",
    "IntelligentTieringAccessTier",
    "IsMultipartUploaded",
    "LastModifiedDate",
    "ObjectAccessControlList",
    "ObjectLockLegalHoldStatus",
    "ObjectLockMode",
    "ObjectLockRetainUntilDate",
    "ObjectOwner",
    "ReplicationStatus",
    "Size",
    "StorageClass",]
JSONTypeType = Literal["DOCUMENT", "LINES"]
ListDirectoryBucketsPaginatorName = Literal["list_directory_buckets"]
ListMultipartUploadsPaginatorName = Literal["list_multipart_uploads"]
ListObjectVersionsPaginatorName = Literal["list_object_versions"]
ListObjectsPaginatorName = Literal["list_objects"]
ListObjectsV2PaginatorName = Literal["list_objects_v2"]
ListPartsPaginatorName = Literal["list_parts"]
LocationTypeType = Literal["AvailabilityZone"]
MFADeleteStatusType = Literal["Disabled", "Enabled"]
MFADeleteType = Literal["Disabled", "Enabled"]
MetadataDirectiveType = Literal["COPY", "REPLACE"]
MetricsStatusType = Literal["Disabled", "Enabled"]
ObjectAttributesType = Literal["Checksum", "ETag", "ObjectParts", "ObjectSize", "StorageClass"]
ObjectCannedACLType = Literal["authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",]
ObjectExistsWaiterName = Literal["object_exists"]
ObjectLockEnabledType = Literal["Enabled"]
ObjectLockLegalHoldStatusType = Literal["OFF", "ON"]
ObjectLockModeType = Literal["COMPLIANCE", "GOVERNANCE"]
ObjectLockRetentionModeType = Literal["COMPLIANCE", "GOVERNANCE"]
ObjectNotExistsWaiterName = Literal["object_not_exists"]
ObjectOwnershipType = Literal["BucketOwnerEnforced", "BucketOwnerPreferred", "ObjectWriter"]
ObjectStorageClassType = Literal["DEEP_ARCHIVE",
    "EXPRESS_ONEZONE",
    "GLACIER",
    "GLACIER_IR",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "REDUCED_REDUNDANCY",
    "SNOW",
    "STANDARD",
    "STANDARD_IA",]
ObjectVersionStorageClassType = Literal["STANDARD"]
OptionalObjectAttributesType = Literal["RestoreStatus"]
OwnerOverrideType = Literal["Destination"]
PartitionDateSourceType = Literal["DeliveryTime", "EventTime"]
PayerType = Literal["BucketOwner", "Requester"]
PermissionType = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
ProtocolType = Literal["http", "https"]
QuoteFieldsType = Literal["ALWAYS", "ASNEEDED"]
ReplicaModificationsStatusType = Literal["Disabled", "Enabled"]
ReplicationRuleStatusType = Literal["Disabled", "Enabled"]
ReplicationStatusType = Literal["COMPLETE", "COMPLETED", "FAILED", "PENDING", "REPLICA"]
ReplicationTimeStatusType = Literal["Disabled", "Enabled"]
RequestChargedType = Literal["requester"]
RequestPayerType = Literal["requester"]
RestoreRequestTypeType = Literal["SELECT"]
ServerSideEncryptionType = Literal["AES256", "aws:kms", "aws:kms:dsse"]
SessionModeType = Literal["ReadOnly", "ReadWrite"]
SseKmsEncryptedObjectsStatusType = Literal["Disabled", "Enabled"]
StorageClassAnalysisSchemaVersionType = Literal["V_1"]
StorageClassType = Literal["DEEP_ARCHIVE",
    "EXPRESS_ONEZONE",
    "GLACIER",
    "GLACIER_IR",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "REDUCED_REDUNDANCY",
    "SNOW",
    "STANDARD",
    "STANDARD_IA",]
TaggingDirectiveType = Literal["COPY", "REPLACE"]
TierType = Literal["Bulk", "Expedited", "Standard"]
TransitionStorageClassType = Literal["DEEP_ARCHIVE", "GLACIER", "GLACIER_IR", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD_IA"]
TypeType = Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"]
S3ServiceName = Literal["s3"]
ServiceName = Literal["accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "amp",
    "amplify",
    "amplifybackend",
    "amplifyuibuilder",
    "apigateway",
    "apigatewaymanagementapi",
    "apigatewayv2",
    "appconfig",
    "appconfigdata",
    "appfabric",
    "appflow",
    "appintegrations",
    "application-autoscaling",
    "application-insights",
    "application-signals",
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "apptest",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "batch",
    "bcm-data-exports",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-runtime",
    "billingconductor",
    "braket",
    "budgets",
    "ce",
    "chatbot",
    "chime",
    "chime-sdk-identity",
    "chime-sdk-media-pipelines",
    "chime-sdk-meetings",
    "chime-sdk-messaging",
    "chime-sdk-voice",
    "cleanrooms",
    "cleanroomsml",
    "cloud9",
    "cloudcontrol",
    "clouddirectory",
    "cloudformation",
    "cloudfront",
    "cloudfront-keyvaluestore",
    "cloudhsm",
    "cloudhsmv2",
    "cloudsearch",
    "cloudsearchdomain",
    "cloudtrail",
    "cloudtrail-data",
    "cloudwatch",
    "codeartifact",
    "codebuild",
    "codecatalyst",
    "codecommit",
    "codeconnections",
    "codedeploy",
    "codeguru-reviewer",
    "codeguru-security",
    "codeguruprofiler",
    "codepipeline",
    "codestar",
    "codestar-connections",
    "codestar-notifications",
    "cognito-identity",
    "cognito-idp",
    "cognito-sync",
    "comprehend",
    "comprehendmedical",
    "compute-optimizer",
    "config",
    "connect",
    "connect-contact-lens",
    "connectcampaigns",
    "connectcases",
    "connectparticipant",
    "controlcatalog",
    "controltower",
    "cost-optimization-hub",
    "cur",
    "customer-profiles",
    "databrew",
    "dataexchange",
    "datapipeline",
    "datasync",
    "datazone",
    "dax",
    "deadline",
    "detective",
    "devicefarm",
    "devops-guru",
    "directconnect",
    "discovery",
    "dlm",
    "dms",
    "docdb",
    "docdb-elastic",
    "drs",
    "ds",
    "dynamodb",
    "dynamodbstreams",
    "ebs",
    "ec2",
    "ec2-instance-connect",
    "ecr",
    "ecr-public",
    "ecs",
    "efs",
    "eks",
    "eks-auth",
    "elastic-inference",
    "elasticache",
    "elasticbeanstalk",
    "elastictranscoder",
    "elb",
    "elbv2",
    "emr",
    "emr-containers",
    "emr-serverless",
    "entityresolution",
    "es",
    "events",
    "evidently",
    "finspace",
    "finspace-data",
    "firehose",
    "fis",
    "fms",
    "forecast",
    "forecastquery",
    "frauddetector",
    "freetier",
    "fsx",
    "gamelift",
    "glacier",
    "globalaccelerator",
    "glue",
    "grafana",
    "greengrass",
    "greengrassv2",
    "groundstation",
    "guardduty",
    "health",
    "healthlake",
    "iam",
    "identitystore",
    "imagebuilder",
    "importexport",
    "inspector",
    "inspector-scan",
    "inspector2",
    "internetmonitor",
    "iot",
    "iot-data",
    "iot-jobs-data",
    "iot1click-devices",
    "iot1click-projects",
    "iotanalytics",
    "iotdeviceadvisor",
    "iotevents",
    "iotevents-data",
    "iotfleethub",
    "iotfleetwise",
    "iotsecuretunneling",
    "iotsitewise",
    "iotthingsgraph",
    "iottwinmaker",
    "iotwireless",
    "ivs",
    "ivs-realtime",
    "ivschat",
    "kafka",
    "kafkaconnect",
    "kendra",
    "kendra-ranking",
    "keyspaces",
    "kinesis",
    "kinesis-video-archived-media",
    "kinesis-video-media",
    "kinesis-video-signaling",
    "kinesis-video-webrtc-storage",
    "kinesisanalytics",
    "kinesisanalyticsv2",
    "kinesisvideo",
    "kms",
    "lakeformation",
    "lambda",
    "launch-wizard",
    "lex-models",
    "lex-runtime",
    "lexv2-models",
    "lexv2-runtime",
    "license-manager",
    "license-manager-linux-subscriptions",
    "license-manager-user-subscriptions",
    "lightsail",
    "location",
    "logs",
    "lookoutequipment",
    "lookoutmetrics",
    "lookoutvision",
    "m2",
    "machinelearning",
    "macie2",
    "mailmanager",
    "managedblockchain",
    "managedblockchain-query",
    "marketplace-agreement",
    "marketplace-catalog",
    "marketplace-deployment",
    "marketplace-entitlement",
    "marketplacecommerceanalytics",
    "mediaconnect",
    "mediaconvert",
    "medialive",
    "mediapackage",
    "mediapackage-vod",
    "mediapackagev2",
    "mediastore",
    "mediastore-data",
    "mediatailor",
    "medical-imaging",
    "memorydb",
    "meteringmarketplace",
    "mgh",
    "mgn",
    "migration-hub-refactor-spaces",
    "migrationhub-config",
    "migrationhuborchestrator",
    "migrationhubstrategy",
    "mobile",
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkmanager",
    "networkmonitor",
    "nimble",
    "oam",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "pca-connector-scep",
    "personalize",
    "personalize-events",
    "personalize-runtime",
    "pi",
    "pinpoint",
    "pinpoint-email",
    "pinpoint-sms-voice",
    "pinpoint-sms-voice-v2",
    "pipes",
    "polly",
    "pricing",
    "privatenetworks",
    "proton",
    "qbusiness",
    "qconnect",
    "qldb",
    "qldb-session",
    "quicksight",
    "ram",
    "rbin",
    "rds",
    "rds-data",
    "redshift",
    "redshift-data",
    "redshift-serverless",
    "rekognition",
    "repostspace",
    "resiliencehub",
    "resource-explorer-2",
    "resource-groups",
    "resourcegroupstaggingapi",
    "robomaker",
    "rolesanywhere",
    "route53",
    "route53-recovery-cluster",
    "route53-recovery-control-config",
    "route53-recovery-readiness",
    "route53domains",
    "route53profiles",
    "route53resolver",
    "rum",
    "s3",
    "s3control",
    "s3outposts",
    "sagemaker",
    "sagemaker-a2i-runtime",
    "sagemaker-edge",
    "sagemaker-featurestore-runtime",
    "sagemaker-geospatial",
    "sagemaker-metrics",
    "sagemaker-runtime",
    "savingsplans",
    "scheduler",
    "schemas",
    "sdb",
    "secretsmanager",
    "securityhub",
    "securitylake",
    "serverlessrepo",
    "service-quotas",
    "servicecatalog",
    "servicecatalog-appregistry",
    "servicediscovery",
    "ses",
    "sesv2",
    "shield",
    "signer",
    "simspaceweaver",
    "sms",
    "sms-voice",
    "snow-device-management",
    "snowball",
    "sns",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-sap",
    "sso",
    "sso-admin",
    "sso-oidc",
    "stepfunctions",
    "storagegateway",
    "sts",
    "supplychain",
    "support",
    "support-app",
    "swf",
    "synthetics",
    "taxsettings",
    "textract",
    "timestream-influxdb",
    "timestream-query",
    "timestream-write",
    "tnb",
    "transcribe",
    "transfer",
    "translate",
    "trustedadvisor",
    "verifiedpermissions",
    "voice-id",
    "vpc-lattice",
    "waf",
    "waf-regional",
    "wafv2",
    "wellarchitected",
    "wisdom",
    "workdocs",
    "worklink",
    "workmail",
    "workmailmessageflow",
    "workspaces",
    "workspaces-thin-client",
    "workspaces-web",
    "xray",]
ResourceServiceName = Literal["cloudformation",
    "cloudwatch",
    "dynamodb",
    "ec2",
    "glacier",
    "iam",
    "opsworks",
    "s3",
    "sns",
    "sqs",]
PaginatorName = Literal["list_directory_buckets",
    "list_multipart_uploads",
    "list_object_versions",
    "list_objects",
    "list_objects_v2",
    "list_parts",]
WaiterName = Literal["bucket_exists", "bucket_not_exists", "object_exists", "object_not_exists"]
RegionName = Literal["af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-southeast-4",
    "ca-central-1",
    "ca-west-1",
    "eu-central-1",
    "eu-central-2",
    "eu-north-1",
    "eu-south-1",
    "eu-south-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "il-central-1",
    "me-central-1",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",]
BlobTypeDef = Union[str, bytes, IO[Any]
FileobjTypeDef = Union[IO[Any]
TimestampTypeDef = Union[datetime, str]
CopySourceOrStrTypeDef = Union[str, 'CopySourceTypeDef']
ObjectLockRetentionUnionTypeDef = Union[   'ObjectLockRetentionTypeDef', 'ObjectLockRetentionOutputTypeDef' ]
OwnershipControlsUnionTypeDef = Union['OwnershipControlsTypeDef', 'OwnershipControlsOutputTypeDef']
ServerSideEncryptionConfigurationUnionTypeDef = Union[   'ServerSideEncryptionConfigurationTypeDef', 'ServerSideEncryptionConfigurationOutputTypeDef' ]
IntelligentTieringConfigurationUnionTypeDef = Union[   'IntelligentTieringConfigurationTypeDef', 'IntelligentTieringConfigurationOutputTypeDef' ]
MetricsConfigurationUnionTypeDef = Union[   'MetricsConfigurationTypeDef', 'MetricsConfigurationOutputTypeDef' ]
AnalyticsConfigurationUnionTypeDef = Union[   'AnalyticsConfigurationTypeDef', 'AnalyticsConfigurationOutputTypeDef' ]
InventoryConfigurationUnionTypeDef = Union[   'InventoryConfigurationTypeDef', 'InventoryConfigurationOutputTypeDef' ]
ReplicationConfigurationUnionTypeDef = Union[   'ReplicationConfigurationTypeDef', 'ReplicationConfigurationOutputTypeDef' ]
