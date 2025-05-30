from typing import Literal
from datetime import datetime


ActionGroupSignatureType = Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']
ActionGroupStateType = Literal['DISABLED', 'ENABLED']
AgentAliasStatusType = Literal['CREATING', 'DELETING', 'DISSOCIATED', 'FAILED', 'PREPARED', 'UPDATING']
AgentCollaborationType = Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']
AgentStatusType = Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
AgentsforBedrockServiceName = Literal['bedrock-agent']
CachePointTypeType = Literal['default']
ChunkingStrategyType = Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
ConfluenceAuthTypeType = Literal['BASIC', 'OAUTH2_CLIENT_CREDENTIALS']
ConfluenceHostTypeType = Literal['SAAS']
ContentDataSourceTypeType = Literal['CUSTOM', 'S3']
ContextEnrichmentTypeType = Literal['BEDROCK_FOUNDATION_MODEL']
ConversationRoleType = Literal['assistant', 'user']
CrawlFilterConfigurationTypeType = Literal['PATTERN']
CreationModeType = Literal['DEFAULT', 'OVERRIDDEN']
CustomControlMethodType = Literal['RETURN_CONTROL']
CustomSourceTypeType = Literal['IN_LINE', 'S3_LOCATION']
DataDeletionPolicyType = Literal['DELETE', 'RETAIN']
DataSourceStatusType = Literal['AVAILABLE', 'DELETE_UNSUCCESSFUL', 'DELETING']
DataSourceTypeType = Literal['CONFLUENCE', 'CUSTOM', 'REDSHIFT_METADATA', 'S3', 'SALESFORCE', 'SHAREPOINT', 'WEB']
DocumentStatusType = Literal['DELETE_IN_PROGRESS', 'DELETING', 'FAILED', 'IGNORED', 'INDEXED', 'IN_PROGRESS', 'METADATA_PARTIALLY_INDEXED', 'METADATA_UPDATE_FAILED', 'NOT_FOUND', 'PARTIALLY_INDEXED', 'PENDING', 'STARTING']
EmbeddingDataTypeType = Literal['BINARY', 'FLOAT32']
EnrichmentStrategyMethodType = Literal['CHUNK_ENTITY_EXTRACTION']
FlowConnectionTypeType = Literal['Conditional', 'Data']
FlowNodeIODataTypeType = Literal['Array', 'Boolean', 'Number', 'Object', 'String']
FlowNodeTypeType = Literal['Agent', 'Collector', 'Condition', 'Input', 'Iterator', 'KnowledgeBase', 'LambdaFunction', 'Lex', 'Output', 'Prompt', 'Retrieval', 'Storage']
FlowStatusType = Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
FlowValidationSeverityType = Literal['Error', 'Warning']
FlowValidationTypeType = Literal['CyclicConnection', 'DuplicateConditionExpression', 'DuplicateConnections', 'IncompatibleConnectionDataType', 'MalformedConditionExpression', 'MalformedNodeInputExpression', 'MismatchedNodeInputType', 'MismatchedNodeOutputType', 'MissingConnectionConfiguration', 'MissingDefaultCondition', 'MissingEndingNodes', 'MissingNodeConfiguration', 'MissingNodeInput', 'MissingNodeOutput', 'MissingStartingNodes', 'MultipleNodeInputConnections', 'UnfulfilledNodeInput', 'UnknownConnectionCondition', 'UnknownConnectionSource', 'UnknownConnectionSourceOutput', 'UnknownConnectionTarget', 'UnknownConnectionTargetInput', 'UnknownNodeInput', 'UnknownNodeOutput', 'UnreachableNode', 'UnsatisfiedConnectionConditions', 'Unspecified']
IncludeExcludeType = Literal['EXCLUDE', 'INCLUDE']
IngestionJobFilterAttributeType = Literal['STATUS']
IngestionJobFilterOperatorType = Literal['EQ']
IngestionJobSortByAttributeType = Literal['STARTED_AT', 'STATUS']
IngestionJobStatusType = Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
InlineContentTypeType = Literal['BYTE', 'TEXT']
KnowledgeBaseStateType = Literal['DISABLED', 'ENABLED']
KnowledgeBaseStatusType = Literal['ACTIVE', 'CREATING', 'DELETE_UNSUCCESSFUL', 'DELETING', 'FAILED', 'UPDATING']
KnowledgeBaseStorageTypeType = Literal['MONGO_DB_ATLAS', 'NEPTUNE_ANALYTICS', 'OPENSEARCH_SERVERLESS', 'PINECONE', 'RDS', 'REDIS_ENTERPRISE_CLOUD']
KnowledgeBaseTypeType = Literal['KENDRA', 'SQL', 'VECTOR']
ListAgentActionGroupsPaginatorName = Literal['list_agent_action_groups']
ListAgentAliasesPaginatorName = Literal['list_agent_aliases']
ListAgentCollaboratorsPaginatorName = Literal['list_agent_collaborators']
ListAgentKnowledgeBasesPaginatorName = Literal['list_agent_knowledge_bases']
ListAgentVersionsPaginatorName = Literal['list_agent_versions']
ListAgentsPaginatorName = Literal['list_agents']
ListDataSourcesPaginatorName = Literal['list_data_sources']
ListFlowAliasesPaginatorName = Literal['list_flow_aliases']
ListFlowVersionsPaginatorName = Literal['list_flow_versions']
ListFlowsPaginatorName = Literal['list_flows']
ListIngestionJobsPaginatorName = Literal['list_ingestion_jobs']
ListKnowledgeBaseDocumentsPaginatorName = Literal['list_knowledge_base_documents']
ListKnowledgeBasesPaginatorName = Literal['list_knowledge_bases']
ListPromptsPaginatorName = Literal['list_prompts']
MemoryTypeType = Literal['SESSION_SUMMARY']
MetadataSourceTypeType = Literal['IN_LINE_ATTRIBUTE', 'S3_LOCATION']
MetadataValueTypeType = Literal['BOOLEAN', 'NUMBER', 'STRING', 'STRING_LIST']
OrchestrationTypeType = Literal['CUSTOM_ORCHESTRATION', 'DEFAULT']
PaginatorName = Literal['list_agent_action_groups', 'list_agent_aliases', 'list_agent_collaborators', 'list_agent_knowledge_bases', 'list_agent_versions', 'list_agents', 'list_data_sources', 'list_flow_aliases', 'list_flow_versions', 'list_flows', 'list_ingestion_jobs', 'list_knowledge_base_documents', 'list_knowledge_bases', 'list_prompts']
ParsingModalityType = Literal['MULTIMODAL']
ParsingStrategyType = Literal['BEDROCK_DATA_AUTOMATION', 'BEDROCK_FOUNDATION_MODEL']
PromptStateType = Literal['DISABLED', 'ENABLED']
PromptTemplateTypeType = Literal['CHAT', 'TEXT']
PromptTypeType = Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'MEMORY_SUMMARIZATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']
QueryEngineTypeType = Literal['REDSHIFT']
RedshiftProvisionedAuthTypeType = Literal['IAM', 'USERNAME', 'USERNAME_PASSWORD']
RedshiftQueryEngineStorageTypeType = Literal['AWS_DATA_CATALOG', 'REDSHIFT']
RedshiftQueryEngineTypeType = Literal['PROVISIONED', 'SERVERLESS']
RedshiftServerlessAuthTypeType = Literal['IAM', 'USERNAME_PASSWORD']
RelayConversationHistoryType = Literal['DISABLED', 'TO_COLLABORATOR']
RequireConfirmationType = Literal['DISABLED', 'ENABLED']
ResourceServiceName = Literal['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']
SalesforceAuthTypeType = Literal['OAUTH2_CLIENT_CREDENTIALS']
ServiceName = Literal['accessanalyzer', 'account', 'acm', 'acm-pca', 'amp', 'amplify', 'amplifybackend', 'amplifyuibuilder', 'apigateway', 'apigatewaymanagementapi', 'apigatewayv2', 'appconfig', 'appconfigdata', 'appfabric', 'appflow', 'appintegrations', 'application-autoscaling', 'application-insights', 'application-signals', 'applicationcostprofiler', 'appmesh', 'apprunner', 'appstream', 'appsync', 'apptest', 'arc-zonal-shift', 'artifact', 'athena', 'auditmanager', 'autoscaling', 'autoscaling-plans', 'b2bi', 'backup', 'backup-gateway', 'backupsearch', 'batch', 'bcm-data-exports', 'bcm-pricing-calculator', 'bedrock', 'bedrock-agent', 'bedrock-agent-runtime', 'bedrock-data-automation', 'bedrock-data-automation-runtime', 'bedrock-runtime', 'billing', 'billingconductor', 'braket', 'budgets', 'ce', 'chatbot', 'chime', 'chime-sdk-identity', 'chime-sdk-media-pipelines', 'chime-sdk-meetings', 'chime-sdk-messaging', 'chime-sdk-voice', 'cleanrooms', 'cleanroomsml', 'cloud9', 'cloudcontrol', 'clouddirectory', 'cloudformation', 'cloudfront', 'cloudfront-keyvaluestore', 'cloudhsm', 'cloudhsmv2', 'cloudsearch', 'cloudsearchdomain', 'cloudtrail', 'cloudtrail-data', 'cloudwatch', 'codeartifact', 'codebuild', 'codecatalyst', 'codecommit', 'codeconnections', 'codedeploy', 'codeguru-reviewer', 'codeguru-security', 'codeguruprofiler', 'codepipeline', 'codestar-connections', 'codestar-notifications', 'cognito-identity', 'cognito-idp', 'cognito-sync', 'comprehend', 'comprehendmedical', 'compute-optimizer', 'config', 'connect', 'connect-contact-lens', 'connectcampaigns', 'connectcampaignsv2', 'connectcases', 'connectparticipant', 'controlcatalog', 'controltower', 'cost-optimization-hub', 'cur', 'customer-profiles', 'databrew', 'dataexchange', 'datapipeline', 'datasync', 'datazone', 'dax', 'deadline', 'detective', 'devicefarm', 'devops-guru', 'directconnect', 'discovery', 'dlm', 'dms', 'docdb', 'docdb-elastic', 'drs', 'ds', 'ds-data', 'dsql', 'dynamodb', 'dynamodbstreams', 'ebs', 'ec2', 'ec2-instance-connect', 'ecr', 'ecr-public', 'ecs', 'efs', 'eks', 'eks-auth', 'elasticache', 'elasticbeanstalk', 'elastictranscoder', 'elb', 'elbv2', 'emr', 'emr-containers', 'emr-serverless', 'entityresolution', 'es', 'events', 'evidently', 'finspace', 'finspace-data', 'firehose', 'fis', 'fms', 'forecast', 'forecastquery', 'frauddetector', 'freetier', 'fsx', 'gamelift', 'gameliftstreams', 'geo-maps', 'geo-places', 'geo-routes', 'glacier', 'globalaccelerator', 'glue', 'grafana', 'greengrass', 'greengrassv2', 'groundstation', 'guardduty', 'health', 'healthlake', 'iam', 'identitystore', 'imagebuilder', 'importexport', 'inspector', 'inspector-scan', 'inspector2', 'internetmonitor', 'invoicing', 'iot', 'iot-data', 'iot-jobs-data', 'iot-managed-integrations', 'iotanalytics', 'iotdeviceadvisor', 'iotevents', 'iotevents-data', 'iotfleethub', 'iotfleetwise', 'iotsecuretunneling', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker', 'iotwireless', 'ivs', 'ivs-realtime', 'ivschat', 'kafka', 'kafkaconnect', 'kendra', 'kendra-ranking', 'keyspaces', 'kinesis', 'kinesis-video-archived-media', 'kinesis-video-media', 'kinesis-video-signaling', 'kinesis-video-webrtc-storage', 'kinesisanalytics', 'kinesisanalyticsv2', 'kinesisvideo', 'kms', 'lakeformation', 'lambda', 'launch-wizard', 'lex-models', 'lex-runtime', 'lexv2-models', 'lexv2-runtime', 'license-manager', 'license-manager-linux-subscriptions', 'license-manager-user-subscriptions', 'lightsail', 'location', 'logs', 'lookoutequipment', 'lookoutmetrics', 'lookoutvision', 'm2', 'machinelearning', 'macie2', 'mailmanager', 'managedblockchain', 'managedblockchain-query', 'marketplace-agreement', 'marketplace-catalog', 'marketplace-deployment', 'marketplace-entitlement', 'marketplace-reporting', 'marketplacecommerceanalytics', 'mediaconnect', 'mediaconvert', 'medialive', 'mediapackage', 'mediapackage-vod', 'mediapackagev2', 'mediastore', 'mediastore-data', 'mediatailor', 'medical-imaging', 'memorydb', 'meteringmarketplace', 'mgh', 'mgn', 'migration-hub-refactor-spaces', 'migrationhub-config', 'migrationhuborchestrator', 'migrationhubstrategy', 'mq', 'mturk', 'mwaa', 'neptune', 'neptune-graph', 'neptunedata', 'network-firewall', 'networkflowmonitor', 'networkmanager', 'networkmonitor', 'notifications', 'notificationscontacts', 'oam', 'observabilityadmin', 'omics', 'opensearch', 'opensearchserverless', 'opsworks', 'opsworkscm', 'organizations', 'osis', 'outposts', 'panorama', 'partnercentral-selling', 'payment-cryptography', 'payment-cryptography-data', 'pca-connector-ad', 'pca-connector-scep', 'pcs', 'personalize', 'personalize-events', 'personalize-runtime', 'pi', 'pinpoint', 'pinpoint-email', 'pinpoint-sms-voice', 'pinpoint-sms-voice-v2', 'pipes', 'polly', 'pricing', 'privatenetworks', 'proton', 'qapps', 'qbusiness', 'qconnect', 'qldb', 'qldb-session', 'quicksight', 'ram', 'rbin', 'rds', 'rds-data', 'redshift', 'redshift-data', 'redshift-serverless', 'rekognition', 'repostspace', 'resiliencehub', 'resource-explorer-2', 'resource-groups', 'resourcegroupstaggingapi', 'robomaker', 'rolesanywhere', 'route53', 'route53-recovery-cluster', 'route53-recovery-control-config', 'route53-recovery-readiness', 'route53domains', 'route53profiles', 'route53resolver', 'rum', 's3', 's3control', 's3outposts', 's3tables', 'sagemaker', 'sagemaker-a2i-runtime', 'sagemaker-edge', 'sagemaker-featurestore-runtime', 'sagemaker-geospatial', 'sagemaker-metrics', 'sagemaker-runtime', 'savingsplans', 'scheduler', 'schemas', 'sdb', 'secretsmanager', 'security-ir', 'securityhub', 'securitylake', 'serverlessrepo', 'service-quotas', 'servicecatalog', 'servicecatalog-appregistry', 'servicediscovery', 'ses', 'sesv2', 'shield', 'signer', 'simspaceweaver', 'sms', 'sms-voice', 'snow-device-management', 'snowball', 'sns', 'socialmessaging', 'sqs', 'ssm', 'ssm-contacts', 'ssm-incidents', 'ssm-quicksetup', 'ssm-sap', 'sso', 'sso-admin', 'sso-oidc', 'stepfunctions', 'storagegateway', 'sts', 'supplychain', 'support', 'support-app', 'swf', 'synthetics', 'taxsettings', 'textract', 'timestream-influxdb', 'timestream-query', 'timestream-write', 'tnb', 'transcribe', 'transfer', 'translate', 'trustedadvisor', 'verifiedpermissions', 'voice-id', 'vpc-lattice', 'waf', 'waf-regional', 'wafv2', 'wellarchitected', 'wisdom', 'workdocs', 'workmail', 'workmailmessageflow', 'workspaces', 'workspaces-thin-client', 'workspaces-web', 'xray']
SharePointAuthTypeType = Literal['OAUTH2_CLIENT_CREDENTIALS', 'OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS']
SharePointHostTypeType = Literal['ONLINE']
SortOrderType = Literal['ASCENDING', 'DESCENDING']
StepTypeType = Literal['POST_CHUNKING']
SupplementalDataStorageLocationTypeType = Literal['S3']
TypeType = Literal['array', 'boolean', 'integer', 'number', 'string']
WebScopeTypeType = Literal['HOST_ONLY', 'SUBDOMAINS']