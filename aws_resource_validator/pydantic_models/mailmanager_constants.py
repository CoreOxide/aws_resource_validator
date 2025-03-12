from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AcceptActionType = Literal["ALLOW", "DENY"]
ActionFailurePolicyType = Literal["CONTINUE", "DROP"]
ArchiveBooleanEmailAttributeType = Literal["HAS_ATTACHMENTS"]
ArchiveBooleanOperatorType = Literal["IS_FALSE", "IS_TRUE"]
ArchiveStateType = Literal["ACTIVE", "PENDING_DELETION"]
ArchiveStringEmailAttributeType = Literal["CC", "ENVELOPE_FROM", "ENVELOPE_TO", "FROM", "SUBJECT", "TO"]
ArchiveStringOperatorType = Literal["CONTAINS"]
ExportStateType = Literal["CANCELLED", "COMPLETED", "FAILED", "PREPROCESSING", "PROCESSING", "QUEUED"]
ImportDataTypeType = Literal["CSV", "JSON"]
ImportJobStatusType = Literal["COMPLETED", "CREATED", "FAILED", "PROCESSING", "STOPPED"]
IngressAddressListEmailAttributeType = Literal["RECIPIENT"]
IngressBooleanOperatorType = Literal["IS_FALSE", "IS_TRUE"]
IngressIpOperatorType = Literal["CIDR_MATCHES", "NOT_CIDR_MATCHES"]
IngressIpv4AttributeType = Literal["SENDER_IP"]
IngressPointStatusToUpdateType = Literal["ACTIVE", "CLOSED"]
IngressPointStatusType = Literal["ACTIVE", "CLOSED", "DEPROVISIONING", "FAILED", "PROVISIONING", "UPDATING"]
IngressPointTypeType = Literal["AUTH", "OPEN"]
IngressStringEmailAttributeType = Literal["RECIPIENT"]
IngressStringOperatorType = Literal["CONTAINS", "ENDS_WITH", "EQUALS", "NOT_EQUALS", "STARTS_WITH"]
IngressTlsAttributeType = Literal["TLS_PROTOCOL"]
IngressTlsProtocolAttributeType = Literal["TLS1_2", "TLS1_3"]
IngressTlsProtocolOperatorType = Literal["IS", "MINIMUM_TLS_VERSION"]
ListAddonInstancesPaginatorName = Literal["list_addon_instances"]
ListAddonSubscriptionsPaginatorName = Literal["list_addon_subscriptions"]
ListAddressListImportJobsPaginatorName = Literal["list_address_list_import_jobs"]
ListAddressListsPaginatorName = Literal["list_address_lists"]
ListArchiveExportsPaginatorName = Literal["list_archive_exports"]
ListArchiveSearchesPaginatorName = Literal["list_archive_searches"]
ListArchivesPaginatorName = Literal["list_archives"]
ListIngressPointsPaginatorName = Literal["list_ingress_points"]
ListMembersOfAddressListPaginatorName = Literal["list_members_of_address_list"]
ListRelaysPaginatorName = Literal["list_relays"]
ListRuleSetsPaginatorName = Literal["list_rule_sets"]
ListTrafficPoliciesPaginatorName = Literal["list_traffic_policies"]
MailFromType = Literal["PRESERVE", "REPLACE"]
RetentionPeriodType = Literal["EIGHTEEN_MONTHS",
    "EIGHT_YEARS",
    "FIVE_YEARS",
    "FOUR_YEARS",
    "NINE_MONTHS",
    "NINE_YEARS",
    "ONE_YEAR",
    "PERMANENT",
    "SEVEN_YEARS",
    "SIX_MONTHS",
    "SIX_YEARS",
    "TEN_YEARS",
    "THIRTY_MONTHS",
    "THREE_MONTHS",
    "THREE_YEARS",
    "TWO_YEARS",]
RuleAddressListEmailAttributeType = Literal["CC", "FROM", "MAIL_FROM", "RECIPIENT", "SENDER", "TO"]
RuleBooleanEmailAttributeType = Literal["READ_RECEIPT_REQUESTED", "TLS", "TLS_WRAPPED"]
RuleBooleanOperatorType = Literal["IS_FALSE", "IS_TRUE"]
RuleDmarcOperatorType = Literal["EQUALS", "NOT_EQUALS"]
RuleDmarcPolicyType = Literal["NONE", "QUARANTINE", "REJECT"]
RuleIpEmailAttributeType = Literal["SOURCE_IP"]
RuleIpOperatorType = Literal["CIDR_MATCHES", "NOT_CIDR_MATCHES"]
RuleNumberEmailAttributeType = Literal["MESSAGE_SIZE"]
RuleNumberOperatorType = Literal["EQUALS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
    "NOT_EQUALS",]
RuleStringEmailAttributeType = Literal["CC", "FROM", "HELO", "MAIL_FROM", "RECIPIENT", "SENDER", "SUBJECT", "TO"]
RuleStringOperatorType = Literal["CONTAINS", "ENDS_WITH", "EQUALS", "NOT_EQUALS", "STARTS_WITH"]
RuleVerdictAttributeType = Literal["DKIM", "SPF"]
RuleVerdictOperatorType = Literal["EQUALS", "NOT_EQUALS"]
RuleVerdictType = Literal["FAIL", "GRAY", "PASS", "PROCESSING_FAILED"]
SearchStateType = Literal["CANCELLED", "COMPLETED", "FAILED", "QUEUED", "RUNNING"]
MailManagerServiceName = Literal["mailmanager"]
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
PaginatorName = Literal["list_addon_instances",
    "list_addon_subscriptions",
    "list_address_list_import_jobs",
    "list_address_lists",
    "list_archive_exports",
    "list_archive_searches",
    "list_archives",
    "list_ingress_points",
    "list_members_of_address_list",
    "list_relays",
    "list_rule_sets",
    "list_traffic_policies",]
