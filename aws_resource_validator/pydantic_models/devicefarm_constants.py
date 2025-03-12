from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

ArtifactCategoryType = Literal["FILE", "LOG", "SCREENSHOT"]
ArtifactTypeType = Literal["APPIUM_JAVA_OUTPUT",
    "APPIUM_JAVA_XML_OUTPUT",
    "APPIUM_PYTHON_OUTPUT",
    "APPIUM_PYTHON_XML_OUTPUT",
    "APPIUM_SERVER_OUTPUT",
    "APPLICATION_CRASH_REPORT",
    "AUTOMATION_OUTPUT",
    "CALABASH_JAVA_XML_OUTPUT",
    "CALABASH_JSON_OUTPUT",
    "CALABASH_PRETTY_OUTPUT",
    "CALABASH_STANDARD_OUTPUT",
    "CUSTOMER_ARTIFACT",
    "CUSTOMER_ARTIFACT_LOG",
    "DEVICE_LOG",
    "EXERCISER_MONKEY_OUTPUT",
    "EXPLORER_EVENT_LOG",
    "EXPLORER_SUMMARY_LOG",
    "INSTRUMENTATION_OUTPUT",
    "MESSAGE_LOG",
    "RESULT_LOG",
    "SCREENSHOT",
    "SERVICE_LOG",
    "TESTSPEC_OUTPUT",
    "UNKNOWN",
    "VIDEO",
    "VIDEO_LOG",
    "WEBKIT_LOG",
    "XCTEST_LOG",]
BillingMethodType = Literal["METERED", "UNMETERED"]
CurrencyCodeType = Literal["USD"]
DeviceAttributeType = Literal["APPIUM_VERSION",
    "ARN",
    "AVAILABILITY",
    "FLEET_TYPE",
    "FORM_FACTOR",
    "INSTANCE_ARN",
    "INSTANCE_LABELS",
    "MANUFACTURER",
    "MODEL",
    "OS_VERSION",
    "PLATFORM",
    "REMOTE_ACCESS_ENABLED",
    "REMOTE_DEBUG_ENABLED",]
DeviceAvailabilityType = Literal["AVAILABLE", "BUSY", "HIGHLY_AVAILABLE", "TEMPORARY_NOT_AVAILABLE"]
DeviceFilterAttributeType = Literal["ARN",
    "AVAILABILITY",
    "FLEET_TYPE",
    "FORM_FACTOR",
    "INSTANCE_ARN",
    "INSTANCE_LABELS",
    "MANUFACTURER",
    "MODEL",
    "OS_VERSION",
    "PLATFORM",
    "REMOTE_ACCESS_ENABLED",
    "REMOTE_DEBUG_ENABLED",]
DeviceFormFactorType = Literal["PHONE", "TABLET"]
DevicePlatformType = Literal["ANDROID", "IOS"]
DevicePoolTypeType = Literal["CURATED", "PRIVATE"]
ExecutionResultCodeType = Literal["PARSING_FAILED", "VPC_ENDPOINT_SETUP_FAILED"]
ExecutionResultType = Literal["ERRORED", "FAILED", "PASSED", "PENDING", "SKIPPED", "STOPPED", "WARNED"]
ExecutionStatusType = Literal["COMPLETED",
    "PENDING",
    "PENDING_CONCURRENCY",
    "PENDING_DEVICE",
    "PREPARING",
    "PROCESSING",
    "RUNNING",
    "SCHEDULING",
    "STOPPING",]
GetOfferingStatusPaginatorName = Literal["get_offering_status"]
InstanceStatusType = Literal["AVAILABLE", "IN_USE", "NOT_AVAILABLE", "PREPARING"]
InteractionModeType = Literal["INTERACTIVE", "NO_VIDEO", "VIDEO_ONLY"]
ListArtifactsPaginatorName = Literal["list_artifacts"]
ListDeviceInstancesPaginatorName = Literal["list_device_instances"]
ListDevicePoolsPaginatorName = Literal["list_device_pools"]
ListDevicesPaginatorName = Literal["list_devices"]
ListInstanceProfilesPaginatorName = Literal["list_instance_profiles"]
ListJobsPaginatorName = Literal["list_jobs"]
ListNetworkProfilesPaginatorName = Literal["list_network_profiles"]
ListOfferingPromotionsPaginatorName = Literal["list_offering_promotions"]
ListOfferingTransactionsPaginatorName = Literal["list_offering_transactions"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListProjectsPaginatorName = Literal["list_projects"]
ListRemoteAccessSessionsPaginatorName = Literal["list_remote_access_sessions"]
ListRunsPaginatorName = Literal["list_runs"]
ListSamplesPaginatorName = Literal["list_samples"]
ListSuitesPaginatorName = Literal["list_suites"]
ListTestsPaginatorName = Literal["list_tests"]
ListUniqueProblemsPaginatorName = Literal["list_unique_problems"]
ListUploadsPaginatorName = Literal["list_uploads"]
ListVPCEConfigurationsPaginatorName = Literal["list_vpce_configurations"]
NetworkProfileTypeType = Literal["CURATED", "PRIVATE"]
OfferingTransactionTypeType = Literal["PURCHASE", "RENEW", "SYSTEM"]
OfferingTypeType = Literal["RECURRING"]
RecurringChargeFrequencyType = Literal["MONTHLY"]
RuleOperatorType = Literal["CONTAINS",
    "EQUALS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUALS",
    "IN",
    "LESS_THAN",
    "LESS_THAN_OR_EQUALS",
    "NOT_IN",]
SampleTypeType = Literal["CPU",
    "MEMORY",
    "NATIVE_AVG_DRAWTIME",
    "NATIVE_FPS",
    "NATIVE_FRAMES",
    "NATIVE_MAX_DRAWTIME",
    "NATIVE_MIN_DRAWTIME",
    "OPENGL_AVG_DRAWTIME",
    "OPENGL_FPS",
    "OPENGL_FRAMES",
    "OPENGL_MAX_DRAWTIME",
    "OPENGL_MIN_DRAWTIME",
    "RX",
    "RX_RATE",
    "THREADS",
    "TX",
    "TX_RATE",]
TestGridSessionArtifactCategoryType = Literal["LOG", "VIDEO"]
TestGridSessionArtifactTypeType = Literal["SELENIUM_LOG", "UNKNOWN", "VIDEO"]
TestGridSessionStatusType = Literal["ACTIVE", "CLOSED", "ERRORED"]
TestTypeType = Literal["APPIUM_JAVA_JUNIT",
    "APPIUM_JAVA_TESTNG",
    "APPIUM_NODE",
    "APPIUM_PYTHON",
    "APPIUM_RUBY",
    "APPIUM_WEB_JAVA_JUNIT",
    "APPIUM_WEB_JAVA_TESTNG",
    "APPIUM_WEB_NODE",
    "APPIUM_WEB_PYTHON",
    "APPIUM_WEB_RUBY",
    "BUILTIN_FUZZ",
    "INSTRUMENTATION",
    "XCTEST",
    "XCTEST_UI",]
UploadCategoryType = Literal["CURATED", "PRIVATE"]
UploadStatusType = Literal["FAILED", "INITIALIZED", "PROCESSING", "SUCCEEDED"]
UploadTypeType = Literal["ANDROID_APP",
    "APPIUM_JAVA_JUNIT_TEST_PACKAGE",
    "APPIUM_JAVA_JUNIT_TEST_SPEC",
    "APPIUM_JAVA_TESTNG_TEST_PACKAGE",
    "APPIUM_JAVA_TESTNG_TEST_SPEC",
    "APPIUM_NODE_TEST_PACKAGE",
    "APPIUM_NODE_TEST_SPEC",
    "APPIUM_PYTHON_TEST_PACKAGE",
    "APPIUM_PYTHON_TEST_SPEC",
    "APPIUM_RUBY_TEST_PACKAGE",
    "APPIUM_RUBY_TEST_SPEC",
    "APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE",
    "APPIUM_WEB_JAVA_JUNIT_TEST_SPEC",
    "APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE",
    "APPIUM_WEB_JAVA_TESTNG_TEST_SPEC",
    "APPIUM_WEB_NODE_TEST_PACKAGE",
    "APPIUM_WEB_NODE_TEST_SPEC",
    "APPIUM_WEB_PYTHON_TEST_PACKAGE",
    "APPIUM_WEB_PYTHON_TEST_SPEC",
    "APPIUM_WEB_RUBY_TEST_PACKAGE",
    "APPIUM_WEB_RUBY_TEST_SPEC",
    "CALABASH_TEST_PACKAGE",
    "EXTERNAL_DATA",
    "INSTRUMENTATION_TEST_PACKAGE",
    "INSTRUMENTATION_TEST_SPEC",
    "IOS_APP",
    "UIAUTOMATION_TEST_PACKAGE",
    "UIAUTOMATOR_TEST_PACKAGE",
    "WEB_APP",
    "XCTEST_TEST_PACKAGE",
    "XCTEST_UI_TEST_PACKAGE",
    "XCTEST_UI_TEST_SPEC",]
DeviceFarmServiceName = Literal["devicefarm"]
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
    "backupsearch",
    "batch",
    "bcm-data-exports",
    "bcm-pricing-calculator",
    "bedrock",
    "bedrock-agent",
    "bedrock-agent-runtime",
    "bedrock-data-automation",
    "bedrock-data-automation-runtime",
    "bedrock-runtime",
    "billing",
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
    "connectcampaignsv2",
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
    "ds-data",
    "dsql",
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
    "geo-maps",
    "geo-places",
    "geo-routes",
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
    "invoicing",
    "iot",
    "iot-data",
    "iot-jobs-data",
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
    "marketplace-reporting",
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
    "mq",
    "mturk",
    "mwaa",
    "neptune",
    "neptune-graph",
    "neptunedata",
    "network-firewall",
    "networkflowmonitor",
    "networkmanager",
    "networkmonitor",
    "notifications",
    "notificationscontacts",
    "oam",
    "observabilityadmin",
    "omics",
    "opensearch",
    "opensearchserverless",
    "opsworks",
    "opsworkscm",
    "organizations",
    "osis",
    "outposts",
    "panorama",
    "partnercentral-selling",
    "payment-cryptography",
    "payment-cryptography-data",
    "pca-connector-ad",
    "pca-connector-scep",
    "pcs",
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
    "s3tables",
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
    "security-ir",
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
    "socialmessaging",
    "sqs",
    "ssm",
    "ssm-contacts",
    "ssm-incidents",
    "ssm-quicksetup",
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
PaginatorName = Literal["get_offering_status",
    "list_artifacts",
    "list_device_instances",
    "list_device_pools",
    "list_devices",
    "list_instance_profiles",
    "list_jobs",
    "list_network_profiles",
    "list_offering_promotions",
    "list_offering_transactions",
    "list_offerings",
    "list_projects",
    "list_remote_access_sessions",
    "list_runs",
    "list_samples",
    "list_suites",
    "list_tests",
    "list_unique_problems",
    "list_uploads",
    "list_vpce_configurations",]
RegionName = Literal["us-west-2"]
