from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AdditionalResultAttributeValueTypeType = Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
AlfrescoEntityType = Literal["blog", "documentLibrary", "wiki"]
AttributeSuggestionsModeType = Literal["ACTIVE", "INACTIVE"]
ConditionOperatorType = Literal["BeginsWith",
    "Contains",
    "Equals",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEquals",
    "LessThan",
    "LessThanOrEquals",
    "NotContains",
    "NotEquals",
    "NotExists",]
ConfluenceAttachmentFieldNameType = Literal["AUTHOR",
    "CONTENT_TYPE",
    "CREATED_DATE",
    "DISPLAY_URL",
    "FILE_SIZE",
    "ITEM_TYPE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",]
ConfluenceAuthenticationTypeType = Literal["HTTP_BASIC", "PAT"]
ConfluenceBlogFieldNameType = Literal["AUTHOR",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "PUBLISH_DATE",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",]
ConfluencePageFieldNameType = Literal["AUTHOR",
    "CONTENT_STATUS",
    "CREATED_DATE",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "MODIFIED_DATE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",]
ConfluenceSpaceFieldNameType = Literal["DISPLAY_URL", "ITEM_TYPE", "SPACE_KEY", "URL"]
ConfluenceVersionType = Literal["CLOUD", "SERVER"]
ContentTypeType = Literal["CSV",
    "HTML",
    "JSON",
    "MD",
    "MS_EXCEL",
    "MS_WORD",
    "PDF",
    "PLAIN_TEXT",
    "PPT",
    "RTF",
    "XML",
    "XSLT",]
DataSourceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
DataSourceSyncJobStatusType = Literal["ABORTED", "FAILED", "INCOMPLETE", "STOPPING", "SUCCEEDED", "SYNCING", "SYNCING_INDEXING"]
DataSourceTypeType = Literal["ALFRESCO",
    "BOX",
    "CONFLUENCE",
    "CUSTOM",
    "DATABASE",
    "FSX",
    "GITHUB",
    "GOOGLEDRIVE",
    "JIRA",
    "ONEDRIVE",
    "QUIP",
    "S3",
    "SALESFORCE",
    "SERVICENOW",
    "SHAREPOINT",
    "SLACK",
    "TEMPLATE",
    "WEBCRAWLER",
    "WORKDOCS",]
DatabaseEngineTypeType = Literal["RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"]
DocumentAttributeValueTypeType = Literal["DATE_VALUE", "LONG_VALUE", "STRING_LIST_VALUE", "STRING_VALUE"]
DocumentStatusType = Literal["FAILED", "INDEXED", "NOT_FOUND", "PROCESSING", "UPDATED", "UPDATE_FAILED"]
EndpointTypeType = Literal["HOME"]
EntityTypeType = Literal["GROUP", "USER"]
ErrorCodeType = Literal["InternalError", "InvalidRequest"]
ExperienceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
FaqFileFormatType = Literal["CSV", "CSV_WITH_HEADER", "JSON"]
FaqStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
FeaturedResultsSetStatusType = Literal["ACTIVE", "INACTIVE"]
FsxFileSystemTypeType = Literal["WINDOWS"]
HighlightTypeType = Literal["STANDARD", "THESAURUS_SYNONYM"]
IndexEditionType = Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"]
IndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "SYSTEM_UPDATING", "UPDATING"]
IntervalType = Literal["ONE_MONTH_AGO", "ONE_WEEK_AGO", "THIS_MONTH", "THIS_WEEK", "TWO_MONTHS_AGO", "TWO_WEEKS_AGO"]
IssueSubEntityType = Literal["ATTACHMENTS", "COMMENTS", "WORKLOGS"]
KeyLocationType = Literal["SECRET_MANAGER", "URL"]
MetricTypeType = Literal["AGG_QUERY_DOC_METRICS",
    "DOCS_BY_CLICK_COUNT",
    "QUERIES_BY_COUNT",
    "QUERIES_BY_ZERO_CLICK_RATE",
    "QUERIES_BY_ZERO_RESULT_RATE",
    "TREND_QUERY_DOC_METRICS",]
MissingAttributeKeyStrategyType = Literal["COLLAPSE", "EXPAND", "IGNORE"]
ModeType = Literal["ENABLED", "LEARN_ONLY"]
OrderType = Literal["ASCENDING", "DESCENDING"]
PersonaType = Literal["OWNER", "VIEWER"]
PrincipalMappingStatusType = Literal["DELETED", "DELETING", "FAILED", "PROCESSING", "SUCCEEDED"]
PrincipalTypeType = Literal["GROUP", "USER"]
QueryIdentifiersEnclosingOptionType = Literal["DOUBLE_QUOTES", "NONE"]
QueryResultFormatType = Literal["TABLE", "TEXT"]
QueryResultTypeType = Literal["ANSWER", "DOCUMENT", "QUESTION_ANSWER"]
QuerySuggestionsBlockListStatusType = Literal["ACTIVE", "ACTIVE_BUT_UPDATE_FAILED", "CREATING", "DELETING", "FAILED", "UPDATING"]
QuerySuggestionsStatusType = Literal["ACTIVE", "UPDATING"]
ReadAccessTypeType = Literal["ALLOW", "DENY"]
RelevanceTypeType = Literal["NOT_RELEVANT", "RELEVANT"]
SalesforceChatterFeedIncludeFilterTypeType = Literal["ACTIVE_USER", "STANDARD_USER"]
SalesforceKnowledgeArticleStateType = Literal["ARCHIVED", "DRAFT", "PUBLISHED"]
SalesforceStandardObjectNameType = Literal["ACCOUNT",
    "CAMPAIGN",
    "CASE",
    "CONTACT",
    "CONTRACT",
    "DOCUMENT",
    "GROUP",
    "IDEA",
    "LEAD",
    "OPPORTUNITY",
    "PARTNER",
    "PRICEBOOK",
    "PRODUCT",
    "PROFILE",
    "SOLUTION",
    "TASK",
    "USER",]
ScoreConfidenceType = Literal["HIGH", "LOW", "MEDIUM", "NOT_AVAILABLE", "VERY_HIGH"]
ServiceNowAuthenticationTypeType = Literal["HTTP_BASIC", "OAUTH2"]
ServiceNowBuildVersionTypeType = Literal["LONDON", "OTHERS"]
SharePointOnlineAuthenticationTypeType = Literal["HTTP_BASIC", "OAUTH2"]
SharePointVersionType = Literal["SHAREPOINT_2013", "SHAREPOINT_2016", "SHAREPOINT_2019", "SHAREPOINT_ONLINE"]
SlackEntityType = Literal["DIRECT_MESSAGE", "GROUP_MESSAGE", "PRIVATE_CHANNEL", "PUBLIC_CHANNEL"]
SortOrderType = Literal["ASC", "DESC"]
SuggestionTypeType = Literal["DOCUMENT_ATTRIBUTES", "QUERY"]
ThesaurusStatusType = Literal["ACTIVE", "ACTIVE_BUT_UPDATE_FAILED", "CREATING", "DELETING", "FAILED", "UPDATING"]
TypeType = Literal["ON_PREMISE", "SAAS"]
UserContextPolicyType = Literal["ATTRIBUTE_FILTER", "USER_TOKEN"]
UserGroupResolutionModeType = Literal["AWS_SSO", "NONE"]
WarningCodeType = Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]
WebCrawlerModeType = Literal["EVERYTHING", "HOST_ONLY", "SUBDOMAINS"]
kendraServiceName = Literal["kendra"]
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
RegionName = Literal["ap-northeast-1",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-west-1",
    "eu-west-2",
    "us-east-1",
    "us-east-2",
    "us-west-2",]
BlobTypeDef = Union[str, bytes, IO[Any]]
TimestampTypeDef = Union[datetime, str]
