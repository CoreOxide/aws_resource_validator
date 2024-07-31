from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AccountRoleStatusType = Literal["CREATING", "DELETED", "DELETING", "PENDING_DELETION", "READY"]
CustomerPolicyScopeIdTypeType = Literal["ACCOUNT", "ORG_UNIT"]
CustomerPolicyStatusType = Literal["ACTIVE", "OUT_OF_ADMIN_SCOPE"]
DependentServiceNameType = Literal["AWSCONFIG", "AWSSHIELD_ADVANCED", "AWSVPC", "AWSWAF"]
DestinationTypeType = Literal["IPV4", "IPV6", "PREFIX_LIST"]
EntryTypeType = Literal["CUSTOM_ENTRY", "FMS_MANAGED_FIRST_ENTRY", "FMS_MANAGED_LAST_ENTRY"]
EntryViolationReasonType = Literal["ENTRY_CONFLICT", "INCORRECT_ENTRY_ORDER", "MISSING_EXPECTED_ENTRY"]
FailedItemReasonType = Literal["NOT_VALID_ACCOUNT_ID",
    "NOT_VALID_ARN",
    "NOT_VALID_PARTITION",
    "NOT_VALID_REGION",
    "NOT_VALID_RESOURCE_TYPE",
    "NOT_VALID_SERVICE",]
FirewallDeploymentModelType = Literal["CENTRALIZED", "DISTRIBUTED"]
ListAdminAccountsForOrganizationPaginatorName = Literal["list_admin_accounts_for_organization"]
ListAdminsManagingAccountPaginatorName = Literal["list_admins_managing_account"]
ListAppsListsPaginatorName = Literal["list_apps_lists"]
ListComplianceStatusPaginatorName = Literal["list_compliance_status"]
ListMemberAccountsPaginatorName = Literal["list_member_accounts"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListProtocolsListsPaginatorName = Literal["list_protocols_lists"]
ListThirdPartyFirewallFirewallPoliciesPaginatorName = Literal["list_third_party_firewall_firewall_policies"]
MarketplaceSubscriptionOnboardingStatusType = Literal["COMPLETE", "NOT_COMPLETE", "NO_SUBSCRIPTION"]
NetworkAclRuleActionType = Literal["allow", "deny"]
NetworkFirewallOverrideActionType = Literal["DROP_TO_ALERT"]
OrganizationStatusType = Literal["OFFBOARDING", "OFFBOARDING_COMPLETE", "ONBOARDING", "ONBOARDING_COMPLETE"]
PolicyComplianceStatusTypeType = Literal["COMPLIANT", "NON_COMPLIANT"]
RemediationActionTypeType = Literal["MODIFY", "REMOVE"]
ResourceSetStatusType = Literal["ACTIVE", "OUT_OF_ADMIN_SCOPE"]
RuleOrderType = Literal["DEFAULT_ACTION_ORDER", "STRICT_ORDER"]
SecurityServiceTypeType = Literal["DNS_FIREWALL",
    "IMPORT_NETWORK_FIREWALL",
    "NETWORK_ACL_COMMON",
    "NETWORK_FIREWALL",
    "SECURITY_GROUPS_COMMON",
    "SECURITY_GROUPS_CONTENT_AUDIT",
    "SECURITY_GROUPS_USAGE_AUDIT",
    "SHIELD_ADVANCED",
    "THIRD_PARTY_FIREWALL",
    "WAF",
    "WAFV2",]
StreamExceptionPolicyType = Literal["CONTINUE", "DROP", "FMS_IGNORE", "REJECT"]
TargetTypeType = Literal["CARRIER_GATEWAY",
    "EGRESS_ONLY_INTERNET_GATEWAY",
    "GATEWAY",
    "INSTANCE",
    "LOCAL_GATEWAY",
    "NAT_GATEWAY",
    "NETWORK_INTERFACE",
    "TRANSIT_GATEWAY",
    "VPC_ENDPOINT",
    "VPC_PEERING_CONNECTION",]
ThirdPartyFirewallAssociationStatusType = Literal["NOT_EXIST", "OFFBOARDING", "OFFBOARD_COMPLETE", "ONBOARDING", "ONBOARD_COMPLETE"]
ThirdPartyFirewallType = Literal["FORTIGATE_CLOUD_NATIVE_FIREWALL", "PALO_ALTO_NETWORKS_CLOUD_NGFW"]
ViolationReasonType = Literal["BLACK_HOLE_ROUTE_DETECTED",
    "BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET",
    "FIREWALL_SUBNET_IS_OUT_OF_SCOPE",
    "FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE",
    "FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT",
    "FMS_CREATED_SECURITY_GROUP_EDITED",
    "INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE",
    "INTERNET_TRAFFIC_NOT_INSPECTED",
    "INVALID_NETWORK_ACL_ENTRY",
    "INVALID_ROUTE_CONFIGURATION",
    "MISSING_EXPECTED_ROUTE_TABLE",
    "MISSING_FIREWALL",
    "MISSING_FIREWALL_SUBNET_IN_AZ",
    "MISSING_TARGET_GATEWAY",
    "NETWORK_FIREWALL_POLICY_MODIFIED",
    "RESOURCE_INCORRECT_WEB_ACL",
    "RESOURCE_MISSING_DNS_FIREWALL",
    "RESOURCE_MISSING_SECURITY_GROUP",
    "RESOURCE_MISSING_SHIELD_PROTECTION",
    "RESOURCE_MISSING_WEB_ACL",
    "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
    "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
    "ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT",
    "SECURITY_GROUP_REDUNDANT",
    "SECURITY_GROUP_UNUSED",
    "TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY",
    "UNEXPECTED_FIREWALL_ROUTES",
    "UNEXPECTED_TARGET_GATEWAY_ROUTES",
    "WEB_ACL_MISSING_RULE_GROUP",]
FMSServiceName = Literal["fms"]
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
PaginatorName = Literal["list_admin_accounts_for_organization",
    "list_admins_managing_account",
    "list_apps_lists",
    "list_compliance_status",
    "list_member_accounts",
    "list_policies",
    "list_protocols_lists",
    "list_third_party_firewall_firewall_policies",]
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
TimestampTypeDef = Union[datetime, str]
AdminScopeUnionTypeDef = Union['AdminScopeTypeDef', 'AdminScopeOutputTypeDef']
AppsListDataUnionTypeDef = Union['AppsListDataTypeDef', 'AppsListDataOutputTypeDef']
ProtocolsListDataUnionTypeDef = Union['ProtocolsListDataTypeDef', 'ProtocolsListDataOutputTypeDef']
ResourceSetUnionTypeDef = Union['ResourceSetTypeDef', 'ResourceSetOutputTypeDef']
PolicyUnionTypeDef = Union['PolicyTypeDef', 'PolicyOutputTypeDef']
