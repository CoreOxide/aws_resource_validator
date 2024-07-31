from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

ActionGroupSignatureType = Literal["AMAZON.CodeInterpreter", "AMAZON.UserInput"]
ActionGroupStateType = Literal["DISABLED", "ENABLED"]
AgentAliasStatusType = Literal["CREATING", "DELETING", "FAILED", "PREPARED", "UPDATING"]
AgentStatusType = Literal["CREATING",
    "DELETING",
    "FAILED",
    "NOT_PREPARED",
    "PREPARED",
    "PREPARING",
    "UPDATING",
    "VERSIONING",]
ChunkingStrategyType = Literal["FIXED_SIZE", "HIERARCHICAL", "NONE", "SEMANTIC"]
ConfluenceAuthTypeType = Literal["BASIC", "OAUTH2_CLIENT_CREDENTIALS"]
ConfluenceHostTypeType = Literal["SAAS"]
CrawlFilterConfigurationTypeType = Literal["PATTERN"]
CreationModeType = Literal["DEFAULT", "OVERRIDDEN"]
CustomControlMethodType = Literal["RETURN_CONTROL"]
DataDeletionPolicyType = Literal["DELETE", "RETAIN"]
DataSourceStatusType = Literal["AVAILABLE", "DELETE_UNSUCCESSFUL", "DELETING"]
DataSourceTypeType = Literal["CONFLUENCE", "S3", "SALESFORCE", "SHAREPOINT", "WEB"]
FlowConnectionTypeType = Literal["Conditional", "Data"]
FlowNodeIODataTypeType = Literal["Array", "Boolean", "Number", "Object", "String"]
FlowNodeTypeType = Literal["Agent",
    "Collector",
    "Condition",
    "Input",
    "Iterator",
    "KnowledgeBase",
    "LambdaFunction",
    "Lex",
    "Output",
    "Prompt",
    "Retrieval",
    "Storage",]
FlowStatusType = Literal["Failed", "NotPrepared", "Prepared", "Preparing"]
FlowValidationSeverityType = Literal["Error", "Warning"]
IngestionJobFilterAttributeType = Literal["STATUS"]
IngestionJobFilterOperatorType = Literal["EQ"]
IngestionJobSortByAttributeType = Literal["STARTED_AT", "STATUS"]
IngestionJobStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS", "STARTING"]
KnowledgeBaseStateType = Literal["DISABLED", "ENABLED"]
KnowledgeBaseStatusType = Literal["ACTIVE", "CREATING", "DELETE_UNSUCCESSFUL", "DELETING", "FAILED", "UPDATING"]
KnowledgeBaseStorageTypeType = Literal["MONGO_DB_ATLAS", "OPENSEARCH_SERVERLESS", "PINECONE", "RDS", "REDIS_ENTERPRISE_CLOUD"]
KnowledgeBaseTypeType = Literal["VECTOR"]
ListAgentActionGroupsPaginatorName = Literal["list_agent_action_groups"]
ListAgentAliasesPaginatorName = Literal["list_agent_aliases"]
ListAgentKnowledgeBasesPaginatorName = Literal["list_agent_knowledge_bases"]
ListAgentVersionsPaginatorName = Literal["list_agent_versions"]
ListAgentsPaginatorName = Literal["list_agents"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListFlowAliasesPaginatorName = Literal["list_flow_aliases"]
ListFlowVersionsPaginatorName = Literal["list_flow_versions"]
ListFlowsPaginatorName = Literal["list_flows"]
ListIngestionJobsPaginatorName = Literal["list_ingestion_jobs"]
ListKnowledgeBasesPaginatorName = Literal["list_knowledge_bases"]
ListPromptsPaginatorName = Literal["list_prompts"]
MemoryTypeType = Literal["SESSION_SUMMARY"]
ParsingStrategyType = Literal["BEDROCK_FOUNDATION_MODEL"]
PromptStateType = Literal["DISABLED", "ENABLED"]
PromptTemplateTypeType = Literal["TEXT"]
PromptTypeType = Literal["KNOWLEDGE_BASE_RESPONSE_GENERATION", "ORCHESTRATION", "POST_PROCESSING", "PRE_PROCESSING"]
SalesforceAuthTypeType = Literal["OAUTH2_CLIENT_CREDENTIALS"]
SharePointAuthTypeType = Literal["OAUTH2_CLIENT_CREDENTIALS"]
SharePointHostTypeType = Literal["ONLINE"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
StepTypeType = Literal["POST_CHUNKING"]
TypeType = Literal["array", "boolean", "integer", "number", "string"]
WebScopeTypeType = Literal["HOST_ONLY", "SUBDOMAINS"]
AgentsforBedrockServiceName = Literal["bedrock-agent"]
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
    "qapps",
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
PaginatorName = Literal["list_agent_action_groups",
    "list_agent_aliases",
    "list_agent_knowledge_bases",
    "list_agent_versions",
    "list_agents",
    "list_data_sources",
    "list_flow_aliases",
    "list_flow_versions",
    "list_flows",
    "list_ingestion_jobs",
    "list_knowledge_bases",
    "list_prompts",]
MemoryConfigurationUnionTypeDef = Union[   'MemoryConfigurationTypeDef', 'MemoryConfigurationOutputTypeDef' ]
FunctionSchemaUnionTypeDef = Union['FunctionSchemaTypeDef', 'FunctionSchemaOutputTypeDef']
PromptOverrideConfigurationUnionTypeDef = Union[   'PromptOverrideConfigurationTypeDef', 'PromptOverrideConfigurationOutputTypeDef' ]
PromptVariantUnionTypeDef = Union['PromptVariantTypeDef', 'PromptVariantOutputTypeDef']
VectorIngestionConfigurationUnionTypeDef = Union[   'VectorIngestionConfigurationTypeDef', 'VectorIngestionConfigurationOutputTypeDef' ]
DataSourceConfigurationUnionTypeDef = Union[   'DataSourceConfigurationTypeDef', 'DataSourceConfigurationOutputTypeDef' ]
FlowDefinitionUnionTypeDef = Union['FlowDefinitionTypeDef', 'FlowDefinitionOutputTypeDef']
