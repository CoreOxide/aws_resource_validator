from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AutomaticTerminationModeType = Literal["ACTIVATED", "DEACTIVATED"]
LaunchProfileDeletedWaiterName = Literal["launch_profile_deleted"]
LaunchProfilePersonaType = Literal["USER"]
LaunchProfilePlatformType = Literal["LINUX", "WINDOWS"]
LaunchProfileReadyWaiterName = Literal["launch_profile_ready"]
LaunchProfileStateType = Literal["CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",]
LaunchProfileStatusCodeType = Literal["ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "INVALID_INSTANCE_TYPES_PROVIDED",
    "INVALID_SUBNETS_COMBINATION",
    "INVALID_SUBNETS_PROVIDED",
    "LAUNCH_PROFILE_CREATED",
    "LAUNCH_PROFILE_CREATE_IN_PROGRESS",
    "LAUNCH_PROFILE_DELETED",
    "LAUNCH_PROFILE_DELETE_IN_PROGRESS",
    "LAUNCH_PROFILE_UPDATED",
    "LAUNCH_PROFILE_UPDATE_IN_PROGRESS",
    "LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED",
    "STREAMING_IMAGE_NOT_FOUND",
    "STREAMING_IMAGE_NOT_READY",]
LaunchProfileValidationStateType = Literal["VALIDATION_FAILED",
    "VALIDATION_FAILED_INTERNAL_SERVER_ERROR",
    "VALIDATION_IN_PROGRESS",
    "VALIDATION_NOT_STARTED",
    "VALIDATION_SUCCESS",]
LaunchProfileValidationStatusCodeType = Literal["VALIDATION_FAILED_INTERNAL_SERVER_ERROR",
    "VALIDATION_FAILED_INVALID_ACTIVE_DIRECTORY",
    "VALIDATION_FAILED_INVALID_SECURITY_GROUP_ASSOCIATION",
    "VALIDATION_FAILED_INVALID_SUBNET_ROUTE_TABLE_ASSOCIATION",
    "VALIDATION_FAILED_SUBNET_NOT_FOUND",
    "VALIDATION_FAILED_UNAUTHORIZED",
    "VALIDATION_IN_PROGRESS",
    "VALIDATION_NOT_STARTED",
    "VALIDATION_SUCCESS",]
LaunchProfileValidationTypeType = Literal["VALIDATE_ACTIVE_DIRECTORY_STUDIO_COMPONENT",
    "VALIDATE_NETWORK_ACL_ASSOCIATION",
    "VALIDATE_SECURITY_GROUP_ASSOCIATION",
    "VALIDATE_SUBNET_ASSOCIATION",]
ListEulaAcceptancesPaginatorName = Literal["list_eula_acceptances"]
ListEulasPaginatorName = Literal["list_eulas"]
ListLaunchProfileMembersPaginatorName = Literal["list_launch_profile_members"]
ListLaunchProfilesPaginatorName = Literal["list_launch_profiles"]
ListStreamingImagesPaginatorName = Literal["list_streaming_images"]
ListStreamingSessionBackupsPaginatorName = Literal["list_streaming_session_backups"]
ListStreamingSessionsPaginatorName = Literal["list_streaming_sessions"]
ListStudioComponentsPaginatorName = Literal["list_studio_components"]
ListStudioMembersPaginatorName = Literal["list_studio_members"]
ListStudiosPaginatorName = Literal["list_studios"]
SessionBackupModeType = Literal["AUTOMATIC", "DEACTIVATED"]
SessionPersistenceModeType = Literal["ACTIVATED", "DEACTIVATED"]
StreamingClipboardModeType = Literal["DISABLED", "ENABLED"]
StreamingImageDeletedWaiterName = Literal["streaming_image_deleted"]
StreamingImageEncryptionConfigurationKeyTypeType = Literal["CUSTOMER_MANAGED_KEY"]
StreamingImageReadyWaiterName = Literal["streaming_image_ready"]
StreamingImageStateType = Literal["CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",]
StreamingImageStatusCodeType = Literal["ACCESS_DENIED",
    "INTERNAL_ERROR",
    "STREAMING_IMAGE_CREATE_IN_PROGRESS",
    "STREAMING_IMAGE_DELETED",
    "STREAMING_IMAGE_DELETE_IN_PROGRESS",
    "STREAMING_IMAGE_READY",
    "STREAMING_IMAGE_UPDATE_IN_PROGRESS",]
StreamingInstanceTypeType = Literal["g3.4xlarge",
    "g3s.xlarge",
    "g4dn.12xlarge",
    "g4dn.16xlarge",
    "g4dn.2xlarge",
    "g4dn.4xlarge",
    "g4dn.8xlarge",
    "g4dn.xlarge",
    "g5.16xlarge",
    "g5.2xlarge",
    "g5.4xlarge",
    "g5.8xlarge",
    "g5.xlarge",]
StreamingSessionDeletedWaiterName = Literal["streaming_session_deleted"]
StreamingSessionReadyWaiterName = Literal["streaming_session_ready"]
StreamingSessionStateType = Literal["CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "START_FAILED",
    "START_IN_PROGRESS",
    "STOPPED",
    "STOP_FAILED",
    "STOP_IN_PROGRESS",]
StreamingSessionStatusCodeType = Literal["ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR",
    "AMI_VALIDATION_ERROR",
    "DECRYPT_STREAMING_IMAGE_ERROR",
    "INITIALIZATION_SCRIPT_ERROR",
    "INSUFFICIENT_CAPACITY",
    "INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "NETWORK_INTERFACE_ERROR",
    "STREAMING_SESSION_CREATE_IN_PROGRESS",
    "STREAMING_SESSION_DELETED",
    "STREAMING_SESSION_DELETE_IN_PROGRESS",
    "STREAMING_SESSION_READY",
    "STREAMING_SESSION_STARTED",
    "STREAMING_SESSION_START_IN_PROGRESS",
    "STREAMING_SESSION_STOPPED",
    "STREAMING_SESSION_STOP_IN_PROGRESS",]
StreamingSessionStoppedWaiterName = Literal["streaming_session_stopped"]
StreamingSessionStorageModeType = Literal["UPLOAD"]
StreamingSessionStreamReadyWaiterName = Literal["streaming_session_stream_ready"]
StreamingSessionStreamStateType = Literal["CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "READY"]
StreamingSessionStreamStatusCodeType = Literal["INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "STREAM_CREATE_IN_PROGRESS",
    "STREAM_DELETED",
    "STREAM_DELETE_IN_PROGRESS",
    "STREAM_READY",]
StudioComponentDeletedWaiterName = Literal["studio_component_deleted"]
StudioComponentInitializationScriptRunContextType = Literal["SYSTEM_INITIALIZATION", "USER_INITIALIZATION"]
StudioComponentReadyWaiterName = Literal["studio_component_ready"]
StudioComponentStateType = Literal["CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",]
StudioComponentStatusCodeType = Literal["ACTIVE_DIRECTORY_ALREADY_EXISTS",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "STUDIO_COMPONENT_CREATED",
    "STUDIO_COMPONENT_CREATE_IN_PROGRESS",
    "STUDIO_COMPONENT_DELETED",
    "STUDIO_COMPONENT_DELETE_IN_PROGRESS",
    "STUDIO_COMPONENT_UPDATED",
    "STUDIO_COMPONENT_UPDATE_IN_PROGRESS",]
StudioComponentSubtypeType = Literal["AMAZON_FSX_FOR_LUSTRE", "AMAZON_FSX_FOR_WINDOWS", "AWS_MANAGED_MICROSOFT_AD", "CUSTOM"]
StudioComponentTypeType = Literal["ACTIVE_DIRECTORY", "COMPUTE_FARM", "CUSTOM", "LICENSE_SERVICE", "SHARED_FILE_SYSTEM"]
StudioDeletedWaiterName = Literal["studio_deleted"]
StudioEncryptionConfigurationKeyTypeType = Literal["AWS_OWNED_KEY", "CUSTOMER_MANAGED_KEY"]
StudioPersonaType = Literal["ADMINISTRATOR"]
StudioReadyWaiterName = Literal["studio_ready"]
StudioStateType = Literal["CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",]
StudioStatusCodeType = Literal["AWS_SSO_ACCESS_DENIED",
    "AWS_SSO_CONFIGURATION_REPAIRED",
    "AWS_SSO_CONFIGURATION_REPAIR_IN_PROGRESS",
    "AWS_SSO_NOT_ENABLED",
    "AWS_STS_REGION_DISABLED",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "ROLE_COULD_NOT_BE_ASSUMED",
    "ROLE_NOT_OWNED_BY_STUDIO_OWNER",
    "STUDIO_CREATED",
    "STUDIO_CREATE_IN_PROGRESS",
    "STUDIO_DELETED",
    "STUDIO_DELETE_IN_PROGRESS",
    "STUDIO_UPDATED",
    "STUDIO_UPDATE_IN_PROGRESS",
    "STUDIO_WITH_LAUNCH_PROFILES_NOT_DELETED",
    "STUDIO_WITH_STREAMING_IMAGES_NOT_DELETED",
    "STUDIO_WITH_STUDIO_COMPONENTS_NOT_DELETED",]
VolumeRetentionModeType = Literal["DELETE", "RETAIN"]
NimbleStudioServiceName = Literal["nimble"]
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
PaginatorName = Literal["list_eula_acceptances",
    "list_eulas",
    "list_launch_profile_members",
    "list_launch_profiles",
    "list_streaming_images",
    "list_streaming_session_backups",
    "list_streaming_sessions",
    "list_studio_components",
    "list_studio_members",
    "list_studios",]
WaiterName = Literal["launch_profile_deleted",
    "launch_profile_ready",
    "streaming_image_deleted",
    "streaming_image_ready",
    "streaming_session_deleted",
    "streaming_session_ready",
    "streaming_session_stopped",
    "streaming_session_stream_ready",
    "studio_component_deleted",
    "studio_component_ready",
    "studio_deleted",
    "studio_ready",]
RegionName = Literal["ap-northeast-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "us-east-1",
    "us-east-2",
    "us-west-2",]