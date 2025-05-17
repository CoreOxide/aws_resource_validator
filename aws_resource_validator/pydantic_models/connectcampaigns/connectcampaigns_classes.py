from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.connectcampaigns.connectcampaigns_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AgentlessDialerConfig(BaseValidatorModel):
    dialingCapacity: Optional[float] = None


class AnswerMachineDetectionConfig(BaseValidatorModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None


class InstanceIdFilter(BaseValidatorModel):
    value: str
    operator: Literal['Eq']


class CampaignSummary(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_campaign' function.
class DeleteCampaignRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_connect_instance_config' function.
class DeleteConnectInstanceConfigRequest(BaseValidatorModel):
    connectInstanceId: str


# This class is the input for the 'delete_instance_onboarding_job' function.
class DeleteInstanceOnboardingJobRequest(BaseValidatorModel):
    connectInstanceId: str


# This class is the input for the 'describe_campaign' function.
class DescribeCampaignRequest(BaseValidatorModel):
    id: str

Timestamp = Union[datetime, str]


class PredictiveDialerConfig(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None


class ProgressiveDialerConfig(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None


class EncryptionConfig(BaseValidatorModel):
    enabled: bool
    encryptionType: Optional[Literal['KMS']] = None
    keyArn: Optional[str] = None


class FailedCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None


class FailedRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None
    failureCode: Optional[FailureCodeType] = None


# This class is the input for the 'get_campaign_state_batch' function.
class GetCampaignStateBatchRequest(BaseValidatorModel):
    campaignIds: List[str]


class SuccessfulCampaignStateResponse(BaseValidatorModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None


# This class is the input for the 'get_campaign_state' function.
class GetCampaignStateRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_connect_instance_config' function.
class GetConnectInstanceConfigRequest(BaseValidatorModel):
    connectInstanceId: str


# This class is the input for the 'get_instance_onboarding_job_status' function.
class GetInstanceOnboardingJobStatusRequest(BaseValidatorModel):
    connectInstanceId: str


class InstanceOnboardingJobStatus(BaseValidatorModel):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: Optional[InstanceOnboardingJobFailureCodeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'pause_campaign' function.
class PauseCampaignRequest(BaseValidatorModel):
    id: str


class SuccessfulRequest(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None


# This class is the input for the 'resume_campaign' function.
class ResumeCampaignRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'start_campaign' function.
class StartCampaignRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'stop_campaign' function.
class StopCampaignRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: List[str]


# This class is the input for the 'update_campaign_name' function.
class UpdateCampaignNameRequest(BaseValidatorModel):
    id: str
    name: str


class OutboundCallConfig(BaseValidatorModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    connectQueueId: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


# This class is the input for the 'update_campaign_outbound_call_config' function.
class UpdateCampaignOutboundCallConfigRequest(BaseValidatorModel):
    id: str
    connectContactFlowId: Optional[str] = None
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None


class CampaignFilters(BaseValidatorModel):
    instanceIdFilter: Optional[InstanceIdFilter] = None


# This class is the output for the 'create_campaign' function.
class CreateCampaignResponse(BaseValidatorModel):
    id: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_campaign_outbound_call_config' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_campaign_state' function.
class GetCampaignStateResponse(BaseValidatorModel):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_campaigns' function.
class ListCampaignsResponse(BaseValidatorModel):
    campaignSummaryList: List[CampaignSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DialRequest(BaseValidatorModel):
    clientToken: str
    phoneNumber: str
    expirationTime: Timestamp
    attributes: Dict[str, str]


class DialerConfig(BaseValidatorModel):
    progressiveDialerConfig: Optional[ProgressiveDialerConfig] = None
    predictiveDialerConfig: Optional[PredictiveDialerConfig] = None
    agentlessDialerConfig: Optional[AgentlessDialerConfig] = None


class InstanceConfig(BaseValidatorModel):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfig


# This class is the input for the 'start_instance_onboarding_job' function.
class StartInstanceOnboardingJobRequest(BaseValidatorModel):
    connectInstanceId: str
    encryptionConfig: EncryptionConfig


# This class is the output for the 'get_campaign_state_batch' function.
class GetCampaignStateBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulCampaignStateResponse]
    failedRequests: List[FailedCampaignStateResponse]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_onboarding_job_status' function.
class GetInstanceOnboardingJobStatusResponse(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_instance_onboarding_job' function.
class StartInstanceOnboardingJobResponse(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_dial_request_batch' function.
class PutDialRequestBatchResponse(BaseValidatorModel):
    successfulRequests: List[SuccessfulRequest]
    failedRequests: List[FailedRequest]
    ResponseMetadata: ResponseMetadata


class ListCampaignsRequestPaginate(BaseValidatorModel):
    filters: Optional[CampaignFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_campaigns' function.
class ListCampaignsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[CampaignFilters] = None


# This class is the input for the 'put_dial_request_batch' function.
class PutDialRequestBatchRequest(BaseValidatorModel):
    id: str
    dialRequests: List[DialRequest]


class Campaign(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfig
    outboundCallConfig: OutboundCallConfig
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_campaign' function.
class CreateCampaignRequest(BaseValidatorModel):
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfig
    outboundCallConfig: OutboundCallConfig
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_campaign_dialer_config' function.
class UpdateCampaignDialerConfigRequest(BaseValidatorModel):
    id: str
    dialerConfig: DialerConfig


# This class is the output for the 'get_connect_instance_config' function.
class GetConnectInstanceConfigResponse(BaseValidatorModel):
    connectInstanceConfig: InstanceConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_campaign' function.
class DescribeCampaignResponse(BaseValidatorModel):
    campaign: Campaign
    ResponseMetadata: ResponseMetadata