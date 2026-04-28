# Packaging & extras

`aws-resource-validator` is distributed as a family of wheels:

- The **main wheel** (`aws-resource-validator`) ships the validator,
  `BaseValidatorModel`, and the generator code — no `pydantic_models/` content.
- **Service wheels** (`aws-resource-validator-<service>`) each ship one
  `pydantic_models/<service>/` subtree and depend on the main wheel.
- **Shard wheels** (`aws-resource-validator-<shard>`) are metapackages —
  empty wheels whose only purpose is to pull in every service in their domain.
- `aws_resource_validator.pydantic_models` is a **PEP 420 namespace package**,
  so service wheels and the main wheel merge cleanly at import time.

All three kinds release in lock-step: every service and shard wheel is pinned
exactly to the current main version.

## Installation patterns

```sh
# Core only (validators + BaseValidatorModel, no service models).
pip install aws-resource-validator

# One or more individual services via their extras.
pip install 'aws-resource-validator[s3,ec2,lambda]'

# An entire domain shard (pulls in every service in that domain).
pip install 'aws-resource-validator[data]'

# Everything — every shard, transitively every service.
pip install 'aws-resource-validator[all]'

# Generator dependencies for regenerating the models yourself.
pip install 'aws-resource-validator[generator]'
```

Extras are composable: `pip install 'aws-resource-validator[s3,security]'` gives
you the S3 models plus every service in the `security` shard.

<!-- BEGIN GENERATED PACKAGING DOCS -->

## Standalone service packages

These AWS services each get their own PyPI project and their own extras
key on the main package — a curated subset chosen for typical usage
(maintained in [`scripts/release/popular_services.txt`][popular]).

| Extras key | PyPI project |
| --- | --- |
| `[apigateway]` | [`aws-resource-validator-apigateway`](https://pypi.org/project/aws-resource-validator-apigateway/) |
| `[apigatewayv2]` | [`aws-resource-validator-apigatewayv2`](https://pypi.org/project/aws-resource-validator-apigatewayv2/) |
| `[athena]` | [`aws-resource-validator-athena`](https://pypi.org/project/aws-resource-validator-athena/) |
| `[bedrock]` | [`aws-resource-validator-bedrock`](https://pypi.org/project/aws-resource-validator-bedrock/) |
| `[cloudformation]` | [`aws-resource-validator-cloudformation`](https://pypi.org/project/aws-resource-validator-cloudformation/) |
| `[cloudwatch]` | [`aws-resource-validator-cloudwatch`](https://pypi.org/project/aws-resource-validator-cloudwatch/) |
| `[cognito-idp]` | [`aws-resource-validator-cognito-idp`](https://pypi.org/project/aws-resource-validator-cognito-idp/) |
| `[dynamodb]` | [`aws-resource-validator-dynamodb`](https://pypi.org/project/aws-resource-validator-dynamodb/) |
| `[ec2]` | [`aws-resource-validator-ec2`](https://pypi.org/project/aws-resource-validator-ec2/) |
| `[ecs]` | [`aws-resource-validator-ecs`](https://pypi.org/project/aws-resource-validator-ecs/) |
| `[elbv2]` | [`aws-resource-validator-elbv2`](https://pypi.org/project/aws-resource-validator-elbv2/) |
| `[events]` | [`aws-resource-validator-events`](https://pypi.org/project/aws-resource-validator-events/) |
| `[firehose]` | [`aws-resource-validator-firehose`](https://pypi.org/project/aws-resource-validator-firehose/) |
| `[glue]` | [`aws-resource-validator-glue`](https://pypi.org/project/aws-resource-validator-glue/) |
| `[iam]` | [`aws-resource-validator-iam`](https://pypi.org/project/aws-resource-validator-iam/) |
| `[kinesis]` | [`aws-resource-validator-kinesis`](https://pypi.org/project/aws-resource-validator-kinesis/) |
| `[kms]` | [`aws-resource-validator-kms`](https://pypi.org/project/aws-resource-validator-kms/) |
| `[lambda]` | [`aws-resource-validator-lambda`](https://pypi.org/project/aws-resource-validator-lambda/) |
| `[logs]` | [`aws-resource-validator-logs`](https://pypi.org/project/aws-resource-validator-logs/) |
| `[rds]` | [`aws-resource-validator-rds`](https://pypi.org/project/aws-resource-validator-rds/) |
| `[redshift]` | [`aws-resource-validator-redshift`](https://pypi.org/project/aws-resource-validator-redshift/) |
| `[route53]` | [`aws-resource-validator-route53`](https://pypi.org/project/aws-resource-validator-route53/) |
| `[s3]` | [`aws-resource-validator-s3`](https://pypi.org/project/aws-resource-validator-s3/) |
| `[sagemaker]` | [`aws-resource-validator-sagemaker`](https://pypi.org/project/aws-resource-validator-sagemaker/) |
| `[secretsmanager]` | [`aws-resource-validator-secretsmanager`](https://pypi.org/project/aws-resource-validator-secretsmanager/) |
| `[sns]` | [`aws-resource-validator-sns`](https://pypi.org/project/aws-resource-validator-sns/) |
| `[sqs]` | [`aws-resource-validator-sqs`](https://pypi.org/project/aws-resource-validator-sqs/) |
| `[ssm]` | [`aws-resource-validator-ssm`](https://pypi.org/project/aws-resource-validator-ssm/) |
| `[stepfunctions]` | [`aws-resource-validator-stepfunctions`](https://pypi.org/project/aws-resource-validator-stepfunctions/) |
| `[sts]` | [`aws-resource-validator-sts`](https://pypi.org/project/aws-resource-validator-sts/) |

Every other AWS service (393 of them) is still available — just
via its shard. If you need a long-tail service as a standalone extra,
open an issue.

## Domain shards

Shards group services by domain. Installing a shard extra transitively
installs every service wheel in its list. Membership is maintained in
[`scripts/release/shards.toml`][shards].

### `[ai]` — ML, generative AI, cognitive services

PyPI: [`aws-resource-validator-ai`](https://pypi.org/project/aws-resource-validator-ai/)

**50 services:**

`aiops`, `bedrock`, `bedrock_agent`, `bedrock_agent_runtime`, `bedrock_agentcore`, `bedrock_agentcore_control`, `bedrock_data_automation`, `bedrock_data_automation_runtime`, `bedrock_runtime`, `braket`, `comprehend`, `comprehendmedical`, `devops_agent`, `devops_guru`, `elementalinference`, `forecast`, `forecastquery`, `frauddetector`, `healthlake`, `kendra`, `kendra_ranking`, `lex_models`, `lex_runtime`, `lexv2_models`, `lexv2_runtime`, `lookoutequipment`, `machinelearning`, `medical_imaging`, `nova_act`, `omics`, `panorama`, `personalize`, `personalize_events`, `personalize_runtime`, `polly`, `qapps`, `qbusiness`, `qconnect`, `rekognition`, `sagemaker`, `sagemaker_a2i_runtime`, `sagemaker_edge`, `sagemaker_featurestore_runtime`, `sagemaker_geospatial`, `sagemaker_metrics`, `sagemaker_runtime`, `textract`, `transcribe`, `translate`, `wisdom`

### `[compute]` — Compute, containers, batch, EMR, Workspaces

PyPI: [`aws-resource-validator-compute`](https://pypi.org/project/aws-resource-validator-compute/)

**40 services:**

`application_autoscaling`, `apprunner`, `appstream`, `autoscaling`, `autoscaling_plans`, `batch`, `compute_optimizer`, `compute_optimizer_automation`, `ebs`, `ec2`, `ec2_instance_connect`, `ecr`, `ecr_public`, `ecs`, `eks`, `eks_auth`, `elasticbeanstalk`, `emr`, `emr_containers`, `emr_serverless`, `evs`, `fis`, `imagebuilder`, `lambda_`, `launch_wizard`, `lightsail`, `m2`, `mwaa`, `mwaa_serverless`, `outposts`, `pcs`, `resiliencehub`, `serverlessrepo`, `simspaceweaver`, `snow_device_management`, `snowball`, `workspaces`, `workspaces_instances`, `workspaces_thin_client`, `workspaces_web`

### `[data]` — Storage, databases, analytics, data movement

PyPI: [`aws-resource-validator-data`](https://pypi.org/project/aws-resource-validator-data/)

**66 services:**

`athena`, `backup`, `backup_gateway`, `backupsearch`, `cleanroomsml`, `cloudsearch`, `cloudsearchdomain`, `databrew`, `dataexchange`, `datapipeline`, `datasync`, `datazone`, `dax`, `dlm`, `dms`, `docdb`, `docdb_elastic`, `drs`, `dsql`, `dynamodb`, `dynamodbstreams`, `efs`, `elasticache`, `entityresolution`, `es`, `finspace`, `finspace_data`, `firehose`, `fsx`, `glacier`, `glue`, `keyspaces`, `keyspacesstreams`, `kinesis`, `kinesisanalytics`, `kinesisanalyticsv2`, `lakeformation`, `memorydb`, `neptune`, `neptune_graph`, `neptunedata`, `odb`, `opensearch`, `opensearchserverless`, `osis`, `quicksight`, `rbin`, `rds`, `rds_data`, `redshift`, `redshift_data`, `redshift_serverless`, `s3`, `s3control`, `s3files`, `s3outposts`, `s3tables`, `s3vectors`, `sdb`, `simpledbv2`, `storagegateway`, `supplychain`, `timestream_influxdb`, `timestream_query`, `timestream_write`, `transfer`

### `[integration]` — Messaging, events, workflows, comms, contact center

PyPI: [`aws-resource-validator-integration`](https://pypi.org/project/aws-resource-validator-integration/)

**47 services:**

`appfabric`, `appflow`, `appintegrations`, `b2bi`, `chatbot`, `chime`, `chime_sdk_identity`, `chime_sdk_media_pipelines`, `chime_sdk_meetings`, `chime_sdk_messaging`, `chime_sdk_voice`, `connect`, `connect_contact_lens`, `connectcampaigns`, `connectcampaignsv2`, `connectcases`, `connecthealth`, `connectparticipant`, `customer_profiles`, `events`, `kafka`, `kafkaconnect`, `mailmanager`, `managedblockchain`, `managedblockchain_query`, `mq`, `mturk`, `notifications`, `notificationscontacts`, `pinpoint`, `pinpoint_email`, `pinpoint_sms_voice`, `pinpoint_sms_voice_v2`, `pipes`, `scheduler`, `schemas`, `ses`, `sesv2`, `sns`, `socialmessaging`, `sqs`, `stepfunctions`, `swf`, `voice_id`, `workdocs`, `workmail`, `workmailmessageflow`

### `[management]` — Governance, ops, monitoring, deploy, billing, dev tools

PyPI: [`aws-resource-validator-management`](https://pypi.org/project/aws-resource-validator-management/)

**103 services:**

`account`, `amp`, `amplify`, `amplifybackend`, `amplifyuibuilder`, `appconfig`, `appconfigdata`, `application_insights`, `application_signals`, `applicationcostprofiler`, `bcm_dashboards`, `bcm_data_exports`, `bcm_pricing_calculator`, `bcm_recommended_actions`, `billing`, `billingconductor`, `budgets`, `ce`, `cleanrooms`, `cloud9`, `cloudcontrol`, `cloudformation`, `cloudtrail`, `cloudtrail_data`, `cloudwatch`, `codeartifact`, `codebuild`, `codecatalyst`, `codecommit`, `codeconnections`, `codedeploy`, `codeguru_reviewer`, `codeguru_security`, `codeguruprofiler`, `codepipeline`, `codestar_connections`, `codestar_notifications`, `config`, `controlcatalog`, `controltower`, `cost_optimization_hub`, `cur`, `devicefarm`, `discovery`, `freetier`, `grafana`, `health`, `importexport`, `invoicing`, `license_manager`, `license_manager_linux_subscriptions`, `license_manager_user_subscriptions`, `logs`, `marketplace_agreement`, `marketplace_catalog`, `marketplace_deployment`, `marketplace_discovery`, `marketplace_entitlement`, `marketplace_reporting`, `marketplacecommerceanalytics`, `meteringmarketplace`, `mgh`, `mgn`, `migration_hub_refactor_spaces`, `migrationhub_config`, `migrationhuborchestrator`, `migrationhubstrategy`, `mpa`, `oam`, `observabilityadmin`, `organizations`, `partnercentral_account`, `partnercentral_benefits`, `partnercentral_channel`, `partnercentral_selling`, `pi`, `pricing`, `proton`, `repostspace`, `resource_explorer_2`, `resource_groups`, `resourcegroupstaggingapi`, `rum`, `savingsplans`, `service_quotas`, `servicecatalog`, `servicecatalog_appregistry`, `servicediscovery`, `ssm`, `ssm_contacts`, `ssm_guiconnect`, `ssm_incidents`, `ssm_quicksetup`, `ssm_sap`, `support`, `support_app`, `sustainability`, `synthetics`, `taxsettings`, `trustedadvisor`, `uxc`, `wellarchitected`, `xray`

### `[networking]` — VPC, DNS, CDN, routing, API gateways, geo

PyPI: [`aws-resource-validator-networking`](https://pypi.org/project/aws-resource-validator-networking/)

**33 services:**

`apigateway`, `apigatewaymanagementapi`, `apigatewayv2`, `appmesh`, `appsync`, `arc_region_switch`, `arc_zonal_shift`, `cloudfront`, `cloudfront_keyvaluestore`, `directconnect`, `elb`, `elbv2`, `geo_maps`, `geo_places`, `geo_routes`, `globalaccelerator`, `interconnect`, `internetmonitor`, `location`, `networkflowmonitor`, `networkmanager`, `networkmonitor`, `route53`, `route53_recovery_cluster`, `route53_recovery_control_config`, `route53_recovery_readiness`, `route53domains`, `route53globalresolver`, `route53profiles`, `route53resolver`, `rtbfabric`, `tnb`, `vpc_lattice`

### `[rest]` — Media, IoT, gaming, satellite, and the long tail

PyPI: [`aws-resource-validator-rest`](https://pypi.org/project/aws-resource-validator-rest/)

*Catch-all shard — any AWS service not explicitly assigned to another
shard lives here.*

**36 services:**

`deadline`, `gamelift`, `gameliftstreams`, `greengrass`, `greengrassv2`, `groundstation`, `iot`, `iot_data`, `iot_jobs_data`, `iot_managed_integrations`, `iotdeviceadvisor`, `iotevents`, `iotevents_data`, `iotfleetwise`, `iotsecuretunneling`, `iotsitewise`, `iotthingsgraph`, `iottwinmaker`, `iotwireless`, `ivs`, `ivs_realtime`, `ivschat`, `kinesis_video_archived_media`, `kinesis_video_media`, `kinesis_video_signaling`, `kinesis_video_webrtc_storage`, `kinesisvideo`, `mediaconnect`, `mediaconvert`, `medialive`, `mediapackage`, `mediapackage_vod`, `mediapackagev2`, `mediastore`, `mediastore_data`, `mediatailor`

### `[security]` — Identity, access, encryption, compliance, threat detection

PyPI: [`aws-resource-validator-security`](https://pypi.org/project/aws-resource-validator-security/)

**48 services:**

`accessanalyzer`, `acm`, `acm_pca`, `artifact`, `auditmanager`, `clouddirectory`, `cloudhsm`, `cloudhsmv2`, `cognito_identity`, `cognito_idp`, `cognito_sync`, `detective`, `ds`, `ds_data`, `fms`, `guardduty`, `iam`, `identitystore`, `inspector`, `inspector2`, `inspector_scan`, `kms`, `macie2`, `network_firewall`, `payment_cryptography`, `payment_cryptography_data`, `pca_connector_ad`, `pca_connector_scep`, `ram`, `rolesanywhere`, `secretsmanager`, `security_ir`, `securityagent`, `securityhub`, `securitylake`, `shield`, `signer`, `signer_data`, `signin`, `sso`, `sso_admin`, `sso_oidc`, `sts`, `verifiedpermissions`, `waf`, `waf_regional`, `wafv2`, `wickr`

[popular]: https://github.com/CoreOxide/aws_resource_validator/blob/main/scripts/release/popular_services.txt
[shards]: https://github.com/CoreOxide/aws_resource_validator/blob/main/scripts/release/shards.toml

<!-- END GENERATED PACKAGING DOCS -->
