# Config Classes

# AccountAggregationSource

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### AllAwsRegions
- **Type**: typing.Optional[bool]

### AwsRegions
- **Type**: typing.Optional[typing.List[str]]


# AccountAggregationSourceOutput

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### AllAwsRegions
- **Type**: typing.Optional[bool]

### AwsRegions
- **Type**: typing.Optional[typing.List[str]]


# AggregateComplianceByConfigRule

### ConfigRuleName
- **Type**: typing.Optional[str]

### Compliance
- **Type**: <class 'NoneType'>

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateComplianceByConformancePack

### ConformancePackName
- **Type**: typing.Optional[str]

### Compliance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregateConformancePackCompliance]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateComplianceCount

### GroupName
- **Type**: typing.Optional[str]

### ComplianceSummary
- **Type**: <class 'NoneType'>


# AggregateConformancePackCompliance

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### CompliantRuleCount
- **Type**: typing.Optional[int]

### NonCompliantRuleCount
- **Type**: typing.Optional[int]

### TotalRuleCount
- **Type**: typing.Optional[int]


# AggregateConformancePackComplianceCount

### CompliantConformancePackCount
- **Type**: typing.Optional[int]

### NonCompliantConformancePackCount
- **Type**: typing.Optional[int]


# AggregateConformancePackComplianceFilters

### ConformancePackName
- **Type**: typing.Optional[str]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateConformancePackComplianceSummary

### ComplianceSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregateConformancePackComplianceCount]

### GroupName
- **Type**: typing.Optional[str]


# AggregateConformancePackComplianceSummaryFilters

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# AggregateEvaluationResult

### EvaluationResultIdentifier
- **Type**: <class 'NoneType'>

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


# AggregateResourceIdentifier

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


# AggregatedSourceStatus

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


# AggregationAuthorization

### AggregationAuthorizationArn
- **Type**: typing.Optional[str]

### AuthorizedAccountId
- **Type**: typing.Optional[str]

### AuthorizedAwsRegion
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# AggregatorFilterResourceType

### Type
- **Type**: typing.Optional[typing.Literal['INCLUDE']]

### Value
- **Type**: typing.Optional[typing.List[str]]


# AggregatorFilterResourceTypeOutput

### Type
- **Type**: typing.Optional[typing.Literal['INCLUDE']]

### Value
- **Type**: typing.Optional[typing.List[str]]


# AggregatorFilterServicePrincipal

### Type
- **Type**: typing.Optional[typing.Literal['INCLUDE']]

### Value
- **Type**: typing.Optional[typing.List[str]]


# AggregatorFilterServicePrincipalOutput

### Type
- **Type**: typing.Optional[typing.Literal['INCLUDE']]

### Value
- **Type**: typing.Optional[typing.List[str]]


# AggregatorFilters

### ResourceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregatorFilterResourceType]

### ServicePrincipal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregatorFilterServicePrincipal]


# AggregatorFiltersOutput

### ResourceType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregatorFilterResourceTypeOutput]

### ServicePrincipal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregatorFilterServicePrincipalOutput]


# AssociateResourceTypesRequest

### ConfigurationRecorderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes


# AssociateResourceTypesResponse

### ConfigurationRecorder
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# BaseConfigurationItem

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

# BatchGetAggregateResourceConfigRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateResourceIdentifier]
- **Required**: Yes


# BatchGetAggregateResourceConfigResponse

### BaseConfigurationItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.BaseConfigurationItem]
- **Required**: Yes

### UnprocessedResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateResourceIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetResourceConfigRequest

### resourceKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceKey]
- **Required**: Yes


# BatchGetResourceConfigResponse

### baseConfigurationItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.BaseConfigurationItem]
- **Required**: Yes

### unprocessedResourceKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# Compliance

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### ComplianceContributorCount
- **Type**: <class 'NoneType'>


# ComplianceByConfigRule

### ConfigRuleName
- **Type**: typing.Optional[str]

### Compliance
- **Type**: <class 'NoneType'>


# ComplianceByResource

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Compliance
- **Type**: <class 'NoneType'>


# ComplianceContributorCount

### CappedCount
- **Type**: typing.Optional[int]

### CapExceeded
- **Type**: typing.Optional[bool]


# ComplianceSummary

### CompliantResourceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ComplianceContributorCount]

### NonCompliantResourceCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ComplianceContributorCount]

### ComplianceSummaryTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ComplianceSummaryByResourceType

### ResourceType
- **Type**: typing.Optional[str]

### ComplianceSummary
- **Type**: <class 'NoneType'>


# ConfigExportDeliveryInfo

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


# ConfigRule

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.Source'>
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
- **Type**: <class 'NoneType'>

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ConfigRuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'DELETING_RESULTS', 'EVALUATING']]

### CreatedBy
- **Type**: typing.Optional[str]

### EvaluationModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.EvaluationModeConfiguration]]


# ConfigRuleComplianceFilters

### ConfigRuleName
- **Type**: typing.Optional[str]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# ConfigRuleComplianceSummaryFilters

### AccountId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]


# ConfigRuleEvaluationStatus

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


# ConfigRuleOutput

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.SourceOutput'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ScopeOutput]

### InputParameters
- **Type**: typing.Optional[str]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]

### ConfigRuleState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'DELETING_RESULTS', 'EVALUATING']]

### CreatedBy
- **Type**: typing.Optional[str]

### EvaluationModes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.EvaluationModeConfiguration]]


# ConfigSnapshotDeliveryProperties

### deliveryFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]


# ConfigStreamDeliveryInfo

### lastStatus
- **Type**: typing.Optional[typing.Literal['Failure', 'Not_Applicable', 'Success']]

### lastErrorCode
- **Type**: typing.Optional[str]

### lastErrorMessage
- **Type**: typing.Optional[str]

### lastStatusChangeTime
- **Type**: typing.Optional[datetime.datetime]


# ConfigurationAggregator

### ConfigurationAggregatorName
- **Type**: typing.Optional[str]

### ConfigurationAggregatorArn
- **Type**: typing.Optional[str]

### AccountAggregationSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.AccountAggregationSourceOutput]]

### OrganizationAggregationSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.OrganizationAggregationSourceOutput]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]

### AggregatorFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregatorFiltersOutput]


# ConfigurationItem

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.Relationship]]

### configuration
- **Type**: typing.Optional[str]

### supplementaryConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### recordingFrequency
- **Type**: typing.Optional[typing.Literal['CONTINUOUS', 'DAILY']]

### configurationItemDeliveryTime
- **Type**: typing.Optional[datetime.datetime]


# ConfigurationRecorder

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### roleARN
- **Type**: typing.Optional[str]

### recordingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.RecordingGroup]

### recordingMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.RecordingMode]

### recordingScope
- **Type**: typing.Optional[typing.Literal['INTERNAL', 'PAID']]

### servicePrincipal
- **Type**: typing.Optional[str]


# ConfigurationRecorderFilter

### filterName
- **Type**: typing.Optional[typing.Literal['recordingScope']]

### filterValue
- **Type**: typing.Optional[typing.List[str]]


# ConfigurationRecorderOutput

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### roleARN
- **Type**: typing.Optional[str]

### recordingGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.RecordingGroupOutput]

### recordingMode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.RecordingModeOutput]

### recordingScope
- **Type**: typing.Optional[typing.Literal['INTERNAL', 'PAID']]

### servicePrincipal
- **Type**: typing.Optional[str]


# ConfigurationRecorderStatus

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


# ConfigurationRecorderSummary

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


# ConformancePackComplianceFilters

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]


# ConformancePackComplianceScore

### Score
- **Type**: typing.Optional[str]

### ConformancePackName
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ConformancePackComplianceScoresFilters

### ConformancePackNames
- **Type**: typing.List[str]
- **Required**: Yes


# ConformancePackComplianceSummary

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackComplianceStatus
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']
- **Required**: Yes


# ConformancePackDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackInputParameter]]

### LastUpdateRequestedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[str]

### TemplateSSMDocumentDetails
- **Type**: <class 'NoneType'>


# ConformancePackEvaluationFilters

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceIds
- **Type**: typing.Optional[typing.List[str]]


# ConformancePackEvaluationResult

### ComplianceType
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']
- **Required**: Yes

### EvaluationResultIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.EvaluationResultIdentifier'>
- **Required**: Yes

### ConfigRuleInvokedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResultRecordedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Annotation
- **Type**: typing.Optional[str]


# ConformancePackInputParameter

### ParameterName
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConformancePackRuleCompliance

### ConfigRuleName
- **Type**: typing.Optional[str]

### ComplianceType
- **Type**: typing.Optional[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT']]

### Controls
- **Type**: typing.Optional[typing.List[str]]


# ConformancePackStatusDetail

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


# CustomPolicyDetails

### PolicyRuntime
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### EnableDebugLogDelivery
- **Type**: typing.Optional[bool]


# DeleteAggregationAuthorizationRequest

### AuthorizedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedAwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigRuleRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationAggregatorRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationRecorderRequest

### ConfigurationRecorderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConformancePackRequest

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryChannelRequest

### DeliveryChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEvaluationResultsRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOrganizationConfigRuleRequest

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOrganizationConformancePackRequest

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePendingAggregationRequestRequest

### RequesterAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RequesterAwsRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRemediationConfigurationRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]


# DeleteRemediationExceptionsRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationExceptionResourceKey]
- **Required**: Yes


# DeleteRemediationExceptionsResponse

### FailedBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.FailedDeleteRemediationExceptionsBatch]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourceConfigRequest

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetentionConfigurationRequest

### RetentionConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedConfigurationRecorderRequest

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedConfigurationRecorderResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteStoredQueryRequest

### QueryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverConfigSnapshotRequest

### deliveryChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverConfigSnapshotResponse

### configSnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DeliveryChannel

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConfigSnapshotDeliveryProperties]


# DeliveryChannelStatus

### name
- **Type**: typing.Optional[str]

### configSnapshotDeliveryInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConfigExportDeliveryInfo]

### configHistoryDeliveryInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConfigExportDeliveryInfo]

### configStreamDeliveryInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConfigStreamDeliveryInfo]


# DescribeAggregateComplianceByConfigRulesRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConfigRuleComplianceFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregateComplianceByConfigRulesRequestPaginate

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConfigRuleComplianceFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeAggregateComplianceByConfigRulesResponse

### AggregateComplianceByConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateComplianceByConfigRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregateComplianceByConformancePacksRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregateConformancePackComplianceFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregateComplianceByConformancePacksRequestPaginate

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregateConformancePackComplianceFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeAggregateComplianceByConformancePacksResponse

### AggregateComplianceByConformancePacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateComplianceByConformancePack]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregationAuthorizationsRequest

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAggregationAuthorizationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeAggregationAuthorizationsResponse

### AggregationAuthorizations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregationAuthorization]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByConfigRuleRequest

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByConfigRuleRequestPaginate

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeComplianceByConfigRuleResponse

### ComplianceByConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ComplianceByConfigRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByResourceRequest

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeComplianceByResourceRequestPaginate

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeComplianceByResourceResponse

### ComplianceByResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ComplianceByResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigRuleEvaluationStatusRequest

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeConfigRuleEvaluationStatusRequestPaginate

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeConfigRuleEvaluationStatusResponse

### ConfigRulesEvaluationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigRuleEvaluationStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigRulesFilters

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]


# DescribeConfigRulesRequest

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.DescribeConfigRulesFilters]


# DescribeConfigRulesRequestPaginate

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.DescribeConfigRulesFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeConfigRulesResponse

### ConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigRuleOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationAggregatorSourcesStatusRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.List[typing.Literal['FAILED', 'OUTDATED', 'SUCCEEDED']]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeConfigurationAggregatorSourcesStatusRequestPaginate

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.List[typing.Literal['FAILED', 'OUTDATED', 'SUCCEEDED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeConfigurationAggregatorSourcesStatusResponse

### AggregatedSourceStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregatedSourceStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationAggregatorsRequest

### ConfigurationAggregatorNames
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeConfigurationAggregatorsRequestPaginate

### ConfigurationAggregatorNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeConfigurationAggregatorsResponse

### ConfigurationAggregators
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationAggregator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationRecorderStatusRequest

### ConfigurationRecorderNames
- **Type**: typing.Optional[typing.List[str]]

### ServicePrincipal
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# DescribeConfigurationRecorderStatusResponse

### ConfigurationRecordersStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConfigurationRecordersRequest

### ConfigurationRecorderNames
- **Type**: typing.Optional[typing.List[str]]

### ServicePrincipal
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# DescribeConfigurationRecordersResponse

### ConfigurationRecorders
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConformancePackComplianceRequest

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackComplianceFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePackComplianceResponse

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackRuleComplianceList
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackRuleCompliance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePackStatusRequest

### ConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePackStatusRequestPaginate

### ConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeConformancePackStatusResponse

### ConformancePackStatusDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackStatusDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePacksRequest

### ConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConformancePacksRequestPaginate

### ConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeConformancePacksResponse

### ConformancePackDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDeliveryChannelStatusRequest

### DeliveryChannelNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeDeliveryChannelStatusResponse

### DeliveryChannelsStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.DeliveryChannelStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeliveryChannelsRequest

### DeliveryChannelNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeDeliveryChannelsResponse

### DeliveryChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.DeliveryChannel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationConfigRuleStatusesRequest

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigRuleStatusesRequestPaginate

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeOrganizationConfigRuleStatusesResponse

### OrganizationConfigRuleStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.OrganizationConfigRuleStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigRulesRequest

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConfigRulesRequestPaginate

### OrganizationConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeOrganizationConfigRulesResponse

### OrganizationConfigRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.OrganizationConfigRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePackStatusesRequest

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePackStatusesRequestPaginate

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeOrganizationConformancePackStatusesResponse

### OrganizationConformancePackStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.OrganizationConformancePackStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePacksRequest

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeOrganizationConformancePacksRequestPaginate

### OrganizationConformancePackNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeOrganizationConformancePacksResponse

### OrganizationConformancePacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.OrganizationConformancePack]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribePendingAggregationRequestsRequest

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribePendingAggregationRequestsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribePendingAggregationRequestsResponse

### PendingAggregationRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.PendingAggregationRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationConfigurationsRequest

### ConfigRuleNames
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeRemediationConfigurationsResponse

### RemediationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationConfigurationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRemediationExceptionsRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationExceptionResourceKey]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationExceptionsResponse

### RemediationExceptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationException]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationExecutionStatusRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceKey]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRemediationExecutionStatusRequestPaginate

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceKey]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeRemediationExecutionStatusResponse

### RemediationExecutionStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationExecutionStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRetentionConfigurationsRequest

### RetentionConfigurationNames
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRetentionConfigurationsRequestPaginate

### RetentionConfigurationNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# DescribeRetentionConfigurationsResponse

### RetentionConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.RetentionConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateResourceTypesRequest

### ConfigurationRecorderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceTypes
- **Type**: typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes


# DisassociateResourceTypesResponse

### ConfigurationRecorder
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# Evaluation

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Annotation
- **Type**: typing.Optional[str]


# EvaluationContext

### EvaluationContextIdentifier
- **Type**: typing.Optional[str]


# EvaluationModeConfiguration

### Mode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]


# EvaluationOutput

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


# EvaluationResult

### EvaluationResultIdentifier
- **Type**: <class 'NoneType'>

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


# EvaluationResultIdentifier

### EvaluationResultQualifier
- **Type**: <class 'NoneType'>

### OrderingTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ResourceEvaluationId
- **Type**: typing.Optional[str]


# EvaluationResultQualifier

### ConfigRuleName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]


# EvaluationStatus

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# ExclusionByResourceTypes

### resourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]


# ExclusionByResourceTypesOutput

### resourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]


# ExecutionControls

### SsmControls
- **Type**: <class 'NoneType'>


# ExternalEvaluation

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Annotation
- **Type**: typing.Optional[str]


# FailedDeleteRemediationExceptionsBatch

### FailureMessage
- **Type**: typing.Optional[str]

### FailedItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationExceptionResourceKey]]


# FailedRemediationBatch

### FailureMessage
- **Type**: typing.Optional[str]

### FailedItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationConfigurationOutput]]


# FailedRemediationExceptionBatch

### FailureMessage
- **Type**: typing.Optional[str]

### FailedItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationException]]


# FieldInfo

### Name
- **Type**: typing.Optional[str]


# GetAggregateComplianceDetailsByConfigRuleRequest

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


# GetAggregateComplianceDetailsByConfigRuleRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# GetAggregateComplianceDetailsByConfigRuleResponse

### AggregateEvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateEvaluationResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConfigRuleComplianceSummaryRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConfigRuleComplianceSummaryFilters]

### GroupByKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AWS_REGION']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConfigRuleComplianceSummaryResponse

### GroupByKey
- **Type**: <class 'str'>
- **Required**: Yes

### AggregateComplianceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateComplianceCount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConformancePackComplianceSummaryRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.AggregateConformancePackComplianceSummaryFilters]

### GroupByKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AWS_REGION']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateConformancePackComplianceSummaryResponse

### AggregateConformancePackComplianceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateConformancePackComplianceSummary]
- **Required**: Yes

### GroupByKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateDiscoveredResourceCountsRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ResourceCountFilters]

### GroupByKey
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AWS_REGION', 'RESOURCE_TYPE']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateDiscoveredResourceCountsResponse

### TotalDiscoveredResources
- **Type**: <class 'int'>
- **Required**: Yes

### GroupByKey
- **Type**: <class 'str'>
- **Required**: Yes

### GroupedResourceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.GroupedResourceCount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAggregateResourceConfigRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.AggregateResourceIdentifier'>
- **Required**: Yes


# GetAggregateResourceConfigResponse

### ConfigurationItem
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ConfigurationItem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# GetComplianceDetailsByConfigRuleRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetComplianceDetailsByConfigRuleRequestPaginate

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# GetComplianceDetailsByConfigRuleResponse

### EvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.EvaluationResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetComplianceDetailsByResourceRequest

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### NextToken
- **Type**: typing.Optional[str]

### ResourceEvaluationId
- **Type**: typing.Optional[str]


# GetComplianceDetailsByResourceRequestPaginate

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ComplianceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']]]

### ResourceEvaluationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# GetComplianceDetailsByResourceResponse

### EvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.EvaluationResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetComplianceSummaryByConfigRuleResponse

### ComplianceSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ComplianceSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# GetComplianceSummaryByResourceTypeRequest

### ResourceTypes
- **Type**: typing.Optional[typing.List[str]]


# GetComplianceSummaryByResourceTypeResponse

### ComplianceSummariesByResourceType
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ComplianceSummaryByResourceType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# GetConformancePackComplianceDetailsRequest

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackEvaluationFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetConformancePackComplianceDetailsResponse

### ConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### ConformancePackRuleEvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackEvaluationResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetConformancePackComplianceSummaryRequest

### ConformancePackNames
- **Type**: typing.List[str]
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetConformancePackComplianceSummaryRequestPaginate

### ConformancePackNames
- **Type**: typing.List[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# GetConformancePackComplianceSummaryResponse

### ConformancePackComplianceSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackComplianceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCustomRulePolicyRequest

### ConfigRuleName
- **Type**: typing.Optional[str]


# GetCustomRulePolicyResponse

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# GetDiscoveredResourceCountsRequest

### resourceTypes
- **Type**: typing.Optional[typing.List[str]]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetDiscoveredResourceCountsResponse

### totalDiscoveredResources
- **Type**: <class 'int'>
- **Required**: Yes

### resourceCounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceCount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetOrganizationConfigRuleDetailedStatusRequest

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.StatusDetailFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationConfigRuleDetailedStatusRequestPaginate

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.StatusDetailFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# GetOrganizationConfigRuleDetailedStatusResponse

### OrganizationConfigRuleDetailedStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.MemberAccountStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationConformancePackDetailedStatusRequest

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.OrganizationResourceDetailedStatusFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationConformancePackDetailedStatusRequestPaginate

### OrganizationConformancePackName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.OrganizationResourceDetailedStatusFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# GetOrganizationConformancePackDetailedStatusResponse

### OrganizationConformancePackDetailedStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.OrganizationConformancePackDetailedStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetOrganizationCustomRulePolicyRequest

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrganizationCustomRulePolicyResponse

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceConfigHistoryRequest

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### laterTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### earlierTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### chronologicalOrder
- **Type**: typing.Optional[typing.Literal['Forward', 'Reverse']]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetResourceConfigHistoryRequestPaginate

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes

### laterTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### earlierTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### chronologicalOrder
- **Type**: typing.Optional[typing.Literal['Forward', 'Reverse']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# GetResourceConfigHistoryResponse

### configurationItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceEvaluationSummaryRequest

### ResourceEvaluationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceEvaluationSummaryResponse

### ResourceEvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluationMode
- **Type**: typing.Literal['DETECTIVE', 'PROACTIVE']
- **Required**: Yes

### EvaluationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.EvaluationStatus'>
- **Required**: Yes

### EvaluationStartTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Compliance
- **Type**: typing.Literal['COMPLIANT', 'INSUFFICIENT_DATA', 'NON_COMPLIANT', 'NOT_APPLICABLE']
- **Required**: Yes

### EvaluationContext
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.EvaluationContext'>
- **Required**: Yes

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResourceDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# GetStoredQueryRequest

### QueryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetStoredQueryResponse

### StoredQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.StoredQuery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# GroupedResourceCount

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceCount
- **Type**: <class 'int'>
- **Required**: Yes


# ListAggregateDiscoveredResourcesRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ResourceFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAggregateDiscoveredResourcesRequestPaginate

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ResourceFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# ListAggregateDiscoveredResourcesResponse

### ResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.AggregateResourceIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRecordersRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRecordersRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# ListConfigurationRecordersResponse

### ConfigurationRecorderSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConformancePackComplianceScoresRequest

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackComplianceScoresFilters]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['SCORE']]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConformancePackComplianceScoresResponse

### ConformancePackComplianceScores
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackComplianceScore]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesRequest

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceIds
- **Type**: typing.Optional[typing.List[str]]

### resourceName
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### includeDeletedResources
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]


# ListDiscoveredResourcesRequestPaginate

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceIds
- **Type**: typing.Optional[typing.List[str]]

### resourceName
- **Type**: typing.Optional[str]

### includeDeletedResources
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# ListDiscoveredResourcesResponse

### resourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceEvaluationsRequest

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ResourceEvaluationFilters]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceEvaluationsRequestPaginate

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ResourceEvaluationFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# ListResourceEvaluationsResponse

### ResourceEvaluations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceEvaluation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStoredQueriesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStoredQueriesResponse

### StoredQueryMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.StoredQueryMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberAccountStatus

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


# OrganizationAggregationSource

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegions
- **Type**: typing.Optional[typing.List[str]]

### AllAwsRegions
- **Type**: typing.Optional[bool]


# OrganizationAggregationSourceOutput

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AwsRegions
- **Type**: typing.Optional[typing.List[str]]

### AllAwsRegions
- **Type**: typing.Optional[bool]


# OrganizationConfigRule

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationConfigRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationManagedRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.OrganizationManagedRuleMetadataOutput]

### OrganizationCustomRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.OrganizationCustomRuleMetadataOutput]

### ExcludedAccounts
- **Type**: typing.Optional[typing.List[str]]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### OrganizationCustomPolicyRuleMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.OrganizationCustomPolicyRuleMetadataNoPolicy]


# OrganizationConfigRuleStatus

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


# OrganizationConformancePack

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackInputParameter]]

### ExcludedAccounts
- **Type**: typing.Optional[typing.List[str]]


# OrganizationConformancePackDetailedStatus

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


# OrganizationConformancePackStatus

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


# OrganizationCustomPolicyRuleMetadata

### PolicyRuntime
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyText
- **Type**: <class 'str'>
- **Required**: Yes

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

### DebugLogDeliveryAccounts
- **Type**: typing.Optional[typing.List[str]]


# OrganizationCustomPolicyRuleMetadataNoPolicy

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


# OrganizationCustomRuleMetadata

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


# OrganizationCustomRuleMetadataOutput

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


# OrganizationManagedRuleMetadata

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


# OrganizationManagedRuleMetadataOutput

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


# OrganizationResourceDetailedStatusFilters

### AccountId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingAggregationRequest

### RequesterAccountId
- **Type**: typing.Optional[str]

### RequesterAwsRegion
- **Type**: typing.Optional[str]


# PutAggregationAuthorizationRequest

### AuthorizedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedAwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]]


# PutAggregationAuthorizationResponse

### AggregationAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.AggregationAuthorization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutConfigRuleRequest

### ConfigRule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.config.config_classes.ConfigRule, aws_resource_validator.pydantic_models.config.config_classes.ConfigRuleOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]]


# PutConfigurationAggregatorRequest

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountAggregationSources
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.config.config_classes.AccountAggregationSource, aws_resource_validator.pydantic_models.config.config_classes.AccountAggregationSourceOutput]]]

### OrganizationAggregationSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.config.config_classes.OrganizationAggregationSource, aws_resource_validator.pydantic_models.config.config_classes.OrganizationAggregationSourceOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]]

### AggregatorFilters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.config.config_classes.AggregatorFilters, aws_resource_validator.pydantic_models.config.config_classes.AggregatorFiltersOutput, NoneType]


# PutConfigurationAggregatorResponse

### ConfigurationAggregator
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ConfigurationAggregator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutConfigurationRecorderRequest

### ConfigurationRecorder
- **Type**: typing.Union[aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorder, aws_resource_validator.pydantic_models.config.config_classes.ConfigurationRecorderOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]]


# PutConformancePackRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackInputParameter]]

### TemplateSSMDocumentDetails
- **Type**: <class 'NoneType'>


# PutConformancePackResponse

### ConformancePackArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutDeliveryChannelRequest

### DeliveryChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.DeliveryChannel'>
- **Required**: Yes


# PutEvaluationsRequest

### ResultToken
- **Type**: <class 'str'>
- **Required**: Yes

### Evaluations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.config.config_classes.Evaluation, aws_resource_validator.pydantic_models.config.config_classes.EvaluationOutput]]]

### TestMode
- **Type**: typing.Optional[bool]


# PutEvaluationsResponse

### FailedEvaluations
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.EvaluationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutExternalEvaluationRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalEvaluation
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ExternalEvaluation'>
- **Required**: Yes


# PutOrganizationConfigRuleRequest

### OrganizationConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationManagedRuleMetadata
- **Type**: typing.Union[aws_resource_validator.pydantic_models.config.config_classes.OrganizationManagedRuleMetadata, aws_resource_validator.pydantic_models.config.config_classes.OrganizationManagedRuleMetadataOutput, NoneType]

### OrganizationCustomRuleMetadata
- **Type**: typing.Union[aws_resource_validator.pydantic_models.config.config_classes.OrganizationCustomRuleMetadata, aws_resource_validator.pydantic_models.config.config_classes.OrganizationCustomRuleMetadataOutput, NoneType]

### ExcludedAccounts
- **Type**: typing.Optional[typing.List[str]]

### OrganizationCustomPolicyRuleMetadata
- **Type**: <class 'NoneType'>


# PutOrganizationConfigRuleResponse

### OrganizationConfigRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutOrganizationConformancePackRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.ConformancePackInputParameter]]

### ExcludedAccounts
- **Type**: typing.Optional[typing.List[str]]


# PutOrganizationConformancePackResponse

### OrganizationConformancePackArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutRemediationConfigurationsRequest

### RemediationConfigurations
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.config.config_classes.RemediationConfiguration, aws_resource_validator.pydantic_models.config.config_classes.RemediationConfigurationOutput]]
- **Required**: Yes


# PutRemediationConfigurationsResponse

### FailedBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.FailedRemediationBatch]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutRemediationExceptionsRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationExceptionResourceKey]
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]

### ExpirationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PutRemediationExceptionsResponse

### FailedBatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.FailedRemediationExceptionBatch]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourceConfigRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutRetentionConfigurationRequest

### RetentionPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes


# PutRetentionConfigurationResponse

### RetentionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.RetentionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutServiceLinkedConfigurationRecorderRequest

### ServicePrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]]


# PutServiceLinkedConfigurationRecorderResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# PutStoredQueryRequest

### StoredQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.StoredQuery'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]]


# PutStoredQueryResponse

### QueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# QueryInfo

### SelectFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.FieldInfo]]


# RecordingGroup

### allSupported
- **Type**: typing.Optional[bool]

### includeGlobalResourceTypes
- **Type**: typing.Optional[bool]

### resourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]

### exclusionByResourceTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ExclusionByResourceTypes]

### recordingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.RecordingStrategy]


# RecordingGroupOutput

### allSupported
- **Type**: typing.Optional[bool]

### includeGlobalResourceTypes
- **Type**: typing.Optional[bool]

### resourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]]

### exclusionByResourceTypes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.ExclusionByResourceTypesOutput]

### recordingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.RecordingStrategy]


# RecordingMode

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### recordingModeOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.RecordingModeOverride]]


# RecordingModeOutput

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### recordingModeOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.RecordingModeOverrideOutput]]


# RecordingModeOverride

### resourceTypes
- **Type**: typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# RecordingModeOverrideOutput

### resourceTypes
- **Type**: typing.List[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]
- **Required**: Yes

### recordingFrequency
- **Type**: typing.Literal['CONTINUOUS', 'DAILY']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# RecordingStrategy

### useOnly
- **Type**: typing.Optional[typing.Literal['ALL_SUPPORTED_RESOURCE_TYPES', 'EXCLUSION_BY_RESOURCE_TYPES', 'INCLUSION_BY_RESOURCE_TYPES']]


# Relationship

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### resourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### relationshipName
- **Type**: typing.Optional[str]


# RemediationConfiguration

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
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.config.config_classes.RemediationParameterValue, aws_resource_validator.pydantic_models.config.config_classes.RemediationParameterValueOutput]]]

### ResourceType
- **Type**: typing.Optional[str]

### Automatic
- **Type**: typing.Optional[bool]

### ExecutionControls
- **Type**: <class 'NoneType'>

### MaximumAutomaticAttempts
- **Type**: typing.Optional[int]

### RetryAttemptSeconds
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### CreatedByService
- **Type**: typing.Optional[str]


# RemediationConfigurationOutput

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.config.config_classes.RemediationParameterValueOutput]]

### ResourceType
- **Type**: typing.Optional[str]

### Automatic
- **Type**: typing.Optional[bool]

### ExecutionControls
- **Type**: <class 'NoneType'>

### MaximumAutomaticAttempts
- **Type**: typing.Optional[int]

### RetryAttemptSeconds
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### CreatedByService
- **Type**: typing.Optional[str]


# RemediationException

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


# RemediationExceptionResourceKey

### ResourceType
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]


# RemediationExecutionStatus

### ResourceKey
- **Type**: <class 'NoneType'>

### State
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']]

### StepDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.RemediationExecutionStep]]

### InvocationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# RemediationExecutionStep

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


# RemediationParameterValue

### ResourceValue
- **Type**: <class 'NoneType'>

### StaticValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.config.config_classes.StaticValue, aws_resource_validator.pydantic_models.config.config_classes.StaticValueOutput, NoneType]


# RemediationParameterValueOutput

### ResourceValue
- **Type**: <class 'NoneType'>

### StaticValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.StaticValueOutput]


# ResourceCount

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### count
- **Type**: typing.Optional[int]


# ResourceCountFilters

### ResourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### AccountId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# ResourceDetails

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


# ResourceEvaluation

### ResourceEvaluationId
- **Type**: typing.Optional[str]

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]

### EvaluationStartTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ResourceEvaluationFilters

### EvaluationMode
- **Type**: typing.Optional[typing.Literal['DETECTIVE', 'PROACTIVE']]

### TimeWindow
- **Type**: <class 'NoneType'>

### EvaluationContextIdentifier
- **Type**: typing.Optional[str]


# ResourceFilters

### AccountId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# ResourceIdentifier

### resourceType
- **Type**: typing.Optional[typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']]

### resourceId
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]

### resourceDeletionTime
- **Type**: typing.Optional[datetime.datetime]


# ResourceKey

### resourceType
- **Type**: typing.Literal['AWS::ACM::Certificate', 'AWS::ACMPCA::CertificateAuthority', 'AWS::ACMPCA::CertificateAuthorityActivation', 'AWS::APS::RuleGroupsNamespace', 'AWS::AccessAnalyzer::Analyzer', 'AWS::AmazonMQ::Broker', 'AWS::Amplify::App', 'AWS::Amplify::Branch', 'AWS::ApiGateway::RestApi', 'AWS::ApiGateway::Stage', 'AWS::ApiGatewayV2::Api', 'AWS::ApiGatewayV2::Stage', 'AWS::AppConfig::Application', 'AWS::AppConfig::ConfigurationProfile', 'AWS::AppConfig::DeploymentStrategy', 'AWS::AppConfig::Environment', 'AWS::AppConfig::HostedConfigurationVersion', 'AWS::AppFlow::Flow', 'AWS::AppIntegrations::EventIntegration', 'AWS::AppMesh::GatewayRoute', 'AWS::AppMesh::Mesh', 'AWS::AppMesh::Route', 'AWS::AppMesh::VirtualGateway', 'AWS::AppMesh::VirtualNode', 'AWS::AppMesh::VirtualRouter', 'AWS::AppMesh::VirtualService', 'AWS::AppRunner::Service', 'AWS::AppRunner::VpcConnector', 'AWS::AppStream::Application', 'AWS::AppStream::DirectoryConfig', 'AWS::AppStream::Fleet', 'AWS::AppStream::Stack', 'AWS::AppSync::GraphQLApi', 'AWS::Athena::DataCatalog', 'AWS::Athena::PreparedStatement', 'AWS::Athena::WorkGroup', 'AWS::AuditManager::Assessment', 'AWS::AutoScaling::AutoScalingGroup', 'AWS::AutoScaling::LaunchConfiguration', 'AWS::AutoScaling::ScalingPolicy', 'AWS::AutoScaling::ScheduledAction', 'AWS::AutoScaling::WarmPool', 'AWS::Backup::BackupPlan', 'AWS::Backup::BackupSelection', 'AWS::Backup::BackupVault', 'AWS::Backup::RecoveryPoint', 'AWS::Backup::ReportPlan', 'AWS::Batch::ComputeEnvironment', 'AWS::Batch::JobQueue', 'AWS::Batch::SchedulingPolicy', 'AWS::Budgets::BudgetsAction', 'AWS::Cassandra::Keyspace', 'AWS::Cloud9::EnvironmentEC2', 'AWS::CloudFormation::Stack', 'AWS::CloudFront::Distribution', 'AWS::CloudFront::StreamingDistribution', 'AWS::CloudTrail::Trail', 'AWS::CloudWatch::Alarm', 'AWS::CloudWatch::MetricStream', 'AWS::CodeArtifact::Repository', 'AWS::CodeBuild::Project', 'AWS::CodeBuild::ReportGroup', 'AWS::CodeDeploy::Application', 'AWS::CodeDeploy::DeploymentConfig', 'AWS::CodeDeploy::DeploymentGroup', 'AWS::CodeGuruProfiler::ProfilingGroup', 'AWS::CodeGuruReviewer::RepositoryAssociation', 'AWS::CodePipeline::Pipeline', 'AWS::Cognito::UserPool', 'AWS::Cognito::UserPoolClient', 'AWS::Cognito::UserPoolGroup', 'AWS::Config::ConformancePackCompliance', 'AWS::Config::ResourceCompliance', 'AWS::Connect::Instance', 'AWS::Connect::PhoneNumber', 'AWS::Connect::QuickConnect', 'AWS::CustomerProfiles::Domain', 'AWS::CustomerProfiles::ObjectType', 'AWS::DMS::Certificate', 'AWS::DMS::Endpoint', 'AWS::DMS::EventSubscription', 'AWS::DMS::ReplicationSubnetGroup', 'AWS::DataSync::LocationEFS', 'AWS::DataSync::LocationFSxLustre', 'AWS::DataSync::LocationFSxWindows', 'AWS::DataSync::LocationHDFS', 'AWS::DataSync::LocationNFS', 'AWS::DataSync::LocationObjectStorage', 'AWS::DataSync::LocationS3', 'AWS::DataSync::LocationSMB', 'AWS::DataSync::Task', 'AWS::Detective::Graph', 'AWS::DeviceFarm::InstanceProfile', 'AWS::DeviceFarm::Project', 'AWS::DeviceFarm::TestGridProject', 'AWS::DynamoDB::Table', 'AWS::EC2::CapacityReservation', 'AWS::EC2::CarrierGateway', 'AWS::EC2::ClientVpnEndpoint', 'AWS::EC2::CustomerGateway', 'AWS::EC2::DHCPOptions', 'AWS::EC2::EC2Fleet', 'AWS::EC2::EIP', 'AWS::EC2::EgressOnlyInternetGateway', 'AWS::EC2::FlowLog', 'AWS::EC2::Host', 'AWS::EC2::IPAM', 'AWS::EC2::IPAMPool', 'AWS::EC2::IPAMScope', 'AWS::EC2::Instance', 'AWS::EC2::InternetGateway', 'AWS::EC2::LaunchTemplate', 'AWS::EC2::NatGateway', 'AWS::EC2::NetworkAcl', 'AWS::EC2::NetworkInsightsAccessScope', 'AWS::EC2::NetworkInsightsAccessScopeAnalysis', 'AWS::EC2::NetworkInsightsAnalysis', 'AWS::EC2::NetworkInsightsPath', 'AWS::EC2::NetworkInterface', 'AWS::EC2::PrefixList', 'AWS::EC2::RegisteredHAInstance', 'AWS::EC2::RouteTable', 'AWS::EC2::SecurityGroup', 'AWS::EC2::SpotFleet', 'AWS::EC2::Subnet', 'AWS::EC2::SubnetRouteTableAssociation', 'AWS::EC2::TrafficMirrorFilter', 'AWS::EC2::TrafficMirrorSession', 'AWS::EC2::TrafficMirrorTarget', 'AWS::EC2::TransitGateway', 'AWS::EC2::TransitGatewayAttachment', 'AWS::EC2::TransitGatewayConnect', 'AWS::EC2::TransitGatewayMulticastDomain', 'AWS::EC2::TransitGatewayRouteTable', 'AWS::EC2::VPC', 'AWS::EC2::VPCEndpoint', 'AWS::EC2::VPCEndpointService', 'AWS::EC2::VPCPeeringConnection', 'AWS::EC2::VPNConnection', 'AWS::EC2::VPNGateway', 'AWS::EC2::Volume', 'AWS::ECR::PublicRepository', 'AWS::ECR::PullThroughCacheRule', 'AWS::ECR::RegistryPolicy', 'AWS::ECR::Repository', 'AWS::ECS::CapacityProvider', 'AWS::ECS::Cluster', 'AWS::ECS::Service', 'AWS::ECS::TaskDefinition', 'AWS::ECS::TaskSet', 'AWS::EFS::AccessPoint', 'AWS::EFS::FileSystem', 'AWS::EKS::Addon', 'AWS::EKS::Cluster', 'AWS::EKS::FargateProfile', 'AWS::EKS::IdentityProviderConfig', 'AWS::EMR::SecurityConfiguration', 'AWS::ElasticBeanstalk::Application', 'AWS::ElasticBeanstalk::ApplicationVersion', 'AWS::ElasticBeanstalk::Environment', 'AWS::ElasticLoadBalancing::LoadBalancer', 'AWS::ElasticLoadBalancingV2::Listener', 'AWS::ElasticLoadBalancingV2::LoadBalancer', 'AWS::Elasticsearch::Domain', 'AWS::EventSchemas::Discoverer', 'AWS::EventSchemas::Registry', 'AWS::EventSchemas::RegistryPolicy', 'AWS::EventSchemas::Schema', 'AWS::Events::ApiDestination', 'AWS::Events::Archive', 'AWS::Events::Connection', 'AWS::Events::Endpoint', 'AWS::Events::EventBus', 'AWS::Events::Rule', 'AWS::Evidently::Launch', 'AWS::Evidently::Project', 'AWS::FIS::ExperimentTemplate', 'AWS::Forecast::Dataset', 'AWS::Forecast::DatasetGroup', 'AWS::FraudDetector::EntityType', 'AWS::FraudDetector::Label', 'AWS::FraudDetector::Outcome', 'AWS::FraudDetector::Variable', 'AWS::GlobalAccelerator::Accelerator', 'AWS::GlobalAccelerator::EndpointGroup', 'AWS::GlobalAccelerator::Listener', 'AWS::Glue::Classifier', 'AWS::Glue::Job', 'AWS::Glue::MLTransform', 'AWS::Grafana::Workspace', 'AWS::GreengrassV2::ComponentVersion', 'AWS::GroundStation::Config', 'AWS::GroundStation::DataflowEndpointGroup', 'AWS::GroundStation::MissionProfile', 'AWS::GuardDuty::Detector', 'AWS::GuardDuty::Filter', 'AWS::GuardDuty::IPSet', 'AWS::GuardDuty::ThreatIntelSet', 'AWS::HealthLake::FHIRDatastore', 'AWS::IAM::Group', 'AWS::IAM::InstanceProfile', 'AWS::IAM::Policy', 'AWS::IAM::Role', 'AWS::IAM::SAMLProvider', 'AWS::IAM::ServerCertificate', 'AWS::IAM::User', 'AWS::IVS::Channel', 'AWS::IVS::PlaybackKeyPair', 'AWS::IVS::RecordingConfiguration', 'AWS::ImageBuilder::ContainerRecipe', 'AWS::ImageBuilder::DistributionConfiguration', 'AWS::ImageBuilder::ImagePipeline', 'AWS::ImageBuilder::ImageRecipe', 'AWS::ImageBuilder::InfrastructureConfiguration', 'AWS::InspectorV2::Filter', 'AWS::IoT::AccountAuditConfiguration', 'AWS::IoT::Authorizer', 'AWS::IoT::CACertificate', 'AWS::IoT::CustomMetric', 'AWS::IoT::Dimension', 'AWS::IoT::FleetMetric', 'AWS::IoT::JobTemplate', 'AWS::IoT::MitigationAction', 'AWS::IoT::Policy', 'AWS::IoT::ProvisioningTemplate', 'AWS::IoT::RoleAlias', 'AWS::IoT::ScheduledAudit', 'AWS::IoT::SecurityProfile', 'AWS::IoTAnalytics::Channel', 'AWS::IoTAnalytics::Dataset', 'AWS::IoTAnalytics::Datastore', 'AWS::IoTAnalytics::Pipeline', 'AWS::IoTEvents::AlarmModel', 'AWS::IoTEvents::DetectorModel', 'AWS::IoTEvents::Input', 'AWS::IoTSiteWise::AssetModel', 'AWS::IoTSiteWise::Dashboard', 'AWS::IoTSiteWise::Gateway', 'AWS::IoTSiteWise::Portal', 'AWS::IoTSiteWise::Project', 'AWS::IoTTwinMaker::ComponentType', 'AWS::IoTTwinMaker::Entity', 'AWS::IoTTwinMaker::Scene', 'AWS::IoTTwinMaker::SyncJob', 'AWS::IoTTwinMaker::Workspace', 'AWS::IoTWireless::FuotaTask', 'AWS::IoTWireless::MulticastGroup', 'AWS::IoTWireless::ServiceProfile', 'AWS::KMS::Alias', 'AWS::KMS::Key', 'AWS::KafkaConnect::Connector', 'AWS::Kendra::Index', 'AWS::Kinesis::Stream', 'AWS::Kinesis::StreamConsumer', 'AWS::KinesisAnalyticsV2::Application', 'AWS::KinesisFirehose::DeliveryStream', 'AWS::KinesisVideo::SignalingChannel', 'AWS::KinesisVideo::Stream', 'AWS::Lambda::CodeSigningConfig', 'AWS::Lambda::Function', 'AWS::Lex::Bot', 'AWS::Lex::BotAlias', 'AWS::Lightsail::Bucket', 'AWS::Lightsail::Certificate', 'AWS::Lightsail::Disk', 'AWS::Lightsail::StaticIp', 'AWS::Logs::Destination', 'AWS::LookoutMetrics::Alert', 'AWS::LookoutVision::Project', 'AWS::M2::Environment', 'AWS::MSK::BatchScramSecret', 'AWS::MSK::Cluster', 'AWS::MSK::Configuration', 'AWS::MediaConnect::FlowEntitlement', 'AWS::MediaConnect::FlowSource', 'AWS::MediaConnect::FlowVpcInterface', 'AWS::MediaPackage::PackagingConfiguration', 'AWS::MediaPackage::PackagingGroup', 'AWS::MediaTailor::PlaybackConfiguration', 'AWS::NetworkFirewall::Firewall', 'AWS::NetworkFirewall::FirewallPolicy', 'AWS::NetworkFirewall::RuleGroup', 'AWS::NetworkManager::ConnectPeer', 'AWS::NetworkManager::CustomerGatewayAssociation', 'AWS::NetworkManager::Device', 'AWS::NetworkManager::GlobalNetwork', 'AWS::NetworkManager::Link', 'AWS::NetworkManager::LinkAssociation', 'AWS::NetworkManager::Site', 'AWS::NetworkManager::TransitGatewayRegistration', 'AWS::OpenSearch::Domain', 'AWS::Panorama::Package', 'AWS::Personalize::Dataset', 'AWS::Personalize::DatasetGroup', 'AWS::Personalize::Schema', 'AWS::Personalize::Solution', 'AWS::Pinpoint::App', 'AWS::Pinpoint::ApplicationSettings', 'AWS::Pinpoint::Campaign', 'AWS::Pinpoint::EmailChannel', 'AWS::Pinpoint::EmailTemplate', 'AWS::Pinpoint::EventStream', 'AWS::Pinpoint::InAppTemplate', 'AWS::Pinpoint::Segment', 'AWS::QLDB::Ledger', 'AWS::QuickSight::DataSource', 'AWS::QuickSight::Template', 'AWS::QuickSight::Theme', 'AWS::RDS::DBCluster', 'AWS::RDS::DBClusterSnapshot', 'AWS::RDS::DBInstance', 'AWS::RDS::DBSecurityGroup', 'AWS::RDS::DBSnapshot', 'AWS::RDS::DBSubnetGroup', 'AWS::RDS::EventSubscription', 'AWS::RDS::GlobalCluster', 'AWS::RDS::OptionGroup', 'AWS::RUM::AppMonitor', 'AWS::Redshift::Cluster', 'AWS::Redshift::ClusterParameterGroup', 'AWS::Redshift::ClusterSecurityGroup', 'AWS::Redshift::ClusterSnapshot', 'AWS::Redshift::ClusterSubnetGroup', 'AWS::Redshift::EndpointAccess', 'AWS::Redshift::EventSubscription', 'AWS::Redshift::ScheduledAction', 'AWS::ResilienceHub::App', 'AWS::ResilienceHub::ResiliencyPolicy', 'AWS::ResourceExplorer2::Index', 'AWS::RoboMaker::RobotApplication', 'AWS::RoboMaker::RobotApplicationVersion', 'AWS::RoboMaker::SimulationApplication', 'AWS::Route53::HostedZone', 'AWS::Route53RecoveryControl::Cluster', 'AWS::Route53RecoveryControl::ControlPanel', 'AWS::Route53RecoveryControl::RoutingControl', 'AWS::Route53RecoveryControl::SafetyRule', 'AWS::Route53RecoveryReadiness::Cell', 'AWS::Route53RecoveryReadiness::ReadinessCheck', 'AWS::Route53RecoveryReadiness::RecoveryGroup', 'AWS::Route53RecoveryReadiness::ResourceSet', 'AWS::Route53Resolver::FirewallDomainList', 'AWS::Route53Resolver::FirewallRuleGroup', 'AWS::Route53Resolver::FirewallRuleGroupAssociation', 'AWS::Route53Resolver::ResolverEndpoint', 'AWS::Route53Resolver::ResolverQueryLoggingConfig', 'AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation', 'AWS::Route53Resolver::ResolverRule', 'AWS::Route53Resolver::ResolverRuleAssociation', 'AWS::S3::AccessPoint', 'AWS::S3::AccountPublicAccessBlock', 'AWS::S3::Bucket', 'AWS::S3::MultiRegionAccessPoint', 'AWS::S3::StorageLens', 'AWS::SES::ConfigurationSet', 'AWS::SES::ContactList', 'AWS::SES::ReceiptFilter', 'AWS::SES::ReceiptRuleSet', 'AWS::SES::Template', 'AWS::SNS::Topic', 'AWS::SQS::Queue', 'AWS::SSM::AssociationCompliance', 'AWS::SSM::Document', 'AWS::SSM::FileData', 'AWS::SSM::ManagedInstanceInventory', 'AWS::SSM::PatchCompliance', 'AWS::SageMaker::AppImageConfig', 'AWS::SageMaker::CodeRepository', 'AWS::SageMaker::Domain', 'AWS::SageMaker::FeatureGroup', 'AWS::SageMaker::Image', 'AWS::SageMaker::Model', 'AWS::SageMaker::NotebookInstanceLifecycleConfig', 'AWS::SageMaker::Workteam', 'AWS::SecretsManager::Secret', 'AWS::ServiceCatalog::CloudFormationProduct', 'AWS::ServiceCatalog::CloudFormationProvisionedProduct', 'AWS::ServiceCatalog::Portfolio', 'AWS::ServiceDiscovery::HttpNamespace', 'AWS::ServiceDiscovery::Instance', 'AWS::ServiceDiscovery::PublicDnsNamespace', 'AWS::ServiceDiscovery::Service', 'AWS::Shield::Protection', 'AWS::ShieldRegional::Protection', 'AWS::Signer::SigningProfile', 'AWS::StepFunctions::Activity', 'AWS::StepFunctions::StateMachine', 'AWS::Transfer::Agreement', 'AWS::Transfer::Certificate', 'AWS::Transfer::Connector', 'AWS::Transfer::Workflow', 'AWS::WAF::RateBasedRule', 'AWS::WAF::Rule', 'AWS::WAF::RuleGroup', 'AWS::WAF::WebACL', 'AWS::WAFRegional::RateBasedRule', 'AWS::WAFRegional::Rule', 'AWS::WAFRegional::RuleGroup', 'AWS::WAFRegional::WebACL', 'AWS::WAFv2::IPSet', 'AWS::WAFv2::ManagedRuleSet', 'AWS::WAFv2::RegexPatternSet', 'AWS::WAFv2::RuleGroup', 'AWS::WAFv2::WebACL', 'AWS::WorkSpaces::ConnectionAlias', 'AWS::WorkSpaces::Workspace', 'AWS::XRay::EncryptionConfig']
- **Required**: Yes

### resourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceValue

### Value
- **Type**: typing.Literal['RESOURCE_ID']
- **Required**: Yes


# ResponseMetadata

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


# RetentionConfiguration

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes


# Scope

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### ComplianceResourceId
- **Type**: typing.Optional[str]


# ScopeOutput

### ComplianceResourceTypes
- **Type**: typing.Optional[typing.List[str]]

### TagKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### ComplianceResourceId
- **Type**: typing.Optional[str]


# SelectAggregateResourceConfigRequest

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


# SelectAggregateResourceConfigRequestPaginate

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationAggregatorName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# SelectAggregateResourceConfigResponse

### Results
- **Type**: typing.List[str]
- **Required**: Yes

### QueryInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.QueryInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SelectResourceConfigRequest

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SelectResourceConfigRequestPaginate

### Expression
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.config.config_classes.PaginatorConfig]


# SelectResourceConfigResponse

### Results
- **Type**: typing.List[str]
- **Required**: Yes

### QueryInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.QueryInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Source

### Owner
- **Type**: typing.Literal['AWS', 'CUSTOM_LAMBDA', 'CUSTOM_POLICY']
- **Required**: Yes

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.SourceDetail]]

### CustomPolicyDetails
- **Type**: <class 'NoneType'>


# SourceDetail

### EventSource
- **Type**: typing.Optional[typing.Literal['aws.config']]

### MessageType
- **Type**: typing.Optional[typing.Literal['ConfigurationItemChangeNotification', 'ConfigurationSnapshotDeliveryCompleted', 'OversizedConfigurationItemChangeNotification', 'ScheduledNotification']]

### MaximumExecutionFrequency
- **Type**: typing.Optional[typing.Literal['One_Hour', 'Six_Hours', 'Three_Hours', 'Twelve_Hours', 'TwentyFour_Hours']]


# SourceOutput

### Owner
- **Type**: typing.Literal['AWS', 'CUSTOM_LAMBDA', 'CUSTOM_POLICY']
- **Required**: Yes

### SourceIdentifier
- **Type**: typing.Optional[str]

### SourceDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.config.config_classes.SourceDetail]]

### CustomPolicyDetails
- **Type**: <class 'NoneType'>


# SsmControls

### ConcurrentExecutionRatePercentage
- **Type**: typing.Optional[int]

### ErrorPercentage
- **Type**: typing.Optional[int]


# StartConfigRulesEvaluationRequest

### ConfigRuleNames
- **Type**: typing.Optional[typing.List[str]]


# StartConfigurationRecorderRequest

### ConfigurationRecorderName
- **Type**: <class 'str'>
- **Required**: Yes


# StartRemediationExecutionRequest

### ConfigRuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceKey]
- **Required**: Yes


# StartRemediationExecutionResponse

### FailureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### FailedItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.ResourceKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# StartResourceEvaluationRequest

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResourceDetails'>
- **Required**: Yes

### EvaluationMode
- **Type**: typing.Literal['DETECTIVE', 'PROACTIVE']
- **Required**: Yes

### EvaluationContext
- **Type**: <class 'NoneType'>

### EvaluationTimeout
- **Type**: typing.Optional[int]

### ClientToken
- **Type**: typing.Optional[str]


# StartResourceEvaluationResponse

### ResourceEvaluationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.config.config_classes.ResponseMetadata'>
- **Required**: Yes


# StaticValue

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# StaticValueOutput

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# StatusDetailFilters

### AccountId
- **Type**: typing.Optional[str]

### MemberAccountRuleStatus
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_SUCCESSFUL', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS', 'UPDATE_SUCCESSFUL']]


# StopConfigurationRecorderRequest

### ConfigurationRecorderName
- **Type**: <class 'str'>
- **Required**: Yes


# StoredQuery

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


# StoredQueryMetadata

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


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.config.config_classes.Tag]
- **Required**: Yes


# TemplateSSMDocumentDetails

### DocumentName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentVersion
- **Type**: typing.Optional[str]


# TimeWindow

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


