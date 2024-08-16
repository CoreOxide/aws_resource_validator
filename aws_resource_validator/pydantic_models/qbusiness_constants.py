from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

APISchemaTypeType = Literal["OPEN_API_V3"]
ActionPayloadFieldTypeType = Literal["ARRAY", "BOOLEAN", "NUMBER", "STRING"]
ApplicationStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
AttachmentStatusType = Literal["FAILED", "SUCCEEDED"]
AttachmentsControlModeType = Literal["DISABLED", "ENABLED"]
AttributeTypeType = Literal["DATE", "NUMBER", "STRING", "STRING_LIST"]
AttributeValueOperatorType = Literal["DELETE"]
ChatModeType = Literal["CREATOR_MODE", "PLUGIN_MODE", "RETRIEVAL_MODE"]
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
CreatorModeControlType = Literal["DISABLED", "ENABLED"]
DataSourceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PENDING_CREATION", "UPDATING"]
DataSourceSyncJobStatusType = Literal["ABORTED", "FAILED", "INCOMPLETE", "STOPPING", "SUCCEEDED", "SYNCING", "SYNCING_INDEXING"]
DocumentAttributeBoostingLevelType = Literal["HIGH", "LOW", "MEDIUM", "NONE", "VERY_HIGH"]
DocumentContentOperatorType = Literal["DELETE"]
DocumentEnrichmentConditionOperatorType = Literal["BEGINS_WITH",
    "CONTAINS",
    "EQUALS",
    "EXISTS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
    "NOT_CONTAINS",
    "NOT_EQUALS",
    "NOT_EXISTS",]
DocumentStatusType = Literal["DELETED",
    "DELETING",
    "DOCUMENT_FAILED_TO_INDEX",
    "FAILED",
    "INDEXED",
    "PROCESSING",
    "RECEIVED",
    "UPDATED",]
ErrorCodeType = Literal["InternalError", "InvalidRequest", "ResourceInactive", "ResourceNotFound"]
GetChatControlsConfigurationPaginatorName = Literal["get_chat_controls_configuration"]
GroupStatusType = Literal["DELETED", "DELETING", "FAILED", "PROCESSING", "SUCCEEDED"]
IndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
IndexTypeType = Literal["ENTERPRISE", "STARTER"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListConversationsPaginatorName = Literal["list_conversations"]
ListDataSourceSyncJobsPaginatorName = Literal["list_data_source_sync_jobs"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListDocumentsPaginatorName = Literal["list_documents"]
ListGroupsPaginatorName = Literal["list_groups"]
ListIndicesPaginatorName = Literal["list_indices"]
ListMessagesPaginatorName = Literal["list_messages"]
ListPluginsPaginatorName = Literal["list_plugins"]
ListRetrieversPaginatorName = Literal["list_retrievers"]
ListWebExperiencesPaginatorName = Literal["list_web_experiences"]
MemberRelationType = Literal["AND", "OR"]
MembershipTypeType = Literal["DATASOURCE", "INDEX"]
MessageTypeType = Literal["SYSTEM", "USER"]
MessageUsefulnessReasonType = Literal["COMPLETE",
    "FACTUALLY_CORRECT",
    "HARMFUL_OR_UNSAFE",
    "HELPFUL",
    "INCORRECT_OR_MISSING_SOURCES",
    "NOT_BASED_ON_DOCUMENTS",
    "NOT_COMPLETE",
    "NOT_CONCISE",
    "NOT_FACTUALLY_CORRECT",
    "NOT_HELPFUL",
    "OTHER",
    "RELEVANT_SOURCES",]
MessageUsefulnessType = Literal["NOT_USEFUL", "USEFUL"]
NumberAttributeBoostingTypeType = Literal["PRIORITIZE_LARGER_VALUES", "PRIORITIZE_SMALLER_VALUES"]
PersonalizationControlModeType = Literal["DISABLED", "ENABLED"]
PluginBuildStatusType = Literal["CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",]
PluginStateType = Literal["DISABLED", "ENABLED"]
PluginTypeType = Literal["CUSTOM", "JIRA", "SALESFORCE", "SERVICE_NOW", "ZENDESK"]
QAppsControlModeType = Literal["DISABLED", "ENABLED"]
ReadAccessTypeType = Literal["ALLOW", "DENY"]
ResponseScopeType = Literal["ENTERPRISE_CONTENT_ONLY", "EXTENDED_KNOWLEDGE_ENABLED"]
RetrieverStatusType = Literal["ACTIVE", "CREATING", "FAILED"]
RetrieverTypeType = Literal["KENDRA_INDEX", "NATIVE_INDEX"]
RuleTypeType = Literal["CONTENT_BLOCKER_RULE", "CONTENT_RETRIEVAL_RULE"]
StatusType = Literal["DISABLED", "ENABLED"]
StringAttributeValueBoostingLevelType = Literal["HIGH", "LOW", "MEDIUM", "VERY_HIGH"]
WebExperienceSamplePromptsControlModeType = Literal["DISABLED", "ENABLED"]
WebExperienceStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PENDING_AUTH_CONFIG"]
QBusinessServiceName = Literal["qbusiness"]
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
PaginatorName = Literal["get_chat_controls_configuration",
    "list_applications",
    "list_conversations",
    "list_data_source_sync_jobs",
    "list_data_sources",
    "list_documents",
    "list_groups",
    "list_indices",
    "list_messages",
    "list_plugins",
    "list_retrievers",
    "list_web_experiences",]
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
BlobTypeDef = Union[str, bytes, IO[Any]]
TimestampTypeDef = Union[datetime, str]
DataSourceVpcConfigurationUnionTypeDef = Union[   'DataSourceVpcConfigurationTypeDef', 'DataSourceVpcConfigurationOutputTypeDef' ]
ActionExecutionUnionTypeDef = Union['ActionExecutionTypeDef', 'ActionExecutionExtraOutputTypeDef']
PluginAuthConfigurationUnionTypeDef = Union[   'PluginAuthConfigurationTypeDef', 'PluginAuthConfigurationOutputTypeDef' ]
RetrieverConfigurationUnionTypeDef = Union[   'RetrieverConfigurationTypeDef', 'RetrieverConfigurationOutputTypeDef' ]
TopicConfigurationUnionTypeDef = Union[   'TopicConfigurationTypeDef', 'TopicConfigurationExtraOutputTypeDef' ]
DocumentEnrichmentConfigurationUnionTypeDef = Union[   'DocumentEnrichmentConfigurationTypeDef', 'DocumentEnrichmentConfigurationOutputTypeDef' ]
