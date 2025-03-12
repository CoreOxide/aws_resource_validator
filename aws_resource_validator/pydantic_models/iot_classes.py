from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.iot_constants import *

class AbortCriteriaTypeDef(BaseValidatorModel):
    failureType: JobExecutionFailureTypeType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int


class AcceptCertificateTransferRequestTypeDef(BaseValidatorModel):
    certificateId: str
    setAsActive: Optional[bool] = None


class CloudwatchAlarmActionTypeDef(BaseValidatorModel):
    roleArn: str
    alarmName: str
    stateReason: str
    stateValue: str


class CloudwatchLogsActionTypeDef(BaseValidatorModel):
    roleArn: str
    logGroupName: str
    batchMode: Optional[bool] = None


class CloudwatchMetricActionTypeDef(BaseValidatorModel):
    roleArn: str
    metricNamespace: str
    metricName: str
    metricValue: str
    metricUnit: str
    metricTimestamp: Optional[str] = None


class DynamoDBActionTypeDef(BaseValidatorModel):
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


class FirehoseActionTypeDef(BaseValidatorModel):
    roleArn: str
    deliveryStreamName: str
    separator: Optional[str] = None
    batchMode: Optional[bool] = None


class IotAnalyticsActionTypeDef(BaseValidatorModel):
    channelArn: Optional[str] = None
    channelName: Optional[str] = None
    batchMode: Optional[bool] = None
    roleArn: Optional[str] = None


class IotEventsActionTypeDef(BaseValidatorModel):
    inputName: str
    roleArn: str
    messageId: Optional[str] = None
    batchMode: Optional[bool] = None


class KinesisActionTypeDef(BaseValidatorModel):
    roleArn: str
    streamName: str
    partitionKey: Optional[str] = None


class LambdaActionTypeDef(BaseValidatorModel):
    functionArn: str


class S3ActionTypeDef(BaseValidatorModel):
    roleArn: str
    bucketName: str
    key: str
    cannedAcl: Optional[CannedAccessControlListType] = None


class SalesforceActionTypeDef(BaseValidatorModel):
    token: str
    url: str


class SnsActionTypeDef(BaseValidatorModel):
    targetArn: str
    roleArn: str
    messageFormat: Optional[MessageFormatType] = None


class SqsActionTypeDef(BaseValidatorModel):
    roleArn: str
    queueUrl: str
    useBase64: Optional[bool] = None


class StepFunctionsActionTypeDef(BaseValidatorModel):
    stateMachineName: str
    roleArn: str
    executionNamePrefix: Optional[str] = None


class MetricValueOutputTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    cidrs: Optional[List[str]] = None
    ports: Optional[List[int]] = None
    number: Optional[float] = None
    numbers: Optional[List[float]] = None
    strings: Optional[List[str]] = None


class ViolationEventAdditionalInfoTypeDef(BaseValidatorModel):
    confidenceLevel: Optional[ConfidenceLevelType] = None


class AddThingToBillingGroupRequestTypeDef(BaseValidatorModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None


class AddThingToThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None
    overrideDynamicGroups: Optional[bool] = None


class AddThingsToThingGroupParamsOutputTypeDef(BaseValidatorModel):
    thingGroupNames: List[str]
    overrideDynamicGroups: Optional[bool] = None


class AddThingsToThingGroupParamsTypeDef(BaseValidatorModel):
    thingGroupNames: Sequence[str]
    overrideDynamicGroups: Optional[bool] = None


class AggregationTypeOutputTypeDef(BaseValidatorModel):
    name: AggregationTypeNameType
    values: Optional[List[str]] = None


class AggregationTypeTypeDef(BaseValidatorModel):
    name: AggregationTypeNameType
    values: Optional[Sequence[str]] = None


class AlertTargetTypeDef(BaseValidatorModel):
    alertTargetArn: str
    roleArn: str


class PolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyArn: Optional[str] = None


class AssetPropertyTimestampTypeDef(BaseValidatorModel):
    timeInSeconds: str
    offsetInNanos: Optional[str] = None


class AssetPropertyVariantTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    integerValue: Optional[str] = None
    doubleValue: Optional[str] = None
    booleanValue: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateTargetsWithJobRequestTypeDef(BaseValidatorModel):
    targets: Sequence[str]
    jobId: str
    comment: Optional[str] = None
    namespaceId: Optional[str] = None


class AttachPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    target: str


class AttachPrincipalPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    principal: str


class AttachSecurityProfileRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileTargetArn: str


class AttachThingPrincipalRequestTypeDef(BaseValidatorModel):
    thingName: str
    principal: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class AttributePayloadOutputTypeDef(BaseValidatorModel):
    attributes: Optional[Dict[str, str]] = None
    merge: Optional[bool] = None


class AttributePayloadTypeDef(BaseValidatorModel):
    attributes: Optional[Mapping[str, str]] = None
    merge: Optional[bool] = None


class AuditCheckConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    configuration: Optional[Dict[ConfigNameType, str]] = None


class AuditCheckConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    configuration: Optional[Mapping[ConfigNameType, str]] = None


class AuditCheckDetailsTypeDef(BaseValidatorModel):
    checkRunStatus: Optional[AuditCheckRunStatusType] = None
    checkCompliant: Optional[bool] = None
    totalResourcesCount: Optional[int] = None
    nonCompliantResourcesCount: Optional[int] = None
    suppressedNonCompliantResourcesCount: Optional[int] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None


class AuditMitigationActionExecutionMetadataTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    findingId: Optional[str] = None
    actionName: Optional[str] = None
    actionId: Optional[str] = None
    status: Optional[AuditMitigationActionsExecutionStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None


class AuditMitigationActionsTaskMetadataTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    startTime: Optional[datetime] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None


class AuditMitigationActionsTaskTargetOutputTypeDef(BaseValidatorModel):
    auditTaskId: Optional[str] = None
    findingIds: Optional[List[str]] = None
    auditCheckToReasonCodeFilter: Optional[Dict[str, List[str]]] = None


class AuditMitigationActionsTaskTargetTypeDef(BaseValidatorModel):
    auditTaskId: Optional[str] = None
    findingIds: Optional[Sequence[str]] = None
    auditCheckToReasonCodeFilter: Optional[Mapping[str, Sequence[str]]] = None


class AuditNotificationTargetTypeDef(BaseValidatorModel):
    targetArn: Optional[str] = None
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None


class AuditTaskMetadataTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    taskType: Optional[AuditTaskTypeType] = None


class AuthInfoOutputTypeDef(BaseValidatorModel):
    resources: List[str]
    actionType: Optional[ActionTypeType] = None


class AuthInfoTypeDef(BaseValidatorModel):
    resources: Sequence[str]
    actionType: Optional[ActionTypeType] = None


class AuthorizerConfigTypeDef(BaseValidatorModel):
    defaultAuthorizerName: Optional[str] = None
    allowAuthorizerOverride: Optional[bool] = None


class AuthorizerDescriptionTypeDef(BaseValidatorModel):
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


class AuthorizerSummaryTypeDef(BaseValidatorModel):
    authorizerName: Optional[str] = None
    authorizerArn: Optional[str] = None


class AwsJobAbortCriteriaTypeDef(BaseValidatorModel):
    failureType: AwsJobAbortCriteriaFailureTypeType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int


class AwsJobRateIncreaseCriteriaTypeDef(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None


class AwsJobPresignedUrlConfigTypeDef(BaseValidatorModel):
    expiresInSec: Optional[int] = None


class AwsJobTimeoutConfigTypeDef(BaseValidatorModel):
    inProgressTimeoutInMinutes: Optional[int] = None


class MachineLearningDetectionConfigTypeDef(BaseValidatorModel):
    confidenceLevel: ConfidenceLevelType


class StatisticalThresholdTypeDef(BaseValidatorModel):
    statistic: Optional[str] = None


class BehaviorModelTrainingSummaryTypeDef(BaseValidatorModel):
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None
    trainingDataCollectionStartDate: Optional[datetime] = None
    modelStatus: Optional[ModelStatusType] = None
    datapointsCollectionPercentage: Optional[float] = None
    lastModelRefreshDate: Optional[datetime] = None


class BillingGroupMetadataTypeDef(BaseValidatorModel):
    creationDate: Optional[datetime] = None


class BillingGroupPropertiesTypeDef(BaseValidatorModel):
    billingGroupDescription: Optional[str] = None


class BucketTypeDef(BaseValidatorModel):
    keyValue: Optional[str] = None
    count: Optional[int] = None


class TermsAggregationTypeDef(BaseValidatorModel):
    maxBuckets: Optional[int] = None


class CertificateValidityTypeDef(BaseValidatorModel):
    notBefore: Optional[datetime] = None
    notAfter: Optional[datetime] = None


class CACertificateTypeDef(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    status: Optional[CACertificateStatusType] = None
    creationDate: Optional[datetime] = None


class CancelAuditMitigationActionsTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class CancelAuditTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class CancelCertificateTransferRequestTypeDef(BaseValidatorModel):
    certificateId: str


class CancelDetectMitigationActionsTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class CancelJobExecutionRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    force: Optional[bool] = None
    expectedVersion: Optional[int] = None
    statusDetails: Optional[Mapping[str, str]] = None


class CancelJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    reasonCode: Optional[str] = None
    comment: Optional[str] = None
    force: Optional[bool] = None


class TransferDataTypeDef(BaseValidatorModel):
    transferMessage: Optional[str] = None
    rejectReason: Optional[str] = None
    transferDate: Optional[datetime] = None
    acceptDate: Optional[datetime] = None
    rejectDate: Optional[datetime] = None


class CertificateProviderSummaryTypeDef(BaseValidatorModel):
    certificateProviderName: Optional[str] = None
    certificateProviderArn: Optional[str] = None


class CertificateTypeDef(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    status: Optional[CertificateStatusType] = None
    certificateMode: Optional[CertificateModeType] = None
    creationDate: Optional[datetime] = None


class ClientCertificateConfigTypeDef(BaseValidatorModel):
    clientCertificateCallbackArn: Optional[str] = None


class CodeSigningCertificateChainTypeDef(BaseValidatorModel):
    certificateName: Optional[str] = None
    inlineDocument: Optional[str] = None


class CodeSigningSignatureOutputTypeDef(BaseValidatorModel):
    inlineDocument: Optional[bytes] = None


class CommandExecutionResultTypeDef(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    BIN: Optional[bytes] = None


class CommandExecutionSummaryTypeDef(BaseValidatorModel):
    commandArn: Optional[str] = None
    executionId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[CommandExecutionStatusType] = None
    createdAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None


class CommandParameterValueOutputTypeDef(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    I: Optional[int] = None
    L: Optional[int] = None
    D: Optional[float] = None
    BIN: Optional[bytes] = None
    UL: Optional[str] = None


class CommandPayloadOutputTypeDef(BaseValidatorModel):
    content: Optional[bytes] = None
    contentType: Optional[str] = None


class CommandSummaryTypeDef(BaseValidatorModel):
    commandArn: Optional[str] = None
    commandId: Optional[str] = None
    displayName: Optional[str] = None
    deprecated: Optional[bool] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    pendingDeletion: Optional[bool] = None


class ConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None


class ConfirmTopicRuleDestinationRequestTypeDef(BaseValidatorModel):
    confirmationToken: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class CreateCertificateFromCsrRequestTypeDef(BaseValidatorModel):
    certificateSigningRequest: str
    setAsActive: Optional[bool] = None


class ServerCertificateConfigTypeDef(BaseValidatorModel):
    enableOCSPCheck: Optional[bool] = None
    ocspLambdaArn: Optional[str] = None
    ocspAuthorizedResponderArn: Optional[str] = None


class TlsConfigTypeDef(BaseValidatorModel):
    securityPolicy: Optional[str] = None


class PresignedUrlConfigTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    expiresInSec: Optional[int] = None


class TimeoutConfigTypeDef(BaseValidatorModel):
    inProgressTimeoutInMinutes: Optional[int] = None


class MaintenanceWindowTypeDef(BaseValidatorModel):
    startTime: str
    durationInMinutes: int


class CreateKeysAndCertificateRequestTypeDef(BaseValidatorModel):
    setAsActive: Optional[bool] = None


class KeyPairTypeDef(BaseValidatorModel):
    PublicKey: Optional[str] = None
    PrivateKey: Optional[str] = None


class CreatePackageRequestTypeDef(BaseValidatorModel):
    packageName: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class CreatePolicyVersionRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyDocument: str
    setAsDefault: Optional[bool] = None


class CreateProvisioningClaimRequestTypeDef(BaseValidatorModel):
    templateName: str


class ProvisioningHookTypeDef(BaseValidatorModel):
    targetArn: str
    payloadVersion: Optional[str] = None


class CreateProvisioningTemplateVersionRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateBody: str
    setAsDefault: Optional[bool] = None


class MetricsExportConfigTypeDef(BaseValidatorModel):
    mqttTopic: str
    roleArn: str


class DeleteAccountAuditConfigurationRequestTypeDef(BaseValidatorModel):
    deleteScheduledAudits: Optional[bool] = None


class DeleteAuthorizerRequestTypeDef(BaseValidatorModel):
    authorizerName: str


class DeleteBillingGroupRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    expectedVersion: Optional[int] = None


class DeleteCACertificateRequestTypeDef(BaseValidatorModel):
    certificateId: str


class DeleteCertificateProviderRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str


class DeleteCertificateRequestTypeDef(BaseValidatorModel):
    certificateId: str
    forceDelete: Optional[bool] = None


class DeleteCommandExecutionRequestTypeDef(BaseValidatorModel):
    executionId: str
    targetArn: str


class DeleteCommandRequestTypeDef(BaseValidatorModel):
    commandId: str


class DeleteCustomMetricRequestTypeDef(BaseValidatorModel):
    metricName: str


class DeleteDimensionRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteDomainConfigurationRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str


class DeleteDynamicThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None


class DeleteFleetMetricRequestTypeDef(BaseValidatorModel):
    metricName: str
    expectedVersion: Optional[int] = None


class DeleteJobExecutionRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    executionNumber: int
    force: Optional[bool] = None
    namespaceId: Optional[str] = None


class DeleteJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    force: Optional[bool] = None
    namespaceId: Optional[str] = None


class DeleteJobTemplateRequestTypeDef(BaseValidatorModel):
    jobTemplateId: str


class DeleteMitigationActionRequestTypeDef(BaseValidatorModel):
    actionName: str


class DeleteOTAUpdateRequestTypeDef(BaseValidatorModel):
    otaUpdateId: str
    deleteStream: Optional[bool] = None
    forceDeleteAWSJob: Optional[bool] = None


class DeletePackageRequestTypeDef(BaseValidatorModel):
    packageName: str
    clientToken: Optional[str] = None


class DeletePackageVersionRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    clientToken: Optional[str] = None


class DeletePolicyRequestTypeDef(BaseValidatorModel):
    policyName: str


class DeletePolicyVersionRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyVersionId: str


class DeleteProvisioningTemplateRequestTypeDef(BaseValidatorModel):
    templateName: str


class DeleteProvisioningTemplateVersionRequestTypeDef(BaseValidatorModel):
    templateName: str
    versionId: int


class DeleteRoleAliasRequestTypeDef(BaseValidatorModel):
    roleAlias: str


class DeleteScheduledAuditRequestTypeDef(BaseValidatorModel):
    scheduledAuditName: str


class DeleteSecurityProfileRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    expectedVersion: Optional[int] = None


class DeleteStreamRequestTypeDef(BaseValidatorModel):
    streamId: str


class DeleteThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None


class DeleteThingRequestTypeDef(BaseValidatorModel):
    thingName: str
    expectedVersion: Optional[int] = None


class DeleteThingTypeRequestTypeDef(BaseValidatorModel):
    thingTypeName: str


class DeleteTopicRuleDestinationRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteTopicRuleRequestTypeDef(BaseValidatorModel):
    ruleName: str


class DeleteV2LoggingLevelRequestTypeDef(BaseValidatorModel):
    targetType: LogTargetTypeType
    targetName: str


class DeprecateThingTypeRequestTypeDef(BaseValidatorModel):
    thingTypeName: str
    undoDeprecate: Optional[bool] = None


class DescribeAuditFindingRequestTypeDef(BaseValidatorModel):
    findingId: str


class DescribeAuditMitigationActionsTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class TaskStatisticsForAuditCheckTypeDef(BaseValidatorModel):
    totalFindingsCount: Optional[int] = None
    failedFindingsCount: Optional[int] = None
    succeededFindingsCount: Optional[int] = None
    skippedFindingsCount: Optional[int] = None
    canceledFindingsCount: Optional[int] = None


class DescribeAuditTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class TaskStatisticsTypeDef(BaseValidatorModel):
    totalChecks: Optional[int] = None
    inProgressChecks: Optional[int] = None
    waitingForDataCollectionChecks: Optional[int] = None
    compliantChecks: Optional[int] = None
    nonCompliantChecks: Optional[int] = None
    failedChecks: Optional[int] = None
    canceledChecks: Optional[int] = None


class DescribeAuthorizerRequestTypeDef(BaseValidatorModel):
    authorizerName: str


class DescribeBillingGroupRequestTypeDef(BaseValidatorModel):
    billingGroupName: str


class DescribeCACertificateRequestTypeDef(BaseValidatorModel):
    certificateId: str


class RegistrationConfigTypeDef(BaseValidatorModel):
    templateBody: Optional[str] = None
    roleArn: Optional[str] = None
    templateName: Optional[str] = None


class DescribeCertificateProviderRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str


class DescribeCertificateRequestTypeDef(BaseValidatorModel):
    certificateId: str


class DescribeCustomMetricRequestTypeDef(BaseValidatorModel):
    metricName: str


class DescribeDetectMitigationActionsTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class DescribeDimensionRequestTypeDef(BaseValidatorModel):
    name: str


class DescribeDomainConfigurationRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str


class ServerCertificateSummaryTypeDef(BaseValidatorModel):
    serverCertificateArn: Optional[str] = None
    serverCertificateStatus: Optional[ServerCertificateStatusType] = None
    serverCertificateStatusDetail: Optional[str] = None


class DescribeEndpointRequestTypeDef(BaseValidatorModel):
    endpointType: Optional[str] = None


class DescribeFleetMetricRequestTypeDef(BaseValidatorModel):
    metricName: str


class DescribeIndexRequestTypeDef(BaseValidatorModel):
    indexName: str


class DescribeJobExecutionRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    executionNumber: Optional[int] = None


class DescribeJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    beforeSubstitution: Optional[bool] = None


class DescribeJobTemplateRequestTypeDef(BaseValidatorModel):
    jobTemplateId: str


class DescribeManagedJobTemplateRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateVersion: Optional[str] = None


class DocumentParameterTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    description: Optional[str] = None
    regex: Optional[str] = None
    example: Optional[str] = None
    optional: Optional[bool] = None


class DescribeMitigationActionRequestTypeDef(BaseValidatorModel):
    actionName: str


class DescribeProvisioningTemplateRequestTypeDef(BaseValidatorModel):
    templateName: str


class DescribeProvisioningTemplateVersionRequestTypeDef(BaseValidatorModel):
    templateName: str
    versionId: int


class DescribeRoleAliasRequestTypeDef(BaseValidatorModel):
    roleAlias: str


class RoleAliasDescriptionTypeDef(BaseValidatorModel):
    roleAlias: Optional[str] = None
    roleAliasArn: Optional[str] = None
    roleArn: Optional[str] = None
    owner: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None


class DescribeScheduledAuditRequestTypeDef(BaseValidatorModel):
    scheduledAuditName: str


class DescribeSecurityProfileRequestTypeDef(BaseValidatorModel):
    securityProfileName: str


class DescribeStreamRequestTypeDef(BaseValidatorModel):
    streamId: str


class DescribeThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str


class DescribeThingRegistrationTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class DescribeThingRequestTypeDef(BaseValidatorModel):
    thingName: str


class DescribeThingTypeRequestTypeDef(BaseValidatorModel):
    thingTypeName: str


class ThingTypeMetadataTypeDef(BaseValidatorModel):
    deprecated: Optional[bool] = None
    deprecationDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None


class S3DestinationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class DetachPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    target: str


class DetachPrincipalPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    principal: str


class DetachSecurityProfileRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileTargetArn: str


class DetachThingPrincipalRequestTypeDef(BaseValidatorModel):
    thingName: str
    principal: str


class DetectMitigationActionExecutionTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    actionName: Optional[str] = None
    thingName: Optional[str] = None
    executionStartDate: Optional[datetime] = None
    executionEndDate: Optional[datetime] = None
    status: Optional[DetectMitigationActionExecutionStatusType] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None


class DetectMitigationActionsTaskStatisticsTypeDef(BaseValidatorModel):
    actionsExecuted: Optional[int] = None
    actionsSkipped: Optional[int] = None
    actionsFailed: Optional[int] = None


class DetectMitigationActionsTaskTargetOutputTypeDef(BaseValidatorModel):
    violationIds: Optional[List[str]] = None
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None


class ViolationEventOccurrenceRangeOutputTypeDef(BaseValidatorModel):
    startTime: datetime
    endTime: datetime


class DetectMitigationActionsTaskTargetTypeDef(BaseValidatorModel):
    violationIds: Optional[Sequence[str]] = None
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None


class DisableTopicRuleRequestTypeDef(BaseValidatorModel):
    ruleName: str


class DisassociateSbomFromPackageVersionRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    clientToken: Optional[str] = None


class DomainConfigurationSummaryTypeDef(BaseValidatorModel):
    domainConfigurationName: Optional[str] = None
    domainConfigurationArn: Optional[str] = None
    serviceType: Optional[ServiceTypeType] = None


class PutItemInputTypeDef(BaseValidatorModel):
    tableName: str


class EffectivePolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyArn: Optional[str] = None
    policyDocument: Optional[str] = None


class EnableIoTLoggingParamsTypeDef(BaseValidatorModel):
    roleArnForLogging: str
    logLevel: LogLevelType


class EnableTopicRuleRequestTypeDef(BaseValidatorModel):
    ruleName: str


class ErrorInfoTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class RateIncreaseCriteriaTypeDef(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None


class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    version: Optional[str] = None


class StreamTypeDef(BaseValidatorModel):
    streamId: Optional[str] = None
    fileId: Optional[int] = None


class FleetMetricNameAndArnTypeDef(BaseValidatorModel):
    metricName: Optional[str] = None
    metricArn: Optional[str] = None


class GeoLocationTargetTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    order: Optional[TargetFieldOrderType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetBehaviorModelTrainingSummariesRequestTypeDef(BaseValidatorModel):
    securityProfileName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetCardinalityRequestTypeDef(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None


class GetCommandExecutionRequestTypeDef(BaseValidatorModel):
    executionId: str
    targetArn: str
    includeResult: Optional[bool] = None


class StatusReasonTypeDef(BaseValidatorModel):
    reasonCode: str
    reasonDescription: Optional[str] = None


class GetCommandRequestTypeDef(BaseValidatorModel):
    commandId: str


class GetEffectivePoliciesRequestTypeDef(BaseValidatorModel):
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    thingName: Optional[str] = None


class GetJobDocumentRequestTypeDef(BaseValidatorModel):
    jobId: str
    beforeSubstitution: Optional[bool] = None


class GetOTAUpdateRequestTypeDef(BaseValidatorModel):
    otaUpdateId: str


class VersionUpdateByJobsConfigTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    roleArn: Optional[str] = None


class GetPackageRequestTypeDef(BaseValidatorModel):
    packageName: str


class GetPackageVersionRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str


class GetPercentilesRequestTypeDef(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None
    percents: Optional[Sequence[float]] = None


class PercentPairTypeDef(BaseValidatorModel):
    percent: Optional[float] = None
    value: Optional[float] = None


class GetPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str


class GetPolicyVersionRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyVersionId: str


class GetStatisticsRequestTypeDef(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None


class GetThingConnectivityDataRequestTypeDef(BaseValidatorModel):
    thingName: str


class GetTopicRuleDestinationRequestTypeDef(BaseValidatorModel):
    arn: str


class GetTopicRuleRequestTypeDef(BaseValidatorModel):
    ruleName: str


class GroupNameAndArnTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None
    groupArn: Optional[str] = None


class HttpActionHeaderTypeDef(BaseValidatorModel):
    key: str
    value: str


class SigV4AuthorizationTypeDef(BaseValidatorModel):
    signingRegion: str
    serviceName: str
    roleArn: str


class HttpContextTypeDef(BaseValidatorModel):
    headers: Optional[Mapping[str, str]] = None
    queryString: Optional[str] = None


class HttpUrlDestinationConfigurationTypeDef(BaseValidatorModel):
    confirmationUrl: str


class HttpUrlDestinationPropertiesTypeDef(BaseValidatorModel):
    confirmationUrl: Optional[str] = None


class HttpUrlDestinationSummaryTypeDef(BaseValidatorModel):
    confirmationUrl: Optional[str] = None


class IssuerCertificateIdentifierTypeDef(BaseValidatorModel):
    issuerCertificateSubject: Optional[str] = None
    issuerId: Optional[str] = None
    issuerCertificateSerialNumber: Optional[str] = None


class JobExecutionStatusDetailsTypeDef(BaseValidatorModel):
    detailsMap: Optional[Dict[str, str]] = None


class JobExecutionSummaryTypeDef(BaseValidatorModel):
    status: Optional[JobExecutionStatusType] = None
    queuedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    executionNumber: Optional[int] = None
    retryAttempt: Optional[int] = None


class RetryCriteriaTypeDef(BaseValidatorModel):
    failureType: RetryableFailureTypeType
    numberOfRetries: int


class JobProcessDetailsTypeDef(BaseValidatorModel):
    processingTargets: Optional[List[str]] = None
    numberOfCanceledThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None
    numberOfFailedThings: Optional[int] = None
    numberOfRejectedThings: Optional[int] = None
    numberOfQueuedThings: Optional[int] = None
    numberOfInProgressThings: Optional[int] = None
    numberOfRemovedThings: Optional[int] = None
    numberOfTimedOutThings: Optional[int] = None


class JobSummaryTypeDef(BaseValidatorModel):
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    thingGroupId: Optional[str] = None
    targetSelection: Optional[TargetSelectionType] = None
    status: Optional[JobStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    isConcurrent: Optional[bool] = None


class JobTemplateSummaryTypeDef(BaseValidatorModel):
    jobTemplateArn: Optional[str] = None
    jobTemplateId: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None


class ScheduledJobRolloutTypeDef(BaseValidatorModel):
    startTime: Optional[str] = None


class KafkaActionHeaderTypeDef(BaseValidatorModel):
    key: str
    value: str


class ListActiveViolationsRequestTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttachedPoliciesRequestTypeDef(BaseValidatorModel):
    target: str
    recursive: Optional[bool] = None
    marker: Optional[str] = None
    pageSize: Optional[int] = None


class ListAuditMitigationActionsExecutionsRequestTypeDef(BaseValidatorModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAuthorizersRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None


class ListBillingGroupsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namePrefixFilter: Optional[str] = None


class ListCACertificatesRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None


class ListCertificateProvidersRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class ListCertificatesByCARequestTypeDef(BaseValidatorModel):
    caCertificateId: str
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class ListCertificatesRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class TimeFilterTypeDef(BaseValidatorModel):
    after: Optional[str] = None
    before: Optional[str] = None


class ListCommandsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namespace: Optional[CommandNamespaceType] = None
    commandParameterName: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None


class ListCustomMetricsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDimensionsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDomainConfigurationsRequestTypeDef(BaseValidatorModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    serviceType: Optional[ServiceTypeType] = None


class ListFleetMetricsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListIndicesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListJobExecutionsForJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobExecutionsForThingRequestTypeDef(BaseValidatorModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    jobId: Optional[str] = None


class ListJobTemplatesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None


class ListManagedJobTemplatesRequestTypeDef(BaseValidatorModel):
    templateName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedJobTemplateSummaryTypeDef(BaseValidatorModel):
    templateArn: Optional[str] = None
    templateName: Optional[str] = None
    description: Optional[str] = None
    environments: Optional[List[str]] = None
    templateVersion: Optional[str] = None


class ListMitigationActionsRequestTypeDef(BaseValidatorModel):
    actionType: Optional[MitigationActionTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MitigationActionIdentifierTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    actionArn: Optional[str] = None
    creationDate: Optional[datetime] = None


class ListOTAUpdatesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None


class OTAUpdateSummaryTypeDef(BaseValidatorModel):
    otaUpdateId: Optional[str] = None
    otaUpdateArn: Optional[str] = None
    creationDate: Optional[datetime] = None


class ListOutgoingCertificatesRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class OutgoingCertificateTypeDef(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    transferredTo: Optional[str] = None
    transferDate: Optional[datetime] = None
    transferMessage: Optional[str] = None
    creationDate: Optional[datetime] = None


class ListPackageVersionsRequestTypeDef(BaseValidatorModel):
    packageName: str
    status: Optional[PackageVersionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PackageVersionSummaryTypeDef(BaseValidatorModel):
    packageName: Optional[str] = None
    versionName: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None


class ListPackagesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PackageSummaryTypeDef(BaseValidatorModel):
    packageName: Optional[str] = None
    defaultVersionName: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None


class ListPoliciesRequestTypeDef(BaseValidatorModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None


class ListPolicyPrincipalsRequestTypeDef(BaseValidatorModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None


class ListPolicyVersionsRequestTypeDef(BaseValidatorModel):
    policyName: str


class PolicyVersionTypeDef(BaseValidatorModel):
    versionId: Optional[str] = None
    isDefaultVersion: Optional[bool] = None
    createDate: Optional[datetime] = None


class ListPrincipalPoliciesRequestTypeDef(BaseValidatorModel):
    principal: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None


class ListPrincipalThingsRequestTypeDef(BaseValidatorModel):
    principal: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPrincipalThingsV2RequestTypeDef(BaseValidatorModel):
    principal: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class PrincipalThingObjectTypeDef(BaseValidatorModel):
    thingName: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class ListProvisioningTemplateVersionsRequestTypeDef(BaseValidatorModel):
    templateName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ProvisioningTemplateVersionSummaryTypeDef(BaseValidatorModel):
    versionId: Optional[int] = None
    creationDate: Optional[datetime] = None
    isDefaultVersion: Optional[bool] = None


class ListProvisioningTemplatesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRelatedResourcesForAuditFindingRequestTypeDef(BaseValidatorModel):
    findingId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRoleAliasesRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class ListSbomValidationResultsRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    validationResult: Optional[SbomValidationResultType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SbomValidationResultSummaryTypeDef(BaseValidatorModel):
    fileName: Optional[str] = None
    validationResult: Optional[SbomValidationResultType] = None
    errorCode: Optional[SbomValidationErrorCodeType] = None
    errorMessage: Optional[str] = None


class ListScheduledAuditsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ScheduledAuditMetadataTypeDef(BaseValidatorModel):
    scheduledAuditName: Optional[str] = None
    scheduledAuditArn: Optional[str] = None
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None


class ListSecurityProfilesForTargetRequestTypeDef(BaseValidatorModel):
    securityProfileTargetArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    recursive: Optional[bool] = None


class ListSecurityProfilesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None


class SecurityProfileIdentifierTypeDef(BaseValidatorModel):
    name: str
    arn: str


class ListStreamsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None


class StreamSummaryTypeDef(BaseValidatorModel):
    streamId: Optional[str] = None
    streamArn: Optional[str] = None
    streamVersion: Optional[int] = None
    description: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None


class ListTargetsForPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None


class ListTargetsForSecurityProfileRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SecurityProfileTargetTypeDef(BaseValidatorModel):
    arn: str


class ListThingGroupsForThingRequestTypeDef(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListThingGroupsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None


class ListThingPrincipalsRequestTypeDef(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListThingPrincipalsV2RequestTypeDef(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class ThingPrincipalObjectTypeDef(BaseValidatorModel):
    principal: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None


class ListThingRegistrationTaskReportsRequestTypeDef(BaseValidatorModel):
    taskId: str
    reportType: ReportTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListThingRegistrationTasksRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[StatusType] = None


class ListThingTypesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingTypeName: Optional[str] = None


class ListThingsInBillingGroupRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListThingsInThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListThingsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    thingTypeName: Optional[str] = None
    usePrefixAttributeValue: Optional[bool] = None


class ThingAttributeTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    thingTypeName: Optional[str] = None
    thingArn: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    version: Optional[int] = None


class ListTopicRuleDestinationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTopicRulesRequestTypeDef(BaseValidatorModel):
    topic: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ruleDisabled: Optional[bool] = None


class TopicRuleListItemTypeDef(BaseValidatorModel):
    ruleArn: Optional[str] = None
    ruleName: Optional[str] = None
    topicPattern: Optional[str] = None
    createdAt: Optional[datetime] = None
    ruleDisabled: Optional[bool] = None


class ListV2LoggingLevelsRequestTypeDef(BaseValidatorModel):
    targetType: Optional[LogTargetTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LocationTimestampTypeDef(BaseValidatorModel):
    value: str
    unit: Optional[str] = None


class LogTargetTypeDef(BaseValidatorModel):
    targetType: LogTargetTypeType
    targetName: Optional[str] = None


class LoggingOptionsPayloadTypeDef(BaseValidatorModel):
    roleArn: str
    logLevel: Optional[LogLevelType] = None


class MetricValueTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    cidrs: Optional[Sequence[str]] = None
    ports: Optional[Sequence[int]] = None
    number: Optional[float] = None
    numbers: Optional[Sequence[float]] = None
    strings: Optional[Sequence[str]] = None


class PublishFindingToSnsParamsTypeDef(BaseValidatorModel):
    topicArn: str


class ReplaceDefaultPolicyVersionParamsTypeDef(BaseValidatorModel):
    templateName: Literal["BLANK_POLICY"]


class UpdateCACertificateParamsTypeDef(BaseValidatorModel):
    action: Literal["DEACTIVATE"]


class UpdateDeviceCertificateParamsTypeDef(BaseValidatorModel):
    action: Literal["DEACTIVATE"]


class PropagatingAttributeTypeDef(BaseValidatorModel):
    userPropertyKey: Optional[str] = None
    thingAttribute: Optional[str] = None
    connectionAttribute: Optional[str] = None


class UserPropertyTypeDef(BaseValidatorModel):
    key: str
    value: str


class PolicyVersionIdentifierTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyVersionId: Optional[str] = None


class PutVerificationStateOnViolationRequestTypeDef(BaseValidatorModel):
    violationId: str
    verificationState: VerificationStateType
    verificationStateDescription: Optional[str] = None


class RegisterCertificateRequestTypeDef(BaseValidatorModel):
    certificatePem: str
    caCertificatePem: Optional[str] = None
    setAsActive: Optional[bool] = None
    status: Optional[CertificateStatusType] = None


class RegisterCertificateWithoutCARequestTypeDef(BaseValidatorModel):
    certificatePem: str
    status: Optional[CertificateStatusType] = None


class RegisterThingRequestTypeDef(BaseValidatorModel):
    templateBody: str
    parameters: Optional[Mapping[str, str]] = None


class RejectCertificateTransferRequestTypeDef(BaseValidatorModel):
    certificateId: str
    rejectReason: Optional[str] = None


class RemoveThingFromBillingGroupRequestTypeDef(BaseValidatorModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None


class RemoveThingFromThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None


class SearchIndexRequestTypeDef(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    queryVersion: Optional[str] = None


class ThingGroupDocumentTypeDef(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    thingGroupDescription: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    parentGroupNames: Optional[List[str]] = None


class SetDefaultAuthorizerRequestTypeDef(BaseValidatorModel):
    authorizerName: str


class SetDefaultPolicyVersionRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyVersionId: str


class SetV2LoggingOptionsRequestTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    defaultLogLevel: Optional[LogLevelType] = None
    disableAllLogs: Optional[bool] = None


class SigningProfileParameterTypeDef(BaseValidatorModel):
    certificateArn: Optional[str] = None
    platform: Optional[str] = None
    certificatePathOnDevice: Optional[str] = None


class StartOnDemandAuditTaskRequestTypeDef(BaseValidatorModel):
    targetCheckNames: Sequence[str]


class StartThingRegistrationTaskRequestTypeDef(BaseValidatorModel):
    templateBody: str
    inputFileBucket: str
    inputFileKey: str
    roleArn: str


class StopThingRegistrationTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class TlsContextTypeDef(BaseValidatorModel):
    serverName: Optional[str] = None


class ThingConnectivityTypeDef(BaseValidatorModel):
    connected: Optional[bool] = None
    timestamp: Optional[int] = None
    disconnectReason: Optional[str] = None


class TimestreamDimensionTypeDef(BaseValidatorModel):
    name: str
    value: str


class TimestreamTimestampTypeDef(BaseValidatorModel):
    value: str
    unit: str


class VpcDestinationConfigurationTypeDef(BaseValidatorModel):
    subnetIds: Sequence[str]
    vpcId: str
    roleArn: str
    securityGroups: Optional[Sequence[str]] = None


class VpcDestinationSummaryTypeDef(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    roleArn: Optional[str] = None


class VpcDestinationPropertiesTypeDef(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    roleArn: Optional[str] = None


class TransferCertificateRequestTypeDef(BaseValidatorModel):
    certificateId: str
    targetAwsAccount: str
    transferMessage: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAuthorizerRequestTypeDef(BaseValidatorModel):
    authorizerName: str
    authorizerFunctionArn: Optional[str] = None
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Mapping[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    enableCachingForHttp: Optional[bool] = None


class UpdateCertificateProviderRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str
    lambdaFunctionArn: Optional[str] = None
    accountDefaultForOperations: Optional[Sequence[Literal["CreateCertificateFromCsr"]]] = None


class UpdateCertificateRequestTypeDef(BaseValidatorModel):
    certificateId: str
    newStatus: CertificateStatusType


class UpdateCommandRequestTypeDef(BaseValidatorModel):
    commandId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    deprecated: Optional[bool] = None


class UpdateCustomMetricRequestTypeDef(BaseValidatorModel):
    metricName: str
    displayName: str


class UpdateDimensionRequestTypeDef(BaseValidatorModel):
    name: str
    stringValues: Sequence[str]


class UpdatePackageRequestTypeDef(BaseValidatorModel):
    packageName: str
    description: Optional[str] = None
    defaultVersionName: Optional[str] = None
    unsetDefaultVersion: Optional[bool] = None
    clientToken: Optional[str] = None


class UpdateRoleAliasRequestTypeDef(BaseValidatorModel):
    roleAlias: str
    roleArn: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None


class UpdateScheduledAuditRequestTypeDef(BaseValidatorModel):
    scheduledAuditName: str
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    targetCheckNames: Optional[Sequence[str]] = None


class UpdateThingGroupsForThingRequestTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    thingGroupsToAdd: Optional[Sequence[str]] = None
    thingGroupsToRemove: Optional[Sequence[str]] = None
    overrideDynamicGroups: Optional[bool] = None


class UpdateTopicRuleDestinationRequestTypeDef(BaseValidatorModel):
    arn: str
    status: TopicRuleDestinationStatusType


class ValidationErrorTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None


class AbortConfigOutputTypeDef(BaseValidatorModel):
    criteriaList: List[AbortCriteriaTypeDef]


class AbortConfigTypeDef(BaseValidatorModel):
    criteriaList: Sequence[AbortCriteriaTypeDef]


class MetricDatumTypeDef(BaseValidatorModel):
    timestamp: Optional[datetime] = None
    value: Optional[MetricValueOutputTypeDef] = None


class AllowedTypeDef(BaseValidatorModel):
    policies: Optional[List[PolicyTypeDef]] = None


class ExplicitDenyTypeDef(BaseValidatorModel):
    policies: Optional[List[PolicyTypeDef]] = None


class ImplicitDenyTypeDef(BaseValidatorModel):
    policies: Optional[List[PolicyTypeDef]] = None


class AssetPropertyValueTypeDef(BaseValidatorModel):
    value: AssetPropertyVariantTypeDef
    timestamp: AssetPropertyTimestampTypeDef
    quality: Optional[str] = None


class AssociateTargetsWithJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAuthorizerResponseTypeDef(BaseValidatorModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBillingGroupResponseTypeDef(BaseValidatorModel):
    billingGroupName: str
    billingGroupArn: str
    billingGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCertificateFromCsrResponseTypeDef(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    certificatePem: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCertificateProviderResponseTypeDef(BaseValidatorModel):
    certificateProviderName: str
    certificateProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCommandResponseTypeDef(BaseValidatorModel):
    commandId: str
    commandArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomMetricResponseTypeDef(BaseValidatorModel):
    metricName: str
    metricArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDimensionResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDomainConfigurationResponseTypeDef(BaseValidatorModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDynamicThingGroupResponseTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str
    indexName: str
    queryString: str
    queryVersion: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFleetMetricResponseTypeDef(BaseValidatorModel):
    metricName: str
    metricArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobTemplateResponseTypeDef(BaseValidatorModel):
    jobTemplateArn: str
    jobTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMitigationActionResponseTypeDef(BaseValidatorModel):
    actionArn: str
    actionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOTAUpdateResponseTypeDef(BaseValidatorModel):
    otaUpdateId: str
    awsIotJobId: str
    otaUpdateArn: str
    awsIotJobArn: str
    otaUpdateStatus: OTAUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePackageResponseTypeDef(BaseValidatorModel):
    packageName: str
    packageArn: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePackageVersionResponseTypeDef(BaseValidatorModel):
    packageVersionArn: str
    packageName: str
    versionName: str
    description: str
    attributes: Dict[str, str]
    status: PackageVersionStatusType
    errorReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePolicyResponseTypeDef(BaseValidatorModel):
    policyName: str
    policyArn: str
    policyDocument: str
    policyVersionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePolicyVersionResponseTypeDef(BaseValidatorModel):
    policyArn: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProvisioningTemplateResponseTypeDef(BaseValidatorModel):
    templateArn: str
    templateName: str
    defaultVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProvisioningTemplateVersionResponseTypeDef(BaseValidatorModel):
    templateArn: str
    templateName: str
    versionId: int
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRoleAliasResponseTypeDef(BaseValidatorModel):
    roleAlias: str
    roleAliasArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateScheduledAuditResponseTypeDef(BaseValidatorModel):
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSecurityProfileResponseTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStreamResponseTypeDef(BaseValidatorModel):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateThingGroupResponseTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateThingResponseTypeDef(BaseValidatorModel):
    thingName: str
    thingArn: str
    thingId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateThingTypeResponseTypeDef(BaseValidatorModel):
    thingTypeName: str
    thingTypeArn: str
    thingTypeId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCommandResponseTypeDef(BaseValidatorModel):
    statusCode: int
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCertificateProviderResponseTypeDef(BaseValidatorModel):
    certificateProviderName: str
    certificateProviderArn: str
    lambdaFunctionArn: str
    accountDefaultForOperations: List[Literal["CreateCertificateFromCsr"]]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCustomMetricResponseTypeDef(BaseValidatorModel):
    metricName: str
    metricArn: str
    metricType: CustomMetricTypeType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEndpointResponseTypeDef(BaseValidatorModel):
    endpointAddress: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFleetMetricResponseTypeDef(BaseValidatorModel):
    metricName: str
    queryString: str
    aggregationType: AggregationTypeOutputTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeIndexResponseTypeDef(BaseValidatorModel):
    indexName: str
    indexStatus: IndexStatusType
    schema: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeProvisioningTemplateVersionResponseTypeDef(BaseValidatorModel):
    versionId: int
    creationDate: datetime
    templateBody: str
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeScheduledAuditResponseTypeDef(BaseValidatorModel):
    frequency: AuditFrequencyType
    dayOfMonth: str
    dayOfWeek: DayOfWeekType
    targetCheckNames: List[str]
    scheduledAuditName: str
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeThingRegistrationTaskResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeThingResponseTypeDef(BaseValidatorModel):
    defaultClientId: str
    thingName: str
    thingId: str
    thingArn: str
    thingTypeName: str
    attributes: Dict[str, str]
    version: int
    billingGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetCardinalityResponseTypeDef(BaseValidatorModel):
    cardinality: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobDocumentResponseTypeDef(BaseValidatorModel):
    document: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetLoggingOptionsResponseTypeDef(BaseValidatorModel):
    roleArn: str
    logLevel: LogLevelType
    ResponseMetadata: ResponseMetadataTypeDef


class GetPackageResponseTypeDef(BaseValidatorModel):
    packageName: str
    packageArn: str
    description: str
    defaultVersionName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetPolicyResponseTypeDef(BaseValidatorModel):
    policyName: str
    policyArn: str
    policyDocument: str
    defaultVersionId: str
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPolicyVersionResponseTypeDef(BaseValidatorModel):
    policyArn: str
    policyName: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRegistrationCodeResponseTypeDef(BaseValidatorModel):
    registrationCode: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetThingConnectivityDataResponseTypeDef(BaseValidatorModel):
    thingName: str
    connected: bool
    timestamp: datetime
    disconnectReason: DisconnectReasonValueType
    ResponseMetadata: ResponseMetadataTypeDef


class GetV2LoggingOptionsResponseTypeDef(BaseValidatorModel):
    roleArn: str
    defaultLogLevel: LogLevelType
    disableAllLogs: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ListAttachedPoliciesResponseTypeDef(BaseValidatorModel):
    policies: List[PolicyTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomMetricsResponseTypeDef(BaseValidatorModel):
    metricNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDimensionsResponseTypeDef(BaseValidatorModel):
    dimensionNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListIndicesResponseTypeDef(BaseValidatorModel):
    indexNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPoliciesResponseTypeDef(BaseValidatorModel):
    policies: List[PolicyTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPolicyPrincipalsResponseTypeDef(BaseValidatorModel):
    principals: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPrincipalPoliciesResponseTypeDef(BaseValidatorModel):
    policies: List[PolicyTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPrincipalThingsResponseTypeDef(BaseValidatorModel):
    things: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRoleAliasesResponseTypeDef(BaseValidatorModel):
    roleAliases: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTargetsForPolicyResponseTypeDef(BaseValidatorModel):
    targets: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListThingPrincipalsResponseTypeDef(BaseValidatorModel):
    principals: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingRegistrationTaskReportsResponseTypeDef(BaseValidatorModel):
    resourceLinks: List[str]
    reportType: ReportTypeType
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingRegistrationTasksResponseTypeDef(BaseValidatorModel):
    taskIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingsInBillingGroupResponseTypeDef(BaseValidatorModel):
    things: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingsInThingGroupResponseTypeDef(BaseValidatorModel):
    things: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RegisterCACertificateResponseTypeDef(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterCertificateResponseTypeDef(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterCertificateWithoutCAResponseTypeDef(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterThingResponseTypeDef(BaseValidatorModel):
    certificatePem: str
    resourceArns: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SetDefaultAuthorizerResponseTypeDef(BaseValidatorModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartAuditMitigationActionsTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDetectMitigationActionsTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartOnDemandAuditTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartThingRegistrationTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class TestInvokeAuthorizerResponseTypeDef(BaseValidatorModel):
    isAuthenticated: bool
    principalId: str
    policyDocuments: List[str]
    refreshAfterInSeconds: int
    disconnectAfterInSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef


class TransferCertificateResponseTypeDef(BaseValidatorModel):
    transferredCertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAuthorizerResponseTypeDef(BaseValidatorModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBillingGroupResponseTypeDef(BaseValidatorModel):
    version: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCertificateProviderResponseTypeDef(BaseValidatorModel):
    certificateProviderName: str
    certificateProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCommandResponseTypeDef(BaseValidatorModel):
    commandId: str
    displayName: str
    description: str
    deprecated: bool
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCustomMetricResponseTypeDef(BaseValidatorModel):
    metricName: str
    metricArn: str
    metricType: CustomMetricTypeType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDomainConfigurationResponseTypeDef(BaseValidatorModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDynamicThingGroupResponseTypeDef(BaseValidatorModel):
    version: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMitigationActionResponseTypeDef(BaseValidatorModel):
    actionArn: str
    actionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRoleAliasResponseTypeDef(BaseValidatorModel):
    roleAlias: str
    roleAliasArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateScheduledAuditResponseTypeDef(BaseValidatorModel):
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateStreamResponseTypeDef(BaseValidatorModel):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateThingGroupResponseTypeDef(BaseValidatorModel):
    version: int
    ResponseMetadata: ResponseMetadataTypeDef


class ThingGroupPropertiesOutputTypeDef(BaseValidatorModel):
    thingGroupDescription: Optional[str] = None
    attributePayload: Optional[AttributePayloadOutputTypeDef] = None


class ThingGroupPropertiesTypeDef(BaseValidatorModel):
    thingGroupDescription: Optional[str] = None
    attributePayload: Optional[AttributePayloadTypeDef] = None


class ListAuditMitigationActionsExecutionsResponseTypeDef(BaseValidatorModel):
    actionsExecutions: List[AuditMitigationActionExecutionMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAuditMitigationActionsTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[AuditMitigationActionsTaskMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeAccountAuditConfigurationResponseTypeDef(BaseValidatorModel):
    roleArn: str
    auditNotificationTargetConfigurations: Dict[Literal["SNS"], AuditNotificationTargetTypeDef]
    auditCheckConfigurations: Dict[str, AuditCheckConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAuditTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[AuditTaskMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeAuthorizerResponseTypeDef(BaseValidatorModel):
    authorizerDescription: AuthorizerDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDefaultAuthorizerResponseTypeDef(BaseValidatorModel):
    authorizerDescription: AuthorizerDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAuthorizersResponseTypeDef(BaseValidatorModel):
    authorizers: List[AuthorizerSummaryTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class AwsJobAbortConfigTypeDef(BaseValidatorModel):
    abortCriteriaList: Sequence[AwsJobAbortCriteriaTypeDef]


class AwsJobExponentialRolloutRateTypeDef(BaseValidatorModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: AwsJobRateIncreaseCriteriaTypeDef


class BehaviorCriteriaOutputTypeDef(BaseValidatorModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValueOutputTypeDef] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThresholdTypeDef] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfigTypeDef] = None


class GetBehaviorModelTrainingSummariesResponseTypeDef(BaseValidatorModel):
    summaries: List[BehaviorModelTrainingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MetricDimensionTypeDef(BaseValidatorModel):
    pass


class MetricToRetainTypeDef(BaseValidatorModel):
    metric: str
    metricDimension: Optional[MetricDimensionTypeDef] = None
    exportMetric: Optional[bool] = None


class DescribeBillingGroupResponseTypeDef(BaseValidatorModel):
    billingGroupName: str
    billingGroupId: str
    billingGroupArn: str
    version: int
    billingGroupProperties: BillingGroupPropertiesTypeDef
    billingGroupMetadata: BillingGroupMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBillingGroupRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    billingGroupProperties: BillingGroupPropertiesTypeDef
    expectedVersion: Optional[int] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class CodeSigningSignatureTypeDef(BaseValidatorModel):
    inlineDocument: Optional[BlobTypeDef] = None


class CommandParameterValueTypeDef(BaseValidatorModel):
    S: Optional[str] = None
    B: Optional[bool] = None
    I: Optional[int] = None
    L: Optional[int] = None
    D: Optional[float] = None
    BIN: Optional[BlobTypeDef] = None
    UL: Optional[str] = None


class CommandPayloadTypeDef(BaseValidatorModel):
    content: Optional[BlobTypeDef] = None
    contentType: Optional[str] = None


class MqttContextTypeDef(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[BlobTypeDef] = None
    clientId: Optional[str] = None


class GetBucketsAggregationResponseTypeDef(BaseValidatorModel):
    totalCount: int
    buckets: List[BucketTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BucketsAggregationTypeTypeDef(BaseValidatorModel):
    termsAggregation: Optional[TermsAggregationTypeDef] = None


class CACertificateDescriptionTypeDef(BaseValidatorModel):
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
    validity: Optional[CertificateValidityTypeDef] = None
    certificateMode: Optional[CertificateModeType] = None


class ListCACertificatesResponseTypeDef(BaseValidatorModel):
    certificates: List[CACertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class CertificateDescriptionTypeDef(BaseValidatorModel):
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
    transferData: Optional[TransferDataTypeDef] = None
    generationId: Optional[str] = None
    validity: Optional[CertificateValidityTypeDef] = None
    certificateMode: Optional[CertificateModeType] = None


class ListCertificateProvidersResponseTypeDef(BaseValidatorModel):
    certificateProviders: List[CertificateProviderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCertificatesByCAResponseTypeDef(BaseValidatorModel):
    certificates: List[CertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListCertificatesResponseTypeDef(BaseValidatorModel):
    certificates: List[CertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class CustomCodeSigningOutputTypeDef(BaseValidatorModel):
    signature: Optional[CodeSigningSignatureOutputTypeDef] = None
    certificateChain: Optional[CodeSigningCertificateChainTypeDef] = None
    hashAlgorithm: Optional[str] = None
    signatureAlgorithm: Optional[str] = None


class ListCommandExecutionsResponseTypeDef(BaseValidatorModel):
    commandExecutions: List[CommandExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CommandParameterOutputTypeDef(BaseValidatorModel):
    name: str
    value: Optional[CommandParameterValueOutputTypeDef] = None
    defaultValue: Optional[CommandParameterValueOutputTypeDef] = None
    description: Optional[str] = None


class ListCommandsResponseTypeDef(BaseValidatorModel):
    commands: List[CommandSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeEventConfigurationsResponseTypeDef(BaseValidatorModel):
    eventConfigurations: Dict[EventTypeType, ConfigurationTypeDef]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEventConfigurationsRequestTypeDef(BaseValidatorModel):
    eventConfigurations: Optional[Mapping[EventTypeType, ConfigurationTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListAuditMitigationActionsTasksRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAuditTasksRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDetectMitigationActionsExecutionsRequestTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDetectMitigationActionsTasksRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListMetricValuesRequestTypeDef(BaseValidatorModel):
    thingName: str
    metricName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListViolationEventsRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ViolationEventOccurrenceRangeTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef


class CreateAuthorizerRequestTypeDef(BaseValidatorModel):
    authorizerName: str
    authorizerFunctionArn: str
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Mapping[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    signingDisabled: Optional[bool] = None
    enableCachingForHttp: Optional[bool] = None


class CreateBillingGroupRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    billingGroupProperties: Optional[BillingGroupPropertiesTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateCertificateProviderRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str
    lambdaFunctionArn: str
    accountDefaultForOperations: Sequence[Literal["CreateCertificateFromCsr"]]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateCustomMetricRequestTypeDef(BaseValidatorModel):
    metricName: str
    metricType: CustomMetricTypeType
    clientRequestToken: str
    displayName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreatePolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyDocument: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateRoleAliasRequestTypeDef(BaseValidatorModel):
    roleAlias: str
    roleArn: str
    credentialDurationSeconds: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateScheduledAuditRequestTypeDef(BaseValidatorModel):
    frequency: AuditFrequencyType
    targetCheckNames: Sequence[str]
    scheduledAuditName: str
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CreateDomainConfigurationRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str
    domainName: Optional[str] = None
    serverCertificateArns: Optional[Sequence[str]] = None
    validationCertificateArn: Optional[str] = None
    authorizerConfig: Optional[AuthorizerConfigTypeDef] = None
    serviceType: Optional[ServiceTypeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None
    serverCertificateConfig: Optional[ServerCertificateConfigTypeDef] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    applicationProtocol: Optional[ApplicationProtocolType] = None
    clientCertificateConfig: Optional[ClientCertificateConfigTypeDef] = None


class UpdateDomainConfigurationRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str
    authorizerConfig: Optional[AuthorizerConfigTypeDef] = None
    domainConfigurationStatus: Optional[DomainConfigurationStatusType] = None
    removeAuthorizerConfig: Optional[bool] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None
    serverCertificateConfig: Optional[ServerCertificateConfigTypeDef] = None
    authenticationType: Optional[AuthenticationTypeType] = None
    applicationProtocol: Optional[ApplicationProtocolType] = None
    clientCertificateConfig: Optional[ClientCertificateConfigTypeDef] = None


class SchedulingConfigOutputTypeDef(BaseValidatorModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    endBehavior: Optional[JobEndBehaviorType] = None
    maintenanceWindows: Optional[List[MaintenanceWindowTypeDef]] = None


class SchedulingConfigTypeDef(BaseValidatorModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    endBehavior: Optional[JobEndBehaviorType] = None
    maintenanceWindows: Optional[Sequence[MaintenanceWindowTypeDef]] = None


class CreateKeysAndCertificateResponseTypeDef(BaseValidatorModel):
    certificateArn: str
    certificateId: str
    certificatePem: str
    keyPair: KeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProvisioningClaimResponseTypeDef(BaseValidatorModel):
    certificateId: str
    certificatePem: str
    keyPair: KeyPairTypeDef
    expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProvisioningTemplateRequestTypeDef(BaseValidatorModel):
    templateName: str
    description: Optional[str] = None
    enabled: Optional[bool] = None
    defaultVersionId: Optional[int] = None
    provisioningRoleArn: Optional[str] = None
    preProvisioningHook: Optional[ProvisioningHookTypeDef] = None
    removePreProvisioningHook: Optional[bool] = None


class DescribeAuditTaskResponseTypeDef(BaseValidatorModel):
    taskStatus: AuditTaskStatusType
    taskType: AuditTaskTypeType
    taskStartTime: datetime
    taskStatistics: TaskStatisticsTypeDef
    scheduledAuditName: str
    auditDetails: Dict[str, AuditCheckDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterCACertificateRequestTypeDef(BaseValidatorModel):
    caCertificate: str
    verificationCertificate: Optional[str] = None
    setAsActive: Optional[bool] = None
    allowAutoRegistration: Optional[bool] = None
    registrationConfig: Optional[RegistrationConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    certificateMode: Optional[CertificateModeType] = None


class UpdateCACertificateRequestTypeDef(BaseValidatorModel):
    certificateId: str
    newStatus: Optional[CACertificateStatusType] = None
    newAutoRegistrationStatus: Optional[AutoRegistrationStatusType] = None
    registrationConfig: Optional[RegistrationConfigTypeDef] = None
    removeAutoRegistration: Optional[bool] = None


class DescribeDomainConfigurationResponseTypeDef(BaseValidatorModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    domainName: str
    serverCertificates: List[ServerCertificateSummaryTypeDef]
    authorizerConfig: AuthorizerConfigTypeDef
    domainConfigurationStatus: DomainConfigurationStatusType
    serviceType: ServiceTypeType
    domainType: DomainTypeType
    lastStatusChangeDate: datetime
    tlsConfig: TlsConfigTypeDef
    serverCertificateConfig: ServerCertificateConfigTypeDef
    authenticationType: AuthenticationTypeType
    applicationProtocol: ApplicationProtocolType
    clientCertificateConfig: ClientCertificateConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeManagedJobTemplateResponseTypeDef(BaseValidatorModel):
    templateName: str
    templateArn: str
    description: str
    templateVersion: str
    environments: List[str]
    documentParameters: List[DocumentParameterTypeDef]
    document: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRoleAliasResponseTypeDef(BaseValidatorModel):
    roleAliasDescription: RoleAliasDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DestinationTypeDef(BaseValidatorModel):
    s3Destination: Optional[S3DestinationTypeDef] = None


class ListDetectMitigationActionsExecutionsResponseTypeDef(BaseValidatorModel):
    actionsExecutions: List[DetectMitigationActionExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDomainConfigurationsResponseTypeDef(BaseValidatorModel):
    domainConfigurations: List[DomainConfigurationSummaryTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DynamoDBv2ActionTypeDef(BaseValidatorModel):
    roleArn: str
    putItem: PutItemInputTypeDef


class GetEffectivePoliciesResponseTypeDef(BaseValidatorModel):
    effectivePolicies: List[EffectivePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ExponentialRolloutRateTypeDef(BaseValidatorModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: RateIncreaseCriteriaTypeDef


class FieldTypeDef(BaseValidatorModel):
    pass


class ThingGroupIndexingConfigurationOutputTypeDef(BaseValidatorModel):
    thingGroupIndexingMode: ThingGroupIndexingModeType
    managedFields: Optional[List[FieldTypeDef]] = None
    customFields: Optional[List[FieldTypeDef]] = None


class ThingGroupIndexingConfigurationTypeDef(BaseValidatorModel):
    thingGroupIndexingMode: ThingGroupIndexingModeType
    managedFields: Optional[Sequence[FieldTypeDef]] = None
    customFields: Optional[Sequence[FieldTypeDef]] = None


class PackageVersionArtifactTypeDef(BaseValidatorModel):
    s3Location: Optional[S3LocationTypeDef] = None


class SbomTypeDef(BaseValidatorModel):
    s3Location: Optional[S3LocationTypeDef] = None


class StreamFileTypeDef(BaseValidatorModel):
    fileId: Optional[int] = None
    s3Location: Optional[S3LocationTypeDef] = None


class FileLocationTypeDef(BaseValidatorModel):
    stream: Optional[StreamTypeDef] = None
    s3Location: Optional[S3LocationTypeDef] = None


class ListFleetMetricsResponseTypeDef(BaseValidatorModel):
    fleetMetrics: List[FleetMetricNameAndArnTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IndexingFilterOutputTypeDef(BaseValidatorModel):
    namedShadowNames: Optional[List[str]] = None
    geoLocations: Optional[List[GeoLocationTargetTypeDef]] = None


class IndexingFilterTypeDef(BaseValidatorModel):
    namedShadowNames: Optional[Sequence[str]] = None
    geoLocations: Optional[Sequence[GeoLocationTargetTypeDef]] = None


class GetBehaviorModelTrainingSummariesRequestPaginateTypeDef(BaseValidatorModel):
    securityProfileName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListActiveViolationsRequestPaginateTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttachedPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    target: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAuditMitigationActionsExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAuditMitigationActionsTasksRequestPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAuditTasksRequestPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAuthorizersRequestPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBillingGroupsRequestPaginateTypeDef(BaseValidatorModel):
    namePrefixFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCACertificatesRequestPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCertificatesByCARequestPaginateTypeDef(BaseValidatorModel):
    caCertificateId: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCommandsRequestPaginateTypeDef(BaseValidatorModel):
    namespace: Optional[CommandNamespaceType] = None
    commandParameterName: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomMetricsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDetectMitigationActionsExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDetectMitigationActionsTasksRequestPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDimensionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    serviceType: Optional[ServiceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFleetMetricsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIndicesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobExecutionsForJobRequestPaginateTypeDef(BaseValidatorModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobExecutionsForThingRequestPaginateTypeDef(BaseValidatorModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    jobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedJobTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMetricValuesRequestPaginateTypeDef(BaseValidatorModel):
    thingName: str
    metricName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMitigationActionsRequestPaginateTypeDef(BaseValidatorModel):
    actionType: Optional[MitigationActionTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOTAUpdatesRequestPaginateTypeDef(BaseValidatorModel):
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOutgoingCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPackageVersionsRequestPaginateTypeDef(BaseValidatorModel):
    packageName: str
    status: Optional[PackageVersionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPackagesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPolicyPrincipalsRequestPaginateTypeDef(BaseValidatorModel):
    policyName: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrincipalPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    principal: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrincipalThingsRequestPaginateTypeDef(BaseValidatorModel):
    principal: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrincipalThingsV2RequestPaginateTypeDef(BaseValidatorModel):
    principal: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisioningTemplateVersionsRequestPaginateTypeDef(BaseValidatorModel):
    templateName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisioningTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRelatedResourcesForAuditFindingRequestPaginateTypeDef(BaseValidatorModel):
    findingId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoleAliasesRequestPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSbomValidationResultsRequestPaginateTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    validationResult: Optional[SbomValidationResultType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListScheduledAuditsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityProfilesForTargetRequestPaginateTypeDef(BaseValidatorModel):
    securityProfileTargetArn: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityProfilesRequestPaginateTypeDef(BaseValidatorModel):
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamsRequestPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTargetsForPolicyRequestPaginateTypeDef(BaseValidatorModel):
    policyName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTargetsForSecurityProfileRequestPaginateTypeDef(BaseValidatorModel):
    securityProfileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingGroupsForThingRequestPaginateTypeDef(BaseValidatorModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingGroupsRequestPaginateTypeDef(BaseValidatorModel):
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingPrincipalsRequestPaginateTypeDef(BaseValidatorModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingPrincipalsV2RequestPaginateTypeDef(BaseValidatorModel):
    thingName: str
    thingPrincipalType: Optional[ThingPrincipalTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingRegistrationTaskReportsRequestPaginateTypeDef(BaseValidatorModel):
    taskId: str
    reportType: ReportTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingRegistrationTasksRequestPaginateTypeDef(BaseValidatorModel):
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingTypesRequestPaginateTypeDef(BaseValidatorModel):
    thingTypeName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingsInBillingGroupRequestPaginateTypeDef(BaseValidatorModel):
    billingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingsInThingGroupRequestPaginateTypeDef(BaseValidatorModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListThingsRequestPaginateTypeDef(BaseValidatorModel):
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    thingTypeName: Optional[str] = None
    usePrefixAttributeValue: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTopicRuleDestinationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTopicRulesRequestPaginateTypeDef(BaseValidatorModel):
    topic: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListV2LoggingLevelsRequestPaginateTypeDef(BaseValidatorModel):
    targetType: Optional[LogTargetTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListViolationEventsRequestPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCommandExecutionResponseTypeDef(BaseValidatorModel):
    executionId: str
    commandArn: str
    targetArn: str
    status: CommandExecutionStatusType
    statusReason: StatusReasonTypeDef
    result: Dict[str, CommandExecutionResultTypeDef]
    parameters: Dict[str, CommandParameterValueOutputTypeDef]
    executionTimeoutSeconds: int
    createdAt: datetime
    lastUpdatedAt: datetime
    startedAt: datetime
    completedAt: datetime
    timeToLive: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetPackageConfigurationResponseTypeDef(BaseValidatorModel):
    versionUpdateByJobsConfig: VersionUpdateByJobsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePackageConfigurationRequestTypeDef(BaseValidatorModel):
    versionUpdateByJobsConfig: Optional[VersionUpdateByJobsConfigTypeDef] = None
    clientToken: Optional[str] = None


class GetPercentilesResponseTypeDef(BaseValidatorModel):
    percentiles: List[PercentPairTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StatisticsTypeDef(BaseValidatorModel):
    pass


class GetStatisticsResponseTypeDef(BaseValidatorModel):
    statistics: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBillingGroupsResponseTypeDef(BaseValidatorModel):
    billingGroups: List[GroupNameAndArnTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingGroupsForThingResponseTypeDef(BaseValidatorModel):
    thingGroups: List[GroupNameAndArnTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingGroupsResponseTypeDef(BaseValidatorModel):
    thingGroups: List[GroupNameAndArnTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ThingGroupMetadataTypeDef(BaseValidatorModel):
    parentGroupName: Optional[str] = None
    rootToParentThingGroups: Optional[List[GroupNameAndArnTypeDef]] = None
    creationDate: Optional[datetime] = None


class HttpAuthorizationTypeDef(BaseValidatorModel):
    sigv4: Optional[SigV4AuthorizationTypeDef] = None


class JobExecutionTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    status: Optional[JobExecutionStatusType] = None
    forceCanceled: Optional[bool] = None
    statusDetails: Optional[JobExecutionStatusDetailsTypeDef] = None
    thingArn: Optional[str] = None
    queuedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    executionNumber: Optional[int] = None
    versionNumber: Optional[int] = None
    approximateSecondsBeforeTimedOut: Optional[int] = None


class JobExecutionSummaryForJobTypeDef(BaseValidatorModel):
    thingArn: Optional[str] = None
    jobExecutionSummary: Optional[JobExecutionSummaryTypeDef] = None


class JobExecutionSummaryForThingTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    jobExecutionSummary: Optional[JobExecutionSummaryTypeDef] = None


class JobExecutionsRetryConfigOutputTypeDef(BaseValidatorModel):
    criteriaList: List[RetryCriteriaTypeDef]


class JobExecutionsRetryConfigTypeDef(BaseValidatorModel):
    criteriaList: Sequence[RetryCriteriaTypeDef]


class ListJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListJobTemplatesResponseTypeDef(BaseValidatorModel):
    jobTemplates: List[JobTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class KafkaActionOutputTypeDef(BaseValidatorModel):
    destinationArn: str
    topic: str
    clientProperties: Dict[str, str]
    key: Optional[str] = None
    partition: Optional[str] = None
    headers: Optional[List[KafkaActionHeaderTypeDef]] = None


class KafkaActionTypeDef(BaseValidatorModel):
    destinationArn: str
    topic: str
    clientProperties: Mapping[str, str]
    key: Optional[str] = None
    partition: Optional[str] = None
    headers: Optional[Sequence[KafkaActionHeaderTypeDef]] = None


class ListCommandExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    namespace: Optional[CommandNamespaceType] = None
    status: Optional[CommandExecutionStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    startedTimeFilter: Optional[TimeFilterTypeDef] = None
    completedTimeFilter: Optional[TimeFilterTypeDef] = None
    targetArn: Optional[str] = None
    commandArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCommandExecutionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    namespace: Optional[CommandNamespaceType] = None
    status: Optional[CommandExecutionStatusType] = None
    sortOrder: Optional[SortOrderType] = None
    startedTimeFilter: Optional[TimeFilterTypeDef] = None
    completedTimeFilter: Optional[TimeFilterTypeDef] = None
    targetArn: Optional[str] = None
    commandArn: Optional[str] = None


class ListManagedJobTemplatesResponseTypeDef(BaseValidatorModel):
    managedJobTemplates: List[ManagedJobTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMitigationActionsResponseTypeDef(BaseValidatorModel):
    actionIdentifiers: List[MitigationActionIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListOTAUpdatesResponseTypeDef(BaseValidatorModel):
    otaUpdates: List[OTAUpdateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListOutgoingCertificatesResponseTypeDef(BaseValidatorModel):
    outgoingCertificates: List[OutgoingCertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPackageVersionsResponseTypeDef(BaseValidatorModel):
    packageVersionSummaries: List[PackageVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPackagesResponseTypeDef(BaseValidatorModel):
    packageSummaries: List[PackageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPolicyVersionsResponseTypeDef(BaseValidatorModel):
    policyVersions: List[PolicyVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListPrincipalThingsV2ResponseTypeDef(BaseValidatorModel):
    principalThingObjects: List[PrincipalThingObjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListProvisioningTemplateVersionsResponseTypeDef(BaseValidatorModel):
    versions: List[ProvisioningTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ProvisioningTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListProvisioningTemplatesResponseTypeDef(BaseValidatorModel):
    templates: List[ProvisioningTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSbomValidationResultsResponseTypeDef(BaseValidatorModel):
    validationResultSummaries: List[SbomValidationResultSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListScheduledAuditsResponseTypeDef(BaseValidatorModel):
    scheduledAudits: List[ScheduledAuditMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSecurityProfilesResponseTypeDef(BaseValidatorModel):
    securityProfileIdentifiers: List[SecurityProfileIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStreamsResponseTypeDef(BaseValidatorModel):
    streams: List[StreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTargetsForSecurityProfileResponseTypeDef(BaseValidatorModel):
    securityProfileTargets: List[SecurityProfileTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SecurityProfileTargetMappingTypeDef(BaseValidatorModel):
    securityProfileIdentifier: Optional[SecurityProfileIdentifierTypeDef] = None
    target: Optional[SecurityProfileTargetTypeDef] = None


class ListThingPrincipalsV2ResponseTypeDef(BaseValidatorModel):
    thingPrincipalObjects: List[ThingPrincipalObjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingsResponseTypeDef(BaseValidatorModel):
    things: List[ThingAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTopicRulesResponseTypeDef(BaseValidatorModel):
    rules: List[TopicRuleListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LocationActionTypeDef(BaseValidatorModel):
    roleArn: str
    trackerName: str
    deviceId: str
    latitude: str
    longitude: str
    timestamp: Optional[LocationTimestampTypeDef] = None


class LogTargetConfigurationTypeDef(BaseValidatorModel):
    logTarget: Optional[LogTargetTypeDef] = None
    logLevel: Optional[LogLevelType] = None


class SetV2LoggingLevelRequestTypeDef(BaseValidatorModel):
    logTarget: LogTargetTypeDef
    logLevel: LogLevelType


class SetLoggingOptionsRequestTypeDef(BaseValidatorModel):
    loggingOptionsPayload: LoggingOptionsPayloadTypeDef


class MitigationActionParamsOutputTypeDef(BaseValidatorModel):
    updateDeviceCertificateParams: Optional[UpdateDeviceCertificateParamsTypeDef] = None
    updateCACertificateParams: Optional[UpdateCACertificateParamsTypeDef] = None
    addThingsToThingGroupParams: Optional[AddThingsToThingGroupParamsOutputTypeDef] = None
    replaceDefaultPolicyVersionParams: Optional[ReplaceDefaultPolicyVersionParamsTypeDef] = None
    enableIoTLoggingParams: Optional[EnableIoTLoggingParamsTypeDef] = None
    publishFindingToSnsParams: Optional[PublishFindingToSnsParamsTypeDef] = None


class MitigationActionParamsTypeDef(BaseValidatorModel):
    updateDeviceCertificateParams: Optional[UpdateDeviceCertificateParamsTypeDef] = None
    updateCACertificateParams: Optional[UpdateCACertificateParamsTypeDef] = None
    addThingsToThingGroupParams: Optional[AddThingsToThingGroupParamsTypeDef] = None
    replaceDefaultPolicyVersionParams: Optional[ReplaceDefaultPolicyVersionParamsTypeDef] = None
    enableIoTLoggingParams: Optional[EnableIoTLoggingParamsTypeDef] = None
    publishFindingToSnsParams: Optional[PublishFindingToSnsParamsTypeDef] = None


class Mqtt5ConfigurationOutputTypeDef(BaseValidatorModel):
    propagatingAttributes: Optional[List[PropagatingAttributeTypeDef]] = None


class Mqtt5ConfigurationTypeDef(BaseValidatorModel):
    propagatingAttributes: Optional[Sequence[PropagatingAttributeTypeDef]] = None


class MqttHeadersOutputTypeDef(BaseValidatorModel):
    payloadFormatIndicator: Optional[str] = None
    contentType: Optional[str] = None
    responseTopic: Optional[str] = None
    correlationData: Optional[str] = None
    messageExpiry: Optional[str] = None
    userProperties: Optional[List[UserPropertyTypeDef]] = None


class MqttHeadersTypeDef(BaseValidatorModel):
    payloadFormatIndicator: Optional[str] = None
    contentType: Optional[str] = None
    responseTopic: Optional[str] = None
    correlationData: Optional[str] = None
    messageExpiry: Optional[str] = None
    userProperties: Optional[Sequence[UserPropertyTypeDef]] = None


class ResourceIdentifierTypeDef(BaseValidatorModel):
    deviceCertificateId: Optional[str] = None
    caCertificateId: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    clientId: Optional[str] = None
    policyVersionIdentifier: Optional[PolicyVersionIdentifierTypeDef] = None
    account: Optional[str] = None
    iamRoleArn: Optional[str] = None
    roleAliasArn: Optional[str] = None
    issuerCertificateIdentifier: Optional[IssuerCertificateIdentifierTypeDef] = None
    deviceCertificateArn: Optional[str] = None


class ThingDocumentTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    thingId: Optional[str] = None
    thingTypeName: Optional[str] = None
    thingGroupNames: Optional[List[str]] = None
    attributes: Optional[Dict[str, str]] = None
    shadow: Optional[str] = None
    deviceDefender: Optional[str] = None
    connectivity: Optional[ThingConnectivityTypeDef] = None


class TimestreamActionOutputTypeDef(BaseValidatorModel):
    roleArn: str
    databaseName: str
    tableName: str
    dimensions: List[TimestreamDimensionTypeDef]
    timestamp: Optional[TimestreamTimestampTypeDef] = None


class TimestreamActionTypeDef(BaseValidatorModel):
    roleArn: str
    databaseName: str
    tableName: str
    dimensions: Sequence[TimestreamDimensionTypeDef]
    timestamp: Optional[TimestreamTimestampTypeDef] = None


class TopicRuleDestinationConfigurationTypeDef(BaseValidatorModel):
    httpUrlConfiguration: Optional[HttpUrlDestinationConfigurationTypeDef] = None
    vpcConfiguration: Optional[VpcDestinationConfigurationTypeDef] = None


class TopicRuleDestinationSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[TopicRuleDestinationStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    statusReason: Optional[str] = None
    httpUrlSummary: Optional[HttpUrlDestinationSummaryTypeDef] = None
    vpcDestinationSummary: Optional[VpcDestinationSummaryTypeDef] = None


class TopicRuleDestinationTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[TopicRuleDestinationStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    statusReason: Optional[str] = None
    httpUrlProperties: Optional[HttpUrlDestinationPropertiesTypeDef] = None
    vpcProperties: Optional[VpcDestinationPropertiesTypeDef] = None


class ValidateSecurityProfileBehaviorsResponseTypeDef(BaseValidatorModel):
    valid: bool
    validationErrors: List[ValidationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListMetricValuesResponseTypeDef(BaseValidatorModel):
    metricDatumList: List[MetricDatumTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AggregationTypeUnionTypeDef(BaseValidatorModel):
    pass


class CreateFleetMetricRequestTypeDef(BaseValidatorModel):
    metricName: str
    queryString: str
    aggregationType: AggregationTypeUnionTypeDef
    period: int
    aggregationField: str
    description: Optional[str] = None
    queryVersion: Optional[str] = None
    indexName: Optional[str] = None
    unit: Optional[FleetMetricUnitType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateFleetMetricRequestTypeDef(BaseValidatorModel):
    metricName: str
    indexName: str
    queryString: Optional[str] = None
    aggregationType: Optional[AggregationTypeUnionTypeDef] = None
    period: Optional[int] = None
    aggregationField: Optional[str] = None
    description: Optional[str] = None
    queryVersion: Optional[str] = None
    unit: Optional[FleetMetricUnitType] = None
    expectedVersion: Optional[int] = None


class DeniedTypeDef(BaseValidatorModel):
    implicitDeny: Optional[ImplicitDenyTypeDef] = None
    explicitDeny: Optional[ExplicitDenyTypeDef] = None


class PutAssetPropertyValueEntryOutputTypeDef(BaseValidatorModel):
    propertyValues: List[AssetPropertyValueTypeDef]
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class PutAssetPropertyValueEntryTypeDef(BaseValidatorModel):
    propertyValues: Sequence[AssetPropertyValueTypeDef]
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None


class AttributePayloadUnionTypeDef(BaseValidatorModel):
    pass


class CreateThingRequestTypeDef(BaseValidatorModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadUnionTypeDef] = None
    billingGroupName: Optional[str] = None


class UpdateThingRequestTypeDef(BaseValidatorModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadUnionTypeDef] = None
    expectedVersion: Optional[int] = None
    removeThingType: Optional[bool] = None


class AuditCheckConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateAccountAuditConfigurationRequestTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    auditNotificationTargetConfigurations: Optional[ Mapping[Literal["SNS"], AuditNotificationTargetTypeDef] ] = None
    auditCheckConfigurations: Optional[Mapping[str, AuditCheckConfigurationUnionTypeDef]] = None


class AuditMitigationActionsTaskTargetUnionTypeDef(BaseValidatorModel):
    pass


class StartAuditMitigationActionsTaskRequestTypeDef(BaseValidatorModel):
    taskId: str
    target: AuditMitigationActionsTaskTargetUnionTypeDef
    auditCheckToActionsMapping: Mapping[str, Sequence[str]]
    clientRequestToken: str


class AuthInfoUnionTypeDef(BaseValidatorModel):
    pass


class TestAuthorizationRequestTypeDef(BaseValidatorModel):
    authInfos: Sequence[AuthInfoUnionTypeDef]
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    clientId: Optional[str] = None
    policyNamesToAdd: Optional[Sequence[str]] = None
    policyNamesToSkip: Optional[Sequence[str]] = None


class AwsJobExecutionsRolloutConfigTypeDef(BaseValidatorModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[AwsJobExponentialRolloutRateTypeDef] = None


class BehaviorOutputTypeDef(BaseValidatorModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimensionTypeDef] = None
    criteria: Optional[BehaviorCriteriaOutputTypeDef] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None


class TestInvokeAuthorizerRequestTypeDef(BaseValidatorModel):
    authorizerName: str
    token: Optional[str] = None
    tokenSignature: Optional[str] = None
    httpContext: Optional[HttpContextTypeDef] = None
    mqttContext: Optional[MqttContextTypeDef] = None
    tlsContext: Optional[TlsContextTypeDef] = None


class GetBucketsAggregationRequestTypeDef(BaseValidatorModel):
    queryString: str
    aggregationField: str
    bucketsAggregationType: BucketsAggregationTypeTypeDef
    indexName: Optional[str] = None
    queryVersion: Optional[str] = None


class DescribeCACertificateResponseTypeDef(BaseValidatorModel):
    certificateDescription: CACertificateDescriptionTypeDef
    registrationConfig: RegistrationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCertificateResponseTypeDef(BaseValidatorModel):
    certificateDescription: CertificateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCommandResponseTypeDef(BaseValidatorModel):
    commandId: str
    commandArn: str
    namespace: CommandNamespaceType
    displayName: str
    description: str
    mandatoryParameters: List[CommandParameterOutputTypeDef]
    payload: CommandPayloadOutputTypeDef
    roleArn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    deprecated: bool
    pendingDeletion: bool
    ResponseMetadata: ResponseMetadataTypeDef


class StartSigningJobParameterTypeDef(BaseValidatorModel):
    signingProfileParameter: Optional[SigningProfileParameterTypeDef] = None
    signingProfileName: Optional[str] = None
    destination: Optional[DestinationTypeDef] = None


class JobExecutionsRolloutConfigTypeDef(BaseValidatorModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[ExponentialRolloutRateTypeDef] = None


class CreatePackageVersionRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    artifact: Optional[PackageVersionArtifactTypeDef] = None
    recipe: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class UpdatePackageVersionRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    artifact: Optional[PackageVersionArtifactTypeDef] = None
    action: Optional[PackageVersionActionType] = None
    recipe: Optional[str] = None
    clientToken: Optional[str] = None


class AssociateSbomWithPackageVersionRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    sbom: SbomTypeDef
    clientToken: Optional[str] = None


class AssociateSbomWithPackageVersionResponseTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    sbom: SbomTypeDef
    sbomValidationStatus: SbomValidationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetPackageVersionResponseTypeDef(BaseValidatorModel):
    packageVersionArn: str
    packageName: str
    versionName: str
    description: str
    attributes: Dict[str, str]
    artifact: PackageVersionArtifactTypeDef
    status: PackageVersionStatusType
    errorReason: str
    creationDate: datetime
    lastModifiedDate: datetime
    sbom: SbomTypeDef
    sbomValidationStatus: SbomValidationStatusType
    recipe: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStreamRequestTypeDef(BaseValidatorModel):
    streamId: str
    files: Sequence[StreamFileTypeDef]
    roleArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class StreamInfoTypeDef(BaseValidatorModel):
    streamId: Optional[str] = None
    streamArn: Optional[str] = None
    streamVersion: Optional[int] = None
    description: Optional[str] = None
    files: Optional[List[StreamFileTypeDef]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    roleArn: Optional[str] = None


class UpdateStreamRequestTypeDef(BaseValidatorModel):
    streamId: str
    description: Optional[str] = None
    files: Optional[Sequence[StreamFileTypeDef]] = None
    roleArn: Optional[str] = None


class DescribeThingGroupResponseTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupId: str
    thingGroupArn: str
    version: int
    thingGroupProperties: ThingGroupPropertiesOutputTypeDef
    thingGroupMetadata: ThingGroupMetadataTypeDef
    indexName: str
    queryString: str
    queryVersion: str
    status: DynamicGroupStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class HttpActionOutputTypeDef(BaseValidatorModel):
    url: str
    confirmationUrl: Optional[str] = None
    headers: Optional[List[HttpActionHeaderTypeDef]] = None
    auth: Optional[HttpAuthorizationTypeDef] = None


class HttpActionTypeDef(BaseValidatorModel):
    url: str
    confirmationUrl: Optional[str] = None
    headers: Optional[Sequence[HttpActionHeaderTypeDef]] = None
    auth: Optional[HttpAuthorizationTypeDef] = None


class DescribeJobExecutionResponseTypeDef(BaseValidatorModel):
    execution: JobExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobExecutionsForJobResponseTypeDef(BaseValidatorModel):
    executionSummaries: List[JobExecutionSummaryForJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListJobExecutionsForThingResponseTypeDef(BaseValidatorModel):
    executionSummaries: List[JobExecutionSummaryForThingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSecurityProfilesForTargetResponseTypeDef(BaseValidatorModel):
    securityProfileTargetMappings: List[SecurityProfileTargetMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListV2LoggingLevelsResponseTypeDef(BaseValidatorModel):
    logTargetConfigurations: List[LogTargetConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MetricValueUnionTypeDef(BaseValidatorModel):
    pass


class BehaviorCriteriaTypeDef(BaseValidatorModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValueUnionTypeDef] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThresholdTypeDef] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfigTypeDef] = None


class DescribeMitigationActionResponseTypeDef(BaseValidatorModel):
    actionName: str
    actionType: MitigationActionTypeType
    actionArn: str
    actionId: str
    roleArn: str
    actionParams: MitigationActionParamsOutputTypeDef
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ThingTypePropertiesOutputTypeDef(BaseValidatorModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[List[str]] = None
    mqtt5Configuration: Optional[Mqtt5ConfigurationOutputTypeDef] = None


class ThingTypePropertiesTypeDef(BaseValidatorModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[Sequence[str]] = None
    mqtt5Configuration: Optional[Mqtt5ConfigurationTypeDef] = None


class RepublishActionOutputTypeDef(BaseValidatorModel):
    roleArn: str
    topic: str
    qos: Optional[int] = None
    headers: Optional[MqttHeadersOutputTypeDef] = None


class AuditSuppressionTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: Optional[datetime] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None


class CreateAuditSuppressionRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    clientRequestToken: str
    expirationDate: Optional[TimestampTypeDef] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None


class DeleteAuditSuppressionRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef


class DescribeAuditSuppressionRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef


class DescribeAuditSuppressionResponseTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: datetime
    suppressIndefinitely: bool
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAuditFindingsRequestPaginateTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    listSuppressedFindings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAuditFindingsRequestTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    listSuppressedFindings: Optional[bool] = None


class ListAuditSuppressionsRequestPaginateTypeDef(BaseValidatorModel):
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAuditSuppressionsRequestTypeDef(BaseValidatorModel):
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    ascendingOrder: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class NonCompliantResourceTypeDef(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    additionalInfo: Optional[Dict[str, str]] = None


class RelatedResourceTypeDef(BaseValidatorModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    additionalInfo: Optional[Dict[str, str]] = None


class UpdateAuditSuppressionRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: Optional[TimestampTypeDef] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None


class SearchIndexResponseTypeDef(BaseValidatorModel):
    things: List[ThingDocumentTypeDef]
    thingGroups: List[ThingGroupDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateTopicRuleDestinationRequestTypeDef(BaseValidatorModel):
    destinationConfiguration: TopicRuleDestinationConfigurationTypeDef


class ListTopicRuleDestinationsResponseTypeDef(BaseValidatorModel):
    destinationSummaries: List[TopicRuleDestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateTopicRuleDestinationResponseTypeDef(BaseValidatorModel):
    topicRuleDestination: TopicRuleDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTopicRuleDestinationResponseTypeDef(BaseValidatorModel):
    topicRuleDestination: TopicRuleDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AuthResultTypeDef(BaseValidatorModel):
    authInfo: Optional[AuthInfoOutputTypeDef] = None
    allowed: Optional[AllowedTypeDef] = None
    denied: Optional[DeniedTypeDef] = None
    authDecision: Optional[AuthDecisionType] = None
    missingContextValues: Optional[List[str]] = None


class IotSiteWiseActionOutputTypeDef(BaseValidatorModel):
    putAssetPropertyValueEntries: List[PutAssetPropertyValueEntryOutputTypeDef]
    roleArn: str


class ThingGroupPropertiesUnionTypeDef(BaseValidatorModel):
    pass


class CreateDynamicThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    queryString: str
    thingGroupProperties: Optional[ThingGroupPropertiesUnionTypeDef] = None
    indexName: Optional[str] = None
    queryVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    parentGroupName: Optional[str] = None
    thingGroupProperties: Optional[ThingGroupPropertiesUnionTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateDynamicThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesUnionTypeDef
    expectedVersion: Optional[int] = None
    indexName: Optional[str] = None
    queryString: Optional[str] = None
    queryVersion: Optional[str] = None


class UpdateThingGroupRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesUnionTypeDef
    expectedVersion: Optional[int] = None


class ActiveViolationTypeDef(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorOutputTypeDef] = None
    lastViolationValue: Optional[MetricValueOutputTypeDef] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfoTypeDef] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    lastViolationTime: Optional[datetime] = None
    violationStartTime: Optional[datetime] = None


class DescribeSecurityProfileResponseTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List[BehaviorOutputTypeDef]
    alertTargets: Dict[Literal["SNS"], AlertTargetTypeDef]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List[MetricToRetainTypeDef]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime
    metricsExportConfig: MetricsExportConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSecurityProfileResponseTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List[BehaviorOutputTypeDef]
    alertTargets: Dict[Literal["SNS"], AlertTargetTypeDef]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List[MetricToRetainTypeDef]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime
    metricsExportConfig: MetricsExportConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ViolationEventTypeDef(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorOutputTypeDef] = None
    metricValue: Optional[MetricValueOutputTypeDef] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfoTypeDef] = None
    violationEventType: Optional[ViolationEventTypeType] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    violationEventTime: Optional[datetime] = None


class CodeSigningSignatureUnionTypeDef(BaseValidatorModel):
    pass


class CustomCodeSigningTypeDef(BaseValidatorModel):
    signature: Optional[CodeSigningSignatureUnionTypeDef] = None
    certificateChain: Optional[CodeSigningCertificateChainTypeDef] = None
    hashAlgorithm: Optional[str] = None
    signatureAlgorithm: Optional[str] = None


class CommandParameterValueUnionTypeDef(BaseValidatorModel):
    pass


class CommandParameterTypeDef(BaseValidatorModel):
    name: str
    value: Optional[CommandParameterValueUnionTypeDef] = None
    defaultValue: Optional[CommandParameterValueUnionTypeDef] = None
    description: Optional[str] = None


class ViolationEventOccurrenceRangeUnionTypeDef(BaseValidatorModel):
    pass


class DetectMitigationActionsTaskTargetUnionTypeDef(BaseValidatorModel):
    pass


class StartDetectMitigationActionsTaskRequestTypeDef(BaseValidatorModel):
    taskId: str
    target: DetectMitigationActionsTaskTargetUnionTypeDef
    actions: Sequence[str]
    clientRequestToken: str
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeUnionTypeDef] = None
    includeOnlyActiveViolations: Optional[bool] = None
    includeSuppressedAlerts: Optional[bool] = None


class CodeSigningOutputTypeDef(BaseValidatorModel):
    awsSignerJobId: Optional[str] = None
    startSigningJobParameter: Optional[StartSigningJobParameterTypeDef] = None
    customCodeSigning: Optional[CustomCodeSigningOutputTypeDef] = None


class DescribeJobTemplateResponseTypeDef(BaseValidatorModel):
    jobTemplateArn: str
    jobTemplateId: str
    description: str
    documentSource: str
    document: str
    createdAt: datetime
    presignedUrlConfig: PresignedUrlConfigTypeDef
    jobExecutionsRolloutConfig: JobExecutionsRolloutConfigTypeDef
    abortConfig: AbortConfigOutputTypeDef
    timeoutConfig: TimeoutConfigTypeDef
    jobExecutionsRetryConfig: JobExecutionsRetryConfigOutputTypeDef
    maintenanceWindows: List[MaintenanceWindowTypeDef]
    destinationPackageVersions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class JobTypeDef(BaseValidatorModel):
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    targetSelection: Optional[TargetSelectionType] = None
    status: Optional[JobStatusType] = None
    forceCanceled: Optional[bool] = None
    reasonCode: Optional[str] = None
    comment: Optional[str] = None
    targets: Optional[List[str]] = None
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigOutputTypeDef] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    jobProcessDetails: Optional[JobProcessDetailsTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    namespaceId: Optional[str] = None
    jobTemplateArn: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigOutputTypeDef] = None
    documentParameters: Optional[Dict[str, str]] = None
    isConcurrent: Optional[bool] = None
    schedulingConfig: Optional[SchedulingConfigOutputTypeDef] = None
    scheduledJobRollouts: Optional[List[ScheduledJobRolloutTypeDef]] = None
    destinationPackageVersions: Optional[List[str]] = None


class DescribeStreamResponseTypeDef(BaseValidatorModel):
    streamInfo: StreamInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ThingIndexingConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class GetIndexingConfigurationResponseTypeDef(BaseValidatorModel):
    thingIndexingConfiguration: ThingIndexingConfigurationOutputTypeDef
    thingGroupIndexingConfiguration: ThingGroupIndexingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SchedulingConfigUnionTypeDef(BaseValidatorModel):
    pass


class JobExecutionsRetryConfigUnionTypeDef(BaseValidatorModel):
    pass


class AbortConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    targets: Sequence[str]
    documentSource: Optional[str] = None
    document: Optional[str] = None
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    targetSelection: Optional[TargetSelectionType] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigUnionTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    namespaceId: Optional[str] = None
    jobTemplateArn: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigUnionTypeDef] = None
    documentParameters: Optional[Mapping[str, str]] = None
    schedulingConfig: Optional[SchedulingConfigUnionTypeDef] = None
    destinationPackageVersions: Optional[Sequence[str]] = None


class CreateJobTemplateRequestTypeDef(BaseValidatorModel):
    jobTemplateId: str
    description: str
    jobArn: Optional[str] = None
    documentSource: Optional[str] = None
    document: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigUnionTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigUnionTypeDef] = None
    maintenanceWindows: Optional[Sequence[MaintenanceWindowTypeDef]] = None
    destinationPackageVersions: Optional[Sequence[str]] = None


class UpdateJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigUnionTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    namespaceId: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigUnionTypeDef] = None


class MitigationActionTypeDef(BaseValidatorModel):
    pass


class DescribeAuditMitigationActionsTaskResponseTypeDef(BaseValidatorModel):
    taskStatus: AuditMitigationActionsTaskStatusType
    startTime: datetime
    endTime: datetime
    taskStatistics: Dict[str, TaskStatisticsForAuditCheckTypeDef]
    target: AuditMitigationActionsTaskTargetOutputTypeDef
    auditCheckToActionsMapping: Dict[str, List[str]]
    actionsDefinition: List[MitigationActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DetectMitigationActionsTaskSummaryTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    taskStatus: Optional[DetectMitigationActionsTaskStatusType] = None
    taskStartTime: Optional[datetime] = None
    taskEndTime: Optional[datetime] = None
    target: Optional[DetectMitigationActionsTaskTargetOutputTypeDef] = None
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeOutputTypeDef] = None
    onlyActiveViolationsIncluded: Optional[bool] = None
    suppressedAlertsIncluded: Optional[bool] = None
    actionsDefinition: Optional[List[MitigationActionTypeDef]] = None
    taskStatistics: Optional[DetectMitigationActionsTaskStatisticsTypeDef] = None


class MitigationActionParamsUnionTypeDef(BaseValidatorModel):
    pass


class CreateMitigationActionRequestTypeDef(BaseValidatorModel):
    actionName: str
    roleArn: str
    actionParams: MitigationActionParamsUnionTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateMitigationActionRequestTypeDef(BaseValidatorModel):
    actionName: str
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsUnionTypeDef] = None


class DescribeThingTypeResponseTypeDef(BaseValidatorModel):
    thingTypeName: str
    thingTypeId: str
    thingTypeArn: str
    thingTypeProperties: ThingTypePropertiesOutputTypeDef
    thingTypeMetadata: ThingTypeMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ThingTypeDefinitionTypeDef(BaseValidatorModel):
    thingTypeName: Optional[str] = None
    thingTypeArn: Optional[str] = None
    thingTypeProperties: Optional[ThingTypePropertiesOutputTypeDef] = None
    thingTypeMetadata: Optional[ThingTypeMetadataTypeDef] = None


class MqttHeadersUnionTypeDef(BaseValidatorModel):
    pass


class RepublishActionTypeDef(BaseValidatorModel):
    roleArn: str
    topic: str
    qos: Optional[int] = None
    headers: Optional[MqttHeadersUnionTypeDef] = None


class ListAuditSuppressionsResponseTypeDef(BaseValidatorModel):
    suppressions: List[AuditSuppressionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AuditFindingTypeDef(BaseValidatorModel):
    findingId: Optional[str] = None
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    taskStartTime: Optional[datetime] = None
    findingTime: Optional[datetime] = None
    severity: Optional[AuditFindingSeverityType] = None
    nonCompliantResource: Optional[NonCompliantResourceTypeDef] = None
    relatedResources: Optional[List[RelatedResourceTypeDef]] = None
    reasonForNonCompliance: Optional[str] = None
    reasonForNonComplianceCode: Optional[str] = None
    isSuppressed: Optional[bool] = None


class ListRelatedResourcesForAuditFindingResponseTypeDef(BaseValidatorModel):
    relatedResources: List[RelatedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TestAuthorizationResponseTypeDef(BaseValidatorModel):
    authResults: List[AuthResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutAssetPropertyValueEntryUnionTypeDef(BaseValidatorModel):
    pass


class IotSiteWiseActionTypeDef(BaseValidatorModel):
    putAssetPropertyValueEntries: Sequence[PutAssetPropertyValueEntryUnionTypeDef]
    roleArn: str


class ListActiveViolationsResponseTypeDef(BaseValidatorModel):
    activeViolations: List[ActiveViolationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListViolationEventsResponseTypeDef(BaseValidatorModel):
    violationEvents: List[ViolationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class OTAUpdateFileOutputTypeDef(BaseValidatorModel):
    fileName: Optional[str] = None
    fileType: Optional[int] = None
    fileVersion: Optional[str] = None
    fileLocation: Optional[FileLocationTypeDef] = None
    codeSigning: Optional[CodeSigningOutputTypeDef] = None
    attributes: Optional[Dict[str, str]] = None


class DescribeJobResponseTypeDef(BaseValidatorModel):
    documentSource: str
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ThingGroupIndexingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ThingIndexingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateIndexingConfigurationRequestTypeDef(BaseValidatorModel):
    thingIndexingConfiguration: Optional[ThingIndexingConfigurationUnionTypeDef] = None
    thingGroupIndexingConfiguration: Optional[ThingGroupIndexingConfigurationUnionTypeDef] = None


class BehaviorCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class BehaviorTypeDef(BaseValidatorModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimensionTypeDef] = None
    criteria: Optional[BehaviorCriteriaUnionTypeDef] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None


class DescribeDetectMitigationActionsTaskResponseTypeDef(BaseValidatorModel):
    taskSummary: DetectMitigationActionsTaskSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDetectMitigationActionsTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[DetectMitigationActionsTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListThingTypesResponseTypeDef(BaseValidatorModel):
    thingTypes: List[ThingTypeDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ThingTypePropertiesUnionTypeDef(BaseValidatorModel):
    pass


class CreateThingTypeRequestTypeDef(BaseValidatorModel):
    thingTypeName: str
    thingTypeProperties: Optional[ThingTypePropertiesUnionTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateThingTypeRequestTypeDef(BaseValidatorModel):
    thingTypeName: str
    thingTypeProperties: Optional[ThingTypePropertiesUnionTypeDef] = None


class DescribeAuditFindingResponseTypeDef(BaseValidatorModel):
    finding: AuditFindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAuditFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[AuditFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ActionOutputTypeDef(BaseValidatorModel):
    pass


class TopicRuleTypeDef(BaseValidatorModel):
    ruleName: Optional[str] = None
    sql: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    actions: Optional[List[ActionOutputTypeDef]] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionOutputTypeDef] = None


class CustomCodeSigningUnionTypeDef(BaseValidatorModel):
    pass


class CodeSigningTypeDef(BaseValidatorModel):
    awsSignerJobId: Optional[str] = None
    startSigningJobParameter: Optional[StartSigningJobParameterTypeDef] = None
    customCodeSigning: Optional[CustomCodeSigningUnionTypeDef] = None


class CommandPayloadUnionTypeDef(BaseValidatorModel):
    pass


class CommandParameterUnionTypeDef(BaseValidatorModel):
    pass


class CreateCommandRequestTypeDef(BaseValidatorModel):
    commandId: str
    namespace: Optional[CommandNamespaceType] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    payload: Optional[CommandPayloadUnionTypeDef] = None
    mandatoryParameters: Optional[Sequence[CommandParameterUnionTypeDef]] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class OTAUpdateInfoTypeDef(BaseValidatorModel):
    otaUpdateId: Optional[str] = None
    otaUpdateArn: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    description: Optional[str] = None
    targets: Optional[List[str]] = None
    protocols: Optional[List[ProtocolType]] = None
    awsJobExecutionsRolloutConfig: Optional[AwsJobExecutionsRolloutConfigTypeDef] = None
    awsJobPresignedUrlConfig: Optional[AwsJobPresignedUrlConfigTypeDef] = None
    targetSelection: Optional[TargetSelectionType] = None
    otaUpdateFiles: Optional[List[OTAUpdateFileOutputTypeDef]] = None
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None
    awsIotJobId: Optional[str] = None
    awsIotJobArn: Optional[str] = None
    errorInfo: Optional[ErrorInfoTypeDef] = None
    additionalParameters: Optional[Dict[str, str]] = None


class GetTopicRuleResponseTypeDef(BaseValidatorModel):
    ruleArn: str
    rule: TopicRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetOTAUpdateResponseTypeDef(BaseValidatorModel):
    otaUpdateInfo: OTAUpdateInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BehaviorUnionTypeDef(BaseValidatorModel):
    pass


class CreateSecurityProfileRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileDescription: Optional[str] = None
    behaviors: Optional[Sequence[BehaviorUnionTypeDef]] = None
    alertTargets: Optional[Mapping[Literal["SNS"], AlertTargetTypeDef]] = None
    additionalMetricsToRetain: Optional[Sequence[str]] = None
    additionalMetricsToRetainV2: Optional[Sequence[MetricToRetainTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    metricsExportConfig: Optional[MetricsExportConfigTypeDef] = None


class UpdateSecurityProfileRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileDescription: Optional[str] = None
    behaviors: Optional[Sequence[BehaviorUnionTypeDef]] = None
    alertTargets: Optional[Mapping[Literal["SNS"], AlertTargetTypeDef]] = None
    additionalMetricsToRetain: Optional[Sequence[str]] = None
    additionalMetricsToRetainV2: Optional[Sequence[MetricToRetainTypeDef]] = None
    deleteBehaviors: Optional[bool] = None
    deleteAlertTargets: Optional[bool] = None
    deleteAdditionalMetricsToRetain: Optional[bool] = None
    expectedVersion: Optional[int] = None
    metricsExportConfig: Optional[MetricsExportConfigTypeDef] = None
    deleteMetricsExportConfig: Optional[bool] = None


class ValidateSecurityProfileBehaviorsRequestTypeDef(BaseValidatorModel):
    behaviors: Sequence[BehaviorUnionTypeDef]


class CodeSigningUnionTypeDef(BaseValidatorModel):
    pass


class OTAUpdateFileTypeDef(BaseValidatorModel):
    fileName: Optional[str] = None
    fileType: Optional[int] = None
    fileVersion: Optional[str] = None
    fileLocation: Optional[FileLocationTypeDef] = None
    codeSigning: Optional[CodeSigningUnionTypeDef] = None
    attributes: Optional[Mapping[str, str]] = None


class ActionUnionTypeDef(BaseValidatorModel):
    pass


class TopicRulePayloadTypeDef(BaseValidatorModel):
    sql: str
    actions: Sequence[ActionUnionTypeDef]
    description: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionUnionTypeDef] = None


class CreateTopicRuleRequestTypeDef(BaseValidatorModel):
    ruleName: str
    topicRulePayload: TopicRulePayloadTypeDef
    tags: Optional[str] = None


class ReplaceTopicRuleRequestTypeDef(BaseValidatorModel):
    ruleName: str
    topicRulePayload: TopicRulePayloadTypeDef


class OTAUpdateFileUnionTypeDef(BaseValidatorModel):
    pass


class CreateOTAUpdateRequestTypeDef(BaseValidatorModel):
    otaUpdateId: str
    targets: Sequence[str]
    files: Sequence[OTAUpdateFileUnionTypeDef]
    roleArn: str
    description: Optional[str] = None
    protocols: Optional[Sequence[ProtocolType]] = None
    targetSelection: Optional[TargetSelectionType] = None
    awsJobExecutionsRolloutConfig: Optional[AwsJobExecutionsRolloutConfigTypeDef] = None
    awsJobPresignedUrlConfig: Optional[AwsJobPresignedUrlConfigTypeDef] = None
    awsJobAbortConfig: Optional[AwsJobAbortConfigTypeDef] = None
    awsJobTimeoutConfig: Optional[AwsJobTimeoutConfigTypeDef] = None
    additionalParameters: Optional[Mapping[str, str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


