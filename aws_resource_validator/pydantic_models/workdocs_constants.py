from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

ActivityTypeType = Literal["DOCUMENT_ANNOTATION_ADDED",
    "DOCUMENT_ANNOTATION_DELETED",
    "DOCUMENT_CHECKED_IN",
    "DOCUMENT_CHECKED_OUT",
    "DOCUMENT_COMMENT_ADDED",
    "DOCUMENT_COMMENT_DELETED",
    "DOCUMENT_MOVED",
    "DOCUMENT_RECYCLED",
    "DOCUMENT_RENAMED",
    "DOCUMENT_RESTORED",
    "DOCUMENT_REVERTED",
    "DOCUMENT_SHAREABLE_LINK_CREATED",
    "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
    "DOCUMENT_SHAREABLE_LINK_REMOVED",
    "DOCUMENT_SHARED",
    "DOCUMENT_SHARE_PERMISSION_CHANGED",
    "DOCUMENT_UNSHARED",
    "DOCUMENT_VERSION_DELETED",
    "DOCUMENT_VERSION_DOWNLOADED",
    "DOCUMENT_VERSION_UPLOADED",
    "DOCUMENT_VERSION_VIEWED",
    "FOLDER_CREATED",
    "FOLDER_DELETED",
    "FOLDER_MOVED",
    "FOLDER_RECYCLED",
    "FOLDER_RENAMED",
    "FOLDER_RESTORED",
    "FOLDER_SHAREABLE_LINK_CREATED",
    "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
    "FOLDER_SHAREABLE_LINK_REMOVED",
    "FOLDER_SHARED",
    "FOLDER_SHARE_PERMISSION_CHANGED",
    "FOLDER_UNSHARED",]
AdditionalResponseFieldTypeType = Literal["WEBURL"]
BooleanEnumTypeType = Literal["FALSE", "TRUE"]
CommentStatusTypeType = Literal["DELETED", "DRAFT", "PUBLISHED"]
CommentVisibilityTypeType = Literal["PRIVATE", "PUBLIC"]
ContentCategoryTypeType = Literal["AUDIO",
    "DOCUMENT",
    "IMAGE",
    "OTHER",
    "PDF",
    "PRESENTATION",
    "SOURCE_CODE",
    "SPREADSHEET",
    "VIDEO",]
DescribeActivitiesPaginatorName = Literal["describe_activities"]
DescribeCommentsPaginatorName = Literal["describe_comments"]
DescribeDocumentVersionsPaginatorName = Literal["describe_document_versions"]
DescribeFolderContentsPaginatorName = Literal["describe_folder_contents"]
DescribeGroupsPaginatorName = Literal["describe_groups"]
DescribeNotificationSubscriptionsPaginatorName = Literal["describe_notification_subscriptions"]
DescribeResourcePermissionsPaginatorName = Literal["describe_resource_permissions"]
DescribeRootFoldersPaginatorName = Literal["describe_root_folders"]
DescribeUsersPaginatorName = Literal["describe_users"]
DocumentSourceTypeType = Literal["ORIGINAL", "WITH_COMMENTS"]
DocumentStatusTypeType = Literal["ACTIVE", "INITIALIZED"]
DocumentThumbnailTypeType = Literal["LARGE", "SMALL", "SMALL_HQ"]
DocumentVersionStatusType = Literal["ACTIVE"]
FolderContentTypeType = Literal["ALL", "DOCUMENT", "FOLDER"]
LanguageCodeTypeType = Literal["AR",
    "BG",
    "BN",
    "CS",
    "DA",
    "DE",
    "DEFAULT",
    "EL",
    "EN",
    "ES",
    "FA",
    "FI",
    "FR",
    "HI",
    "HU",
    "ID",
    "IT",
    "JA",
    "KO",
    "LT",
    "LV",
    "NL",
    "NO",
    "PT",
    "RO",
    "RU",
    "SV",
    "SW",
    "TH",
    "TR",
    "ZH",]
LocaleTypeType = Literal["de", "default", "en", "es", "fr", "ja", "ko", "pt_BR", "ru", "zh_CN", "zh_TW"]
OrderByFieldTypeType = Literal["CREATED_TIMESTAMP", "MODIFIED_TIMESTAMP", "NAME", "RELEVANCE", "SIZE"]
OrderTypeType = Literal["ASCENDING", "DESCENDING"]
PrincipalRoleTypeType = Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"]
PrincipalTypeType = Literal["ANONYMOUS", "GROUP", "INVITE", "ORGANIZATION", "USER"]
ResourceCollectionTypeType = Literal["SHARED_WITH_ME"]
ResourceSortTypeType = Literal["DATE", "NAME"]
ResourceStateTypeType = Literal["ACTIVE", "RECYCLED", "RECYCLING", "RESTORING"]
ResourceTypeType = Literal["DOCUMENT", "FOLDER"]
ResponseItemTypeType = Literal["COMMENT", "DOCUMENT", "DOCUMENT_VERSION", "FOLDER"]
RolePermissionTypeType = Literal["DIRECT", "INHERITED"]
RoleTypeType = Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"]
SearchCollectionTypeType = Literal["OWNED", "SHARED_WITH_ME"]
SearchQueryScopeTypeType = Literal["CONTENT", "NAME"]
SearchResourceTypeType = Literal["COMMENT", "DOCUMENT", "DOCUMENT_VERSION", "FOLDER"]
SearchResourcesPaginatorName = Literal["search_resources"]
ShareStatusTypeType = Literal["FAILURE", "SUCCESS"]
SortOrderType = Literal["ASC", "DESC"]
StorageTypeType = Literal["QUOTA", "UNLIMITED"]
SubscriptionProtocolTypeType = Literal["HTTPS", "SQS"]
SubscriptionTypeType = Literal["ALL"]
UserFilterTypeType = Literal["ACTIVE_PENDING", "ALL"]
UserSortTypeType = Literal["FULL_NAME", "STORAGE_LIMIT", "STORAGE_USED", "USER_NAME", "USER_STATUS"]
UserStatusTypeType = Literal["ACTIVE", "INACTIVE", "PENDING"]
UserTypeType = Literal["ADMIN", "MINIMALUSER", "POWERUSER", "USER", "WORKSPACESUSER"]
WorkDocsServiceName = Literal["workdocs"]
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
    "iot-roborunner",
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
    "neptunedata",
    "network-firewall",
    "networkmanager",
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
    "support",
    "support-app",
    "swf",
    "synthetics",
    "textract",
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
PaginatorName = Literal["describe_activities",
    "describe_comments",
    "describe_document_versions",
    "describe_folder_contents",
    "describe_groups",
    "describe_notification_subscriptions",
    "describe_resource_permissions",
    "describe_root_folders",
    "describe_users",
    "search_resources",]
RegionName = Literal["ap-northeast-1", "ap-southeast-1", "ap-southeast-2", "eu-west-1", "us-east-1", "us-west-2"]
TimestampTypeDef = Union[datetime, str]
