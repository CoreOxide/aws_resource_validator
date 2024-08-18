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
from aws_resource_validator.pydantic_models.connectcampaigns_constants import *

class AgentlessDialerConfigTypeDef(BaseValidatorModel):
    dialingCapacity: Optional[float] = None

class AnswerMachineDetectionConfigTypeDef(BaseValidatorModel):
    enableAnswerMachineDetection: bool
    awaitAnswerMachinePrompt: Optional[bool] = None

class InstanceIdFilterTypeDef(BaseValidatorModel):
    value: str
    operator: Literal["Eq"]

class CampaignSummaryTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteCampaignRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteConnectInstanceConfigRequestRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str

class DeleteInstanceOnboardingJobRequestRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str

class DescribeCampaignRequestRequestTypeDef(BaseValidatorModel):
    id: str

class PredictiveDialerConfigTypeDef(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None

class ProgressiveDialerConfigTypeDef(BaseValidatorModel):
    bandwidthAllocation: float
    dialingCapacity: Optional[float] = None

class EncryptionConfigTypeDef(BaseValidatorModel):
    enabled: bool
    encryptionType: Optional[Literal["KMS"]] = None
    keyArn: Optional[str] = None

class FailedCampaignStateResponseTypeDef(BaseValidatorModel):
    campaignId: Optional[str] = None
    failureCode: Optional[GetCampaignStateBatchFailureCodeType] = None

class FailedRequestTypeDef(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None
    failureCode: Optional[FailureCodeType] = None

class GetCampaignStateBatchRequestRequestTypeDef(BaseValidatorModel):
    campaignIds: Sequence[str]

class SuccessfulCampaignStateResponseTypeDef(BaseValidatorModel):
    campaignId: Optional[str] = None
    state: Optional[CampaignStateType] = None

class GetCampaignStateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetConnectInstanceConfigRequestRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str

class GetInstanceOnboardingJobStatusRequestRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str

class InstanceOnboardingJobStatusTypeDef(BaseValidatorModel):
    connectInstanceId: str
    status: InstanceOnboardingJobStatusCodeType
    failureCode: Optional[InstanceOnboardingJobFailureCodeType] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class PauseCampaignRequestRequestTypeDef(BaseValidatorModel):
    id: str

class SuccessfulRequestTypeDef(BaseValidatorModel):
    clientToken: Optional[str] = None
    id: Optional[str] = None

class ResumeCampaignRequestRequestTypeDef(BaseValidatorModel):
    id: str

class StartCampaignRequestRequestTypeDef(BaseValidatorModel):
    id: str

class StopCampaignRequestRequestTypeDef(BaseValidatorModel):
    id: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]

class UpdateCampaignNameRequestRequestTypeDef(BaseValidatorModel):
    id: str
    name: str

class OutboundCallConfigTypeDef(BaseValidatorModel):
    connectContactFlowId: str
    connectSourcePhoneNumber: Optional[str] = None
    connectQueueId: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None

class UpdateCampaignOutboundCallConfigRequestRequestTypeDef(BaseValidatorModel):
    id: str
    connectContactFlowId: Optional[str] = None
    connectSourcePhoneNumber: Optional[str] = None
    answerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None

class CampaignFiltersTypeDef(BaseValidatorModel):
    instanceIdFilter: Optional[InstanceIdFilterTypeDef] = None

class CreateCampaignResponseTypeDef(BaseValidatorModel):
    id: str
    arn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCampaignStateResponseTypeDef(BaseValidatorModel):
    state: CampaignStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListCampaignsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    campaignSummaryList: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DialRequestTypeDef(BaseValidatorModel):
    clientToken: str
    phoneNumber: str
    expirationTime: TimestampTypeDef
    attributes: Mapping[str, str]

class DialerConfigTypeDef(BaseValidatorModel):
    progressiveDialerConfig: Optional[ProgressiveDialerConfigTypeDef] = None
    predictiveDialerConfig: Optional[PredictiveDialerConfigTypeDef] = None
    agentlessDialerConfig: Optional[AgentlessDialerConfigTypeDef] = None

class InstanceConfigTypeDef(BaseValidatorModel):
    connectInstanceId: str
    serviceLinkedRoleArn: str
    encryptionConfig: EncryptionConfigTypeDef

class StartInstanceOnboardingJobRequestRequestTypeDef(BaseValidatorModel):
    connectInstanceId: str
    encryptionConfig: EncryptionConfigTypeDef

class GetCampaignStateBatchResponseTypeDef(BaseValidatorModel):
    successfulRequests: List[SuccessfulCampaignStateResponseTypeDef]
    failedRequests: List[FailedCampaignStateResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceOnboardingJobStatusResponseTypeDef(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartInstanceOnboardingJobResponseTypeDef(BaseValidatorModel):
    connectInstanceOnboardingJobStatus: InstanceOnboardingJobStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDialRequestBatchResponseTypeDef(BaseValidatorModel):
    successfulRequests: List[SuccessfulRequestTypeDef]
    failedRequests: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCampaignsRequestListCampaignsPaginateTypeDef(BaseValidatorModel):
    filters: Optional[CampaignFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCampaignsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[CampaignFiltersTypeDef] = None

class PutDialRequestBatchRequestRequestTypeDef(BaseValidatorModel):
    id: str
    dialRequests: Sequence[DialRequestTypeDef]

class CampaignTypeDef(BaseValidatorModel):
    id: str
    arn: str
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfigTypeDef
    outboundCallConfig: OutboundCallConfigTypeDef
    tags: Optional[Dict[str, str]] = None

class CreateCampaignRequestRequestTypeDef(BaseValidatorModel):
    name: str
    connectInstanceId: str
    dialerConfig: DialerConfigTypeDef
    outboundCallConfig: OutboundCallConfigTypeDef
    tags: Optional[Mapping[str, str]] = None

class UpdateCampaignDialerConfigRequestRequestTypeDef(BaseValidatorModel):
    id: str
    dialerConfig: DialerConfigTypeDef

class GetConnectInstanceConfigResponseTypeDef(BaseValidatorModel):
    connectInstanceConfig: InstanceConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCampaignResponseTypeDef(BaseValidatorModel):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

