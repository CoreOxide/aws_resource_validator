from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.iot.iot_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AbortCriteria(BaseValidatorModel):
    failureType: JobExecutionFailureTypeType
    action: Literal['CANCEL']
    thresholdPercentage: float
    minNumberOfExecutedThings: int


# This class is the input for the 'accept_certificate_transfer' function.
class AcceptCertificateTransferRequest(BaseValidatorModel):
    certificateId: str
    setAsActive: Optional[bool] = None


class CloudwatchAlarmAction(BaseValidatorModel):
    roleArn: str
    alarmName: str
    stateReason: str
    stateValue: str


class CloudwatchLogsAction(BaseValidatorModel):
    roleArn: str
    logGroupName: str
    batchMode: Optional[bool] = None


class CloudwatchMetricAction(BaseValidatorModel):
    roleArn: str
    metricNamespace: str
    metricName: str
    metricValue: str
    metricUnit: str
    metricTimestamp: Optional[str] = None


class DynamoDBAction(BaseValidatorModel):
    tableName: str
    roleArn: str
    hashKeyField: str
    hashKeyValue: str
    operation: Optional[str] = None
    hashKeyType: Optional[DynamoKeyTypeType] = None
    rangeKeyField: Optional[str] = None
    rangeKeyValue: Optional[str] = None
    rangeKeyType: Optional[DynamoKeyTypeType] = None
    payloadField: Optional[str] = None


class ElasticsearchAction(BaseValidatorModel):
    roleArn: str
    endpoint: str
    index: str
    type: str
    id: str


class FirehoseAction(BaseValidatorModel):
    roleArn: str
    deliveryStreamName: str
    separator: Optional[str] = None
    batchMode: Optional[bool] = None


class IotAnalyticsAction(BaseValidatorModel):
    channelArn: Optional[str] = None
    channelName: Optional[str] = None
    batchMode: Optional[bool] = None
    roleArn: Optional[str] = None


class IotEventsAction(BaseValidatorModel):
    inputName: str
    roleArn: str
    messageId: Optional[str] = None
    batchMode: Optional[bool] = None


class KinesisAction(BaseValidatorModel):
    roleArn: str
    streamName: str
    partitionKey: Optional[str] = None


class LambdaAction(BaseValidatorModel):
    functionArn: str


class OpenSearchAction(BaseValidatorModel):
    roleArn: str
    endpoint: str
    index: str
    type: str
    id: str


class S3Action(BaseValidatorModel):
    roleArn: str
    bucketName: str
    key: str
    cannedAcl: Optional[CannedAccessControlListType] = None


class SalesforceAction(BaseValidatorModel):
    token: str
    url: str


class SnsAction(BaseValidatorModel):
    targetArn: str
    roleArn: str
    messageFormat: Optional[MessageFormatType] = None


class SqsAction(BaseValidatorModel):
    roleArn: str
    queueUrl: str
    useBase64: Optional[bool] = None


class StepFunctionsAction(BaseValidatorModel):
    stateMachineName: str
    roleArn: str
    executionNamePrefix: Optional[str] = None


class MetricValueOutput(BaseValidatorModel):
    count: Optional[int] = None
    cidrs: Optional[List[str]] = None
    ports: Optional[List[int]] = None
    number: Optional[float] = None
    numbers: Optional[List[float]] = None
    strings: Optional[List[str]] = None


class ViolationEventAdditionalInfo(BaseValidatorModel):
    confidenceLevel: Optional[ConfidenceLevelType] = None


class AddThingToBillingGroupRequest(BaseValidatorModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None


class AddThingToThingGroupRequest(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None
    overrideDynamicGroups: Optional[bool] = None


class AddThingsToThingGroupParamsOutput(BaseValidatorModel):
    thingGroupNames: List[str]
    overrideDynamicGroups: Optional[bool] = None


class AddThingsToThingGroupParams(BaseValidatorModel):
    thingGroupNames: List[str]
    overrideDynamicGroups: Optional[bool] = None


class AggregationTypeOutput(BaseValidatorModel):
    name: AggregationTypeNameType
    values: Optional[List[str]] = None


class AggregationType(BaseValidatorModel):
    name: AggregationTypeNameType
    values: Optional[List[str]] = None


class AlertTarget(BaseValidatorModel):
    alertTargetArn: str
    roleArn: str


class Policy(BaseValidatorModel):
    policyName: Optional[str] = None
    policyArn: Optional[str] = None


class AssetPropertyTimestamp(BaseValidatorModel):
    timeInSeconds: str
    offsetInNanos: Optional[str] = None


class AssetPropertyVariant(BaseValidatorModel):
    stringValue: Optional[str] = None
    integerValue: Optional[str] = None
    doubleValue: Optional[str] = None
    booleanValue: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_targets_with_job' function.
class AssociateTargetsWithJobRequest(BaseValidatorModel):
    targets: List[str]
    jobId: str
    comment: Optional[str] = None
    namespaceId: Optional[str] = None


# This class is the input for the 'attach_policy' function.
class AttachPolicyRequest(BaseValidatorModel):
    policyName: str
    target: str


# This class is the input for the 'attach_principal_policy' function.
class AttachPrincipalPolicyRequest(BaseValidatorModel):
    policyName: str
    principal: str


class AttachSecurityProfileRequest(BaseValidatorModel):
    securityProfileName: str
    securityProfileTargetArn: str


class AttachThingPrincipalRequest(BaseValidatorModel):
    thingName: str
    principal: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class AttributePayloadOutput(BaseValidatorModel):
    attributes: Optional[Dict[str, str]] = None
    merge: Optional[bool] = None


class AttributePayload(BaseValidatorModel):
    attributes: Optional[Dict[str, str]] = None
    merge: Optional[bool] = None


class AuditCheckConfigurationOutput(BaseValidatorModel):
    enabled: Optional[bool] = None
    configuration: Optional[Dict[ConfigNameType, str]] = None


class AuditCheckConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None
    configuration: Optional[Dict[ConfigNameType, str]] = None


class AuditCheckDetails(BaseValidatorModel):
    checkRunStatus: Optional[AuditCheckRunStatusType] = None
    checkCompliant: Optional[bool] = None
    totalResourcesCount: Optional[int] = None
    nonCompliantResourcesCount: Optional[int] = None
    suppressedNonCompliantResourcesCount: Optional[int] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None


class AuditMitigationActionExecutionMetadata(BaseValidatorModel):
    taskId: Optional[str] = None
    findingId: Optional[str] = None
    actionName: Optional[str] = None
    actionId: Optional[str] = None
    status: Optional[AuditMitigationActionsExecutionStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None


class AuditMitigationActionsTaskMetadata(BaseValidatorModel):
    taskId: Optional[str] = None
    startTime: Optional[datetime] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None


class AuditMitigationActionsTaskTargetOutput(BaseValidatorModel):
    auditTaskId: Optional[str] = None
    findingIds: Optional[List[str]] = None
    auditCheckToReasonCodeFilter: Optional[Dict[str, List[str]]] = None


class AuditMitigationActionsTaskTarget(BaseValidatorModel):
    auditTaskId: Optional[str] = None
    findingIds: Optional[List[str]] = None
    auditCheckToReasonCodeFilter: Optional[Dict[str, List[str]]] = None


class AuditNotificationTarget(BaseValidatorModel):
    targetArn: Optional[str] = None
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None


class AuditTaskMetadata(BaseValidatorModel):
    taskId: Optional[str] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    taskType: Optional[AuditTaskTypeType] = None


class AuthInfoOutput(BaseValidatorModel):
    resources: List[str]
    actionType: Optional[ActionTypeType] = None


class AuthInfo(BaseValidatorModel):
    resources: List[str]
    actionType: Optional[ActionTypeType] = None


class AuthorizerConfig(BaseValidatorModel):
    defaultAuthorizerName: Optional[str] = None
    allowAuthorizerOverride: Optional[bool] = None


class AuthorizerDescription(BaseValidatorModel):
    authorizerName: Optional[str] = None
    authorizerArn: Optional[str] = None
    authorizerFunctionArn: Optional[str] = None
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Dict[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    signingDisabled: Optional[bool] = None
    enableCachingForHttp: Optional[bool] = None


class AuthorizerSummary(BaseValidatorModel):
    authorizerName: Optional[str] = None
    authorizerArn: Optional[str] = None


class AwsJobAbortCriteria(BaseValidatorModel):
    failureType: AwsJobAbortCriteriaFailureTypeType
    action: Literal['CANCEL']
    thresholdPercentage: float
    minNumberOfExecutedThings: int


class AwsJobRateIncreaseCriteria(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None


class AwsJobPresignedUrlConfig(BaseValidatorModel):
    expiresInSec: Optional[int] = None


class AwsJobTimeoutConfig(BaseValidatorModel):
    inProgressTimeoutInMinutes: Optional[int] = None


class MachineLearningDetectionConfig(BaseValidatorModel):
    confidenceLevel: ConfidenceLevelType


class StatisticalThreshold(BaseValidatorModel):
    statistic: Optional[str] = None


class BehaviorModelTrainingSummary(BaseValidatorModel):
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None
    trainingDataCollectionStartDate: Optional[datetime] = None
    modelStatus: Optional[ModelStatusType] = None
    datapointsCollectionPercentage: Optional[float] = None
    lastModelRefreshDate: Optional[datetime] = None


class MetricDimension(BaseValidatorModel):
    dimensionName: str
    operator: Optional[DimensionValueOperatorType] = None


class BillingGroupMetadata(BaseValidatorModel):
    creationDate: Optional[datetime] = None


class BillingGroupProperties(BaseValidatorModel):
    billingGroupDescription: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class Bucket(BaseValidatorModel):
    keyValue: Optional[str] = None
    count: Optional[int] = None


class TermsAggregation(BaseValidatorModel):
    maxBuckets: Optional[int] = None


class CertificateValidity(BaseValidatorModel):
    notBefore: Optional[datetime] = None
    notAfter: Optional[datetime] = None


class CACertificate(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    status: Optional[CACertificateStatusType] = None
    creationDate: Optional[datetime] = None


class CancelAuditMitigationActionsTaskRequest(BaseValidatorModel):
    taskId: str


class CancelAuditTaskRequest(BaseValidatorModel):
    taskId: str


# This class is the input for the 'cancel_certificate_transfer' function.
class CancelCertificateTransferRequest(BaseValidatorModel):
    certificateId: str


class CancelDetectMitigationActionsTaskRequest(BaseValidatorModel):
    taskId: str


# This class is the input for the 'cancel_job_execution' function.
class CancelJobExecutionRequest(BaseValidatorModel):
    jobId: str
    thingName: str
    force: Optional[bool] = None
    expectedVersion: Optional[int] = None
    statusDetails: Optional[Dict[str, str]] = None


# This class is the input for the 'cancel_job' function.
class CancelJobRequest(BaseValidatorModel):
    jobId: str
    reasonCode: Optional[str] = None
    comment: Optional[str] = None
    force: Optional[bool] = None


class TransferData(BaseValidatorModel):
    transferMessage: Optional[str] = None
    rejectReason: Optional[str] = None
    transferDate: Optional[datetime] = None
    acceptDate: Optional[datetime] = None
    rejectDate: Optional[datetime] = None


class CertificateProviderSummary(BaseValidatorModel):
    certificateProviderName: Optional[str] = None
    certificateProviderArn: Optional[str] = None


class Certificate(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    status: Optional[CertificateStatusType] = None
    certificateMode: Optional[CertificateModeType] = None
    creationDate: Optional[datetime] = None


class ClientCertificateConfig(BaseValidatorModel):
    clientCertificateCallbackArn: Optional[str] = None


class CodeSigningCertificateChain(BaseValidatorModel):
    certificateName: Optional[str] = None
    inlineDocument: Optional[str] = None


class CodeSigningSignatureOutput(BaseValidatorModel):
    inlineDocument: Optional[bytes] = None


class CommandExecutionResult(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    BIN: Optional[bytes] = None


class CommandExecutionSummary(BaseValidatorModel):
    commandArn: Optional[str] = None
    executionId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[CommandExecutionStatusType] = None
    createdAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None


class CommandParameterValueOutput(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    I: Optional[int] = None
    L: Optional[int] = None
    D: Optional[float] = None
    BIN: Optional[bytes] = None
    UL: Optional[str] = None


class CommandPayloadOutput(BaseValidatorModel):
    content: Optional[bytes] = None
    contentType: Optional[str] = None


class CommandSummary(BaseValidatorModel):
    commandArn: Optional[str] = None
    commandId: Optional[str] = None
    displayName: Optional[str] = None
    deprecated: Optional[bool] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    pendingDeletion: Optional[bool] = None


class Configuration(BaseValidatorModel):
    Enabled: Optional[bool] = None


class ConfirmTopicRuleDestinationRequest(BaseValidatorModel):
    confirmationToken: str

Timestamp = Union[datetime, str]


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


# This class is the input for the 'create_certificate_from_csr' function.
class CreateCertificateFromCsrRequest(BaseValidatorModel):
    certificateSigningRequest: str
    setAsActive: Optional[bool] = None


class ServerCertificateConfig(BaseValidatorModel):
    enableOCSPCheck: Optional[bool] = None
    ocspLambdaArn: Optional[str] = None
    ocspAuthorizedResponderArn: Optional[str] = None


class TlsConfig(BaseValidatorModel):
    securityPolicy: Optional[str] = None


class PresignedUrlConfig(BaseValidatorModel):
    roleArn: Optional[str] = None
    expiresInSec: Optional[int] = None


class TimeoutConfig(BaseValidatorModel):
    inProgressTimeoutInMinutes: Optional[int] = None


class MaintenanceWindow(BaseValidatorModel):
    startTime: str
    durationInMinutes: int


# This class is the input for the 'create_keys_and_certificate' function.
class CreateKeysAndCertificateRequest(BaseValidatorModel):
    setAsActive: Optional[bool] = None


class KeyPair(BaseValidatorModel):
    PublicKey: Optional[str] = None
    PrivateKey: Optional[str] = None


# This class is the input for the 'create_package' function.
class CreatePackageRequest(BaseValidatorModel):
    packageName: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None


# This class is the input for the 'create_policy_version' function.
class CreatePolicyVersionRequest(BaseValidatorModel):
    policyName: str
    policyDocument: str
    setAsDefault: Optional[bool] = None


# This class is the input for the 'create_provisioning_claim' function.
class CreateProvisioningClaimRequest(BaseValidatorModel):
    templateName: str


class ProvisioningHook(BaseValidatorModel):
    targetArn: str
    payloadVersion: Optional[str] = None


# This class is the input for the 'create_provisioning_template_version' function.
class CreateProvisioningTemplateVersionRequest(BaseValidatorModel):
    templateName: str
    templateBody: str
    setAsDefault: Optional[bool] = None


class MetricsExportConfig(BaseValidatorModel):
    mqttTopic: str
    roleArn: str


class DeleteAccountAuditConfigurationRequest(BaseValidatorModel):
    deleteScheduledAudits: Optional[bool] = None


class DeleteAuthorizerRequest(BaseValidatorModel):
    authorizerName: str


class DeleteBillingGroupRequest(BaseValidatorModel):
    billingGroupName: str
    expectedVersion: Optional[int] = None


class DeleteCACertificateRequest(BaseValidatorModel):
    certificateId: str


class DeleteCertificateProviderRequest(BaseValidatorModel):
    certificateProviderName: str


# This class is the input for the 'delete_certificate' function.
class DeleteCertificateRequest(BaseValidatorModel):
    certificateId: str
    forceDelete: Optional[bool] = None


class DeleteCommandExecutionRequest(BaseValidatorModel):
    executionId: str
    targetArn: str


# This class is the input for the 'delete_command' function.
class DeleteCommandRequest(BaseValidatorModel):
    commandId: str


class DeleteCustomMetricRequest(BaseValidatorModel):
    metricName: str


class DeleteDimensionRequest(BaseValidatorModel):
    name: str


class DeleteDomainConfigurationRequest(BaseValidatorModel):
    domainConfigurationName: str


class DeleteDynamicThingGroupRequest(BaseValidatorModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None


# This class is the input for the 'delete_fleet_metric' function.
class DeleteFleetMetricRequest(BaseValidatorModel):
    metricName: str
    expectedVersion: Optional[int] = None


# This class is the input for the 'delete_job_execution' function.
class DeleteJobExecutionRequest(BaseValidatorModel):
    jobId: str
    thingName: str
    executionNumber: int
    force: Optional[bool] = None
    namespaceId: Optional[str] = None


# This class is the input for the 'delete_job' function.
class DeleteJobRequest(BaseValidatorModel):
    jobId: str
    force: Optional[bool] = None
    namespaceId: Optional[str] = None


# This class is the input for the 'delete_job_template' function.
class DeleteJobTemplateRequest(BaseValidatorModel):
    jobTemplateId: str


class DeleteMitigationActionRequest(BaseValidatorModel):
    actionName: str


class DeleteOTAUpdateRequest(BaseValidatorModel):
    otaUpdateId: str
    deleteStream: Optional[bool] = None
    forceDeleteAWSJob: Optional[bool] = None


class DeletePackageRequest(BaseValidatorModel):
    packageName: str
    clientToken: Optional[str] = None


class DeletePackageVersionRequest(BaseValidatorModel):
    packageName: str
    versionName: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_policy' function.
class DeletePolicyRequest(BaseValidatorModel):
    policyName: str


# This class is the input for the 'delete_policy_version' function.
class DeletePolicyVersionRequest(BaseValidatorModel):
    policyName: str
    policyVersionId: str


class DeleteProvisioningTemplateRequest(BaseValidatorModel):
    templateName: str


class DeleteProvisioningTemplateVersionRequest(BaseValidatorModel):
    templateName: str
    versionId: int


class DeleteRoleAliasRequest(BaseValidatorModel):
    roleAlias: str


class DeleteScheduledAuditRequest(BaseValidatorModel):
    scheduledAuditName: str


class DeleteSecurityProfileRequest(BaseValidatorModel):
    securityProfileName: str
    expectedVersion: Optional[int] = None


class DeleteStreamRequest(BaseValidatorModel):
    streamId: str


class DeleteThingGroupRequest(BaseValidatorModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None


class DeleteThingRequest(BaseValidatorModel):
    thingName: str
    expectedVersion: Optional[int] = None


class DeleteThingTypeRequest(BaseValidatorModel):
    thingTypeName: str


class DeleteTopicRuleDestinationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'delete_topic_rule' function.
class DeleteTopicRuleRequest(BaseValidatorModel):
    ruleName: str


# This class is the input for the 'delete_v2_logging_level' function.
class DeleteV2LoggingLevelRequest(BaseValidatorModel):
    targetType: LogTargetTypeType
    targetName: str


class DeprecateThingTypeRequest(BaseValidatorModel):
    thingTypeName: str
    undoDeprecate: Optional[bool] = None


# This class is the input for the 'describe_audit_finding' function.
class DescribeAuditFindingRequest(BaseValidatorModel):
    findingId: str


# This class is the input for the 'describe_audit_mitigation_actions_task' function.
class DescribeAuditMitigationActionsTaskRequest(BaseValidatorModel):
    taskId: str


class TaskStatisticsForAuditCheck(BaseValidatorModel):
    totalFindingsCount: Optional[int] = None
    failedFindingsCount: Optional[int] = None
    succeededFindingsCount: Optional[int] = None
    skippedFindingsCount: Optional[int] = None
    canceledFindingsCount: Optional[int] = None


# This class is the input for the 'describe_audit_task' function.
class DescribeAuditTaskRequest(BaseValidatorModel):
    taskId: str


class TaskStatistics(BaseValidatorModel):
    totalChecks: Optional[int] = None
    inProgressChecks: Optional[int] = None
    waitingForDataCollectionChecks: Optional[int] = None
    compliantChecks: Optional[int] = None
    nonCompliantChecks: Optional[int] = None
    failedChecks: Optional[int] = None
    canceledChecks: Optional[int] = None


# This class is the input for the 'describe_authorizer' function.
class DescribeAuthorizerRequest(BaseValidatorModel):
    authorizerName: str


# This class is the input for the 'describe_billing_group' function.
class DescribeBillingGroupRequest(BaseValidatorModel):
    billingGroupName: str


# This class is the input for the 'describe_ca_certificate' function.
class DescribeCACertificateRequest(BaseValidatorModel):
    certificateId: str


class RegistrationConfig(BaseValidatorModel):
    templateBody: Optional[str] = None
    roleArn: Optional[str] = None
    templateName: Optional[str] = None


# This class is the input for the 'describe_certificate_provider' function.
class DescribeCertificateProviderRequest(BaseValidatorModel):
    certificateProviderName: str


# This class is the input for the 'describe_certificate' function.
class DescribeCertificateRequest(BaseValidatorModel):
    certificateId: str


# This class is the input for the 'describe_custom_metric' function.
class DescribeCustomMetricRequest(BaseValidatorModel):
    metricName: str


# This class is the input for the 'describe_detect_mitigation_actions_task' function.
class DescribeDetectMitigationActionsTaskRequest(BaseValidatorModel):
    taskId: str


# This class is the input for the 'describe_dimension' function.
class DescribeDimensionRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'describe_domain_configuration' function.
class DescribeDomainConfigurationRequest(BaseValidatorModel):
    domainConfigurationName: str


class ServerCertificateSummary(BaseValidatorModel):
    serverCertificateArn: Optional[str] = None
    serverCertificateStatus: Optional[ServerCertificateStatusType] = None
    serverCertificateStatusDetail: Optional[str] = None


# This class is the input for the 'describe_endpoint' function.
class DescribeEndpointRequest(BaseValidatorModel):
    endpointType: Optional[str] = None


# This class is the input for the 'describe_fleet_metric' function.
class DescribeFleetMetricRequest(BaseValidatorModel):
    metricName: str


# This class is the input for the 'describe_index' function.
class DescribeIndexRequest(BaseValidatorModel):
    indexName: str


# This class is the input for the 'describe_job_execution' function.
class DescribeJobExecutionRequest(BaseValidatorModel):
    jobId: str
    thingName: str
    executionNumber: Optional[int] = None


# This class is the input for the 'describe_job' function.
class DescribeJobRequest(BaseValidatorModel):
    jobId: str
    beforeSubstitution: Optional[bool] = None


# This class is the input for the 'describe_job_template' function.
class DescribeJobTemplateRequest(BaseValidatorModel):
    jobTemplateId: str


# This class is the input for the 'describe_managed_job_template' function.
class DescribeManagedJobTemplateRequest(BaseValidatorModel):
    templateName: str
    templateVersion: Optional[str] = None


class DocumentParameter(BaseValidatorModel):
    key: Optional[str] = None
    description: Optional[str] = None
    regex: Optional[str] = None
    example: Optional[str] = None
    optional: Optional[bool] = None


# This class is the input for the 'describe_mitigation_action' function.
class DescribeMitigationActionRequest(BaseValidatorModel):
    actionName: str


# This class is the input for the 'describe_provisioning_template' function.
class DescribeProvisioningTemplateRequest(BaseValidatorModel):
    templateName: str


# This class is the input for the 'describe_provisioning_template_version' function.
class DescribeProvisioningTemplateVersionRequest(BaseValidatorModel):
    templateName: str
    versionId: int


# This class is the input for the 'describe_role_alias' function.
class DescribeRoleAliasRequest(BaseValidatorModel):
    roleAlias: str


class RoleAliasDescription(BaseValidatorModel):
    roleAlias: Optional[str] = None
    roleAliasArn: Optional[str] = None
    roleArn: Optional[str] = None
    owner: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None


# This class is the input for the 'describe_scheduled_audit' function.
class DescribeScheduledAuditRequest(BaseValidatorModel):
    scheduledAuditName: str


# This class is the input for the 'describe_security_profile' function.
class DescribeSecurityProfileRequest(BaseValidatorModel):
    securityProfileName: str


# This class is the input for the 'describe_stream' function.
class DescribeStreamRequest(BaseValidatorModel):
    streamId: str


# This class is the input for the 'describe_thing_group' function.
class DescribeThingGroupRequest(BaseValidatorModel):
    thingGroupName: str


# This class is the input for the 'describe_thing_registration_task' function.
class DescribeThingRegistrationTaskRequest(BaseValidatorModel):
    taskId: str


# This class is the input for the 'describe_thing' function.
class DescribeThingRequest(BaseValidatorModel):
    thingName: str


# This class is the input for the 'describe_thing_type' function.
class DescribeThingTypeRequest(BaseValidatorModel):
    thingTypeName: str


class ThingTypeMetadata(BaseValidatorModel):
    deprecated: Optional[bool] = None
    deprecationDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None


class S3Destination(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


# This class is the input for the 'detach_policy' function.
class DetachPolicyRequest(BaseValidatorModel):
    policyName: str
    target: str


# This class is the input for the 'detach_principal_policy' function.
class DetachPrincipalPolicyRequest(BaseValidatorModel):
    policyName: str
    principal: str


class DetachSecurityProfileRequest(BaseValidatorModel):
    securityProfileName: str
    securityProfileTargetArn: str


class DetachThingPrincipalRequest(BaseValidatorModel):
    thingName: str
    principal: str


class DetectMitigationActionExecution(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    actionName: Optional[str] = None
    thingName: Optional[str] = None
    executionStartDate: Optional[datetime] = None
    executionEndDate: Optional[datetime] = None
    status: Optional[DetectMitigationActionExecutionStatusType] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None


class DetectMitigationActionsTaskStatistics(BaseValidatorModel):
    actionsExecuted: Optional[int] = None
    actionsSkipped: Optional[int] = None
    actionsFailed: Optional[int] = None


class DetectMitigationActionsTaskTargetOutput(BaseValidatorModel):
    violationIds: Optional[List[str]] = None
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None


class ViolationEventOccurrenceRangeOutput(BaseValidatorModel):
    startTime: datetime
    endTime: datetime


class DetectMitigationActionsTaskTarget(BaseValidatorModel):
    violationIds: Optional[List[str]] = None
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None


# This class is the input for the 'disable_topic_rule' function.
class DisableTopicRuleRequest(BaseValidatorModel):
    ruleName: str


class DisassociateSbomFromPackageVersionRequest(BaseValidatorModel):
    packageName: str
    versionName: str
    clientToken: Optional[str] = None


class DomainConfigurationSummary(BaseValidatorModel):
    domainConfigurationName: Optional[str] = None
    domainConfigurationArn: Optional[str] = None
    serviceType: Optional[ServiceTypeType] = None


class PutItemInput(BaseValidatorModel):
    tableName: str


class EffectivePolicy(BaseValidatorModel):
    policyName: Optional[str] = None
    policyArn: Optional[str] = None
    policyDocument: Optional[str] = None


class EnableIoTLoggingParams(BaseValidatorModel):
    roleArnForLogging: str
    logLevel: LogLevelType


# This class is the input for the 'enable_topic_rule' function.
class EnableTopicRuleRequest(BaseValidatorModel):
    ruleName: str


class ErrorInfo(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class RateIncreaseCriteria(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None


class Field(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[FieldTypeType] = None


class S3Location(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    version: Optional[str] = None


class Stream(BaseValidatorModel):
    streamId: Optional[str] = None
    fileId: Optional[int] = None


class FleetMetricNameAndArn(BaseValidatorModel):
    metricName: Optional[str] = None
    metricArn: Optional[str] = None


class GeoLocationTarget(BaseValidatorModel):
    name: Optional[str] = None
    order: Optional[TargetFieldOrderType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_behavior_model_training_summaries' function.
class GetBehaviorModelTrainingSummariesRequest(BaseValidatorModel):
    securityProfileName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'get_cardinality' function.
class GetCardinalityRequest(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None


# This class is the input for the 'get_command_execution' function.
class GetCommandExecutionRequest(BaseValidatorModel):
    executionId: str
    targetArn: str
    includeResult: Optional[bool] = None


class StatusReason(BaseValidatorModel):
    reasonCode: str
    reasonDescription: Optional[str] = None


# This class is the input for the 'get_command' function.
class GetCommandRequest(BaseValidatorModel):
    commandId: str


# This class is the input for the 'get_effective_policies' function.
class GetEffectivePoliciesRequest(BaseValidatorModel):
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    thingName: Optional[str] = None


# This class is the input for the 'get_job_document' function.
class GetJobDocumentRequest(BaseValidatorModel):
    jobId: str
    beforeSubstitution: Optional[bool] = None


# This class is the input for the 'get_ota_update' function.
class GetOTAUpdateRequest(BaseValidatorModel):
    otaUpdateId: str


class VersionUpdateByJobsConfig(BaseValidatorModel):
    enabled: Optional[bool] = None
    roleArn: Optional[str] = None


# This class is the input for the 'get_package' function.
class GetPackageRequest(BaseValidatorModel):
    packageName: str


# This class is the input for the 'get_package_version' function.
class GetPackageVersionRequest(BaseValidatorModel):
    packageName: str
    versionName: str


# This class is the input for the 'get_percentiles' function.
class GetPercentilesRequest(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None
    percents: Optional[List[float]] = None


class PercentPair(BaseValidatorModel):
    percent: Optional[float] = None
    value: Optional[float] = None


# This class is the input for the 'get_policy' function.
class GetPolicyRequest(BaseValidatorModel):
    policyName: str


# This class is the input for the 'get_policy_version' function.
class GetPolicyVersionRequest(BaseValidatorModel):
    policyName: str
    policyVersionId: str


# This class is the input for the 'get_statistics' function.
class GetStatisticsRequest(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None


class Statistics(BaseValidatorModel):
    count: Optional[int] = None
    average: Optional[float] = None
    sum: Optional[float] = None
    minimum: Optional[float] = None
    maximum: Optional[float] = None
    sumOfSquares: Optional[float] = None
    variance: Optional[float] = None
    stdDeviation: Optional[float] = None


# This class is the input for the 'get_thing_connectivity_data' function.
class GetThingConnectivityDataRequest(BaseValidatorModel):
    thingName: str


# This class is the input for the 'get_topic_rule_destination' function.
class GetTopicRuleDestinationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_topic_rule' function.
class GetTopicRuleRequest(BaseValidatorModel):
    ruleName: str


class GroupNameAndArn(BaseValidatorModel):
    groupName: Optional[str] = None
    groupArn: Optional[str] = None


class HttpActionHeader(BaseValidatorModel):
    key: str
    value: str


class SigV4Authorization(BaseValidatorModel):
    signingRegion: str
    serviceName: str
    roleArn: str


class HttpContext(BaseValidatorModel):
    headers: Optional[Dict[str, str]] = None
    queryString: Optional[str] = None


class HttpUrlDestinationConfiguration(BaseValidatorModel):
    confirmationUrl: str


class HttpUrlDestinationProperties(BaseValidatorModel):
    confirmationUrl: Optional[str] = None


class HttpUrlDestinationSummary(BaseValidatorModel):
    confirmationUrl: Optional[str] = None


class IssuerCertificateIdentifier(BaseValidatorModel):
    issuerCertificateSubject: Optional[str] = None
    issuerId: Optional[str] = None
    issuerCertificateSerialNumber: Optional[str] = None


class JobExecutionStatusDetails(BaseValidatorModel):
    detailsMap: Optional[Dict[str, str]] = None


class JobExecutionSummary(BaseValidatorModel):
    status: Optional[JobExecutionStatusType] = None
    queuedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    executionNumber: Optional[int] = None
    retryAttempt: Optional[int] = None


class RetryCriteria(BaseValidatorModel):
    failureType: RetryableFailureTypeType
    numberOfRetries: int


class JobProcessDetails(BaseValidatorModel):
    processingTargets: Optional[List[str]] = None
    numberOfCanceledThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None
    numberOfFailedThings: Optional[int] = None
    numberOfRejectedThings: Optional[int] = None
    numberOfQueuedThings: Optional[int] = None
    numberOfInProgressThings: Optional[int] = None
    numberOfRemovedThings: Optional[int] = None
    numberOfTimedOutThings: Optional[int] = None


class JobSummary(BaseValidatorModel):
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    thingGroupId: Optional[str] = None
    targetSelection: Optional[TargetSelectionType] = None
    status: Optional[JobStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    isConcurrent: Optional[bool] = None


class JobTemplateSummary(BaseValidatorModel):
    jobTemplateArn: Optional[str] = None
    jobTemplateId: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None


class ScheduledJobRollout(BaseValidatorModel):
    startTime: Optional[str] = None


class KafkaActionHeader(BaseValidatorModel):
    key: str
    value: str


# This class is the input for the 'list_active_violations' function.
class ListActiveViolationsRequest(BaseValidatorModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_attached_policies' function.
class ListAttachedPoliciesRequest(BaseValidatorModel):
    target: str
    recursive: Optional[bool] = None
    marker: Optional[str] = None
    pageSize: Optional[int] = None


# This class is the input for the 'list_audit_mitigation_actions_executions' function.
class ListAuditMitigationActionsExecutionsRequest(BaseValidatorModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_authorizers' function.
class ListAuthorizersRequest(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None


# This class is the input for the 'list_billing_groups' function.
class ListBillingGroupsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namePrefixFilter: Optional[str] = None


# This class is the input for the 'list_ca_certificates' function.
class ListCACertificatesRequest(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None


# This class is the input for the 'list_certificate_providers' function.
class ListCertificateProvidersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None


# This class is the input for the 'list_certificates_by_ca' function.
class ListCertificatesByCARequest(BaseValidatorModel):
    caCertificateId: str
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


# This class is the input for the 'list_certificates' function.
class ListCertificatesRequest(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class TimeFilter(BaseValidatorModel):
    after: Optional[str] = None
    before: Optional[str] = None


# This class is the input for the 'list_commands' function.
class ListCommandsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namespace: Optional[CommandNamespaceType] = None
    commandParameterName: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None


# This class is the input for the 'list_custom_metrics' function.
class ListCustomMetricsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_dimensions' function.
class ListDimensionsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_domain_configurations' function.
class ListDomainConfigurationsRequest(BaseValidatorModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    serviceType: Optional[ServiceTypeType] = None


# This class is the input for the 'list_fleet_metrics' function.
class ListFleetMetricsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_indices' function.
class ListIndicesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_job_executions_for_job' function.
class ListJobExecutionsForJobRequest(BaseValidatorModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_job_executions_for_thing' function.
class ListJobExecutionsForThingRequest(BaseValidatorModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    jobId: Optional[str] = None


# This class is the input for the 'list_job_templates' function.
class ListJobTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_jobs' function.
class ListJobsRequest(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None


# This class is the input for the 'list_managed_job_templates' function.
class ListManagedJobTemplatesRequest(BaseValidatorModel):
    templateName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedJobTemplateSummary(BaseValidatorModel):
    templateArn: Optional[str] = None
    templateName: Optional[str] = None
    description: Optional[str] = None
    environments: Optional[List[str]] = None
    templateVersion: Optional[str] = None


# This class is the input for the 'list_mitigation_actions' function.
class ListMitigationActionsRequest(BaseValidatorModel):
    actionType: Optional[MitigationActionTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MitigationActionIdentifier(BaseValidatorModel):
    actionName: Optional[str] = None
    actionArn: Optional[str] = None
    creationDate: Optional[datetime] = None


# This class is the input for the 'list_ota_updates' function.
class ListOTAUpdatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None


class OTAUpdateSummary(BaseValidatorModel):
    otaUpdateId: Optional[str] = None
    otaUpdateArn: Optional[str] = None
    creationDate: Optional[datetime] = None


# This class is the input for the 'list_outgoing_certificates' function.
class ListOutgoingCertificatesRequest(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class OutgoingCertificate(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    transferredTo: Optional[str] = None
    transferDate: Optional[datetime] = None
    transferMessage: Optional[str] = None
    creationDate: Optional[datetime] = None


# This class is the input for the 'list_package_versions' function.
class ListPackageVersionsRequest(BaseValidatorModel):
    packageName: str
    status: Optional[PackageVersionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PackageVersionSummary(BaseValidatorModel):
    packageName: Optional[str] = None
    versionName: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None


# This class is the input for the 'list_packages' function.
class ListPackagesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PackageSummary(BaseValidatorModel):
    packageName: Optional[str] = None
    defaultVersionName: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None


# This class is the input for the 'list_policies' function.
class ListPoliciesRequest(BaseValidatorModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None


# This class is the input for the 'list_policy_principals' function.
class ListPolicyPrincipalsRequest(BaseValidatorModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None


# This class is the input for the 'list_policy_versions' function.
class ListPolicyVersionsRequest(BaseValidatorModel):
    policyName: str


class PolicyVersion(BaseValidatorModel):
    versionId: Optional[str] = None
    isDefaultVersion: Optional[bool] = None
    createDate: Optional[datetime] = None


# This class is the input for the 'list_principal_policies' function.
class ListPrincipalPoliciesRequest(BaseValidatorModel):
    principal: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None


# This class is the input for the 'list_principal_things' function.
class ListPrincipalThingsRequest(BaseValidatorModel):
    principal: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_principal_things_v2' function.
class ListPrincipalThingsV2Request(BaseValidatorModel):
    principal: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class PrincipalThingObject(BaseValidatorModel):
    thingName: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


# This class is the input for the 'list_provisioning_template_versions' function.
class ListProvisioningTemplateVersionsRequest(BaseValidatorModel):
    templateName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ProvisioningTemplateVersionSummary(BaseValidatorModel):
    versionId: Optional[int] = None
    creationDate: Optional[datetime] = None
    isDefaultVersion: Optional[bool] = None


# This class is the input for the 'list_provisioning_templates' function.
class ListProvisioningTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ProvisioningTemplateSummary(BaseValidatorModel):
    templateArn: Optional[str] = None
    templateName: Optional[str] = None
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    enabled: Optional[bool] = None
    type: Optional[TemplateTypeType] = None


# This class is the input for the 'list_related_resources_for_audit_finding' function.
class ListRelatedResourcesForAuditFindingRequest(BaseValidatorModel):
    findingId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_role_aliases' function.
class ListRoleAliasesRequest(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


# This class is the input for the 'list_sbom_validation_results' function.
class ListSbomValidationResultsRequest(BaseValidatorModel):
    packageName: str
    versionName: str
    validationResult: Optional[SbomValidationResultType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SbomValidationResultSummary(BaseValidatorModel):
    fileName: Optional[str] = None
    validationResult: Optional[SbomValidationResultType] = None
    errorCode: Optional[SbomValidationErrorCodeType] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'list_scheduled_audits' function.
class ListScheduledAuditsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ScheduledAuditMetadata(BaseValidatorModel):
    scheduledAuditName: Optional[str] = None
    scheduledAuditArn: Optional[str] = None
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None


# This class is the input for the 'list_security_profiles_for_target' function.
class ListSecurityProfilesForTargetRequest(BaseValidatorModel):
    securityProfileTargetArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    recursive: Optional[bool] = None


# This class is the input for the 'list_security_profiles' function.
class ListSecurityProfilesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None


class SecurityProfileIdentifier(BaseValidatorModel):
    name: str
    arn: str


# This class is the input for the 'list_streams' function.
class ListStreamsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class StreamSummary(BaseValidatorModel):
    streamId: Optional[str] = None
    streamArn: Optional[str] = None
    streamVersion: Optional[int] = None
    description: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None


# This class is the input for the 'list_targets_for_policy' function.
class ListTargetsForPolicyRequest(BaseValidatorModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None


# This class is the input for the 'list_targets_for_security_profile' function.
class ListTargetsForSecurityProfileRequest(BaseValidatorModel):
    securityProfileName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SecurityProfileTarget(BaseValidatorModel):
    arn: str


# This class is the input for the 'list_thing_groups_for_thing' function.
class ListThingGroupsForThingRequest(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_thing_groups' function.
class ListThingGroupsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None


# This class is the input for the 'list_thing_principals' function.
class ListThingPrincipalsRequest(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_thing_principals_v2' function.
class ListThingPrincipalsV2Request(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class ThingPrincipalObject(BaseValidatorModel):
    principal: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


# This class is the input for the 'list_thing_registration_task_reports' function.
class ListThingRegistrationTaskReportsRequest(BaseValidatorModel):
    taskId: str
    reportType: ReportTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_thing_registration_tasks' function.
class ListThingRegistrationTasksRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[StatusType] = None


# This class is the input for the 'list_thing_types' function.
class ListThingTypesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingTypeName: Optional[str] = None


# This class is the input for the 'list_things_in_billing_group' function.
class ListThingsInBillingGroupRequest(BaseValidatorModel):
    billingGroupName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_things_in_thing_group' function.
class ListThingsInThingGroupRequest(BaseValidatorModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_things' function.
class ListThingsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    thingTypeName: Optional[str] = None
    usePrefixAttributeValue: Optional[bool] = None


class ThingAttribute(BaseValidatorModel):
    thingName: Optional[str] = None
    thingTypeName: Optional[str] = None
    thingArn: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    version: Optional[int] = None


# This class is the input for the 'list_topic_rule_destinations' function.
class ListTopicRuleDestinationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_topic_rules' function.
class ListTopicRulesRequest(BaseValidatorModel):
    topic: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ruleDisabled: Optional[bool] = None


class TopicRuleListItem(BaseValidatorModel):
    ruleArn: Optional[str] = None
    ruleName: Optional[str] = None
    topicPattern: Optional[str] = None
    createdAt: Optional[datetime] = None
    ruleDisabled: Optional[bool] = None


# This class is the input for the 'list_v2_logging_levels' function.
class ListV2LoggingLevelsRequest(BaseValidatorModel):
    targetType: Optional[LogTargetTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LocationTimestamp(BaseValidatorModel):
    value: str
    unit: Optional[str] = None


class LogTarget(BaseValidatorModel):
    targetType: LogTargetTypeType
    targetName: Optional[str] = None


class LoggingOptionsPayload(BaseValidatorModel):
    roleArn: str
    logLevel: Optional[LogLevelType] = None


class MetricValue(BaseValidatorModel):
    count: Optional[int] = None
    cidrs: Optional[List[str]] = None
    ports: Optional[List[int]] = None
    number: Optional[float] = None
    numbers: Optional[List[float]] = None
    strings: Optional[List[str]] = None


class PublishFindingToSnsParams(BaseValidatorModel):
    topicArn: str


class ReplaceDefaultPolicyVersionParams(BaseValidatorModel):
    templateName: Literal['BLANK_POLICY']


class UpdateCACertificateParams(BaseValidatorModel):
    action: Literal['DEACTIVATE']


class UpdateDeviceCertificateParams(BaseValidatorModel):
    action: Literal['DEACTIVATE']


class PropagatingAttribute(BaseValidatorModel):
    userPropertyKey: Optional[str] = None
    thingAttribute: Optional[str] = None
    connectionAttribute: Optional[str] = None


class UserProperty(BaseValidatorModel):
    key: str
    value: str


class PolicyVersionIdentifier(BaseValidatorModel):
    policyName: Optional[str] = None
    policyVersionId: Optional[str] = None


class PutVerificationStateOnViolationRequest(BaseValidatorModel):
    violationId: str
    verificationState: VerificationStateType
    verificationStateDescription: Optional[str] = None


# This class is the input for the 'register_certificate' function.
class RegisterCertificateRequest(BaseValidatorModel):
    certificatePem: str
    caCertificatePem: Optional[str] = None
    setAsActive: Optional[bool] = None
    status: Optional[CertificateStatusType] = None


# This class is the input for the 'register_certificate_without_ca' function.
class RegisterCertificateWithoutCARequest(BaseValidatorModel):
    certificatePem: str
    status: Optional[CertificateStatusType] = None


# This class is the input for the 'register_thing' function.
class RegisterThingRequest(BaseValidatorModel):
    templateBody: str
    parameters: Optional[Dict[str, str]] = None


# This class is the input for the 'reject_certificate_transfer' function.
class RejectCertificateTransferRequest(BaseValidatorModel):
    certificateId: str
    rejectReason: Optional[str] = None


class RemoveThingFromBillingGroupRequest(BaseValidatorModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None


class RemoveThingFromThingGroupRequest(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None


# This class is the input for the 'search_index' function.
class SearchIndexRequest(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    queryVersion: Optional[str] = None


class ThingGroupDocument(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    thingGroupDescription: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    parentGroupNames: Optional[List[str]] = None


# This class is the input for the 'set_default_authorizer' function.
class SetDefaultAuthorizerRequest(BaseValidatorModel):
    authorizerName: str


# This class is the input for the 'set_default_policy_version' function.
class SetDefaultPolicyVersionRequest(BaseValidatorModel):
    policyName: str
    policyVersionId: str


# This class is the input for the 'set_v2_logging_options' function.
class SetV2LoggingOptionsRequest(BaseValidatorModel):
    roleArn: Optional[str] = None
    defaultLogLevel: Optional[LogLevelType] = None
    disableAllLogs: Optional[bool] = None


class SigningProfileParameter(BaseValidatorModel):
    certificateArn: Optional[str] = None
    platform: Optional[str] = None
    certificatePathOnDevice: Optional[str] = None


# This class is the input for the 'start_on_demand_audit_task' function.
class StartOnDemandAuditTaskRequest(BaseValidatorModel):
    targetCheckNames: List[str]


# This class is the input for the 'start_thing_registration_task' function.
class StartThingRegistrationTaskRequest(BaseValidatorModel):
    templateBody: str
    inputFileBucket: str
    inputFileKey: str
    roleArn: str


class StopThingRegistrationTaskRequest(BaseValidatorModel):
    taskId: str


class TlsContext(BaseValidatorModel):
    serverName: Optional[str] = None


class ThingConnectivity(BaseValidatorModel):
    connected: Optional[bool] = None
    timestamp: Optional[int] = None
    disconnectReason: Optional[str] = None


class TimestreamDimension(BaseValidatorModel):
    name: str
    value: str


class TimestreamTimestamp(BaseValidatorModel):
    value: str
    unit: str


class VpcDestinationConfiguration(BaseValidatorModel):
    subnetIds: List[str]
    vpcId: str
    roleArn: str
    securityGroups: Optional[List[str]] = None


class VpcDestinationSummary(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    roleArn: Optional[str] = None


class VpcDestinationProperties(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    roleArn: Optional[str] = None


# This class is the input for the 'transfer_certificate' function.
class TransferCertificateRequest(BaseValidatorModel):
    certificateId: str
    targetAwsAccount: str
    transferMessage: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_authorizer' function.
class UpdateAuthorizerRequest(BaseValidatorModel):
    authorizerName: str
    authorizerFunctionArn: Optional[str] = None
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Dict[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    enableCachingForHttp: Optional[bool] = None


# This class is the input for the 'update_certificate_provider' function.
class UpdateCertificateProviderRequest(BaseValidatorModel):
    certificateProviderName: str
    lambdaFunctionArn: Optional[str] = None
    accountDefaultForOperations: Optional[List[Literal['CreateCertificateFromCsr']]] = None


# This class is the input for the 'update_certificate' function.
class UpdateCertificateRequest(BaseValidatorModel):
    certificateId: str
    newStatus: CertificateStatusType


# This class is the input for the 'update_command' function.
class UpdateCommandRequest(BaseValidatorModel):
    commandId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    deprecated: Optional[bool] = None


# This class is the input for the 'update_custom_metric' function.
class UpdateCustomMetricRequest(BaseValidatorModel):
    metricName: str
    displayName: str


# This class is the input for the 'update_dimension' function.
class UpdateDimensionRequest(BaseValidatorModel):
    name: str
    stringValues: List[str]


class UpdatePackageRequest(BaseValidatorModel):
    packageName: str
    description: Optional[str] = None
    defaultVersionName: Optional[str] = None
    unsetDefaultVersion: Optional[bool] = None
    clientToken: Optional[str] = None


# This class is the input for the 'update_role_alias' function.
class UpdateRoleAliasRequest(BaseValidatorModel):
    roleAlias: str
    roleArn: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None


# This class is the input for the 'update_scheduled_audit' function.
class UpdateScheduledAuditRequest(BaseValidatorModel):
    scheduledAuditName: str
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    targetCheckNames: Optional[List[str]] = None


class UpdateThingGroupsForThingRequest(BaseValidatorModel):
    thingName: Optional[str] = None
    thingGroupsToAdd: Optional[List[str]] = None
    thingGroupsToRemove: Optional[List[str]] = None
    overrideDynamicGroups: Optional[bool] = None


class UpdateTopicRuleDestinationRequest(BaseValidatorModel):
    arn: str
    status: TopicRuleDestinationStatusType


class ValidationError(BaseValidatorModel):
    errorMessage: Optional[str] = None


class AbortConfigOutput(BaseValidatorModel):
    criteriaList: List[AbortCriteria]


class AbortConfig(BaseValidatorModel):
    criteriaList: List[AbortCriteria]


class MetricDatum(BaseValidatorModel):
    timestamp: Optional[datetime] = None
    value: Optional[MetricValueOutput] = None

AggregationTypeUnion = Union[AggregationType, AggregationTypeOutput]


class Allowed(BaseValidatorModel):
    policies: Optional[List[Policy]] = None


class ExplicitDeny(BaseValidatorModel):
    policies: Optional[List[Policy]] = None


class ImplicitDeny(BaseValidatorModel):
    policies: Optional[List[Policy]] = None


class AssetPropertyValue(BaseValidatorModel):
    value: AssetPropertyVariant
    timestamp: AssetPropertyTimestamp
    quality: Optional[str] = None


# This class is the output for the 'associate_targets_with_job' function.
class AssociateTargetsWithJobResponse(BaseValidatorModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_job' function.
class CancelJobResponse(BaseValidatorModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_authorizer' function.
class CreateAuthorizerResponse(BaseValidatorModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_billing_group' function.
class CreateBillingGroupResponse(BaseValidatorModel):
    billingGroupName: str
    billingGroupArn: str
    billingGroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_certificate_from_csr' function.
class CreateCertificateFromCsrResponse(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    certificatePem: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_certificate_provider' function.
class CreateCertificateProviderResponse(BaseValidatorModel):
    certificateProviderName: str
    certificateProviderArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_command' function.
class CreateCommandResponse(BaseValidatorModel):
    commandId: str
    commandArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_custom_metric' function.
class CreateCustomMetricResponse(BaseValidatorModel):
    metricName: str
    metricArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_dimension' function.
class CreateDimensionResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain_configuration' function.
class CreateDomainConfigurationResponse(BaseValidatorModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_dynamic_thing_group' function.
class CreateDynamicThingGroupResponse(BaseValidatorModel):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str
    indexName: str
    queryString: str
    queryVersion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_fleet_metric' function.
class CreateFleetMetricResponse(BaseValidatorModel):
    metricName: str
    metricArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_job' function.
class CreateJobResponse(BaseValidatorModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_job_template' function.
class CreateJobTemplateResponse(BaseValidatorModel):
    jobTemplateArn: str
    jobTemplateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_mitigation_action' function.
class CreateMitigationActionResponse(BaseValidatorModel):
    actionArn: str
    actionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ota_update' function.
class CreateOTAUpdateResponse(BaseValidatorModel):
    otaUpdateId: str
    awsIotJobId: str
    otaUpdateArn: str
    awsIotJobArn: str
    otaUpdateStatus: OTAUpdateStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_package' function.
class CreatePackageResponse(BaseValidatorModel):
    packageName: str
    packageArn: str
    description: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_package_version' function.
class CreatePackageVersionResponse(BaseValidatorModel):
    packageVersionArn: str
    packageName: str
    versionName: str
    description: str
    attributes: Dict[str, str]
    status: PackageVersionStatusType
    errorReason: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_policy' function.
class CreatePolicyResponse(BaseValidatorModel):
    policyName: str
    policyArn: str
    policyDocument: str
    policyVersionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_policy_version' function.
class CreatePolicyVersionResponse(BaseValidatorModel):
    policyArn: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_provisioning_template' function.
class CreateProvisioningTemplateResponse(BaseValidatorModel):
    templateArn: str
    templateName: str
    defaultVersionId: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_provisioning_template_version' function.
class CreateProvisioningTemplateVersionResponse(BaseValidatorModel):
    templateArn: str
    templateName: str
    versionId: int
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_role_alias' function.
class CreateRoleAliasResponse(BaseValidatorModel):
    roleAlias: str
    roleAliasArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_scheduled_audit' function.
class CreateScheduledAuditResponse(BaseValidatorModel):
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_security_profile' function.
class CreateSecurityProfileResponse(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stream' function.
class CreateStreamResponse(BaseValidatorModel):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_thing_group' function.
class CreateThingGroupResponse(BaseValidatorModel):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_thing' function.
class CreateThingResponse(BaseValidatorModel):
    thingName: str
    thingArn: str
    thingId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_thing_type' function.
class CreateThingTypeResponse(BaseValidatorModel):
    thingTypeName: str
    thingTypeArn: str
    thingTypeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_command' function.
class DeleteCommandResponse(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_certificate_provider' function.
class DescribeCertificateProviderResponse(BaseValidatorModel):
    certificateProviderName: str
    certificateProviderArn: str
    lambdaFunctionArn: str
    accountDefaultForOperations: List[Literal['CreateCertificateFromCsr']]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_custom_metric' function.
class DescribeCustomMetricResponse(BaseValidatorModel):
    metricName: str
    metricArn: str
    metricType: CustomMetricTypeType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_dimension' function.
class DescribeDimensionResponse(BaseValidatorModel):
    name: str
    arn: str
    type: Literal['TOPIC_FILTER']
    stringValues: List[str]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_endpoint' function.
class DescribeEndpointResponse(BaseValidatorModel):
    endpointAddress: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fleet_metric' function.
class DescribeFleetMetricResponse(BaseValidatorModel):
    metricName: str
    queryString: str
    aggregationType: AggregationTypeOutput
    period: int
    aggregationField: str
    description: str
    queryVersion: str
    indexName: str
    creationDate: datetime
    lastModifiedDate: datetime
    unit: FleetMetricUnitType
    version: int
    metricArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_index' function.
class DescribeIndexResponse(BaseValidatorModel):
    indexName: str
    indexStatus: IndexStatusType
    schema: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_provisioning_template_version' function.
class DescribeProvisioningTemplateVersionResponse(BaseValidatorModel):
    versionId: int
    creationDate: datetime
    templateBody: str
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_scheduled_audit' function.
class DescribeScheduledAuditResponse(BaseValidatorModel):
    frequency: AuditFrequencyType
    dayOfMonth: str
    dayOfWeek: DayOfWeekType
    targetCheckNames: List[str]
    scheduledAuditName: str
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_thing_registration_task' function.
class DescribeThingRegistrationTaskResponse(BaseValidatorModel):
    taskId: str
    creationDate: datetime
    lastModifiedDate: datetime
    templateBody: str
    inputFileBucket: str
    inputFileKey: str
    roleArn: str
    status: StatusType
    message: str
    successCount: int
    failureCount: int
    percentageProgress: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_thing' function.
class DescribeThingResponse(BaseValidatorModel):
    defaultClientId: str
    thingName: str
    thingId: str
    thingArn: str
    thingTypeName: str
    attributes: Dict[str, str]
    version: int
    billingGroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_job' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cardinality' function.
class GetCardinalityResponse(BaseValidatorModel):
    cardinality: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_job_document' function.
class GetJobDocumentResponse(BaseValidatorModel):
    document: str
    ResponseMetadata: ResponseMetadata


class GetLoggingOptionsResponse(BaseValidatorModel):
    roleArn: str
    logLevel: LogLevelType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_package' function.
class GetPackageResponse(BaseValidatorModel):
    packageName: str
    packageArn: str
    description: str
    defaultVersionName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_policy' function.
class GetPolicyResponse(BaseValidatorModel):
    policyName: str
    policyArn: str
    policyDocument: str
    defaultVersionId: str
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_policy_version' function.
class GetPolicyVersionResponse(BaseValidatorModel):
    policyArn: str
    policyName: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str
    ResponseMetadata: ResponseMetadata


class GetRegistrationCodeResponse(BaseValidatorModel):
    registrationCode: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_thing_connectivity_data' function.
class GetThingConnectivityDataResponse(BaseValidatorModel):
    thingName: str
    connected: bool
    timestamp: datetime
    disconnectReason: DisconnectReasonValueType
    ResponseMetadata: ResponseMetadata


class GetV2LoggingOptionsResponse(BaseValidatorModel):
    roleArn: str
    defaultLogLevel: LogLevelType
    disableAllLogs: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attached_policies' function.
class ListAttachedPoliciesResponse(BaseValidatorModel):
    policies: List[Policy]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_custom_metrics' function.
class ListCustomMetricsResponse(BaseValidatorModel):
    metricNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_dimensions' function.
class ListDimensionsResponse(BaseValidatorModel):
    dimensionNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_indices' function.
class ListIndicesResponse(BaseValidatorModel):
    indexNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_policies' function.
class ListPoliciesResponse(BaseValidatorModel):
    policies: List[Policy]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_policy_principals' function.
class ListPolicyPrincipalsResponse(BaseValidatorModel):
    principals: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_principal_policies' function.
class ListPrincipalPoliciesResponse(BaseValidatorModel):
    policies: List[Policy]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_principal_things' function.
class ListPrincipalThingsResponse(BaseValidatorModel):
    things: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_role_aliases' function.
class ListRoleAliasesResponse(BaseValidatorModel):
    roleAliases: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_targets_for_policy' function.
class ListTargetsForPolicyResponse(BaseValidatorModel):
    targets: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_thing_principals' function.
class ListThingPrincipalsResponse(BaseValidatorModel):
    principals: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_thing_registration_task_reports' function.
class ListThingRegistrationTaskReportsResponse(BaseValidatorModel):
    resourceLinks: List[str]
    reportType: ReportTypeType
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_thing_registration_tasks' function.
class ListThingRegistrationTasksResponse(BaseValidatorModel):
    taskIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_things_in_billing_group' function.
class ListThingsInBillingGroupResponse(BaseValidatorModel):
    things: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_things_in_thing_group' function.
class ListThingsInThingGroupResponse(BaseValidatorModel):
    things: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'register_ca_certificate' function.
class RegisterCACertificateResponse(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_certificate' function.
class RegisterCertificateResponse(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_certificate_without_ca' function.
class RegisterCertificateWithoutCAResponse(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_thing' function.
class RegisterThingResponse(BaseValidatorModel):
    certificatePem: str
    resourceArns: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_default_authorizer' function.
class SetDefaultAuthorizerResponse(BaseValidatorModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_audit_mitigation_actions_task' function.
class StartAuditMitigationActionsTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_detect_mitigation_actions_task' function.
class StartDetectMitigationActionsTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_on_demand_audit_task' function.
class StartOnDemandAuditTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_thing_registration_task' function.
class StartThingRegistrationTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_invoke_authorizer' function.
class TestInvokeAuthorizerResponse(BaseValidatorModel):
    isAuthenticated: bool
    principalId: str
    policyDocuments: List[str]
    refreshAfterInSeconds: int
    disconnectAfterInSeconds: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'transfer_certificate' function.
class TransferCertificateResponse(BaseValidatorModel):
    transferredCertificateArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_authorizer' function.
class UpdateAuthorizerResponse(BaseValidatorModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_billing_group' function.
class UpdateBillingGroupResponse(BaseValidatorModel):
    version: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_certificate_provider' function.
class UpdateCertificateProviderResponse(BaseValidatorModel):
    certificateProviderName: str
    certificateProviderArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_command' function.
class UpdateCommandResponse(BaseValidatorModel):
    commandId: str
    displayName: str
    description: str
    deprecated: bool
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_custom_metric' function.
class UpdateCustomMetricResponse(BaseValidatorModel):
    metricName: str
    metricArn: str
    metricType: CustomMetricTypeType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_dimension' function.
class UpdateDimensionResponse(BaseValidatorModel):
    name: str
    arn: str
    type: Literal['TOPIC_FILTER']
    stringValues: List[str]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_configuration' function.
class UpdateDomainConfigurationResponse(BaseValidatorModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_dynamic_thing_group' function.
class UpdateDynamicThingGroupResponse(BaseValidatorModel):
    version: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_mitigation_action' function.
class UpdateMitigationActionResponse(BaseValidatorModel):
    actionArn: str
    actionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_role_alias' function.
class UpdateRoleAliasResponse(BaseValidatorModel):
    roleAlias: str
    roleAliasArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_scheduled_audit' function.
class UpdateScheduledAuditResponse(BaseValidatorModel):
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_stream' function.
class UpdateStreamResponse(BaseValidatorModel):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_thing_group' function.
class UpdateThingGroupResponse(BaseValidatorModel):
    version: int
    ResponseMetadata: ResponseMetadata


class ThingGroupPropertiesOutput(BaseValidatorModel):
    thingGroupDescription: Optional[str] = None
    attributePayload: Optional[AttributePayloadOutput] = None

AttributePayloadUnion = Union[AttributePayload, AttributePayloadOutput]


class ThingGroupProperties(BaseValidatorModel):
    thingGroupDescription: Optional[str] = None
    attributePayload: Optional[AttributePayload] = None

AuditCheckConfigurationUnion = Union[AuditCheckConfiguration, AuditCheckConfigurationOutput]


# This class is the output for the 'list_audit_mitigation_actions_executions' function.
class ListAuditMitigationActionsExecutionsResponse(BaseValidatorModel):
    actionsExecutions: List[AuditMitigationActionExecutionMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_audit_mitigation_actions_tasks' function.
class ListAuditMitigationActionsTasksResponse(BaseValidatorModel):
    tasks: List[AuditMitigationActionsTaskMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

AuditMitigationActionsTaskTargetUnion = Union[AuditMitigationActionsTaskTarget, AuditMitigationActionsTaskTargetOutput]


class DescribeAccountAuditConfigurationResponse(BaseValidatorModel):
    roleArn: str
    auditNotificationTargetConfigurations: Dict[Literal['SNS'], AuditNotificationTarget]
    auditCheckConfigurations: Dict[str, AuditCheckConfigurationOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_audit_tasks' function.
class ListAuditTasksResponse(BaseValidatorModel):
    tasks: List[AuditTaskMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

AuthInfoUnion = Union[AuthInfo, AuthInfoOutput]


# This class is the output for the 'describe_authorizer' function.
class DescribeAuthorizerResponse(BaseValidatorModel):
    authorizerDescription: AuthorizerDescription
    ResponseMetadata: ResponseMetadata


class DescribeDefaultAuthorizerResponse(BaseValidatorModel):
    authorizerDescription: AuthorizerDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_authorizers' function.
class ListAuthorizersResponse(BaseValidatorModel):
    authorizers: List[AuthorizerSummary]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


class AwsJobAbortConfig(BaseValidatorModel):
    abortCriteriaList: List[AwsJobAbortCriteria]


class AwsJobExponentialRolloutRate(BaseValidatorModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: AwsJobRateIncreaseCriteria


class BehaviorCriteriaOutput(BaseValidatorModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValueOutput] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThreshold] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfig] = None


# This class is the output for the 'get_behavior_model_training_summaries' function.
class GetBehaviorModelTrainingSummariesResponse(BaseValidatorModel):
    summaries: List[BehaviorModelTrainingSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MetricToRetain(BaseValidatorModel):
    metric: str
    metricDimension: Optional[MetricDimension] = None
    exportMetric: Optional[bool] = None


# This class is the output for the 'describe_billing_group' function.
class DescribeBillingGroupResponse(BaseValidatorModel):
    billingGroupName: str
    billingGroupId: str
    billingGroupArn: str
    version: int
    billingGroupProperties: BillingGroupProperties
    billingGroupMetadata: BillingGroupMetadata
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_billing_group' function.
class UpdateBillingGroupRequest(BaseValidatorModel):
    billingGroupName: str
    billingGroupProperties: BillingGroupProperties
    expectedVersion: Optional[int] = None


class CodeSigningSignature(BaseValidatorModel):
    inlineDocument: Optional[Blob] = None


class CommandParameterValue(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    I: Optional[int] = None
    L: Optional[int] = None
    D: Optional[float] = None
    BIN: Optional[Blob] = None
    UL: Optional[str] = None


class CommandPayload(BaseValidatorModel):
    content: Optional[Blob] = None
    contentType: Optional[str] = None


class MqttContext(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[Blob] = None
    clientId: Optional[str] = None


# This class is the output for the 'get_buckets_aggregation' function.
class GetBucketsAggregationResponse(BaseValidatorModel):
    totalCount: int
    buckets: List[Bucket]
    ResponseMetadata: ResponseMetadata


class BucketsAggregationType(BaseValidatorModel):
    termsAggregation: Optional[TermsAggregation] = None


class CACertificateDescription(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    status: Optional[CACertificateStatusType] = None
    certificatePem: Optional[str] = None
    ownedBy: Optional[str] = None
    creationDate: Optional[datetime] = None
    autoRegistrationStatus: Optional[AutoRegistrationStatusType] = None
    lastModifiedDate: Optional[datetime] = None
    customerVersion: Optional[int] = None
    generationId: Optional[str] = None
    validity: Optional[CertificateValidity] = None
    certificateMode: Optional[CertificateModeType] = None


# This class is the output for the 'list_ca_certificates' function.
class ListCACertificatesResponse(BaseValidatorModel):
    certificates: List[CACertificate]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


class CertificateDescription(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    caCertificateId: Optional[str] = None
    status: Optional[CertificateStatusType] = None
    certificatePem: Optional[str] = None
    ownedBy: Optional[str] = None
    previousOwnedBy: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    customerVersion: Optional[int] = None
    transferData: Optional[TransferData] = None
    generationId: Optional[str] = None
    validity: Optional[CertificateValidity] = None
    certificateMode: Optional[CertificateModeType] = None


# This class is the output for the 'list_certificate_providers' function.
class ListCertificateProvidersResponse(BaseValidatorModel):
    certificateProviders: List[CertificateProviderSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_certificates_by_ca' function.
class ListCertificatesByCAResponse(BaseValidatorModel):
    certificates: List[Certificate]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_certificates' function.
class ListCertificatesResponse(BaseValidatorModel):
    certificates: List[Certificate]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


class CustomCodeSigningOutput(BaseValidatorModel):
    signature: Optional[CodeSigningSignatureOutput] = None
    certificateChain: Optional[CodeSigningCertificateChain] = None
    hashAlgorithm: Optional[str] = None
    signatureAlgorithm: Optional[str] = None


# This class is the output for the 'list_command_executions' function.
class ListCommandExecutionsResponse(BaseValidatorModel):
    commandExecutions: List[CommandExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CommandParameterOutput(BaseValidatorModel):
    name: str
    value: Optional[CommandParameterValueOutput] = None
    defaultValue: Optional[CommandParameterValueOutput] = None
    description: Optional[str] = None


# This class is the output for the 'list_commands' function.
class ListCommandsResponse(BaseValidatorModel):
    commands: List[CommandSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeEventConfigurationsResponse(BaseValidatorModel):
    eventConfigurations: Dict[EventTypeType, Configuration]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


class UpdateEventConfigurationsRequest(BaseValidatorModel):
    eventConfigurations: Optional[Dict[EventTypeType, Configuration]] = None


# This class is the input for the 'list_audit_mitigation_actions_tasks' function.
class ListAuditMitigationActionsTasksRequest(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_audit_tasks' function.
class ListAuditTasksRequest(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_detect_mitigation_actions_executions' function.
class ListDetectMitigationActionsExecutionsRequest(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_detect_mitigation_actions_tasks' function.
class ListDetectMitigationActionsTasksRequest(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_metric_values' function.
class ListMetricValuesRequest(BaseValidatorModel):
    thingName: str
    metricName: str
    startTime: Timestamp
    endTime: Timestamp
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_violation_events' function.
class ListViolationEventsRequest(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ViolationEventOccurrenceRange(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp


# This class is the input for the 'create_authorizer' function.
class CreateAuthorizerRequest(BaseValidatorModel):
    authorizerName: str
    authorizerFunctionArn: str
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Dict[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    tags: Optional[List[Tag]] = None
    signingDisabled: Optional[bool] = None
    enableCachingForHttp: Optional[bool] = None


# This class is the input for the 'create_billing_group' function.
class CreateBillingGroupRequest(BaseValidatorModel):
    billingGroupName: str
    billingGroupProperties: Optional[BillingGroupProperties] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_certificate_provider' function.
class CreateCertificateProviderRequest(BaseValidatorModel):
    certificateProviderName: str
    lambdaFunctionArn: str
    accountDefaultForOperations: List[Literal['CreateCertificateFromCsr']]
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_custom_metric' function.
class CreateCustomMetricRequest(BaseValidatorModel):
    metricName: str
    metricType: CustomMetricTypeType
    clientRequestToken: str
    displayName: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_dimension' function.
class CreateDimensionRequest(BaseValidatorModel):
    name: str
    type: Literal['TOPIC_FILTER']
    stringValues: List[str]
    clientRequestToken: str
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_policy' function.
class CreatePolicyRequest(BaseValidatorModel):
    policyName: str
    policyDocument: str
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_role_alias' function.
class CreateRoleAliasRequest(BaseValidatorModel):
    roleAlias: str
    roleArn: str
    credentialDurationSeconds: Optional[int] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_scheduled_audit' function.
class CreateScheduledAuditRequest(BaseValidatorModel):
    frequency: AuditFrequencyType
    targetCheckNames: List[str]
    scheduledAuditName: str
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the input for the 'create_domain_configuration' function.
class CreateDomainConfigurationRequest(BaseValidatorModel):
    domainConfigurationName: str
    domainName: Optional[str] = None
    serverCertificateArns: Optional[List[str]] = None
    validationCertificateArn: Optional[str] = None
    authorizerConfig: Optional[AuthorizerConfig] = None
    serviceType: Optional[ServiceTypeType] = None
    tags: Optional[List[Tag]] = None
    tlsConfig: Optional[TlsConfig] = None
    serverCertificateConfig: Optional[ServerCertificateConfig] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    applicationProtocol: Optional[ApplicationProtocolType] = None
    clientCertificateConfig: Optional[ClientCertificateConfig] = None


# This class is the input for the 'update_domain_configuration' function.
class UpdateDomainConfigurationRequest(BaseValidatorModel):
    domainConfigurationName: str
    authorizerConfig: Optional[AuthorizerConfig] = None
    domainConfigurationStatus: Optional[DomainConfigurationStatusType] = None
    removeAuthorizerConfig: Optional[bool] = None
    tlsConfig: Optional[TlsConfig] = None
    serverCertificateConfig: Optional[ServerCertificateConfig] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    applicationProtocol: Optional[ApplicationProtocolType] = None
    clientCertificateConfig: Optional[ClientCertificateConfig] = None


class SchedulingConfigOutput(BaseValidatorModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    endBehavior: Optional[JobEndBehaviorType] = None
    maintenanceWindows: Optional[List[MaintenanceWindow]] = None


class SchedulingConfig(BaseValidatorModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    endBehavior: Optional[JobEndBehaviorType] = None
    maintenanceWindows: Optional[List[MaintenanceWindow]] = None


# This class is the output for the 'create_keys_and_certificate' function.
class CreateKeysAndCertificateResponse(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    certificatePem: str
    keyPair: KeyPair
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_provisioning_claim' function.
class CreateProvisioningClaimResponse(BaseValidatorModel):
    certificateId: str
    certificatePem: str
    keyPair: KeyPair
    expiration: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_provisioning_template' function.
class CreateProvisioningTemplateRequest(BaseValidatorModel):
    templateName: str
    templateBody: str
    provisioningRoleArn: str
    description: Optional[str] = None
    enabled: Optional[bool] = None
    preProvisioningHook: Optional[ProvisioningHook] = None
    tags: Optional[List[Tag]] = None
    type: Optional[TemplateTypeType] = None


# This class is the output for the 'describe_provisioning_template' function.
class DescribeProvisioningTemplateResponse(BaseValidatorModel):
    templateArn: str
    templateName: str
    description: str
    creationDate: datetime
    lastModifiedDate: datetime
    defaultVersionId: int
    templateBody: str
    enabled: bool
    provisioningRoleArn: str
    preProvisioningHook: ProvisioningHook
    type: TemplateTypeType
    ResponseMetadata: ResponseMetadata


class UpdateProvisioningTemplateRequest(BaseValidatorModel):
    templateName: str
    description: Optional[str] = None
    enabled: Optional[bool] = None
    defaultVersionId: Optional[int] = None
    provisioningRoleArn: Optional[str] = None
    preProvisioningHook: Optional[ProvisioningHook] = None
    removePreProvisioningHook: Optional[bool] = None


# This class is the output for the 'describe_audit_task' function.
class DescribeAuditTaskResponse(BaseValidatorModel):
    taskStatus: AuditTaskStatusType
    taskType: AuditTaskTypeType
    taskStartTime: datetime
    taskStatistics: TaskStatistics
    scheduledAuditName: str
    auditDetails: Dict[str, AuditCheckDetails]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'register_ca_certificate' function.
class RegisterCACertificateRequest(BaseValidatorModel):
    caCertificate: str
    verificationCertificate: Optional[str] = None
    setAsActive: Optional[bool] = None
    allowAutoRegistration: Optional[bool] = None
    registrationConfig: Optional[RegistrationConfig] = None
    tags: Optional[List[Tag]] = None
    certificateMode: Optional[CertificateModeType] = None


# This class is the input for the 'update_ca_certificate' function.
class UpdateCACertificateRequest(BaseValidatorModel):
    certificateId: str
    newStatus: Optional[CACertificateStatusType] = None
    newAutoRegistrationStatus: Optional[AutoRegistrationStatusType] = None
    registrationConfig: Optional[RegistrationConfig] = None
    removeAutoRegistration: Optional[bool] = None


# This class is the output for the 'describe_domain_configuration' function.
class DescribeDomainConfigurationResponse(BaseValidatorModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    domainName: str
    serverCertificates: List[ServerCertificateSummary]
    authorizerConfig: AuthorizerConfig
    domainConfigurationStatus: DomainConfigurationStatusType
    serviceType: ServiceTypeType
    domainType: DomainTypeType
    lastStatusChangeDate: datetime
    tlsConfig: TlsConfig
    serverCertificateConfig: ServerCertificateConfig
    authenticationType: AuthenticationTypeType
    applicationProtocol: ApplicationProtocolType
    clientCertificateConfig: ClientCertificateConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_managed_job_template' function.
class DescribeManagedJobTemplateResponse(BaseValidatorModel):
    templateName: str
    templateArn: str
    description: str
    templateVersion: str
    environments: List[str]
    documentParameters: List[DocumentParameter]
    document: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_role_alias' function.
class DescribeRoleAliasResponse(BaseValidatorModel):
    roleAliasDescription: RoleAliasDescription
    ResponseMetadata: ResponseMetadata


class Destination(BaseValidatorModel):
    s3Destination: Optional[S3Destination] = None


# This class is the output for the 'list_detect_mitigation_actions_executions' function.
class ListDetectMitigationActionsExecutionsResponse(BaseValidatorModel):
    actionsExecutions: List[DetectMitigationActionExecution]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

DetectMitigationActionsTaskTargetUnion = Union[DetectMitigationActionsTaskTarget, DetectMitigationActionsTaskTargetOutput]


# This class is the output for the 'list_domain_configurations' function.
class ListDomainConfigurationsResponse(BaseValidatorModel):
    domainConfigurations: List[DomainConfigurationSummary]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


class DynamoDBv2Action(BaseValidatorModel):
    roleArn: str
    putItem: PutItemInput


# This class is the output for the 'get_effective_policies' function.
class GetEffectivePoliciesResponse(BaseValidatorModel):
    effectivePolicies: List[EffectivePolicy]
    ResponseMetadata: ResponseMetadata


class ExponentialRolloutRate(BaseValidatorModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: RateIncreaseCriteria


class ThingGroupIndexingConfigurationOutput(BaseValidatorModel):
    thingGroupIndexingMode: ThingGroupIndexingModeType
    managedFields: Optional[List[Field]] = None
    customFields: Optional[List[Field]] = None


class ThingGroupIndexingConfiguration(BaseValidatorModel):
    thingGroupIndexingMode: ThingGroupIndexingModeType
    managedFields: Optional[List[Field]] = None
    customFields: Optional[List[Field]] = None


class PackageVersionArtifact(BaseValidatorModel):
    s3Location: Optional[S3Location] = None


class Sbom(BaseValidatorModel):
    s3Location: Optional[S3Location] = None


class StreamFile(BaseValidatorModel):
    fileId: Optional[int] = None
    s3Location: Optional[S3Location] = None


class FileLocation(BaseValidatorModel):
    stream: Optional[Stream] = None
    s3Location: Optional[S3Location] = None


# This class is the output for the 'list_fleet_metrics' function.
class ListFleetMetricsResponse(BaseValidatorModel):
    fleetMetrics: List[FleetMetricNameAndArn]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IndexingFilterOutput(BaseValidatorModel):
    namedShadowNames: Optional[List[str]] = None
    geoLocations: Optional[List[GeoLocationTarget]] = None


class IndexingFilter(BaseValidatorModel):
    namedShadowNames: Optional[List[str]] = None
    geoLocations: Optional[List[GeoLocationTarget]] = None


class GetBehaviorModelTrainingSummariesRequestPaginate(BaseValidatorModel):
    securityProfileName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListActiveViolationsRequestPaginate(BaseValidatorModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttachedPoliciesRequestPaginate(BaseValidatorModel):
    target: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAuditMitigationActionsExecutionsRequestPaginate(BaseValidatorModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAuditMitigationActionsTasksRequestPaginate(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAuditTasksRequestPaginate(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAuthorizersRequestPaginate(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBillingGroupsRequestPaginate(BaseValidatorModel):
    namePrefixFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCACertificatesRequestPaginate(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCertificatesByCARequestPaginate(BaseValidatorModel):
    caCertificateId: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCertificatesRequestPaginate(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCommandsRequestPaginate(BaseValidatorModel):
    namespace: Optional[CommandNamespaceType] = None
    commandParameterName: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomMetricsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDetectMitigationActionsExecutionsRequestPaginate(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDetectMitigationActionsTasksRequestPaginate(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDimensionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainConfigurationsRequestPaginate(BaseValidatorModel):
    serviceType: Optional[ServiceTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFleetMetricsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIndicesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobExecutionsForJobRequestPaginate(BaseValidatorModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobExecutionsForThingRequestPaginate(BaseValidatorModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    jobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobTemplatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedJobTemplatesRequestPaginate(BaseValidatorModel):
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMetricValuesRequestPaginate(BaseValidatorModel):
    thingName: str
    metricName: str
    startTime: Timestamp
    endTime: Timestamp
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMitigationActionsRequestPaginate(BaseValidatorModel):
    actionType: Optional[MitigationActionTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOTAUpdatesRequestPaginate(BaseValidatorModel):
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOutgoingCertificatesRequestPaginate(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackageVersionsRequestPaginate(BaseValidatorModel):
    packageName: str
    status: Optional[PackageVersionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackagesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPoliciesRequestPaginate(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPolicyPrincipalsRequestPaginate(BaseValidatorModel):
    policyName: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrincipalPoliciesRequestPaginate(BaseValidatorModel):
    principal: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrincipalThingsRequestPaginate(BaseValidatorModel):
    principal: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrincipalThingsV2RequestPaginate(BaseValidatorModel):
    principal: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisioningTemplateVersionsRequestPaginate(BaseValidatorModel):
    templateName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisioningTemplatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRelatedResourcesForAuditFindingRequestPaginate(BaseValidatorModel):
    findingId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoleAliasesRequestPaginate(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSbomValidationResultsRequestPaginate(BaseValidatorModel):
    packageName: str
    versionName: str
    validationResult: Optional[SbomValidationResultType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListScheduledAuditsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityProfilesForTargetRequestPaginate(BaseValidatorModel):
    securityProfileTargetArn: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityProfilesRequestPaginate(BaseValidatorModel):
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamsRequestPaginate(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetsForPolicyRequestPaginate(BaseValidatorModel):
    policyName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetsForSecurityProfileRequestPaginate(BaseValidatorModel):
    securityProfileName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingGroupsForThingRequestPaginate(BaseValidatorModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingGroupsRequestPaginate(BaseValidatorModel):
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingPrincipalsRequestPaginate(BaseValidatorModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingPrincipalsV2RequestPaginate(BaseValidatorModel):
    thingName: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingRegistrationTaskReportsRequestPaginate(BaseValidatorModel):
    taskId: str
    reportType: ReportTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingRegistrationTasksRequestPaginate(BaseValidatorModel):
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingTypesRequestPaginate(BaseValidatorModel):
    thingTypeName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingsInBillingGroupRequestPaginate(BaseValidatorModel):
    billingGroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingsInThingGroupRequestPaginate(BaseValidatorModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListThingsRequestPaginate(BaseValidatorModel):
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    thingTypeName: Optional[str] = None
    usePrefixAttributeValue: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTopicRuleDestinationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTopicRulesRequestPaginate(BaseValidatorModel):
    topic: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListV2LoggingLevelsRequestPaginate(BaseValidatorModel):
    targetType: Optional[LogTargetTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListViolationEventsRequestPaginate(BaseValidatorModel):
    startTime: Timestamp
    endTime: Timestamp
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_command_execution' function.
class GetCommandExecutionResponse(BaseValidatorModel):
    executionId: str
    commandArn: str
    targetArn: str
    status: CommandExecutionStatusType
    statusReason: StatusReason
    result: Dict[str, CommandExecutionResult]
    parameters: Dict[str, CommandParameterValueOutput]
    executionTimeoutSeconds: int
    createdAt: datetime
    lastUpdatedAt: datetime
    startedAt: datetime
    completedAt: datetime
    timeToLive: datetime
    ResponseMetadata: ResponseMetadata


class GetPackageConfigurationResponse(BaseValidatorModel):
    versionUpdateByJobsConfig: VersionUpdateByJobsConfig
    ResponseMetadata: ResponseMetadata


class UpdatePackageConfigurationRequest(BaseValidatorModel):
    versionUpdateByJobsConfig: Optional[VersionUpdateByJobsConfig] = None
    clientToken: Optional[str] = None


# This class is the output for the 'get_percentiles' function.
class GetPercentilesResponse(BaseValidatorModel):
    percentiles: List[PercentPair]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_statistics' function.
class GetStatisticsResponse(BaseValidatorModel):
    statistics: Statistics
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_billing_groups' function.
class ListBillingGroupsResponse(BaseValidatorModel):
    billingGroups: List[GroupNameAndArn]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_thing_groups_for_thing' function.
class ListThingGroupsForThingResponse(BaseValidatorModel):
    thingGroups: List[GroupNameAndArn]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_thing_groups' function.
class ListThingGroupsResponse(BaseValidatorModel):
    thingGroups: List[GroupNameAndArn]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ThingGroupMetadata(BaseValidatorModel):
    parentGroupName: Optional[str] = None
    rootToParentThingGroups: Optional[List[GroupNameAndArn]] = None
    creationDate: Optional[datetime] = None


class HttpAuthorization(BaseValidatorModel):
    sigv4: Optional[SigV4Authorization] = None


class JobExecution(BaseValidatorModel):
    jobId: Optional[str] = None
    status: Optional[JobExecutionStatusType] = None
    forceCanceled: Optional[bool] = None
    statusDetails: Optional[JobExecutionStatusDetails] = None
    thingArn: Optional[str] = None
    queuedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    executionNumber: Optional[int] = None
    versionNumber: Optional[int] = None
    approximateSecondsBeforeTimedOut: Optional[int] = None


class JobExecutionSummaryForJob(BaseValidatorModel):
    thingArn: Optional[str] = None
    jobExecutionSummary: Optional[JobExecutionSummary] = None


class JobExecutionSummaryForThing(BaseValidatorModel):
    jobId: Optional[str] = None
    jobExecutionSummary: Optional[JobExecutionSummary] = None


class JobExecutionsRetryConfigOutput(BaseValidatorModel):
    criteriaList: List[RetryCriteria]


class JobExecutionsRetryConfig(BaseValidatorModel):
    criteriaList: List[RetryCriteria]


# This class is the output for the 'list_jobs' function.
class ListJobsResponse(BaseValidatorModel):
    jobs: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_job_templates' function.
class ListJobTemplatesResponse(BaseValidatorModel):
    jobTemplates: List[JobTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class KafkaActionOutput(BaseValidatorModel):
    destinationArn: str
    topic: str
    clientProperties: Dict[str, str]
    key: Optional[str] = None
    partition: Optional[str] = None
    headers: Optional[List[KafkaActionHeader]] = None


class KafkaAction(BaseValidatorModel):
    destinationArn: str
    topic: str
    clientProperties: Dict[str, str]
    key: Optional[str] = None
    partition: Optional[str] = None
    headers: Optional[List[KafkaActionHeader]] = None


class ListCommandExecutionsRequestPaginate(BaseValidatorModel):
    namespace: Optional[CommandNamespaceType] = None
    status: Optional[CommandExecutionStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    startedTimeFilter: Optional[TimeFilter] = None
    completedTimeFilter: Optional[TimeFilter] = None
    targetArn: Optional[str] = None
    commandArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_command_executions' function.
class ListCommandExecutionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namespace: Optional[CommandNamespaceType] = None
    status: Optional[CommandExecutionStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    startedTimeFilter: Optional[TimeFilter] = None
    completedTimeFilter: Optional[TimeFilter] = None
    targetArn: Optional[str] = None
    commandArn: Optional[str] = None


# This class is the output for the 'list_managed_job_templates' function.
class ListManagedJobTemplatesResponse(BaseValidatorModel):
    managedJobTemplates: List[ManagedJobTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_mitigation_actions' function.
class ListMitigationActionsResponse(BaseValidatorModel):
    actionIdentifiers: List[MitigationActionIdentifier]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_ota_updates' function.
class ListOTAUpdatesResponse(BaseValidatorModel):
    otaUpdates: List[OTAUpdateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_outgoing_certificates' function.
class ListOutgoingCertificatesResponse(BaseValidatorModel):
    outgoingCertificates: List[OutgoingCertificate]
    nextMarker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_package_versions' function.
class ListPackageVersionsResponse(BaseValidatorModel):
    packageVersionSummaries: List[PackageVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_packages' function.
class ListPackagesResponse(BaseValidatorModel):
    packageSummaries: List[PackageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_policy_versions' function.
class ListPolicyVersionsResponse(BaseValidatorModel):
    policyVersions: List[PolicyVersion]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_principal_things_v2' function.
class ListPrincipalThingsV2Response(BaseValidatorModel):
    principalThingObjects: List[PrincipalThingObject]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_provisioning_template_versions' function.
class ListProvisioningTemplateVersionsResponse(BaseValidatorModel):
    versions: List[ProvisioningTemplateVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_provisioning_templates' function.
class ListProvisioningTemplatesResponse(BaseValidatorModel):
    templates: List[ProvisioningTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sbom_validation_results' function.
class ListSbomValidationResultsResponse(BaseValidatorModel):
    validationResultSummaries: List[SbomValidationResultSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_scheduled_audits' function.
class ListScheduledAuditsResponse(BaseValidatorModel):
    scheduledAudits: List[ScheduledAuditMetadata]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_security_profiles' function.
class ListSecurityProfilesResponse(BaseValidatorModel):
    securityProfileIdentifiers: List[SecurityProfileIdentifier]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_streams' function.
class ListStreamsResponse(BaseValidatorModel):
    streams: List[StreamSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_targets_for_security_profile' function.
class ListTargetsForSecurityProfileResponse(BaseValidatorModel):
    securityProfileTargets: List[SecurityProfileTarget]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SecurityProfileTargetMapping(BaseValidatorModel):
    securityProfileIdentifier: Optional[SecurityProfileIdentifier] = None
    target: Optional[SecurityProfileTarget] = None


# This class is the output for the 'list_thing_principals_v2' function.
class ListThingPrincipalsV2Response(BaseValidatorModel):
    thingPrincipalObjects: List[ThingPrincipalObject]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_things' function.
class ListThingsResponse(BaseValidatorModel):
    things: List[ThingAttribute]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_topic_rules' function.
class ListTopicRulesResponse(BaseValidatorModel):
    rules: List[TopicRuleListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LocationAction(BaseValidatorModel):
    roleArn: str
    trackerName: str
    deviceId: str
    latitude: str
    longitude: str
    timestamp: Optional[LocationTimestamp] = None


class LogTargetConfiguration(BaseValidatorModel):
    logTarget: Optional[LogTarget] = None
    logLevel: Optional[LogLevelType] = None


# This class is the input for the 'set_v2_logging_level' function.
class SetV2LoggingLevelRequest(BaseValidatorModel):
    logTarget: LogTarget
    logLevel: LogLevelType


# This class is the input for the 'set_logging_options' function.
class SetLoggingOptionsRequest(BaseValidatorModel):
    loggingOptionsPayload: LoggingOptionsPayload

MetricValueUnion = Union[MetricValue, MetricValueOutput]


class MitigationActionParamsOutput(BaseValidatorModel):
    updateDeviceCertificateParams: Optional[UpdateDeviceCertificateParams] = None
    updateCACertificateParams: Optional[UpdateCACertificateParams] = None
    addThingsToThingGroupParams: Optional[AddThingsToThingGroupParamsOutput] = None
    replaceDefaultPolicyVersionParams: Optional[ReplaceDefaultPolicyVersionParams] = None
    enableIoTLoggingParams: Optional[EnableIoTLoggingParams] = None
    publishFindingToSnsParams: Optional[PublishFindingToSnsParams] = None


class MitigationActionParams(BaseValidatorModel):
    updateDeviceCertificateParams: Optional[UpdateDeviceCertificateParams] = None
    updateCACertificateParams: Optional[UpdateCACertificateParams] = None
    addThingsToThingGroupParams: Optional[AddThingsToThingGroupParams] = None
    replaceDefaultPolicyVersionParams: Optional[ReplaceDefaultPolicyVersionParams] = None
    enableIoTLoggingParams: Optional[EnableIoTLoggingParams] = None
    publishFindingToSnsParams: Optional[PublishFindingToSnsParams] = None


class Mqtt5ConfigurationOutput(BaseValidatorModel):
    propagatingAttributes: Optional[List[PropagatingAttribute]] = None


class Mqtt5Configuration(BaseValidatorModel):
    propagatingAttributes: Optional[List[PropagatingAttribute]] = None


class MqttHeadersOutput(BaseValidatorModel):
    payloadFormatIndicator: Optional[str] = None
    contentType: Optional[str] = None
    responseTopic: Optional[str] = None
    correlationData: Optional[str] = None
    messageExpiry: Optional[str] = None
    userProperties: Optional[List[UserProperty]] = None


class MqttHeaders(BaseValidatorModel):
    payloadFormatIndicator: Optional[str] = None
    contentType: Optional[str] = None
    responseTopic: Optional[str] = None
    correlationData: Optional[str] = None
    messageExpiry: Optional[str] = None
    userProperties: Optional[List[UserProperty]] = None


class ResourceIdentifier(BaseValidatorModel):
    deviceCertificateId: Optional[str] = None
    caCertificateId: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    clientId: Optional[str] = None
    policyVersionIdentifier: Optional[PolicyVersionIdentifier] = None
    account: Optional[str] = None
    iamRoleArn: Optional[str] = None
    roleAliasArn: Optional[str] = None
    issuerCertificateIdentifier: Optional[IssuerCertificateIdentifier] = None
    deviceCertificateArn: Optional[str] = None


class ThingDocument(BaseValidatorModel):
    thingName: Optional[str] = None
    thingId: Optional[str] = None
    thingTypeName: Optional[str] = None
    thingGroupNames: Optional[List[str]] = None
    attributes: Optional[Dict[str, str]] = None
    shadow: Optional[str] = None
    deviceDefender: Optional[str] = None
    connectivity: Optional[ThingConnectivity] = None


class TimestreamActionOutput(BaseValidatorModel):
    roleArn: str
    databaseName: str
    tableName: str
    dimensions: List[TimestreamDimension]
    timestamp: Optional[TimestreamTimestamp] = None


class TimestreamAction(BaseValidatorModel):
    roleArn: str
    databaseName: str
    tableName: str
    dimensions: List[TimestreamDimension]
    timestamp: Optional[TimestreamTimestamp] = None


class TopicRuleDestinationConfiguration(BaseValidatorModel):
    httpUrlConfiguration: Optional[HttpUrlDestinationConfiguration] = None
    vpcConfiguration: Optional[VpcDestinationConfiguration] = None


class TopicRuleDestinationSummary(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[TopicRuleDestinationStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    statusReason: Optional[str] = None
    httpUrlSummary: Optional[HttpUrlDestinationSummary] = None
    vpcDestinationSummary: Optional[VpcDestinationSummary] = None


class TopicRuleDestination(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[TopicRuleDestinationStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    statusReason: Optional[str] = None
    httpUrlProperties: Optional[HttpUrlDestinationProperties] = None
    vpcProperties: Optional[VpcDestinationProperties] = None


# This class is the output for the 'validate_security_profile_behaviors' function.
class ValidateSecurityProfileBehaviorsResponse(BaseValidatorModel):
    valid: bool
    validationErrors: List[ValidationError]
    ResponseMetadata: ResponseMetadata

AbortConfigUnion = Union[AbortConfig, AbortConfigOutput]


# This class is the output for the 'list_metric_values' function.
class ListMetricValuesResponse(BaseValidatorModel):
    metricDatumList: List[MetricDatum]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_fleet_metric' function.
class CreateFleetMetricRequest(BaseValidatorModel):
    metricName: str
    queryString: str
    aggregationType: AggregationTypeUnion
    period: int
    aggregationField: str
    description: Optional[str] = None
    queryVersion: Optional[str] = None
    indexName: Optional[str] = None
    unit: Optional[FleetMetricUnitType] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_fleet_metric' function.
class UpdateFleetMetricRequest(BaseValidatorModel):
    metricName: str
    indexName: str
    queryString: Optional[str] = None
    aggregationType: Optional[AggregationTypeUnion] = None
    period: Optional[int] = None
    aggregationField: Optional[str] = None
    description: Optional[str] = None
    queryVersion: Optional[str] = None
    unit: Optional[FleetMetricUnitType] = None
    expectedVersion: Optional[int] = None


class Denied(BaseValidatorModel):
    implicitDeny: Optional[ImplicitDeny] = None
    explicitDeny: Optional[ExplicitDeny] = None


class PutAssetPropertyValueEntryOutput(BaseValidatorModel):
    propertyValues: List[AssetPropertyValue]
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class PutAssetPropertyValueEntry(BaseValidatorModel):
    propertyValues: List[AssetPropertyValue]
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


# This class is the input for the 'create_thing' function.
class CreateThingRequest(BaseValidatorModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadUnion] = None
    billingGroupName: Optional[str] = None


class UpdateThingRequest(BaseValidatorModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadUnion] = None
    expectedVersion: Optional[int] = None
    removeThingType: Optional[bool] = None

ThingGroupPropertiesUnion = Union[ThingGroupProperties, ThingGroupPropertiesOutput]


class UpdateAccountAuditConfigurationRequest(BaseValidatorModel):
    roleArn: Optional[str] = None
    auditNotificationTargetConfigurations: Optional[Dict[Literal['SNS'], AuditNotificationTarget]] = None
    auditCheckConfigurations: Optional[Dict[str, AuditCheckConfigurationUnion]] = None


# This class is the input for the 'start_audit_mitigation_actions_task' function.
class StartAuditMitigationActionsTaskRequest(BaseValidatorModel):
    taskId: str
    target: AuditMitigationActionsTaskTargetUnion
    auditCheckToActionsMapping: Dict[str, List[str]]
    clientRequestToken: str


# This class is the input for the 'test_authorization' function.
class TestAuthorizationRequest(BaseValidatorModel):
    authInfos: List[AuthInfoUnion]
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    clientId: Optional[str] = None
    policyNamesToAdd: Optional[List[str]] = None
    policyNamesToSkip: Optional[List[str]] = None


class AwsJobExecutionsRolloutConfig(BaseValidatorModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[AwsJobExponentialRolloutRate] = None


class BehaviorOutput(BaseValidatorModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimension] = None
    criteria: Optional[BehaviorCriteriaOutput] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None

CodeSigningSignatureUnion = Union[CodeSigningSignature, CodeSigningSignatureOutput]

CommandParameterValueUnion = Union[CommandParameterValue, CommandParameterValueOutput]

CommandPayloadUnion = Union[CommandPayload, CommandPayloadOutput]


# This class is the input for the 'test_invoke_authorizer' function.
class TestInvokeAuthorizerRequest(BaseValidatorModel):
    authorizerName: str
    token: Optional[str] = None
    tokenSignature: Optional[str] = None
    httpContext: Optional[HttpContext] = None
    mqttContext: Optional[MqttContext] = None
    tlsContext: Optional[TlsContext] = None


# This class is the input for the 'get_buckets_aggregation' function.
class GetBucketsAggregationRequest(BaseValidatorModel):
    queryString: str
    aggregationField: str
    bucketsAggregationType: BucketsAggregationType
    indexName: Optional[str] = None
    queryVersion: Optional[str] = None


# This class is the output for the 'describe_ca_certificate' function.
class DescribeCACertificateResponse(BaseValidatorModel):
    certificateDescription: CACertificateDescription
    registrationConfig: RegistrationConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_certificate' function.
class DescribeCertificateResponse(BaseValidatorModel):
    certificateDescription: CertificateDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_command' function.
class GetCommandResponse(BaseValidatorModel):
    commandId: str
    commandArn: str
    namespace: CommandNamespaceType
    displayName: str
    description: str
    mandatoryParameters: List[CommandParameterOutput]
    payload: CommandPayloadOutput
    roleArn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    deprecated: bool
    pendingDeletion: bool
    ResponseMetadata: ResponseMetadata

ViolationEventOccurrenceRangeUnion = Union[ViolationEventOccurrenceRange, ViolationEventOccurrenceRangeOutput]

SchedulingConfigUnion = Union[SchedulingConfig, SchedulingConfigOutput]


class StartSigningJobParameter(BaseValidatorModel):
    signingProfileParameter: Optional[SigningProfileParameter] = None
    signingProfileName: Optional[str] = None
    destination: Optional[Destination] = None


class JobExecutionsRolloutConfig(BaseValidatorModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[ExponentialRolloutRate] = None

ThingGroupIndexingConfigurationUnion = Union[ThingGroupIndexingConfiguration, ThingGroupIndexingConfigurationOutput]


# This class is the input for the 'create_package_version' function.
class CreatePackageVersionRequest(BaseValidatorModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    artifact: Optional[PackageVersionArtifact] = None
    recipe: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None


class UpdatePackageVersionRequest(BaseValidatorModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    artifact: Optional[PackageVersionArtifact] = None
    action: Optional[PackageVersionActionType] = None
    recipe: Optional[str] = None
    clientToken: Optional[str] = None


# This class is the input for the 'associate_sbom_with_package_version' function.
class AssociateSbomWithPackageVersionRequest(BaseValidatorModel):
    packageName: str
    versionName: str
    sbom: Sbom
    clientToken: Optional[str] = None


# This class is the output for the 'associate_sbom_with_package_version' function.
class AssociateSbomWithPackageVersionResponse(BaseValidatorModel):
    packageName: str
    versionName: str
    sbom: Sbom
    sbomValidationStatus: SbomValidationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_package_version' function.
class GetPackageVersionResponse(BaseValidatorModel):
    packageVersionArn: str
    packageName: str
    versionName: str
    description: str
    attributes: Dict[str, str]
    artifact: PackageVersionArtifact
    status: PackageVersionStatusType
    errorReason: str
    creationDate: datetime
    lastModifiedDate: datetime
    sbom: Sbom
    sbomValidationStatus: SbomValidationStatusType
    recipe: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_stream' function.
class CreateStreamRequest(BaseValidatorModel):
    streamId: str
    files: List[StreamFile]
    roleArn: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class StreamInfo(BaseValidatorModel):
    streamId: Optional[str] = None
    streamArn: Optional[str] = None
    streamVersion: Optional[int] = None
    description: Optional[str] = None
    files: Optional[List[StreamFile]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    roleArn: Optional[str] = None


# This class is the input for the 'update_stream' function.
class UpdateStreamRequest(BaseValidatorModel):
    streamId: str
    description: Optional[str] = None
    files: Optional[List[StreamFile]] = None
    roleArn: Optional[str] = None


class ThingIndexingConfigurationOutput(BaseValidatorModel):
    thingIndexingMode: ThingIndexingModeType
    thingConnectivityIndexingMode: Optional[ThingConnectivityIndexingModeType] = None
    deviceDefenderIndexingMode: Optional[DeviceDefenderIndexingModeType] = None
    namedShadowIndexingMode: Optional[NamedShadowIndexingModeType] = None
    managedFields: Optional[List[Field]] = None
    customFields: Optional[List[Field]] = None
    filter: Optional[IndexingFilterOutput] = None


class ThingIndexingConfiguration(BaseValidatorModel):
    thingIndexingMode: ThingIndexingModeType
    thingConnectivityIndexingMode: Optional[ThingConnectivityIndexingModeType] = None
    deviceDefenderIndexingMode: Optional[DeviceDefenderIndexingModeType] = None
    namedShadowIndexingMode: Optional[NamedShadowIndexingModeType] = None
    managedFields: Optional[List[Field]] = None
    customFields: Optional[List[Field]] = None
    filter: Optional[IndexingFilter] = None


# This class is the output for the 'describe_thing_group' function.
class DescribeThingGroupResponse(BaseValidatorModel):
    thingGroupName: str
    thingGroupId: str
    thingGroupArn: str
    version: int
    thingGroupProperties: ThingGroupPropertiesOutput
    thingGroupMetadata: ThingGroupMetadata
    indexName: str
    queryString: str
    queryVersion: str
    status: DynamicGroupStatusType
    ResponseMetadata: ResponseMetadata


class HttpActionOutput(BaseValidatorModel):
    url: str
    confirmationUrl: Optional[str] = None
    headers: Optional[List[HttpActionHeader]] = None
    auth: Optional[HttpAuthorization] = None


class HttpAction(BaseValidatorModel):
    url: str
    confirmationUrl: Optional[str] = None
    headers: Optional[List[HttpActionHeader]] = None
    auth: Optional[HttpAuthorization] = None


# This class is the output for the 'describe_job_execution' function.
class DescribeJobExecutionResponse(BaseValidatorModel):
    execution: JobExecution
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_job_executions_for_job' function.
class ListJobExecutionsForJobResponse(BaseValidatorModel):
    executionSummaries: List[JobExecutionSummaryForJob]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_job_executions_for_thing' function.
class ListJobExecutionsForThingResponse(BaseValidatorModel):
    executionSummaries: List[JobExecutionSummaryForThing]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

JobExecutionsRetryConfigUnion = Union[JobExecutionsRetryConfig, JobExecutionsRetryConfigOutput]

KafkaActionUnion = Union[KafkaAction, KafkaActionOutput]


# This class is the output for the 'list_security_profiles_for_target' function.
class ListSecurityProfilesForTargetResponse(BaseValidatorModel):
    securityProfileTargetMappings: List[SecurityProfileTargetMapping]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_v2_logging_levels' function.
class ListV2LoggingLevelsResponse(BaseValidatorModel):
    logTargetConfigurations: List[LogTargetConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BehaviorCriteria(BaseValidatorModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValueUnion] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThreshold] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfig] = None


# This class is the output for the 'describe_mitigation_action' function.
class DescribeMitigationActionResponse(BaseValidatorModel):
    actionName: str
    actionType: MitigationActionTypeType
    actionArn: str
    actionId: str
    roleArn: str
    actionParams: MitigationActionParamsOutput
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadata


class MitigationAction(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsOutput] = None

MitigationActionParamsUnion = Union[MitigationActionParams, MitigationActionParamsOutput]


class ThingTypePropertiesOutput(BaseValidatorModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[List[str]] = None
    mqtt5Configuration: Optional[Mqtt5ConfigurationOutput] = None


class ThingTypeProperties(BaseValidatorModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[List[str]] = None
    mqtt5Configuration: Optional[Mqtt5Configuration] = None


class RepublishActionOutput(BaseValidatorModel):
    roleArn: str
    topic: str
    qos: Optional[int] = None
    headers: Optional[MqttHeadersOutput] = None

MqttHeadersUnion = Union[MqttHeaders, MqttHeadersOutput]


class AuditSuppression(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifier
    expirationDate: Optional[datetime] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None


class CreateAuditSuppressionRequest(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifier
    clientRequestToken: str
    expirationDate: Optional[Timestamp] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None


class DeleteAuditSuppressionRequest(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifier


# This class is the input for the 'describe_audit_suppression' function.
class DescribeAuditSuppressionRequest(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifier


# This class is the output for the 'describe_audit_suppression' function.
class DescribeAuditSuppressionResponse(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifier
    expirationDate: datetime
    suppressIndefinitely: bool
    description: str
    ResponseMetadata: ResponseMetadata


class ListAuditFindingsRequestPaginate(BaseValidatorModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifier] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    listSuppressedFindings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_audit_findings' function.
class ListAuditFindingsRequest(BaseValidatorModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifier] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    listSuppressedFindings: Optional[bool] = None


class ListAuditSuppressionsRequestPaginate(BaseValidatorModel):
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifier] = None
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_audit_suppressions' function.
class ListAuditSuppressionsRequest(BaseValidatorModel):
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifier] = None
    ascendingOrder: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class NonCompliantResource(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceIdentifier: Optional[ResourceIdentifier] = None
    additionalInfo: Optional[Dict[str, str]] = None


class RelatedResource(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceIdentifier: Optional[ResourceIdentifier] = None
    additionalInfo: Optional[Dict[str, str]] = None


class UpdateAuditSuppressionRequest(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifier
    expirationDate: Optional[Timestamp] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None


# This class is the output for the 'search_index' function.
class SearchIndexResponse(BaseValidatorModel):
    things: List[ThingDocument]
    thingGroups: List[ThingGroupDocument]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

TimestreamActionUnion = Union[TimestreamAction, TimestreamActionOutput]


# This class is the input for the 'create_topic_rule_destination' function.
class CreateTopicRuleDestinationRequest(BaseValidatorModel):
    destinationConfiguration: TopicRuleDestinationConfiguration


# This class is the output for the 'list_topic_rule_destinations' function.
class ListTopicRuleDestinationsResponse(BaseValidatorModel):
    destinationSummaries: List[TopicRuleDestinationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_topic_rule_destination' function.
class CreateTopicRuleDestinationResponse(BaseValidatorModel):
    topicRuleDestination: TopicRuleDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_topic_rule_destination' function.
class GetTopicRuleDestinationResponse(BaseValidatorModel):
    topicRuleDestination: TopicRuleDestination
    ResponseMetadata: ResponseMetadata


class AuthResult(BaseValidatorModel):
    authInfo: Optional[AuthInfoOutput] = None
    allowed: Optional[Allowed] = None
    denied: Optional[Denied] = None
    authDecision: Optional[AuthDecisionType] = None
    missingContextValues: Optional[List[str]] = None


class IotSiteWiseActionOutput(BaseValidatorModel):
    putAssetPropertyValueEntries: List[PutAssetPropertyValueEntryOutput]
    roleArn: str

PutAssetPropertyValueEntryUnion = Union[PutAssetPropertyValueEntry, PutAssetPropertyValueEntryOutput]


# This class is the input for the 'create_dynamic_thing_group' function.
class CreateDynamicThingGroupRequest(BaseValidatorModel):
    thingGroupName: str
    queryString: str
    thingGroupProperties: Optional[ThingGroupPropertiesUnion] = None
    indexName: Optional[str] = None
    queryVersion: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_thing_group' function.
class CreateThingGroupRequest(BaseValidatorModel):
    thingGroupName: str
    parentGroupName: Optional[str] = None
    thingGroupProperties: Optional[ThingGroupPropertiesUnion] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_dynamic_thing_group' function.
class UpdateDynamicThingGroupRequest(BaseValidatorModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesUnion
    expectedVersion: Optional[int] = None
    indexName: Optional[str] = None
    queryString: Optional[str] = None
    queryVersion: Optional[str] = None


# This class is the input for the 'update_thing_group' function.
class UpdateThingGroupRequest(BaseValidatorModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesUnion
    expectedVersion: Optional[int] = None


class ActiveViolation(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorOutput] = None
    lastViolationValue: Optional[MetricValueOutput] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfo] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    lastViolationTime: Optional[datetime] = None
    violationStartTime: Optional[datetime] = None


# This class is the output for the 'describe_security_profile' function.
class DescribeSecurityProfileResponse(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List[BehaviorOutput]
    alertTargets: Dict[Literal['SNS'], AlertTarget]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List[MetricToRetain]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime
    metricsExportConfig: MetricsExportConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_security_profile' function.
class UpdateSecurityProfileResponse(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List[BehaviorOutput]
    alertTargets: Dict[Literal['SNS'], AlertTarget]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List[MetricToRetain]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime
    metricsExportConfig: MetricsExportConfig
    ResponseMetadata: ResponseMetadata


class ViolationEvent(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorOutput] = None
    metricValue: Optional[MetricValueOutput] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfo] = None
    violationEventType: Optional[ViolationEventTypeType] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    violationEventTime: Optional[datetime] = None


class CustomCodeSigning(BaseValidatorModel):
    signature: Optional[CodeSigningSignatureUnion] = None
    certificateChain: Optional[CodeSigningCertificateChain] = None
    hashAlgorithm: Optional[str] = None
    signatureAlgorithm: Optional[str] = None


class CommandParameter(BaseValidatorModel):
    name: str
    value: Optional[CommandParameterValueUnion] = None
    defaultValue: Optional[CommandParameterValueUnion] = None
    description: Optional[str] = None


# This class is the input for the 'start_detect_mitigation_actions_task' function.
class StartDetectMitigationActionsTaskRequest(BaseValidatorModel):
    taskId: str
    target: DetectMitigationActionsTaskTargetUnion
    actions: List[str]
    clientRequestToken: str
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeUnion] = None
    includeOnlyActiveViolations: Optional[bool] = None
    includeSuppressedAlerts: Optional[bool] = None


class CodeSigningOutput(BaseValidatorModel):
    awsSignerJobId: Optional[str] = None
    startSigningJobParameter: Optional[StartSigningJobParameter] = None
    customCodeSigning: Optional[CustomCodeSigningOutput] = None


# This class is the output for the 'describe_job_template' function.
class DescribeJobTemplateResponse(BaseValidatorModel):
    jobTemplateArn: str
    jobTemplateId: str
    description: str
    documentSource: str
    document: str
    createdAt: datetime
    presignedUrlConfig: PresignedUrlConfig
    jobExecutionsRolloutConfig: JobExecutionsRolloutConfig
    abortConfig: AbortConfigOutput
    timeoutConfig: TimeoutConfig
    jobExecutionsRetryConfig: JobExecutionsRetryConfigOutput
    maintenanceWindows: List[MaintenanceWindow]
    destinationPackageVersions: List[str]
    ResponseMetadata: ResponseMetadata


class Job(BaseValidatorModel):
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    targetSelection: Optional[TargetSelectionType] = None
    status: Optional[JobStatusType] = None
    forceCanceled: Optional[bool] = None
    reasonCode: Optional[str] = None
    comment: Optional[str] = None
    targets: Optional[List[str]] = None
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfig] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfig] = None
    abortConfig: Optional[AbortConfigOutput] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    jobProcessDetails: Optional[JobProcessDetails] = None
    timeoutConfig: Optional[TimeoutConfig] = None
    namespaceId: Optional[str] = None
    jobTemplateArn: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigOutput] = None
    documentParameters: Optional[Dict[str, str]] = None
    isConcurrent: Optional[bool] = None
    schedulingConfig: Optional[SchedulingConfigOutput] = None
    scheduledJobRollouts: Optional[List[ScheduledJobRollout]] = None
    destinationPackageVersions: Optional[List[str]] = None


# This class is the output for the 'describe_stream' function.
class DescribeStreamResponse(BaseValidatorModel):
    streamInfo: StreamInfo
    ResponseMetadata: ResponseMetadata


class GetIndexingConfigurationResponse(BaseValidatorModel):
    thingIndexingConfiguration: ThingIndexingConfigurationOutput
    thingGroupIndexingConfiguration: ThingGroupIndexingConfigurationOutput
    ResponseMetadata: ResponseMetadata

ThingIndexingConfigurationUnion = Union[ThingIndexingConfiguration, ThingIndexingConfigurationOutput]

HttpActionUnion = Union[HttpAction, HttpActionOutput]


# This class is the input for the 'create_job' function.
class CreateJobRequest(BaseValidatorModel):
    jobId: str
    targets: List[str]
    documentSource: Optional[str] = None
    document: Optional[str] = None
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfig] = None
    targetSelection: Optional[TargetSelectionType] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfig] = None
    abortConfig: Optional[AbortConfigUnion] = None
    timeoutConfig: Optional[TimeoutConfig] = None
    tags: Optional[List[Tag]] = None
    namespaceId: Optional[str] = None
    jobTemplateArn: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigUnion] = None
    documentParameters: Optional[Dict[str, str]] = None
    schedulingConfig: Optional[SchedulingConfigUnion] = None
    destinationPackageVersions: Optional[List[str]] = None


# This class is the input for the 'create_job_template' function.
class CreateJobTemplateRequest(BaseValidatorModel):
    jobTemplateId: str
    description: str
    jobArn: Optional[str] = None
    documentSource: Optional[str] = None
    document: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfig] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfig] = None
    abortConfig: Optional[AbortConfigUnion] = None
    timeoutConfig: Optional[TimeoutConfig] = None
    tags: Optional[List[Tag]] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigUnion] = None
    maintenanceWindows: Optional[List[MaintenanceWindow]] = None
    destinationPackageVersions: Optional[List[str]] = None


# This class is the input for the 'update_job' function.
class UpdateJobRequest(BaseValidatorModel):
    jobId: str
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfig] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfig] = None
    abortConfig: Optional[AbortConfigUnion] = None
    timeoutConfig: Optional[TimeoutConfig] = None
    namespaceId: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigUnion] = None

BehaviorCriteriaUnion = Union[BehaviorCriteria, BehaviorCriteriaOutput]


# This class is the output for the 'describe_audit_mitigation_actions_task' function.
class DescribeAuditMitigationActionsTaskResponse(BaseValidatorModel):
    taskStatus: AuditMitigationActionsTaskStatusType
    startTime: datetime
    endTime: datetime
    taskStatistics: Dict[str, TaskStatisticsForAuditCheck]
    target: AuditMitigationActionsTaskTargetOutput
    auditCheckToActionsMapping: Dict[str, List[str]]
    actionsDefinition: List[MitigationAction]
    ResponseMetadata: ResponseMetadata


class DetectMitigationActionsTaskSummary(BaseValidatorModel):
    taskId: Optional[str] = None
    taskStatus: Optional[DetectMitigationActionsTaskStatusType] = None
    taskStartTime: Optional[datetime] = None
    taskEndTime: Optional[datetime] = None
    target: Optional[DetectMitigationActionsTaskTargetOutput] = None
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeOutput] = None
    onlyActiveViolationsIncluded: Optional[bool] = None
    suppressedAlertsIncluded: Optional[bool] = None
    actionsDefinition: Optional[List[MitigationAction]] = None
    taskStatistics: Optional[DetectMitigationActionsTaskStatistics] = None


# This class is the input for the 'create_mitigation_action' function.
class CreateMitigationActionRequest(BaseValidatorModel):
    actionName: str
    roleArn: str
    actionParams: MitigationActionParamsUnion
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_mitigation_action' function.
class UpdateMitigationActionRequest(BaseValidatorModel):
    actionName: str
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsUnion] = None


# This class is the output for the 'describe_thing_type' function.
class DescribeThingTypeResponse(BaseValidatorModel):
    thingTypeName: str
    thingTypeId: str
    thingTypeArn: str
    thingTypeProperties: ThingTypePropertiesOutput
    thingTypeMetadata: ThingTypeMetadata
    ResponseMetadata: ResponseMetadata


class Thinginition(BaseValidatorModel):
    thingTypeName: Optional[str] = None
    thingTypeArn: Optional[str] = None
    thingTypeProperties: Optional[ThingTypePropertiesOutput] = None
    thingTypeMetadata: Optional[ThingTypeMetadata] = None

ThingTypePropertiesUnion = Union[ThingTypeProperties, ThingTypePropertiesOutput]


class RepublishAction(BaseValidatorModel):
    roleArn: str
    topic: str
    qos: Optional[int] = None
    headers: Optional[MqttHeadersUnion] = None


# This class is the output for the 'list_audit_suppressions' function.
class ListAuditSuppressionsResponse(BaseValidatorModel):
    suppressions: List[AuditSuppression]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AuditFinding(BaseValidatorModel):
    findingId: Optional[str] = None
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    taskStartTime: Optional[datetime] = None
    findingTime: Optional[datetime] = None
    severity: Optional[AuditFindingSeverityType] = None
    nonCompliantResource: Optional[NonCompliantResource] = None
    relatedResources: Optional[List[RelatedResource]] = None
    reasonForNonCompliance: Optional[str] = None
    reasonForNonComplianceCode: Optional[str] = None
    isSuppressed: Optional[bool] = None


# This class is the output for the 'list_related_resources_for_audit_finding' function.
class ListRelatedResourcesForAuditFindingResponse(BaseValidatorModel):
    relatedResources: List[RelatedResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'test_authorization' function.
class TestAuthorizationResponse(BaseValidatorModel):
    authResults: List[AuthResult]
    ResponseMetadata: ResponseMetadata


class ActionOutput(BaseValidatorModel):
    dynamoDB: Optional[DynamoDBAction] = None
    dynamoDBv2: Optional[DynamoDBv2Action] = None
    lambda_:Optional[LambdaAction] = None
    sns: Optional[SnsAction] = None
    sqs: Optional[SqsAction] = None
    kinesis: Optional[KinesisAction] = None
    republish: Optional[RepublishActionOutput] = None
    s3: Optional[S3Action] = None
    firehose: Optional[FirehoseAction] = None
    cloudwatchMetric: Optional[CloudwatchMetricAction] = None
    cloudwatchAlarm: Optional[CloudwatchAlarmAction] = None
    cloudwatchLogs: Optional[CloudwatchLogsAction] = None
    elasticsearch: Optional[ElasticsearchAction] = None
    salesforce: Optional[SalesforceAction] = None
    iotAnalytics: Optional[IotAnalyticsAction] = None
    iotEvents: Optional[IotEventsAction] = None
    iotSiteWise: Optional[IotSiteWiseActionOutput] = None
    stepFunctions: Optional[StepFunctionsAction] = None
    timestream: Optional[TimestreamActionOutput] = None
    http: Optional[HttpActionOutput] = None
    kafka: Optional[KafkaActionOutput] = None
    openSearch: Optional[OpenSearchAction] = None
    location: Optional[LocationAction] = None


class IotSiteWiseAction(BaseValidatorModel):
    putAssetPropertyValueEntries: List[PutAssetPropertyValueEntryUnion]
    roleArn: str


# This class is the output for the 'list_active_violations' function.
class ListActiveViolationsResponse(BaseValidatorModel):
    activeViolations: List[ActiveViolation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_violation_events' function.
class ListViolationEventsResponse(BaseValidatorModel):
    violationEvents: List[ViolationEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

CustomCodeSigningUnion = Union[CustomCodeSigning, CustomCodeSigningOutput]

CommandParameterUnion = Union[CommandParameter, CommandParameterOutput]


class OTAUpdateFileOutput(BaseValidatorModel):
    fileName: Optional[str] = None
    fileType: Optional[int] = None
    fileVersion: Optional[str] = None
    fileLocation: Optional[FileLocation] = None
    codeSigning: Optional[CodeSigningOutput] = None
    attributes: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_job' function.
class DescribeJobResponse(BaseValidatorModel):
    documentSource: str
    job: Job
    ResponseMetadata: ResponseMetadata


class UpdateIndexingConfigurationRequest(BaseValidatorModel):
    thingIndexingConfiguration: Optional[ThingIndexingConfigurationUnion] = None
    thingGroupIndexingConfiguration: Optional[ThingGroupIndexingConfigurationUnion] = None


class Behavior(BaseValidatorModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimension] = None
    criteria: Optional[BehaviorCriteriaUnion] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None


# This class is the output for the 'describe_detect_mitigation_actions_task' function.
class DescribeDetectMitigationActionsTaskResponse(BaseValidatorModel):
    taskSummary: DetectMitigationActionsTaskSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_detect_mitigation_actions_tasks' function.
class ListDetectMitigationActionsTasksResponse(BaseValidatorModel):
    tasks: List[DetectMitigationActionsTaskSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_thing_types' function.
class ListThingTypesResponse(BaseValidatorModel):
    thingTypes: List[Thinginition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_thing_type' function.
class CreateThingTypeRequest(BaseValidatorModel):
    thingTypeName: str
    thingTypeProperties: Optional[ThingTypePropertiesUnion] = None
    tags: Optional[List[Tag]] = None


class UpdateThingTypeRequest(BaseValidatorModel):
    thingTypeName: str
    thingTypeProperties: Optional[ThingTypePropertiesUnion] = None

RepublishActionUnion = Union[RepublishAction, RepublishActionOutput]


# This class is the output for the 'describe_audit_finding' function.
class DescribeAuditFindingResponse(BaseValidatorModel):
    finding: AuditFinding
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_audit_findings' function.
class ListAuditFindingsResponse(BaseValidatorModel):
    findings: List[AuditFinding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TopicRule(BaseValidatorModel):
    ruleName: Optional[str] = None
    sql: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    actions: Optional[List[ActionOutput]] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionOutput] = None

IotSiteWiseActionUnion = Union[IotSiteWiseAction, IotSiteWiseActionOutput]


class CodeSigning(BaseValidatorModel):
    awsSignerJobId: Optional[str] = None
    startSigningJobParameter: Optional[StartSigningJobParameter] = None
    customCodeSigning: Optional[CustomCodeSigningUnion] = None


# This class is the input for the 'create_command' function.
class CreateCommandRequest(BaseValidatorModel):
    commandId: str
    namespace: Optional[CommandNamespaceType] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    payload: Optional[CommandPayloadUnion] = None
    mandatoryParameters: Optional[List[CommandParameterUnion]] = None
    roleArn: Optional[str] = None
    tags: Optional[List[Tag]] = None


class OTAUpdateInfo(BaseValidatorModel):
    otaUpdateId: Optional[str] = None
    otaUpdateArn: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    description: Optional[str] = None
    targets: Optional[List[str]] = None
    protocols: Optional[List[ProtocolType]] = None
    awsJobExecutionsRolloutConfig: Optional[AwsJobExecutionsRolloutConfig] = None
    awsJobPresignedUrlConfig: Optional[AwsJobPresignedUrlConfig] = None
    targetSelection: Optional[TargetSelectionType] = None
    otaUpdateFiles: Optional[List[OTAUpdateFileOutput]] = None
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None
    awsIotJobId: Optional[str] = None
    awsIotJobArn: Optional[str] = None
    errorInfo: Optional[ErrorInfo] = None
    additionalParameters: Optional[Dict[str, str]] = None

BehaviorUnion = Union[Behavior, BehaviorOutput]


# This class is the output for the 'get_topic_rule' function.
class GetTopicRuleResponse(BaseValidatorModel):
    ruleArn: str
    rule: TopicRule
    ResponseMetadata: ResponseMetadata


class Action(BaseValidatorModel):
    dynamoDB: Optional[DynamoDBAction] = None
    dynamoDBv2: Optional[DynamoDBv2Action] = None
    lambda_:Optional[LambdaAction] = None
    sns: Optional[SnsAction] = None
    sqs: Optional[SqsAction] = None
    kinesis: Optional[KinesisAction] = None
    republish: Optional[RepublishActionUnion] = None
    s3: Optional[S3Action] = None
    firehose: Optional[FirehoseAction] = None
    cloudwatchMetric: Optional[CloudwatchMetricAction] = None
    cloudwatchAlarm: Optional[CloudwatchAlarmAction] = None
    cloudwatchLogs: Optional[CloudwatchLogsAction] = None
    elasticsearch: Optional[ElasticsearchAction] = None
    salesforce: Optional[SalesforceAction] = None
    iotAnalytics: Optional[IotAnalyticsAction] = None
    iotEvents: Optional[IotEventsAction] = None
    iotSiteWise: Optional[IotSiteWiseActionUnion] = None
    stepFunctions: Optional[StepFunctionsAction] = None
    timestream: Optional[TimestreamActionUnion] = None
    http: Optional[HttpActionUnion] = None
    kafka: Optional[KafkaActionUnion] = None
    openSearch: Optional[OpenSearchAction] = None
    location: Optional[LocationAction] = None

CodeSigningUnion = Union[CodeSigning, CodeSigningOutput]


# This class is the output for the 'get_ota_update' function.
class GetOTAUpdateResponse(BaseValidatorModel):
    otaUpdateInfo: OTAUpdateInfo
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_security_profile' function.
class CreateSecurityProfileRequest(BaseValidatorModel):
    securityProfileName: str
    securityProfileDescription: Optional[str] = None
    behaviors: Optional[List[BehaviorUnion]] = None
    alertTargets: Optional[Dict[Literal['SNS'], AlertTarget]] = None
    additionalMetricsToRetain: Optional[List[str]] = None
    additionalMetricsToRetainV2: Optional[List[MetricToRetain]] = None
    tags: Optional[List[Tag]] = None
    metricsExportConfig: Optional[MetricsExportConfig] = None


# This class is the input for the 'update_security_profile' function.
class UpdateSecurityProfileRequest(BaseValidatorModel):
    securityProfileName: str
    securityProfileDescription: Optional[str] = None
    behaviors: Optional[List[BehaviorUnion]] = None
    alertTargets: Optional[Dict[Literal['SNS'], AlertTarget]] = None
    additionalMetricsToRetain: Optional[List[str]] = None
    additionalMetricsToRetainV2: Optional[List[MetricToRetain]] = None
    deleteBehaviors: Optional[bool] = None
    deleteAlertTargets: Optional[bool] = None
    deleteAdditionalMetricsToRetain: Optional[bool] = None
    expectedVersion: Optional[int] = None
    metricsExportConfig: Optional[MetricsExportConfig] = None
    deleteMetricsExportConfig: Optional[bool] = None


# This class is the input for the 'validate_security_profile_behaviors' function.
class ValidateSecurityProfileBehaviorsRequest(BaseValidatorModel):
    behaviors: List[BehaviorUnion]

ActionUnion = Union[Action, ActionOutput]


class OTAUpdateFile(BaseValidatorModel):
    fileName: Optional[str] = None
    fileType: Optional[int] = None
    fileVersion: Optional[str] = None
    fileLocation: Optional[FileLocation] = None
    codeSigning: Optional[CodeSigningUnion] = None
    attributes: Optional[Dict[str, str]] = None


class TopicRulePayload(BaseValidatorModel):
    sql: str
    actions: List[ActionUnion]
    description: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionUnion] = None

OTAUpdateFileUnion = Union[OTAUpdateFile, OTAUpdateFileOutput]


# This class is the input for the 'create_topic_rule' function.
class CreateTopicRuleRequest(BaseValidatorModel):
    ruleName: str
    topicRulePayload: TopicRulePayload
    tags: Optional[str] = None


# This class is the input for the 'replace_topic_rule' function.
class ReplaceTopicRuleRequest(BaseValidatorModel):
    ruleName: str
    topicRulePayload: TopicRulePayload


# This class is the input for the 'create_ota_update' function.
class CreateOTAUpdateRequest(BaseValidatorModel):
    otaUpdateId: str
    targets: List[str]
    files: List[OTAUpdateFileUnion]
    roleArn: str
    description: Optional[str] = None
    protocols: Optional[List[ProtocolType]] = None
    targetSelection: Optional[TargetSelectionType] = None
    awsJobExecutionsRolloutConfig: Optional[AwsJobExecutionsRolloutConfig] = None
    awsJobPresignedUrlConfig: Optional[AwsJobPresignedUrlConfig] = None
    awsJobAbortConfig: Optional[AwsJobAbortConfig] = None
    awsJobTimeoutConfig: Optional[AwsJobTimeoutConfig] = None
    additionalParameters: Optional[Dict[str, str]] = None
    tags: Optional[List[Tag]] = None