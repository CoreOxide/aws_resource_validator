from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AgentStatusType = Literal["OFFLINE", "ONLINE"]
AtimeType = Literal["BEST_EFFORT", "NONE"]
AzureAccessTierType = Literal["ARCHIVE", "COOL", "HOT"]
AzureBlobAuthenticationTypeType = Literal["SAS"]
AzureBlobTypeType = Literal["BLOCK"]
DescribeStorageSystemResourceMetricsPaginatorName = Literal["describe_storage_system_resource_metrics"]
DiscoveryJobStatusType = Literal["COMPLETED", "COMPLETED_WITH_ISSUES", "FAILED", "RUNNING", "STOPPED", "TERMINATED", "WARNING"]
DiscoveryResourceFilterType = Literal["SVM"]
DiscoveryResourceTypeType = Literal["CLUSTER", "SVM", "VOLUME"]
DiscoverySystemTypeType = Literal["NetAppONTAP"]
EfsInTransitEncryptionType = Literal["NONE", "TLS1_2"]
EndpointTypeType = Literal["FIPS", "PRIVATE_LINK", "PUBLIC"]
FilterTypeType = Literal["SIMPLE_PATTERN"]
GidType = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
HdfsAuthenticationTypeType = Literal["KERBEROS", "SIMPLE"]
HdfsDataTransferProtectionType = Literal["AUTHENTICATION", "DISABLED", "INTEGRITY", "PRIVACY"]
HdfsRpcProtectionType = Literal["AUTHENTICATION", "DISABLED", "INTEGRITY", "PRIVACY"]
ListAgentsPaginatorName = Literal["list_agents"]
ListDiscoveryJobsPaginatorName = Literal["list_discovery_jobs"]
ListLocationsPaginatorName = Literal["list_locations"]
ListStorageSystemsPaginatorName = Literal["list_storage_systems"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTaskExecutionsPaginatorName = Literal["list_task_executions"]
ListTasksPaginatorName = Literal["list_tasks"]
LocationFilterNameType = Literal["CreationTime", "LocationType", "LocationUri"]
LogLevelType = Literal["BASIC", "OFF", "TRANSFER"]
ManifestActionType = Literal["TRANSFER"]
ManifestFormatType = Literal["CSV"]
MtimeType = Literal["NONE", "PRESERVE"]
NfsVersionType = Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]
ObjectStorageServerProtocolType = Literal["HTTP", "HTTPS"]
ObjectTagsType = Literal["NONE", "PRESERVE"]
ObjectVersionIdsType = Literal["INCLUDE", "NONE"]
OperatorType = Literal["BeginsWith",
    "Contains",
    "Equals",
    "GreaterThan",
    "GreaterThanOrEqual",
    "In",
    "LessThan",
    "LessThanOrEqual",
    "NotContains",
    "NotEquals",]
OverwriteModeType = Literal["ALWAYS", "NEVER"]
PhaseStatusType = Literal["ERROR", "PENDING", "SUCCESS"]
PosixPermissionsType = Literal["NONE", "PRESERVE"]
PreserveDeletedFilesType = Literal["PRESERVE", "REMOVE"]
PreserveDevicesType = Literal["NONE", "PRESERVE"]
RecommendationStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "NONE"]
ReportLevelType = Literal["ERRORS_ONLY", "SUCCESSES_AND_ERRORS"]
ReportOutputTypeType = Literal["STANDARD", "SUMMARY_ONLY"]
S3StorageClassType = Literal["DEEP_ARCHIVE",
    "GLACIER",
    "GLACIER_INSTANT_RETRIEVAL",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "STANDARD",
    "STANDARD_IA",]
ScheduleDisabledByType = Literal["SERVICE", "USER"]
ScheduleStatusType = Literal["DISABLED", "ENABLED"]
SmbSecurityDescriptorCopyFlagsType = Literal["NONE", "OWNER_DACL", "OWNER_DACL_SACL"]
SmbVersionType = Literal["AUTOMATIC", "SMB1", "SMB2", "SMB2_0", "SMB3"]
StorageSystemConnectivityStatusType = Literal["FAIL", "PASS", "UNKNOWN"]
TaskExecutionStatusType = Literal["CANCELLING",
    "ERROR",
    "LAUNCHING",
    "PREPARING",
    "QUEUED",
    "SUCCESS",
    "TRANSFERRING",
    "VERIFYING",]
TaskFilterNameType = Literal["CreationTime", "LocationId"]
TaskQueueingType = Literal["DISABLED", "ENABLED"]
TaskStatusType = Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"]
TransferModeType = Literal["ALL", "CHANGED"]
UidType = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
VerifyModeType = Literal["NONE", "ONLY_FILES_TRANSFERRED", "POINT_IN_TIME_CONSISTENT"]
DataSyncServiceName = Literal["datasync"]
ServiceName = Literal["accessanalyzer",
    "account",
    "acm",
    "acm-pca",
    "alexaforbusiness",
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
    "applicationcostprofiler",
    "appmesh",
    "apprunner",
    "appstream",
    "appsync",
    "arc-zonal-shift",
    "artifact",
    "athena",
    "auditmanager",
    "autoscaling",
    "autoscaling-plans",
    "b2bi",
    "backup",
    "backup-gateway",
    "backupstorage",
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
    "honeycode",
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
PaginatorName = Literal["describe_storage_system_resource_metrics",
    "list_agents",
    "list_discovery_jobs",
    "list_locations",
    "list_storage_systems",
    "list_tags_for_resource",
    "list_task_executions",
    "list_tasks",]
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
TimestampTypeDef = Union[datetime, str]
Ec2ConfigUnionTypeDef = Union['Ec2ConfigTypeDef', 'Ec2ConfigOutputTypeDef']
OnPremConfigUnionTypeDef = Union['OnPremConfigTypeDef', 'OnPremConfigOutputTypeDef']
