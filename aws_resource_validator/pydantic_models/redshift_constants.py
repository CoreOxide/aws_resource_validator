from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

ActionTypeType = Literal["recommend-node-config", "resize-cluster", "restore-cluster"]
AquaConfigurationStatusType = Literal["auto", "disabled", "enabled"]
AquaStatusType = Literal["applying", "disabled", "enabled"]
AuthorizationStatusType = Literal["Authorized", "Revoking"]
ClusterAvailableWaiterName = Literal["cluster_available"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ClusterRestoredWaiterName = Literal["cluster_restored"]
DataShareStatusForConsumerType = Literal["ACTIVE", "AVAILABLE"]
DataShareStatusForProducerType = Literal["ACTIVE", "AUTHORIZED", "DEAUTHORIZED", "PENDING_AUTHORIZATION", "REJECTED"]
DataShareStatusType = Literal["ACTIVE", "AUTHORIZED", "AVAILABLE", "DEAUTHORIZED", "PENDING_AUTHORIZATION", "REJECTED"]
DescribeClusterDbRevisionsPaginatorName = Literal["describe_cluster_db_revisions"]
DescribeClusterParameterGroupsPaginatorName = Literal["describe_cluster_parameter_groups"]
DescribeClusterParametersPaginatorName = Literal["describe_cluster_parameters"]
DescribeClusterSecurityGroupsPaginatorName = Literal["describe_cluster_security_groups"]
DescribeClusterSnapshotsPaginatorName = Literal["describe_cluster_snapshots"]
DescribeClusterSubnetGroupsPaginatorName = Literal["describe_cluster_subnet_groups"]
DescribeClusterTracksPaginatorName = Literal["describe_cluster_tracks"]
DescribeClusterVersionsPaginatorName = Literal["describe_cluster_versions"]
DescribeClustersPaginatorName = Literal["describe_clusters"]
DescribeCustomDomainAssociationsPaginatorName = Literal["describe_custom_domain_associations"]
DescribeDataSharesForConsumerPaginatorName = Literal["describe_data_shares_for_consumer"]
DescribeDataSharesForProducerPaginatorName = Literal["describe_data_shares_for_producer"]
DescribeDataSharesPaginatorName = Literal["describe_data_shares"]
DescribeDefaultClusterParametersPaginatorName = Literal["describe_default_cluster_parameters"]
DescribeEndpointAccessPaginatorName = Literal["describe_endpoint_access"]
DescribeEndpointAuthorizationPaginatorName = Literal["describe_endpoint_authorization"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeHsmClientCertificatesPaginatorName = Literal["describe_hsm_client_certificates"]
DescribeHsmConfigurationsPaginatorName = Literal["describe_hsm_configurations"]
DescribeInboundIntegrationsPaginatorName = Literal["describe_inbound_integrations"]
DescribeNodeConfigurationOptionsPaginatorName = Literal["describe_node_configuration_options"]
DescribeOrderableClusterOptionsPaginatorName = Literal["describe_orderable_cluster_options"]
DescribeRedshiftIdcApplicationsPaginatorName = Literal["describe_redshift_idc_applications"]
DescribeReservedNodeExchangeStatusPaginatorName = Literal["describe_reserved_node_exchange_status"]
DescribeReservedNodeOfferingsPaginatorName = Literal["describe_reserved_node_offerings"]
DescribeReservedNodesPaginatorName = Literal["describe_reserved_nodes"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
DescribeSnapshotCopyGrantsPaginatorName = Literal["describe_snapshot_copy_grants"]
DescribeSnapshotSchedulesPaginatorName = Literal["describe_snapshot_schedules"]
DescribeTableRestoreStatusPaginatorName = Literal["describe_table_restore_status"]
DescribeTagsPaginatorName = Literal["describe_tags"]
DescribeUsageLimitsPaginatorName = Literal["describe_usage_limits"]
GetReservedNodeExchangeConfigurationOptionsPaginatorName = Literal["get_reserved_node_exchange_configuration_options"]
GetReservedNodeExchangeOfferingsPaginatorName = Literal["get_reserved_node_exchange_offerings"]
ImpactRankingTypeType = Literal["HIGH", "LOW", "MEDIUM"]
ListRecommendationsPaginatorName = Literal["list_recommendations"]
LogDestinationTypeType = Literal["cloudwatch", "s3"]
ModeType = Literal["high-performance", "standard"]
NodeConfigurationOptionsFilterNameType = Literal["EstimatedDiskUtilizationPercent", "Mode", "NodeType", "NumberOfNodes"]
OperatorTypeType = Literal["between", "eq", "ge", "gt", "in", "le", "lt"]
ParameterApplyTypeType = Literal["dynamic", "static"]
PartnerIntegrationStatusType = Literal["Active", "ConnectionFailure", "Inactive", "RuntimeFailure"]
RecommendedActionTypeType = Literal["CLI", "SQL"]
ReservedNodeExchangeActionTypeType = Literal["resize-cluster", "restore-cluster"]
ReservedNodeExchangeStatusTypeType = Literal["FAILED", "IN_PROGRESS", "PENDING", "REQUESTED", "RETRYING", "SUCCEEDED"]
ReservedNodeOfferingTypeType = Literal["Regular", "Upgradable"]
ScheduleStateType = Literal["ACTIVE", "FAILED", "MODIFYING"]
ScheduledActionFilterNameType = Literal["cluster-identifier", "iam-role"]
ScheduledActionStateType = Literal["ACTIVE", "DISABLED"]
ScheduledActionTypeValuesType = Literal["PauseCluster", "ResizeCluster", "ResumeCluster"]
ServiceAuthorizationType = Literal["Disabled", "Enabled"]
SnapshotAttributeToSortByType = Literal["CREATE_TIME", "SOURCE_TYPE", "TOTAL_SIZE"]
SnapshotAvailableWaiterName = Literal["snapshot_available"]
SortByOrderType = Literal["ASC", "DESC"]
SourceTypeType = Literal["cluster",
    "cluster-parameter-group",
    "cluster-security-group",
    "cluster-snapshot",
    "scheduled-action",]
TableRestoreStatusTypeType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "PENDING", "SUCCEEDED"]
UsageLimitBreachActionType = Literal["disable", "emit-metric", "log"]
UsageLimitFeatureTypeType = Literal["concurrency-scaling", "cross-region-datasharing", "spectrum"]
UsageLimitLimitTypeType = Literal["data-scanned", "time"]
UsageLimitPeriodType = Literal["daily", "monthly", "weekly"]
ZeroETLIntegrationStatusType = Literal["active", "creating", "deleting", "failed", "modifying", "needs_attention", "syncing"]
RedshiftServiceName = Literal["redshift"]
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
PaginatorName = Literal["describe_cluster_db_revisions",
    "describe_cluster_parameter_groups",
    "describe_cluster_parameters",
    "describe_cluster_security_groups",
    "describe_cluster_snapshots",
    "describe_cluster_subnet_groups",
    "describe_cluster_tracks",
    "describe_cluster_versions",
    "describe_clusters",
    "describe_custom_domain_associations",
    "describe_data_shares",
    "describe_data_shares_for_consumer",
    "describe_data_shares_for_producer",
    "describe_default_cluster_parameters",
    "describe_endpoint_access",
    "describe_endpoint_authorization",
    "describe_event_subscriptions",
    "describe_events",
    "describe_hsm_client_certificates",
    "describe_hsm_configurations",
    "describe_inbound_integrations",
    "describe_node_configuration_options",
    "describe_orderable_cluster_options",
    "describe_redshift_idc_applications",
    "describe_reserved_node_exchange_status",
    "describe_reserved_node_offerings",
    "describe_reserved_nodes",
    "describe_scheduled_actions",
    "describe_snapshot_copy_grants",
    "describe_snapshot_schedules",
    "describe_table_restore_status",
    "describe_tags",
    "describe_usage_limits",
    "get_reserved_node_exchange_configuration_options",
    "get_reserved_node_exchange_offerings",
    "list_recommendations",]
WaiterName = Literal["cluster_available", "cluster_deleted", "cluster_restored", "snapshot_available"]
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
AuthorizedTokenIssuerUnionTypeDef = Union[   'AuthorizedTokenIssuerTypeDef', 'AuthorizedTokenIssuerExtraOutputTypeDef' ]
ServiceIntegrationsUnionUnionTypeDef = Union[   'ServiceIntegrationsUnionTypeDef', 'ServiceIntegrationsUnionExtraOutputTypeDef' ]