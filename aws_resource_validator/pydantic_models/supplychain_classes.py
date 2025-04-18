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
from aws_resource_validator.pydantic_models.supplychain_constants import *

class BillOfMaterialsImportJob(BaseValidatorModel):
    instanceId: str
    jobId: str
    status: ConfigurationJobStatusType
    s3uri: str
    message: Optional[str] = None


class CreateBillOfMaterialsImportJobRequest(BaseValidatorModel):
    instanceId: str
    s3uri: str
    clientToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateInstanceRequest(BaseValidatorModel):
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    webAppDnsDomain: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class Instance(BaseValidatorModel):
    instanceId: str
    awsAccountId: str
    state: InstanceStateType
    errorMessage: Optional[str] = None
    webAppDnsDomain: Optional[str] = None
    createdTime: Optional[datetime] = None
    lastModifiedTime: Optional[datetime] = None
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    versionNumber: Optional[float] = None


class DataIntegrationFlowDatasetOptions(BaseValidatorModel):
    loadType: Optional[DataIntegrationFlowLoadTypeType] = None
    dedupeRecords: Optional[bool] = None


class DataIntegrationFlowS3Options(BaseValidatorModel):
    fileType: Optional[DataIntegrationFlowFileTypeType] = None


class DataIntegrationFlowSQLTransformationConfiguration(BaseValidatorModel):
    query: str


class DeleteDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str


class DeleteDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str


class DeleteInstanceRequest(BaseValidatorModel):
    instanceId: str


class GetBillOfMaterialsImportJobRequest(BaseValidatorModel):
    instanceId: str
    jobId: str


class GetDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str


class GetDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str


class GetInstanceRequest(BaseValidatorModel):
    instanceId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDataIntegrationFlowsRequest(BaseValidatorModel):
    instanceId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataLakeDatasetsRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListInstancesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    instanceNameFilter: Optional[Sequence[str]] = None
    instanceStateFilter: Optional[Sequence[InstanceStateType]] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    description: Optional[str] = None


class UpdateInstanceRequest(BaseValidatorModel):
    instanceId: str
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None


class CreateBillOfMaterialsImportJobResponse(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


class CreateDataIntegrationFlowResponse(BaseValidatorModel):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadata


class DeleteDataIntegrationFlowResponse(BaseValidatorModel):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadata


class DeleteDataLakeDatasetResponse(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    ResponseMetadata: ResponseMetadata


class GetBillOfMaterialsImportJobResponse(BaseValidatorModel):
    job: BillOfMaterialsImportJob
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SendDataIntegrationEventResponse(BaseValidatorModel):
    eventId: str
    ResponseMetadata: ResponseMetadata


class CreateInstanceResponse(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


class DeleteInstanceResponse(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


class GetInstanceResponse(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


class ListInstancesResponse(BaseValidatorModel):
    instances: List[Instance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateInstanceResponse(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


class DataIntegrationFlowDatasetSourceConfiguration(BaseValidatorModel):
    datasetIdentifier: str
    options: Optional[DataIntegrationFlowDatasetOptions] = None


class DataIntegrationFlowDatasetTargetConfiguration(BaseValidatorModel):
    datasetIdentifier: str
    options: Optional[DataIntegrationFlowDatasetOptions] = None


class DataIntegrationFlowS3SourceConfiguration(BaseValidatorModel):
    bucketName: str
    prefix: str
    options: Optional[DataIntegrationFlowS3Options] = None


class DataIntegrationFlowS3TargetConfiguration(BaseValidatorModel):
    bucketName: str
    prefix: str
    options: Optional[DataIntegrationFlowS3Options] = None


class DataIntegrationFlowTransformation(BaseValidatorModel):
    transformationType: DataIntegrationFlowTransformationTypeType
    sqlTransformation: Optional[DataIntegrationFlowSQLTransformationConfiguration] = None


class DataLakeDatasetSchemaField(BaseValidatorModel):
    pass


class DataLakeDatasetSchemaOutput(BaseValidatorModel):
    name: str
    fields: List[DataLakeDatasetSchemaField]


class DataLakeDatasetSchema(BaseValidatorModel):
    name: str
    fields: Sequence[DataLakeDatasetSchemaField]


class ListDataIntegrationFlowsRequestPaginate(BaseValidatorModel):
    instanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataLakeDatasetsRequestPaginate(BaseValidatorModel):
    instanceId: str
    namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    instanceNameFilter: Optional[Sequence[str]] = None
    instanceStateFilter: Optional[Sequence[InstanceStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class SendDataIntegrationEventRequest(BaseValidatorModel):
    instanceId: str
    eventType: DataIntegrationEventTypeType
    data: str
    eventGroupId: str
    eventTimestamp: Optional[Timestamp] = None
    clientToken: Optional[str] = None


class DataIntegrationFlowSource(BaseValidatorModel):
    sourceType: DataIntegrationFlowSourceTypeType
    sourceName: str
    s3Source: Optional[DataIntegrationFlowS3SourceConfiguration] = None
    datasetSource: Optional[DataIntegrationFlowDatasetSourceConfiguration] = None


class DataIntegrationFlowTarget(BaseValidatorModel):
    targetType: DataIntegrationFlowTargetTypeType
    s3Target: Optional[DataIntegrationFlowS3TargetConfiguration] = None
    datasetTarget: Optional[DataIntegrationFlowDatasetTargetConfiguration] = None


class DataLakeDataset(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    arn: str
    schema: DataLakeDatasetSchemaOutput
    createdTime: datetime
    lastModifiedTime: datetime
    description: Optional[str] = None


class CreateDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str
    sources: Sequence[DataIntegrationFlowSource]
    transformation: DataIntegrationFlowTransformation
    target: DataIntegrationFlowTarget
    tags: Optional[Mapping[str, str]] = None


class DataIntegrationFlow(BaseValidatorModel):
    instanceId: str
    name: str
    sources: List[DataIntegrationFlowSource]
    transformation: DataIntegrationFlowTransformation
    target: DataIntegrationFlowTarget
    createdTime: datetime
    lastModifiedTime: datetime


class UpdateDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str
    sources: Optional[Sequence[DataIntegrationFlowSource]] = None
    transformation: Optional[DataIntegrationFlowTransformation] = None
    target: Optional[DataIntegrationFlowTarget] = None


class CreateDataLakeDatasetResponse(BaseValidatorModel):
    dataset: DataLakeDataset
    ResponseMetadata: ResponseMetadata


class GetDataLakeDatasetResponse(BaseValidatorModel):
    dataset: DataLakeDataset
    ResponseMetadata: ResponseMetadata


class ListDataLakeDatasetsResponse(BaseValidatorModel):
    datasets: List[DataLakeDataset]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateDataLakeDatasetResponse(BaseValidatorModel):
    dataset: DataLakeDataset
    ResponseMetadata: ResponseMetadata


class DataLakeDatasetSchemaUnion(BaseValidatorModel):
    pass


class CreateDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    schema: Optional[DataLakeDatasetSchemaUnion] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetDataIntegrationFlowResponse(BaseValidatorModel):
    flow: DataIntegrationFlow
    ResponseMetadata: ResponseMetadata


class ListDataIntegrationFlowsResponse(BaseValidatorModel):
    flows: List[DataIntegrationFlow]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateDataIntegrationFlowResponse(BaseValidatorModel):
    flow: DataIntegrationFlow
    ResponseMetadata: ResponseMetadata


