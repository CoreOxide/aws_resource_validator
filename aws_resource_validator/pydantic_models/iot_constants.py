from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AbortActionType = Literal["CANCEL"]
ActionTypeType = Literal["CONNECT", "PUBLISH", "RECEIVE", "SUBSCRIBE"]
AggregationTypeNameType = Literal["Cardinality", "Percentiles", "Statistics"]
AlertTargetTypeType = Literal["SNS"]
AuditCheckRunStatusType = Literal["CANCELED",
    "COMPLETED_COMPLIANT",
    "COMPLETED_NON_COMPLIANT",
    "FAILED",
    "IN_PROGRESS",
    "WAITING_FOR_DATA_COLLECTION",]
AuditFindingSeverityType = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]
AuditFrequencyType = Literal["BIWEEKLY", "DAILY", "MONTHLY", "WEEKLY"]
AuditMitigationActionsExecutionStatusType = Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "SKIPPED"]
AuditMitigationActionsTaskStatusType = Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
AuditNotificationTypeType = Literal["SNS"]
AuditTaskStatusType = Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
AuditTaskTypeType = Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"]
AuthDecisionType = Literal["ALLOWED", "EXPLICIT_DENY", "IMPLICIT_DENY"]
AuthorizerStatusType = Literal["ACTIVE", "INACTIVE"]
AutoRegistrationStatusType = Literal["DISABLE", "ENABLE"]
AwsJobAbortCriteriaAbortActionType = Literal["CANCEL"]
AwsJobAbortCriteriaFailureTypeType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
BehaviorCriteriaTypeType = Literal["MACHINE_LEARNING", "STATIC", "STATISTICAL"]
CACertificateStatusType = Literal["ACTIVE", "INACTIVE"]
CACertificateUpdateActionType = Literal["DEACTIVATE"]
CannedAccessControlListType = Literal["authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "log-delivery-write",
    "private",
    "public-read",
    "public-read-write",]
CertificateModeType = Literal["DEFAULT", "SNI_ONLY"]
CertificateProviderOperationType = Literal["CreateCertificateFromCsr"]
CertificateStatusType = Literal["ACTIVE", "INACTIVE", "PENDING_ACTIVATION", "PENDING_TRANSFER", "REGISTER_INACTIVE", "REVOKED"]
ComparisonOperatorType = Literal["greater-than",
    "greater-than-equals",
    "in-cidr-set",
    "in-port-set",
    "in-set",
    "less-than",
    "less-than-equals",
    "not-in-cidr-set",
    "not-in-port-set",
    "not-in-set",]
ConfidenceLevelType = Literal["HIGH", "LOW", "MEDIUM"]
CustomMetricTypeType = Literal["ip-address-list", "number", "number-list", "string-list"]
DayOfWeekType = Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"]
DetectMitigationActionExecutionStatusType = Literal["FAILED", "IN_PROGRESS", "SKIPPED", "SUCCESSFUL"]
DetectMitigationActionsTaskStatusType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCESSFUL"]
DeviceCertificateUpdateActionType = Literal["DEACTIVATE"]
DeviceDefenderIndexingModeType = Literal["OFF", "VIOLATIONS"]
DimensionTypeType = Literal["TOPIC_FILTER"]
DimensionValueOperatorType = Literal["IN", "NOT_IN"]
DomainConfigurationStatusType = Literal["DISABLED", "ENABLED"]
DomainTypeType = Literal["AWS_MANAGED", "CUSTOMER_MANAGED", "ENDPOINT"]
DynamicGroupStatusType = Literal["ACTIVE", "BUILDING", "REBUILDING"]
DynamoKeyTypeType = Literal["NUMBER", "STRING"]
EventTypeType = Literal["CA_CERTIFICATE",
    "CERTIFICATE",
    "JOB",
    "JOB_EXECUTION",
    "POLICY",
    "THING",
    "THING_GROUP",
    "THING_GROUP_HIERARCHY",
    "THING_GROUP_MEMBERSHIP",
    "THING_TYPE",
    "THING_TYPE_ASSOCIATION",]
FieldTypeType = Literal["Boolean", "Number", "String"]
FleetMetricUnitType = Literal["Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",]
GetBehaviorModelTrainingSummariesPaginatorName = Literal["get_behavior_model_training_summaries"]
IndexStatusType = Literal["ACTIVE", "BUILDING", "REBUILDING"]
JobEndBehaviorType = Literal["CANCEL", "FORCE_CANCEL", "STOP_ROLLOUT"]
JobExecutionFailureTypeType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
JobExecutionStatusType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "QUEUED", "REJECTED", "REMOVED", "SUCCEEDED", "TIMED_OUT"]
JobStatusType = Literal["CANCELED", "COMPLETED", "DELETION_IN_PROGRESS", "IN_PROGRESS", "SCHEDULED"]
ListActiveViolationsPaginatorName = Literal["list_active_violations"]
ListAttachedPoliciesPaginatorName = Literal["list_attached_policies"]
ListAuditFindingsPaginatorName = Literal["list_audit_findings"]
ListAuditMitigationActionsExecutionsPaginatorName = Literal["list_audit_mitigation_actions_executions"]
ListAuditMitigationActionsTasksPaginatorName = Literal["list_audit_mitigation_actions_tasks"]
ListAuditSuppressionsPaginatorName = Literal["list_audit_suppressions"]
ListAuditTasksPaginatorName = Literal["list_audit_tasks"]
ListAuthorizersPaginatorName = Literal["list_authorizers"]
ListBillingGroupsPaginatorName = Literal["list_billing_groups"]
ListCACertificatesPaginatorName = Literal["list_ca_certificates"]
ListCertificatesByCAPaginatorName = Literal["list_certificates_by_ca"]
ListCertificatesPaginatorName = Literal["list_certificates"]
ListCustomMetricsPaginatorName = Literal["list_custom_metrics"]
ListDetectMitigationActionsExecutionsPaginatorName = Literal["list_detect_mitigation_actions_executions"]
ListDetectMitigationActionsTasksPaginatorName = Literal["list_detect_mitigation_actions_tasks"]
ListDimensionsPaginatorName = Literal["list_dimensions"]
ListDomainConfigurationsPaginatorName = Literal["list_domain_configurations"]
ListFleetMetricsPaginatorName = Literal["list_fleet_metrics"]
ListIndicesPaginatorName = Literal["list_indices"]
ListJobExecutionsForJobPaginatorName = Literal["list_job_executions_for_job"]
ListJobExecutionsForThingPaginatorName = Literal["list_job_executions_for_thing"]
ListJobTemplatesPaginatorName = Literal["list_job_templates"]
ListJobsPaginatorName = Literal["list_jobs"]
ListManagedJobTemplatesPaginatorName = Literal["list_managed_job_templates"]
ListMetricValuesPaginatorName = Literal["list_metric_values"]
ListMitigationActionsPaginatorName = Literal["list_mitigation_actions"]
ListOTAUpdatesPaginatorName = Literal["list_ota_updates"]
ListOutgoingCertificatesPaginatorName = Literal["list_outgoing_certificates"]
ListPackageVersionsPaginatorName = Literal["list_package_versions"]
ListPackagesPaginatorName = Literal["list_packages"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListPolicyPrincipalsPaginatorName = Literal["list_policy_principals"]
ListPrincipalPoliciesPaginatorName = Literal["list_principal_policies"]
ListPrincipalThingsPaginatorName = Literal["list_principal_things"]
ListProvisioningTemplateVersionsPaginatorName = Literal["list_provisioning_template_versions"]
ListProvisioningTemplatesPaginatorName = Literal["list_provisioning_templates"]
ListRelatedResourcesForAuditFindingPaginatorName = Literal["list_related_resources_for_audit_finding"]
ListRoleAliasesPaginatorName = Literal["list_role_aliases"]
ListScheduledAuditsPaginatorName = Literal["list_scheduled_audits"]
ListSecurityProfilesForTargetPaginatorName = Literal["list_security_profiles_for_target"]
ListSecurityProfilesPaginatorName = Literal["list_security_profiles"]
ListStreamsPaginatorName = Literal["list_streams"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTargetsForPolicyPaginatorName = Literal["list_targets_for_policy"]
ListTargetsForSecurityProfilePaginatorName = Literal["list_targets_for_security_profile"]
ListThingGroupsForThingPaginatorName = Literal["list_thing_groups_for_thing"]
ListThingGroupsPaginatorName = Literal["list_thing_groups"]
ListThingPrincipalsPaginatorName = Literal["list_thing_principals"]
ListThingRegistrationTaskReportsPaginatorName = Literal["list_thing_registration_task_reports"]
ListThingRegistrationTasksPaginatorName = Literal["list_thing_registration_tasks"]
ListThingTypesPaginatorName = Literal["list_thing_types"]
ListThingsInBillingGroupPaginatorName = Literal["list_things_in_billing_group"]
ListThingsInThingGroupPaginatorName = Literal["list_things_in_thing_group"]
ListThingsPaginatorName = Literal["list_things"]
ListTopicRuleDestinationsPaginatorName = Literal["list_topic_rule_destinations"]
ListTopicRulesPaginatorName = Literal["list_topic_rules"]
ListV2LoggingLevelsPaginatorName = Literal["list_v2_logging_levels"]
ListViolationEventsPaginatorName = Literal["list_violation_events"]
LogLevelType = Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"]
LogTargetTypeType = Literal["CLIENT_ID", "DEFAULT", "PRINCIPAL_ID", "SOURCE_IP", "THING_GROUP"]
MessageFormatType = Literal["JSON", "RAW"]
MitigationActionTypeType = Literal["ADD_THINGS_TO_THING_GROUP",
    "ENABLE_IOT_LOGGING",
    "PUBLISH_FINDING_TO_SNS",
    "REPLACE_DEFAULT_POLICY_VERSION",
    "UPDATE_CA_CERTIFICATE",
    "UPDATE_DEVICE_CERTIFICATE",]
ModelStatusType = Literal["ACTIVE", "EXPIRED", "PENDING_BUILD"]
NamedShadowIndexingModeType = Literal["OFF", "ON"]
OTAUpdateStatusType = Literal["CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_PENDING",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",]
PackageVersionActionType = Literal["DEPRECATE", "PUBLISH"]
PackageVersionStatusType = Literal["DEPRECATED", "DRAFT", "PUBLISHED"]
PolicyTemplateNameType = Literal["BLANK_POLICY"]
ProtocolType = Literal["HTTP", "MQTT"]
ReportTypeType = Literal["ERRORS", "RESULTS"]
ResourceTypeType = Literal["ACCOUNT_SETTINGS",
    "CA_CERTIFICATE",
    "CLIENT_ID",
    "COGNITO_IDENTITY_POOL",
    "DEVICE_CERTIFICATE",
    "IAM_ROLE",
    "IOT_POLICY",
    "ISSUER_CERTIFICATE",
    "ROLE_ALIAS",]
RetryableFailureTypeType = Literal["ALL", "FAILED", "TIMED_OUT"]
ServerCertificateStatusType = Literal["INVALID", "VALID"]
ServiceTypeType = Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"]
StatusType = Literal["Cancelled", "Cancelling", "Completed", "Failed", "InProgress"]
TargetFieldOrderType = Literal["LatLon", "LonLat"]
TargetSelectionType = Literal["CONTINUOUS", "SNAPSHOT"]
TemplateTypeType = Literal["FLEET_PROVISIONING", "JITP"]
ThingConnectivityIndexingModeType = Literal["OFF", "STATUS"]
ThingGroupIndexingModeType = Literal["OFF", "ON"]
ThingIndexingModeType = Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"]
TopicRuleDestinationStatusType = Literal["DELETING", "DISABLED", "ENABLED", "ERROR", "IN_PROGRESS"]
VerificationStateType = Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
ViolationEventTypeType = Literal["alarm-cleared", "alarm-invalidated", "in-alarm"]
IoTServiceName = Literal["iot"]
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
PaginatorName = Literal["get_behavior_model_training_summaries",
    "list_active_violations",
    "list_attached_policies",
    "list_audit_findings",
    "list_audit_mitigation_actions_executions",
    "list_audit_mitigation_actions_tasks",
    "list_audit_suppressions",
    "list_audit_tasks",
    "list_authorizers",
    "list_billing_groups",
    "list_ca_certificates",
    "list_certificates",
    "list_certificates_by_ca",
    "list_custom_metrics",
    "list_detect_mitigation_actions_executions",
    "list_detect_mitigation_actions_tasks",
    "list_dimensions",
    "list_domain_configurations",
    "list_fleet_metrics",
    "list_indices",
    "list_job_executions_for_job",
    "list_job_executions_for_thing",
    "list_job_templates",
    "list_jobs",
    "list_managed_job_templates",
    "list_metric_values",
    "list_mitigation_actions",
    "list_ota_updates",
    "list_outgoing_certificates",
    "list_package_versions",
    "list_packages",
    "list_policies",
    "list_policy_principals",
    "list_principal_policies",
    "list_principal_things",
    "list_provisioning_template_versions",
    "list_provisioning_templates",
    "list_related_resources_for_audit_finding",
    "list_role_aliases",
    "list_scheduled_audits",
    "list_security_profiles",
    "list_security_profiles_for_target",
    "list_streams",
    "list_tags_for_resource",
    "list_targets_for_policy",
    "list_targets_for_security_profile",
    "list_thing_groups",
    "list_thing_groups_for_thing",
    "list_thing_principals",
    "list_thing_registration_task_reports",
    "list_thing_registration_tasks",
    "list_thing_types",
    "list_things",
    "list_things_in_billing_group",
    "list_things_in_thing_group",
    "list_topic_rule_destinations",
    "list_topic_rules",
    "list_v2_logging_levels",
    "list_violation_events",]
RegionName = Literal["ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-central-1",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",]
BlobTypeDef = Union[str, bytes, IO[Any]
TimestampTypeDef = Union[datetime, str]
