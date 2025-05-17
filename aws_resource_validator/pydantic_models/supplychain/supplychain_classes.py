from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.supplychain.supplychain_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BillOfMaterialsImportJob(BaseValidatorModel):
    instanceId: str
    jobId: str
    status: ConfigurationJobStatusType
    s3uri: str
    message: Optional[str] = None


# This class is the input for the 'create_bill_of_materials_import_job' function.
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


# This class is the input for the 'create_instance' function.
class CreateInstanceRequest(BaseValidatorModel):
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    webAppDnsDomain: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
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


class DataLakeDatasetSchemaField(BaseValidatorModel):
    name: str
    type: DataLakeDatasetSchemaFieldTypeType
    isRequired: bool


# This class is the input for the 'delete_data_integration_flow' function.
class DeleteDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str


# This class is the input for the 'delete_data_lake_dataset' function.
class DeleteDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str


# This class is the input for the 'delete_instance' function.
class DeleteInstanceRequest(BaseValidatorModel):
    instanceId: str


# This class is the input for the 'get_bill_of_materials_import_job' function.
class GetBillOfMaterialsImportJobRequest(BaseValidatorModel):
    instanceId: str
    jobId: str


# This class is the input for the 'get_data_integration_flow' function.
class GetDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str


# This class is the input for the 'get_data_lake_dataset' function.
class GetDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str


# This class is the input for the 'get_instance' function.
class GetInstanceRequest(BaseValidatorModel):
    instanceId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_data_integration_flows' function.
class ListDataIntegrationFlowsRequest(BaseValidatorModel):
    instanceId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_data_lake_datasets' function.
class ListDataLakeDatasetsRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_instances' function.
class ListInstancesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    instanceNameFilter: Optional[List[str]] = None
    instanceStateFilter: Optional[List[InstanceStateType]] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str

Timestamp = Union[datetime, str]


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_data_lake_dataset' function.
class UpdateDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    description: Optional[str] = None


# This class is the input for the 'update_instance' function.
class UpdateInstanceRequest(BaseValidatorModel):
    instanceId: str
    instanceName: Optional[str] = None
    instanceDescription: Optional[str] = None


# This class is the output for the 'create_bill_of_materials_import_job' function.
class CreateBillOfMaterialsImportJobResponse(BaseValidatorModel):
    jobId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_integration_flow' function.
class CreateDataIntegrationFlowResponse(BaseValidatorModel):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_data_integration_flow' function.
class DeleteDataIntegrationFlowResponse(BaseValidatorModel):
    instanceId: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_data_lake_dataset' function.
class DeleteDataLakeDatasetResponse(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bill_of_materials_import_job' function.
class GetBillOfMaterialsImportJobResponse(BaseValidatorModel):
    job: BillOfMaterialsImportJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_data_integration_event' function.
class SendDataIntegrationEventResponse(BaseValidatorModel):
    eventId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_instance' function.
class CreateInstanceResponse(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_instance' function.
class DeleteInstanceResponse(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance' function.
class GetInstanceResponse(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instances' function.
class ListInstancesResponse(BaseValidatorModel):
    instances: List[Instance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_instance' function.
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


class DataLakeDatasetSchemaOutput(BaseValidatorModel):
    name: str
    fields: List[DataLakeDatasetSchemaField]


class DataLakeDatasetSchema(BaseValidatorModel):
    name: str
    fields: List[DataLakeDatasetSchemaField]


class ListDataIntegrationFlowsRequestPaginate(BaseValidatorModel):
    instanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataLakeDatasetsRequestPaginate(BaseValidatorModel):
    instanceId: str
    namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    instanceNameFilter: Optional[List[str]] = None
    instanceStateFilter: Optional[List[InstanceStateType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'send_data_integration_event' function.
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

DataLakeDatasetSchemaUnion = Union[DataLakeDatasetSchema, DataLakeDatasetSchemaOutput]


# This class is the input for the 'create_data_integration_flow' function.
class CreateDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str
    sources: List[DataIntegrationFlowSource]
    transformation: DataIntegrationFlowTransformation
    target: DataIntegrationFlowTarget
    tags: Optional[Dict[str, str]] = None


class DataIntegrationFlow(BaseValidatorModel):
    instanceId: str
    name: str
    sources: List[DataIntegrationFlowSource]
    transformation: DataIntegrationFlowTransformation
    target: DataIntegrationFlowTarget
    createdTime: datetime
    lastModifiedTime: datetime


# This class is the input for the 'update_data_integration_flow' function.
class UpdateDataIntegrationFlowRequest(BaseValidatorModel):
    instanceId: str
    name: str
    sources: Optional[List[DataIntegrationFlowSource]] = None
    transformation: Optional[DataIntegrationFlowTransformation] = None
    target: Optional[DataIntegrationFlowTarget] = None


# This class is the output for the 'create_data_lake_dataset' function.
class CreateDataLakeDatasetResponse(BaseValidatorModel):
    dataset: DataLakeDataset
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_lake_dataset' function.
class GetDataLakeDatasetResponse(BaseValidatorModel):
    dataset: DataLakeDataset
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_lake_datasets' function.
class ListDataLakeDatasetsResponse(BaseValidatorModel):
    datasets: List[DataLakeDataset]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_data_lake_dataset' function.
class UpdateDataLakeDatasetResponse(BaseValidatorModel):
    dataset: DataLakeDataset
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_data_lake_dataset' function.
class CreateDataLakeDatasetRequest(BaseValidatorModel):
    instanceId: str
    namespace: str
    name: str
    schema: Optional[DataLakeDatasetSchemaUnion] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_data_integration_flow' function.
class GetDataIntegrationFlowResponse(BaseValidatorModel):
    flow: DataIntegrationFlow
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_integration_flows' function.
class ListDataIntegrationFlowsResponse(BaseValidatorModel):
    flows: List[DataIntegrationFlow]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_data_integration_flow' function.
class UpdateDataIntegrationFlowResponse(BaseValidatorModel):
    flow: DataIntegrationFlow
    ResponseMetadata: ResponseMetadata