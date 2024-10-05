from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AcceptCertificateTransferRequestRequestTypeDef(BaseValidatorModel):
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

class ElasticsearchActionTypeDef(BaseValidatorModel):
    roleArn: str
    endpoint: str
    index: str
    type: str
    id: str

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

class OpenSearchActionTypeDef(BaseValidatorModel):
    roleArn: str
    endpoint: str
    index: str
    type: str
    id: str

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

class MetricValuePaginatorTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    cidrs: Optional[List[str]] = None
    ports: Optional[List[int]] = None
    number: Optional[float] = None
    numbers: Optional[List[float]] = None
    strings: Optional[List[str]] = None

class ViolationEventAdditionalInfoTypeDef(BaseValidatorModel):
    confidenceLevel: Optional[ConfidenceLevelType] = None

class MetricValueTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    cidrs: Optional[Sequence[str]] = None
    ports: Optional[Sequence[int]] = None
    number: Optional[float] = None
    numbers: Optional[Sequence[float]] = None
    strings: Optional[Sequence[str]] = None

class AddThingToBillingGroupRequestRequestTypeDef(BaseValidatorModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None

class AddThingToThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None
    overrideDynamicGroups: Optional[bool] = None

class AddThingsToThingGroupParamsPaginatorTypeDef(BaseValidatorModel):
    thingGroupNames: List[str]
    overrideDynamicGroups: Optional[bool] = None

class AddThingsToThingGroupParamsTypeDef(BaseValidatorModel):
    thingGroupNames: Sequence[str]
    overrideDynamicGroups: Optional[bool] = None

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

class AssociateTargetsWithJobRequestRequestTypeDef(BaseValidatorModel):
    targets: Sequence[str]
    jobId: str
    comment: Optional[str] = None
    namespaceId: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AttachPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    target: str

class AttachPrincipalPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    principal: str

class AttachSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileTargetArn: str

class AttachThingPrincipalRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    principal: str

class AttributePayloadTypeDef(BaseValidatorModel):
    attributes: Optional[Mapping[str, str]] = None
    merge: Optional[bool] = None

class AuditCheckConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None

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

class AuditMitigationActionsTaskTargetTypeDef(BaseValidatorModel):
    auditTaskId: Optional[str] = None
    findingIds: Optional[List[str]] = None
    auditCheckToReasonCodeFilter: Optional[Dict[str, List[str]]] = None

class AuditNotificationTargetTypeDef(BaseValidatorModel):
    targetArn: Optional[str] = None
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None

class AuditTaskMetadataTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    taskType: Optional[AuditTaskTypeType] = None

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

class MetricDimensionTypeDef(BaseValidatorModel):
    dimensionName: str
    operator: Optional[DimensionValueOperatorType] = None

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

class CancelAuditMitigationActionsTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class CancelAuditTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class CancelCertificateTransferRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str

class CancelDetectMitigationActionsTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class CancelJobExecutionRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    force: Optional[bool] = None
    expectedVersion: Optional[int] = None
    statusDetails: Optional[Mapping[str, str]] = None

class CancelJobRequestRequestTypeDef(BaseValidatorModel):
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

class CodeSigningCertificateChainTypeDef(BaseValidatorModel):
    certificateName: Optional[str] = None
    inlineDocument: Optional[str] = None

class ConfigurationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class ConfirmTopicRuleDestinationRequestRequestTypeDef(BaseValidatorModel):
    confirmationToken: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class CreateCertificateFromCsrRequestRequestTypeDef(BaseValidatorModel):
    certificateSigningRequest: str
    setAsActive: Optional[bool] = None

class ServerCertificateConfigTypeDef(BaseValidatorModel):
    enableOCSPCheck: Optional[bool] = None

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

class CreateKeysAndCertificateRequestRequestTypeDef(BaseValidatorModel):
    setAsActive: Optional[bool] = None

class KeyPairTypeDef(BaseValidatorModel):
    PublicKey: Optional[str] = None
    PrivateKey: Optional[str] = None

class CreatePackageRequestRequestTypeDef(BaseValidatorModel):
    packageName: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreatePackageVersionRequestRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreatePolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyDocument: str
    setAsDefault: Optional[bool] = None

class CreateProvisioningClaimRequestRequestTypeDef(BaseValidatorModel):
    templateName: str

class ProvisioningHookTypeDef(BaseValidatorModel):
    targetArn: str
    payloadVersion: Optional[str] = None

class CreateProvisioningTemplateVersionRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateBody: str
    setAsDefault: Optional[bool] = None

class MetricsExportConfigTypeDef(BaseValidatorModel):
    mqttTopic: str
    roleArn: str

class ThingTypePropertiesTypeDef(BaseValidatorModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[Sequence[str]] = None

class DeleteAccountAuditConfigurationRequestRequestTypeDef(BaseValidatorModel):
    deleteScheduledAudits: Optional[bool] = None

class DeleteAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    authorizerName: str

class DeleteBillingGroupRequestRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    expectedVersion: Optional[int] = None

class DeleteCACertificateRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str

class DeleteCertificateProviderRequestRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str

class DeleteCertificateRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str
    forceDelete: Optional[bool] = None

class DeleteCustomMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str

class DeleteDimensionRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteDomainConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str

class DeleteDynamicThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None

class DeleteFleetMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str
    expectedVersion: Optional[int] = None

class DeleteJobExecutionRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    executionNumber: int
    force: Optional[bool] = None
    namespaceId: Optional[str] = None

class DeleteJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    force: Optional[bool] = None
    namespaceId: Optional[str] = None

class DeleteJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    jobTemplateId: str

class DeleteMitigationActionRequestRequestTypeDef(BaseValidatorModel):
    actionName: str

class DeleteOTAUpdateRequestRequestTypeDef(BaseValidatorModel):
    otaUpdateId: str
    deleteStream: Optional[bool] = None
    forceDeleteAWSJob: Optional[bool] = None

class DeletePackageRequestRequestTypeDef(BaseValidatorModel):
    packageName: str
    clientToken: Optional[str] = None

class DeletePackageVersionRequestRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    clientToken: Optional[str] = None

class DeletePolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str

class DeletePolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyVersionId: str

class DeleteProvisioningTemplateRequestRequestTypeDef(BaseValidatorModel):
    templateName: str

class DeleteProvisioningTemplateVersionRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    versionId: int

class DeleteRoleAliasRequestRequestTypeDef(BaseValidatorModel):
    roleAlias: str

class DeleteScheduledAuditRequestRequestTypeDef(BaseValidatorModel):
    scheduledAuditName: str

class DeleteSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    expectedVersion: Optional[int] = None

class DeleteStreamRequestRequestTypeDef(BaseValidatorModel):
    streamId: str

class DeleteThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None

class DeleteThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    expectedVersion: Optional[int] = None

class DeleteThingTypeRequestRequestTypeDef(BaseValidatorModel):
    thingTypeName: str

class DeleteTopicRuleDestinationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteTopicRuleRequestRequestTypeDef(BaseValidatorModel):
    ruleName: str

class DeleteV2LoggingLevelRequestRequestTypeDef(BaseValidatorModel):
    targetType: LogTargetTypeType
    targetName: str

class DeprecateThingTypeRequestRequestTypeDef(BaseValidatorModel):
    thingTypeName: str
    undoDeprecate: Optional[bool] = None

class DescribeAuditFindingRequestRequestTypeDef(BaseValidatorModel):
    findingId: str

class DescribeAuditMitigationActionsTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class TaskStatisticsForAuditCheckTypeDef(BaseValidatorModel):
    totalFindingsCount: Optional[int] = None
    failedFindingsCount: Optional[int] = None
    succeededFindingsCount: Optional[int] = None
    skippedFindingsCount: Optional[int] = None
    canceledFindingsCount: Optional[int] = None

class DescribeAuditTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class TaskStatisticsTypeDef(BaseValidatorModel):
    totalChecks: Optional[int] = None
    inProgressChecks: Optional[int] = None
    waitingForDataCollectionChecks: Optional[int] = None
    compliantChecks: Optional[int] = None
    nonCompliantChecks: Optional[int] = None
    failedChecks: Optional[int] = None
    canceledChecks: Optional[int] = None

class DescribeAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    authorizerName: str

class DescribeBillingGroupRequestRequestTypeDef(BaseValidatorModel):
    billingGroupName: str

class DescribeCACertificateRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str

class RegistrationConfigTypeDef(BaseValidatorModel):
    templateBody: Optional[str] = None
    roleArn: Optional[str] = None
    templateName: Optional[str] = None

class DescribeCertificateProviderRequestRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str

class DescribeCertificateRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str

class DescribeCustomMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str

class DescribeDetectMitigationActionsTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class DescribeDimensionRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DescribeDomainConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str

class ServerCertificateSummaryTypeDef(BaseValidatorModel):
    serverCertificateArn: Optional[str] = None
    serverCertificateStatus: Optional[ServerCertificateStatusType] = None
    serverCertificateStatusDetail: Optional[str] = None

class DescribeEndpointRequestRequestTypeDef(BaseValidatorModel):
    endpointType: Optional[str] = None

class DescribeFleetMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str

class DescribeIndexRequestRequestTypeDef(BaseValidatorModel):
    indexName: str

class DescribeJobExecutionRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    thingName: str
    executionNumber: Optional[int] = None

class DescribeJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class DescribeJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    jobTemplateId: str

class DescribeManagedJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateVersion: Optional[str] = None

class DocumentParameterTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    description: Optional[str] = None
    regex: Optional[str] = None
    example: Optional[str] = None
    optional: Optional[bool] = None

class DescribeMitigationActionRequestRequestTypeDef(BaseValidatorModel):
    actionName: str

class DescribeProvisioningTemplateRequestRequestTypeDef(BaseValidatorModel):
    templateName: str

class DescribeProvisioningTemplateVersionRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    versionId: int

class DescribeRoleAliasRequestRequestTypeDef(BaseValidatorModel):
    roleAlias: str

class RoleAliasDescriptionTypeDef(BaseValidatorModel):
    roleAlias: Optional[str] = None
    roleAliasArn: Optional[str] = None
    roleArn: Optional[str] = None
    owner: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None

class DescribeScheduledAuditRequestRequestTypeDef(BaseValidatorModel):
    scheduledAuditName: str

class DescribeSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: str

class DescribeStreamRequestRequestTypeDef(BaseValidatorModel):
    streamId: str

class DescribeThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str

class DescribeThingRegistrationTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class DescribeThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str

class DescribeThingTypeRequestRequestTypeDef(BaseValidatorModel):
    thingTypeName: str

class ThingTypeMetadataTypeDef(BaseValidatorModel):
    deprecated: Optional[bool] = None
    deprecationDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None

class S3DestinationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None

class DetachPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    target: str

class DetachPrincipalPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    principal: str

class DetachSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileTargetArn: str

class DetachThingPrincipalRequestRequestTypeDef(BaseValidatorModel):
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

class DetectMitigationActionsTaskTargetTypeDef(BaseValidatorModel):
    violationIds: Optional[List[str]] = None
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None

class ViolationEventOccurrenceRangeTypeDef(BaseValidatorModel):
    startTime: datetime
    endTime: datetime

class DisableTopicRuleRequestRequestTypeDef(BaseValidatorModel):
    ruleName: str

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

class EnableTopicRuleRequestRequestTypeDef(BaseValidatorModel):
    ruleName: str

class ErrorInfoTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None

class RateIncreaseCriteriaTypeDef(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None

class FieldTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[FieldTypeType] = None

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

class GetBehaviorModelTrainingSummariesRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetCardinalityRequestRequestTypeDef(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None

class GetEffectivePoliciesRequestRequestTypeDef(BaseValidatorModel):
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    thingName: Optional[str] = None

class GetJobDocumentRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class GetOTAUpdateRequestRequestTypeDef(BaseValidatorModel):
    otaUpdateId: str

class VersionUpdateByJobsConfigTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    roleArn: Optional[str] = None

class GetPackageRequestRequestTypeDef(BaseValidatorModel):
    packageName: str

class GetPackageVersionRequestRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str

class GetPercentilesRequestRequestTypeDef(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None
    percents: Optional[Sequence[float]] = None

class PercentPairTypeDef(BaseValidatorModel):
    percent: Optional[float] = None
    value: Optional[float] = None

class GetPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str

class GetPolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyVersionId: str

class GetStatisticsRequestRequestTypeDef(BaseValidatorModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None

class StatisticsTypeDef(BaseValidatorModel):
    count: Optional[int] = None
    average: Optional[float] = None
    sum: Optional[float] = None
    minimum: Optional[float] = None
    maximum: Optional[float] = None
    sumOfSquares: Optional[float] = None
    variance: Optional[float] = None
    stdDeviation: Optional[float] = None

class GetTopicRuleDestinationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetTopicRuleRequestRequestTypeDef(BaseValidatorModel):
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

class ListActiveViolationsRequestRequestTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAttachedPoliciesRequestRequestTypeDef(BaseValidatorModel):
    target: str
    recursive: Optional[bool] = None
    marker: Optional[str] = None
    pageSize: Optional[int] = None

class ListAuditMitigationActionsExecutionsRequestRequestTypeDef(BaseValidatorModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAuthorizersRequestRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None

class ListBillingGroupsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namePrefixFilter: Optional[str] = None

class ListCACertificatesRequestRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None

class ListCertificateProvidersRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListCertificatesByCARequestRequestTypeDef(BaseValidatorModel):
    caCertificateId: str
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListCertificatesRequestRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListCustomMetricsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDimensionsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDomainConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    serviceType: Optional[ServiceTypeType] = None

class ListFleetMetricsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListIndicesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListJobExecutionsForJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobExecutionsForThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    jobId: Optional[str] = None

class ListJobTemplatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None

class ListManagedJobTemplatesRequestRequestTypeDef(BaseValidatorModel):
    templateName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ManagedJobTemplateSummaryTypeDef(BaseValidatorModel):
    templateArn: Optional[str] = None
    templateName: Optional[str] = None
    description: Optional[str] = None
    environments: Optional[List[str]] = None
    templateVersion: Optional[str] = None

class ListMitigationActionsRequestRequestTypeDef(BaseValidatorModel):
    actionType: Optional[MitigationActionTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MitigationActionIdentifierTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    actionArn: Optional[str] = None
    creationDate: Optional[datetime] = None

class ListOTAUpdatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None

class OTAUpdateSummaryTypeDef(BaseValidatorModel):
    otaUpdateId: Optional[str] = None
    otaUpdateArn: Optional[str] = None
    creationDate: Optional[datetime] = None

class ListOutgoingCertificatesRequestRequestTypeDef(BaseValidatorModel):
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

class ListPackageVersionsRequestRequestTypeDef(BaseValidatorModel):
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

class ListPackagesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PackageSummaryTypeDef(BaseValidatorModel):
    packageName: Optional[str] = None
    defaultVersionName: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None

class ListPoliciesRequestRequestTypeDef(BaseValidatorModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None

class ListPolicyPrincipalsRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None

class ListPolicyVersionsRequestRequestTypeDef(BaseValidatorModel):
    policyName: str

class PolicyVersionTypeDef(BaseValidatorModel):
    versionId: Optional[str] = None
    isDefaultVersion: Optional[bool] = None
    createDate: Optional[datetime] = None

class ListPrincipalPoliciesRequestRequestTypeDef(BaseValidatorModel):
    principal: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None

class ListPrincipalThingsRequestRequestTypeDef(BaseValidatorModel):
    principal: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProvisioningTemplateVersionsRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ProvisioningTemplateVersionSummaryTypeDef(BaseValidatorModel):
    versionId: Optional[int] = None
    creationDate: Optional[datetime] = None
    isDefaultVersion: Optional[bool] = None

class ListProvisioningTemplatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ProvisioningTemplateSummaryTypeDef(BaseValidatorModel):
    templateArn: Optional[str] = None
    templateName: Optional[str] = None
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    enabled: Optional[bool] = None
    type: Optional[TemplateTypeType] = None

class ListRelatedResourcesForAuditFindingRequestRequestTypeDef(BaseValidatorModel):
    findingId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListRoleAliasesRequestRequestTypeDef(BaseValidatorModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListScheduledAuditsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ScheduledAuditMetadataTypeDef(BaseValidatorModel):
    scheduledAuditName: Optional[str] = None
    scheduledAuditArn: Optional[str] = None
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None

class ListSecurityProfilesForTargetRequestRequestTypeDef(BaseValidatorModel):
    securityProfileTargetArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    recursive: Optional[bool] = None

class ListSecurityProfilesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None

class SecurityProfileIdentifierTypeDef(BaseValidatorModel):
    name: str
    arn: str

class ListStreamsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class StreamSummaryTypeDef(BaseValidatorModel):
    streamId: Optional[str] = None
    streamArn: Optional[str] = None
    streamVersion: Optional[int] = None
    description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None

class ListTargetsForPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None

class ListTargetsForSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SecurityProfileTargetTypeDef(BaseValidatorModel):
    arn: str

class ListThingGroupsForThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingGroupsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None

class ListThingPrincipalsRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingRegistrationTaskReportsRequestRequestTypeDef(BaseValidatorModel):
    taskId: str
    reportType: ReportTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingRegistrationTasksRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[StatusType] = None

class ListThingTypesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingTypeName: Optional[str] = None

class ListThingsInBillingGroupRequestRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingsInThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingsRequestRequestTypeDef(BaseValidatorModel):
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

class ListTopicRuleDestinationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTopicRulesRequestRequestTypeDef(BaseValidatorModel):
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

class ListV2LoggingLevelsRequestRequestTypeDef(BaseValidatorModel):
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

class PublishFindingToSnsParamsTypeDef(BaseValidatorModel):
    topicArn: str

class ReplaceDefaultPolicyVersionParamsTypeDef(BaseValidatorModel):
    templateName: Literal["BLANK_POLICY"]

class UpdateCACertificateParamsTypeDef(BaseValidatorModel):
    action: Literal["DEACTIVATE"]

class UpdateDeviceCertificateParamsTypeDef(BaseValidatorModel):
    action: Literal["DEACTIVATE"]

class UserPropertyTypeDef(BaseValidatorModel):
    key: str
    value: str

class PolicyVersionIdentifierTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyVersionId: Optional[str] = None

class PutVerificationStateOnViolationRequestRequestTypeDef(BaseValidatorModel):
    violationId: str
    verificationState: VerificationStateType
    verificationStateDescription: Optional[str] = None

class RegisterCertificateRequestRequestTypeDef(BaseValidatorModel):
    certificatePem: str
    caCertificatePem: Optional[str] = None
    setAsActive: Optional[bool] = None
    status: Optional[CertificateStatusType] = None

class RegisterCertificateWithoutCARequestRequestTypeDef(BaseValidatorModel):
    certificatePem: str
    status: Optional[CertificateStatusType] = None

class RegisterThingRequestRequestTypeDef(BaseValidatorModel):
    templateBody: str
    parameters: Optional[Mapping[str, str]] = None

class RejectCertificateTransferRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str
    rejectReason: Optional[str] = None

class RemoveThingFromBillingGroupRequestRequestTypeDef(BaseValidatorModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None

class RemoveThingFromThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None

class SearchIndexRequestRequestTypeDef(BaseValidatorModel):
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

class SetDefaultAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    authorizerName: str

class SetDefaultPolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyVersionId: str

class SetV2LoggingOptionsRequestRequestTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    defaultLogLevel: Optional[LogLevelType] = None
    disableAllLogs: Optional[bool] = None

class SigningProfileParameterTypeDef(BaseValidatorModel):
    certificateArn: Optional[str] = None
    platform: Optional[str] = None
    certificatePathOnDevice: Optional[str] = None

class StartOnDemandAuditTaskRequestRequestTypeDef(BaseValidatorModel):
    targetCheckNames: Sequence[str]

class StartThingRegistrationTaskRequestRequestTypeDef(BaseValidatorModel):
    templateBody: str
    inputFileBucket: str
    inputFileKey: str
    roleArn: str

class StopThingRegistrationTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class TlsContextTypeDef(BaseValidatorModel):
    serverName: Optional[str] = None

class ThingConnectivityTypeDef(BaseValidatorModel):
    connected: Optional[bool] = None
    timestamp: Optional[int] = None
    disconnectReason: Optional[str] = None

class ThingTypePropertiesPaginatorTypeDef(BaseValidatorModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[List[str]] = None

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

class TransferCertificateRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str
    targetAwsAccount: str
    transferMessage: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    authorizerName: str
    authorizerFunctionArn: Optional[str] = None
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Mapping[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    enableCachingForHttp: Optional[bool] = None

class UpdateCertificateProviderRequestRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str
    lambdaFunctionArn: Optional[str] = None
    accountDefaultForOperations: Optional[Sequence[Literal["CreateCertificateFromCsr"]]] = None

class UpdateCertificateRequestRequestTypeDef(BaseValidatorModel):
    certificateId: str
    newStatus: CertificateStatusType

class UpdateCustomMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str
    displayName: str

class UpdateDimensionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    stringValues: Sequence[str]

class UpdatePackageRequestRequestTypeDef(BaseValidatorModel):
    packageName: str
    description: Optional[str] = None
    defaultVersionName: Optional[str] = None
    unsetDefaultVersion: Optional[bool] = None
    clientToken: Optional[str] = None

class UpdatePackageVersionRequestRequestTypeDef(BaseValidatorModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    action: Optional[PackageVersionActionType] = None
    clientToken: Optional[str] = None

class UpdateRoleAliasRequestRequestTypeDef(BaseValidatorModel):
    roleAlias: str
    roleArn: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None

class UpdateScheduledAuditRequestRequestTypeDef(BaseValidatorModel):
    scheduledAuditName: str
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    targetCheckNames: Optional[Sequence[str]] = None

class UpdateThingGroupsForThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    thingGroupsToAdd: Optional[Sequence[str]] = None
    thingGroupsToRemove: Optional[Sequence[str]] = None
    overrideDynamicGroups: Optional[bool] = None

class UpdateTopicRuleDestinationRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    status: TopicRuleDestinationStatusType

class ValidationErrorTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None

class AbortConfigTypeDef(BaseValidatorModel):
    criteriaList: Sequence[AbortCriteriaTypeDef]

class MetricDatumPaginatorTypeDef(BaseValidatorModel):
    timestamp: Optional[datetime] = None
    value: Optional[MetricValuePaginatorTypeDef] = None

class MetricDatumTypeDef(BaseValidatorModel):
    timestamp: Optional[datetime] = None
    value: Optional[MetricValueTypeDef] = None

class UpdateFleetMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str
    indexName: str
    queryString: Optional[str] = None
    aggregationType: Optional[AggregationTypeTypeDef] = None
    period: Optional[int] = None
    aggregationField: Optional[str] = None
    description: Optional[str] = None
    queryVersion: Optional[str] = None
    unit: Optional[FleetMetricUnitType] = None
    expectedVersion: Optional[int] = None

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

class DescribeDimensionResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    type: Literal["TOPIC_FILTER"]
    stringValues: List[str]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointResponseTypeDef(BaseValidatorModel):
    endpointAddress: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetMetricResponseTypeDef(BaseValidatorModel):
    metricName: str
    queryString: str
    aggregationType: AggregationTypeTypeDef
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

class GetPackageVersionResponseTypeDef(BaseValidatorModel):
    packageVersionArn: str
    packageName: str
    versionName: str
    description: str
    attributes: Dict[str, str]
    status: PackageVersionStatusType
    errorReason: str
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDimensionsResponseTypeDef(BaseValidatorModel):
    dimensionNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndicesResponseTypeDef(BaseValidatorModel):
    indexNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingRegistrationTaskReportsResponseTypeDef(BaseValidatorModel):
    resourceLinks: List[str]
    reportType: ReportTypeType
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingRegistrationTasksResponseTypeDef(BaseValidatorModel):
    taskIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingsInBillingGroupResponseTypeDef(BaseValidatorModel):
    things: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingsInThingGroupResponseTypeDef(BaseValidatorModel):
    things: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class UpdateCustomMetricResponseTypeDef(BaseValidatorModel):
    metricName: str
    metricArn: str
    metricType: CustomMetricTypeType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDimensionResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    type: Literal["TOPIC_FILTER"]
    stringValues: List[str]
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

class CreateThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadTypeDef] = None
    billingGroupName: Optional[str] = None

class ThingGroupPropertiesTypeDef(BaseValidatorModel):
    thingGroupDescription: Optional[str] = None
    attributePayload: Optional[AttributePayloadTypeDef] = None

class UpdateThingRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadTypeDef] = None
    expectedVersion: Optional[int] = None
    removeThingType: Optional[bool] = None

class ListAuditMitigationActionsExecutionsResponseTypeDef(BaseValidatorModel):
    actionsExecutions: List[AuditMitigationActionExecutionMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAuditMitigationActionsTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[AuditMitigationActionsTaskMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAuditMitigationActionsTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str
    target: AuditMitigationActionsTaskTargetTypeDef
    auditCheckToActionsMapping: Mapping[str, Sequence[str]]
    clientRequestToken: str

class DescribeAccountAuditConfigurationResponseTypeDef(BaseValidatorModel):
    roleArn: str
    auditNotificationTargetConfigurations: Dict[       Literal["SNS"], AuditNotificationTargetTypeDef]
    auditCheckConfigurations: Dict[str, AuditCheckConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountAuditConfigurationRequestRequestTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    auditNotificationTargetConfigurations: Optional[       Mapping[Literal["SNS"], AuditNotificationTargetTypeDef]] = None
    auditCheckConfigurations: Optional[Mapping[str, AuditCheckConfigurationTypeDef]] = None

class ListAuditTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[AuditTaskMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestAuthorizationRequestRequestTypeDef(BaseValidatorModel):
    authInfos: Sequence[AuthInfoTypeDef]
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    clientId: Optional[str] = None
    policyNamesToAdd: Optional[Sequence[str]] = None
    policyNamesToSkip: Optional[Sequence[str]] = None

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

class BehaviorCriteriaPaginatorTypeDef(BaseValidatorModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValuePaginatorTypeDef] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThresholdTypeDef] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfigTypeDef] = None

class BehaviorCriteriaTypeDef(BaseValidatorModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValueTypeDef] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThresholdTypeDef] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfigTypeDef] = None

class GetBehaviorModelTrainingSummariesResponseTypeDef(BaseValidatorModel):
    summaries: List[BehaviorModelTrainingSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class UpdateBillingGroupRequestRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    billingGroupProperties: BillingGroupPropertiesTypeDef
    expectedVersion: Optional[int] = None

class CodeSigningSignatureTypeDef(BaseValidatorModel):
    inlineDocument: Optional[BlobTypeDef] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificatesByCAResponseTypeDef(BaseValidatorModel):
    certificates: List[CertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificatesResponseTypeDef(BaseValidatorModel):
    certificates: List[CertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventConfigurationsResponseTypeDef(BaseValidatorModel):
    eventConfigurations: Dict[EventTypeType, ConfigurationTypeDef]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    eventConfigurations: Optional[Mapping[EventTypeType, ConfigurationTypeDef]] = None

class ListAuditMitigationActionsTasksRequestRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAuditTasksRequestRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectMitigationActionsExecutionsRequestRequestTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDetectMitigationActionsTasksRequestRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMetricValuesRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    metricName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListViolationEventsRequestRequestTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class CreateAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    authorizerName: str
    authorizerFunctionArn: str
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Mapping[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    signingDisabled: Optional[bool] = None
    enableCachingForHttp: Optional[bool] = None

class CreateBillingGroupRequestRequestTypeDef(BaseValidatorModel):
    billingGroupName: str
    billingGroupProperties: Optional[BillingGroupPropertiesTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateCertificateProviderRequestRequestTypeDef(BaseValidatorModel):
    certificateProviderName: str
    lambdaFunctionArn: str
    accountDefaultForOperations: Sequence[Literal["CreateCertificateFromCsr"]]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateCustomMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str
    metricType: CustomMetricTypeType
    clientRequestToken: str
    displayName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDimensionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: Literal["TOPIC_FILTER"]
    stringValues: Sequence[str]
    clientRequestToken: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateFleetMetricRequestRequestTypeDef(BaseValidatorModel):
    metricName: str
    queryString: str
    aggregationType: AggregationTypeTypeDef
    period: int
    aggregationField: str
    description: Optional[str] = None
    queryVersion: Optional[str] = None
    indexName: Optional[str] = None
    unit: Optional[FleetMetricUnitType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreatePolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyDocument: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRoleAliasRequestRequestTypeDef(BaseValidatorModel):
    roleAlias: str
    roleArn: str
    credentialDurationSeconds: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateScheduledAuditRequestRequestTypeDef(BaseValidatorModel):
    frequency: AuditFrequencyType
    targetCheckNames: Sequence[str]
    scheduledAuditName: str
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateDomainConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str
    domainName: Optional[str] = None
    serverCertificateArns: Optional[Sequence[str]] = None
    validationCertificateArn: Optional[str] = None
    authorizerConfig: Optional[AuthorizerConfigTypeDef] = None
    serviceType: Optional[ServiceTypeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None
    serverCertificateConfig: Optional[ServerCertificateConfigTypeDef] = None

class UpdateDomainConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domainConfigurationName: str
    authorizerConfig: Optional[AuthorizerConfigTypeDef] = None
    domainConfigurationStatus: Optional[DomainConfigurationStatusType] = None
    removeAuthorizerConfig: Optional[bool] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None
    serverCertificateConfig: Optional[ServerCertificateConfigTypeDef] = None

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

class CreateProvisioningTemplateRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    templateBody: str
    provisioningRoleArn: str
    description: Optional[str] = None
    enabled: Optional[bool] = None
    preProvisioningHook: Optional[ProvisioningHookTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    type: Optional[TemplateTypeType] = None

class DescribeProvisioningTemplateResponseTypeDef(BaseValidatorModel):
    templateArn: str
    templateName: str
    description: str
    creationDate: datetime
    lastModifiedDate: datetime
    defaultVersionId: int
    templateBody: str
    enabled: bool
    provisioningRoleArn: str
    preProvisioningHook: ProvisioningHookTypeDef
    type: TemplateTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProvisioningTemplateRequestRequestTypeDef(BaseValidatorModel):
    templateName: str
    description: Optional[str] = None
    enabled: Optional[bool] = None
    defaultVersionId: Optional[int] = None
    provisioningRoleArn: Optional[str] = None
    preProvisioningHook: Optional[ProvisioningHookTypeDef] = None
    removePreProvisioningHook: Optional[bool] = None

class CreateThingTypeRequestRequestTypeDef(BaseValidatorModel):
    thingTypeName: str
    thingTypeProperties: Optional[ThingTypePropertiesTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class DescribeAuditTaskResponseTypeDef(BaseValidatorModel):
    taskStatus: AuditTaskStatusType
    taskType: AuditTaskTypeType
    taskStartTime: datetime
    taskStatistics: TaskStatisticsTypeDef
    scheduledAuditName: str
    auditDetails: Dict[str, AuditCheckDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCACertificateRequestRequestTypeDef(BaseValidatorModel):
    caCertificate: str
    verificationCertificate: Optional[str] = None
    setAsActive: Optional[bool] = None
    allowAutoRegistration: Optional[bool] = None
    registrationConfig: Optional[RegistrationConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    certificateMode: Optional[CertificateModeType] = None

class UpdateCACertificateRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeThingTypeResponseTypeDef(BaseValidatorModel):
    thingTypeName: str
    thingTypeId: str
    thingTypeArn: str
    thingTypeProperties: ThingTypePropertiesTypeDef
    thingTypeMetadata: ThingTypeMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ThingTypeDefinitionTypeDef(BaseValidatorModel):
    thingTypeName: Optional[str] = None
    thingTypeArn: Optional[str] = None
    thingTypeProperties: Optional[ThingTypePropertiesTypeDef] = None
    thingTypeMetadata: Optional[ThingTypeMetadataTypeDef] = None

class DestinationTypeDef(BaseValidatorModel):
    s3Destination: Optional[S3DestinationTypeDef] = None

class ListDetectMitigationActionsExecutionsResponseTypeDef(BaseValidatorModel):
    actionsExecutions: List[DetectMitigationActionExecutionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDetectMitigationActionsTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str
    target: DetectMitigationActionsTaskTargetTypeDef
    actions: Sequence[str]
    clientRequestToken: str
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeTypeDef] = None
    includeOnlyActiveViolations: Optional[bool] = None
    includeSuppressedAlerts: Optional[bool] = None

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

class ThingGroupIndexingConfigurationTypeDef(BaseValidatorModel):
    thingGroupIndexingMode: ThingGroupIndexingModeType
    managedFields: Optional[List[FieldTypeDef]] = None
    customFields: Optional[List[FieldTypeDef]] = None

class StreamFileTypeDef(BaseValidatorModel):
    fileId: Optional[int] = None
    s3Location: Optional[S3LocationTypeDef] = None

class FileLocationTypeDef(BaseValidatorModel):
    stream: Optional[StreamTypeDef] = None
    s3Location: Optional[S3LocationTypeDef] = None

class ListFleetMetricsResponseTypeDef(BaseValidatorModel):
    fleetMetrics: List[FleetMetricNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IndexingFilterTypeDef(BaseValidatorModel):
    namedShadowNames: Optional[List[str]] = None
    geoLocations: Optional[List[GeoLocationTargetTypeDef]] = None

class ListActiveViolationsRequestListActiveViolationsPaginateTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef(BaseValidatorModel):
    target: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef(BaseValidatorModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditTasksRequestListAuditTasksPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuthorizersRequestListAuthorizersPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupsRequestListBillingGroupsPaginateTypeDef(BaseValidatorModel):
    namePrefixFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCACertificatesRequestListCACertificatesPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesByCARequestListCertificatesByCAPaginateTypeDef(BaseValidatorModel):
    caCertificateId: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesRequestListCertificatesPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomMetricsRequestListCustomMetricsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDetectMitigationActionsExecutionsRequestListDetectMitigationActionsExecutionsPaginateTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDimensionsRequestListDimensionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainConfigurationsRequestListDomainConfigurationsPaginateTypeDef(BaseValidatorModel):
    serviceType: Optional[ServiceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetMetricsRequestListFleetMetricsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndicesRequestListIndicesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef(BaseValidatorModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef(BaseValidatorModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    jobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobTemplatesRequestListJobTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseValidatorModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedJobTemplatesRequestListManagedJobTemplatesPaginateTypeDef(BaseValidatorModel):
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetricValuesRequestListMetricValuesPaginateTypeDef(BaseValidatorModel):
    thingName: str
    metricName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMitigationActionsRequestListMitigationActionsPaginateTypeDef(BaseValidatorModel):
    actionType: Optional[MitigationActionTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOTAUpdatesRequestListOTAUpdatesPaginateTypeDef(BaseValidatorModel):
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutgoingCertificatesRequestListOutgoingCertificatesPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionsRequestListPackageVersionsPaginateTypeDef(BaseValidatorModel):
    packageName: str
    status: Optional[PackageVersionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagesRequestListPackagesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesRequestListPoliciesPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef(BaseValidatorModel):
    policyName: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef(BaseValidatorModel):
    principal: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef(BaseValidatorModel):
    principal: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef(BaseValidatorModel):
    templateName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisioningTemplatesRequestListProvisioningTemplatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef(BaseValidatorModel):
    findingId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoleAliasesRequestListRoleAliasesPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduledAuditsRequestListScheduledAuditsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef(BaseValidatorModel):
    securityProfileTargetArn: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef(BaseValidatorModel):
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsRequestListStreamsPaginateTypeDef(BaseValidatorModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef(BaseValidatorModel):
    policyName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef(BaseValidatorModel):
    securityProfileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef(BaseValidatorModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingGroupsRequestListThingGroupsPaginateTypeDef(BaseValidatorModel):
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef(BaseValidatorModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef(BaseValidatorModel):
    taskId: str
    reportType: ReportTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingRegistrationTasksRequestListThingRegistrationTasksPaginateTypeDef(BaseValidatorModel):
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingTypesRequestListThingTypesPaginateTypeDef(BaseValidatorModel):
    thingTypeName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef(BaseValidatorModel):
    billingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef(BaseValidatorModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingsRequestListThingsPaginateTypeDef(BaseValidatorModel):
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    thingTypeName: Optional[str] = None
    usePrefixAttributeValue: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicRuleDestinationsRequestListTopicRuleDestinationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicRulesRequestListTopicRulesPaginateTypeDef(BaseValidatorModel):
    topic: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListV2LoggingLevelsRequestListV2LoggingLevelsPaginateTypeDef(BaseValidatorModel):
    targetType: Optional[LogTargetTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViolationEventsRequestListViolationEventsPaginateTypeDef(BaseValidatorModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetPackageConfigurationResponseTypeDef(BaseValidatorModel):
    versionUpdateByJobsConfig: VersionUpdateByJobsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageConfigurationRequestRequestTypeDef(BaseValidatorModel):
    versionUpdateByJobsConfig: Optional[VersionUpdateByJobsConfigTypeDef] = None
    clientToken: Optional[str] = None

class GetPercentilesResponseTypeDef(BaseValidatorModel):
    percentiles: List[PercentPairTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStatisticsResponseTypeDef(BaseValidatorModel):
    statistics: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBillingGroupsResponseTypeDef(BaseValidatorModel):
    billingGroups: List[GroupNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingGroupsForThingResponseTypeDef(BaseValidatorModel):
    thingGroups: List[GroupNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingGroupsResponseTypeDef(BaseValidatorModel):
    thingGroups: List[GroupNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class JobExecutionsRetryConfigTypeDef(BaseValidatorModel):
    criteriaList: Sequence[RetryCriteriaTypeDef]

class ListJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobTemplatesResponseTypeDef(BaseValidatorModel):
    jobTemplates: List[JobTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class KafkaActionTypeDef(BaseValidatorModel):
    destinationArn: str
    topic: str
    clientProperties: Mapping[str, str]
    key: Optional[str] = None
    partition: Optional[str] = None
    headers: Optional[Sequence[KafkaActionHeaderTypeDef]] = None

class ListManagedJobTemplatesResponseTypeDef(BaseValidatorModel):
    managedJobTemplates: List[ManagedJobTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMitigationActionsResponseTypeDef(BaseValidatorModel):
    actionIdentifiers: List[MitigationActionIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOTAUpdatesResponseTypeDef(BaseValidatorModel):
    otaUpdates: List[OTAUpdateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutgoingCertificatesResponseTypeDef(BaseValidatorModel):
    outgoingCertificates: List[OutgoingCertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageVersionsResponseTypeDef(BaseValidatorModel):
    packageVersionSummaries: List[PackageVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagesResponseTypeDef(BaseValidatorModel):
    packageSummaries: List[PackageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyVersionsResponseTypeDef(BaseValidatorModel):
    policyVersions: List[PolicyVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisioningTemplateVersionsResponseTypeDef(BaseValidatorModel):
    versions: List[ProvisioningTemplateVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisioningTemplatesResponseTypeDef(BaseValidatorModel):
    templates: List[ProvisioningTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListScheduledAuditsResponseTypeDef(BaseValidatorModel):
    scheduledAudits: List[ScheduledAuditMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityProfilesResponseTypeDef(BaseValidatorModel):
    securityProfileIdentifiers: List[SecurityProfileIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsResponseTypeDef(BaseValidatorModel):
    streams: List[StreamSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsForSecurityProfileResponseTypeDef(BaseValidatorModel):
    securityProfileTargets: List[SecurityProfileTargetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SecurityProfileTargetMappingTypeDef(BaseValidatorModel):
    securityProfileIdentifier: Optional[SecurityProfileIdentifierTypeDef] = None
    target: Optional[SecurityProfileTargetTypeDef] = None

class ListThingsResponseTypeDef(BaseValidatorModel):
    things: List[ThingAttributeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicRulesResponseTypeDef(BaseValidatorModel):
    rules: List[TopicRuleListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class SetV2LoggingLevelRequestRequestTypeDef(BaseValidatorModel):
    logTarget: LogTargetTypeDef
    logLevel: LogLevelType

class SetLoggingOptionsRequestRequestTypeDef(BaseValidatorModel):
    loggingOptionsPayload: LoggingOptionsPayloadTypeDef

class MitigationActionParamsPaginatorTypeDef(BaseValidatorModel):
    updateDeviceCertificateParams: Optional[UpdateDeviceCertificateParamsTypeDef] = None
    updateCACertificateParams: Optional[UpdateCACertificateParamsTypeDef] = None
    addThingsToThingGroupParams: Optional[AddThingsToThingGroupParamsPaginatorTypeDef] = None
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

class ThingTypeDefinitionPaginatorTypeDef(BaseValidatorModel):
    thingTypeName: Optional[str] = None
    thingTypeArn: Optional[str] = None
    thingTypeProperties: Optional[ThingTypePropertiesPaginatorTypeDef] = None
    thingTypeMetadata: Optional[ThingTypeMetadataTypeDef] = None

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

class ListMetricValuesResponsePaginatorTypeDef(BaseValidatorModel):
    metricDatumList: List[MetricDatumPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricValuesResponseTypeDef(BaseValidatorModel):
    metricDatumList: List[MetricDatumTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeniedTypeDef(BaseValidatorModel):
    implicitDeny: Optional[ImplicitDenyTypeDef] = None
    explicitDeny: Optional[ExplicitDenyTypeDef] = None

class PutAssetPropertyValueEntryTypeDef(BaseValidatorModel):
    propertyValues: Sequence[AssetPropertyValueTypeDef]
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None

class CreateDynamicThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    queryString: str
    thingGroupProperties: Optional[ThingGroupPropertiesTypeDef] = None
    indexName: Optional[str] = None
    queryVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    parentGroupName: Optional[str] = None
    thingGroupProperties: Optional[ThingGroupPropertiesTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateDynamicThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesTypeDef
    expectedVersion: Optional[int] = None
    indexName: Optional[str] = None
    queryString: Optional[str] = None
    queryVersion: Optional[str] = None

class UpdateThingGroupRequestRequestTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesTypeDef
    expectedVersion: Optional[int] = None

class AwsJobExecutionsRolloutConfigTypeDef(BaseValidatorModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[AwsJobExponentialRolloutRateTypeDef] = None

class BehaviorPaginatorTypeDef(BaseValidatorModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimensionTypeDef] = None
    criteria: Optional[BehaviorCriteriaPaginatorTypeDef] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None

class BehaviorTypeDef(BaseValidatorModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimensionTypeDef] = None
    criteria: Optional[BehaviorCriteriaTypeDef] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None

class CustomCodeSigningTypeDef(BaseValidatorModel):
    signature: Optional[CodeSigningSignatureTypeDef] = None
    certificateChain: Optional[CodeSigningCertificateChainTypeDef] = None
    hashAlgorithm: Optional[str] = None
    signatureAlgorithm: Optional[str] = None

class TestInvokeAuthorizerRequestRequestTypeDef(BaseValidatorModel):
    authorizerName: str
    token: Optional[str] = None
    tokenSignature: Optional[str] = None
    httpContext: Optional[HttpContextTypeDef] = None
    mqttContext: Optional[MqttContextTypeDef] = None
    tlsContext: Optional[TlsContextTypeDef] = None

class GetBucketsAggregationRequestRequestTypeDef(BaseValidatorModel):
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

class ListThingTypesResponseTypeDef(BaseValidatorModel):
    thingTypes: List[ThingTypeDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSigningJobParameterTypeDef(BaseValidatorModel):
    signingProfileParameter: Optional[SigningProfileParameterTypeDef] = None
    signingProfileName: Optional[str] = None
    destination: Optional[DestinationTypeDef] = None

class JobExecutionsRolloutConfigTypeDef(BaseValidatorModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[ExponentialRolloutRateTypeDef] = None

class CreateStreamRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateStreamRequestRequestTypeDef(BaseValidatorModel):
    streamId: str
    description: Optional[str] = None
    files: Optional[Sequence[StreamFileTypeDef]] = None
    roleArn: Optional[str] = None

class ThingIndexingConfigurationTypeDef(BaseValidatorModel):
    thingIndexingMode: ThingIndexingModeType
    thingConnectivityIndexingMode: Optional[ThingConnectivityIndexingModeType] = None
    deviceDefenderIndexingMode: Optional[DeviceDefenderIndexingModeType] = None
    namedShadowIndexingMode: Optional[NamedShadowIndexingModeType] = None
    managedFields: Optional[List[FieldTypeDef]] = None
    customFields: Optional[List[FieldTypeDef]] = None
    filter: Optional[IndexingFilterTypeDef] = None

class DescribeThingGroupResponseTypeDef(BaseValidatorModel):
    thingGroupName: str
    thingGroupId: str
    thingGroupArn: str
    version: int
    thingGroupProperties: ThingGroupPropertiesTypeDef
    thingGroupMetadata: ThingGroupMetadataTypeDef
    indexName: str
    queryString: str
    queryVersion: str
    status: DynamicGroupStatusType
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobExecutionsForThingResponseTypeDef(BaseValidatorModel):
    executionSummaries: List[JobExecutionSummaryForThingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityProfilesForTargetResponseTypeDef(BaseValidatorModel):
    securityProfileTargetMappings: List[SecurityProfileTargetMappingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListV2LoggingLevelsResponseTypeDef(BaseValidatorModel):
    logTargetConfigurations: List[LogTargetConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MitigationActionPaginatorTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsPaginatorTypeDef] = None

class CreateMitigationActionRequestRequestTypeDef(BaseValidatorModel):
    actionName: str
    roleArn: str
    actionParams: MitigationActionParamsTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class DescribeMitigationActionResponseTypeDef(BaseValidatorModel):
    actionName: str
    actionType: MitigationActionTypeType
    actionArn: str
    actionId: str
    roleArn: str
    actionParams: MitigationActionParamsTypeDef
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class MitigationActionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    id: Optional[str] = None
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsTypeDef] = None

class UpdateMitigationActionRequestRequestTypeDef(BaseValidatorModel):
    actionName: str
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsTypeDef] = None

class RepublishActionTypeDef(BaseValidatorModel):
    roleArn: str
    topic: str
    qos: Optional[int] = None
    headers: Optional[MqttHeadersTypeDef] = None

class AuditSuppressionTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: Optional[datetime] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None

class CreateAuditSuppressionRequestRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    clientRequestToken: str
    expirationDate: Optional[TimestampTypeDef] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None

class DeleteAuditSuppressionRequestRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef

class DescribeAuditSuppressionRequestRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef

class DescribeAuditSuppressionResponseTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: datetime
    suppressIndefinitely: bool
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAuditFindingsRequestListAuditFindingsPaginateTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    listSuppressedFindings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditFindingsRequestRequestTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    listSuppressedFindings: Optional[bool] = None

class ListAuditSuppressionsRequestListAuditSuppressionsPaginateTypeDef(BaseValidatorModel):
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditSuppressionsRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateAuditSuppressionRequestRequestTypeDef(BaseValidatorModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: Optional[TimestampTypeDef] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None

class SearchIndexResponseTypeDef(BaseValidatorModel):
    nextToken: str
    things: List[ThingDocumentTypeDef]
    thingGroups: List[ThingGroupDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingTypesResponsePaginatorTypeDef(BaseValidatorModel):
    thingTypes: List[ThingTypeDefinitionPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRuleDestinationRequestRequestTypeDef(BaseValidatorModel):
    destinationConfiguration: TopicRuleDestinationConfigurationTypeDef

class ListTopicRuleDestinationsResponseTypeDef(BaseValidatorModel):
    destinationSummaries: List[TopicRuleDestinationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRuleDestinationResponseTypeDef(BaseValidatorModel):
    topicRuleDestination: TopicRuleDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTopicRuleDestinationResponseTypeDef(BaseValidatorModel):
    topicRuleDestination: TopicRuleDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AuthResultTypeDef(BaseValidatorModel):
    authInfo: Optional[AuthInfoTypeDef] = None
    allowed: Optional[AllowedTypeDef] = None
    denied: Optional[DeniedTypeDef] = None
    authDecision: Optional[AuthDecisionType] = None
    missingContextValues: Optional[List[str]] = None

class IotSiteWiseActionTypeDef(BaseValidatorModel):
    putAssetPropertyValueEntries: Sequence[PutAssetPropertyValueEntryTypeDef]
    roleArn: str

class ActiveViolationPaginatorTypeDef(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorPaginatorTypeDef] = None
    lastViolationValue: Optional[MetricValuePaginatorTypeDef] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfoTypeDef] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    lastViolationTime: Optional[datetime] = None
    violationStartTime: Optional[datetime] = None

class ViolationEventPaginatorTypeDef(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorPaginatorTypeDef] = None
    metricValue: Optional[MetricValuePaginatorTypeDef] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfoTypeDef] = None
    violationEventType: Optional[ViolationEventTypeType] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    violationEventTime: Optional[datetime] = None

class ActiveViolationTypeDef(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorTypeDef] = None
    lastViolationValue: Optional[MetricValueTypeDef] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfoTypeDef] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    lastViolationTime: Optional[datetime] = None
    violationStartTime: Optional[datetime] = None

class CreateSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileDescription: Optional[str] = None
    behaviors: Optional[Sequence[BehaviorTypeDef]] = None
    alertTargets: Optional[Mapping[Literal["SNS"], AlertTargetTypeDef]] = None
    additionalMetricsToRetain: Optional[Sequence[str]] = None
    additionalMetricsToRetainV2: Optional[Sequence[MetricToRetainTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    metricsExportConfig: Optional[MetricsExportConfigTypeDef] = None

class DescribeSecurityProfileResponseTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List[BehaviorTypeDef]
    alertTargets: Dict[Literal["SNS"], AlertTargetTypeDef]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List[MetricToRetainTypeDef]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime
    metricsExportConfig: MetricsExportConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileDescription: Optional[str] = None
    behaviors: Optional[Sequence[BehaviorTypeDef]] = None
    alertTargets: Optional[Mapping[Literal["SNS"], AlertTargetTypeDef]] = None
    additionalMetricsToRetain: Optional[Sequence[str]] = None
    additionalMetricsToRetainV2: Optional[Sequence[MetricToRetainTypeDef]] = None
    deleteBehaviors: Optional[bool] = None
    deleteAlertTargets: Optional[bool] = None
    deleteAdditionalMetricsToRetain: Optional[bool] = None
    expectedVersion: Optional[int] = None
    metricsExportConfig: Optional[MetricsExportConfigTypeDef] = None
    deleteMetricsExportConfig: Optional[bool] = None

class UpdateSecurityProfileResponseTypeDef(BaseValidatorModel):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List[BehaviorTypeDef]
    alertTargets: Dict[Literal["SNS"], AlertTargetTypeDef]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List[MetricToRetainTypeDef]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime
    metricsExportConfig: MetricsExportConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateSecurityProfileBehaviorsRequestRequestTypeDef(BaseValidatorModel):
    behaviors: Sequence[BehaviorTypeDef]

class ViolationEventTypeDef(BaseValidatorModel):
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behavior: Optional[BehaviorTypeDef] = None
    metricValue: Optional[MetricValueTypeDef] = None
    violationEventAdditionalInfo: Optional[ViolationEventAdditionalInfoTypeDef] = None
    violationEventType: Optional[ViolationEventTypeType] = None
    verificationState: Optional[VerificationStateType] = None
    verificationStateDescription: Optional[str] = None
    violationEventTime: Optional[datetime] = None

class CodeSigningTypeDef(BaseValidatorModel):
    awsSignerJobId: Optional[str] = None
    startSigningJobParameter: Optional[StartSigningJobParameterTypeDef] = None
    customCodeSigning: Optional[CustomCodeSigningTypeDef] = None

class CreateJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    targets: Sequence[str]
    documentSource: Optional[str] = None
    document: Optional[str] = None
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    targetSelection: Optional[TargetSelectionType] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    namespaceId: Optional[str] = None
    jobTemplateArn: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigTypeDef] = None
    documentParameters: Optional[Mapping[str, str]] = None
    schedulingConfig: Optional[SchedulingConfigTypeDef] = None
    destinationPackageVersions: Optional[Sequence[str]] = None

class CreateJobTemplateRequestRequestTypeDef(BaseValidatorModel):
    jobTemplateId: str
    description: str
    jobArn: Optional[str] = None
    documentSource: Optional[str] = None
    document: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigTypeDef] = None
    maintenanceWindows: Optional[Sequence[MaintenanceWindowTypeDef]] = None
    destinationPackageVersions: Optional[Sequence[str]] = None

class DescribeJobTemplateResponseTypeDef(BaseValidatorModel):
    jobTemplateArn: str
    jobTemplateId: str
    description: str
    documentSource: str
    document: str
    createdAt: datetime
    presignedUrlConfig: PresignedUrlConfigTypeDef
    jobExecutionsRolloutConfig: JobExecutionsRolloutConfigTypeDef
    abortConfig: AbortConfigTypeDef
    timeoutConfig: TimeoutConfigTypeDef
    jobExecutionsRetryConfig: JobExecutionsRetryConfigTypeDef
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
    abortConfig: Optional[AbortConfigTypeDef] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    jobProcessDetails: Optional[JobProcessDetailsTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    namespaceId: Optional[str] = None
    jobTemplateArn: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigTypeDef] = None
    documentParameters: Optional[Dict[str, str]] = None
    isConcurrent: Optional[bool] = None
    schedulingConfig: Optional[SchedulingConfigTypeDef] = None
    scheduledJobRollouts: Optional[List[ScheduledJobRolloutTypeDef]] = None
    destinationPackageVersions: Optional[List[str]] = None

class UpdateJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    namespaceId: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigTypeDef] = None

class DescribeStreamResponseTypeDef(BaseValidatorModel):
    streamInfo: StreamInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIndexingConfigurationResponseTypeDef(BaseValidatorModel):
    thingIndexingConfiguration: ThingIndexingConfigurationTypeDef
    thingGroupIndexingConfiguration: ThingGroupIndexingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIndexingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    thingIndexingConfiguration: Optional[ThingIndexingConfigurationTypeDef] = None
    thingGroupIndexingConfiguration: Optional[ThingGroupIndexingConfigurationTypeDef] = None

class DetectMitigationActionsTaskSummaryPaginatorTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    taskStatus: Optional[DetectMitigationActionsTaskStatusType] = None
    taskStartTime: Optional[datetime] = None
    taskEndTime: Optional[datetime] = None
    target: Optional[DetectMitigationActionsTaskTargetTypeDef] = None
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeTypeDef] = None
    onlyActiveViolationsIncluded: Optional[bool] = None
    suppressedAlertsIncluded: Optional[bool] = None
    actionsDefinition: Optional[List[MitigationActionPaginatorTypeDef]] = None
    taskStatistics: Optional[DetectMitigationActionsTaskStatisticsTypeDef] = None

class DescribeAuditMitigationActionsTaskResponseTypeDef(BaseValidatorModel):
    taskStatus: AuditMitigationActionsTaskStatusType
    startTime: datetime
    endTime: datetime
    taskStatistics: Dict[str, TaskStatisticsForAuditCheckTypeDef]
    target: AuditMitigationActionsTaskTargetTypeDef
    auditCheckToActionsMapping: Dict[str, List[str]]
    actionsDefinition: List[MitigationActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectMitigationActionsTaskSummaryTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    taskStatus: Optional[DetectMitigationActionsTaskStatusType] = None
    taskStartTime: Optional[datetime] = None
    taskEndTime: Optional[datetime] = None
    target: Optional[DetectMitigationActionsTaskTargetTypeDef] = None
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeTypeDef] = None
    onlyActiveViolationsIncluded: Optional[bool] = None
    suppressedAlertsIncluded: Optional[bool] = None
    actionsDefinition: Optional[List[MitigationActionTypeDef]] = None
    taskStatistics: Optional[DetectMitigationActionsTaskStatisticsTypeDef] = None

class ListAuditSuppressionsResponseTypeDef(BaseValidatorModel):
    suppressions: List[AuditSuppressionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestAuthorizationResponseTypeDef(BaseValidatorModel):
    authResults: List[AuthResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ActionTypeDef(BaseValidatorModel):
    dynamoDB: Optional[DynamoDBActionTypeDef] = None
    dynamoDBv2: Optional[DynamoDBv2ActionTypeDef] = None
    _lambda: Optional[LambdaActionTypeDef] = None
    sns: Optional[SnsActionTypeDef] = None
    sqs: Optional[SqsActionTypeDef] = None
    kinesis: Optional[KinesisActionTypeDef] = None
    republish: Optional[RepublishActionTypeDef] = None
    s3: Optional[S3ActionTypeDef] = None
    firehose: Optional[FirehoseActionTypeDef] = None
    cloudwatchMetric: Optional[CloudwatchMetricActionTypeDef] = None
    cloudwatchAlarm: Optional[CloudwatchAlarmActionTypeDef] = None
    cloudwatchLogs: Optional[CloudwatchLogsActionTypeDef] = None
    elasticsearch: Optional[ElasticsearchActionTypeDef] = None
    salesforce: Optional[SalesforceActionTypeDef] = None
    iotAnalytics: Optional[IotAnalyticsActionTypeDef] = None
    iotEvents: Optional[IotEventsActionTypeDef] = None
    iotSiteWise: Optional[IotSiteWiseActionTypeDef] = None
    stepFunctions: Optional[StepFunctionsActionTypeDef] = None
    timestream: Optional[TimestreamActionTypeDef] = None
    http: Optional[HttpActionTypeDef] = None
    kafka: Optional[KafkaActionTypeDef] = None
    openSearch: Optional[OpenSearchActionTypeDef] = None
    location: Optional[LocationActionTypeDef] = None

class ListActiveViolationsResponsePaginatorTypeDef(BaseValidatorModel):
    activeViolations: List[ActiveViolationPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListViolationEventsResponsePaginatorTypeDef(BaseValidatorModel):
    violationEvents: List[ViolationEventPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListActiveViolationsResponseTypeDef(BaseValidatorModel):
    activeViolations: List[ActiveViolationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListViolationEventsResponseTypeDef(BaseValidatorModel):
    violationEvents: List[ViolationEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OTAUpdateFileTypeDef(BaseValidatorModel):
    fileName: Optional[str] = None
    fileType: Optional[int] = None
    fileVersion: Optional[str] = None
    fileLocation: Optional[FileLocationTypeDef] = None
    codeSigning: Optional[CodeSigningTypeDef] = None
    attributes: Optional[Mapping[str, str]] = None

class DescribeJobResponseTypeDef(BaseValidatorModel):
    documentSource: str
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectMitigationActionsTasksResponsePaginatorTypeDef(BaseValidatorModel):
    tasks: List[DetectMitigationActionsTaskSummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDetectMitigationActionsTaskResponseTypeDef(BaseValidatorModel):
    taskSummary: DetectMitigationActionsTaskSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectMitigationActionsTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[DetectMitigationActionsTaskSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAuditFindingResponseTypeDef(BaseValidatorModel):
    finding: AuditFindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAuditFindingsResponseTypeDef(BaseValidatorModel):
    findings: List[AuditFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TopicRulePayloadTypeDef(BaseValidatorModel):
    sql: str
    actions: Sequence[ActionTypeDef]
    description: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionTypeDef] = None

class TopicRuleTypeDef(BaseValidatorModel):
    ruleName: Optional[str] = None
    sql: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    actions: Optional[List[ActionTypeDef]] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionTypeDef] = None

class CreateOTAUpdateRequestRequestTypeDef(BaseValidatorModel):
    otaUpdateId: str
    targets: Sequence[str]
    files: Sequence[OTAUpdateFileTypeDef]
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
    otaUpdateFiles: Optional[List[OTAUpdateFileTypeDef]] = None
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None
    awsIotJobId: Optional[str] = None
    awsIotJobArn: Optional[str] = None
    errorInfo: Optional[ErrorInfoTypeDef] = None
    additionalParameters: Optional[Dict[str, str]] = None

class CreateTopicRuleRequestRequestTypeDef(BaseValidatorModel):
    ruleName: str
    topicRulePayload: TopicRulePayloadTypeDef
    tags: Optional[str] = None

class ReplaceTopicRuleRequestRequestTypeDef(BaseValidatorModel):
    ruleName: str
    topicRulePayload: TopicRulePayloadTypeDef

class GetTopicRuleResponseTypeDef(BaseValidatorModel):
    ruleArn: str
    rule: TopicRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOTAUpdateResponseTypeDef(BaseValidatorModel):
    otaUpdateInfo: OTAUpdateInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

