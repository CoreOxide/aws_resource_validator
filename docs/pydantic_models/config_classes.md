# Config Classes

# AccountAggregationSourceOutputTypeDef

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### AllAwsRegions
- **Type**: typing.Optional[bool]

### AwsRegions
- **Type**: typing.Optional[typing.List[str]]


# AccountAggregationSourceTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AllAwsRegions
- **Type**: typing.Optional[bool]

### AwsRegions
- **Type**: typing.Optional[typing.Sequence[str]]


# AccountAggregationSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregateComplianceByConfigRuleTypeDef

### ConfigRuleName
- **Type**: typing.Optional[str]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceTypeDef]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateComplianceByConformancePackTypeDef

### ConformancePackName
- **Type**: typing.Optional[str]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregateConformancePackComplianceTypeDef]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateComplianceCountTypeDef

### GroupName
- **Type**: typing.Optional[str]

### ComplianceSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceSummaryTypeDef]


# AggregateConformancePackComplianceCountTypeDef

### CompliantConformancePackCount
- **Type**: typing.Optional[int]

### NonCompliantConformancePackCount
- **Type**: typing.Optional[int]


# AggregateConformancePackComplianceFiltersTypeDef

### ConformancePackName
- **Type**: typing.Optional[str]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateConformancePackComplianceSummaryFiltersTypeDef

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateConformancePackComplianceSummaryTypeDef

### ComplianceSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregateConformancePackComplianceCountTypeDef]

### GroupName
- **Type**: typing.Optional[str]


# AggregateConformancePackComplianceTypeDef

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### CompliantRuleCount
- **Type**: typing.Optional[int]

### NonCompliantRuleCount
- **Type**: typing.Optional[int]

### TotalRuleCount
- **Type**: typing.Optional[int]


# AggregateEvaluationResultTypeDef

### EvaluationResultIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.EvaluationResultIdentifierTypeDef]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### ResultRecordedTime
- **Type**: typing.Optional[datetime.datetime]

### ConfigRuleInvokedTime
- **Type**: typing.Optional[datetime.datetime]

### Annotation
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateResourceIdentifierTypeDef

### SourceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### ResourceName
- **Type**: typing.Optional[str]


# AggregatedSourceStatusTypeDef

### SourceId
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'ORGANIZATION']]

### AwsRegion
- **Type**: typing.Optional[str]

### LastUpdateStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'OUTDATED', 'SUCCEEDED']]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### LastErrorCode
- **Type**: typing.Optional[str]

### LastErrorMessage
- **Type**: typing.Optional[str]


# AggregationAuthorizationTypeDef

### AggregationAuthorizationArn
- **Type**: typing.Optional[str]

### AuthorizedAccountId
- **Type**: typing.Optional[str]

### AuthorizedAwsRegion
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# AggregatorFilterResourceTypeOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregatorFilterResourceTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregatorFilterServicePrincipalOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregatorFilterServicePrincipalTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AggregatorFiltersOutputTypeDef

### ResourceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregatorFilterResourceTypeOutputTypeDef]

### ServicePrincipal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregatorFilterServicePrincipalOutputTypeDef]


# AggregatorFiltersTypeDef

### ResourceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregatorFilterResourceTypeTypeDef]

### ServicePrincipal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregatorFilterServicePrincipalTypeDef]


# AggregatorFiltersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateResourceTypesRequestTypeDef

### ConfigurationRecorderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Sequence[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes


# AssociateResourceTypesResponseTypeDef

### ConfigurationRecorder
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseConfigurationItemTypeDef

### version
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### configurationItemCaptureTime
- **Type**: typing.Optional[datetime.datetime]

### configurationItemStatus
- **Type**: typing.Optional[typing.Literal['OK', 'ResourceDeleted', 'ResourceDeletedNotRecorded', 'ResourceDiscovered', 'ResourceNotRecorded']]

### configurationStateId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### resourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### resourceCreationTime
- **Type**: typing.Optional[datetime.datetime]

### configuration
- **Type**: typing.Optional[str]

### supplementaryConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### recordingFrequency
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'DAILY']]

### configurationItemDeliveryTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetAggregateResourceConfigRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.config_classes.AggregateResourceIdentifierTypeDef]
- **Required**: Yes


# BatchGetAggregateResourceConfigResponseTypeDef

### BaseConfigurationItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.BaseConfigurationItemTypeDef]
- **Required**: Yes

### UnprocessedResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregateResourceIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetResourceConfigRequestTypeDef

### resourceKeys
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ResourceKeyTypeDef]
- **Required**: Yes


# BatchGetResourceConfigResponseTypeDef

### baseConfigurationItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.BaseConfigurationItemTypeDef]
- **Required**: Yes

### unprocessedResourceKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ResourceKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ComplianceByConfigRuleTypeDef

### ConfigRuleName
- **Type**: typing.Optional[str]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceTypeDef]


# ComplianceByResourceTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceTypeDef]


# ComplianceContributorCountTypeDef

### CappedCount
- **Type**: typing.Optional[int]

### CapExceeded
- **Type**: typing.Optional[bool]


# ComplianceSummaryByResourceTypeTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ComplianceSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceSummaryTypeDef]


# ComplianceSummaryTypeDef

### CompliantResourceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceContributorCountTypeDef]

### NonCompliantResourceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceContributorCountTypeDef]

### ComplianceSummaryTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ComplianceTypeDef

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### ComplianceContributorCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ComplianceContributorCountTypeDef]


# ConfigExportDeliveryInfoTypeDef

### lastStatus
- **Type**: typing.Optional[typing.Literal['Failure', 'Not_Applicable', 'Success']]

### lastErrorCode
- **Type**: typing.Optional[str]

### lastErrorMessage
- **Type**: typing.Optional[str]

### lastAttemptTime
- **Type**: typing.Optional[datetime.datetime]

### lastSuccessfulTime
- **Type**: typing.Optional[datetime.datetime]

### nextDeliveryTime
- **Type**: typing.Optional[datetime.datetime]


# ConfigRuleComplianceFiltersTypeDef

### ConfigRuleName
- **Type**: typing.Optional[str]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# ConfigRuleComplianceSummaryFiltersTypeDef

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# ConfigRuleEvaluationStatusTypeDef

### ConfigRuleName
- **Type**: typing.Optional[str]

### ConfigRuleArn
- **Type**: typing.Optional[str]

### ConfigRuleId
- **Type**: typing.Optional[str]

### LastSuccessfulInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### LastFailedInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### LastSuccessfulEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### LastFailedEvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### FirstActivatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastDeactivatedTime
- **Type**: typing.Optional[datetime.datetime]

### LastErrorCode
- **Type**: typing.Optional[str]

### LastErrorMessage
- **Type**: typing.Optional[str]

### FirstEvaluationStarted
- **Type**: typing.Optional[bool]

### LastDebugLogDeliveryStatus
- **Type**: typing.Optional[str]

### LastDebugLogDeliveryStatusReason
- **Type**: typing.Optional[str]

### LastDebugLogDeliveryTime
- **Type**: typing.Optional[datetime.datetime]


# ConfigRuleOutputTypeDef

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.SourceOutputTypeDef'>
- **Required**: Yes

### ConfigRuleName
- **Type**: typing.Optional[str]

### ConfigRuleArn
- **Type**: typing.Optional[str]

### ConfigRuleId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ScopeOutputTypeDef]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ConfigRuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'DELETING_RESULTS', 'EVALUATING']]

### CreatedBy
- **Type**: typing.Optional[str]

### EvaluationModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.EvaluationModeConfigurationTypeDef]]


# ConfigRuleTypeDef

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.SourceTypeDef'>
- **Required**: Yes

### ConfigRuleName
- **Type**: typing.Optional[str]

### ConfigRuleArn
- **Type**: typing.Optional[str]

### ConfigRuleId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ScopeTypeDef]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ConfigRuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'DELETING_RESULTS', 'EVALUATING']]

### CreatedBy
- **Type**: typing.Optional[str]

### EvaluationModes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.EvaluationModeConfigurationTypeDef]]


# ConfigRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigSnapshotDeliveryPropertiesTypeDef

### deliveryFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]


# ConfigStreamDeliveryInfoTypeDef

### lastStatus
- **Type**: typing.Optional[typing.Literal['Failure', 'Not_Applicable', 'Success']]

### lastErrorCode
- **Type**: typing.Optional[str]

### lastErrorMessage
- **Type**: typing.Optional[str]

### lastStatusChangeTime
- **Type**: typing.Optional[datetime.datetime]


# ConfigurationAggregatorTypeDef

### ConfigurationAggregatorName
- **Type**: typing.Optional[str]

### ConfigurationAggregatorArn
- **Type**: typing.Optional[str]

### AccountAggregationSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.AccountAggregationSourceOutputTypeDef]]

### OrganizationAggregationSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationAggregationSourceOutputTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]

### AggregatorFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregatorFiltersOutputTypeDef]


# ConfigurationItemTypeDef

### version
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### configurationItemCaptureTime
- **Type**: typing.Optional[datetime.datetime]

### configurationItemStatus
- **Type**: typing.Optional[typing.Literal['OK', 'ResourceDeleted', 'ResourceDeletedNotRecorded', 'ResourceDiscovered', 'ResourceNotRecorded']]

### configurationStateId
- **Type**: typing.Optional[str]

### configurationItemMD5Hash
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### resourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### awsRegion
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### resourceCreationTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### relatedEvents
- **Type**: typing.Optional[typing.List[str]]

### relationships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.RelationshipTypeDef]]

### configuration
- **Type**: typing.Optional[str]

### supplementaryConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### recordingFrequency
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'DAILY']]

### configurationItemDeliveryTime
- **Type**: typing.Optional[datetime.datetime]


# ConfigurationRecorderFilterTypeDef

### filterName
- **Type**: typing.Optional[typing.Literal['recordingScope']]

### filterValue
- **Type**: typing.Optional[typing.Sequence[str]]


# ConfigurationRecorderOutputTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### roleARN
- **Type**: typing.Optional[str]

### recordingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.RecordingGroupOutputTypeDef]

### recordingMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.RecordingModeOutputTypeDef]

### recordingScope
- **Type**: typing.Optional[typing.Literal['INTERNAL', 'PAID']]

### servicePrincipal
- **Type**: typing.Optional[str]


# ConfigurationRecorderStatusTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### lastStartTime
- **Type**: typing.Optional[datetime.datetime]

### lastStopTime
- **Type**: typing.Optional[datetime.datetime]

### recording
- **Type**: typing.Optional[bool]

### lastStatus
- **Type**: typing.Optional[typing.Literal['Failure', 'NotApplicable', 'Pending', 'Success']]

### lastErrorCode
- **Type**: typing.Optional[str]

### lastErrorMessage
- **Type**: typing.Optional[str]

### lastStatusChangeTime
- **Type**: typing.Optional[datetime.datetime]

### servicePrincipal
- **Type**: typing.Optional[str]


# ConfigurationRecorderSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### recordingScope
- **Type**: typing.Literal['INTERNAL', 'PAID']
- **Required**: Yes

### servicePrincipal
- **Type**: typing.Optional[str]


# ConfigurationRecorderTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### roleARN
- **Type**: typing.Optional[str]

### recordingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.RecordingGroupTypeDef]

### recordingMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.RecordingModeTypeDef]

### recordingScope
- **Type**: typing.Optional[typing.Literal['INTERNAL', 'PAID']]

### servicePrincipal
- **Type**: typing.Optional[str]


# ConfigurationRecorderUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConformancePackComplianceFiltersTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]


# ConformancePackComplianceScoreTypeDef

### Score
- **Type**: typing.Optional[str]

### ConformancePackName
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ConformancePackComplianceScoresFiltersTypeDef

### ConformancePackNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ConformancePackComplianceSummaryTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackComplianceStatus
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']
- **Required**: Yes


# ConformancePackDetailTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackId
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryS3Bucket
- **Type**: typing.Optional[str]

### DeliveryS3KeyPrefix
- **Type**: typing.Optional[str]

### ConformancePackInputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackInputParameterTypeDef]]

### LastUpdateRequestedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]

### TemplateSSMDocumentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TemplateSSMDocumentDetailsTypeDef]


# ConformancePackEvaluationFiltersTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ConformancePackEvaluationResultTypeDef

### ComplianceType
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']
- **Required**: Yes

### EvaluationResultIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.EvaluationResultIdentifierTypeDef'>
- **Required**: Yes

### ConfigRuleInvokedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResultRecordedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Annotation
- **Type**: typing.Optional[str]


# ConformancePackInputParameterTypeDef

### ParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConformancePackRuleComplianceTypeDef

### ConfigRuleName
- **Type**: typing.Optional[str]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### Controls
- **Type**: typing.Optional[typing.List[str]]


# ConformancePackStatusDetailTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackId
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackState
- **Type**: typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### StackArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdateRequestedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ConformancePackStatusReason
- **Type**: typing.Optional[str]

### LastUpdateCompletedTime
- **Type**: typing.Optional[datetime.datetime]


# CustomPolicyDetailsTypeDef

### PolicyRuntime
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### EnableDebugLogDelivery
- **Type**: typing.Optional[bool]


# DeleteAggregationAuthorizationRequestTypeDef

### AuthorizedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedAwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigRuleRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationAggregatorRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationRecorderRequestTypeDef

### ConfigurationRecorderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConformancePackRequestTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryChannelRequestTypeDef

### DeliveryChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEvaluationResultsRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOrganizationConfigRuleRequestTypeDef

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOrganizationConformancePackRequestTypeDef

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePendingAggregationRequestRequestTypeDef

### RequesterAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RequesterAwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRemediationConfigurationRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]


# DeleteRemediationExceptionsRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.config_classes.RemediationExceptionResourceKeyTypeDef]
- **Required**: Yes


# DeleteRemediationExceptionsResponseTypeDef

### FailedBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.FailedDeleteRemediationExceptionsBatchTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourceConfigRequestTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetentionConfigurationRequestTypeDef

### RetentionConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedConfigurationRecorderRequestTypeDef

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedConfigurationRecorderResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStoredQueryRequestTypeDef

### QueryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverConfigSnapshotRequestTypeDef

### deliveryChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverConfigSnapshotResponseTypeDef

### configSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeliveryChannelStatusTypeDef

### name
- **Type**: typing.Optional[str]

### configSnapshotDeliveryInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConfigExportDeliveryInfoTypeDef]

### configHistoryDeliveryInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConfigExportDeliveryInfoTypeDef]

### configStreamDeliveryInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConfigStreamDeliveryInfoTypeDef]


# DeliveryChannelTypeDef

### name
- **Type**: typing.Optional[str]

### s3BucketName
- **Type**: typing.Optional[str]

### s3KeyPrefix
- **Type**: typing.Optional[str]

### s3KmsKeyArn
- **Type**: typing.Optional[str]

### snsTopicARN
- **Type**: typing.Optional[str]

### configSnapshotDeliveryProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConfigSnapshotDeliveryPropertiesTypeDef]


# DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConfigRuleComplianceFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeAggregateComplianceByConfigRulesRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConfigRuleComplianceFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregateComplianceByConfigRulesResponseTypeDef

### AggregateComplianceByConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregateComplianceByConfigRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregateConformancePackComplianceFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeAggregateComplianceByConformancePacksRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregateConformancePackComplianceFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregateComplianceByConformancePacksResponseTypeDef

### AggregateComplianceByConformancePacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregateComplianceByConformancePackTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregationAuthorizationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeAggregationAuthorizationsRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregationAuthorizationsResponseTypeDef

### AggregationAuthorizations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregationAuthorizationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByConfigRuleRequestPaginateTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeComplianceByConfigRuleRequestTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByConfigRuleResponseTypeDef

### ComplianceByConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ComplianceByConfigRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByResourceRequestPaginateTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeComplianceByResourceRequestTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByResourceResponseTypeDef

### ComplianceByResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ComplianceByResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeConfigRuleEvaluationStatusRequestTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeConfigRuleEvaluationStatusResponseTypeDef

### ConfigRulesEvaluationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConfigRuleEvaluationStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigRulesFiltersTypeDef

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]


# DescribeConfigRulesRequestPaginateTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.DescribeConfigRulesFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeConfigRulesRequestTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.DescribeConfigRulesFiltersTypeDef]


# DescribeConfigRulesResponseTypeDef

### ConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConfigRuleOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'OUTDATED', 'SUCCEEDED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeConfigurationAggregatorSourcesStatusRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FAILED', 'OUTDATED', 'SUCCEEDED']]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeConfigurationAggregatorSourcesStatusResponseTypeDef

### AggregatedSourceStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregatedSourceStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationAggregatorsRequestPaginateTypeDef

### ConfigurationAggregatorNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeConfigurationAggregatorsRequestTypeDef

### ConfigurationAggregatorNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeConfigurationAggregatorsResponseTypeDef

### ConfigurationAggregators
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConfigurationAggregatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationRecorderStatusRequestTypeDef

### ConfigurationRecorderNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ServicePrincipal
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# DescribeConfigurationRecorderStatusResponseTypeDef

### ConfigurationRecordersStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConfigurationRecordersRequestTypeDef

### ConfigurationRecorderNames
- **Type**: typing.Optional[typing.Sequence[str]]

### ServicePrincipal
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# DescribeConfigurationRecordersResponseTypeDef

### ConfigurationRecorders
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConformancePackComplianceRequestTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConformancePackComplianceFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePackComplianceResponseTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackRuleComplianceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackRuleComplianceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePackStatusRequestPaginateTypeDef

### ConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeConformancePackStatusRequestTypeDef

### ConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePackStatusResponseTypeDef

### ConformancePackStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackStatusDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePacksRequestPaginateTypeDef

### ConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeConformancePacksRequestTypeDef

### ConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePacksResponseTypeDef

### ConformancePackDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDeliveryChannelStatusRequestTypeDef

### DeliveryChannelNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeDeliveryChannelStatusResponseTypeDef

### DeliveryChannelsStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.DeliveryChannelStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeliveryChannelsRequestTypeDef

### DeliveryChannelNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeDeliveryChannelsResponseTypeDef

### DeliveryChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.DeliveryChannelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeOrganizationConfigRuleStatusesRequestTypeDef

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigRuleStatusesResponseTypeDef

### OrganizationConfigRuleStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.OrganizationConfigRuleStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigRulesRequestPaginateTypeDef

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeOrganizationConfigRulesRequestTypeDef

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigRulesResponseTypeDef

### OrganizationConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.OrganizationConfigRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeOrganizationConformancePackStatusesRequestTypeDef

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePackStatusesResponseTypeDef

### OrganizationConformancePackStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.OrganizationConformancePackStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePacksRequestPaginateTypeDef

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeOrganizationConformancePacksRequestTypeDef

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePacksResponseTypeDef

### OrganizationConformancePacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.OrganizationConformancePackTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePendingAggregationRequestsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribePendingAggregationRequestsRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePendingAggregationRequestsResponseTypeDef

### PendingAggregationRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.PendingAggregationRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationConfigurationsRequestTypeDef

### ConfigRuleNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeRemediationConfigurationsResponseTypeDef

### RemediationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.RemediationConfigurationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRemediationExceptionsRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.RemediationExceptionResourceKeyTypeDef]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationExceptionsResponseTypeDef

### RemediationExceptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.RemediationExceptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationExecutionStatusRequestPaginateTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ResourceKeyTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeRemediationExecutionStatusRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ResourceKeyTypeDef]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationExecutionStatusResponseTypeDef

### RemediationExecutionStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.RemediationExecutionStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRetentionConfigurationsRequestPaginateTypeDef

### RetentionConfigurationNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# DescribeRetentionConfigurationsRequestTypeDef

### RetentionConfigurationNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRetentionConfigurationsResponseTypeDef

### RetentionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.RetentionConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateResourceTypesRequestTypeDef

### ConfigurationRecorderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.Sequence[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes


# DisassociateResourceTypesResponseTypeDef

### ConfigurationRecorder
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluationContextTypeDef

### EvaluationContextIdentifier
- **Type**: typing.Optional[str]


# EvaluationModeConfigurationTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]


# EvaluationOutputTypeDef

### ComplianceResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceType
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']
- **Required**: Yes

### OrderingTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Annotation
- **Type**: typing.Optional[str]


# EvaluationResultIdentifierTypeDef

### EvaluationResultQualifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.EvaluationResultQualifierTypeDef]

### OrderingTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ResourceEvaluationId
- **Type**: typing.Optional[str]


# EvaluationResultQualifierTypeDef

### ConfigRuleName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]


# EvaluationResultTypeDef

### EvaluationResultIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.EvaluationResultIdentifierTypeDef]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### ResultRecordedTime
- **Type**: typing.Optional[datetime.datetime]

### ConfigRuleInvokedTime
- **Type**: typing.Optional[datetime.datetime]

### Annotation
- **Type**: typing.Optional[str]

### ResultToken
- **Type**: typing.Optional[str]


# EvaluationStatusTypeDef

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# EvaluationTypeDef

### ComplianceResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceType
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']
- **Required**: Yes

### OrderingTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef'>
- **Required**: Yes

### Annotation
- **Type**: typing.Optional[str]


# EvaluationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExclusionByResourceTypesOutputTypeDef

### resourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]


# ExclusionByResourceTypesTypeDef

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]


# ExecutionControlsTypeDef

### SsmControls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.SsmControlsTypeDef]


# ExternalEvaluationTypeDef

### ComplianceResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceType
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']
- **Required**: Yes

### OrderingTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef'>
- **Required**: Yes

### Annotation
- **Type**: typing.Optional[str]


# FailedDeleteRemediationExceptionsBatchTypeDef

### FailureMessage
- **Type**: typing.Optional[str]

### FailedItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.RemediationExceptionResourceKeyTypeDef]]


# FailedRemediationBatchTypeDef

### FailureMessage
- **Type**: typing.Optional[str]

### FailedItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.RemediationConfigurationOutputTypeDef]]


# FailedRemediationExceptionBatchTypeDef

### FailureMessage
- **Type**: typing.Optional[str]

### FailedItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.RemediationExceptionTypeDef]]


# FieldInfoTypeDef

### Name
- **Type**: typing.Optional[str]


# GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# GetAggregateComplianceDetailsByConfigRuleRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateComplianceDetailsByConfigRuleResponseTypeDef

### AggregateEvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregateEvaluationResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConfigRuleComplianceSummaryRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConfigRuleComplianceSummaryFiltersTypeDef]

### GroupByKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AWS_REGION']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConfigRuleComplianceSummaryResponseTypeDef

### GroupByKey
- **Type**: <class 'str'>
- **Required**: Yes

### AggregateComplianceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregateComplianceCountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConformancePackComplianceSummaryRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregateConformancePackComplianceSummaryFiltersTypeDef]

### GroupByKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AWS_REGION']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConformancePackComplianceSummaryResponseTypeDef

### AggregateConformancePackComplianceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregateConformancePackComplianceSummaryTypeDef]
- **Required**: Yes

### GroupByKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateDiscoveredResourceCountsRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceCountFiltersTypeDef]

### GroupByKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AWS_REGION', 'RESOURCE_TYPE']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateDiscoveredResourceCountsResponseTypeDef

### TotalDiscoveredResources
- **Type**: <class 'int'>
- **Required**: Yes

### GroupByKey
- **Type**: <class 'str'>
- **Required**: Yes

### GroupedResourceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.GroupedResourceCountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateResourceConfigRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.AggregateResourceIdentifierTypeDef'>
- **Required**: Yes


# GetAggregateResourceConfigResponseTypeDef

### ConfigurationItem
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ConfigurationItemTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComplianceDetailsByConfigRuleRequestPaginateTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# GetComplianceDetailsByConfigRuleRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetComplianceDetailsByConfigRuleResponseTypeDef

### EvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.EvaluationResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetComplianceDetailsByResourceRequestPaginateTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### ResourceEvaluationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# GetComplianceDetailsByResourceRequestTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### NextToken
- **Type**: typing.Optional[str]

### ResourceEvaluationId
- **Type**: typing.Optional[str]


# GetComplianceDetailsByResourceResponseTypeDef

### EvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.EvaluationResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetComplianceSummaryByConfigRuleResponseTypeDef

### ComplianceSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ComplianceSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetComplianceSummaryByResourceTypeRequestTypeDef

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# GetComplianceSummaryByResourceTypeResponseTypeDef

### ComplianceSummariesByResourceType
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ComplianceSummaryByResourceTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConformancePackComplianceDetailsRequestTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConformancePackEvaluationFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetConformancePackComplianceDetailsResponseTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackRuleEvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackEvaluationResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetConformancePackComplianceSummaryRequestPaginateTypeDef

### ConformancePackNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# GetConformancePackComplianceSummaryRequestTypeDef

### ConformancePackNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetConformancePackComplianceSummaryResponseTypeDef

### ConformancePackComplianceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackComplianceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCustomRulePolicyRequestTypeDef

### ConfigRuleName
- **Type**: typing.Optional[str]


# GetCustomRulePolicyResponseTypeDef

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDiscoveredResourceCountsRequestTypeDef

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetDiscoveredResourceCountsResponseTypeDef

### totalDiscoveredResources
- **Type**: <class 'int'>
- **Required**: Yes

### resourceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ResourceCountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.StatusDetailFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# GetOrganizationConfigRuleDetailedStatusRequestTypeDef

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.StatusDetailFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationConfigRuleDetailedStatusResponseTypeDef

### OrganizationConfigRuleDetailedStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.MemberAccountStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationResourceDetailedStatusFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# GetOrganizationConformancePackDetailedStatusRequestTypeDef

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationResourceDetailedStatusFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationConformancePackDetailedStatusResponseTypeDef

### OrganizationConformancePackDetailedStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.OrganizationConformancePackDetailedStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationCustomRulePolicyRequestTypeDef

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrganizationCustomRulePolicyResponseTypeDef

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceConfigHistoryRequestPaginateTypeDef

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### laterTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef]

### earlierTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef]

### chronologicalOrder
- **Type**: typing.Optional[typing.Literal['Forward', 'Reverse']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# GetResourceConfigHistoryRequestTypeDef

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### laterTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef]

### earlierTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef]

### chronologicalOrder
- **Type**: typing.Optional[typing.Literal['Forward', 'Reverse']]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetResourceConfigHistoryResponseTypeDef

### configurationItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConfigurationItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceEvaluationSummaryRequestTypeDef

### ResourceEvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceEvaluationSummaryResponseTypeDef

### ResourceEvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationMode
- **Type**: typing.Literal['DETECTIVE', 'PROACTIVE']
- **Required**: Yes

### EvaluationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.EvaluationStatusTypeDef'>
- **Required**: Yes

### EvaluationStartTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Compliance
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']
- **Required**: Yes

### EvaluationContext
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.EvaluationContextTypeDef'>
- **Required**: Yes

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResourceDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStoredQueryRequestTypeDef

### QueryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStoredQueryResponseTypeDef

### StoredQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.StoredQueryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupedResourceCountTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceCount
- **Type**: <class 'int'>
- **Required**: Yes


# ListAggregateDiscoveredResourcesRequestPaginateTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# ListAggregateDiscoveredResourcesRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAggregateDiscoveredResourcesResponseTypeDef

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.AggregateResourceIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRecordersRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# ListConfigurationRecordersRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRecordersResponseTypeDef

### ConfigurationRecorderSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConformancePackComplianceScoresRequestTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ConformancePackComplianceScoresFiltersTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['SCORE']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConformancePackComplianceScoresResponseTypeDef

### ConformancePackComplianceScores
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackComplianceScoreTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesRequestPaginateTypeDef

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceName
- **Type**: typing.Optional[str]

### includeDeletedResources
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# ListDiscoveredResourcesRequestTypeDef

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceName
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### includeDeletedResources
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesResponseTypeDef

### resourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ResourceIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceEvaluationsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceEvaluationFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# ListResourceEvaluationsRequestTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceEvaluationFiltersTypeDef]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceEvaluationsResponseTypeDef

### ResourceEvaluations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ResourceEvaluationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStoredQueriesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStoredQueriesResponseTypeDef

### StoredQueryMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.StoredQueryMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberAccountStatusTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberAccountRuleStatus
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# OrganizationAggregationSourceOutputTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegions
- **Type**: typing.Optional[typing.List[str]]

### AllAwsRegions
- **Type**: typing.Optional[bool]


# OrganizationAggregationSourceTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegions
- **Type**: typing.Optional[typing.Sequence[str]]

### AllAwsRegions
- **Type**: typing.Optional[bool]


# OrganizationAggregationSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationConfigRuleStatusTypeDef

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationRuleStatus
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# OrganizationConfigRuleTypeDef

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationConfigRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationManagedRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationManagedRuleMetadataOutputTypeDef]

### OrganizationCustomRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationCustomRuleMetadataOutputTypeDef]

### ExcludedAccounts
- **Type**: typing.Optional[typing.List[str]]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### OrganizationCustomPolicyRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef]


# OrganizationConformancePackDetailedStatusTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# OrganizationConformancePackStatusTypeDef

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']
- **Required**: Yes

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# OrganizationConformancePackTypeDef

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationConformancePackArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeliveryS3Bucket
- **Type**: typing.Optional[str]

### DeliveryS3KeyPrefix
- **Type**: typing.Optional[str]

### ConformancePackInputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.ConformancePackInputParameterTypeDef]]

### ExcludedAccounts
- **Type**: typing.Optional[typing.List[str]]


# OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef

### Description
- **Type**: typing.Optional[str]

### OrganizationConfigRuleTriggerTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ConfigurationItemChangeNotification', 'OversizedConfigurationItemChangeNotification']]]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ResourceTypesScope
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdScope
- **Type**: typing.Optional[str]

### TagKeyScope
- **Type**: typing.Optional[str]

### TagValueScope
- **Type**: typing.Optional[str]

### PolicyRuntime
- **Type**: typing.Optional[str]

### DebugLogDeliveryAccounts
- **Type**: typing.Optional[typing.List[str]]


# OrganizationCustomPolicyRuleMetadataTypeDef

### PolicyRuntime
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OrganizationConfigRuleTriggerTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ConfigurationItemChangeNotification', 'OversizedConfigurationItemChangeNotification']]]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ResourceTypesScope
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceIdScope
- **Type**: typing.Optional[str]

### TagKeyScope
- **Type**: typing.Optional[str]

### TagValueScope
- **Type**: typing.Optional[str]

### DebugLogDeliveryAccounts
- **Type**: typing.Optional[typing.Sequence[str]]


# OrganizationCustomRuleMetadataOutputTypeDef

### LambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationConfigRuleTriggerTypes
- **Type**: typing.List[typing.Literal['ConfigurationItemChangeNotification', 'OversizedConfigurationItemChangeNotification', 'ScheduledNotification']]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ResourceTypesScope
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdScope
- **Type**: typing.Optional[str]

### TagKeyScope
- **Type**: typing.Optional[str]

### TagValueScope
- **Type**: typing.Optional[str]


# OrganizationCustomRuleMetadataTypeDef

### LambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationConfigRuleTriggerTypes
- **Type**: typing.Sequence[typing.Literal['ConfigurationItemChangeNotification', 'OversizedConfigurationItemChangeNotification', 'ScheduledNotification']]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ResourceTypesScope
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceIdScope
- **Type**: typing.Optional[str]

### TagKeyScope
- **Type**: typing.Optional[str]

### TagValueScope
- **Type**: typing.Optional[str]


# OrganizationCustomRuleMetadataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationManagedRuleMetadataOutputTypeDef

### RuleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ResourceTypesScope
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdScope
- **Type**: typing.Optional[str]

### TagKeyScope
- **Type**: typing.Optional[str]

### TagValueScope
- **Type**: typing.Optional[str]


# OrganizationManagedRuleMetadataTypeDef

### RuleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ResourceTypesScope
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceIdScope
- **Type**: typing.Optional[str]

### TagKeyScope
- **Type**: typing.Optional[str]

### TagValueScope
- **Type**: typing.Optional[str]


# OrganizationManagedRuleMetadataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationResourceDetailedStatusFiltersTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingAggregationRequestTypeDef

### RequesterAccountId
- **Type**: typing.Optional[str]

### RequesterAwsRegion
- **Type**: typing.Optional[str]


# PutAggregationAuthorizationRequestTypeDef

### AuthorizedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedAwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]]


# PutAggregationAuthorizationResponseTypeDef

### AggregationAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.AggregationAuthorizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutConfigRuleRequestTypeDef

### ConfigRule
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ConfigRuleUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]]


# PutConfigurationAggregatorRequestTypeDef

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountAggregationSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.AccountAggregationSourceUnionTypeDef]]

### OrganizationAggregationSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationAggregationSourceUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]]

### AggregatorFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.AggregatorFiltersUnionTypeDef]


# PutConfigurationAggregatorResponseTypeDef

### ConfigurationAggregator
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ConfigurationAggregatorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutConfigurationRecorderRequestTypeDef

### ConfigurationRecorder
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ConfigurationRecorderUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]]


# PutConformancePackRequestTypeDef

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateS3Uri
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### DeliveryS3Bucket
- **Type**: typing.Optional[str]

### DeliveryS3KeyPrefix
- **Type**: typing.Optional[str]

### ConformancePackInputParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ConformancePackInputParameterTypeDef]]

### TemplateSSMDocumentDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TemplateSSMDocumentDetailsTypeDef]


# PutConformancePackResponseTypeDef

### ConformancePackArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDeliveryChannelRequestTypeDef

### DeliveryChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.DeliveryChannelTypeDef'>
- **Required**: Yes


# PutEvaluationsRequestTypeDef

### ResultToken
- **Type**: <class 'str'>
- **Required**: Yes

### Evaluations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.EvaluationUnionTypeDef]]

### TestMode
- **Type**: typing.Optional[bool]


# PutEvaluationsResponseTypeDef

### FailedEvaluations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.EvaluationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutExternalEvaluationRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalEvaluation
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ExternalEvaluationTypeDef'>
- **Required**: Yes


# PutOrganizationConfigRuleRequestTypeDef

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationManagedRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationManagedRuleMetadataUnionTypeDef]

### OrganizationCustomRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationCustomRuleMetadataUnionTypeDef]

### ExcludedAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationCustomPolicyRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.OrganizationCustomPolicyRuleMetadataTypeDef]


# PutOrganizationConfigRuleResponseTypeDef

### OrganizationConfigRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutOrganizationConformancePackRequestTypeDef

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateS3Uri
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### DeliveryS3Bucket
- **Type**: typing.Optional[str]

### DeliveryS3KeyPrefix
- **Type**: typing.Optional[str]

### ConformancePackInputParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ConformancePackInputParameterTypeDef]]

### ExcludedAccounts
- **Type**: typing.Optional[typing.Sequence[str]]


# PutOrganizationConformancePackResponseTypeDef

### OrganizationConformancePackArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRemediationConfigurationsRequestTypeDef

### RemediationConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.config_classes.RemediationConfigurationUnionTypeDef]
- **Required**: Yes


# PutRemediationConfigurationsResponseTypeDef

### FailedBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.FailedRemediationBatchTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRemediationExceptionsRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.config_classes.RemediationExceptionResourceKeyTypeDef]
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]

### ExpirationTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef]


# PutRemediationExceptionsResponseTypeDef

### FailedBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.FailedRemediationExceptionBatchTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourceConfigRequestTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutRetentionConfigurationRequestTypeDef

### RetentionPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes


# PutRetentionConfigurationResponseTypeDef

### RetentionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.RetentionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutServiceLinkedConfigurationRecorderRequestTypeDef

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]]


# PutServiceLinkedConfigurationRecorderResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutStoredQueryRequestTypeDef

### StoredQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.StoredQueryTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]]


# PutStoredQueryResponseTypeDef

### QueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryInfoTypeDef

### SelectFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.FieldInfoTypeDef]]


# RecordingGroupOutputTypeDef

### allSupported
- **Type**: typing.Optional[bool]

### includeGlobalResourceTypes
- **Type**: typing.Optional[bool]

### resourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]

### exclusionByResourceTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ExclusionByResourceTypesOutputTypeDef]

### recordingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.RecordingStrategyTypeDef]


# RecordingGroupTypeDef

### allSupported
- **Type**: typing.Optional[bool]

### includeGlobalResourceTypes
- **Type**: typing.Optional[bool]

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]

### exclusionByResourceTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ExclusionByResourceTypesTypeDef]

### recordingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.RecordingStrategyTypeDef]


# RecordingModeOutputTypeDef

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### recordingModeOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.RecordingModeOverrideOutputTypeDef]]


# RecordingModeOverrideOutputTypeDef

### resourceTypes
- **Type**: typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# RecordingModeOverrideTypeDef

### resourceTypes
- **Type**: typing.Sequence[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# RecordingModeTypeDef

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### recordingModeOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.RecordingModeOverrideTypeDef]]


# RecordingStrategyTypeDef

### useOnly
- **Type**: typing.Optional[typing.Literal['ALL_SUPPORTED_RESOURCE_TYPES', 'EXCLUSION_BY_RESOURCE_TYPES', 'INCLUSION_BY_RESOURCE_TYPES']]


# RelationshipTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### resourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### relationshipName
- **Type**: typing.Optional[str]


# RemediationConfigurationOutputTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['SSM_DOCUMENT']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.config_classes.RemediationParameterValueOutputTypeDef]]

### ResourceType
- **Type**: typing.Optional[str]

### Automatic
- **Type**: typing.Optional[bool]

### ExecutionControls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ExecutionControlsTypeDef]

### MaximumAutomaticAttempts
- **Type**: typing.Optional[int]

### RetryAttemptSeconds
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### CreatedByService
- **Type**: typing.Optional[str]


# RemediationConfigurationTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['SSM_DOCUMENT']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.config_classes.RemediationParameterValueUnionTypeDef]]

### ResourceType
- **Type**: typing.Optional[str]

### Automatic
- **Type**: typing.Optional[bool]

### ExecutionControls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ExecutionControlsTypeDef]

### MaximumAutomaticAttempts
- **Type**: typing.Optional[int]

### RetryAttemptSeconds
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### CreatedByService
- **Type**: typing.Optional[str]


# RemediationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemediationExceptionResourceKeyTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]


# RemediationExceptionTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]

### ExpirationTime
- **Type**: typing.Optional[datetime.datetime]


# RemediationExecutionStatusTypeDef

### ResourceKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceKeyTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']]

### StepDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.RemediationExecutionStepTypeDef]]

### InvocationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# RemediationExecutionStepTypeDef

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### ErrorMessage
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### StopTime
- **Type**: typing.Optional[datetime.datetime]


# RemediationParameterValueOutputTypeDef

### ResourceValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceValueTypeDef]

### StaticValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.StaticValueOutputTypeDef]


# RemediationParameterValueTypeDef

### ResourceValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.ResourceValueTypeDef]

### StaticValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.StaticValueUnionTypeDef]


# RemediationParameterValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceCountFiltersTypeDef

### ResourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### AccountId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# ResourceCountTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### count
- **Type**: typing.Optional[int]


# ResourceDetailsTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfigurationSchemaType
- **Type**: typing.Optional[typing.Literal['CFN_RESOURCE_SCHEMA']]


# ResourceEvaluationFiltersTypeDef

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]

### TimeWindow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimeWindowTypeDef]

### EvaluationContextIdentifier
- **Type**: typing.Optional[str]


# ResourceEvaluationTypeDef

### ResourceEvaluationId
- **Type**: typing.Optional[str]

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]

### EvaluationStartTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ResourceFiltersTypeDef

### AccountId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# ResourceIdentifierTypeDef

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### resourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### resourceDeletionTime
- **Type**: typing.Optional[datetime.datetime]


# ResourceKeyTypeDef

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceValueTypeDef

### Value
- **Type**: typing.Literal['RESOURCE_ID']
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RetentionConfigurationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes


# ScopeOutputTypeDef

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### ComplianceResourceId
- **Type**: typing.Optional[str]


# ScopeTypeDef

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### ComplianceResourceId
- **Type**: typing.Optional[str]


# SelectAggregateResourceConfigRequestPaginateTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# SelectAggregateResourceConfigRequestTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SelectAggregateResourceConfigResponseTypeDef

### Results
- **Type**: typing.List[str]
- **Required**: Yes

### QueryInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.QueryInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SelectResourceConfigRequestPaginateTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.PaginatorConfigTypeDef]


# SelectResourceConfigRequestTypeDef

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SelectResourceConfigResponseTypeDef

### Results
- **Type**: typing.List[str]
- **Required**: Yes

### QueryInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.QueryInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SourceDetailTypeDef

### EventSource
- **Type**: typing.Optional[typing.Literal['aws.config']]

### MessageType
- **Type**: typing.Optional[typing.Literal['ConfigurationItemChangeNotification', 'ConfigurationSnapshotDeliveryCompleted', 'OversizedConfigurationItemChangeNotification', 'ScheduledNotification']]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]


# SourceOutputTypeDef

### Owner
- **Type**: typing.Literal['AWS', 'CUSTOM_LAMBDA', 'CUSTOM_POLICY']
- **Required**: Yes

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config_classes.SourceDetailTypeDef]]

### CustomPolicyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.CustomPolicyDetailsTypeDef]


# SourceTypeDef

### Owner
- **Type**: typing.Literal['AWS', 'CUSTOM_LAMBDA', 'CUSTOM_POLICY']
- **Required**: Yes

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceDetails
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.config_classes.SourceDetailTypeDef]]

### CustomPolicyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.CustomPolicyDetailsTypeDef]


# SsmControlsTypeDef

### ConcurrentExecutionRatePercentage
- **Type**: typing.Optional[int]

### ErrorPercentage
- **Type**: typing.Optional[int]


# StartConfigRulesEvaluationRequestTypeDef

### ConfigRuleNames
- **Type**: typing.Optional[typing.Sequence[str]]


# StartConfigurationRecorderRequestTypeDef

### ConfigurationRecorderName
- **Type**: <class 'str'>
- **Required**: Yes


# StartRemediationExecutionRequestTypeDef

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.config_classes.ResourceKeyTypeDef]
- **Required**: Yes


# StartRemediationExecutionResponseTypeDef

### FailureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### FailedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config_classes.ResourceKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartResourceEvaluationRequestTypeDef

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResourceDetailsTypeDef'>
- **Required**: Yes

### EvaluationMode
- **Type**: typing.Literal['DETECTIVE', 'PROACTIVE']
- **Required**: Yes

### EvaluationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.EvaluationContextTypeDef]

### EvaluationTimeout
- **Type**: typing.Optional[int]

### ClientToken
- **Type**: typing.Optional[str]


# StartResourceEvaluationResponseTypeDef

### ResourceEvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StaticValueOutputTypeDef

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# StaticValueTypeDef

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# StaticValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatusDetailFiltersTypeDef

### AccountId
- **Type**: typing.Optional[str]

### MemberAccountRuleStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]


# StopConfigurationRecorderRequestTypeDef

### ConfigurationRecorderName
- **Type**: <class 'str'>
- **Required**: Yes


# StoredQueryMetadataTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### QueryName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# StoredQueryTypeDef

### QueryName
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: typing.Optional[str]

### QueryArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Expression
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.config_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TemplateSSMDocumentDetailsTypeDef

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]


# TimeWindowTypeDef

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config_classes.TimestampTypeDef]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


