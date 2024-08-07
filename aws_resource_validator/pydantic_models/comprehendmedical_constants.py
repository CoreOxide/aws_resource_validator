from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO
from datetime import datetime

AttributeNameType = Literal["DIAGNOSIS",
    "FUTURE",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "NEGATION",
    "PAST_HISTORY",
    "PERTAINS_TO_FAMILY",
    "SIGN",
    "SYMPTOM",]
EntitySubTypeType = Literal["ACUITY",
    "ADDRESS",
    "AGE",
    "ALCOHOL_CONSUMPTION",
    "ALLERGIES",
    "AMOUNT",
    "BRAND_NAME",
    "CONTACT_POINT",
    "DATE",
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "DX_NAME",
    "EMAIL",
    "FORM",
    "FREQUENCY",
    "GENDER",
    "GENERIC_NAME",
    "ID",
    "IDENTIFIER",
    "NAME",
    "PHONE_OR_FAX",
    "PROCEDURE_NAME",
    "PROFESSION",
    "QUALITY",
    "QUANTITY",
    "RACE_ETHNICITY",
    "RATE",
    "REC_DRUG_USE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_NAME",
    "TEST_UNIT",
    "TEST_UNITS",
    "TEST_VALUE",
    "TIME_EXPRESSION",
    "TIME_TO_DX_NAME",
    "TIME_TO_MEDICATION_NAME",
    "TIME_TO_PROCEDURE_NAME",
    "TIME_TO_TEST_NAME",
    "TIME_TO_TREATMENT_NAME",
    "TOBACCO_USE",
    "TREATMENT_NAME",
    "URL",]
EntityTypeType = Literal["ANATOMY",
    "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
    "MEDICAL_CONDITION",
    "MEDICATION",
    "PROTECTED_HEALTH_INFORMATION",
    "TEST_TREATMENT_PROCEDURE",
    "TIME_EXPRESSION",]
ICD10CMAttributeTypeType = Literal["ACUITY",
    "DIRECTION",
    "QUALITY",
    "QUANTITY",
    "SYSTEM_ORGAN_SITE",
    "TIME_EXPRESSION",
    "TIME_TO_DX_NAME",]
ICD10CMEntityCategoryType = Literal["MEDICAL_CONDITION"]
ICD10CMEntityTypeType = Literal["DX_NAME", "TIME_EXPRESSION"]
ICD10CMRelationshipTypeType = Literal["OVERLAP", "QUALITY", "SYSTEM_ORGAN_SITE"]
ICD10CMTraitNameType = Literal["DIAGNOSIS",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "NEGATION",
    "PERTAINS_TO_FAMILY",
    "SIGN",
    "SYMPTOM",]
JobStatusType = Literal["COMPLETED",
    "FAILED",
    "IN_PROGRESS",
    "PARTIAL_SUCCESS",
    "STOPPED",
    "STOP_REQUESTED",
    "SUBMITTED",]
LanguageCodeType = Literal["en"]
RelationshipTypeType = Literal["ACUITY",
    "ADMINISTERED_VIA",
    "AMOUNT",
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "EVERY",
    "FOR",
    "FORM",
    "FREQUENCY",
    "NEGATIVE",
    "OVERLAP",
    "QUALITY",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_UNIT",
    "TEST_UNITS",
    "TEST_VALUE",
    "USAGE",
    "WITH_DOSAGE",]
RxNormAttributeTypeType = Literal["DOSAGE", "DURATION", "FORM", "FREQUENCY", "RATE", "ROUTE_OR_MODE", "STRENGTH"]
RxNormEntityCategoryType = Literal["MEDICATION"]
RxNormEntityTypeType = Literal["BRAND_NAME", "GENERIC_NAME"]
RxNormTraitNameType = Literal["NEGATION", "PAST_HISTORY"]
SNOMEDCTAttributeTypeType = Literal["ACUITY", "DIRECTION", "QUALITY", "SYSTEM_ORGAN_SITE", "TEST_UNIT", "TEST_VALUE"]
SNOMEDCTEntityCategoryType = Literal["ANATOMY", "MEDICAL_CONDITION", "TEST_TREATMENT_PROCEDURE"]
SNOMEDCTEntityTypeType = Literal["DX_NAME", "PROCEDURE_NAME", "TEST_NAME", "TREATMENT_NAME"]
SNOMEDCTRelationshipTypeType = Literal["ACUITY", "DIRECTION", "QUALITY", "SYSTEM_ORGAN_SITE", "TEST_UNIT", "TEST_UNITS", "TEST_VALUE"]
SNOMEDCTTraitNameType = Literal["DIAGNOSIS",
    "FUTURE",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "NEGATION",
    "PAST_HISTORY",
    "PERTAINS_TO_FAMILY",
    "SIGN",
    "SYMPTOM",]
ComprehendMedicalServiceName = Literal["comprehendmedical"]
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
RegionName = Literal["ap-southeast-2",
    "ca-central-1",
    "eu-west-1",
    "eu-west-2",
    "us-east-1",
    "us-east-2",
    "us-west-2",]
TimestampTypeDef = Union[datetime, str]
