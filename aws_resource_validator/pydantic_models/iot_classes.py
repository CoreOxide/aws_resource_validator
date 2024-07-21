from datetime import datetime
from pydantic import BaseModel
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

class AbortCriteriaTypeDef(BaseModel):
    failureType: JobExecutionFailureTypeType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int

class AcceptCertificateTransferRequestRequestTypeDef(BaseModel):
    certificateId: str
    setAsActive: Optional[bool] = None

class CloudwatchAlarmActionTypeDef(BaseModel):
    roleArn: str
    alarmName: str
    stateReason: str
    stateValue: str

class CloudwatchLogsActionTypeDef(BaseModel):
    roleArn: str
    logGroupName: str
    batchMode: Optional[bool] = None

class CloudwatchMetricActionTypeDef(BaseModel):
    roleArn: str
    metricNamespace: str
    metricName: str
    metricValue: str
    metricUnit: str
    metricTimestamp: Optional[str] = None

class DynamoDBActionTypeDef(BaseModel):
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

class ElasticsearchActionTypeDef(BaseModel):
    roleArn: str
    endpoint: str
    index: str
    type: str
    id: str

class FirehoseActionTypeDef(BaseModel):
    roleArn: str
    deliveryStreamName: str
    separator: Optional[str] = None
    batchMode: Optional[bool] = None

class IotAnalyticsActionTypeDef(BaseModel):
    channelArn: Optional[str] = None
    channelName: Optional[str] = None
    batchMode: Optional[bool] = None
    roleArn: Optional[str] = None

class IotEventsActionTypeDef(BaseModel):
    inputName: str
    roleArn: str
    messageId: Optional[str] = None
    batchMode: Optional[bool] = None

class KinesisActionTypeDef(BaseModel):
    roleArn: str
    streamName: str
    partitionKey: Optional[str] = None

class LambdaActionTypeDef(BaseModel):
    functionArn: str

class OpenSearchActionTypeDef(BaseModel):
    roleArn: str
    endpoint: str
    index: str
    type: str
    id: str

class S3ActionTypeDef(BaseModel):
    roleArn: str
    bucketName: str
    key: str
    cannedAcl: Optional[CannedAccessControlListType] = None

class SalesforceActionTypeDef(BaseModel):
    token: str
    url: str

class SnsActionTypeDef(BaseModel):
    targetArn: str
    roleArn: str
    messageFormat: Optional[MessageFormatType] = None

class SqsActionTypeDef(BaseModel):
    roleArn: str
    queueUrl: str
    useBase64: Optional[bool] = None

class StepFunctionsActionTypeDef(BaseModel):
    stateMachineName: str
    roleArn: str
    executionNamePrefix: Optional[str] = None

class MetricValuePaginatorTypeDef(BaseModel):
    count: Optional[int] = None
    cidrs: Optional[List[str]] = None
    ports: Optional[List[int]] = None
    number: Optional[float] = None
    numbers: Optional[List[float]] = None
    strings: Optional[List[str]] = None

class ViolationEventAdditionalInfoTypeDef(BaseModel):
    confidenceLevel: Optional[ConfidenceLevelType] = None

class MetricValueTypeDef(BaseModel):
    count: Optional[int] = None
    cidrs: Optional[Sequence[str]] = None
    ports: Optional[Sequence[int]] = None
    number: Optional[float] = None
    numbers: Optional[Sequence[float]] = None
    strings: Optional[Sequence[str]] = None

class AddThingToBillingGroupRequestRequestTypeDef(BaseModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None

class AddThingToThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None
    overrideDynamicGroups: Optional[bool] = None

class AddThingsToThingGroupParamsPaginatorTypeDef(BaseModel):
    thingGroupNames: List[str]
    overrideDynamicGroups: Optional[bool] = None

class AddThingsToThingGroupParamsTypeDef(BaseModel):
    thingGroupNames: Sequence[str]
    overrideDynamicGroups: Optional[bool] = None

class AggregationTypeTypeDef(BaseModel):
    name: AggregationTypeNameType
    values: Optional[Sequence[str]] = None

class AlertTargetTypeDef(BaseModel):
    alertTargetArn: str
    roleArn: str

class PolicyTypeDef(BaseModel):
    policyName: Optional[str] = None
    policyArn: Optional[str] = None

class AssetPropertyTimestampTypeDef(BaseModel):
    timeInSeconds: str
    offsetInNanos: Optional[str] = None

class AssetPropertyVariantTypeDef(BaseModel):
    stringValue: Optional[str] = None
    integerValue: Optional[str] = None
    doubleValue: Optional[str] = None
    booleanValue: Optional[str] = None

class AssociateTargetsWithJobRequestRequestTypeDef(BaseModel):
    targets: Sequence[str]
    jobId: str
    comment: Optional[str] = None
    namespaceId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AttachPolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    target: str

class AttachPrincipalPolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    principal: str

class AttachSecurityProfileRequestRequestTypeDef(BaseModel):
    securityProfileName: str
    securityProfileTargetArn: str

class AttachThingPrincipalRequestRequestTypeDef(BaseModel):
    thingName: str
    principal: str

class AttributePayloadTypeDef(BaseModel):
    attributes: Optional[Mapping[str, str]] = None
    merge: Optional[bool] = None

class AuditCheckConfigurationTypeDef(BaseModel):
    enabled: Optional[bool] = None

class AuditCheckDetailsTypeDef(BaseModel):
    checkRunStatus: Optional[AuditCheckRunStatusType] = None
    checkCompliant: Optional[bool] = None
    totalResourcesCount: Optional[int] = None
    nonCompliantResourcesCount: Optional[int] = None
    suppressedNonCompliantResourcesCount: Optional[int] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None

class AuditMitigationActionExecutionMetadataTypeDef(BaseModel):
    taskId: Optional[str] = None
    findingId: Optional[str] = None
    actionName: Optional[str] = None
    actionId: Optional[str] = None
    status: Optional[AuditMitigationActionsExecutionStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None

class AuditMitigationActionsTaskMetadataTypeDef(BaseModel):
    taskId: Optional[str] = None
    startTime: Optional[datetime] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None

class AuditMitigationActionsTaskTargetTypeDef(BaseModel):
    auditTaskId: Optional[str] = None
    findingIds: Optional[List[str]] = None
    auditCheckToReasonCodeFilter: Optional[Dict[str, List[str]]] = None

class AuditNotificationTargetTypeDef(BaseModel):
    targetArn: Optional[str] = None
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None

class AuditTaskMetadataTypeDef(BaseModel):
    taskId: Optional[str] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    taskType: Optional[AuditTaskTypeType] = None

class AuthInfoTypeDef(BaseModel):
    resources: Sequence[str]
    actionType: Optional[ActionTypeType] = None

class AuthorizerConfigTypeDef(BaseModel):
    defaultAuthorizerName: Optional[str] = None
    allowAuthorizerOverride: Optional[bool] = None

class AuthorizerDescriptionTypeDef(BaseModel):
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

class AuthorizerSummaryTypeDef(BaseModel):
    authorizerName: Optional[str] = None
    authorizerArn: Optional[str] = None

class AwsJobAbortCriteriaTypeDef(BaseModel):
    failureType: AwsJobAbortCriteriaFailureTypeType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int

class AwsJobRateIncreaseCriteriaTypeDef(BaseModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None

class AwsJobPresignedUrlConfigTypeDef(BaseModel):
    expiresInSec: Optional[int] = None

class AwsJobTimeoutConfigTypeDef(BaseModel):
    inProgressTimeoutInMinutes: Optional[int] = None

class MachineLearningDetectionConfigTypeDef(BaseModel):
    confidenceLevel: ConfidenceLevelType

class StatisticalThresholdTypeDef(BaseModel):
    statistic: Optional[str] = None

class BehaviorModelTrainingSummaryTypeDef(BaseModel):
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None
    trainingDataCollectionStartDate: Optional[datetime] = None
    modelStatus: Optional[ModelStatusType] = None
    datapointsCollectionPercentage: Optional[float] = None
    lastModelRefreshDate: Optional[datetime] = None

class MetricDimensionTypeDef(BaseModel):
    dimensionName: str
    operator: Optional[DimensionValueOperatorType] = None

class BillingGroupMetadataTypeDef(BaseModel):
    creationDate: Optional[datetime] = None

class BillingGroupPropertiesTypeDef(BaseModel):
    billingGroupDescription: Optional[str] = None

class BucketTypeDef(BaseModel):
    keyValue: Optional[str] = None
    count: Optional[int] = None

class TermsAggregationTypeDef(BaseModel):
    maxBuckets: Optional[int] = None

class CertificateValidityTypeDef(BaseModel):
    notBefore: Optional[datetime] = None
    notAfter: Optional[datetime] = None

class CACertificateTypeDef(BaseModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    status: Optional[CACertificateStatusType] = None
    creationDate: Optional[datetime] = None

class CancelAuditMitigationActionsTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class CancelAuditTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class CancelCertificateTransferRequestRequestTypeDef(BaseModel):
    certificateId: str

class CancelDetectMitigationActionsTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class CancelJobExecutionRequestRequestTypeDef(BaseModel):
    jobId: str
    thingName: str
    force: Optional[bool] = None
    expectedVersion: Optional[int] = None
    statusDetails: Optional[Mapping[str, str]] = None

class CancelJobRequestRequestTypeDef(BaseModel):
    jobId: str
    reasonCode: Optional[str] = None
    comment: Optional[str] = None
    force: Optional[bool] = None

class TransferDataTypeDef(BaseModel):
    transferMessage: Optional[str] = None
    rejectReason: Optional[str] = None
    transferDate: Optional[datetime] = None
    acceptDate: Optional[datetime] = None
    rejectDate: Optional[datetime] = None

class CertificateProviderSummaryTypeDef(BaseModel):
    certificateProviderName: Optional[str] = None
    certificateProviderArn: Optional[str] = None

class CertificateTypeDef(BaseModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    status: Optional[CertificateStatusType] = None
    certificateMode: Optional[CertificateModeType] = None
    creationDate: Optional[datetime] = None

class CodeSigningCertificateChainTypeDef(BaseModel):
    certificateName: Optional[str] = None
    inlineDocument: Optional[str] = None

class ConfigurationTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class ConfirmTopicRuleDestinationRequestRequestTypeDef(BaseModel):
    confirmationToken: str

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class CreateCertificateFromCsrRequestRequestTypeDef(BaseModel):
    certificateSigningRequest: str
    setAsActive: Optional[bool] = None

class ServerCertificateConfigTypeDef(BaseModel):
    enableOCSPCheck: Optional[bool] = None

class TlsConfigTypeDef(BaseModel):
    securityPolicy: Optional[str] = None

class PresignedUrlConfigTypeDef(BaseModel):
    roleArn: Optional[str] = None
    expiresInSec: Optional[int] = None

class TimeoutConfigTypeDef(BaseModel):
    inProgressTimeoutInMinutes: Optional[int] = None

class MaintenanceWindowTypeDef(BaseModel):
    startTime: str
    durationInMinutes: int

class CreateKeysAndCertificateRequestRequestTypeDef(BaseModel):
    setAsActive: Optional[bool] = None

class KeyPairTypeDef(BaseModel):
    PublicKey: Optional[str] = None
    PrivateKey: Optional[str] = None

class CreatePackageRequestRequestTypeDef(BaseModel):
    packageName: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreatePackageVersionRequestRequestTypeDef(BaseModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class CreatePolicyVersionRequestRequestTypeDef(BaseModel):
    policyName: str
    policyDocument: str
    setAsDefault: Optional[bool] = None

class CreateProvisioningClaimRequestRequestTypeDef(BaseModel):
    templateName: str

class ProvisioningHookTypeDef(BaseModel):
    targetArn: str
    payloadVersion: Optional[str] = None

class CreateProvisioningTemplateVersionRequestRequestTypeDef(BaseModel):
    templateName: str
    templateBody: str
    setAsDefault: Optional[bool] = None

class MetricsExportConfigTypeDef(BaseModel):
    mqttTopic: str
    roleArn: str

class ThingTypePropertiesTypeDef(BaseModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[Sequence[str]] = None

class DeleteAccountAuditConfigurationRequestRequestTypeDef(BaseModel):
    deleteScheduledAudits: Optional[bool] = None

class DeleteAuthorizerRequestRequestTypeDef(BaseModel):
    authorizerName: str

class DeleteBillingGroupRequestRequestTypeDef(BaseModel):
    billingGroupName: str
    expectedVersion: Optional[int] = None

class DeleteCACertificateRequestRequestTypeDef(BaseModel):
    certificateId: str

class DeleteCertificateProviderRequestRequestTypeDef(BaseModel):
    certificateProviderName: str

class DeleteCertificateRequestRequestTypeDef(BaseModel):
    certificateId: str
    forceDelete: Optional[bool] = None

class DeleteCustomMetricRequestRequestTypeDef(BaseModel):
    metricName: str

class DeleteDimensionRequestRequestTypeDef(BaseModel):
    name: str

class DeleteDomainConfigurationRequestRequestTypeDef(BaseModel):
    domainConfigurationName: str

class DeleteDynamicThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None

class DeleteFleetMetricRequestRequestTypeDef(BaseModel):
    metricName: str
    expectedVersion: Optional[int] = None

class DeleteJobExecutionRequestRequestTypeDef(BaseModel):
    jobId: str
    thingName: str
    executionNumber: int
    force: Optional[bool] = None
    namespaceId: Optional[str] = None

class DeleteJobRequestRequestTypeDef(BaseModel):
    jobId: str
    force: Optional[bool] = None
    namespaceId: Optional[str] = None

class DeleteJobTemplateRequestRequestTypeDef(BaseModel):
    jobTemplateId: str

class DeleteMitigationActionRequestRequestTypeDef(BaseModel):
    actionName: str

class DeleteOTAUpdateRequestRequestTypeDef(BaseModel):
    otaUpdateId: str
    deleteStream: Optional[bool] = None
    forceDeleteAWSJob: Optional[bool] = None

class DeletePackageRequestRequestTypeDef(BaseModel):
    packageName: str
    clientToken: Optional[str] = None

class DeletePackageVersionRequestRequestTypeDef(BaseModel):
    packageName: str
    versionName: str
    clientToken: Optional[str] = None

class DeletePolicyRequestRequestTypeDef(BaseModel):
    policyName: str

class DeletePolicyVersionRequestRequestTypeDef(BaseModel):
    policyName: str
    policyVersionId: str

class DeleteProvisioningTemplateRequestRequestTypeDef(BaseModel):
    templateName: str

class DeleteProvisioningTemplateVersionRequestRequestTypeDef(BaseModel):
    templateName: str
    versionId: int

class DeleteRoleAliasRequestRequestTypeDef(BaseModel):
    roleAlias: str

class DeleteScheduledAuditRequestRequestTypeDef(BaseModel):
    scheduledAuditName: str

class DeleteSecurityProfileRequestRequestTypeDef(BaseModel):
    securityProfileName: str
    expectedVersion: Optional[int] = None

class DeleteStreamRequestRequestTypeDef(BaseModel):
    streamId: str

class DeleteThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str
    expectedVersion: Optional[int] = None

class DeleteThingRequestRequestTypeDef(BaseModel):
    thingName: str
    expectedVersion: Optional[int] = None

class DeleteThingTypeRequestRequestTypeDef(BaseModel):
    thingTypeName: str

class DeleteTopicRuleDestinationRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteTopicRuleRequestRequestTypeDef(BaseModel):
    ruleName: str

class DeleteV2LoggingLevelRequestRequestTypeDef(BaseModel):
    targetType: LogTargetTypeType
    targetName: str

class DeprecateThingTypeRequestRequestTypeDef(BaseModel):
    thingTypeName: str
    undoDeprecate: Optional[bool] = None

class DescribeAuditFindingRequestRequestTypeDef(BaseModel):
    findingId: str

class DescribeAuditMitigationActionsTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class TaskStatisticsForAuditCheckTypeDef(BaseModel):
    totalFindingsCount: Optional[int] = None
    failedFindingsCount: Optional[int] = None
    succeededFindingsCount: Optional[int] = None
    skippedFindingsCount: Optional[int] = None
    canceledFindingsCount: Optional[int] = None

class DescribeAuditTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class TaskStatisticsTypeDef(BaseModel):
    totalChecks: Optional[int] = None
    inProgressChecks: Optional[int] = None
    waitingForDataCollectionChecks: Optional[int] = None
    compliantChecks: Optional[int] = None
    nonCompliantChecks: Optional[int] = None
    failedChecks: Optional[int] = None
    canceledChecks: Optional[int] = None

class DescribeAuthorizerRequestRequestTypeDef(BaseModel):
    authorizerName: str

class DescribeBillingGroupRequestRequestTypeDef(BaseModel):
    billingGroupName: str

class DescribeCACertificateRequestRequestTypeDef(BaseModel):
    certificateId: str

class RegistrationConfigTypeDef(BaseModel):
    templateBody: Optional[str] = None
    roleArn: Optional[str] = None
    templateName: Optional[str] = None

class DescribeCertificateProviderRequestRequestTypeDef(BaseModel):
    certificateProviderName: str

class DescribeCertificateRequestRequestTypeDef(BaseModel):
    certificateId: str

class DescribeCustomMetricRequestRequestTypeDef(BaseModel):
    metricName: str

class DescribeDetectMitigationActionsTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class DescribeDimensionRequestRequestTypeDef(BaseModel):
    name: str

class DescribeDomainConfigurationRequestRequestTypeDef(BaseModel):
    domainConfigurationName: str

class ServerCertificateSummaryTypeDef(BaseModel):
    serverCertificateArn: Optional[str] = None
    serverCertificateStatus: Optional[ServerCertificateStatusType] = None
    serverCertificateStatusDetail: Optional[str] = None

class DescribeEndpointRequestRequestTypeDef(BaseModel):
    endpointType: Optional[str] = None

class DescribeFleetMetricRequestRequestTypeDef(BaseModel):
    metricName: str

class DescribeIndexRequestRequestTypeDef(BaseModel):
    indexName: str

class DescribeJobExecutionRequestRequestTypeDef(BaseModel):
    jobId: str
    thingName: str
    executionNumber: Optional[int] = None

class DescribeJobRequestRequestTypeDef(BaseModel):
    jobId: str

class DescribeJobTemplateRequestRequestTypeDef(BaseModel):
    jobTemplateId: str

class DescribeManagedJobTemplateRequestRequestTypeDef(BaseModel):
    templateName: str
    templateVersion: Optional[str] = None

class DocumentParameterTypeDef(BaseModel):
    key: Optional[str] = None
    description: Optional[str] = None
    regex: Optional[str] = None
    example: Optional[str] = None
    optional: Optional[bool] = None

class DescribeMitigationActionRequestRequestTypeDef(BaseModel):
    actionName: str

class DescribeProvisioningTemplateRequestRequestTypeDef(BaseModel):
    templateName: str

class DescribeProvisioningTemplateVersionRequestRequestTypeDef(BaseModel):
    templateName: str
    versionId: int

class DescribeRoleAliasRequestRequestTypeDef(BaseModel):
    roleAlias: str

class RoleAliasDescriptionTypeDef(BaseModel):
    roleAlias: Optional[str] = None
    roleAliasArn: Optional[str] = None
    roleArn: Optional[str] = None
    owner: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None

class DescribeScheduledAuditRequestRequestTypeDef(BaseModel):
    scheduledAuditName: str

class DescribeSecurityProfileRequestRequestTypeDef(BaseModel):
    securityProfileName: str

class DescribeStreamRequestRequestTypeDef(BaseModel):
    streamId: str

class DescribeThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str

class DescribeThingRegistrationTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class DescribeThingRequestRequestTypeDef(BaseModel):
    thingName: str

class DescribeThingTypeRequestRequestTypeDef(BaseModel):
    thingTypeName: str

class ThingTypeMetadataTypeDef(BaseModel):
    deprecated: Optional[bool] = None
    deprecationDate: Optional[datetime] = None
    creationDate: Optional[datetime] = None

class S3DestinationTypeDef(BaseModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None

class DetachPolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    target: str

class DetachPrincipalPolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    principal: str

class DetachSecurityProfileRequestRequestTypeDef(BaseModel):
    securityProfileName: str
    securityProfileTargetArn: str

class DetachThingPrincipalRequestRequestTypeDef(BaseModel):
    thingName: str
    principal: str

class DetectMitigationActionExecutionTypeDef(BaseModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    actionName: Optional[str] = None
    thingName: Optional[str] = None
    executionStartDate: Optional[datetime] = None
    executionEndDate: Optional[datetime] = None
    status: Optional[DetectMitigationActionExecutionStatusType] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None

class DetectMitigationActionsTaskStatisticsTypeDef(BaseModel):
    actionsExecuted: Optional[int] = None
    actionsSkipped: Optional[int] = None
    actionsFailed: Optional[int] = None

class DetectMitigationActionsTaskTargetTypeDef(BaseModel):
    violationIds: Optional[List[str]] = None
    securityProfileName: Optional[str] = None
    behaviorName: Optional[str] = None

class ViolationEventOccurrenceRangeTypeDef(BaseModel):
    startTime: datetime
    endTime: datetime

class DisableTopicRuleRequestRequestTypeDef(BaseModel):
    ruleName: str

class DomainConfigurationSummaryTypeDef(BaseModel):
    domainConfigurationName: Optional[str] = None
    domainConfigurationArn: Optional[str] = None
    serviceType: Optional[ServiceTypeType] = None

class PutItemInputTypeDef(BaseModel):
    tableName: str

class EffectivePolicyTypeDef(BaseModel):
    policyName: Optional[str] = None
    policyArn: Optional[str] = None
    policyDocument: Optional[str] = None

class EnableIoTLoggingParamsTypeDef(BaseModel):
    roleArnForLogging: str
    logLevel: LogLevelType

class EnableTopicRuleRequestRequestTypeDef(BaseModel):
    ruleName: str

class ErrorInfoTypeDef(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

class RateIncreaseCriteriaTypeDef(BaseModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None

class FieldTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[FieldTypeType] = None

class S3LocationTypeDef(BaseModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    version: Optional[str] = None

class StreamTypeDef(BaseModel):
    streamId: Optional[str] = None
    fileId: Optional[int] = None

class FleetMetricNameAndArnTypeDef(BaseModel):
    metricName: Optional[str] = None
    metricArn: Optional[str] = None

class GeoLocationTargetTypeDef(BaseModel):
    name: Optional[str] = None
    order: Optional[TargetFieldOrderType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetBehaviorModelTrainingSummariesRequestRequestTypeDef(BaseModel):
    securityProfileName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetCardinalityRequestRequestTypeDef(BaseModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None

class GetEffectivePoliciesRequestRequestTypeDef(BaseModel):
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    thingName: Optional[str] = None

class GetJobDocumentRequestRequestTypeDef(BaseModel):
    jobId: str

class GetOTAUpdateRequestRequestTypeDef(BaseModel):
    otaUpdateId: str

class VersionUpdateByJobsConfigTypeDef(BaseModel):
    enabled: Optional[bool] = None
    roleArn: Optional[str] = None

class GetPackageRequestRequestTypeDef(BaseModel):
    packageName: str

class GetPackageVersionRequestRequestTypeDef(BaseModel):
    packageName: str
    versionName: str

class GetPercentilesRequestRequestTypeDef(BaseModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None
    percents: Optional[Sequence[float]] = None

class PercentPairTypeDef(BaseModel):
    percent: Optional[float] = None
    value: Optional[float] = None

class GetPolicyRequestRequestTypeDef(BaseModel):
    policyName: str

class GetPolicyVersionRequestRequestTypeDef(BaseModel):
    policyName: str
    policyVersionId: str

class GetStatisticsRequestRequestTypeDef(BaseModel):
    queryString: str
    indexName: Optional[str] = None
    aggregationField: Optional[str] = None
    queryVersion: Optional[str] = None

class StatisticsTypeDef(BaseModel):
    count: Optional[int] = None
    average: Optional[float] = None
    sum: Optional[float] = None
    minimum: Optional[float] = None
    maximum: Optional[float] = None
    sumOfSquares: Optional[float] = None
    variance: Optional[float] = None
    stdDeviation: Optional[float] = None

class GetTopicRuleDestinationRequestRequestTypeDef(BaseModel):
    arn: str

class GetTopicRuleRequestRequestTypeDef(BaseModel):
    ruleName: str

class GroupNameAndArnTypeDef(BaseModel):
    groupName: Optional[str] = None
    groupArn: Optional[str] = None

class HttpActionHeaderTypeDef(BaseModel):
    key: str
    value: str

class SigV4AuthorizationTypeDef(BaseModel):
    signingRegion: str
    serviceName: str
    roleArn: str

class HttpContextTypeDef(BaseModel):
    headers: Optional[Mapping[str, str]] = None
    queryString: Optional[str] = None

class HttpUrlDestinationConfigurationTypeDef(BaseModel):
    confirmationUrl: str

class HttpUrlDestinationPropertiesTypeDef(BaseModel):
    confirmationUrl: Optional[str] = None

class HttpUrlDestinationSummaryTypeDef(BaseModel):
    confirmationUrl: Optional[str] = None

class IssuerCertificateIdentifierTypeDef(BaseModel):
    issuerCertificateSubject: Optional[str] = None
    issuerId: Optional[str] = None
    issuerCertificateSerialNumber: Optional[str] = None

class JobExecutionStatusDetailsTypeDef(BaseModel):
    detailsMap: Optional[Dict[str, str]] = None

class JobExecutionSummaryTypeDef(BaseModel):
    status: Optional[JobExecutionStatusType] = None
    queuedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    executionNumber: Optional[int] = None
    retryAttempt: Optional[int] = None

class RetryCriteriaTypeDef(BaseModel):
    failureType: RetryableFailureTypeType
    numberOfRetries: int

class JobProcessDetailsTypeDef(BaseModel):
    processingTargets: Optional[List[str]] = None
    numberOfCanceledThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None
    numberOfFailedThings: Optional[int] = None
    numberOfRejectedThings: Optional[int] = None
    numberOfQueuedThings: Optional[int] = None
    numberOfInProgressThings: Optional[int] = None
    numberOfRemovedThings: Optional[int] = None
    numberOfTimedOutThings: Optional[int] = None

class JobSummaryTypeDef(BaseModel):
    jobArn: Optional[str] = None
    jobId: Optional[str] = None
    thingGroupId: Optional[str] = None
    targetSelection: Optional[TargetSelectionType] = None
    status: Optional[JobStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    isConcurrent: Optional[bool] = None

class JobTemplateSummaryTypeDef(BaseModel):
    jobTemplateArn: Optional[str] = None
    jobTemplateId: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None

class ScheduledJobRolloutTypeDef(BaseModel):
    startTime: Optional[str] = None

class KafkaActionHeaderTypeDef(BaseModel):
    key: str
    value: str

class ListActiveViolationsRequestRequestTypeDef(BaseModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAttachedPoliciesRequestRequestTypeDef(BaseModel):
    target: str
    recursive: Optional[bool] = None
    marker: Optional[str] = None
    pageSize: Optional[int] = None

class ListAuditMitigationActionsExecutionsRequestRequestTypeDef(BaseModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAuthorizersRequestRequestTypeDef(BaseModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None

class ListBillingGroupsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    namePrefixFilter: Optional[str] = None

class ListCACertificatesRequestRequestTypeDef(BaseModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None

class ListCertificateProvidersRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListCertificatesByCARequestRequestTypeDef(BaseModel):
    caCertificateId: str
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListCertificatesRequestRequestTypeDef(BaseModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListCustomMetricsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDimensionsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDomainConfigurationsRequestRequestTypeDef(BaseModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    serviceType: Optional[ServiceTypeType] = None

class ListFleetMetricsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListIndicesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListJobExecutionsForJobRequestRequestTypeDef(BaseModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobExecutionsForThingRequestRequestTypeDef(BaseModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    jobId: Optional[str] = None

class ListJobTemplatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None

class ListManagedJobTemplatesRequestRequestTypeDef(BaseModel):
    templateName: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ManagedJobTemplateSummaryTypeDef(BaseModel):
    templateArn: Optional[str] = None
    templateName: Optional[str] = None
    description: Optional[str] = None
    environments: Optional[List[str]] = None
    templateVersion: Optional[str] = None

class ListMitigationActionsRequestRequestTypeDef(BaseModel):
    actionType: Optional[MitigationActionTypeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MitigationActionIdentifierTypeDef(BaseModel):
    actionName: Optional[str] = None
    actionArn: Optional[str] = None
    creationDate: Optional[datetime] = None

class ListOTAUpdatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None

class OTAUpdateSummaryTypeDef(BaseModel):
    otaUpdateId: Optional[str] = None
    otaUpdateArn: Optional[str] = None
    creationDate: Optional[datetime] = None

class ListOutgoingCertificatesRequestRequestTypeDef(BaseModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class OutgoingCertificateTypeDef(BaseModel):
    certificateArn: Optional[str] = None
    certificateId: Optional[str] = None
    transferredTo: Optional[str] = None
    transferDate: Optional[datetime] = None
    transferMessage: Optional[str] = None
    creationDate: Optional[datetime] = None

class ListPackageVersionsRequestRequestTypeDef(BaseModel):
    packageName: str
    status: Optional[PackageVersionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PackageVersionSummaryTypeDef(BaseModel):
    packageName: Optional[str] = None
    versionName: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None

class ListPackagesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PackageSummaryTypeDef(BaseModel):
    packageName: Optional[str] = None
    defaultVersionName: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None

class ListPoliciesRequestRequestTypeDef(BaseModel):
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None

class ListPolicyPrincipalsRequestRequestTypeDef(BaseModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None

class ListPolicyVersionsRequestRequestTypeDef(BaseModel):
    policyName: str

class PolicyVersionTypeDef(BaseModel):
    versionId: Optional[str] = None
    isDefaultVersion: Optional[bool] = None
    createDate: Optional[datetime] = None

class ListPrincipalPoliciesRequestRequestTypeDef(BaseModel):
    principal: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None
    ascendingOrder: Optional[bool] = None

class ListPrincipalThingsRequestRequestTypeDef(BaseModel):
    principal: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListProvisioningTemplateVersionsRequestRequestTypeDef(BaseModel):
    templateName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ProvisioningTemplateVersionSummaryTypeDef(BaseModel):
    versionId: Optional[int] = None
    creationDate: Optional[datetime] = None
    isDefaultVersion: Optional[bool] = None

class ListProvisioningTemplatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ProvisioningTemplateSummaryTypeDef(BaseModel):
    templateArn: Optional[str] = None
    templateName: Optional[str] = None
    description: Optional[str] = None
    creationDate: Optional[datetime] = None
    lastModifiedDate: Optional[datetime] = None
    enabled: Optional[bool] = None
    type: Optional[TemplateTypeType] = None

class ListRelatedResourcesForAuditFindingRequestRequestTypeDef(BaseModel):
    findingId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListRoleAliasesRequestRequestTypeDef(BaseModel):
    pageSize: Optional[int] = None
    marker: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class ListScheduledAuditsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ScheduledAuditMetadataTypeDef(BaseModel):
    scheduledAuditName: Optional[str] = None
    scheduledAuditArn: Optional[str] = None
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None

class ListSecurityProfilesForTargetRequestRequestTypeDef(BaseModel):
    securityProfileTargetArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    recursive: Optional[bool] = None

class ListSecurityProfilesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None

class SecurityProfileIdentifierTypeDef(BaseModel):
    name: str
    arn: str

class ListStreamsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ascendingOrder: Optional[bool] = None

class StreamSummaryTypeDef(BaseModel):
    streamId: Optional[str] = None
    streamArn: Optional[str] = None
    streamVersion: Optional[int] = None
    description: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    nextToken: Optional[str] = None

class ListTargetsForPolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    marker: Optional[str] = None
    pageSize: Optional[int] = None

class ListTargetsForSecurityProfileRequestRequestTypeDef(BaseModel):
    securityProfileName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SecurityProfileTargetTypeDef(BaseModel):
    arn: str

class ListThingGroupsForThingRequestRequestTypeDef(BaseModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingGroupsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None

class ListThingPrincipalsRequestRequestTypeDef(BaseModel):
    thingName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingRegistrationTaskReportsRequestRequestTypeDef(BaseModel):
    taskId: str
    reportType: ReportTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingRegistrationTasksRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[StatusType] = None

class ListThingTypesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    thingTypeName: Optional[str] = None

class ListThingsInBillingGroupRequestRequestTypeDef(BaseModel):
    billingGroupName: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingsInThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListThingsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    thingTypeName: Optional[str] = None
    usePrefixAttributeValue: Optional[bool] = None

class ThingAttributeTypeDef(BaseModel):
    thingName: Optional[str] = None
    thingTypeName: Optional[str] = None
    thingArn: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    version: Optional[int] = None

class ListTopicRuleDestinationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTopicRulesRequestRequestTypeDef(BaseModel):
    topic: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    ruleDisabled: Optional[bool] = None

class TopicRuleListItemTypeDef(BaseModel):
    ruleArn: Optional[str] = None
    ruleName: Optional[str] = None
    topicPattern: Optional[str] = None
    createdAt: Optional[datetime] = None
    ruleDisabled: Optional[bool] = None

class ListV2LoggingLevelsRequestRequestTypeDef(BaseModel):
    targetType: Optional[LogTargetTypeType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LocationTimestampTypeDef(BaseModel):
    value: str
    unit: Optional[str] = None

class LogTargetTypeDef(BaseModel):
    targetType: LogTargetTypeType
    targetName: Optional[str] = None

class LoggingOptionsPayloadTypeDef(BaseModel):
    roleArn: str
    logLevel: Optional[LogLevelType] = None

class PublishFindingToSnsParamsTypeDef(BaseModel):
    topicArn: str

class ReplaceDefaultPolicyVersionParamsTypeDef(BaseModel):
    templateName: Literal["BLANK_POLICY"]

class UpdateCACertificateParamsTypeDef(BaseModel):
    action: Literal["DEACTIVATE"]

class UpdateDeviceCertificateParamsTypeDef(BaseModel):
    action: Literal["DEACTIVATE"]

class UserPropertyTypeDef(BaseModel):
    key: str
    value: str

class PolicyVersionIdentifierTypeDef(BaseModel):
    policyName: Optional[str] = None
    policyVersionId: Optional[str] = None

class PutVerificationStateOnViolationRequestRequestTypeDef(BaseModel):
    violationId: str
    verificationState: VerificationStateType
    verificationStateDescription: Optional[str] = None

class RegisterCertificateRequestRequestTypeDef(BaseModel):
    certificatePem: str
    caCertificatePem: Optional[str] = None
    setAsActive: Optional[bool] = None
    status: Optional[CertificateStatusType] = None

class RegisterCertificateWithoutCARequestRequestTypeDef(BaseModel):
    certificatePem: str
    status: Optional[CertificateStatusType] = None

class RegisterThingRequestRequestTypeDef(BaseModel):
    templateBody: str
    parameters: Optional[Mapping[str, str]] = None

class RejectCertificateTransferRequestRequestTypeDef(BaseModel):
    certificateId: str
    rejectReason: Optional[str] = None

class RemoveThingFromBillingGroupRequestRequestTypeDef(BaseModel):
    billingGroupName: Optional[str] = None
    billingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None

class RemoveThingFromThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: Optional[str] = None
    thingGroupArn: Optional[str] = None
    thingName: Optional[str] = None
    thingArn: Optional[str] = None

class SearchIndexRequestRequestTypeDef(BaseModel):
    queryString: str
    indexName: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    queryVersion: Optional[str] = None

class ThingGroupDocumentTypeDef(BaseModel):
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    thingGroupDescription: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    parentGroupNames: Optional[List[str]] = None

class SetDefaultAuthorizerRequestRequestTypeDef(BaseModel):
    authorizerName: str

class SetDefaultPolicyVersionRequestRequestTypeDef(BaseModel):
    policyName: str
    policyVersionId: str

class SetV2LoggingOptionsRequestRequestTypeDef(BaseModel):
    roleArn: Optional[str] = None
    defaultLogLevel: Optional[LogLevelType] = None
    disableAllLogs: Optional[bool] = None

class SigningProfileParameterTypeDef(BaseModel):
    certificateArn: Optional[str] = None
    platform: Optional[str] = None
    certificatePathOnDevice: Optional[str] = None

class StartOnDemandAuditTaskRequestRequestTypeDef(BaseModel):
    targetCheckNames: Sequence[str]

class StartThingRegistrationTaskRequestRequestTypeDef(BaseModel):
    templateBody: str
    inputFileBucket: str
    inputFileKey: str
    roleArn: str

class StopThingRegistrationTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class TlsContextTypeDef(BaseModel):
    serverName: Optional[str] = None

class ThingConnectivityTypeDef(BaseModel):
    connected: Optional[bool] = None
    timestamp: Optional[int] = None
    disconnectReason: Optional[str] = None

class ThingTypePropertiesPaginatorTypeDef(BaseModel):
    thingTypeDescription: Optional[str] = None
    searchableAttributes: Optional[List[str]] = None

class TimestreamDimensionTypeDef(BaseModel):
    name: str
    value: str

class TimestreamTimestampTypeDef(BaseModel):
    value: str
    unit: str

class VpcDestinationConfigurationTypeDef(BaseModel):
    subnetIds: Sequence[str]
    vpcId: str
    roleArn: str
    securityGroups: Optional[Sequence[str]] = None

class VpcDestinationSummaryTypeDef(BaseModel):
    subnetIds: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    roleArn: Optional[str] = None

class VpcDestinationPropertiesTypeDef(BaseModel):
    subnetIds: Optional[List[str]] = None
    securityGroups: Optional[List[str]] = None
    vpcId: Optional[str] = None
    roleArn: Optional[str] = None

class TransferCertificateRequestRequestTypeDef(BaseModel):
    certificateId: str
    targetAwsAccount: str
    transferMessage: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAuthorizerRequestRequestTypeDef(BaseModel):
    authorizerName: str
    authorizerFunctionArn: Optional[str] = None
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Mapping[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    enableCachingForHttp: Optional[bool] = None

class UpdateCertificateProviderRequestRequestTypeDef(BaseModel):
    certificateProviderName: str
    lambdaFunctionArn: Optional[str] = None
    accountDefaultForOperations: Optional[Sequence[Literal["CreateCertificateFromCsr"]]] = None

class UpdateCertificateRequestRequestTypeDef(BaseModel):
    certificateId: str
    newStatus: CertificateStatusType

class UpdateCustomMetricRequestRequestTypeDef(BaseModel):
    metricName: str
    displayName: str

class UpdateDimensionRequestRequestTypeDef(BaseModel):
    name: str
    stringValues: Sequence[str]

class UpdatePackageRequestRequestTypeDef(BaseModel):
    packageName: str
    description: Optional[str] = None
    defaultVersionName: Optional[str] = None
    unsetDefaultVersion: Optional[bool] = None
    clientToken: Optional[str] = None

class UpdatePackageVersionRequestRequestTypeDef(BaseModel):
    packageName: str
    versionName: str
    description: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    action: Optional[PackageVersionActionType] = None
    clientToken: Optional[str] = None

class UpdateRoleAliasRequestRequestTypeDef(BaseModel):
    roleAlias: str
    roleArn: Optional[str] = None
    credentialDurationSeconds: Optional[int] = None

class UpdateScheduledAuditRequestRequestTypeDef(BaseModel):
    scheduledAuditName: str
    frequency: Optional[AuditFrequencyType] = None
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    targetCheckNames: Optional[Sequence[str]] = None

class UpdateThingGroupsForThingRequestRequestTypeDef(BaseModel):
    thingName: Optional[str] = None
    thingGroupsToAdd: Optional[Sequence[str]] = None
    thingGroupsToRemove: Optional[Sequence[str]] = None
    overrideDynamicGroups: Optional[bool] = None

class UpdateTopicRuleDestinationRequestRequestTypeDef(BaseModel):
    arn: str
    status: TopicRuleDestinationStatusType

class ValidationErrorTypeDef(BaseModel):
    errorMessage: Optional[str] = None

class AbortConfigTypeDef(BaseModel):
    criteriaList: Sequence[AbortCriteriaTypeDef]

class MetricDatumPaginatorTypeDef(BaseModel):
    timestamp: Optional[datetime] = None
    value: Optional[MetricValuePaginatorTypeDef] = None

class MetricDatumTypeDef(BaseModel):
    timestamp: Optional[datetime] = None
    value: Optional[MetricValueTypeDef] = None

class UpdateFleetMetricRequestRequestTypeDef(BaseModel):
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

class AllowedTypeDef(BaseModel):
    policies: Optional[List[PolicyTypeDef]] = None

class ExplicitDenyTypeDef(BaseModel):
    policies: Optional[List[PolicyTypeDef]] = None

class ImplicitDenyTypeDef(BaseModel):
    policies: Optional[List[PolicyTypeDef]] = None

class AssetPropertyValueTypeDef(BaseModel):
    value: AssetPropertyVariantTypeDef
    timestamp: AssetPropertyTimestampTypeDef
    quality: Optional[str] = None

class AssociateTargetsWithJobResponseTypeDef(BaseModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelJobResponseTypeDef(BaseModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAuthorizerResponseTypeDef(BaseModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBillingGroupResponseTypeDef(BaseModel):
    billingGroupName: str
    billingGroupArn: str
    billingGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCertificateFromCsrResponseTypeDef(BaseModel):
    certificateArn: str
    certificateId: str
    certificatePem: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCertificateProviderResponseTypeDef(BaseModel):
    certificateProviderName: str
    certificateProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomMetricResponseTypeDef(BaseModel):
    metricName: str
    metricArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDimensionResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainConfigurationResponseTypeDef(BaseModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDynamicThingGroupResponseTypeDef(BaseModel):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str
    indexName: str
    queryString: str
    queryVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetMetricResponseTypeDef(BaseModel):
    metricName: str
    metricArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResponseTypeDef(BaseModel):
    jobArn: str
    jobId: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobTemplateResponseTypeDef(BaseModel):
    jobTemplateArn: str
    jobTemplateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMitigationActionResponseTypeDef(BaseModel):
    actionArn: str
    actionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOTAUpdateResponseTypeDef(BaseModel):
    otaUpdateId: str
    awsIotJobId: str
    otaUpdateArn: str
    awsIotJobArn: str
    otaUpdateStatus: OTAUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageResponseTypeDef(BaseModel):
    packageName: str
    packageArn: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageVersionResponseTypeDef(BaseModel):
    packageVersionArn: str
    packageName: str
    versionName: str
    description: str
    attributes: Dict[str, str]
    status: PackageVersionStatusType
    errorReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyResponseTypeDef(BaseModel):
    policyName: str
    policyArn: str
    policyDocument: str
    policyVersionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyVersionResponseTypeDef(BaseModel):
    policyArn: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisioningTemplateResponseTypeDef(BaseModel):
    templateArn: str
    templateName: str
    defaultVersionId: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisioningTemplateVersionResponseTypeDef(BaseModel):
    templateArn: str
    templateName: str
    versionId: int
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoleAliasResponseTypeDef(BaseModel):
    roleAlias: str
    roleAliasArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledAuditResponseTypeDef(BaseModel):
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityProfileResponseTypeDef(BaseModel):
    securityProfileName: str
    securityProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamResponseTypeDef(BaseModel):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThingGroupResponseTypeDef(BaseModel):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThingResponseTypeDef(BaseModel):
    thingName: str
    thingArn: str
    thingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThingTypeResponseTypeDef(BaseModel):
    thingTypeName: str
    thingTypeArn: str
    thingTypeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateProviderResponseTypeDef(BaseModel):
    certificateProviderName: str
    certificateProviderArn: str
    lambdaFunctionArn: str
    accountDefaultForOperations: List[Literal["CreateCertificateFromCsr"]]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomMetricResponseTypeDef(BaseModel):
    metricName: str
    metricArn: str
    metricType: CustomMetricTypeType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDimensionResponseTypeDef(BaseModel):
    name: str
    arn: str
    type: Literal["TOPIC_FILTER"]
    stringValues: List[str]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointResponseTypeDef(BaseModel):
    endpointAddress: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetMetricResponseTypeDef(BaseModel):
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

class DescribeIndexResponseTypeDef(BaseModel):
    indexName: str
    indexStatus: IndexStatusType
    schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProvisioningTemplateVersionResponseTypeDef(BaseModel):
    versionId: int
    creationDate: datetime
    templateBody: str
    isDefaultVersion: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScheduledAuditResponseTypeDef(BaseModel):
    frequency: AuditFrequencyType
    dayOfMonth: str
    dayOfWeek: DayOfWeekType
    targetCheckNames: List[str]
    scheduledAuditName: str
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThingRegistrationTaskResponseTypeDef(BaseModel):
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

class DescribeThingResponseTypeDef(BaseModel):
    defaultClientId: str
    thingName: str
    thingId: str
    thingArn: str
    thingTypeName: str
    attributes: Dict[str, str]
    version: int
    billingGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCardinalityResponseTypeDef(BaseModel):
    cardinality: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobDocumentResponseTypeDef(BaseModel):
    document: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoggingOptionsResponseTypeDef(BaseModel):
    roleArn: str
    logLevel: LogLevelType
    ResponseMetadata: ResponseMetadataTypeDef

class GetPackageResponseTypeDef(BaseModel):
    packageName: str
    packageArn: str
    description: str
    defaultVersionName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPackageVersionResponseTypeDef(BaseModel):
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

class GetPolicyResponseTypeDef(BaseModel):
    policyName: str
    policyArn: str
    policyDocument: str
    defaultVersionId: str
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyVersionResponseTypeDef(BaseModel):
    policyArn: str
    policyName: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegistrationCodeResponseTypeDef(BaseModel):
    registrationCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetV2LoggingOptionsResponseTypeDef(BaseModel):
    roleArn: str
    defaultLogLevel: LogLevelType
    disableAllLogs: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachedPoliciesResponseTypeDef(BaseModel):
    policies: List[PolicyTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomMetricsResponseTypeDef(BaseModel):
    metricNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDimensionsResponseTypeDef(BaseModel):
    dimensionNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndicesResponseTypeDef(BaseModel):
    indexNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoliciesResponseTypeDef(BaseModel):
    policies: List[PolicyTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyPrincipalsResponseTypeDef(BaseModel):
    principals: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrincipalPoliciesResponseTypeDef(BaseModel):
    policies: List[PolicyTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrincipalThingsResponseTypeDef(BaseModel):
    things: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoleAliasesResponseTypeDef(BaseModel):
    roleAliases: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsForPolicyResponseTypeDef(BaseModel):
    targets: List[str]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingPrincipalsResponseTypeDef(BaseModel):
    principals: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingRegistrationTaskReportsResponseTypeDef(BaseModel):
    resourceLinks: List[str]
    reportType: ReportTypeType
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingRegistrationTasksResponseTypeDef(BaseModel):
    taskIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingsInBillingGroupResponseTypeDef(BaseModel):
    things: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingsInThingGroupResponseTypeDef(BaseModel):
    things: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCACertificateResponseTypeDef(BaseModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCertificateResponseTypeDef(BaseModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCertificateWithoutCAResponseTypeDef(BaseModel):
    certificateArn: str
    certificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterThingResponseTypeDef(BaseModel):
    certificatePem: str
    resourceArns: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultAuthorizerResponseTypeDef(BaseModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAuditMitigationActionsTaskResponseTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDetectMitigationActionsTaskResponseTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOnDemandAuditTaskResponseTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartThingRegistrationTaskResponseTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestInvokeAuthorizerResponseTypeDef(BaseModel):
    isAuthenticated: bool
    principalId: str
    policyDocuments: List[str]
    refreshAfterInSeconds: int
    disconnectAfterInSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class TransferCertificateResponseTypeDef(BaseModel):
    transferredCertificateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAuthorizerResponseTypeDef(BaseModel):
    authorizerName: str
    authorizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBillingGroupResponseTypeDef(BaseModel):
    version: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCertificateProviderResponseTypeDef(BaseModel):
    certificateProviderName: str
    certificateProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCustomMetricResponseTypeDef(BaseModel):
    metricName: str
    metricArn: str
    metricType: CustomMetricTypeType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDimensionResponseTypeDef(BaseModel):
    name: str
    arn: str
    type: Literal["TOPIC_FILTER"]
    stringValues: List[str]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainConfigurationResponseTypeDef(BaseModel):
    domainConfigurationName: str
    domainConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDynamicThingGroupResponseTypeDef(BaseModel):
    version: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMitigationActionResponseTypeDef(BaseModel):
    actionArn: str
    actionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoleAliasResponseTypeDef(BaseModel):
    roleAlias: str
    roleAliasArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScheduledAuditResponseTypeDef(BaseModel):
    scheduledAuditArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStreamResponseTypeDef(BaseModel):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateThingGroupResponseTypeDef(BaseModel):
    version: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateThingRequestRequestTypeDef(BaseModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadTypeDef] = None
    billingGroupName: Optional[str] = None

class ThingGroupPropertiesTypeDef(BaseModel):
    thingGroupDescription: Optional[str] = None
    attributePayload: Optional[AttributePayloadTypeDef] = None

class UpdateThingRequestRequestTypeDef(BaseModel):
    thingName: str
    thingTypeName: Optional[str] = None
    attributePayload: Optional[AttributePayloadTypeDef] = None
    expectedVersion: Optional[int] = None
    removeThingType: Optional[bool] = None

class ListAuditMitigationActionsExecutionsResponseTypeDef(BaseModel):
    actionsExecutions: List[AuditMitigationActionExecutionMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAuditMitigationActionsTasksResponseTypeDef(BaseModel):
    tasks: List[AuditMitigationActionsTaskMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAuditMitigationActionsTaskRequestRequestTypeDef(BaseModel):
    taskId: str
    target: AuditMitigationActionsTaskTargetTypeDef
    auditCheckToActionsMapping: Mapping[str, Sequence[str]]
    clientRequestToken: str

class DescribeAccountAuditConfigurationResponseTypeDef(BaseModel):
    roleArn: str
    auditNotificationTargetConfigurations: Dict[       Literal["SNS"], AuditNotificationTargetTypeDef
    auditCheckConfigurations: Dict[str, AuditCheckConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountAuditConfigurationRequestRequestTypeDef(BaseModel):
    roleArn: Optional[str] = None
    auditNotificationTargetConfigurations: Optional[       Mapping[Literal["SNS"], AuditNotificationTargetTypeDef] = None
    auditCheckConfigurations: Optional[Mapping[str, AuditCheckConfigurationTypeDef]] = None

class ListAuditTasksResponseTypeDef(BaseModel):
    tasks: List[AuditTaskMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestAuthorizationRequestRequestTypeDef(BaseModel):
    authInfos: Sequence[AuthInfoTypeDef]
    principal: Optional[str] = None
    cognitoIdentityPoolId: Optional[str] = None
    clientId: Optional[str] = None
    policyNamesToAdd: Optional[Sequence[str]] = None
    policyNamesToSkip: Optional[Sequence[str]] = None

class DescribeAuthorizerResponseTypeDef(BaseModel):
    authorizerDescription: AuthorizerDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDefaultAuthorizerResponseTypeDef(BaseModel):
    authorizerDescription: AuthorizerDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAuthorizersResponseTypeDef(BaseModel):
    authorizers: List[AuthorizerSummaryTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class AwsJobAbortConfigTypeDef(BaseModel):
    abortCriteriaList: Sequence[AwsJobAbortCriteriaTypeDef]

class AwsJobExponentialRolloutRateTypeDef(BaseModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: AwsJobRateIncreaseCriteriaTypeDef

class BehaviorCriteriaPaginatorTypeDef(BaseModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValuePaginatorTypeDef] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThresholdTypeDef] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfigTypeDef] = None

class BehaviorCriteriaTypeDef(BaseModel):
    comparisonOperator: Optional[ComparisonOperatorType] = None
    value: Optional[MetricValueTypeDef] = None
    durationSeconds: Optional[int] = None
    consecutiveDatapointsToAlarm: Optional[int] = None
    consecutiveDatapointsToClear: Optional[int] = None
    statisticalThreshold: Optional[StatisticalThresholdTypeDef] = None
    mlDetectionConfig: Optional[MachineLearningDetectionConfigTypeDef] = None

class GetBehaviorModelTrainingSummariesResponseTypeDef(BaseModel):
    summaries: List[BehaviorModelTrainingSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MetricToRetainTypeDef(BaseModel):
    metric: str
    metricDimension: Optional[MetricDimensionTypeDef] = None
    exportMetric: Optional[bool] = None

class DescribeBillingGroupResponseTypeDef(BaseModel):
    billingGroupName: str
    billingGroupId: str
    billingGroupArn: str
    version: int
    billingGroupProperties: BillingGroupPropertiesTypeDef
    billingGroupMetadata: BillingGroupMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBillingGroupRequestRequestTypeDef(BaseModel):
    billingGroupName: str
    billingGroupProperties: BillingGroupPropertiesTypeDef
    expectedVersion: Optional[int] = None

class CodeSigningSignatureTypeDef(BaseModel):
    inlineDocument: Optional[BlobTypeDef] = None

class MqttContextTypeDef(BaseModel):
    username: Optional[str] = None
    password: Optional[BlobTypeDef] = None
    clientId: Optional[str] = None

class GetBucketsAggregationResponseTypeDef(BaseModel):
    totalCount: int
    buckets: List[BucketTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BucketsAggregationTypeTypeDef(BaseModel):
    termsAggregation: Optional[TermsAggregationTypeDef] = None

class CACertificateDescriptionTypeDef(BaseModel):
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

class ListCACertificatesResponseTypeDef(BaseModel):
    certificates: List[CACertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CertificateDescriptionTypeDef(BaseModel):
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

class ListCertificateProvidersResponseTypeDef(BaseModel):
    certificateProviders: List[CertificateProviderSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificatesByCAResponseTypeDef(BaseModel):
    certificates: List[CertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCertificatesResponseTypeDef(BaseModel):
    certificates: List[CertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventConfigurationsResponseTypeDef(BaseModel):
    eventConfigurations: Dict[EventTypeType, ConfigurationTypeDef]
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventConfigurationsRequestRequestTypeDef(BaseModel):
    eventConfigurations: Optional[Mapping[EventTypeType, ConfigurationTypeDef]] = None

class ListAuditMitigationActionsTasksRequestRequestTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAuditTasksRequestRequestTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDetectMitigationActionsExecutionsRequestRequestTypeDef(BaseModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDetectMitigationActionsTasksRequestRequestTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListMetricValuesRequestRequestTypeDef(BaseModel):
    thingName: str
    metricName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListViolationEventsRequestRequestTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class CreateAuthorizerRequestRequestTypeDef(BaseModel):
    authorizerName: str
    authorizerFunctionArn: str
    tokenKeyName: Optional[str] = None
    tokenSigningPublicKeys: Optional[Mapping[str, str]] = None
    status: Optional[AuthorizerStatusType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    signingDisabled: Optional[bool] = None
    enableCachingForHttp: Optional[bool] = None

class CreateBillingGroupRequestRequestTypeDef(BaseModel):
    billingGroupName: str
    billingGroupProperties: Optional[BillingGroupPropertiesTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateCertificateProviderRequestRequestTypeDef(BaseModel):
    certificateProviderName: str
    lambdaFunctionArn: str
    accountDefaultForOperations: Sequence[Literal["CreateCertificateFromCsr"]]
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateCustomMetricRequestRequestTypeDef(BaseModel):
    metricName: str
    metricType: CustomMetricTypeType
    clientRequestToken: str
    displayName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDimensionRequestRequestTypeDef(BaseModel):
    name: str
    type: Literal["TOPIC_FILTER"]
    stringValues: Sequence[str]
    clientRequestToken: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateFleetMetricRequestRequestTypeDef(BaseModel):
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

class CreatePolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    policyDocument: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRoleAliasRequestRequestTypeDef(BaseModel):
    roleAlias: str
    roleArn: str
    credentialDurationSeconds: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateScheduledAuditRequestRequestTypeDef(BaseModel):
    frequency: AuditFrequencyType
    targetCheckNames: Sequence[str]
    scheduledAuditName: str
    dayOfMonth: Optional[str] = None
    dayOfWeek: Optional[DayOfWeekType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateDomainConfigurationRequestRequestTypeDef(BaseModel):
    domainConfigurationName: str
    domainName: Optional[str] = None
    serverCertificateArns: Optional[Sequence[str]] = None
    validationCertificateArn: Optional[str] = None
    authorizerConfig: Optional[AuthorizerConfigTypeDef] = None
    serviceType: Optional[ServiceTypeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None
    serverCertificateConfig: Optional[ServerCertificateConfigTypeDef] = None

class UpdateDomainConfigurationRequestRequestTypeDef(BaseModel):
    domainConfigurationName: str
    authorizerConfig: Optional[AuthorizerConfigTypeDef] = None
    domainConfigurationStatus: Optional[DomainConfigurationStatusType] = None
    removeAuthorizerConfig: Optional[bool] = None
    tlsConfig: Optional[TlsConfigTypeDef] = None
    serverCertificateConfig: Optional[ServerCertificateConfigTypeDef] = None

class SchedulingConfigTypeDef(BaseModel):
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    endBehavior: Optional[JobEndBehaviorType] = None
    maintenanceWindows: Optional[Sequence[MaintenanceWindowTypeDef]] = None

class CreateKeysAndCertificateResponseTypeDef(BaseModel):
    certificateArn: str
    certificateId: str
    certificatePem: str
    keyPair: KeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisioningClaimResponseTypeDef(BaseModel):
    certificateId: str
    certificatePem: str
    keyPair: KeyPairTypeDef
    expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisioningTemplateRequestRequestTypeDef(BaseModel):
    templateName: str
    templateBody: str
    provisioningRoleArn: str
    description: Optional[str] = None
    enabled: Optional[bool] = None
    preProvisioningHook: Optional[ProvisioningHookTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    type: Optional[TemplateTypeType] = None

class DescribeProvisioningTemplateResponseTypeDef(BaseModel):
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

class UpdateProvisioningTemplateRequestRequestTypeDef(BaseModel):
    templateName: str
    description: Optional[str] = None
    enabled: Optional[bool] = None
    defaultVersionId: Optional[int] = None
    provisioningRoleArn: Optional[str] = None
    preProvisioningHook: Optional[ProvisioningHookTypeDef] = None
    removePreProvisioningHook: Optional[bool] = None

class CreateThingTypeRequestRequestTypeDef(BaseModel):
    thingTypeName: str
    thingTypeProperties: Optional[ThingTypePropertiesTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class DescribeAuditTaskResponseTypeDef(BaseModel):
    taskStatus: AuditTaskStatusType
    taskType: AuditTaskTypeType
    taskStartTime: datetime
    taskStatistics: TaskStatisticsTypeDef
    scheduledAuditName: str
    auditDetails: Dict[str, AuditCheckDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCACertificateRequestRequestTypeDef(BaseModel):
    caCertificate: str
    verificationCertificate: Optional[str] = None
    setAsActive: Optional[bool] = None
    allowAutoRegistration: Optional[bool] = None
    registrationConfig: Optional[RegistrationConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    certificateMode: Optional[CertificateModeType] = None

class UpdateCACertificateRequestRequestTypeDef(BaseModel):
    certificateId: str
    newStatus: Optional[CACertificateStatusType] = None
    newAutoRegistrationStatus: Optional[AutoRegistrationStatusType] = None
    registrationConfig: Optional[RegistrationConfigTypeDef] = None
    removeAutoRegistration: Optional[bool] = None

class DescribeDomainConfigurationResponseTypeDef(BaseModel):
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

class DescribeManagedJobTemplateResponseTypeDef(BaseModel):
    templateName: str
    templateArn: str
    description: str
    templateVersion: str
    environments: List[str]
    documentParameters: List[DocumentParameterTypeDef]
    document: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRoleAliasResponseTypeDef(BaseModel):
    roleAliasDescription: RoleAliasDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeThingTypeResponseTypeDef(BaseModel):
    thingTypeName: str
    thingTypeId: str
    thingTypeArn: str
    thingTypeProperties: ThingTypePropertiesTypeDef
    thingTypeMetadata: ThingTypeMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ThingTypeDefinitionTypeDef(BaseModel):
    thingTypeName: Optional[str] = None
    thingTypeArn: Optional[str] = None
    thingTypeProperties: Optional[ThingTypePropertiesTypeDef] = None
    thingTypeMetadata: Optional[ThingTypeMetadataTypeDef] = None

class DestinationTypeDef(BaseModel):
    s3Destination: Optional[S3DestinationTypeDef] = None

class ListDetectMitigationActionsExecutionsResponseTypeDef(BaseModel):
    actionsExecutions: List[DetectMitigationActionExecutionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDetectMitigationActionsTaskRequestRequestTypeDef(BaseModel):
    taskId: str
    target: DetectMitigationActionsTaskTargetTypeDef
    actions: Sequence[str]
    clientRequestToken: str
    violationEventOccurrenceRange: Optional[ViolationEventOccurrenceRangeTypeDef] = None
    includeOnlyActiveViolations: Optional[bool] = None
    includeSuppressedAlerts: Optional[bool] = None

class ListDomainConfigurationsResponseTypeDef(BaseModel):
    domainConfigurations: List[DomainConfigurationSummaryTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DynamoDBv2ActionTypeDef(BaseModel):
    roleArn: str
    putItem: PutItemInputTypeDef

class GetEffectivePoliciesResponseTypeDef(BaseModel):
    effectivePolicies: List[EffectivePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExponentialRolloutRateTypeDef(BaseModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: RateIncreaseCriteriaTypeDef

class ThingGroupIndexingConfigurationTypeDef(BaseModel):
    thingGroupIndexingMode: ThingGroupIndexingModeType
    managedFields: Optional[List[FieldTypeDef]] = None
    customFields: Optional[List[FieldTypeDef]] = None

class StreamFileTypeDef(BaseModel):
    fileId: Optional[int] = None
    s3Location: Optional[S3LocationTypeDef] = None

class FileLocationTypeDef(BaseModel):
    stream: Optional[StreamTypeDef] = None
    s3Location: Optional[S3LocationTypeDef] = None

class ListFleetMetricsResponseTypeDef(BaseModel):
    fleetMetrics: List[FleetMetricNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IndexingFilterTypeDef(BaseModel):
    namedShadowNames: Optional[List[str]] = None
    geoLocations: Optional[List[GeoLocationTargetTypeDef]] = None

class ListActiveViolationsRequestListActiveViolationsPaginateTypeDef(BaseModel):
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachedPoliciesRequestListAttachedPoliciesPaginateTypeDef(BaseModel):
    target: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditMitigationActionsExecutionsRequestListAuditMitigationActionsExecutionsPaginateTypeDef(BaseModel):
    taskId: str
    findingId: str
    actionStatus: Optional[AuditMitigationActionsExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditMitigationActionsTasksRequestListAuditMitigationActionsTasksPaginateTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    auditTaskId: Optional[str] = None
    findingId: Optional[str] = None
    taskStatus: Optional[AuditMitigationActionsTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditTasksRequestListAuditTasksPaginateTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    taskType: Optional[AuditTaskTypeType] = None
    taskStatus: Optional[AuditTaskStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuthorizersRequestListAuthorizersPaginateTypeDef(BaseModel):
    ascendingOrder: Optional[bool] = None
    status: Optional[AuthorizerStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBillingGroupsRequestListBillingGroupsPaginateTypeDef(BaseModel):
    namePrefixFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCACertificatesRequestListCACertificatesPaginateTypeDef(BaseModel):
    ascendingOrder: Optional[bool] = None
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesByCARequestListCertificatesByCAPaginateTypeDef(BaseModel):
    caCertificateId: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesRequestListCertificatesPaginateTypeDef(BaseModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomMetricsRequestListCustomMetricsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDetectMitigationActionsExecutionsRequestListDetectMitigationActionsExecutionsPaginateTypeDef(BaseModel):
    taskId: Optional[str] = None
    violationId: Optional[str] = None
    thingName: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDetectMitigationActionsTasksRequestListDetectMitigationActionsTasksPaginateTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDimensionsRequestListDimensionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainConfigurationsRequestListDomainConfigurationsPaginateTypeDef(BaseModel):
    serviceType: Optional[ServiceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFleetMetricsRequestListFleetMetricsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndicesRequestListIndicesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobExecutionsForJobRequestListJobExecutionsForJobPaginateTypeDef(BaseModel):
    jobId: str
    status: Optional[JobExecutionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobExecutionsForThingRequestListJobExecutionsForThingPaginateTypeDef(BaseModel):
    thingName: str
    status: Optional[JobExecutionStatusType] = None
    namespaceId: Optional[str] = None
    jobId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobTemplatesRequestListJobTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    status: Optional[JobStatusType] = None
    targetSelection: Optional[TargetSelectionType] = None
    thingGroupName: Optional[str] = None
    thingGroupId: Optional[str] = None
    namespaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListManagedJobTemplatesRequestListManagedJobTemplatesPaginateTypeDef(BaseModel):
    templateName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetricValuesRequestListMetricValuesPaginateTypeDef(BaseModel):
    thingName: str
    metricName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    dimensionName: Optional[str] = None
    dimensionValueOperator: Optional[DimensionValueOperatorType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMitigationActionsRequestListMitigationActionsPaginateTypeDef(BaseModel):
    actionType: Optional[MitigationActionTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOTAUpdatesRequestListOTAUpdatesPaginateTypeDef(BaseModel):
    otaUpdateStatus: Optional[OTAUpdateStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOutgoingCertificatesRequestListOutgoingCertificatesPaginateTypeDef(BaseModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionsRequestListPackageVersionsPaginateTypeDef(BaseModel):
    packageName: str
    status: Optional[PackageVersionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagesRequestListPackagesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPoliciesRequestListPoliciesPaginateTypeDef(BaseModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPolicyPrincipalsRequestListPolicyPrincipalsPaginateTypeDef(BaseModel):
    policyName: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalPoliciesRequestListPrincipalPoliciesPaginateTypeDef(BaseModel):
    principal: str
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalThingsRequestListPrincipalThingsPaginateTypeDef(BaseModel):
    principal: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisioningTemplateVersionsRequestListProvisioningTemplateVersionsPaginateTypeDef(BaseModel):
    templateName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisioningTemplatesRequestListProvisioningTemplatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRelatedResourcesForAuditFindingRequestListRelatedResourcesForAuditFindingPaginateTypeDef(BaseModel):
    findingId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoleAliasesRequestListRoleAliasesPaginateTypeDef(BaseModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListScheduledAuditsRequestListScheduledAuditsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilesForTargetRequestListSecurityProfilesForTargetPaginateTypeDef(BaseModel):
    securityProfileTargetArn: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef(BaseModel):
    dimensionName: Optional[str] = None
    metricName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsRequestListStreamsPaginateTypeDef(BaseModel):
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsForPolicyRequestListTargetsForPolicyPaginateTypeDef(BaseModel):
    policyName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsForSecurityProfileRequestListTargetsForSecurityProfilePaginateTypeDef(BaseModel):
    securityProfileName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingGroupsForThingRequestListThingGroupsForThingPaginateTypeDef(BaseModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingGroupsRequestListThingGroupsPaginateTypeDef(BaseModel):
    parentGroup: Optional[str] = None
    namePrefixFilter: Optional[str] = None
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingPrincipalsRequestListThingPrincipalsPaginateTypeDef(BaseModel):
    thingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingRegistrationTaskReportsRequestListThingRegistrationTaskReportsPaginateTypeDef(BaseModel):
    taskId: str
    reportType: ReportTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingRegistrationTasksRequestListThingRegistrationTasksPaginateTypeDef(BaseModel):
    status: Optional[StatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingTypesRequestListThingTypesPaginateTypeDef(BaseModel):
    thingTypeName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingsInBillingGroupRequestListThingsInBillingGroupPaginateTypeDef(BaseModel):
    billingGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingsInThingGroupRequestListThingsInThingGroupPaginateTypeDef(BaseModel):
    thingGroupName: str
    recursive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListThingsRequestListThingsPaginateTypeDef(BaseModel):
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    thingTypeName: Optional[str] = None
    usePrefixAttributeValue: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicRuleDestinationsRequestListTopicRuleDestinationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTopicRulesRequestListTopicRulesPaginateTypeDef(BaseModel):
    topic: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListV2LoggingLevelsRequestListV2LoggingLevelsPaginateTypeDef(BaseModel):
    targetType: Optional[LogTargetTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViolationEventsRequestListViolationEventsPaginateTypeDef(BaseModel):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    thingName: Optional[str] = None
    securityProfileName: Optional[str] = None
    behaviorCriteriaType: Optional[BehaviorCriteriaTypeType] = None
    listSuppressedAlerts: Optional[bool] = None
    verificationState: Optional[VerificationStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetPackageConfigurationResponseTypeDef(BaseModel):
    versionUpdateByJobsConfig: VersionUpdateByJobsConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageConfigurationRequestRequestTypeDef(BaseModel):
    versionUpdateByJobsConfig: Optional[VersionUpdateByJobsConfigTypeDef] = None
    clientToken: Optional[str] = None

class GetPercentilesResponseTypeDef(BaseModel):
    percentiles: List[PercentPairTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStatisticsResponseTypeDef(BaseModel):
    statistics: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBillingGroupsResponseTypeDef(BaseModel):
    billingGroups: List[GroupNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingGroupsForThingResponseTypeDef(BaseModel):
    thingGroups: List[GroupNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingGroupsResponseTypeDef(BaseModel):
    thingGroups: List[GroupNameAndArnTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ThingGroupMetadataTypeDef(BaseModel):
    parentGroupName: Optional[str] = None
    rootToParentThingGroups: Optional[List[GroupNameAndArnTypeDef]] = None
    creationDate: Optional[datetime] = None

class HttpAuthorizationTypeDef(BaseModel):
    sigv4: Optional[SigV4AuthorizationTypeDef] = None

class JobExecutionTypeDef(BaseModel):
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

class JobExecutionSummaryForJobTypeDef(BaseModel):
    thingArn: Optional[str] = None
    jobExecutionSummary: Optional[JobExecutionSummaryTypeDef] = None

class JobExecutionSummaryForThingTypeDef(BaseModel):
    jobId: Optional[str] = None
    jobExecutionSummary: Optional[JobExecutionSummaryTypeDef] = None

class JobExecutionsRetryConfigTypeDef(BaseModel):
    criteriaList: Sequence[RetryCriteriaTypeDef]

class ListJobsResponseTypeDef(BaseModel):
    jobs: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobTemplatesResponseTypeDef(BaseModel):
    jobTemplates: List[JobTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class KafkaActionTypeDef(BaseModel):
    destinationArn: str
    topic: str
    clientProperties: Mapping[str, str]
    key: Optional[str] = None
    partition: Optional[str] = None
    headers: Optional[Sequence[KafkaActionHeaderTypeDef]] = None

class ListManagedJobTemplatesResponseTypeDef(BaseModel):
    managedJobTemplates: List[ManagedJobTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMitigationActionsResponseTypeDef(BaseModel):
    actionIdentifiers: List[MitigationActionIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOTAUpdatesResponseTypeDef(BaseModel):
    otaUpdates: List[OTAUpdateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutgoingCertificatesResponseTypeDef(BaseModel):
    outgoingCertificates: List[OutgoingCertificateTypeDef]
    nextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageVersionsResponseTypeDef(BaseModel):
    packageVersionSummaries: List[PackageVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagesResponseTypeDef(BaseModel):
    packageSummaries: List[PackageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPolicyVersionsResponseTypeDef(BaseModel):
    policyVersions: List[PolicyVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisioningTemplateVersionsResponseTypeDef(BaseModel):
    versions: List[ProvisioningTemplateVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisioningTemplatesResponseTypeDef(BaseModel):
    templates: List[ProvisioningTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListScheduledAuditsResponseTypeDef(BaseModel):
    scheduledAudits: List[ScheduledAuditMetadataTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityProfilesResponseTypeDef(BaseModel):
    securityProfileIdentifiers: List[SecurityProfileIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsResponseTypeDef(BaseModel):
    streams: List[StreamSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsForSecurityProfileResponseTypeDef(BaseModel):
    securityProfileTargets: List[SecurityProfileTargetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SecurityProfileTargetMappingTypeDef(BaseModel):
    securityProfileIdentifier: Optional[SecurityProfileIdentifierTypeDef] = None
    target: Optional[SecurityProfileTargetTypeDef] = None

class ListThingsResponseTypeDef(BaseModel):
    things: List[ThingAttributeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicRulesResponseTypeDef(BaseModel):
    rules: List[TopicRuleListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LocationActionTypeDef(BaseModel):
    roleArn: str
    trackerName: str
    deviceId: str
    latitude: str
    longitude: str
    timestamp: Optional[LocationTimestampTypeDef] = None

class LogTargetConfigurationTypeDef(BaseModel):
    logTarget: Optional[LogTargetTypeDef] = None
    logLevel: Optional[LogLevelType] = None

class SetV2LoggingLevelRequestRequestTypeDef(BaseModel):
    logTarget: LogTargetTypeDef
    logLevel: LogLevelType

class SetLoggingOptionsRequestRequestTypeDef(BaseModel):
    loggingOptionsPayload: LoggingOptionsPayloadTypeDef

class MitigationActionParamsPaginatorTypeDef(BaseModel):
    updateDeviceCertificateParams: Optional[UpdateDeviceCertificateParamsTypeDef] = None
    updateCACertificateParams: Optional[UpdateCACertificateParamsTypeDef] = None
    addThingsToThingGroupParams: Optional[AddThingsToThingGroupParamsPaginatorTypeDef] = None
    replaceDefaultPolicyVersionParams: Optional[ReplaceDefaultPolicyVersionParamsTypeDef] = None
    enableIoTLoggingParams: Optional[EnableIoTLoggingParamsTypeDef] = None
    publishFindingToSnsParams: Optional[PublishFindingToSnsParamsTypeDef] = None

class MitigationActionParamsTypeDef(BaseModel):
    updateDeviceCertificateParams: Optional[UpdateDeviceCertificateParamsTypeDef] = None
    updateCACertificateParams: Optional[UpdateCACertificateParamsTypeDef] = None
    addThingsToThingGroupParams: Optional[AddThingsToThingGroupParamsTypeDef] = None
    replaceDefaultPolicyVersionParams: Optional[ReplaceDefaultPolicyVersionParamsTypeDef] = None
    enableIoTLoggingParams: Optional[EnableIoTLoggingParamsTypeDef] = None
    publishFindingToSnsParams: Optional[PublishFindingToSnsParamsTypeDef] = None

class MqttHeadersTypeDef(BaseModel):
    payloadFormatIndicator: Optional[str] = None
    contentType: Optional[str] = None
    responseTopic: Optional[str] = None
    correlationData: Optional[str] = None
    messageExpiry: Optional[str] = None
    userProperties: Optional[Sequence[UserPropertyTypeDef]] = None

class ResourceIdentifierTypeDef(BaseModel):
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

class ThingDocumentTypeDef(BaseModel):
    thingName: Optional[str] = None
    thingId: Optional[str] = None
    thingTypeName: Optional[str] = None
    thingGroupNames: Optional[List[str]] = None
    attributes: Optional[Dict[str, str]] = None
    shadow: Optional[str] = None
    deviceDefender: Optional[str] = None
    connectivity: Optional[ThingConnectivityTypeDef] = None

class ThingTypeDefinitionPaginatorTypeDef(BaseModel):
    thingTypeName: Optional[str] = None
    thingTypeArn: Optional[str] = None
    thingTypeProperties: Optional[ThingTypePropertiesPaginatorTypeDef] = None
    thingTypeMetadata: Optional[ThingTypeMetadataTypeDef] = None

class TimestreamActionTypeDef(BaseModel):
    roleArn: str
    databaseName: str
    tableName: str
    dimensions: Sequence[TimestreamDimensionTypeDef]
    timestamp: Optional[TimestreamTimestampTypeDef] = None

class TopicRuleDestinationConfigurationTypeDef(BaseModel):
    httpUrlConfiguration: Optional[HttpUrlDestinationConfigurationTypeDef] = None
    vpcConfiguration: Optional[VpcDestinationConfigurationTypeDef] = None

class TopicRuleDestinationSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    status: Optional[TopicRuleDestinationStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    statusReason: Optional[str] = None
    httpUrlSummary: Optional[HttpUrlDestinationSummaryTypeDef] = None
    vpcDestinationSummary: Optional[VpcDestinationSummaryTypeDef] = None

class TopicRuleDestinationTypeDef(BaseModel):
    arn: Optional[str] = None
    status: Optional[TopicRuleDestinationStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    statusReason: Optional[str] = None
    httpUrlProperties: Optional[HttpUrlDestinationPropertiesTypeDef] = None
    vpcProperties: Optional[VpcDestinationPropertiesTypeDef] = None

class ValidateSecurityProfileBehaviorsResponseTypeDef(BaseModel):
    valid: bool
    validationErrors: List[ValidationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricValuesResponsePaginatorTypeDef(BaseModel):
    metricDatumList: List[MetricDatumPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricValuesResponseTypeDef(BaseModel):
    metricDatumList: List[MetricDatumTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeniedTypeDef(BaseModel):
    implicitDeny: Optional[ImplicitDenyTypeDef] = None
    explicitDeny: Optional[ExplicitDenyTypeDef] = None

class PutAssetPropertyValueEntryTypeDef(BaseModel):
    propertyValues: Sequence[AssetPropertyValueTypeDef]
    entryId: Optional[str] = None
    assetId: Optional[str] = None
    propertyId: Optional[str] = None
    propertyAlias: Optional[str] = None

class CreateDynamicThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str
    queryString: str
    thingGroupProperties: Optional[ThingGroupPropertiesTypeDef] = None
    indexName: Optional[str] = None
    queryVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str
    parentGroupName: Optional[str] = None
    thingGroupProperties: Optional[ThingGroupPropertiesTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateDynamicThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesTypeDef
    expectedVersion: Optional[int] = None
    indexName: Optional[str] = None
    queryString: Optional[str] = None
    queryVersion: Optional[str] = None

class UpdateThingGroupRequestRequestTypeDef(BaseModel):
    thingGroupName: str
    thingGroupProperties: ThingGroupPropertiesTypeDef
    expectedVersion: Optional[int] = None

class AwsJobExecutionsRolloutConfigTypeDef(BaseModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[AwsJobExponentialRolloutRateTypeDef] = None

class BehaviorPaginatorTypeDef(BaseModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimensionTypeDef] = None
    criteria: Optional[BehaviorCriteriaPaginatorTypeDef] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None

class BehaviorTypeDef(BaseModel):
    name: str
    metric: Optional[str] = None
    metricDimension: Optional[MetricDimensionTypeDef] = None
    criteria: Optional[BehaviorCriteriaTypeDef] = None
    suppressAlerts: Optional[bool] = None
    exportMetric: Optional[bool] = None

class CustomCodeSigningTypeDef(BaseModel):
    signature: Optional[CodeSigningSignatureTypeDef] = None
    certificateChain: Optional[CodeSigningCertificateChainTypeDef] = None
    hashAlgorithm: Optional[str] = None
    signatureAlgorithm: Optional[str] = None

class TestInvokeAuthorizerRequestRequestTypeDef(BaseModel):
    authorizerName: str
    token: Optional[str] = None
    tokenSignature: Optional[str] = None
    httpContext: Optional[HttpContextTypeDef] = None
    mqttContext: Optional[MqttContextTypeDef] = None
    tlsContext: Optional[TlsContextTypeDef] = None

class GetBucketsAggregationRequestRequestTypeDef(BaseModel):
    queryString: str
    aggregationField: str
    bucketsAggregationType: BucketsAggregationTypeTypeDef
    indexName: Optional[str] = None
    queryVersion: Optional[str] = None

class DescribeCACertificateResponseTypeDef(BaseModel):
    certificateDescription: CACertificateDescriptionTypeDef
    registrationConfig: RegistrationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateResponseTypeDef(BaseModel):
    certificateDescription: CertificateDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingTypesResponseTypeDef(BaseModel):
    thingTypes: List[ThingTypeDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSigningJobParameterTypeDef(BaseModel):
    signingProfileParameter: Optional[SigningProfileParameterTypeDef] = None
    signingProfileName: Optional[str] = None
    destination: Optional[DestinationTypeDef] = None

class JobExecutionsRolloutConfigTypeDef(BaseModel):
    maximumPerMinute: Optional[int] = None
    exponentialRate: Optional[ExponentialRolloutRateTypeDef] = None

class CreateStreamRequestRequestTypeDef(BaseModel):
    streamId: str
    files: Sequence[StreamFileTypeDef]
    roleArn: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class StreamInfoTypeDef(BaseModel):
    streamId: Optional[str] = None
    streamArn: Optional[str] = None
    streamVersion: Optional[int] = None
    description: Optional[str] = None
    files: Optional[List[StreamFileTypeDef]] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None
    roleArn: Optional[str] = None

class UpdateStreamRequestRequestTypeDef(BaseModel):
    streamId: str
    description: Optional[str] = None
    files: Optional[Sequence[StreamFileTypeDef]] = None
    roleArn: Optional[str] = None

class ThingIndexingConfigurationTypeDef(BaseModel):
    thingIndexingMode: ThingIndexingModeType
    thingConnectivityIndexingMode: Optional[ThingConnectivityIndexingModeType] = None
    deviceDefenderIndexingMode: Optional[DeviceDefenderIndexingModeType] = None
    namedShadowIndexingMode: Optional[NamedShadowIndexingModeType] = None
    managedFields: Optional[List[FieldTypeDef]] = None
    customFields: Optional[List[FieldTypeDef]] = None
    filter: Optional[IndexingFilterTypeDef] = None

class DescribeThingGroupResponseTypeDef(BaseModel):
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

class HttpActionTypeDef(BaseModel):
    url: str
    confirmationUrl: Optional[str] = None
    headers: Optional[Sequence[HttpActionHeaderTypeDef]] = None
    auth: Optional[HttpAuthorizationTypeDef] = None

class DescribeJobExecutionResponseTypeDef(BaseModel):
    execution: JobExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobExecutionsForJobResponseTypeDef(BaseModel):
    executionSummaries: List[JobExecutionSummaryForJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobExecutionsForThingResponseTypeDef(BaseModel):
    executionSummaries: List[JobExecutionSummaryForThingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityProfilesForTargetResponseTypeDef(BaseModel):
    securityProfileTargetMappings: List[SecurityProfileTargetMappingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListV2LoggingLevelsResponseTypeDef(BaseModel):
    logTargetConfigurations: List[LogTargetConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class MitigationActionPaginatorTypeDef(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsPaginatorTypeDef] = None

class CreateMitigationActionRequestRequestTypeDef(BaseModel):
    actionName: str
    roleArn: str
    actionParams: MitigationActionParamsTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class DescribeMitigationActionResponseTypeDef(BaseModel):
    actionName: str
    actionType: MitigationActionTypeType
    actionArn: str
    actionId: str
    roleArn: str
    actionParams: MitigationActionParamsTypeDef
    creationDate: datetime
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class MitigationActionTypeDef(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsTypeDef] = None

class UpdateMitigationActionRequestRequestTypeDef(BaseModel):
    actionName: str
    roleArn: Optional[str] = None
    actionParams: Optional[MitigationActionParamsTypeDef] = None

class RepublishActionTypeDef(BaseModel):
    roleArn: str
    topic: str
    qos: Optional[int] = None
    headers: Optional[MqttHeadersTypeDef] = None

class AuditSuppressionTypeDef(BaseModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: Optional[datetime] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None

class CreateAuditSuppressionRequestRequestTypeDef(BaseModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    clientRequestToken: str
    expirationDate: Optional[TimestampTypeDef] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None

class DeleteAuditSuppressionRequestRequestTypeDef(BaseModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef

class DescribeAuditSuppressionRequestRequestTypeDef(BaseModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef

class DescribeAuditSuppressionResponseTypeDef(BaseModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: datetime
    suppressIndefinitely: bool
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAuditFindingsRequestListAuditFindingsPaginateTypeDef(BaseModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    listSuppressedFindings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditFindingsRequestRequestTypeDef(BaseModel):
    taskId: Optional[str] = None
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    listSuppressedFindings: Optional[bool] = None

class ListAuditSuppressionsRequestListAuditSuppressionsPaginateTypeDef(BaseModel):
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    ascendingOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuditSuppressionsRequestRequestTypeDef(BaseModel):
    checkName: Optional[str] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    ascendingOrder: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class NonCompliantResourceTypeDef(BaseModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    additionalInfo: Optional[Dict[str, str]] = None

class RelatedResourceTypeDef(BaseModel):
    resourceType: Optional[ResourceTypeType] = None
    resourceIdentifier: Optional[ResourceIdentifierTypeDef] = None
    additionalInfo: Optional[Dict[str, str]] = None

class UpdateAuditSuppressionRequestRequestTypeDef(BaseModel):
    checkName: str
    resourceIdentifier: ResourceIdentifierTypeDef
    expirationDate: Optional[TimestampTypeDef] = None
    suppressIndefinitely: Optional[bool] = None
    description: Optional[str] = None

class SearchIndexResponseTypeDef(BaseModel):
    nextToken: str
    things: List[ThingDocumentTypeDef]
    thingGroups: List[ThingGroupDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListThingTypesResponsePaginatorTypeDef(BaseModel):
    thingTypes: List[ThingTypeDefinitionPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRuleDestinationRequestRequestTypeDef(BaseModel):
    destinationConfiguration: TopicRuleDestinationConfigurationTypeDef

class ListTopicRuleDestinationsResponseTypeDef(BaseModel):
    destinationSummaries: List[TopicRuleDestinationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTopicRuleDestinationResponseTypeDef(BaseModel):
    topicRuleDestination: TopicRuleDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTopicRuleDestinationResponseTypeDef(BaseModel):
    topicRuleDestination: TopicRuleDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AuthResultTypeDef(BaseModel):
    authInfo: Optional[AuthInfoTypeDef] = None
    allowed: Optional[AllowedTypeDef] = None
    denied: Optional[DeniedTypeDef] = None
    authDecision: Optional[AuthDecisionType] = None
    missingContextValues: Optional[List[str]] = None

class IotSiteWiseActionTypeDef(BaseModel):
    putAssetPropertyValueEntries: Sequence[PutAssetPropertyValueEntryTypeDef]
    roleArn: str

class ActiveViolationPaginatorTypeDef(BaseModel):
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

class ViolationEventPaginatorTypeDef(BaseModel):
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

class ActiveViolationTypeDef(BaseModel):
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

class CreateSecurityProfileRequestRequestTypeDef(BaseModel):
    securityProfileName: str
    securityProfileDescription: Optional[str] = None
    behaviors: Optional[Sequence[BehaviorTypeDef]] = None
    alertTargets: Optional[Mapping[Literal["SNS"], AlertTargetTypeDef]] = None
    additionalMetricsToRetain: Optional[Sequence[str]] = None
    additionalMetricsToRetainV2: Optional[Sequence[MetricToRetainTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    metricsExportConfig: Optional[MetricsExportConfigTypeDef] = None

class DescribeSecurityProfileResponseTypeDef(BaseModel):
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

class UpdateSecurityProfileRequestRequestTypeDef(BaseModel):
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

class UpdateSecurityProfileResponseTypeDef(BaseModel):
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

class ValidateSecurityProfileBehaviorsRequestRequestTypeDef(BaseModel):
    behaviors: Sequence[BehaviorTypeDef]

class ViolationEventTypeDef(BaseModel):
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

class CodeSigningTypeDef(BaseModel):
    awsSignerJobId: Optional[str] = None
    startSigningJobParameter: Optional[StartSigningJobParameterTypeDef] = None
    customCodeSigning: Optional[CustomCodeSigningTypeDef] = None

class CreateJobRequestRequestTypeDef(BaseModel):
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

class CreateJobTemplateRequestRequestTypeDef(BaseModel):
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

class DescribeJobTemplateResponseTypeDef(BaseModel):
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

class JobTypeDef(BaseModel):
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

class UpdateJobRequestRequestTypeDef(BaseModel):
    jobId: str
    description: Optional[str] = None
    presignedUrlConfig: Optional[PresignedUrlConfigTypeDef] = None
    jobExecutionsRolloutConfig: Optional[JobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[AbortConfigTypeDef] = None
    timeoutConfig: Optional[TimeoutConfigTypeDef] = None
    namespaceId: Optional[str] = None
    jobExecutionsRetryConfig: Optional[JobExecutionsRetryConfigTypeDef] = None

class DescribeStreamResponseTypeDef(BaseModel):
    streamInfo: StreamInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIndexingConfigurationResponseTypeDef(BaseModel):
    thingIndexingConfiguration: ThingIndexingConfigurationTypeDef
    thingGroupIndexingConfiguration: ThingGroupIndexingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIndexingConfigurationRequestRequestTypeDef(BaseModel):
    thingIndexingConfiguration: Optional[ThingIndexingConfigurationTypeDef] = None
    thingGroupIndexingConfiguration: Optional[ThingGroupIndexingConfigurationTypeDef] = None

class DetectMitigationActionsTaskSummaryPaginatorTypeDef(BaseModel):
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

class DescribeAuditMitigationActionsTaskResponseTypeDef(BaseModel):
    taskStatus: AuditMitigationActionsTaskStatusType
    startTime: datetime
    endTime: datetime
    taskStatistics: Dict[str, TaskStatisticsForAuditCheckTypeDef]
    target: AuditMitigationActionsTaskTargetTypeDef
    auditCheckToActionsMapping: Dict[str, List[str]]
    actionsDefinition: List[MitigationActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectMitigationActionsTaskSummaryTypeDef(BaseModel):
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

class ListAuditSuppressionsResponseTypeDef(BaseModel):
    suppressions: List[AuditSuppressionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AuditFindingTypeDef(BaseModel):
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

class ListRelatedResourcesForAuditFindingResponseTypeDef(BaseModel):
    relatedResources: List[RelatedResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestAuthorizationResponseTypeDef(BaseModel):
    authResults: List[AuthResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ActionTypeDef(BaseModel):
    dynamoDB: Optional[DynamoDBActionTypeDef] = None
    dynamoDBv2: Optional[DynamoDBv2ActionTypeDef] = None
    lambda: Optional[LambdaActionTypeDef] = None
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

class ListActiveViolationsResponsePaginatorTypeDef(BaseModel):
    activeViolations: List[ActiveViolationPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListViolationEventsResponsePaginatorTypeDef(BaseModel):
    violationEvents: List[ViolationEventPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListActiveViolationsResponseTypeDef(BaseModel):
    activeViolations: List[ActiveViolationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListViolationEventsResponseTypeDef(BaseModel):
    violationEvents: List[ViolationEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OTAUpdateFileTypeDef(BaseModel):
    fileName: Optional[str] = None
    fileType: Optional[int] = None
    fileVersion: Optional[str] = None
    fileLocation: Optional[FileLocationTypeDef] = None
    codeSigning: Optional[CodeSigningTypeDef] = None
    attributes: Optional[Mapping[str, str]] = None

class DescribeJobResponseTypeDef(BaseModel):
    documentSource: str
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectMitigationActionsTasksResponsePaginatorTypeDef(BaseModel):
    tasks: List[DetectMitigationActionsTaskSummaryPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDetectMitigationActionsTaskResponseTypeDef(BaseModel):
    taskSummary: DetectMitigationActionsTaskSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDetectMitigationActionsTasksResponseTypeDef(BaseModel):
    tasks: List[DetectMitigationActionsTaskSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAuditFindingResponseTypeDef(BaseModel):
    finding: AuditFindingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAuditFindingsResponseTypeDef(BaseModel):
    findings: List[AuditFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TopicRulePayloadTypeDef(BaseModel):
    sql: str
    actions: Sequence[ActionTypeDef]
    description: Optional[str] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionTypeDef] = None

class TopicRuleTypeDef(BaseModel):
    ruleName: Optional[str] = None
    sql: Optional[str] = None
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    actions: Optional[List[ActionTypeDef]] = None
    ruleDisabled: Optional[bool] = None
    awsIotSqlVersion: Optional[str] = None
    errorAction: Optional[ActionTypeDef] = None

class CreateOTAUpdateRequestRequestTypeDef(BaseModel):
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

class OTAUpdateInfoTypeDef(BaseModel):
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

class CreateTopicRuleRequestRequestTypeDef(BaseModel):
    ruleName: str
    topicRulePayload: TopicRulePayloadTypeDef
    tags: Optional[str] = None

class ReplaceTopicRuleRequestRequestTypeDef(BaseModel):
    ruleName: str
    topicRulePayload: TopicRulePayloadTypeDef

class GetTopicRuleResponseTypeDef(BaseModel):
    ruleArn: str
    rule: TopicRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOTAUpdateResponseTypeDef(BaseModel):
    otaUpdateInfo: OTAUpdateInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

