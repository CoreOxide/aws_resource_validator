from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AdditionalOptionKeysType = Literal["observations.scope", "performanceTuning.caching"]
AggFunctionType = Literal["avg",
    "count",
    "countDistinct",
    "first",
    "kurtosis",
    "last",
    "max",
    "min",
    "skewness",
    "stddev_pop",
    "stddev_samp",
    "sum",
    "sumDistinct",
    "var_pop",
    "var_samp",]
AuthenticationTypeType = Literal["BASIC", "CUSTOM", "OAUTH2"]
BackfillErrorCodeType = Literal["ENCRYPTED_PARTITION_ERROR",
    "INTERNAL_ERROR",
    "INVALID_PARTITION_TYPE_DATA_ERROR",
    "MISSING_PARTITION_VALUE_ERROR",
    "UNSUPPORTED_PARTITION_CHARACTER_ERROR",]
BlueprintRunStateType = Literal["FAILED", "ROLLING_BACK", "RUNNING", "SUCCEEDED"]
BlueprintStatusType = Literal["ACTIVE", "CREATING", "FAILED", "UPDATING"]
CatalogEncryptionModeType = Literal["DISABLED", "SSE-KMS", "SSE-KMS-WITH-SERVICE-ROLE"]
CloudWatchEncryptionModeType = Literal["DISABLED", "SSE-KMS"]
ColumnStatisticsStateType = Literal["FAILED", "RUNNING", "STARTING", "STOPPED", "SUCCEEDED"]
ColumnStatisticsTypeType = Literal["BINARY", "BOOLEAN", "DATE", "DECIMAL", "DOUBLE", "LONG", "STRING"]
ComparatorType = Literal["EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "LESS_THAN", "LESS_THAN_EQUALS"]
CompatibilityType = Literal["BACKWARD", "BACKWARD_ALL", "DISABLED", "FORWARD", "FORWARD_ALL", "FULL", "FULL_ALL", "NONE"]
CompressionTypeType = Literal["bzip2", "gzip"]
ConnectionPropertyKeyType = Literal["CONFIG_FILES",
    "CONNECTION_URL",
    "CONNECTOR_CLASS_NAME",
    "CONNECTOR_TYPE",
    "CONNECTOR_URL",
    "CUSTOM_JDBC_CERT",
    "CUSTOM_JDBC_CERT_STRING",
    "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
    "ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD",
    "ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD",
    "ENCRYPTED_PASSWORD",
    "HOST",
    "INSTANCE_ID",
    "JDBC_CONNECTION_URL",
    "JDBC_DRIVER_CLASS_NAME",
    "JDBC_DRIVER_JAR_URI",
    "JDBC_ENFORCE_SSL",
    "JDBC_ENGINE",
    "JDBC_ENGINE_VERSION",
    "KAFKA_BOOTSTRAP_SERVERS",
    "KAFKA_CLIENT_KEYSTORE",
    "KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "KAFKA_CLIENT_KEY_PASSWORD",
    "KAFKA_CUSTOM_CERT",
    "KAFKA_SASL_GSSAPI_KEYTAB",
    "KAFKA_SASL_GSSAPI_KRB5_CONF",
    "KAFKA_SASL_GSSAPI_PRINCIPAL",
    "KAFKA_SASL_GSSAPI_SERVICE",
    "KAFKA_SASL_MECHANISM",
    "KAFKA_SASL_PLAIN_PASSWORD",
    "KAFKA_SASL_PLAIN_USERNAME",
    "KAFKA_SASL_SCRAM_PASSWORD",
    "KAFKA_SASL_SCRAM_SECRETS_ARN",
    "KAFKA_SASL_SCRAM_USERNAME",
    "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
    "KAFKA_SSL_ENABLED",
    "PASSWORD",
    "PORT",
    "ROLE_ARN",
    "SECRET_ID",
    "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
    "USERNAME",]
ConnectionStatusType = Literal["FAILED", "IN_PROGRESS", "READY"]
ConnectionTypeType = Literal["CUSTOM", "JDBC", "KAFKA", "MARKETPLACE", "MONGODB", "NETWORK", "SALESFORCE", "SFTP"]
CrawlStateType = Literal["CANCELLED", "CANCELLING", "ERROR", "FAILED", "RUNNING", "SUCCEEDED"]
CrawlerHistoryStateType = Literal["COMPLETED", "FAILED", "RUNNING", "STOPPED"]
CrawlerLineageSettingsType = Literal["DISABLE", "ENABLE"]
CrawlerStateType = Literal["READY", "RUNNING", "STOPPING"]
CsvHeaderOptionType = Literal["ABSENT", "PRESENT", "UNKNOWN"]
CsvSerdeOptionType = Literal["LazySimpleSerDe", "None", "OpenCSVSerDe"]
DQCompositeRuleEvaluationMethodType = Literal["COLUMN", "ROW"]
DQStopJobOnFailureTimingType = Literal["AfterDataLoad", "Immediate"]
DQTransformOutputType = Literal["EvaluationResults", "PrimaryInput"]
DataFormatType = Literal["AVRO", "JSON", "PROTOBUF"]
DataQualityRuleResultStatusType = Literal["ERROR", "FAIL", "PASS"]
DatabaseAttributesType = Literal["NAME"]
DeleteBehaviorType = Literal["DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE", "LOG"]
DeltaTargetCompressionTypeType = Literal["snappy", "uncompressed"]
EnableHybridValuesType = Literal["FALSE", "TRUE"]
ExecutionClassType = Literal["FLEX", "STANDARD"]
ExistConditionType = Literal["MUST_EXIST", "NONE", "NOT_EXIST"]
FieldNameType = Literal["CRAWL_ID", "DPU_HOUR", "END_TIME", "START_TIME", "STATE"]
FilterLogicalOperatorType = Literal["AND", "OR"]
FilterOperationType = Literal["EQ", "GT", "GTE", "ISNULL", "LT", "LTE", "REGEX"]
FilterOperatorType = Literal["EQ", "GE", "GT", "LE", "LT", "NE"]
FilterValueTypeType = Literal["COLUMNEXTRACTED", "CONSTANT"]
GetClassifiersPaginatorName = Literal["get_classifiers"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCrawlerMetricsPaginatorName = Literal["get_crawler_metrics"]
GetCrawlersPaginatorName = Literal["get_crawlers"]
GetDatabasesPaginatorName = Literal["get_databases"]
GetDevEndpointsPaginatorName = Literal["get_dev_endpoints"]
GetJobRunsPaginatorName = Literal["get_job_runs"]
GetJobsPaginatorName = Literal["get_jobs"]
GetPartitionIndexesPaginatorName = Literal["get_partition_indexes"]
GetPartitionsPaginatorName = Literal["get_partitions"]
GetResourcePoliciesPaginatorName = Literal["get_resource_policies"]
GetSecurityConfigurationsPaginatorName = Literal["get_security_configurations"]
GetTableVersionsPaginatorName = Literal["get_table_versions"]
GetTablesPaginatorName = Literal["get_tables"]
GetTriggersPaginatorName = Literal["get_triggers"]
GetUserDefinedFunctionsPaginatorName = Literal["get_user_defined_functions"]
GetWorkflowRunsPaginatorName = Literal["get_workflow_runs"]
GlueRecordTypeType = Literal["BIGDECIMAL", "BYTE", "DATE", "DOUBLE", "FLOAT", "INT", "LONG", "SHORT", "STRING", "TIMESTAMP"]
HudiTargetCompressionTypeType = Literal["gzip", "lzo", "snappy", "uncompressed"]
JDBCConnectionTypeType = Literal["mysql", "oracle", "postgresql", "redshift", "sqlserver"]
JDBCDataTypeType = Literal["ARRAY",
    "BIGINT",
    "BINARY",
    "BIT",
    "BLOB",
    "BOOLEAN",
    "CHAR",
    "CLOB",
    "DATALINK",
    "DATE",
    "DECIMAL",
    "DISTINCT",
    "DOUBLE",
    "FLOAT",
    "INTEGER",
    "JAVA_OBJECT",
    "LONGNVARCHAR",
    "LONGVARBINARY",
    "LONGVARCHAR",
    "NCHAR",
    "NCLOB",
    "NULL",
    "NUMERIC",
    "NVARCHAR",
    "OTHER",
    "REAL",
    "REF",
    "REF_CURSOR",
    "ROWID",
    "SMALLINT",
    "SQLXML",
    "STRUCT",
    "TIME",
    "TIMESTAMP",
    "TIMESTAMP_WITH_TIMEZONE",
    "TIME_WITH_TIMEZONE",
    "TINYINT",
    "VARBINARY",
    "VARCHAR",]
JdbcMetadataEntryType = Literal["COMMENTS", "RAWTYPES"]
JobBookmarksEncryptionModeType = Literal["CSE-KMS", "DISABLED"]
JobModeType = Literal["NOTEBOOK", "SCRIPT", "VISUAL"]
JobRunStateType = Literal["ERROR",
    "EXPIRED",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "SUCCEEDED",
    "TIMEOUT",
    "WAITING",]
JoinTypeType = Literal["equijoin", "left", "leftanti", "leftsemi", "outer", "right"]
LanguageType = Literal["PYTHON", "SCALA"]
LastCrawlStatusType = Literal["CANCELLED", "FAILED", "SUCCEEDED"]
ListBlueprintsPaginatorName = Literal["list_blueprints"]
ListJobsPaginatorName = Literal["list_jobs"]
ListRegistriesPaginatorName = Literal["list_registries"]
ListSchemaVersionsPaginatorName = Literal["list_schema_versions"]
ListSchemasPaginatorName = Literal["list_schemas"]
ListTriggersPaginatorName = Literal["list_triggers"]
ListUsageProfilesPaginatorName = Literal["list_usage_profiles"]
ListWorkflowsPaginatorName = Literal["list_workflows"]
LogicalOperatorType = Literal["EQUALS"]
LogicalType = Literal["AND", "ANY"]
MLUserDataEncryptionModeStringType = Literal["DISABLED", "SSE-KMS"]
MetadataOperationType = Literal["CREATE"]
NodeTypeType = Literal["CRAWLER", "JOB", "TRIGGER"]
OAuth2GrantTypeType = Literal["AUTHORIZATION_CODE", "CLIENT_CREDENTIALS", "JWT_BEARER"]
ParamTypeType = Literal["bool", "complex", "float", "int", "list", "null", "str"]
ParquetCompressionTypeType = Literal["gzip", "lzo", "none", "snappy", "uncompressed"]
PartitionIndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
PermissionType = Literal["ALL",
    "ALTER",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "DELETE",
    "DROP",
    "INSERT",
    "SELECT",]
PermissionTypeType = Literal["CELL_FILTER_PERMISSION", "COLUMN_PERMISSION", "NESTED_CELL_PERMISSION", "NESTED_PERMISSION"]
PiiTypeType = Literal["ColumnAudit", "ColumnMasking", "RowAudit", "RowMasking"]
PrincipalTypeType = Literal["GROUP", "ROLE", "USER"]
QuoteCharType = Literal["disabled", "quillemet", "quote", "single_quote"]
RecrawlBehaviorType = Literal["CRAWL_EVENT_MODE", "CRAWL_EVERYTHING", "CRAWL_NEW_FOLDERS_ONLY"]
RegistryStatusType = Literal["AVAILABLE", "DELETING"]
ResourceShareTypeType = Literal["ALL", "FEDERATED", "FOREIGN"]
ResourceTypeType = Literal["ARCHIVE", "FILE", "JAR"]
S3EncryptionModeType = Literal["DISABLED", "SSE-KMS", "SSE-S3"]
ScheduleStateType = Literal["NOT_SCHEDULED", "SCHEDULED", "TRANSITIONING"]
SchemaDiffTypeType = Literal["SYNTAX_DIFF"]
SchemaStatusType = Literal["AVAILABLE", "DELETING", "PENDING"]
SchemaVersionStatusType = Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"]
SeparatorType = Literal["comma", "ctrla", "pipe", "semicolon", "tab"]
SessionStatusType = Literal["FAILED", "PROVISIONING", "READY", "STOPPED", "STOPPING", "TIMEOUT"]
SortDirectionTypeType = Literal["ASCENDING", "DESCENDING"]
SortType = Literal["ASC", "DESC"]
SourceControlAuthStrategyType = Literal["AWS_SECRETS_MANAGER", "PERSONAL_ACCESS_TOKEN"]
SourceControlProviderType = Literal["AWS_CODE_COMMIT", "BITBUCKET", "GITHUB", "GITLAB"]
StartingPositionType = Literal["earliest", "latest", "timestamp", "trim_horizon"]
StatementStateType = Literal["AVAILABLE", "CANCELLED", "CANCELLING", "ERROR", "RUNNING", "WAITING"]
TableOptimizerEventTypeType = Literal["completed", "failed", "in_progress", "starting"]
TableOptimizerTypeType = Literal["compaction"]
TargetFormatType = Literal["avro", "csv", "delta", "hudi", "json", "orc", "parquet"]
TaskRunSortColumnTypeType = Literal["STARTED", "STATUS", "TASK_RUN_TYPE"]
TaskStatusTypeType = Literal["FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"]
TaskTypeType = Literal["EVALUATION", "EXPORT_LABELS", "FIND_MATCHES", "IMPORT_LABELS", "LABELING_SET_GENERATION"]
TransformSortColumnTypeType = Literal["CREATED", "LAST_MODIFIED", "NAME", "STATUS", "TRANSFORM_TYPE"]
TransformStatusTypeType = Literal["DELETING", "NOT_READY", "READY"]
TransformTypeType = Literal["FIND_MATCHES"]
TriggerStateType = Literal["ACTIVATED",
    "ACTIVATING",
    "CREATED",
    "CREATING",
    "DEACTIVATED",
    "DEACTIVATING",
    "DELETING",
    "UPDATING",]
TriggerTypeType = Literal["CONDITIONAL", "EVENT", "ON_DEMAND", "SCHEDULED"]
UnionTypeType = Literal["ALL", "DISTINCT"]
UpdateBehaviorType = Literal["LOG", "UPDATE_IN_DATABASE"]
UpdateCatalogBehaviorType = Literal["LOG", "UPDATE_IN_DATABASE"]
ViewDialectType = Literal["ATHENA", "REDSHIFT", "SPARK"]
ViewUpdateActionType = Literal["ADD", "ADD_OR_REPLACE", "DROP", "REPLACE"]
WorkerTypeType = Literal["G.025X", "G.1X", "G.2X", "G.4X", "G.8X", "Standard", "Z.2X"]
WorkflowRunStatusType = Literal["COMPLETED", "ERROR", "RUNNING", "STOPPED", "STOPPING"]
GlueServiceName = Literal["glue"]
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
PaginatorName = Literal["get_classifiers",
    "get_connections",
    "get_crawler_metrics",
    "get_crawlers",
    "get_databases",
    "get_dev_endpoints",
    "get_job_runs",
    "get_jobs",
    "get_partition_indexes",
    "get_partitions",
    "get_resource_policies",
    "get_security_configurations",
    "get_table_versions",
    "get_tables",
    "get_triggers",
    "get_user_defined_functions",
    "get_workflow_runs",
    "list_blueprints",
    "list_jobs",
    "list_registries",
    "list_schema_versions",
    "list_schemas",
    "list_triggers",
    "list_usage_profiles",
    "list_workflows",]
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
ConnectionsListUnionTypeDef = Union['ConnectionsListTypeDef', 'ConnectionsListExtraOutputTypeDef']
GlueTableUnionTypeDef = Union['GlueTableTypeDef', 'GlueTableOutputTypeDef']
PartitionValueListUnionTypeDef = Union[   'PartitionValueListTypeDef', 'PartitionValueListExtraOutputTypeDef' ]
ActionUnionTypeDef = Union['ActionTypeDef', 'ActionExtraOutputTypeDef']
CodeGenNodeUnionTypeDef = Union['CodeGenNodeTypeDef', 'CodeGenNodeOutputTypeDef']
PredicateUnionTypeDef = Union['PredicateTypeDef', 'PredicateExtraOutputTypeDef']
ProfileConfigurationUnionTypeDef = Union[   'ProfileConfigurationTypeDef', 'ProfileConfigurationOutputTypeDef' ]
CrawlerTargetsUnionTypeDef = Union['CrawlerTargetsTypeDef', 'CrawlerTargetsExtraOutputTypeDef']
DataSourceUnionTypeDef = Union['DataSourceTypeDef', 'DataSourceOutputTypeDef']
EncryptionConfigurationUnionTypeDef = Union[   'EncryptionConfigurationTypeDef', 'EncryptionConfigurationExtraOutputTypeDef' ]
CodeGenConfigurationNodeUnionTypeDef = Union[   'CodeGenConfigurationNodeTypeDef', 'CodeGenConfigurationNodeExtraOutputTypeDef' ]
ColumnStatisticsUnionTypeDef = Union['ColumnStatisticsTypeDef', 'ColumnStatisticsOutputTypeDef']
