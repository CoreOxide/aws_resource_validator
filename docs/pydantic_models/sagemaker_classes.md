# Sagemaker Classes

# ActionSourceTypeDef

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### SourceId
- **Type**: typing.Optional[str]


# ActionSummaryTypeDef

### ActionArn
- **Type**: typing.Optional[str]

### ActionName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ActionSourceTypeDef]

### ActionType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# AddAssociationRequestTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]


# AddAssociationResponseTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]
- **Required**: Yes


# AddTagsOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdditionalInferenceSpecificationDefinitionOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageContainerDefinitionOutputTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# AdditionalInferenceSpecificationDefinitionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Containers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageContainerDefinitionUnionTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.Sequence[str]]


# AdditionalInferenceSpecificationDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AdditionalModelDataSourceTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### S3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.S3ModelDataSourceTypeDef'>
- **Required**: Yes


# AdditionalS3DataSourceTypeDef

### S3DataType
- **Type**: typing.Literal['S3Object', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### ETag
- **Type**: typing.Optional[str]


# AgentVersionTypeDef

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### AgentCount
- **Type**: <class 'int'>
- **Required**: Yes


# AlarmTypeDef

### AlarmName
- **Type**: typing.Optional[str]


# AlgorithmSpecificationOutputTypeDef

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDefinitionTypeDef]]

### EnableSageMakerMetricsTimeSeries
- **Type**: typing.Optional[bool]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### TrainingImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingImageConfigTypeDef]


# AlgorithmSpecificationTypeDef

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDefinitionTypeDef]]

### EnableSageMakerMetricsTimeSeries
- **Type**: typing.Optional[bool]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.Sequence[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### TrainingImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingImageConfigTypeDef]


# AlgorithmSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlgorithmStatusDetailsTypeDef

### ValidationStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmStatusItemTypeDef]]

### ImageScanStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmStatusItemTypeDef]]


# AlgorithmStatusItemTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'NotStarted']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# AlgorithmSummaryTypeDef

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlgorithmStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### AlgorithmDescription
- **Type**: typing.Optional[str]


# AlgorithmValidationProfileOutputTypeDef

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobDefinitionOutputTypeDef'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobDefinitionOutputTypeDef]


# AlgorithmValidationProfileTypeDef

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobDefinitionTypeDef'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobDefinitionTypeDef]


# AlgorithmValidationSpecificationOutputTypeDef

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmValidationProfileOutputTypeDef]
- **Required**: Yes


# AlgorithmValidationSpecificationTypeDef

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmValidationProfileTypeDef]
- **Required**: Yes


# AlgorithmValidationSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AmazonQSettingsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### QProfileArn
- **Type**: typing.Optional[str]


# AnnotationConsolidationConfigTypeDef

### AnnotationConsolidationLambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# AppDetailsTypeDef

### DomainId
- **Type**: typing.Optional[str]

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### AppName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Deleted', 'Deleting', 'Failed', 'InService', 'Pending']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]


# AppImageConfigDetailsTypeDef

### AppImageConfigArn
- **Type**: typing.Optional[str]

### AppImageConfigName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### KernelGatewayImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayImageConfigOutputTypeDef]

### JupyterLabAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppImageConfigOutputTypeDef]

### CodeEditorAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CodeEditorAppImageConfigOutputTypeDef]


# AppLifecycleManagementTypeDef

### IdleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.IdleSettingsTypeDef]


# AppSpecificationOutputTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]


# AppSpecificationTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.Sequence[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.Sequence[str]]


# AppSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ArtifactSourceOutputTypeDef

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ArtifactSourceTypeTypeDef]]


# ArtifactSourceTypeDef

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceTypes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ArtifactSourceTypeTypeDef]]


# ArtifactSourceTypeTypeDef

### SourceIdType
- **Type**: typing.Literal['Custom', 'MD5Hash', 'S3ETag', 'S3Version']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ArtifactSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ArtifactSummaryTypeDef

### ArtifactArn
- **Type**: typing.Optional[str]

### ArtifactName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ArtifactSourceOutputTypeDef]

### ArtifactType
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# AssociateTrialComponentRequestTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateTrialComponentResponseTypeDef

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociationSummaryTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### DestinationType
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]

### SourceName
- **Type**: typing.Optional[str]

### DestinationName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]


# AsyncInferenceClientConfigTypeDef

### MaxConcurrentInvocationsPerInstance
- **Type**: typing.Optional[int]


# AsyncInferenceConfigOutputTypeDef

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceOutputConfigOutputTypeDef'>
- **Required**: Yes

### ClientConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceClientConfigTypeDef]


# AsyncInferenceConfigTypeDef

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceOutputConfigTypeDef'>
- **Required**: Yes

### ClientConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceClientConfigTypeDef]


# AsyncInferenceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AsyncInferenceNotificationConfigOutputTypeDef

### SuccessTopic
- **Type**: typing.Optional[str]

### ErrorTopic
- **Type**: typing.Optional[str]

### IncludeInferenceResponseIn
- **Type**: typing.Optional[typing.List[typing.Literal['ERROR_NOTIFICATION_TOPIC', 'SUCCESS_NOTIFICATION_TOPIC']]]


# AsyncInferenceNotificationConfigTypeDef

### SuccessTopic
- **Type**: typing.Optional[str]

### ErrorTopic
- **Type**: typing.Optional[str]

### IncludeInferenceResponseIn
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ERROR_NOTIFICATION_TOPIC', 'SUCCESS_NOTIFICATION_TOPIC']]]


# AsyncInferenceOutputConfigOutputTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceNotificationConfigOutputTypeDef]

### S3FailurePath
- **Type**: typing.Optional[str]


# AsyncInferenceOutputConfigTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### NotificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceNotificationConfigTypeDef]

### S3FailurePath
- **Type**: typing.Optional[str]


# AthenaDatasetDefinitionTypeDef

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Literal['AVRO', 'JSON', 'ORC', 'PARQUET', 'TEXTFILE']
- **Required**: Yes

### WorkGroup
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### OutputCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'SNAPPY', 'ZLIB']]


# AutoMLAlgorithmConfigOutputTypeDef

### AutoMLAlgorithms
- **Type**: typing.List[typing.Literal['arima', 'catboost', 'cnn-qr', 'deepar', 'ets', 'extra-trees', 'fastai', 'lightgbm', 'linear-learner', 'mlp', 'nn-torch', 'npts', 'prophet', 'randomforest', 'xgboost']]
- **Required**: Yes


# AutoMLAlgorithmConfigTypeDef

### AutoMLAlgorithms
- **Type**: typing.Sequence[typing.Literal['arima', 'catboost', 'cnn-qr', 'deepar', 'ets', 'extra-trees', 'fastai', 'lightgbm', 'linear-learner', 'mlp', 'nn-torch', 'npts', 'prophet', 'randomforest', 'xgboost']]
- **Required**: Yes


# AutoMLCandidateGenerationConfigOutputTypeDef

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### AlgorithmsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLAlgorithmConfigOutputTypeDef]]


# AutoMLCandidateGenerationConfigTypeDef

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### AlgorithmsConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLAlgorithmConfigTypeDef]]


# AutoMLCandidateStepTypeDef

### CandidateStepType
- **Type**: typing.Literal['AWS::SageMaker::ProcessingJob', 'AWS::SageMaker::TrainingJob', 'AWS::SageMaker::TransformJob']
- **Required**: Yes

### CandidateStepArn
- **Type**: <class 'str'>
- **Required**: Yes

### CandidateStepName
- **Type**: <class 'str'>
- **Required**: Yes


# AutoMLCandidateTypeDef

### CandidateName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectiveStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Succeeded']
- **Required**: Yes

### CandidateSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLCandidateStepTypeDef]
- **Required**: Yes

### CandidateStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FinalAutoMLJobObjectiveMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FinalAutoMLJobObjectiveMetricTypeDef]

### InferenceContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLContainerDefinitionTypeDef]]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### CandidateProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CandidatePropertiesTypeDef]

### InferenceContainerDefinitions
- **Type**: typing.Optional[typing.Dict[typing.Literal['CPU', 'GPU'], typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLContainerDefinitionTypeDef]]]


# AutoMLChannelTypeDef

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLDataSourceTypeDef]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### ContentType
- **Type**: typing.Optional[str]

### ChannelType
- **Type**: typing.Optional[typing.Literal['training', 'validation']]

### SampleWeightAttributeName
- **Type**: typing.Optional[str]


# AutoMLComputeConfigTypeDef

### EmrServerlessComputeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EmrServerlessComputeConfigTypeDef]


# AutoMLContainerDefinitionTypeDef

### Image
- **Type**: <class 'str'>
- **Required**: Yes

### ModelDataUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# AutoMLDataSourceTypeDef

### S3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLS3DataSourceTypeDef'>
- **Required**: Yes


# AutoMLDataSplitConfigTypeDef

### ValidationFraction
- **Type**: typing.Optional[float]


# AutoMLJobArtifactsTypeDef

### CandidateDefinitionNotebookLocation
- **Type**: typing.Optional[str]

### DataExplorationNotebookLocation
- **Type**: typing.Optional[str]


# AutoMLJobChannelTypeDef

### ChannelType
- **Type**: typing.Optional[typing.Literal['training', 'validation']]

### ContentType
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLDataSourceTypeDef]


# AutoMLJobCompletionCriteriaTypeDef

### MaxCandidates
- **Type**: typing.Optional[int]

### MaxRuntimePerTrainingJobInSeconds
- **Type**: typing.Optional[int]

### MaxAutoMLJobRuntimeInSeconds
- **Type**: typing.Optional[int]


# AutoMLJobConfigOutputTypeDef

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLSecurityConfigOutputTypeDef]

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLCandidateGenerationConfigOutputTypeDef]

### DataSplitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLDataSplitConfigTypeDef]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]


# AutoMLJobConfigTypeDef

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLSecurityConfigTypeDef]

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLCandidateGenerationConfigTypeDef]

### DataSplitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLDataSplitConfigTypeDef]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]


# AutoMLJobConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoMLJobObjectiveTypeDef

### MetricName
- **Type**: typing.Literal['AUC', 'Accuracy', 'AverageWeightedQuantileLoss', 'BalancedAccuracy', 'F1', 'F1macro', 'MAE', 'MAPE', 'MASE', 'MSE', 'Precision', 'PrecisionMacro', 'R2', 'RMSE', 'Recall', 'RecallMacro', 'WAPE']
- **Required**: Yes


# AutoMLJobStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# AutoMLJobSummaryTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### AutoMLJobSecondaryStatus
- **Type**: typing.Literal['AnalyzingData', 'CandidateDefinitionsGenerated', 'Completed', 'DeployingModel', 'ExplainabilityError', 'Failed', 'FeatureEngineering', 'GeneratingExplainabilityReport', 'GeneratingModelInsightsReport', 'MaxAutoMLJobRuntimeReached', 'MaxCandidatesReached', 'ModelDeploymentError', 'ModelInsightsError', 'ModelTuning', 'PreTraining', 'Starting', 'Stopped', 'Stopping', 'TrainingModels']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### PartialFailureReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLPartialFailureReasonTypeDef]]


# AutoMLOutputDataConfigTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# AutoMLPartialFailureReasonTypeDef

### PartialFailureMessage
- **Type**: typing.Optional[str]


# AutoMLProblemTypeConfigOutputTypeDef

### ImageClassificationJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ImageClassificationJobConfigTypeDef]

### TextClassificationJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TextClassificationJobConfigTypeDef]

### TimeSeriesForecastingJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesForecastingJobConfigOutputTypeDef]

### TabularJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TabularJobConfigOutputTypeDef]

### TextGenerationJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TextGenerationJobConfigOutputTypeDef]


# AutoMLProblemTypeConfigTypeDef

### ImageClassificationJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ImageClassificationJobConfigTypeDef]

### TextClassificationJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TextClassificationJobConfigTypeDef]

### TimeSeriesForecastingJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesForecastingJobConfigTypeDef]

### TabularJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TabularJobConfigTypeDef]

### TextGenerationJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TextGenerationJobConfigTypeDef]


# AutoMLProblemTypeConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoMLProblemTypeResolvedAttributesTypeDef

### TabularResolvedAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TabularResolvedAttributesTypeDef]

### TextGenerationResolvedAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TextGenerationResolvedAttributesTypeDef]


# AutoMLResolvedAttributesTypeDef

### AutoMLJobObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobObjectiveTypeDef]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### AutoMLProblemTypeResolvedAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLProblemTypeResolvedAttributesTypeDef]


# AutoMLS3DataSourceTypeDef

### S3DataType
- **Type**: typing.Literal['AugmentedManifestFile', 'ManifestFile', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# AutoMLSecurityConfigOutputTypeDef

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]


# AutoMLSecurityConfigTypeDef

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigTypeDef]


# AutoMLSecurityConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ValueHint
- **Type**: <class 'str'>
- **Required**: Yes


# AutoRollbackConfigOutputTypeDef

### Alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AlarmTypeDef]]


# AutoRollbackConfigTypeDef

### Alarms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AlarmTypeDef]]


# AutotuneTypeDef

### Mode
- **Type**: typing.Literal['Enabled']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDataCaptureConfigTypeDef

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### GenerateInferenceId
- **Type**: typing.Optional[bool]


# BatchDeleteClusterNodesErrorTypeDef

### Code
- **Type**: typing.Literal['InvalidNodeStatus', 'NodeIdInUse', 'NodeIdNotFound']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteClusterNodesRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteClusterNodesResponseTypeDef

### Failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.BatchDeleteClusterNodesErrorTypeDef]
- **Required**: Yes

### Successful
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDescribeModelPackageErrorTypeDef

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorResponse
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDescribeModelPackageInputTypeDef

### ModelPackageArnList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDescribeModelPackageOutputTypeDef

### ModelPackageSummaries
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.BatchDescribeModelPackageSummaryTypeDef]
- **Required**: Yes

### BatchDescribeModelPackageErrorMap
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.BatchDescribeModelPackageErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDescribeModelPackageSummaryTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceSpecificationOutputTypeDef'>
- **Required**: Yes

### ModelPackageStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageVersion
- **Type**: typing.Optional[int]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]


# BatchTransformInputOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchTransformInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BestObjectiveNotImprovingTypeDef

### MaxNumberOfTrainingJobsNotImproving
- **Type**: typing.Optional[int]


# BiasTypeDef

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### PreTrainingReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### PostTrainingReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]


# BlueGreenUpdatePolicyTypeDef

### TrafficRoutingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrafficRoutingConfigTypeDef'>
- **Required**: Yes

### TerminationWaitInSeconds
- **Type**: typing.Optional[int]

### MaximumExecutionTimeoutInSeconds
- **Type**: typing.Optional[int]


# CacheHitResultTypeDef

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# CallbackStepMetadataTypeDef

### CallbackToken
- **Type**: typing.Optional[str]

### SqsQueueUrl
- **Type**: typing.Optional[str]

### OutputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.OutputParameterTypeDef]]


# CandidateArtifactLocationsTypeDef

### Explainability
- **Type**: <class 'str'>
- **Required**: Yes

### ModelInsights
- **Type**: typing.Optional[str]

### BacktestResults
- **Type**: typing.Optional[str]


# CandidateGenerationConfigOutputTypeDef

### AlgorithmsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLAlgorithmConfigOutputTypeDef]]


# CandidateGenerationConfigTypeDef

### AlgorithmsConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLAlgorithmConfigTypeDef]]


# CandidatePropertiesTypeDef

### CandidateArtifactLocations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CandidateArtifactLocationsTypeDef]

### CandidateMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDatumTypeDef]]


# CanvasAppSettingsOutputTypeDef

### TimeSeriesForecastingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesForecastingSettingsTypeDef]

### ModelRegisterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelRegisterSettingsTypeDef]

### WorkspaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkspaceSettingsTypeDef]

### IdentityProviderOAuthSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.IdentityProviderOAuthSettingTypeDef]]

### DirectDeploySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DirectDeploySettingsTypeDef]

### KendraSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KendraSettingsTypeDef]

### GenerativeAiSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.GenerativeAiSettingsTypeDef]

### EmrServerlessSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EmrServerlessSettingsTypeDef]


# CanvasAppSettingsTypeDef

### TimeSeriesForecastingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesForecastingSettingsTypeDef]

### ModelRegisterSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelRegisterSettingsTypeDef]

### WorkspaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkspaceSettingsTypeDef]

### IdentityProviderOAuthSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.IdentityProviderOAuthSettingTypeDef]]

### DirectDeploySettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DirectDeploySettingsTypeDef]

### KendraSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KendraSettingsTypeDef]

### GenerativeAiSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.GenerativeAiSettingsTypeDef]

### EmrServerlessSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EmrServerlessSettingsTypeDef]


# CapacitySizeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaptureContentTypeHeaderOutputTypeDef

### CsvContentTypes
- **Type**: typing.Optional[typing.List[str]]

### JsonContentTypes
- **Type**: typing.Optional[typing.List[str]]


# CaptureContentTypeHeaderTypeDef

### CsvContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### JsonContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# CaptureOptionTypeDef

### CaptureMode
- **Type**: typing.Literal['Input', 'InputAndOutput', 'Output']
- **Required**: Yes


# CategoricalParameterOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterRangeOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterRangeSpecificationOutputTypeDef

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CategoricalParameterRangeSpecificationTypeDef

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CategoricalParameterRangeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CategoricalParameterRangeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CategoricalParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ChannelOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelSpecificationOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedContentTypes
- **Type**: typing.List[str]
- **Required**: Yes

### SupportedInputModes
- **Type**: typing.List[typing.Literal['FastFile', 'File', 'Pipe']]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IsRequired
- **Type**: typing.Optional[bool]

### SupportedCompressionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Gzip', 'None']]]


# ChannelSpecificationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedContentTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SupportedInputModes
- **Type**: typing.Sequence[typing.Literal['FastFile', 'File', 'Pipe']]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IsRequired
- **Type**: typing.Optional[bool]

### SupportedCompressionTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Gzip', 'None']]]


# ChannelTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CheckpointConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]


# ClarifyCheckStepMetadataTypeDef

### CheckType
- **Type**: typing.Optional[str]

### BaselineUsedForDriftCheckConstraints
- **Type**: typing.Optional[str]

### CalculatedBaselineConstraints
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ViolationReport
- **Type**: typing.Optional[str]

### CheckJobArn
- **Type**: typing.Optional[str]

### SkipCheck
- **Type**: typing.Optional[bool]

### RegisterNewBaseline
- **Type**: typing.Optional[bool]


# ClarifyExplainerConfigOutputTypeDef

### ShapConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyShapConfigTypeDef'>
- **Required**: Yes

### EnableExplanations
- **Type**: typing.Optional[str]

### InferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyInferenceConfigOutputTypeDef]


# ClarifyExplainerConfigTypeDef

### ShapConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyShapConfigTypeDef'>
- **Required**: Yes

### EnableExplanations
- **Type**: typing.Optional[str]

### InferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyInferenceConfigTypeDef]


# ClarifyInferenceConfigOutputTypeDef

### FeaturesAttribute
- **Type**: typing.Optional[str]

### ContentTemplate
- **Type**: typing.Optional[str]

### MaxRecordCount
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### ProbabilityIndex
- **Type**: typing.Optional[int]

### LabelIndex
- **Type**: typing.Optional[int]

### ProbabilityAttribute
- **Type**: typing.Optional[str]

### LabelAttribute
- **Type**: typing.Optional[str]

### LabelHeaders
- **Type**: typing.Optional[typing.List[str]]

### FeatureHeaders
- **Type**: typing.Optional[typing.List[str]]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['categorical', 'numerical', 'text']]]


# ClarifyInferenceConfigTypeDef

### FeaturesAttribute
- **Type**: typing.Optional[str]

### ContentTemplate
- **Type**: typing.Optional[str]

### MaxRecordCount
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### ProbabilityIndex
- **Type**: typing.Optional[int]

### LabelIndex
- **Type**: typing.Optional[int]

### ProbabilityAttribute
- **Type**: typing.Optional[str]

### LabelAttribute
- **Type**: typing.Optional[str]

### LabelHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### FeatureHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### FeatureTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['categorical', 'numerical', 'text']]]


# ClarifyShapBaselineConfigTypeDef

### MimeType
- **Type**: typing.Optional[str]

### ShapBaseline
- **Type**: typing.Optional[str]

### ShapBaselineUri
- **Type**: typing.Optional[str]


# ClarifyShapConfigTypeDef

### ShapBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyShapBaselineConfigTypeDef'>
- **Required**: Yes

### NumberOfSamples
- **Type**: typing.Optional[int]

### UseLogit
- **Type**: typing.Optional[bool]

### Seed
- **Type**: typing.Optional[int]

### TextConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyTextConfigTypeDef]


# ClarifyTextConfigTypeDef

### Language
- **Type**: typing.Literal['af', 'ar', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'ga', 'gu', 'he', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'kn', 'ky', 'lb', 'lij', 'lt', 'lv', 'mk', 'ml', 'mr', 'nb', 'ne', 'nl', 'pl', 'pt', 'ro', 'ru', 'sa', 'si', 'sk', 'sl', 'sq', 'sr', 'sv', 'ta', 'te', 'tl', 'tn', 'tr', 'tt', 'uk', 'ur', 'xx', 'yo', 'zh']
- **Required**: Yes

### Granularity
- **Type**: typing.Literal['paragraph', 'sentence', 'token']
- **Required**: Yes


# ClusterEbsVolumeConfigTypeDef

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes


# ClusterInstanceGroupDetailsTypeDef

### CurrentCount
- **Type**: typing.Optional[int]

### TargetCount
- **Type**: typing.Optional[int]

### InstanceGroupName
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### LifeCycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterLifeCycleConfigTypeDef]

### ExecutionRole
- **Type**: typing.Optional[str]

### ThreadsPerCore
- **Type**: typing.Optional[int]

### InstanceStorageConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceStorageConfigTypeDef]]

### OnStartDeepHealthChecks
- **Type**: typing.Optional[typing.List[typing.Literal['InstanceConnectivity', 'InstanceStress']]]

### Status
- **Type**: typing.Optional[typing.Literal['Creating', 'Degraded', 'Deleting', 'Failed', 'InService', 'SystemUpdating', 'Updating']]

### TrainingPlanArn
- **Type**: typing.Optional[str]

### TrainingPlanStatus
- **Type**: typing.Optional[str]

### OverrideVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]


# ClusterInstanceGroupSpecificationTypeDef

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### LifeCycleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClusterLifeCycleConfigTypeDef'>
- **Required**: Yes

### ExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes

### ThreadsPerCore
- **Type**: typing.Optional[int]

### InstanceStorageConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceStorageConfigTypeDef]]

### OnStartDeepHealthChecks
- **Type**: typing.Optional[typing.Sequence[typing.Literal['InstanceConnectivity', 'InstanceStress']]]

### TrainingPlanArn
- **Type**: typing.Optional[str]

### OverrideVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigUnionTypeDef]


# ClusterInstancePlacementTypeDef

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]


# ClusterInstanceStatusDetailsTypeDef

### Status
- **Type**: typing.Literal['DeepHealthCheckInProgress', 'Failure', 'Pending', 'Running', 'ShuttingDown', 'SystemUpdating']
- **Required**: Yes

### Message
- **Type**: typing.Optional[str]


# ClusterInstanceStorageConfigTypeDef

### EbsVolumeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterEbsVolumeConfigTypeDef]


# ClusterLifeCycleConfigTypeDef

### SourceS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterNodeDetailsTypeDef

### InstanceGroupName
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceStatusDetailsTypeDef]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### LaunchTime
- **Type**: typing.Optional[datetime.datetime]

### LifeCycleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterLifeCycleConfigTypeDef]

### OverrideVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]

### ThreadsPerCore
- **Type**: typing.Optional[int]

### InstanceStorageConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceStorageConfigTypeDef]]

### PrivatePrimaryIp
- **Type**: typing.Optional[str]

### PrivatePrimaryIpv6
- **Type**: typing.Optional[str]

### PrivateDnsHostname
- **Type**: typing.Optional[str]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstancePlacementTypeDef]


# ClusterNodeSummaryTypeDef

### InstanceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### LaunchTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InstanceStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceStatusDetailsTypeDef'>
- **Required**: Yes


# ClusterOrchestratorEksConfigTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterOrchestratorTypeDef

### Eks
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClusterOrchestratorEksConfigTypeDef'>
- **Required**: Yes


# ClusterSchedulerConfigSummaryTypeDef

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: typing.Optional[int]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### ClusterArn
- **Type**: typing.Optional[str]


# ClusterSummaryTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ClusterStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'RollingBack', 'SystemUpdating', 'Updating']
- **Required**: Yes

### TrainingPlanArns
- **Type**: typing.Optional[typing.List[str]]


# CodeEditorAppImageConfigOutputTypeDef

### FileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemConfigTypeDef]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerConfigOutputTypeDef]


# CodeEditorAppImageConfigTypeDef

### FileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemConfigTypeDef]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerConfigTypeDef]


# CodeEditorAppImageConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeEditorAppSettingsOutputTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AppLifecycleManagementTypeDef]

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# CodeEditorAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.Sequence[str]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AppLifecycleManagementTypeDef]

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# CodeRepositorySummaryTypeDef

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.GitConfigTypeDef]


# CodeRepositoryTypeDef

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes


# CognitoConfigTypeDef

### UserPool
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# CognitoMemberDefinitionTypeDef

### UserPool
- **Type**: <class 'str'>
- **Required**: Yes

### UserGroup
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# CollectionConfigTypeDef

### VectorConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VectorConfigTypeDef]


# CollectionConfigurationOutputTypeDef

### CollectionName
- **Type**: typing.Optional[str]

### CollectionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CollectionConfigurationTypeDef

### CollectionName
- **Type**: typing.Optional[str]

### CollectionParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CompilationJobSummaryTypeDef

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompilationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CompilationStartTime
- **Type**: typing.Optional[datetime.datetime]

### CompilationEndTime
- **Type**: typing.Optional[datetime.datetime]

### CompilationTargetDevice
- **Type**: typing.Optional[typing.Literal['aisage', 'amba_cv2', 'amba_cv22', 'amba_cv25', 'coreml', 'deeplens', 'imx8mplus', 'imx8qm', 'jacinto_tda4vm', 'jetson_nano', 'jetson_tx1', 'jetson_tx2', 'jetson_xavier', 'lambda', 'ml_c4', 'ml_c5', 'ml_c6g', 'ml_eia2', 'ml_g4dn', 'ml_inf1', 'ml_inf2', 'ml_m4', 'ml_m5', 'ml_m6g', 'ml_p2', 'ml_p3', 'ml_trn1', 'qcs603', 'qcs605', 'rasp3b', 'rasp4b', 'rk3288', 'rk3399', 'sbe_c', 'sitara_am57x', 'x86_win32', 'x86_win64']]

### CompilationTargetPlatformOs
- **Type**: typing.Optional[typing.Literal['ANDROID', 'LINUX']]

### CompilationTargetPlatformArch
- **Type**: typing.Optional[typing.Literal['ARM64', 'ARM_EABI', 'ARM_EABIHF', 'X86', 'X86_64']]

### CompilationTargetPlatformAccelerator
- **Type**: typing.Optional[typing.Literal['INTEL_GRAPHICS', 'MALI', 'NNA', 'NVIDIA']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ComputeQuotaConfigOutputTypeDef

### ComputeQuotaResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaResourceConfigTypeDef]]

### ResourceSharingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSharingConfigTypeDef]

### PreemptTeamTasks
- **Type**: typing.Optional[typing.Literal['LowerPriority', 'Never']]


# ComputeQuotaConfigTypeDef

### ComputeQuotaResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaResourceConfigTypeDef]]

### ResourceSharingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSharingConfigTypeDef]

### PreemptTeamTasks
- **Type**: typing.Optional[typing.Literal['LowerPriority', 'Never']]


# ComputeQuotaConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComputeQuotaResourceConfigTypeDef

### InstanceType
- **Type**: typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.large', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.gr6.4xlarge', 'ml.gr6.8xlarge', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes


# ComputeQuotaSummaryTypeDef

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### ComputeQuotaTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaTargetTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: typing.Optional[int]

### ClusterArn
- **Type**: typing.Optional[str]

### ComputeQuotaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaConfigOutputTypeDef]

### ActivationState
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ComputeQuotaTargetTypeDef

### TeamName
- **Type**: <class 'str'>
- **Required**: Yes

### FairShareWeight
- **Type**: typing.Optional[int]


# ConditionStepMetadataTypeDef

### Outcome
- **Type**: typing.Optional[typing.Literal['False', 'True']]


# ContainerConfigOutputTypeDef

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerEnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# ContainerConfigTypeDef

### ContainerArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### ContainerEntrypoint
- **Type**: typing.Optional[typing.Sequence[str]]

### ContainerEnvironmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ContainerDefinitionOutputTypeDef

### ContainerHostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ImageConfigTypeDef]

### Mode
- **Type**: typing.Optional[typing.Literal['MultiModel', 'SingleModel']]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDataSourceTypeDef]

### AdditionalModelDataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalModelDataSourceTypeDef]]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelPackageName
- **Type**: typing.Optional[str]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### MultiModelConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MultiModelConfigTypeDef]


# ContainerDefinitionTypeDef

### ContainerHostname
- **Type**: typing.Optional[str]

### Image
- **Type**: typing.Optional[str]

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ImageConfigTypeDef]

### Mode
- **Type**: typing.Optional[typing.Literal['MultiModel', 'SingleModel']]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDataSourceTypeDef]

### AdditionalModelDataSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalModelDataSourceTypeDef]]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ModelPackageName
- **Type**: typing.Optional[str]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### MultiModelConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MultiModelConfigTypeDef]


# ContainerDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContextSourceTypeDef

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]

### SourceId
- **Type**: typing.Optional[str]


# ContextSummaryTypeDef

### ContextArn
- **Type**: typing.Optional[str]

### ContextName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContextSourceTypeDef]

### ContextType
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ContinuousParameterRangeSpecificationTypeDef

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes


# ContinuousParameterRangeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Linear', 'Logarithmic', 'ReverseLogarithmic']]


# ConvergenceDetectedTypeDef

### CompleteOnConvergence
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# CreateActionRequestTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ActionSourceTypeDef'>
- **Required**: Yes

### ActionType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateActionResponseTypeDef

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAlgorithmInputTypeDef

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrainingSpecificationUnionTypeDef'>
- **Required**: Yes

### AlgorithmDescription
- **Type**: typing.Optional[str]

### InferenceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceSpecificationUnionTypeDef]

### ValidationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmValidationSpecificationUnionTypeDef]

### CertifyForMarketplace
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateAlgorithmOutputTypeDef

### AlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppImageConfigRequestTypeDef

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### KernelGatewayImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayImageConfigUnionTypeDef]

### JupyterLabAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppImageConfigUnionTypeDef]

### CodeEditorAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CodeEditorAppImageConfigUnionTypeDef]


# CreateAppImageConfigResponseTypeDef

### AppImageConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]


# CreateAppResponseTypeDef

### AppArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateArtifactRequestTypeDef

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ArtifactSourceUnionTypeDef'>
- **Required**: Yes

### ArtifactType
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactName
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateArtifactResponseTypeDef

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAutoMLJobRequestTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLChannelTypeDef]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLOutputDataConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### AutoMLJobObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobObjectiveTypeDef]

### AutoMLJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobConfigUnionTypeDef]

### GenerateCandidateDefinitionsOnly
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ModelDeployConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDeployConfigTypeDef]


# CreateAutoMLJobResponseTypeDef

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAutoMLJobV2RequestTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobInputDataConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobChannelTypeDef]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLOutputDataConfigTypeDef'>
- **Required**: Yes

### AutoMLProblemTypeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLProblemTypeConfigUnionTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLSecurityConfigUnionTypeDef]

### AutoMLJobObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobObjectiveTypeDef]

### ModelDeployConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDeployConfigTypeDef]

### DataSplitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLDataSplitConfigTypeDef]

### AutoMLComputeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLComputeConfigTypeDef]


# CreateAutoMLJobV2ResponseTypeDef

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceGroupSpecificationTypeDef]
- **Required**: Yes

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### Orchestrator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterOrchestratorTypeDef]

### NodeRecovery
- **Type**: typing.Optional[typing.Literal['Automatic', 'None']]


# CreateClusterResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterSchedulerConfigRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchedulerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.SchedulerConfigUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateClusterSchedulerConfigResponseTypeDef

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCodeRepositoryInputTypeDef

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### GitConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.GitConfigTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateCodeRepositoryOutputTypeDef

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCompilationJobRequestTypeDef

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputConfigTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### ModelPackageVersionArn
- **Type**: typing.Optional[str]

### InputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InputConfigTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NeoVpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateCompilationJobResponseTypeDef

### CompilationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateComputeQuotaRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaConfigUnionTypeDef'>
- **Required**: Yes

### ComputeQuotaTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaTargetTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ActivationState
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateComputeQuotaResponseTypeDef

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContextRequestTypeDef

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ContextSourceTypeDef'>
- **Required**: Yes

### ContextType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateContextResponseTypeDef

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataQualityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### DataQualityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataQualityAppSpecificationUnionTypeDef'>
- **Required**: Yes

### DataQualityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataQualityJobInputUnionTypeDef'>
- **Required**: Yes

### DataQualityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigUnionTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataQualityBaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DataQualityBaselineConfigTypeDef]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigUnionTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateDataQualityJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeviceFleetRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeOutputConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### EnableIotRoleAlias
- **Type**: typing.Optional[bool]


# CreateDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthMode
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### DefaultUserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserSettingsUnionTypeDef'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DomainSettingsUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### AppNetworkAccessType
- **Type**: typing.Optional[typing.Literal['PublicInternetOnly', 'VpcOnly']]

### HomeEfsFileSystemKmsKeyId
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### AppSecurityGroupManagement
- **Type**: typing.Optional[typing.Literal['Customer', 'Service']]

### TagPropagation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DefaultSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DefaultSpaceSettingsUnionTypeDef]


# CreateDomainResponseTypeDef

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEdgeDeploymentPlanRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeDeploymentModelConfigTypeDef]
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### Stages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentStageTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateEdgeDeploymentPlanResponseTypeDef

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEdgeDeploymentStageRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Stages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentStageTypeDef]
- **Required**: Yes


# CreateEdgePackagingJobRequestTypeDef

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeOutputConfigTypeDef'>
- **Required**: Yes

### ResourceKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateEndpointConfigInputTypeDef

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantTypeDef]
- **Required**: Yes

### DataCaptureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DataCaptureConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### AsyncInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceConfigUnionTypeDef]

### ExplainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExplainerConfigUnionTypeDef]

### ShadowProductionVariants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantTypeDef]]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigUnionTypeDef]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]


# CreateEndpointConfigOutputTypeDef

### EndpointConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointInputTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateEndpointOutputTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExperimentRequestTypeDef

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateExperimentResponseTypeDef

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFeatureGroupRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTimeFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureDefinitionTypeDef]
- **Required**: Yes

### OnlineStoreConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OnlineStoreConfigTypeDef]

### OfflineStoreConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OfflineStoreConfigTypeDef]

### ThroughputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ThroughputConfigTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateFeatureGroupResponseTypeDef

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlowDefinitionRequestTypeDef

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.FlowDefinitionOutputConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopRequestSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HumanLoopRequestSourceTypeDef]

### HumanLoopActivationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HumanLoopActivationConfigTypeDef]

### HumanLoopConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HumanLoopConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateFlowDefinitionResponseTypeDef

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHubContentReferenceRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### SageMakerPublicHubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentName
- **Type**: typing.Optional[str]

### MinVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateHubContentReferenceResponseTypeDef

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHubRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubDescription
- **Type**: <class 'str'>
- **Required**: Yes

### HubDisplayName
- **Type**: typing.Optional[str]

### HubSearchKeywords
- **Type**: typing.Optional[typing.Sequence[str]]

### S3StorageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HubS3StorageConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateHubResponseTypeDef

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHumanTaskUiRequestTypeDef

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes

### UiTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UiTemplateTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateHumanTaskUiResponseTypeDef

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHyperParameterTuningJobRequestTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobConfigUnionTypeDef'>
- **Required**: Yes

### TrainingJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobDefinitionUnionTypeDef]

### TrainingJobDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobDefinitionUnionTypeDef]]

### WarmStartConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobWarmStartConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### Autotune
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutotuneTypeDef]


# CreateHyperParameterTuningJobResponseTypeDef

### HyperParameterTuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImageRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateImageResponseTypeDef

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImageVersionRequestTypeDef

### BaseImage
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[typing.Sequence[str]]

### VendorGuidance
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'NOT_PROVIDED', 'STABLE', 'TO_BE_ARCHIVED']]

### JobType
- **Type**: typing.Optional[typing.Literal['INFERENCE', 'NOTEBOOK_KERNEL', 'TRAINING']]

### MLFramework
- **Type**: typing.Optional[str]

### ProgrammingLang
- **Type**: typing.Optional[str]

### Processor
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU']]

### Horovod
- **Type**: typing.Optional[bool]

### ReleaseNotes
- **Type**: typing.Optional[str]


# CreateImageVersionResponseTypeDef

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInferenceComponentInputTypeDef

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Specification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentSpecificationTypeDef'>
- **Required**: Yes

### VariantName
- **Type**: typing.Optional[str]

### RuntimeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentRuntimeConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateInferenceComponentOutputTypeDef

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInferenceExperimentResponseTypeDef

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInferenceRecommendationsJobRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Advanced', 'Default']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobInputConfigUnionTypeDef'>
- **Required**: Yes

### JobDescription
- **Type**: typing.Optional[str]

### StoppingConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobStoppingConditionsUnionTypeDef]

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobOutputConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateInferenceRecommendationsJobResponseTypeDef

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLabelingJobRequestTypeDef

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobInputConfigUnionTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobOutputConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HumanTaskConfigUnionTypeDef'>
- **Required**: Yes

### LabelCategoryConfigS3Uri
- **Type**: typing.Optional[str]

### StoppingConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobStoppingConditionsTypeDef]

### LabelingJobAlgorithmsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobAlgorithmsConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateLabelingJobResponseTypeDef

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMlflowTrackingServerRequestTypeDef

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactStoreUri
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerSize
- **Type**: typing.Optional[typing.Literal['Large', 'Medium', 'Small']]

### MlflowVersion
- **Type**: typing.Optional[str]

### AutomaticModelRegistration
- **Type**: typing.Optional[bool]

### WeeklyMaintenanceWindowStart
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateMlflowTrackingServerResponseTypeDef

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelBiasJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelBiasAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelBiasAppSpecificationUnionTypeDef'>
- **Required**: Yes

### ModelBiasJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelBiasJobInputUnionTypeDef'>
- **Required**: Yes

### ModelBiasJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigUnionTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelBiasBaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelBiasBaselineConfigTypeDef]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigUnionTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateModelBiasJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelCardExportJobRequestTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardExportOutputConfigTypeDef'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]


# CreateModelCardExportJobResponseTypeDef

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelCardRequestTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardSecurityConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateModelCardResponseTypeDef

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelExplainabilityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelExplainabilityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelExplainabilityAppSpecificationUnionTypeDef'>
- **Required**: Yes

### ModelExplainabilityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelExplainabilityJobInputUnionTypeDef'>
- **Required**: Yes

### ModelExplainabilityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigUnionTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelExplainabilityBaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelExplainabilityBaselineConfigTypeDef]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigUnionTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateModelExplainabilityJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelInputTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryContainer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerDefinitionUnionTypeDef]

### Containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerDefinitionUnionTypeDef]]

### InferenceExecutionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceExecutionConfigTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigUnionTypeDef]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]


# CreateModelOutputTypeDef

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelPackageGroupInputTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateModelPackageGroupOutputTypeDef

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelPackageInputTypeDef

### ModelPackageName
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### InferenceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceSpecificationUnionTypeDef]

### ValidationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageValidationSpecificationUnionTypeDef]

### SourceAlgorithmSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SourceAlgorithmSpecificationUnionTypeDef]

### CertifyForMarketplace
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### ModelMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelMetricsTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### CustomerMetadataProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DriftCheckBaselines
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DriftCheckBaselinesTypeDef]

### AdditionalInferenceSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalInferenceSpecificationDefinitionUnionTypeDef]]

### SkipModelValidation
- **Type**: typing.Optional[typing.Literal['All', 'None']]

### SourceUri
- **Type**: typing.Optional[str]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageSecurityConfigTypeDef]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageModelCardTypeDef]

### ModelLifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelLifeCycleTypeDef]


# CreateModelPackageOutputTypeDef

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelQualityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelQualityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelQualityAppSpecificationUnionTypeDef'>
- **Required**: Yes

### ModelQualityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelQualityJobInputUnionTypeDef'>
- **Required**: Yes

### ModelQualityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigUnionTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelQualityBaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelQualityBaselineConfigTypeDef]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigUnionTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateModelQualityJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMonitoringScheduleRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringScheduleConfigUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateMonitoringScheduleResponseTypeDef

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNotebookInstanceInputTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### LifecycleConfigName
- **Type**: typing.Optional[str]

### DirectInternetAccess
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### AcceleratorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.Sequence[str]]

### RootAccess
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### PlatformIdentifier
- **Type**: typing.Optional[str]

### InstanceMetadataServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InstanceMetadataServiceConfigurationTypeDef]


# CreateNotebookInstanceLifecycleConfigInputTypeDef

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceLifecycleHookTypeDef]]

### OnStart
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceLifecycleHookTypeDef]]


# CreateNotebookInstanceLifecycleConfigOutputTypeDef

### NotebookInstanceLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNotebookInstanceOutputTypeDef

### NotebookInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOptimizationJobRequestTypeDef

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationJobModelSourceTypeDef'>
- **Required**: Yes

### DeploymentInstanceType
- **Type**: typing.Literal['ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### OptimizationConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationConfigUnionTypeDef]
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationJobOutputConfigTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### OptimizationEnvironment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationVpcConfigUnionTypeDef]


# CreateOptimizationJobResponseTypeDef

### OptimizationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePartnerAppPresignedUrlRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiresInSeconds
- **Type**: typing.Optional[int]

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreatePartnerAppPresignedUrlResponseTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePartnerAppResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePipelineRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDefinition
- **Type**: typing.Optional[str]

### PipelineDefinitionS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineDefinitionS3LocationTypeDef]

### PipelineDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef]


# CreatePipelineResponseTypeDef

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePresignedDomainUrlRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]

### ExpiresInSeconds
- **Type**: typing.Optional[int]

### SpaceName
- **Type**: typing.Optional[str]

### LandingUri
- **Type**: typing.Optional[str]


# CreatePresignedDomainUrlResponseTypeDef

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePresignedMlflowTrackingServerUrlRequestTypeDef

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiresInSeconds
- **Type**: typing.Optional[int]

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreatePresignedMlflowTrackingServerUrlResponseTypeDef

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePresignedNotebookInstanceUrlInputTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### SessionExpirationDurationInSeconds
- **Type**: typing.Optional[int]


# CreatePresignedNotebookInstanceUrlOutputTypeDef

### AuthorizedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProcessingJobRequestTypeDef

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingResourcesTypeDef'>
- **Required**: Yes

### AppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AppSpecificationUnionTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingInputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingInputTypeDef]]

### ProcessingOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingOutputConfigUnionTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingStoppingConditionTypeDef]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NetworkConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ExperimentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef]


# CreateProcessingJobResponseTypeDef

### ProcessingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectInputTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCatalogProvisioningDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ServiceCatalogProvisioningDetailsUnionTypeDef'>
- **Required**: Yes

### ProjectDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateProjectOutputTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSpaceRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### SpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceSettingsUnionTypeDef]

### OwnershipSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OwnershipSettingsTypeDef]

### SpaceSharingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceSharingSettingsTypeDef]

### SpaceDisplayName
- **Type**: typing.Optional[str]


# CreateSpaceResponseTypeDef

### SpaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStudioLifecycleConfigRequestTypeDef

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigContent
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigAppType
- **Type**: typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateStudioLifecycleConfigResponseTypeDef

### StudioLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrainingJobRequestTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmSpecificationUnionTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigUnionTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### InputDataConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelUnionTypeDef]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CheckpointConfigTypeDef]

### DebugHookConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DebugHookConfigUnionTypeDef]

### DebugRuleConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.DebugRuleConfigurationUnionTypeDef]]

### TensorBoardOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TensorBoardOutputConfigTypeDef]

### ExperimentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef]

### ProfilerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerConfigUnionTypeDef]

### ProfilerRuleConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerRuleConfigurationUnionTypeDef]]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RetryStrategyTypeDef]

### RemoteDebugConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RemoteDebugConfigTypeDef]

### InfraCheckConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InfraCheckConfigTypeDef]

### SessionChainingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SessionChainingConfigTypeDef]


# CreateTrainingJobResponseTypeDef

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrainingPlanRequestTypeDef

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingPlanOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateTrainingPlanResponseTypeDef

### TrainingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTransformJobRequestTypeDef

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformInputTypeDef'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformOutputTypeDef'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformResourcesTypeDef'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### ModelClientConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelClientConfigTypeDef]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DataCaptureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchDataCaptureConfigTypeDef]

### DataProcessing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DataProcessingTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ExperimentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef]


# CreateTransformJobResponseTypeDef

### TransformJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrialComponentRequestTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentStatusTypeDef]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentParameterValueTypeDef]]

### InputArtifacts
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]]

### OutputArtifacts
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateTrialComponentResponseTypeDef

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrialRequestTypeDef

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateTrialResponseTypeDef

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserProfileRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnUserIdentifier
- **Type**: typing.Optional[str]

### SingleSignOnUserValue
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### UserSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserSettingsUnionTypeDef]


# CreateUserProfileResponseTypeDef

### UserProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkforceRequestTypeDef

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes

### CognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CognitoConfigTypeDef]

### OidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OidcConfigTypeDef]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SourceIpConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### WorkforceVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkforceVpcConfigRequestTypeDef]


# CreateWorkforceResponseTypeDef

### WorkforceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkteamRequestTypeDef

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.MemberDefinitionUnionTypeDef]
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### WorkforceName
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NotificationConfigurationTypeDef]

### WorkerAccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkerAccessConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# CreateWorkteamResponseTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomFileSystemConfigTypeDef

### EFSFileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EFSFileSystemConfigTypeDef]

### FSxLustreFileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FSxLustreFileSystemConfigTypeDef]


# CustomFileSystemTypeDef

### EFSFileSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EFSFileSystemTypeDef]

### FSxLustreFileSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FSxLustreFileSystemTypeDef]


# CustomImageTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionNumber
- **Type**: typing.Optional[int]


# CustomPosixUserConfigTypeDef

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes


# CustomizedMetricSpecificationTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']]


# DataCaptureConfigOutputTypeDef

### InitialSamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CaptureOptionTypeDef]
- **Required**: Yes

### EnableCapture
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### CaptureContentTypeHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CaptureContentTypeHeaderOutputTypeDef]


# DataCaptureConfigSummaryTypeDef

### EnableCapture
- **Type**: <class 'bool'>
- **Required**: Yes

### CaptureStatus
- **Type**: typing.Literal['Started', 'Stopped']
- **Required**: Yes

### CurrentSamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DataCaptureConfigTypeDef

### InitialSamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### CaptureOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CaptureOptionTypeDef]
- **Required**: Yes

### EnableCapture
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### CaptureContentTypeHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CaptureContentTypeHeaderTypeDef]


# DataCaptureConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataCatalogConfigTypeDef

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Catalog
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes


# DataProcessingTypeDef

### InputFilter
- **Type**: typing.Optional[str]

### OutputFilter
- **Type**: typing.Optional[str]

### JoinSource
- **Type**: typing.Optional[typing.Literal['Input', 'None']]


# DataQualityAppSpecificationOutputTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataQualityAppSpecificationTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.Sequence[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DataQualityAppSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataQualityBaselineConfigTypeDef

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringConstraintsResourceTypeDef]

### StatisticsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStatisticsResourceTypeDef]


# DataQualityJobInputOutputTypeDef

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputOutputTypeDef]


# DataQualityJobInputTypeDef

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputTypeDef]


# DataQualityJobInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceOutputTypeDef

### S3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.S3DataSourceOutputTypeDef]

### FileSystemDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemDataSourceTypeDef]


# DataSourceTypeDef

### S3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.S3DataSourceUnionTypeDef]

### FileSystemDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemDataSourceTypeDef]


# DatasetDefinitionTypeDef

### AthenaDatasetDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AthenaDatasetDefinitionTypeDef]

### RedshiftDatasetDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RedshiftDatasetDefinitionTypeDef]

### LocalPath
- **Type**: typing.Optional[str]

### DataDistributionType
- **Type**: typing.Optional[typing.Literal['FullyReplicated', 'ShardedByS3Key']]

### InputMode
- **Type**: typing.Optional[typing.Literal['File', 'Pipe']]


# DebugHookConfigOutputTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### HookParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### CollectionConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CollectionConfigurationOutputTypeDef]]


# DebugHookConfigTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### HookParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CollectionConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CollectionConfigurationTypeDef]]


# DebugHookConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DebugRuleConfigurationOutputTypeDef

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# DebugRuleConfigurationTypeDef

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DebugRuleConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DebugRuleEvaluationStatusTypeDef

### RuleConfigurationName
- **Type**: typing.Optional[str]

### RuleEvaluationJobArn
- **Type**: typing.Optional[str]

### RuleEvaluationStatus
- **Type**: typing.Optional[typing.Literal['Error', 'InProgress', 'IssuesFound', 'NoIssuesFound', 'Stopped', 'Stopping']]

### StatusDetails
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# DefaultEbsStorageSettingsTypeDef

### DefaultEbsVolumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumEbsVolumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes


# DefaultSpaceSettingsOutputTypeDef

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterServerAppSettingsOutputTypeDef]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayAppSettingsOutputTypeDef]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppSettingsOutputTypeDef]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DefaultSpaceStorageSettingsTypeDef]

### CustomPosixUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CustomPosixUserConfigTypeDef]

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CustomFileSystemConfigTypeDef]]


# DefaultSpaceSettingsTypeDef

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterServerAppSettingsTypeDef]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayAppSettingsTypeDef]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppSettingsTypeDef]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DefaultSpaceStorageSettingsTypeDef]

### CustomPosixUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CustomPosixUserConfigTypeDef]

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CustomFileSystemConfigTypeDef]]


# DefaultSpaceSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultSpaceStorageSettingsTypeDef

### DefaultEbsStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DefaultEbsStorageSettingsTypeDef]


# DeleteActionRequestTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteActionResponseTypeDef

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAlgorithmInputTypeDef

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppImageConfigRequestTypeDef

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]


# DeleteArtifactRequestTypeDef

### ArtifactArn
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ArtifactSourceUnionTypeDef]


# DeleteArtifactResponseTypeDef

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAssociationRequestTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssociationResponseTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterSchedulerConfigRequestTypeDef

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCodeRepositoryInputTypeDef

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCompilationJobRequestTypeDef

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComputeQuotaRequestTypeDef

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContextRequestTypeDef

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContextResponseTypeDef

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataQualityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeviceFleetRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RetentionPolicyTypeDef]


# DeleteEdgeDeploymentPlanRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEdgeDeploymentStageRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointConfigInputTypeDef

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointInputTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperimentRequestTypeDef

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperimentResponseTypeDef

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFeatureGroupRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowDefinitionRequestTypeDef

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHubContentReferenceRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHubContentRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHubRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHumanTaskUiRequestTypeDef

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHyperParameterTuningJobRequestTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImageVersionRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]


# DeleteInferenceComponentInputTypeDef

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceExperimentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceExperimentResponseTypeDef

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMlflowTrackingServerRequestTypeDef

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMlflowTrackingServerResponseTypeDef

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteModelBiasJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelCardRequestTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelExplainabilityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelInputTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelPackageGroupInputTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelPackageGroupPolicyInputTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelPackageInputTypeDef

### ModelPackageName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelQualityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitoringScheduleRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotebookInstanceInputTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotebookInstanceLifecycleConfigInputTypeDef

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOptimizationJobRequestTypeDef

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePartnerAppRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeletePartnerAppResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePipelineRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineResponseTypeDef

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectInputTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSpaceRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStudioLifecycleConfigRequestTypeDef

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteTrialComponentRequestTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrialComponentResponseTypeDef

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTrialRequestTypeDef

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrialResponseTypeDef

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteUserProfileRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkforceRequestTypeDef

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkteamRequestTypeDef

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkteamResponseTypeDef

### Success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeployedImageTypeDef

### SpecifiedImage
- **Type**: typing.Optional[str]

### ResolvedImage
- **Type**: typing.Optional[str]

### ResolutionTime
- **Type**: typing.Optional[datetime.datetime]


# DeploymentConfigOutputTypeDef

### BlueGreenUpdatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BlueGreenUpdatePolicyTypeDef]

### RollingUpdatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RollingUpdatePolicyTypeDef]

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoRollbackConfigOutputTypeDef]


# DeploymentConfigTypeDef

### BlueGreenUpdatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BlueGreenUpdatePolicyTypeDef]

### RollingUpdatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RollingUpdatePolicyTypeDef]

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoRollbackConfigTypeDef]


# DeploymentConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentRecommendationTypeDef

### RecommendationStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NOT_APPLICABLE']
- **Required**: Yes

### RealTimeInferenceRecommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.RealTimeInferenceRecommendationTypeDef]]


# DeploymentStageStatusSummaryTypeDef

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceSelectionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DeviceSelectionConfigOutputTypeDef'>
- **Required**: Yes

### DeploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeDeploymentConfigTypeDef'>
- **Required**: Yes

### DeploymentStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeDeploymentStatusTypeDef'>
- **Required**: Yes


# DeploymentStageTypeDef

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceSelectionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DeviceSelectionConfigUnionTypeDef'>
- **Required**: Yes

### DeploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeDeploymentConfigTypeDef]


# DeregisterDevicesRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DerivedInformationTypeDef

### DerivedDataInputConfig
- **Type**: typing.Optional[str]


# DescribeActionRequestTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActionResponseTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ActionSourceTypeDef'>
- **Required**: Yes

### ActionType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']
- **Required**: Yes

### Properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAlgorithmInputTypeDef

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlgorithmOutputTypeDef

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrainingSpecificationOutputTypeDef'>
- **Required**: Yes

### InferenceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceSpecificationOutputTypeDef'>
- **Required**: Yes

### ValidationSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmValidationSpecificationOutputTypeDef'>
- **Required**: Yes

### AlgorithmStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### AlgorithmStatusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmStatusDetailsTypeDef'>
- **Required**: Yes

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### CertifyForMarketplace
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppImageConfigRequestTypeDef

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppImageConfigResponseTypeDef

### AppImageConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KernelGatewayImageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayImageConfigOutputTypeDef'>
- **Required**: Yes

### JupyterLabAppImageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppImageConfigOutputTypeDef'>
- **Required**: Yes

### CodeEditorAppImageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.CodeEditorAppImageConfigOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]


# DescribeAppResponseTypeDef

### AppArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppType
- **Type**: typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Deleted', 'Deleting', 'Failed', 'InService', 'Pending']
- **Required**: Yes

### LastHealthCheckTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUserActivityTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSpec
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef'>
- **Required**: Yes

### BuiltInLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeArtifactRequestTypeDef

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeArtifactResponseTypeDef

### ArtifactName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ArtifactSourceOutputTypeDef'>
- **Required**: Yes

### ArtifactType
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAutoMLJobRequestTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoMLJobResponseTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLChannelTypeDef]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLOutputDataConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobObjective
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobObjectiveTypeDef'>
- **Required**: Yes

### ProblemType
- **Type**: typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']
- **Required**: Yes

### AutoMLJobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobConfigOutputTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### PartialFailureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLPartialFailureReasonTypeDef]
- **Required**: Yes

### BestCandidate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLCandidateTypeDef'>
- **Required**: Yes

### AutoMLJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### AutoMLJobSecondaryStatus
- **Type**: typing.Literal['AnalyzingData', 'CandidateDefinitionsGenerated', 'Completed', 'DeployingModel', 'ExplainabilityError', 'Failed', 'FeatureEngineering', 'GeneratingExplainabilityReport', 'GeneratingModelInsightsReport', 'MaxAutoMLJobRuntimeReached', 'MaxCandidatesReached', 'ModelDeploymentError', 'ModelInsightsError', 'ModelTuning', 'PreTraining', 'Starting', 'Stopped', 'Stopping', 'TrainingModels']
- **Required**: Yes

### GenerateCandidateDefinitionsOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoMLJobArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobArtifactsTypeDef'>
- **Required**: Yes

### ResolvedAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResolvedAttributesTypeDef'>
- **Required**: Yes

### ModelDeployConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelDeployConfigTypeDef'>
- **Required**: Yes

### ModelDeployResult
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelDeployResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAutoMLJobV2RequestTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoMLJobV2ResponseTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobInputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobChannelTypeDef]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLOutputDataConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobObjective
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobObjectiveTypeDef'>
- **Required**: Yes

### AutoMLProblemTypeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLProblemTypeConfigOutputTypeDef'>
- **Required**: Yes

### AutoMLProblemTypeConfigName
- **Type**: typing.Literal['ImageClassification', 'Tabular', 'TextClassification', 'TextGeneration', 'TimeSeriesForecasting']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### PartialFailureReasons
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLPartialFailureReasonTypeDef]
- **Required**: Yes

### BestCandidate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLCandidateTypeDef'>
- **Required**: Yes

### AutoMLJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### AutoMLJobSecondaryStatus
- **Type**: typing.Literal['AnalyzingData', 'CandidateDefinitionsGenerated', 'Completed', 'DeployingModel', 'ExplainabilityError', 'Failed', 'FeatureEngineering', 'GeneratingExplainabilityReport', 'GeneratingModelInsightsReport', 'MaxAutoMLJobRuntimeReached', 'MaxCandidatesReached', 'ModelDeploymentError', 'ModelInsightsError', 'ModelTuning', 'PreTraining', 'Starting', 'Stopped', 'Stopping', 'TrainingModels']
- **Required**: Yes

### AutoMLJobArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobArtifactsTypeDef'>
- **Required**: Yes

### ResolvedAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLResolvedAttributesTypeDef'>
- **Required**: Yes

### ModelDeployConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelDeployConfigTypeDef'>
- **Required**: Yes

### ModelDeployResult
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelDeployResultTypeDef'>
- **Required**: Yes

### DataSplitConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLDataSplitConfigTypeDef'>
- **Required**: Yes

### SecurityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLSecurityConfigOutputTypeDef'>
- **Required**: Yes

### AutoMLComputeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLComputeConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterNodeRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### NodeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterNodeResponseTypeDef

### NodeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClusterNodeDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'RollingBack', 'SystemUpdating', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceGroupDetailsTypeDef]
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef'>
- **Required**: Yes

### Orchestrator
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ClusterOrchestratorTypeDef'>
- **Required**: Yes

### NodeRecovery
- **Type**: typing.Literal['Automatic', 'None']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterSchedulerConfigRequestTypeDef

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: typing.Optional[int]


# DescribeClusterSchedulerConfigResponseTypeDef

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SchedulerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.SchedulerConfigOutputTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCodeRepositoryInputTypeDef

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCodeRepositoryOutputTypeDef

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GitConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.GitConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCompilationJobRequestTypeDef

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCompilationJobResponseTypeDef

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CompilationStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompilationEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### InferenceImage
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelArtifactsTypeDef'>
- **Required**: Yes

### ModelDigests
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelDigestsTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InputConfigTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputConfigTypeDef'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.NeoVpcConfigOutputTypeDef'>
- **Required**: Yes

### DerivedInformation
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DerivedInformationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeComputeQuotaRequestTypeDef

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: typing.Optional[int]


# DescribeComputeQuotaResponseTypeDef

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaConfigOutputTypeDef'>
- **Required**: Yes

### ComputeQuotaTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaTargetTypeDef'>
- **Required**: Yes

### ActivationState
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContextRequestTypeDef

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeContextResponseTypeDef

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ContextSourceTypeDef'>
- **Required**: Yes

### ContextType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataQualityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataQualityJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataQualityBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataQualityBaselineConfigTypeDef'>
- **Required**: Yes

### DataQualityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataQualityAppSpecificationOutputTypeDef'>
- **Required**: Yes

### DataQualityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataQualityJobInputOutputTypeDef'>
- **Required**: Yes

### DataQualityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigOutputTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceFleetRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceFleetResponseTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeOutputConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### IotRoleAlias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceRequestTypeDef

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDeviceResponseTypeDef

### DeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### IotThingName
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestHeartbeat
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeModelTypeDef]
- **Required**: Yes

### MaxModels
- **Type**: <class 'int'>
- **Required**: Yes

### AgentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainResponseTypeDef

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeEfsFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnManagedApplicationInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIdForDomainBoundary
- **Type**: <class 'str'>
- **Required**: Yes

### AuthMode
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### DefaultUserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserSettingsOutputTypeDef'>
- **Required**: Yes

### DomainSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DomainSettingsOutputTypeDef'>
- **Required**: Yes

### AppNetworkAccessType
- **Type**: typing.Literal['PublicInternetOnly', 'VpcOnly']
- **Required**: Yes

### HomeEfsFileSystemKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AppSecurityGroupManagement
- **Type**: typing.Literal['Customer', 'Service']
- **Required**: Yes

### TagPropagation
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DefaultSpaceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DefaultSpaceSettingsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEdgeDeploymentPlanRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEdgeDeploymentPlanResponseTypeDef

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeDeploymentModelConfigTypeDef]
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentSuccess
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentPending
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentFailed
- **Type**: <class 'int'>
- **Required**: Yes

### Stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentStageStatusSummaryTypeDef]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEdgePackagingJobRequestTypeDef

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEdgePackagingJobResponseTypeDef

### EdgePackagingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeOutputConfigTypeDef'>
- **Required**: Yes

### ResourceKey
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### EdgePackagingJobStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelArtifact
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSignature
- **Type**: <class 'str'>
- **Required**: Yes

### PresetDeploymentOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgePresetDeploymentOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointConfigInputTypeDef

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointConfigOutputTypeDef

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantTypeDef]
- **Required**: Yes

### DataCaptureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataCaptureConfigOutputTypeDef'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AsyncInferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceConfigOutputTypeDef'>
- **Required**: Yes

### ExplainerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ExplainerConfigOutputTypeDef'>
- **Required**: Yes

### ShadowProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantTypeDef]
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef'>
- **Required**: Yes

### EnableNetworkIsolation
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointInputTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointInputWaitExtraTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeEndpointInputWaitTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeEndpointOutputTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantSummaryTypeDef]
- **Required**: Yes

### DataCaptureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataCaptureConfigSummaryTypeDef'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastDeploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentConfigOutputTypeDef'>
- **Required**: Yes

### AsyncInferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AsyncInferenceConfigOutputTypeDef'>
- **Required**: Yes

### PendingDeploymentSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.PendingDeploymentSummaryTypeDef'>
- **Required**: Yes

### ExplainerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ExplainerConfigOutputTypeDef'>
- **Required**: Yes

### ShadowProductionVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExperimentRequestTypeDef

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExperimentResponseTypeDef

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentSourceTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFeatureGroupRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFeatureGroupResponseTypeDef

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordIdentifierFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTimeFeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureDefinitionTypeDef]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OnlineStoreConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OnlineStoreConfigTypeDef'>
- **Required**: Yes

### OfflineStoreConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OfflineStoreConfigTypeDef'>
- **Required**: Yes

### ThroughputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ThroughputConfigDescriptionTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupStatus
- **Type**: typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']
- **Required**: Yes

### OfflineStoreStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OfflineStoreStatusTypeDef'>
- **Required**: Yes

### LastUpdateStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LastUpdateStatusTypeDef'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### OnlineStoreTotalSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFeatureMetadataRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFeatureMetadataResponseTypeDef

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureType
- **Type**: typing.Literal['Fractional', 'Integral', 'String']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFlowDefinitionRequestTypeDef

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowDefinitionResponseTypeDef

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionStatus
- **Type**: typing.Literal['Active', 'Deleting', 'Failed', 'Initializing']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HumanLoopRequestSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HumanLoopRequestSourceTypeDef'>
- **Required**: Yes

### HumanLoopActivationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HumanLoopActivationConfigTypeDef'>
- **Required**: Yes

### HumanLoopConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HumanLoopConfigOutputTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.FlowDefinitionOutputConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHubContentRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: typing.Optional[str]


# DescribeHubContentResponseTypeDef

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### DocumentSchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDescription
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentMarkdown
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDocument
- **Type**: <class 'str'>
- **Required**: Yes

### SageMakerPublicHubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceMinVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SupportStatus
- **Type**: typing.Literal['Deprecated', 'Restricted', 'Supported']
- **Required**: Yes

### HubContentSearchKeywords
- **Type**: typing.List[str]
- **Required**: Yes

### HubContentDependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HubContentDependencyTypeDef]
- **Required**: Yes

### HubContentStatus
- **Type**: typing.Literal['Available', 'DeleteFailed', 'Deleting', 'ImportFailed', 'Importing']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHubRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHubResponseTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### HubDescription
- **Type**: <class 'str'>
- **Required**: Yes

### HubSearchKeywords
- **Type**: typing.List[str]
- **Required**: Yes

### S3StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HubS3StorageConfigTypeDef'>
- **Required**: Yes

### HubStatus
- **Type**: typing.Literal['CreateFailed', 'Creating', 'DeleteFailed', 'Deleting', 'InService', 'UpdateFailed', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHumanTaskUiRequestTypeDef

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHumanTaskUiResponseTypeDef

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiStatus
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UiTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UiTemplateInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHyperParameterTuningJobRequestTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHyperParameterTuningJobResponseTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobConfigOutputTypeDef'>
- **Required**: Yes

### TrainingJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobDefinitionOutputTypeDef'>
- **Required**: Yes

### TrainingJobDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobDefinitionOutputTypeDef]
- **Required**: Yes

### HyperParameterTuningJobStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HyperParameterTuningEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobStatusCountersTypeDef'>
- **Required**: Yes

### ObjectiveStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ObjectiveStatusCountersTypeDef'>
- **Required**: Yes

### BestTrainingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobSummaryTypeDef'>
- **Required**: Yes

### OverallBestTrainingJob
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobSummaryTypeDef'>
- **Required**: Yes

### WarmStartConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobWarmStartConfigOutputTypeDef'>
- **Required**: Yes

### Autotune
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AutotuneTypeDef'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### TuningJobCompletionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobCompletionDetailsTypeDef'>
- **Required**: Yes

### ConsumedResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobConsumedResourcesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeImageRequestWaitExtraExtraTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeImageRequestWaitExtraTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeImageRequestWaitTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeImageResponseTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageVersionRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]


# DescribeImageVersionRequestWaitExtraTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeImageVersionRequestWaitTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[int]

### Alias
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeImageVersionResponseTypeDef

### BaseImage
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerImage
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### VendorGuidance
- **Type**: typing.Literal['ARCHIVED', 'NOT_PROVIDED', 'STABLE', 'TO_BE_ARCHIVED']
- **Required**: Yes

### JobType
- **Type**: typing.Literal['INFERENCE', 'NOTEBOOK_KERNEL', 'TRAINING']
- **Required**: Yes

### MLFramework
- **Type**: <class 'str'>
- **Required**: Yes

### ProgrammingLang
- **Type**: <class 'str'>
- **Required**: Yes

### Processor
- **Type**: typing.Literal['CPU', 'GPU']
- **Required**: Yes

### Horovod
- **Type**: <class 'bool'>
- **Required**: Yes

### ReleaseNotes
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInferenceComponentInputTypeDef

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceComponentOutputTypeDef

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### Specification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentSpecificationSummaryTypeDef'>
- **Required**: Yes

### RuntimeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentRuntimeConfigSummaryTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceComponentStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']
- **Required**: Yes

### LastDeploymentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentDeploymentConfigOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInferenceExperimentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceRecommendationsJobRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceRecommendationsJobResponseTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobDescription
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Advanced', 'Default']
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobInputConfigOutputTypeDef'>
- **Required**: Yes

### StoppingConditions
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobStoppingConditionsOutputTypeDef'>
- **Required**: Yes

### InferenceRecommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceRecommendationTypeDef]
- **Required**: Yes

### EndpointPerformances
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointPerformanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLabelingJobRequestTypeDef

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLabelingJobResponseTypeDef

### LabelingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']
- **Required**: Yes

### LabelCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelCountersTypeDef'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobReferenceCode
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### LabelAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobInputConfigOutputTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobOutputConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LabelCategoryConfigS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingConditions
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobStoppingConditionsTypeDef'>
- **Required**: Yes

### LabelingJobAlgorithmsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobAlgorithmsConfigOutputTypeDef'>
- **Required**: Yes

### HumanTaskConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HumanTaskConfigOutputTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]
- **Required**: Yes

### LabelingJobOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLineageGroupRequestTypeDef

### LineageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLineageGroupResponseTypeDef

### LineageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMlflowTrackingServerRequestTypeDef

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMlflowTrackingServerResponseTypeDef

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactStoreUri
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerSize
- **Type**: typing.Literal['Large', 'Medium', 'Small']
- **Required**: Yes

### MlflowVersion
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrackingServerStatus
- **Type**: typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']
- **Required**: Yes

### IsActive
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### TrackingServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### WeeklyMaintenanceWindowStart
- **Type**: <class 'str'>
- **Required**: Yes

### AutomaticModelRegistration
- **Type**: <class 'bool'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelBiasJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelBiasJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelBiasBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelBiasBaselineConfigTypeDef'>
- **Required**: Yes

### ModelBiasAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelBiasAppSpecificationOutputTypeDef'>
- **Required**: Yes

### ModelBiasJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelBiasJobInputOutputTypeDef'>
- **Required**: Yes

### ModelBiasJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigOutputTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelCardExportJobRequestTypeDef

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelCardExportJobResponseTypeDef

### ModelCardExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardExportOutputConfigTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ExportArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardExportArtifactsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelCardRequestTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]


# DescribeModelCardResponseTypeDef

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### SecurityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardSecurityConfigTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ModelCardProcessingStatus
- **Type**: typing.Literal['ContentDeleted', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'DeletePending', 'ExportJobsDeleted']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelExplainabilityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelExplainabilityJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelExplainabilityBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelExplainabilityBaselineConfigTypeDef'>
- **Required**: Yes

### ModelExplainabilityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelExplainabilityAppSpecificationOutputTypeDef'>
- **Required**: Yes

### ModelExplainabilityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelExplainabilityJobInputOutputTypeDef'>
- **Required**: Yes

### ModelExplainabilityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigOutputTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelInputTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelOutputTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### PrimaryContainer
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ContainerDefinitionOutputTypeDef'>
- **Required**: Yes

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerDefinitionOutputTypeDef]
- **Required**: Yes

### InferenceExecutionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceExecutionConfigTypeDef'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### EnableNetworkIsolation
- **Type**: <class 'bool'>
- **Required**: Yes

### DeploymentRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentRecommendationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelPackageGroupInputTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelPackageGroupOutputTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ModelPackageGroupStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelPackageInputTypeDef

### ModelPackageName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelPackageOutputTypeDef

### ModelPackageName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceSpecificationOutputTypeDef'>
- **Required**: Yes

### SourceAlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.SourceAlgorithmSpecificationOutputTypeDef'>
- **Required**: Yes

### ValidationSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageValidationSpecificationOutputTypeDef'>
- **Required**: Yes

### ModelPackageStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageStatusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageStatusDetailsTypeDef'>
- **Required**: Yes

### CertifyForMarketplace
- **Type**: <class 'bool'>
- **Required**: Yes

### ModelApprovalStatus
- **Type**: typing.Literal['Approved', 'PendingManualApproval', 'Rejected']
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef'>
- **Required**: Yes

### ModelMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelMetricsTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ApprovalDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Task
- **Type**: <class 'str'>
- **Required**: Yes

### SamplePayloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### CustomerMetadataProperties
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DriftCheckBaselines
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DriftCheckBaselinesTypeDef'>
- **Required**: Yes

### AdditionalInferenceSpecifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalInferenceSpecificationDefinitionOutputTypeDef]
- **Required**: Yes

### SkipModelValidation
- **Type**: typing.Literal['All', 'None']
- **Required**: Yes

### SourceUri
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageSecurityConfigTypeDef'>
- **Required**: Yes

### ModelCard
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageModelCardTypeDef'>
- **Required**: Yes

### ModelLifeCycle
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelLifeCycleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelQualityJobDefinitionRequestTypeDef

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelQualityJobDefinitionResponseTypeDef

### JobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelQualityBaselineConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelQualityBaselineConfigTypeDef'>
- **Required**: Yes

### ModelQualityAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelQualityAppSpecificationOutputTypeDef'>
- **Required**: Yes

### ModelQualityJobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelQualityJobInputOutputTypeDef'>
- **Required**: Yes

### ModelQualityJobOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigOutputTypeDef'>
- **Required**: Yes

### JobResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringNetworkConfigOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMonitoringScheduleRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMonitoringScheduleResponseTypeDef

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']
- **Required**: Yes

### MonitoringType
- **Type**: typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringScheduleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringScheduleConfigOutputTypeDef'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### LastMonitoringExecutionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringExecutionSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNotebookInstanceInputTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotebookInstanceInputWaitExtraExtraTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeNotebookInstanceInputWaitExtraTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeNotebookInstanceInputWaitTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeNotebookInstanceLifecycleConfigInputTypeDef

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotebookInstanceLifecycleConfigOutputTypeDef

### NotebookInstanceLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceLifecycleHookTypeDef]
- **Required**: Yes

### OnStart
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceLifecycleHookTypeDef]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNotebookInstanceOutputTypeDef

### NotebookInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceStatus
- **Type**: typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### DirectInternetAccess
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### AcceleratorTypes
- **Type**: typing.List[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]
- **Required**: Yes

### DefaultCodeRepository
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalCodeRepositories
- **Type**: typing.List[str]
- **Required**: Yes

### RootAccess
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### PlatformIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceMetadataServiceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InstanceMetadataServiceConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOptimizationJobRequestTypeDef

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOptimizationJobResponseTypeDef

### OptimizationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### OptimizationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### OptimizationStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OptimizationEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationJobModelSourceTypeDef'>
- **Required**: Yes

### OptimizationEnvironment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DeploymentInstanceType
- **Type**: typing.Literal['ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### OptimizationConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationConfigOutputTypeDef]
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationJobOutputConfigTypeDef'>
- **Required**: Yes

### OptimizationOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationVpcConfigOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePartnerAppRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineDefinitionForExecutionRequestTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineDefinitionForExecutionResponseTypeDef

### PipelineDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePipelineExecutionRequestTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineExecutionResponseTypeDef

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionStatus
- **Type**: typing.Literal['Executing', 'Failed', 'Stopped', 'Stopping', 'Succeeded']
- **Required**: Yes

### PipelineExecutionDescription
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.PipelineExperimentConfigTypeDef'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ParallelismConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef'>
- **Required**: Yes

### SelectiveExecutionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.SelectiveExecutionConfigOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePipelineRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipelineResponseTypeDef

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDescription
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineStatus
- **Type**: typing.Literal['Active', 'Deleting']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastRunTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ParallelismConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProcessingJobRequestTypeDef

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProcessingJobRequestWaitTypeDef

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeProcessingJobResponseTypeDef

### ProcessingInputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingInputTypeDef]
- **Required**: Yes

### ProcessingOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingOutputConfigOutputTypeDef'>
- **Required**: Yes

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingResourcesTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingStoppingConditionTypeDef'>
- **Required**: Yes

### AppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AppSpecificationOutputTypeDef'>
- **Required**: Yes

### Environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### NetworkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.NetworkConfigOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef'>
- **Required**: Yes

### ProcessingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### ExitMessage
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProcessingStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectInputTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProjectOutputTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceCatalogProvisioningDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ServiceCatalogProvisioningDetailsOutputTypeDef'>
- **Required**: Yes

### ServiceCatalogProvisionedProductDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ServiceCatalogProvisionedProductDetailsTypeDef'>
- **Required**: Yes

### ProjectStatus
- **Type**: typing.Literal['CreateCompleted', 'CreateFailed', 'CreateInProgress', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'Pending', 'UpdateCompleted', 'UpdateFailed', 'UpdateInProgress']
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSpaceRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSpaceResponseTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeEfsFileSystemUid
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.SpaceSettingsOutputTypeDef'>
- **Required**: Yes

### OwnershipSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OwnershipSettingsTypeDef'>
- **Required**: Yes

### SpaceSharingSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.SpaceSharingSettingsTypeDef'>
- **Required**: Yes

### SpaceDisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStudioLifecycleConfigRequestTypeDef

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStudioLifecycleConfigResponseTypeDef

### StudioLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StudioLifecycleConfigContent
- **Type**: <class 'str'>
- **Required**: Yes

### StudioLifecycleConfigAppType
- **Type**: typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSubscribedWorkteamRequestTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSubscribedWorkteamResponseTypeDef

### SubscribedWorkteam
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.SubscribedWorkteamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrainingJobRequestTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrainingJobRequestWaitTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeTrainingJobResponseTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### TuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArtifacts
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelArtifactsTypeDef'>
- **Required**: Yes

### TrainingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### SecondaryStatus
- **Type**: typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmSpecificationOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelOutputTypeDef]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigOutputTypeDef'>
- **Required**: Yes

### WarmPoolStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.WarmPoolStatusTypeDef'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SecondaryStatusTransitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.SecondaryStatusTransitionTypeDef]
- **Required**: Yes

### FinalMetricDataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDataTypeDef]
- **Required**: Yes

### EnableNetworkIsolation
- **Type**: <class 'bool'>
- **Required**: Yes

### EnableInterContainerTrafficEncryption
- **Type**: <class 'bool'>
- **Required**: Yes

### EnableManagedSpotTraining
- **Type**: <class 'bool'>
- **Required**: Yes

### CheckpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.CheckpointConfigTypeDef'>
- **Required**: Yes

### TrainingTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### BillableTimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### DebugHookConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DebugHookConfigOutputTypeDef'>
- **Required**: Yes

### ExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef'>
- **Required**: Yes

### DebugRuleConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DebugRuleConfigurationOutputTypeDef]
- **Required**: Yes

### TensorBoardOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TensorBoardOutputConfigTypeDef'>
- **Required**: Yes

### DebugRuleEvaluationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DebugRuleEvaluationStatusTypeDef]
- **Required**: Yes

### ProfilerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerConfigOutputTypeDef'>
- **Required**: Yes

### ProfilerRuleConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerRuleConfigurationOutputTypeDef]
- **Required**: Yes

### ProfilerRuleEvaluationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerRuleEvaluationStatusTypeDef]
- **Required**: Yes

### ProfilingStatus
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryStrategy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.RetryStrategyTypeDef'>
- **Required**: Yes

### RemoteDebugConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.RemoteDebugConfigTypeDef'>
- **Required**: Yes

### InfraCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InfraCheckConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrainingPlanRequestTypeDef

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrainingPlanResponseTypeDef

### TrainingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Expired', 'Failed', 'Pending', 'Scheduled']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DurationHours
- **Type**: <class 'int'>
- **Required**: Yes

### DurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpfrontFee
- **Type**: <class 'str'>
- **Required**: Yes

### CurrencyCode
- **Type**: <class 'str'>
- **Required**: Yes

### TotalInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### AvailableInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InUseInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### TargetResources
- **Type**: typing.List[typing.Literal['hyperpod-cluster', 'training-job']]
- **Required**: Yes

### ReservedCapacitySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ReservedCapacitySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTransformJobRequestTypeDef

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTransformJobRequestWaitTypeDef

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WaiterConfigTypeDef]


# DescribeTransformJobResponseTypeDef

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: <class 'int'>
- **Required**: Yes

### ModelClientConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelClientConfigTypeDef'>
- **Required**: Yes

### MaxPayloadInMB
- **Type**: <class 'int'>
- **Required**: Yes

### BatchStrategy
- **Type**: typing.Literal['MultiRecord', 'SingleRecord']
- **Required**: Yes

### Environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformInputTypeDef'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformOutputTypeDef'>
- **Required**: Yes

### DataCaptureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.BatchDataCaptureConfigTypeDef'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformResourcesTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransformStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransformEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataProcessing
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DataProcessingTypeDef'>
- **Required**: Yes

### ExperimentConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrialComponentRequestTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrialComponentResponseTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSourceTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentStatusTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentParameterValueTypeDef]
- **Required**: Yes

### InputArtifacts
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]
- **Required**: Yes

### OutputArtifacts
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef'>
- **Required**: Yes

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentMetricSummaryTypeDef]
- **Required**: Yes

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrialRequestTypeDef

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrialResponseTypeDef

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrialSourceTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef'>
- **Required**: Yes

### MetadataProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserProfileRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserProfileResponseTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeEfsFileSystemUid
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnUserIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### SingleSignOnUserValue
- **Type**: <class 'str'>
- **Required**: Yes

### UserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UserSettingsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkforceRequestTypeDef

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkforceResponseTypeDef

### Workforce
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.WorkforceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkteamRequestTypeDef

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkteamResponseTypeDef

### Workteam
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.WorkteamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DesiredWeightAndCapacityTypeDef

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredWeight
- **Type**: typing.Optional[float]

### DesiredInstanceCount
- **Type**: typing.Optional[int]

### ServerlessUpdateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessUpdateConfigTypeDef]


# DeviceDeploymentSummaryTypeDef

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeployedStageName
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]

### DeviceDeploymentStatus
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'FAILED', 'INPROGRESS', 'READYTODEPLOY', 'STOPPED', 'STOPPING']]

### DeviceDeploymentStatusMessage
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DeploymentStartTime
- **Type**: typing.Optional[datetime.datetime]


# DeviceFleetSummaryTypeDef

### DeviceFleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# DeviceSelectionConfigOutputTypeDef

### DeviceSubsetType
- **Type**: typing.Literal['NAMECONTAINS', 'PERCENTAGE', 'SELECTION']
- **Required**: Yes

### Percentage
- **Type**: typing.Optional[int]

### DeviceNames
- **Type**: typing.Optional[typing.List[str]]

### DeviceNameContains
- **Type**: typing.Optional[str]


# DeviceSelectionConfigTypeDef

### DeviceSubsetType
- **Type**: typing.Literal['NAMECONTAINS', 'PERCENTAGE', 'SELECTION']
- **Required**: Yes

### Percentage
- **Type**: typing.Optional[int]

### DeviceNames
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceNameContains
- **Type**: typing.Optional[str]


# DeviceSelectionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeviceStatsTypeDef

### ConnectedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### RegisteredDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes


# DeviceSummaryTypeDef

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]

### IotThingName
- **Type**: typing.Optional[str]

### RegistrationTime
- **Type**: typing.Optional[datetime.datetime]

### LatestHeartbeat
- **Type**: typing.Optional[datetime.datetime]

### Models
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeModelSummaryTypeDef]]

### AgentVersion
- **Type**: typing.Optional[str]


# DeviceTypeDef

### DeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### IotThingName
- **Type**: typing.Optional[str]


# DirectDeploySettingsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# DisassociateTrialComponentRequestTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateTrialComponentResponseTypeDef

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DockerSettingsOutputTypeDef

### EnableDockerAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VpcOnlyTrustedAccounts
- **Type**: typing.Optional[typing.List[str]]


# DockerSettingsTypeDef

### EnableDockerAccess
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### VpcOnlyTrustedAccounts
- **Type**: typing.Optional[typing.Sequence[str]]


# DockerSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainDetailsTypeDef

### DomainArn
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Url
- **Type**: typing.Optional[str]


# DomainSettingsForUpdateTypeDef

### RStudioServerProDomainSettingsForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RStudioServerProDomainSettingsForUpdateTypeDef]

### ExecutionRoleIdentityConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'USER_PROFILE_NAME']]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DockerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DockerSettingsUnionTypeDef]

### AmazonQSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AmazonQSettingsTypeDef]


# DomainSettingsOutputTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### RStudioServerProDomainSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RStudioServerProDomainSettingsTypeDef]

### ExecutionRoleIdentityConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'USER_PROFILE_NAME']]

### DockerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DockerSettingsOutputTypeDef]

### AmazonQSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AmazonQSettingsTypeDef]


# DomainSettingsTypeDef

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### RStudioServerProDomainSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RStudioServerProDomainSettingsTypeDef]

### ExecutionRoleIdentityConfig
- **Type**: typing.Optional[typing.Literal['DISABLED', 'USER_PROFILE_NAME']]

### DockerSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DockerSettingsTypeDef]

### AmazonQSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AmazonQSettingsTypeDef]


# DomainSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DriftCheckBaselinesTypeDef

### Bias
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DriftCheckBiasTypeDef]

### Explainability
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DriftCheckExplainabilityTypeDef]

### ModelQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DriftCheckModelQualityTypeDef]

### ModelDataQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DriftCheckModelDataQualityTypeDef]


# DriftCheckBiasTypeDef

### ConfigFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSourceTypeDef]

### PreTrainingConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### PostTrainingConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]


# DriftCheckExplainabilityTypeDef

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### ConfigFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSourceTypeDef]


# DriftCheckModelDataQualityTypeDef

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]


# DriftCheckModelQualityTypeDef

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]


# DynamicScalingConfigurationTypeDef

### MinCapacity
- **Type**: typing.Optional[int]

### MaxCapacity
- **Type**: typing.Optional[int]

### ScaleInCooldown
- **Type**: typing.Optional[int]

### ScaleOutCooldown
- **Type**: typing.Optional[int]

### ScalingPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ScalingPolicyTypeDef]]


# EFSFileSystemConfigTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemPath
- **Type**: typing.Optional[str]


# EFSFileSystemTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# EMRStepMetadataTypeDef

### ClusterId
- **Type**: typing.Optional[str]

### StepId
- **Type**: typing.Optional[str]

### StepName
- **Type**: typing.Optional[str]

### LogFilePath
- **Type**: typing.Optional[str]


# EbsStorageSettingsTypeDef

### EbsVolumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes


# EdgeDeploymentConfigTypeDef

### FailureHandlingPolicy
- **Type**: typing.Literal['DO_NOTHING', 'ROLLBACK_ON_FAILURE']
- **Required**: Yes


# EdgeDeploymentModelConfigTypeDef

### ModelHandle
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# EdgeDeploymentPlanSummaryTypeDef

### EdgeDeploymentPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeDeploymentSuccess
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentPending
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentFailed
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# EdgeDeploymentStatusTypeDef

### StageStatus
- **Type**: typing.Literal['CREATING', 'DEPLOYED', 'FAILED', 'INPROGRESS', 'READYTODEPLOY', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### EdgeDeploymentSuccessInStage
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentPendingInStage
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentFailedInStage
- **Type**: <class 'int'>
- **Required**: Yes

### EdgeDeploymentStatusMessage
- **Type**: typing.Optional[str]

### EdgeDeploymentStageStartTime
- **Type**: typing.Optional[datetime.datetime]


# EdgeModelStatTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### OfflineDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ConnectedDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ActiveDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes

### SamplingDeviceCount
- **Type**: <class 'int'>
- **Required**: Yes


# EdgeModelSummaryTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes


# EdgeModelTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### LatestSampleTime
- **Type**: typing.Optional[datetime.datetime]

### LatestInference
- **Type**: typing.Optional[datetime.datetime]


# EdgeOutputConfigTypeDef

### S3OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### PresetDeploymentType
- **Type**: typing.Optional[typing.Literal['GreengrassV2Component']]

### PresetDeploymentConfig
- **Type**: typing.Optional[str]


# EdgePackagingJobSummaryTypeDef

### EdgePackagingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### EdgePackagingJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CompilationJobName
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# EdgePresetDeploymentOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EdgeTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmrServerlessComputeConfigTypeDef

### ExecutionRoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# EmrServerlessSettingsTypeDef

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# EmrSettingsOutputTypeDef

### AssumableRoleArns
- **Type**: typing.Optional[typing.List[str]]

### ExecutionRoleArns
- **Type**: typing.Optional[typing.List[str]]


# EmrSettingsTypeDef

### AssumableRoleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExecutionRoleArns
- **Type**: typing.Optional[typing.Sequence[str]]


# EndpointConfigStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# EndpointConfigSummaryTypeDef

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# EndpointInfoTypeDef

### EndpointName
- **Type**: typing.Optional[str]


# EndpointInputConfigurationOutputTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### EnvironmentParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EnvironmentParameterRangesOutputTypeDef]


# EndpointInputConfigurationTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### EnvironmentParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EnvironmentParameterRangesTypeDef]


# EndpointInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EndpointMetadataTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: typing.Optional[str]

### EndpointStatus
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']]

### FailureReason
- **Type**: typing.Optional[str]


# EndpointOutputConfigurationTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InitialInstanceCount
- **Type**: typing.Optional[int]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]


# EndpointPerformanceTypeDef

### Metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceMetricsTypeDef'>
- **Required**: Yes

### EndpointInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInfoTypeDef'>
- **Required**: Yes


# EndpointStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# EndpointSummaryTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes


# EndpointTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantSummaryTypeDef]]

### DataCaptureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DataCaptureConfigSummaryTypeDef]

### FailureReason
- **Type**: typing.Optional[str]

### MonitoringSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringScheduleTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ShadowProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantSummaryTypeDef]]


# EnvironmentParameterRangesOutputTypeDef

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CategoricalParameterOutputTypeDef]]


# EnvironmentParameterRangesTypeDef

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CategoricalParameterTypeDef]]


# EnvironmentParameterTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorInfoTypeDef

### Code
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]


# ExperimentConfigTypeDef

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### TrialComponentDisplayName
- **Type**: typing.Optional[str]

### RunName
- **Type**: typing.Optional[str]


# ExperimentSourceTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]


# ExperimentSummaryTypeDef

### ExperimentArn
- **Type**: typing.Optional[str]

### ExperimentName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### ExperimentSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentSourceTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ExperimentTypeDef

### ExperimentName
- **Type**: typing.Optional[str]

### ExperimentArn
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentSourceTypeDef]

### Description
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# ExplainabilityTypeDef

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]


# ExplainerConfigOutputTypeDef

### ClarifyExplainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyExplainerConfigOutputTypeDef]


# ExplainerConfigTypeDef

### ClarifyExplainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyExplainerConfigTypeDef]


# ExplainerConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FSxLustreFileSystemConfigTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemPath
- **Type**: typing.Optional[str]


# FSxLustreFileSystemTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# FailStepMetadataTypeDef

### ErrorMessage
- **Type**: typing.Optional[str]


# FeatureDefinitionTypeDef

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureType
- **Type**: typing.Literal['Fractional', 'Integral', 'String']
- **Required**: Yes

### CollectionType
- **Type**: typing.Optional[typing.Literal['List', 'Set', 'Vector']]

### CollectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CollectionConfigTypeDef]


# FeatureGroupSummaryTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FeatureGroupStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OfflineStoreStatusTypeDef]


# FeatureGroupTypeDef

### FeatureGroupArn
- **Type**: typing.Optional[str]

### FeatureGroupName
- **Type**: typing.Optional[str]

### RecordIdentifierFeatureName
- **Type**: typing.Optional[str]

### EventTimeFeatureName
- **Type**: typing.Optional[str]

### FeatureDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureDefinitionTypeDef]]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### OnlineStoreConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OnlineStoreConfigTypeDef]

### OfflineStoreConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OfflineStoreConfigTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### FeatureGroupStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OfflineStoreStatusTypeDef]

### LastUpdateStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LastUpdateStatusTypeDef]

### FailureReason
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# FeatureMetadataTypeDef

### FeatureGroupArn
- **Type**: typing.Optional[str]

### FeatureGroupName
- **Type**: typing.Optional[str]

### FeatureName
- **Type**: typing.Optional[str]

### FeatureType
- **Type**: typing.Optional[typing.Literal['Fractional', 'Integral', 'String']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureParameterTypeDef]]


# FeatureParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# FileSourceTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### ContentDigest
- **Type**: typing.Optional[str]


# FileSystemConfigTypeDef

### MountPath
- **Type**: typing.Optional[str]

### DefaultUid
- **Type**: typing.Optional[int]

### DefaultGid
- **Type**: typing.Optional[int]


# FileSystemDataSourceTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemAccessMode
- **Type**: typing.Literal['ro', 'rw']
- **Required**: Yes

### FileSystemType
- **Type**: typing.Literal['EFS', 'FSxLustre']
- **Required**: Yes

### DirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes


# FilterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Optional[typing.Literal['Contains', 'Equals', 'Exists', 'GreaterThan', 'GreaterThanOrEqualTo', 'In', 'LessThan', 'LessThanOrEqualTo', 'NotEquals', 'NotExists']]

### Value
- **Type**: typing.Optional[str]


# FinalAutoMLJobObjectiveMetricTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FinalHyperParameterTuningJobObjectiveMetricTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowDefinitionOutputConfigTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# FlowDefinitionSummaryTypeDef

### FlowDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionStatus
- **Type**: typing.Literal['Active', 'Deleting', 'Failed', 'Initializing']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# GenerativeAiSettingsTypeDef

### AmazonBedrockRoleArn
- **Type**: typing.Optional[str]


# GetDeviceFleetReportRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceFleetReportResponseTypeDef

### DeviceFleetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeOutputConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ReportGenerated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DeviceStats
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DeviceStatsTypeDef'>
- **Required**: Yes

### AgentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AgentVersionTypeDef]
- **Required**: Yes

### ModelStats
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeModelStatTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLineageGroupPolicyRequestTypeDef

### LineageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLineageGroupPolicyResponseTypeDef

### LineageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelPackageGroupPolicyInputTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelPackageGroupPolicyOutputTypeDef

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSagemakerServicecatalogPortfolioStatusOutputTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetScalingConfigurationRecommendationRequestTypeDef

### InferenceRecommendationsJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### TargetCpuUtilizationPerCore
- **Type**: typing.Optional[int]

### ScalingPolicyObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ScalingPolicyObjectiveTypeDef]


# GetScalingConfigurationRecommendationResponseTypeDef

### InferenceRecommendationsJobName
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetCpuUtilizationPerCore
- **Type**: <class 'int'>
- **Required**: Yes

### ScalingPolicyObjective
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ScalingPolicyObjectiveTypeDef'>
- **Required**: Yes

### Metric
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ScalingPolicyMetricTypeDef'>
- **Required**: Yes

### DynamicScalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.DynamicScalingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSearchSuggestionsRequestTypeDef

### Resource
- **Type**: typing.Literal['Endpoint', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'FeatureGroup', 'FeatureMetadata', 'HyperParameterTuningJob', 'Image', 'ImageVersion', 'Model', 'ModelCard', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'Project', 'TrainingJob']
- **Required**: Yes

### SuggestionQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SuggestionQueryTypeDef]


# GetSearchSuggestionsResponseTypeDef

### PropertyNameSuggestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PropertyNameSuggestionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GitConfigForUpdateTypeDef

### SecretArn
- **Type**: typing.Optional[str]


# GitConfigTypeDef

### RepositoryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Branch
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]


# HiddenSageMakerImageOutputTypeDef

### SageMakerImageName
- **Type**: typing.Optional[typing.Literal['sagemaker_distribution']]

### VersionAliases
- **Type**: typing.Optional[typing.List[str]]


# HiddenSageMakerImageTypeDef

### SageMakerImageName
- **Type**: typing.Optional[typing.Literal['sagemaker_distribution']]

### VersionAliases
- **Type**: typing.Optional[typing.Sequence[str]]


# HolidayConfigAttributesTypeDef

### CountryCode
- **Type**: typing.Optional[str]


# HubAccessConfigTypeDef

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes


# HubContentDependencyTypeDef

### DependencyOriginPath
- **Type**: typing.Optional[str]

### DependencyCopyPath
- **Type**: typing.Optional[str]


# HubContentInfoTypeDef

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### DocumentSchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentStatus
- **Type**: typing.Literal['Available', 'DeleteFailed', 'Deleting', 'ImportFailed', 'Importing']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SageMakerPublicHubContentArn
- **Type**: typing.Optional[str]

### HubContentDisplayName
- **Type**: typing.Optional[str]

### HubContentDescription
- **Type**: typing.Optional[str]

### SupportStatus
- **Type**: typing.Optional[typing.Literal['Deprecated', 'Restricted', 'Supported']]

### HubContentSearchKeywords
- **Type**: typing.Optional[typing.List[str]]

### OriginalCreationTime
- **Type**: typing.Optional[datetime.datetime]


# HubInfoTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubStatus
- **Type**: typing.Literal['CreateFailed', 'Creating', 'DeleteFailed', 'Deleting', 'InService', 'UpdateFailed', 'Updating']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HubDisplayName
- **Type**: typing.Optional[str]

### HubDescription
- **Type**: typing.Optional[str]

### HubSearchKeywords
- **Type**: typing.Optional[typing.List[str]]


# HubS3StorageConfigTypeDef

### S3OutputPath
- **Type**: typing.Optional[str]


# HumanLoopActivationConditionsConfigTypeDef

### HumanLoopActivationConditions
- **Type**: <class 'str'>
- **Required**: Yes


# HumanLoopActivationConfigTypeDef

### HumanLoopActivationConditionsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HumanLoopActivationConditionsConfigTypeDef'>
- **Required**: Yes


# HumanLoopConfigOutputTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: <class 'int'>
- **Required**: Yes

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### TaskTimeLimitInSeconds
- **Type**: typing.Optional[int]

### TaskKeywords
- **Type**: typing.Optional[typing.List[str]]

### PublicWorkforceTaskPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PublicWorkforceTaskPriceTypeDef]


# HumanLoopConfigTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: <class 'int'>
- **Required**: Yes

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### TaskTimeLimitInSeconds
- **Type**: typing.Optional[int]

### TaskKeywords
- **Type**: typing.Optional[typing.Sequence[str]]

### PublicWorkforceTaskPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PublicWorkforceTaskPriceTypeDef]


# HumanLoopConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HumanLoopRequestSourceTypeDef

### AwsManagedHumanLoopRequestSource
- **Type**: typing.Literal['AWS/Rekognition/DetectModerationLabels/Image/V3', 'AWS/Textract/AnalyzeDocument/Forms/V1']
- **Required**: Yes


# HumanTaskConfigOutputTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### UiConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UiConfigTypeDef'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfHumanWorkersPerDataObject
- **Type**: <class 'int'>
- **Required**: Yes

### TaskTimeLimitInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### PreHumanTaskLambdaArn
- **Type**: typing.Optional[str]

### TaskKeywords
- **Type**: typing.Optional[typing.List[str]]

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### MaxConcurrentTaskCount
- **Type**: typing.Optional[int]

### AnnotationConsolidationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AnnotationConsolidationConfigTypeDef]

### PublicWorkforceTaskPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PublicWorkforceTaskPriceTypeDef]


# HumanTaskConfigTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### UiConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.UiConfigTypeDef'>
- **Required**: Yes

### TaskTitle
- **Type**: <class 'str'>
- **Required**: Yes

### TaskDescription
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfHumanWorkersPerDataObject
- **Type**: <class 'int'>
- **Required**: Yes

### TaskTimeLimitInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### PreHumanTaskLambdaArn
- **Type**: typing.Optional[str]

### TaskKeywords
- **Type**: typing.Optional[typing.Sequence[str]]

### TaskAvailabilityLifetimeInSeconds
- **Type**: typing.Optional[int]

### MaxConcurrentTaskCount
- **Type**: typing.Optional[int]

### AnnotationConsolidationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AnnotationConsolidationConfigTypeDef]

### PublicWorkforceTaskPrice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PublicWorkforceTaskPriceTypeDef]


# HumanTaskConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HumanTaskUiSummaryTypeDef

### HumanTaskUiName
- **Type**: <class 'str'>
- **Required**: Yes

### HumanTaskUiArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# HyperParameterAlgorithmSpecificationOutputTypeDef

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDefinitionTypeDef]]


# HyperParameterAlgorithmSpecificationTypeDef

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### TrainingImage
- **Type**: typing.Optional[str]

### AlgorithmName
- **Type**: typing.Optional[str]

### MetricDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDefinitionTypeDef]]


# HyperParameterAlgorithmSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperParameterSpecificationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperParameterSpecificationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperParameterTrainingJobDefinitionOutputTypeDef

### AlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterAlgorithmSpecificationOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### DefinitionName
- **Type**: typing.Optional[str]

### TuningObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobObjectiveTypeDef]

### HyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParameterRangesOutputTypeDef]

### StaticHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### InputDataConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelOutputTypeDef]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigOutputTypeDef]

### HyperParameterTuningResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningResourceConfigOutputTypeDef]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CheckpointConfigTypeDef]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RetryStrategyTypeDef]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# HyperParameterTrainingJobDefinitionTypeDef

### AlgorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterAlgorithmSpecificationUnionTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### DefinitionName
- **Type**: typing.Optional[str]

### TuningObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobObjectiveTypeDef]

### HyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParameterRangesUnionTypeDef]

### StaticHyperParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### InputDataConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelUnionTypeDef]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigUnionTypeDef]

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigUnionTypeDef]

### HyperParameterTuningResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningResourceConfigUnionTypeDef]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CheckpointConfigTypeDef]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RetryStrategyTypeDef]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# HyperParameterTrainingJobDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperParameterTrainingJobSummaryTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### TunedHyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TrainingJobDefinitionName
- **Type**: typing.Optional[str]

### TuningJobName
- **Type**: typing.Optional[str]

### TrainingStartTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### FinalHyperParameterTuningJobObjectiveMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FinalHyperParameterTuningJobObjectiveMetricTypeDef]

### ObjectiveStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Succeeded']]


# HyperParameterTuningInstanceConfigTypeDef

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes


# HyperParameterTuningJobCompletionDetailsTypeDef

### NumberOfTrainingJobsObjectiveNotImproving
- **Type**: typing.Optional[int]

### ConvergenceDetectedTime
- **Type**: typing.Optional[datetime.datetime]


# HyperParameterTuningJobConfigOutputTypeDef

### Strategy
- **Type**: typing.Literal['Bayesian', 'Grid', 'Hyperband', 'Random']
- **Required**: Yes

### ResourceLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResourceLimitsTypeDef'>
- **Required**: Yes

### StrategyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobStrategyConfigTypeDef]

### HyperParameterTuningJobObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobObjectiveTypeDef]

### ParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParameterRangesOutputTypeDef]

### TrainingJobEarlyStoppingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Off']]

### TuningJobCompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TuningJobCompletionCriteriaTypeDef]

### RandomSeed
- **Type**: typing.Optional[int]


# HyperParameterTuningJobConfigTypeDef

### Strategy
- **Type**: typing.Literal['Bayesian', 'Grid', 'Hyperband', 'Random']
- **Required**: Yes

### ResourceLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResourceLimitsTypeDef'>
- **Required**: Yes

### StrategyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobStrategyConfigTypeDef]

### HyperParameterTuningJobObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobObjectiveTypeDef]

### ParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParameterRangesTypeDef]

### TrainingJobEarlyStoppingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Off']]

### TuningJobCompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TuningJobCompletionCriteriaTypeDef]

### RandomSeed
- **Type**: typing.Optional[int]


# HyperParameterTuningJobConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperParameterTuningJobConsumedResourcesTypeDef

### RuntimeInSeconds
- **Type**: typing.Optional[int]


# HyperParameterTuningJobObjectiveTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperParameterTuningJobSearchEntityTypeDef

### HyperParameterTuningJobName
- **Type**: typing.Optional[str]

### HyperParameterTuningJobArn
- **Type**: typing.Optional[str]

### HyperParameterTuningJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobConfigOutputTypeDef]

### TrainingJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobDefinitionOutputTypeDef]

### TrainingJobDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobDefinitionOutputTypeDef]]

### HyperParameterTuningJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### HyperParameterTuningEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingJobStatusCounters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobStatusCountersTypeDef]

### ObjectiveStatusCounters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ObjectiveStatusCountersTypeDef]

### BestTrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobSummaryTypeDef]

### OverallBestTrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobSummaryTypeDef]

### WarmStartConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobWarmStartConfigOutputTypeDef]

### FailureReason
- **Type**: typing.Optional[str]

### TuningJobCompletionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobCompletionDetailsTypeDef]

### ConsumedResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobConsumedResourcesTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# HyperParameterTuningJobStrategyConfigTypeDef

### HyperbandStrategyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperbandStrategyConfigTypeDef]


# HyperParameterTuningJobSummaryTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### HyperParameterTuningJobStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### Strategy
- **Type**: typing.Literal['Bayesian', 'Grid', 'Hyperband', 'Random']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobStatusCountersTypeDef'>
- **Required**: Yes

### ObjectiveStatusCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ObjectiveStatusCountersTypeDef'>
- **Required**: Yes

### HyperParameterTuningEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceLimitsTypeDef]


# HyperParameterTuningJobWarmStartConfigOutputTypeDef

### ParentHyperParameterTuningJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ParentHyperParameterTuningJobTypeDef]
- **Required**: Yes

### WarmStartType
- **Type**: typing.Literal['IdenticalDataAndAlgorithm', 'TransferLearning']
- **Required**: Yes


# HyperParameterTuningJobWarmStartConfigTypeDef

### ParentHyperParameterTuningJobs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ParentHyperParameterTuningJobTypeDef]
- **Required**: Yes

### WarmStartType
- **Type**: typing.Literal['IdenticalDataAndAlgorithm', 'TransferLearning']
- **Required**: Yes


# HyperParameterTuningJobWarmStartConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperParameterTuningResourceConfigOutputTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### AllocationStrategy
- **Type**: typing.Optional[typing.Literal['Prioritized']]

### InstanceConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningInstanceConfigTypeDef]]


# HyperParameterTuningResourceConfigTypeDef

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### AllocationStrategy
- **Type**: typing.Optional[typing.Literal['Prioritized']]

### InstanceConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningInstanceConfigTypeDef]]


# HyperParameterTuningResourceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HyperbandStrategyConfigTypeDef

### MinResource
- **Type**: typing.Optional[int]

### MaxResource
- **Type**: typing.Optional[int]


# IamIdentityTypeDef

### Arn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### SourceIdentity
- **Type**: typing.Optional[str]


# IamPolicyConstraintsTypeDef

### SourceIp
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### VpcSourceIp
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# IdentityProviderOAuthSettingTypeDef

### DataSourceName
- **Type**: typing.Optional[typing.Literal['SalesforceGenie', 'Snowflake']]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SecretArn
- **Type**: typing.Optional[str]


# IdleSettingsTypeDef

### LifecycleManagement
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IdleTimeoutInMinutes
- **Type**: typing.Optional[int]

### MinIdleTimeoutInMinutes
- **Type**: typing.Optional[int]

### MaxIdleTimeoutInMinutes
- **Type**: typing.Optional[int]


# ImageClassificationJobConfigTypeDef

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]


# ImageConfigTypeDef

### RepositoryAccessMode
- **Type**: typing.Literal['Platform', 'Vpc']
- **Required**: Yes

### RepositoryAuthConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RepositoryAuthConfigTypeDef]


# ImageTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# ImageVersionTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageVersionStatus
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# ImportHubContentRequestTypeDef

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### DocumentSchemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDocument
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentVersion
- **Type**: typing.Optional[str]

### HubContentDisplayName
- **Type**: typing.Optional[str]

### HubContentDescription
- **Type**: typing.Optional[str]

### HubContentMarkdown
- **Type**: typing.Optional[str]

### SupportStatus
- **Type**: typing.Optional[typing.Literal['Deprecated', 'Restricted', 'Supported']]

### HubContentSearchKeywords
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# ImportHubContentResponseTypeDef

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InferenceComponentCapacitySizeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceComponentComputeResourceRequirementsTypeDef

### MinMemoryRequiredInMb
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfCpuCoresRequired
- **Type**: typing.Optional[float]

### NumberOfAcceleratorDevicesRequired
- **Type**: typing.Optional[float]

### MaxMemoryRequiredInMb
- **Type**: typing.Optional[int]


# InferenceComponentContainerSpecificationSummaryTypeDef

### DeployedImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DeployedImageTypeDef]

### ArtifactUrl
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# InferenceComponentContainerSpecificationTypeDef

### Image
- **Type**: typing.Optional[str]

### ArtifactUrl
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# InferenceComponentDeploymentConfigOutputTypeDef

### RollingUpdatePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentRollingUpdatePolicyTypeDef'>
- **Required**: Yes

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoRollbackConfigOutputTypeDef]


# InferenceComponentDeploymentConfigTypeDef

### RollingUpdatePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentRollingUpdatePolicyTypeDef'>
- **Required**: Yes

### AutoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoRollbackConfigTypeDef]


# InferenceComponentDeploymentConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceComponentRollingUpdatePolicyTypeDef

### MaximumBatchSize
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentCapacitySizeTypeDef'>
- **Required**: Yes

### WaitIntervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumExecutionTimeoutInSeconds
- **Type**: typing.Optional[int]

### RollbackMaximumBatchSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentCapacitySizeTypeDef]


# InferenceComponentRuntimeConfigSummaryTypeDef

### DesiredCopyCount
- **Type**: typing.Optional[int]

### CurrentCopyCount
- **Type**: typing.Optional[int]


# InferenceComponentRuntimeConfigTypeDef

### CopyCount
- **Type**: <class 'int'>
- **Required**: Yes


# InferenceComponentSpecificationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceComponentSpecificationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceComponentStartupParametersTypeDef

### ModelDataDownloadTimeoutInSeconds
- **Type**: typing.Optional[int]

### ContainerStartupHealthCheckTimeoutInSeconds
- **Type**: typing.Optional[int]


# InferenceComponentSummaryTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InferenceComponentStatus
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']]


# InferenceExecutionConfigTypeDef

### Mode
- **Type**: typing.Literal['Direct', 'Serial']
- **Required**: Yes


# InferenceExperimentDataStorageConfigOutputTypeDef

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CaptureContentTypeHeaderOutputTypeDef]


# InferenceExperimentDataStorageConfigTypeDef

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKey
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CaptureContentTypeHeaderTypeDef]


# InferenceExperimentDataStorageConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceExperimentScheduleOutputTypeDef

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# InferenceExperimentScheduleTypeDef

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# InferenceExperimentScheduleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceExperimentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceHubAccessConfigTypeDef

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceMetricsTypeDef

### MaxInvocations
- **Type**: <class 'int'>
- **Required**: Yes

### ModelLatency
- **Type**: <class 'int'>
- **Required**: Yes


# InferenceRecommendationTypeDef

### EndpointConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EndpointOutputConfigurationTypeDef'>
- **Required**: Yes

### ModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelConfigurationTypeDef'>
- **Required**: Yes

### RecommendationId
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationMetricsTypeDef]

### InvocationEndTime
- **Type**: typing.Optional[datetime.datetime]

### InvocationStartTime
- **Type**: typing.Optional[datetime.datetime]


# InferenceRecommendationsJobStepTypeDef

### StepType
- **Type**: typing.Literal['BENCHMARK']
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### InferenceBenchmark
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobInferenceBenchmarkTypeDef]


# InferenceRecommendationsJobTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### JobDescription
- **Type**: <class 'str'>
- **Required**: Yes

### JobType
- **Type**: typing.Literal['Advanced', 'Default']
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### ModelPackageVersionArn
- **Type**: typing.Optional[str]


# InferenceSpecificationOutputTypeDef

### Containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageContainerDefinitionOutputTypeDef]
- **Required**: Yes

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# InferenceSpecificationTypeDef

### Containers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageContainerDefinitionTypeDef]
- **Required**: Yes

### SupportedTransformInstanceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']]]

### SupportedRealtimeInferenceInstanceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]]

### SupportedContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.Sequence[str]]


# InferenceSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InfraCheckConfigTypeDef

### EnableInfraCheck
- **Type**: typing.Optional[bool]


# InputConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### Framework
- **Type**: typing.Literal['DARKNET', 'KERAS', 'MXNET', 'ONNX', 'PYTORCH', 'SKLEARN', 'TENSORFLOW', 'TFLITE', 'XGBOOST']
- **Required**: Yes

### DataInputConfig
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]


# InstanceGroupTypeDef

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# InstanceMetadataServiceConfigurationTypeDef

### MinimumInstanceMetadataServiceVersion
- **Type**: <class 'str'>
- **Required**: Yes


# IntegerParameterRangeSpecificationTypeDef

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes


# IntegerParameterRangeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MinValue
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Linear', 'Logarithmic', 'ReverseLogarithmic']]


# JupyterLabAppImageConfigOutputTypeDef

### FileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemConfigTypeDef]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerConfigOutputTypeDef]


# JupyterLabAppImageConfigTypeDef

### FileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemConfigTypeDef]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerConfigTypeDef]


# JupyterLabAppImageConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JupyterLabAppSettingsOutputTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CodeRepositoryTypeDef]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AppLifecycleManagementTypeDef]

### EmrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EmrSettingsOutputTypeDef]

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# JupyterLabAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.Sequence[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CodeRepositoryTypeDef]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AppLifecycleManagementTypeDef]

### EmrSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EmrSettingsTypeDef]

### BuiltInLifecycleConfigArn
- **Type**: typing.Optional[str]


# JupyterServerAppSettingsOutputTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CodeRepositoryTypeDef]]


# JupyterServerAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.Sequence[str]]

### CodeRepositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CodeRepositoryTypeDef]]


# KendraSettingsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# KernelGatewayAppSettingsOutputTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.List[str]]


# KernelGatewayAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]

### LifecycleConfigArns
- **Type**: typing.Optional[typing.Sequence[str]]


# KernelGatewayImageConfigOutputTypeDef

### KernelSpecs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.KernelSpecTypeDef]
- **Required**: Yes

### FileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemConfigTypeDef]


# KernelGatewayImageConfigTypeDef

### KernelSpecs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.KernelSpecTypeDef]
- **Required**: Yes

### FileSystemConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FileSystemConfigTypeDef]


# KernelGatewayImageConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KernelSpecTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# LabelCountersForWorkteamTypeDef

### HumanLabeled
- **Type**: typing.Optional[int]

### PendingHuman
- **Type**: typing.Optional[int]

### Total
- **Type**: typing.Optional[int]


# LabelCountersTypeDef

### TotalLabeled
- **Type**: typing.Optional[int]

### HumanLabeled
- **Type**: typing.Optional[int]

### MachineLabeled
- **Type**: typing.Optional[int]

### FailedNonRetryableError
- **Type**: typing.Optional[int]

### Unlabeled
- **Type**: typing.Optional[int]


# LabelingJobAlgorithmsConfigOutputTypeDef

### LabelingJobAlgorithmSpecificationArn
- **Type**: <class 'str'>
- **Required**: Yes

### InitialActiveLearningModelArn
- **Type**: typing.Optional[str]

### LabelingJobResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobResourceConfigOutputTypeDef]


# LabelingJobAlgorithmsConfigTypeDef

### LabelingJobAlgorithmSpecificationArn
- **Type**: <class 'str'>
- **Required**: Yes

### InitialActiveLearningModelArn
- **Type**: typing.Optional[str]

### LabelingJobResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobResourceConfigTypeDef]


# LabelingJobAlgorithmsConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LabelingJobDataAttributesOutputTypeDef

### ContentClassifiers
- **Type**: typing.Optional[typing.List[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# LabelingJobDataAttributesTypeDef

### ContentClassifiers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# LabelingJobDataSourceTypeDef

### S3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobS3DataSourceTypeDef]

### SnsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobSnsDataSourceTypeDef]


# LabelingJobForWorkteamSummaryTypeDef

### JobReferenceCode
- **Type**: <class 'str'>
- **Required**: Yes

### WorkRequesterAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LabelingJobName
- **Type**: typing.Optional[str]

### LabelCounters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelCountersForWorkteamTypeDef]

### NumberOfHumanWorkersPerDataObject
- **Type**: typing.Optional[int]


# LabelingJobInputConfigOutputTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobDataSourceTypeDef'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobDataAttributesOutputTypeDef]


# LabelingJobInputConfigTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobDataSourceTypeDef'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobDataAttributesTypeDef]


# LabelingJobInputConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LabelingJobOutputConfigTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]


# LabelingJobOutputTypeDef

### OutputDatasetS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### FinalActiveLearningModelArn
- **Type**: typing.Optional[str]


# LabelingJobResourceConfigOutputTypeDef

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]


# LabelingJobResourceConfigTypeDef

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigTypeDef]


# LabelingJobS3DataSourceTypeDef

### ManifestS3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# LabelingJobSnsDataSourceTypeDef

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# LabelingJobStoppingConditionsTypeDef

### MaxHumanLabeledObjectCount
- **Type**: typing.Optional[int]

### MaxPercentageOfInputDatasetLabeled
- **Type**: typing.Optional[int]


# LabelingJobSummaryTypeDef

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LabelingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']
- **Required**: Yes

### LabelCounters
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.LabelCountersTypeDef'>
- **Required**: Yes

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### PreHumanTaskLambdaArn
- **Type**: typing.Optional[str]

### AnnotationConsolidationLambdaArn
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### LabelingJobOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobOutputTypeDef]

### InputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobInputConfigOutputTypeDef]


# LambdaStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]

### OutputParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.OutputParameterTypeDef]]


# LastUpdateStatusTypeDef

### Status
- **Type**: typing.Literal['Failed', 'InProgress', 'Successful']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# LineageGroupSummaryTypeDef

### LineageGroupArn
- **Type**: typing.Optional[str]

### LineageGroupName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ListActionsRequestPaginateTypeDef

### SourceUri
- **Type**: typing.Optional[str]

### ActionType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListActionsRequestTypeDef

### SourceUri
- **Type**: typing.Optional[str]

### ActionType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListActionsResponseTypeDef

### ActionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ActionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAlgorithmsInputPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListAlgorithmsInputTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListAlgorithmsOutputTypeDef

### AlgorithmSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAliasesRequestPaginateTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListAliasesRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAliasesResponseTypeDef

### SageMakerImageVersionAliases
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppImageConfigsRequestPaginateTypeDef

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListAppImageConfigsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListAppImageConfigsResponseTypeDef

### AppImageConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AppImageConfigDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppsRequestPaginateTypeDef

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameEquals
- **Type**: typing.Optional[str]

### SpaceNameEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListAppsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameEquals
- **Type**: typing.Optional[str]

### SpaceNameEquals
- **Type**: typing.Optional[str]


# ListAppsResponseTypeDef

### Apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AppDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArtifactsRequestPaginateTypeDef

### SourceUri
- **Type**: typing.Optional[str]

### ArtifactType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListArtifactsRequestTypeDef

### SourceUri
- **Type**: typing.Optional[str]

### ArtifactType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListArtifactsResponseTypeDef

### ArtifactSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ArtifactSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAssociationsRequestPaginateTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### DestinationType
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'DestinationArn', 'DestinationType', 'SourceArn', 'SourceType']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListAssociationsRequestTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### DestinationArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[str]

### DestinationType
- **Type**: typing.Optional[str]

### AssociationType
- **Type**: typing.Optional[typing.Literal['AssociatedWith', 'ContributedTo', 'DerivedFrom', 'Produced', 'SameAs']]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'DestinationArn', 'DestinationType', 'SourceArn', 'SourceType']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAssociationsResponseTypeDef

### AssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAutoMLJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListAutoMLJobsRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAutoMLJobsResponseTypeDef

### AutoMLJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCandidatesForAutoMLJobRequestPaginateTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### CandidateNameEquals
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Status']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListCandidatesForAutoMLJobRequestTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### CandidateNameEquals
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Status']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCandidatesForAutoMLJobResponseTypeDef

### Candidates
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLCandidateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClusterNodesRequestPaginateTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### InstanceGroupNameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListClusterNodesRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### InstanceGroupNameContains
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListClusterNodesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterNodeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterNodeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClusterSchedulerConfigsRequestPaginateTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListClusterSchedulerConfigsRequestTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListClusterSchedulerConfigsResponseTypeDef

### ClusterSchedulerConfigSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterSchedulerConfigSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### TrainingPlanArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListClustersRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### TrainingPlanArn
- **Type**: typing.Optional[str]


# ListClustersResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCodeRepositoriesInputPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListCodeRepositoriesInputTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListCodeRepositoriesOutputTypeDef

### CodeRepositorySummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CodeRepositorySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCompilationJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListCompilationJobsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListCompilationJobsResponseTypeDef

### CompilationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CompilationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComputeQuotasRequestPaginateTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### ClusterArn
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['ClusterArn', 'CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListComputeQuotasRequestTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'CreateRollbackFailed', 'Created', 'Creating', 'DeleteFailed', 'DeleteRollbackFailed', 'Deleted', 'Deleting', 'UpdateFailed', 'UpdateRollbackFailed', 'Updated', 'Updating']]

### ClusterArn
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['ClusterArn', 'CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListComputeQuotasResponseTypeDef

### ComputeQuotaSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListContextsRequestPaginateTypeDef

### SourceUri
- **Type**: typing.Optional[str]

### ContextType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListContextsRequestTypeDef

### SourceUri
- **Type**: typing.Optional[str]

### ContextType
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListContextsResponseTypeDef

### ContextSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ContextSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataQualityJobDefinitionsRequestPaginateTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListDataQualityJobDefinitionsRequestTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# ListDataQualityJobDefinitionsResponseTypeDef

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJobDefinitionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceFleetsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListDeviceFleetsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListDeviceFleetsResponseTypeDef

### DeviceFleetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DeviceFleetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesRequestPaginateTypeDef

### LatestHeartbeatAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModelName
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListDevicesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### LatestHeartbeatAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModelName
- **Type**: typing.Optional[str]

### DeviceFleetName
- **Type**: typing.Optional[str]


# ListDevicesResponseTypeDef

### DeviceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DeviceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListDomainsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDomainsResponseTypeDef

### Domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DomainDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEdgeDeploymentPlansRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### DeviceFleetNameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'DEVICE_FLEET_NAME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListEdgeDeploymentPlansRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### DeviceFleetNameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'DEVICE_FLEET_NAME', 'LAST_MODIFIED_TIME', 'NAME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListEdgeDeploymentPlansResponseTypeDef

### EdgeDeploymentPlanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeDeploymentPlanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEdgePackagingJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### ModelNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'MODEL_NAME', 'NAME', 'STATUS']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListEdgePackagingJobsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### ModelNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'MODEL_NAME', 'NAME', 'STATUS']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListEdgePackagingJobsResponseTypeDef

### EdgePackagingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EdgePackagingJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointConfigsInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListEndpointConfigsInputTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# ListEndpointConfigsOutputTypeDef

### EndpointConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointConfigSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListEndpointsInputTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']]


# ListEndpointsOutputTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperimentsRequestPaginateTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListExperimentsRequestTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListExperimentsResponseTypeDef

### ExperimentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFeatureGroupsRequestPaginateTypeDef

### NameContains
- **Type**: typing.Optional[str]

### FeatureGroupStatusEquals
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatusEquals
- **Type**: typing.Optional[typing.Literal['Active', 'Blocked', 'Disabled']]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FeatureGroupStatus', 'Name', 'OfflineStoreStatus']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListFeatureGroupsRequestTypeDef

### NameContains
- **Type**: typing.Optional[str]

### FeatureGroupStatusEquals
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting']]

### OfflineStoreStatusEquals
- **Type**: typing.Optional[typing.Literal['Active', 'Blocked', 'Disabled']]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FeatureGroupStatus', 'Name', 'OfflineStoreStatus']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFeatureGroupsResponseTypeDef

### FeatureGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlowDefinitionsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListFlowDefinitionsRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlowDefinitionsResponseTypeDef

### FlowDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.FlowDefinitionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentVersionsRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### MinVersion
- **Type**: typing.Optional[str]

### MaxSchemaVersion
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'HubContentName', 'HubContentStatus']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentVersionsResponseTypeDef

### HubContentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HubContentInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentsRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### NameContains
- **Type**: typing.Optional[str]

### MaxSchemaVersion
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'HubContentName', 'HubContentStatus']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHubContentsResponseTypeDef

### HubContentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HubContentInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHubsRequestTypeDef

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['AccountIdOwner', 'CreationTime', 'HubName', 'HubStatus']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHubsResponseTypeDef

### HubSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HubInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHumanTaskUisRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListHumanTaskUisRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListHumanTaskUisResponseTypeDef

### HumanTaskUiSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HumanTaskUiSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHyperParameterTuningJobsRequestPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListHyperParameterTuningJobsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Stopped', 'Stopping']]


# ListHyperParameterTuningJobsResponseTypeDef

### HyperParameterTuningJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImageVersionsRequestPaginateTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'VERSION']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListImageVersionsRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'LAST_MODIFIED_TIME', 'VERSION']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListImageVersionsResponseTypeDef

### ImageVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ImageVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImagesRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'IMAGE_NAME', 'LAST_MODIFIED_TIME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListImagesRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CREATION_TIME', 'IMAGE_NAME', 'LAST_MODIFIED_TIME']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# ListImagesResponseTypeDef

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ImageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceComponentsInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']]

### EndpointNameEquals
- **Type**: typing.Optional[str]

### VariantNameEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListInferenceComponentsInputTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'Updating']]

### EndpointNameEquals
- **Type**: typing.Optional[str]

### VariantNameEquals
- **Type**: typing.Optional[str]


# ListInferenceComponentsOutputTypeDef

### InferenceComponents
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceExperimentsResponseTypeDef

### InferenceExperiments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceExperimentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobStepsRequestPaginateTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### StepType
- **Type**: typing.Optional[typing.Literal['BENCHMARK']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListInferenceRecommendationsJobStepsRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### StepType
- **Type**: typing.Optional[typing.Literal['BENCHMARK']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobStepsResponseTypeDef

### Steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceRecommendationsJobStepTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### ModelNameEquals
- **Type**: typing.Optional[str]

### ModelPackageVersionArnEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListInferenceRecommendationsJobsRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'IN_PROGRESS', 'PENDING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ModelNameEquals
- **Type**: typing.Optional[str]

### ModelPackageVersionArnEquals
- **Type**: typing.Optional[str]


# ListInferenceRecommendationsJobsResponseTypeDef

### InferenceRecommendationsJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceRecommendationsJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelingJobsForWorkteamRequestPaginateTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### JobReferenceCodeContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListLabelingJobsForWorkteamRequestTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### JobReferenceCodeContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListLabelingJobsForWorkteamResponseTypeDef

### LabelingJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobForWorkteamSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelingJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListLabelingJobsRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']]


# ListLabelingJobsResponseTypeDef

### LabelingJobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.LabelingJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLineageGroupsRequestPaginateTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListLineageGroupsRequestTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLineageGroupsResponseTypeDef

### LineageGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.LineageGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMlflowTrackingServersRequestPaginateTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### TrackingServerStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']]

### MlflowVersion
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListMlflowTrackingServersRequestTypeDef

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### TrackingServerStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']]

### MlflowVersion
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMlflowTrackingServersResponseTypeDef

### TrackingServerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrackingServerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelBiasJobDefinitionsRequestPaginateTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelBiasJobDefinitionsRequestTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# ListModelBiasJobDefinitionsResponseTypeDef

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJobDefinitionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelCardExportJobsRequestPaginateTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModelCardExportJobNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelCardExportJobsRequestTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModelCardExportJobNameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelCardExportJobsResponseTypeDef

### ModelCardExportJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardExportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelCardVersionsRequestPaginateTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SortBy
- **Type**: typing.Optional[typing.Literal['Version']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelCardVersionsRequestTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['Version']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelCardVersionsResponseTypeDef

### ModelCardVersionSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelCardsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelCardsRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelCardsResponseTypeDef

### ModelCardSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelExplainabilityJobDefinitionsRequestPaginateTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelExplainabilityJobDefinitionsRequestTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# ListModelExplainabilityJobDefinitionsResponseTypeDef

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJobDefinitionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelMetadataRequestPaginateTypeDef

### SearchExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelMetadataSearchExpressionTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelMetadataRequestTypeDef

### SearchExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelMetadataSearchExpressionTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListModelMetadataResponseTypeDef

### ModelMetadataSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelMetadataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelPackageGroupsInputPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelPackageGroupsInputTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]


# ListModelPackageGroupsOutputTypeDef

### ModelPackageGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelPackagesInputPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageType
- **Type**: typing.Optional[typing.Literal['Both', 'Unversioned', 'Versioned']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelPackagesInputTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageType
- **Type**: typing.Optional[typing.Literal['Both', 'Unversioned', 'Versioned']]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListModelPackagesOutputTypeDef

### ModelPackageSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelQualityJobDefinitionsRequestPaginateTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelQualityJobDefinitionsRequestTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# ListModelQualityJobDefinitionsResponseTypeDef

### JobDefinitionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJobDefinitionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelsInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListModelsInputTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# ListModelsOutputTypeDef

### Models
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringAlertHistoryRequestPaginateTypeDef

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringAlertName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['InAlert', 'OK']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListMonitoringAlertHistoryRequestTypeDef

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringAlertName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['InAlert', 'OK']]


# ListMonitoringAlertHistoryResponseTypeDef

### MonitoringAlertHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringAlertHistorySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringAlertsRequestPaginateTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListMonitoringAlertsRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMonitoringAlertsResponseTypeDef

### MonitoringAlertSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringAlertSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringExecutionsRequestPaginateTypeDef

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'ScheduledTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### ScheduledTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ScheduledTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'CompletedWithViolations', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListMonitoringExecutionsRequestTypeDef

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'ScheduledTime', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ScheduledTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ScheduledTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'CompletedWithViolations', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# ListMonitoringExecutionsResponseTypeDef

### MonitoringExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoringSchedulesRequestPaginateTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListMonitoringSchedulesRequestTypeDef

### EndpointName
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringTypeEquals
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# ListMonitoringSchedulesResponseTypeDef

### MonitoringScheduleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringScheduleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookInstanceLifecycleConfigsInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListNotebookInstanceLifecycleConfigsInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]


# ListNotebookInstanceLifecycleConfigsOutputTypeDef

### NotebookInstanceLifecycleConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceLifecycleConfigSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotebookInstancesInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']]

### NotebookInstanceLifecycleConfigNameContains
- **Type**: typing.Optional[str]

### DefaultCodeRepositoryContains
- **Type**: typing.Optional[str]

### AdditionalCodeRepositoryEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListNotebookInstancesInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']]

### NotebookInstanceLifecycleConfigNameContains
- **Type**: typing.Optional[str]

### DefaultCodeRepositoryContains
- **Type**: typing.Optional[str]

### AdditionalCodeRepositoryEquals
- **Type**: typing.Optional[str]


# ListNotebookInstancesOutputTypeDef

### NotebookInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOptimizationJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### OptimizationContains
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListOptimizationJobsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### OptimizationContains
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListOptimizationJobsResponseTypeDef

### OptimizationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerAppsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListPartnerAppsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPartnerAppsResponseTypeDef

### Summaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PartnerAppSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionStepsRequestPaginateTypeDef

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListPipelineExecutionStepsRequestTypeDef

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListPipelineExecutionStepsResponseTypeDef

### PipelineExecutionSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineExecutionStepTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionsRequestPaginateTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'PipelineExecutionArn']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListPipelineExecutionsRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'PipelineExecutionArn']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPipelineExecutionsResponseTypeDef

### PipelineExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelineParametersForExecutionRequestPaginateTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListPipelineParametersForExecutionRequestTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPipelineParametersForExecutionResponseTypeDef

### PipelineParameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPipelinesRequestPaginateTypeDef

### PipelineNamePrefix
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListPipelinesRequestTypeDef

### PipelineNamePrefix
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPipelinesResponseTypeDef

### PipelineSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProcessingJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListProcessingJobsRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProcessingJobsResponseTypeDef

### ProcessingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProjectsInputTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListProjectsOutputTypeDef

### ProjectSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceCatalogsRequestPaginateTypeDef

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListResourceCatalogsRequestTypeDef

### NameContains
- **Type**: typing.Optional[str]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceCatalogsResponseTypeDef

### ResourceCatalogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceCatalogTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSpacesRequestPaginateTypeDef

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### SpaceNameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListSpacesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### SpaceNameContains
- **Type**: typing.Optional[str]


# ListSpacesResponseTypeDef

### Spaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStageDevicesRequestPaginateTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludeDevicesDeployedInOtherStage
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListStageDevicesRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ExcludeDevicesDeployedInOtherStage
- **Type**: typing.Optional[bool]


# ListStageDevicesResponseTypeDef

### DeviceDeploymentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DeviceDeploymentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStudioLifecycleConfigsRequestPaginateTypeDef

### NameContains
- **Type**: typing.Optional[str]

### AppTypeEquals
- **Type**: typing.Optional[typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListStudioLifecycleConfigsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### NameContains
- **Type**: typing.Optional[str]

### AppTypeEquals
- **Type**: typing.Optional[typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListStudioLifecycleConfigsResponseTypeDef

### StudioLifecycleConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.StudioLifecycleConfigDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubscribedWorkteamsRequestPaginateTypeDef

### NameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListSubscribedWorkteamsRequestTypeDef

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSubscribedWorkteamsResponseTypeDef

### SubscribedWorkteams
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.SubscribedWorkteamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsInputPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListTagsInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTagsOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrainingJobsForHyperParameterTuningJobRequestPaginateTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListTrainingJobsForHyperParameterTuningJobRequestTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'FinalObjectiveMetricValue', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListTrainingJobsForHyperParameterTuningJobResponseTypeDef

### TrainingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTrainingJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrainingJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### WarmPoolStatusEquals
- **Type**: typing.Optional[typing.Literal['Available', 'InUse', 'Reused', 'Terminated']]

### TrainingPlanArnEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListTrainingJobsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### WarmPoolStatusEquals
- **Type**: typing.Optional[typing.Literal['Available', 'InUse', 'Reused', 'Terminated']]

### TrainingPlanArnEquals
- **Type**: typing.Optional[str]


# ListTrainingJobsResponseTypeDef

### TrainingJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrainingPlansRequestPaginateTypeDef

### StartTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StartTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['StartTime', 'Status', 'TrainingPlanName']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingPlanFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListTrainingPlansRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### StartTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['StartTime', 'Status', 'TrainingPlanName']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingPlanFilterTypeDef]]


# ListTrainingPlansResponseTypeDef

### TrainingPlanSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingPlanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTransformJobsRequestPaginateTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListTransformJobsRequestTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### LastModifiedTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### NameContains
- **Type**: typing.Optional[str]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name', 'Status']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTransformJobsResponseTypeDef

### TransformJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrialComponentsRequestPaginateTypeDef

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListTrialComponentsRequestTypeDef

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrialComponentsResponseTypeDef

### TrialComponentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrialsRequestPaginateTypeDef

### ExperimentName
- **Type**: typing.Optional[str]

### TrialComponentName
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListTrialsRequestTypeDef

### ExperimentName
- **Type**: typing.Optional[str]

### TrialComponentName
- **Type**: typing.Optional[str]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrialsResponseTypeDef

### TrialSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrialSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserProfilesRequestPaginateTypeDef

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListUserProfilesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### SortBy
- **Type**: typing.Optional[typing.Literal['CreationTime', 'LastModifiedTime']]

### DomainIdEquals
- **Type**: typing.Optional[str]

### UserProfileNameContains
- **Type**: typing.Optional[str]


# ListUserProfilesResponseTypeDef

### UserProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.UserProfileDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkforcesRequestPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListWorkforcesRequestTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkforcesResponseTypeDef

### Workforces
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.WorkforceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkteamsRequestPaginateTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# ListWorkteamsRequestTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['CreateDate', 'Name']]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NameContains
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkteamsResponseTypeDef

### Workteams
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.WorkteamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberDefinitionOutputTypeDef

### CognitoMemberDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CognitoMemberDefinitionTypeDef]

### OidcMemberDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OidcMemberDefinitionOutputTypeDef]


# MemberDefinitionTypeDef

### CognitoMemberDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CognitoMemberDefinitionTypeDef]

### OidcMemberDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OidcMemberDefinitionUnionTypeDef]


# MemberDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetadataPropertiesTypeDef

### CommitId
- **Type**: typing.Optional[str]

### Repository
- **Type**: typing.Optional[str]

### GeneratedBy
- **Type**: typing.Optional[str]

### ProjectId
- **Type**: typing.Optional[str]


# MetricDataTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# MetricDatumTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricDefinitionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Regex
- **Type**: <class 'str'>
- **Required**: Yes


# MetricSpecificationTypeDef

### Predefined
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PredefinedMetricSpecificationTypeDef]

### Customized
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CustomizedMetricSpecificationTypeDef]


# MetricsSourceTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ContentDigest
- **Type**: typing.Optional[str]


# ModelAccessConfigTypeDef

### AcceptEula
- **Type**: <class 'bool'>
- **Required**: Yes


# ModelArtifactsTypeDef

### S3ModelArtifacts
- **Type**: <class 'str'>
- **Required**: Yes


# ModelBiasAppSpecificationOutputTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelBiasAppSpecificationTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ModelBiasAppSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelBiasBaselineConfigTypeDef

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringConstraintsResourceTypeDef]


# ModelBiasJobInputOutputTypeDef

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringGroundTruthS3InputTypeDef'>
- **Required**: Yes

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputOutputTypeDef]


# ModelBiasJobInputTypeDef

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringGroundTruthS3InputTypeDef'>
- **Required**: Yes

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputTypeDef]


# ModelBiasJobInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelCardExportArtifactsTypeDef

### S3ExportArtifacts
- **Type**: <class 'str'>
- **Required**: Yes


# ModelCardExportJobSummaryTypeDef

### ModelCardExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ModelCardExportOutputConfigTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes


# ModelCardSecurityConfigTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]


# ModelCardSummaryTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ModelCardTypeDef

### ModelCardArn
- **Type**: typing.Optional[str]

### ModelCardName
- **Type**: typing.Optional[str]

### ModelCardVersion
- **Type**: typing.Optional[int]

### Content
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardSecurityConfigTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ModelId
- **Type**: typing.Optional[str]

### RiskRating
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]


# ModelCardVersionSummaryTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelCardStatus
- **Type**: typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']
- **Required**: Yes

### ModelCardVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ModelClientConfigTypeDef

### InvocationsTimeoutInSeconds
- **Type**: typing.Optional[int]

### InvocationsMaxRetries
- **Type**: typing.Optional[int]


# ModelCompilationConfigOutputTypeDef

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelCompilationConfigTypeDef

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ModelCompilationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelConfigurationTypeDef

### InferenceSpecificationName
- **Type**: typing.Optional[str]

### EnvironmentParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EnvironmentParameterTypeDef]]

### CompilationJobName
- **Type**: typing.Optional[str]


# ModelDashboardEndpointTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndpointStatus
- **Type**: typing.Literal['Creating', 'Deleting', 'Failed', 'InService', 'OutOfService', 'RollingBack', 'SystemUpdating', 'UpdateRollbackFailed', 'Updating']
- **Required**: Yes


# ModelDashboardIndicatorActionTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# ModelDashboardModelCardTypeDef

### ModelCardArn
- **Type**: typing.Optional[str]

### ModelCardName
- **Type**: typing.Optional[str]

### ModelCardVersion
- **Type**: typing.Optional[int]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardSecurityConfigTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### ModelId
- **Type**: typing.Optional[str]

### RiskRating
- **Type**: typing.Optional[str]


# ModelDashboardModelTypeDef

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelTypeDef]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDashboardEndpointTypeDef]]

### LastBatchTransformJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobTypeDef]

### MonitoringSchedules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDashboardMonitoringScheduleTypeDef]]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDashboardModelCardTypeDef]


# ModelDashboardMonitoringScheduleTypeDef

### MonitoringScheduleArn
- **Type**: typing.Optional[str]

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringScheduleStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### FailureReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### MonitoringScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringScheduleConfigOutputTypeDef]

### EndpointName
- **Type**: typing.Optional[str]

### MonitoringAlertSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringAlertSummaryTypeDef]]

### LastMonitoringExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringExecutionSummaryTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputOutputTypeDef]


# ModelDataQualityTypeDef

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]


# ModelDataSourceTypeDef

### S3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.S3ModelDataSourceTypeDef]


# ModelDeployConfigTypeDef

### AutoGenerateEndpointName
- **Type**: typing.Optional[bool]

### EndpointName
- **Type**: typing.Optional[str]


# ModelDeployResultTypeDef

### EndpointName
- **Type**: typing.Optional[str]


# ModelDigestsTypeDef

### ArtifactDigest
- **Type**: typing.Optional[str]


# ModelExplainabilityAppSpecificationOutputTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelExplainabilityAppSpecificationTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigUri
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ModelExplainabilityAppSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelExplainabilityBaselineConfigTypeDef

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringConstraintsResourceTypeDef]


# ModelExplainabilityJobInputOutputTypeDef

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputOutputTypeDef]


# ModelExplainabilityJobInputTypeDef

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputTypeDef]


# ModelExplainabilityJobInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelInfrastructureConfigTypeDef

### InfrastructureType
- **Type**: typing.Literal['RealTimeInference']
- **Required**: Yes

### RealTimeInferenceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.RealTimeInferenceConfigTypeDef'>
- **Required**: Yes


# ModelInputTypeDef

### DataInputConfig
- **Type**: <class 'str'>
- **Required**: Yes


# ModelLatencyThresholdTypeDef

### Percentile
- **Type**: typing.Optional[str]

### ValueInMilliseconds
- **Type**: typing.Optional[int]


# ModelLifeCycleTypeDef

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### StageStatus
- **Type**: <class 'str'>
- **Required**: Yes

### StageDescription
- **Type**: typing.Optional[str]


# ModelMetadataFilterTypeDef

### Name
- **Type**: typing.Literal['Domain', 'Framework', 'FrameworkVersion', 'Task']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ModelMetadataSearchExpressionTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ModelMetadataFilterTypeDef]]


# ModelMetadataSummaryTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Framework
- **Type**: <class 'str'>
- **Required**: Yes

### Task
- **Type**: <class 'str'>
- **Required**: Yes

### Model
- **Type**: <class 'str'>
- **Required**: Yes

### FrameworkVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ModelMetricsTypeDef

### ModelQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelQualityTypeDef]

### ModelDataQuality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDataQualityTypeDef]

### Bias
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BiasTypeDef]

### Explainability
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExplainabilityTypeDef]


# ModelPackageContainerDefinitionOutputTypeDef

### Image
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerHostname
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDataSourceTypeDef]

### ProductId
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelInputTypeDef]

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### NearestModelName
- **Type**: typing.Optional[str]

### AdditionalS3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalS3DataSourceTypeDef]

### ModelDataETag
- **Type**: typing.Optional[str]


# ModelPackageContainerDefinitionTypeDef

### Image
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerHostname
- **Type**: typing.Optional[str]

### ImageDigest
- **Type**: typing.Optional[str]

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDataSourceTypeDef]

### ProductId
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ModelInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelInputTypeDef]

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### NearestModelName
- **Type**: typing.Optional[str]

### AdditionalS3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalS3DataSourceTypeDef]

### ModelDataETag
- **Type**: typing.Optional[str]


# ModelPackageContainerDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelPackageGroupSummaryTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelPackageGroupStatus
- **Type**: typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageGroupDescription
- **Type**: typing.Optional[str]


# ModelPackageGroupTypeDef

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageGroupArn
- **Type**: typing.Optional[str]

### ModelPackageGroupDescription
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### ModelPackageGroupStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'DeleteFailed', 'Deleting', 'Failed', 'InProgress', 'Pending']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# ModelPackageModelCardTypeDef

### ModelCardContent
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]


# ModelPackageSecurityConfigTypeDef

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# ModelPackageStatusDetailsTypeDef

### ValidationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageStatusItemTypeDef]
- **Required**: Yes

### ImageScanStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageStatusItemTypeDef]]


# ModelPackageStatusItemTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'NotStarted']
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]


# ModelPackageSummaryTypeDef

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModelPackageStatus
- **Type**: typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']
- **Required**: Yes

### ModelPackageName
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageVersion
- **Type**: typing.Optional[int]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]


# ModelPackageTypeDef

### ModelPackageName
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ModelPackageVersion
- **Type**: typing.Optional[int]

### ModelPackageArn
- **Type**: typing.Optional[str]

### ModelPackageDescription
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### InferenceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceSpecificationOutputTypeDef]

### SourceAlgorithmSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SourceAlgorithmSpecificationOutputTypeDef]

### ValidationSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageValidationSpecificationOutputTypeDef]

### ModelPackageStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Deleting', 'Failed', 'InProgress', 'Pending']]

### ModelPackageStatusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageStatusDetailsTypeDef]

### CertifyForMarketplace
- **Type**: typing.Optional[bool]

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### ModelMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelMetricsTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### ApprovalDescription
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### AdditionalInferenceSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalInferenceSpecificationDefinitionOutputTypeDef]]

### SourceUri
- **Type**: typing.Optional[str]

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageSecurityConfigTypeDef]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageModelCardTypeDef]

### ModelLifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelLifeCycleTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### CustomerMetadataProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### DriftCheckBaselines
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DriftCheckBaselinesTypeDef]

### SkipModelValidation
- **Type**: typing.Optional[typing.Literal['All', 'None']]


# ModelPackageValidationProfileOutputTypeDef

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobDefinitionOutputTypeDef'>
- **Required**: Yes


# ModelPackageValidationProfileTypeDef

### ProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobDefinitionTypeDef'>
- **Required**: Yes


# ModelPackageValidationSpecificationOutputTypeDef

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageValidationProfileOutputTypeDef]
- **Required**: Yes


# ModelPackageValidationSpecificationTypeDef

### ValidationRole
- **Type**: <class 'str'>
- **Required**: Yes

### ValidationProfiles
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageValidationProfileTypeDef]
- **Required**: Yes


# ModelPackageValidationSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelQualityAppSpecificationOutputTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelQualityAppSpecificationTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.Sequence[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ModelQualityAppSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelQualityBaselineConfigTypeDef

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringConstraintsResourceTypeDef]


# ModelQualityJobInputOutputTypeDef

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringGroundTruthS3InputTypeDef'>
- **Required**: Yes

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputOutputTypeDef]


# ModelQualityJobInputTypeDef

### GroundTruthS3Input
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringGroundTruthS3InputTypeDef'>
- **Required**: Yes

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputTypeDef]


# ModelQualityJobInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelQualityTypeDef

### Statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricsSourceTypeDef]


# ModelQuantizationConfigOutputTypeDef

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelQuantizationConfigTypeDef

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ModelQuantizationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelRegisterSettingsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CrossAccountModelRegisterRoleArn
- **Type**: typing.Optional[str]


# ModelShardingConfigOutputTypeDef

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelShardingConfigTypeDef

### Image
- **Type**: typing.Optional[str]

### OverrideEnvironment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ModelShardingConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# ModelSummaryTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ModelTypeDef

### ModelName
- **Type**: typing.Optional[str]

### PrimaryContainer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerDefinitionOutputTypeDef]

### Containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ContainerDefinitionOutputTypeDef]]

### InferenceExecutionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceExecutionConfigTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### ModelArn
- **Type**: typing.Optional[str]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### DeploymentRecommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentRecommendationTypeDef]


# ModelVariantConfigSummaryTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### InfrastructureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelInfrastructureConfigTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Creating', 'Deleted', 'Deleting', 'InService', 'Updating']
- **Required**: Yes


# ModelVariantConfigTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### InfrastructureConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelInfrastructureConfigTypeDef'>
- **Required**: Yes


# MonitoringAlertActionsTypeDef

### ModelDashboardIndicator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDashboardIndicatorActionTypeDef]


# MonitoringAlertHistorySummaryTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlertStatus
- **Type**: typing.Literal['InAlert', 'OK']
- **Required**: Yes


# MonitoringAlertSummaryTypeDef

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlertStatus
- **Type**: typing.Literal['InAlert', 'OK']
- **Required**: Yes

### DatapointsToAlert
- **Type**: <class 'int'>
- **Required**: Yes

### EvaluationPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringAlertActionsTypeDef'>
- **Required**: Yes


# MonitoringAppSpecificationOutputTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.List[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.List[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]


# MonitoringAppSpecificationTypeDef

### ImageUri
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerEntrypoint
- **Type**: typing.Optional[typing.Sequence[str]]

### ContainerArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### RecordPreprocessorSourceUri
- **Type**: typing.Optional[str]

### PostAnalyticsProcessorSourceUri
- **Type**: typing.Optional[str]


# MonitoringBaselineConfigTypeDef

### BaseliningJobName
- **Type**: typing.Optional[str]

### ConstraintsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringConstraintsResourceTypeDef]

### StatisticsResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStatisticsResourceTypeDef]


# MonitoringClusterConfigTypeDef

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeKmsKeyId
- **Type**: typing.Optional[str]


# MonitoringConstraintsResourceTypeDef

### S3Uri
- **Type**: typing.Optional[str]


# MonitoringCsvDatasetFormatTypeDef

### Header
- **Type**: typing.Optional[bool]


# MonitoringDatasetFormatOutputTypeDef

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringCsvDatasetFormatTypeDef]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJsonDatasetFormatTypeDef]

### Parquet
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# MonitoringDatasetFormatTypeDef

### Csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringCsvDatasetFormatTypeDef]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJsonDatasetFormatTypeDef]

### Parquet
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# MonitoringExecutionSummaryTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringExecutionStatus
- **Type**: typing.Literal['Completed', 'CompletedWithViolations', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping']
- **Required**: Yes

### ProcessingJobArn
- **Type**: typing.Optional[str]

### EndpointName
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringGroundTruthS3InputTypeDef

### S3Uri
- **Type**: typing.Optional[str]


# MonitoringInputOutputTypeDef

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputOutputTypeDef]


# MonitoringInputTypeDef

### EndpointInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputTypeDef]

### BatchTransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchTransformInputTypeDef]


# MonitoringJobDefinitionOutputTypeDef

### MonitoringInputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringInputOutputTypeDef]
- **Required**: Yes

### MonitoringOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigOutputTypeDef'>
- **Required**: Yes

### MonitoringResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### MonitoringAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringAppSpecificationOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringBaselineConfigTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NetworkConfigOutputTypeDef]


# MonitoringJobDefinitionSummaryTypeDef

### MonitoringJobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringJobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# MonitoringJobDefinitionTypeDef

### MonitoringInputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringInputTypeDef]
- **Required**: Yes

### MonitoringOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputConfigTypeDef'>
- **Required**: Yes

### MonitoringResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringResourcesTypeDef'>
- **Required**: Yes

### MonitoringAppSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringAppSpecificationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### BaselineConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringBaselineConfigTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringStoppingConditionTypeDef]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NetworkConfigTypeDef]


# MonitoringJsonDatasetFormatTypeDef

### Line
- **Type**: typing.Optional[bool]


# MonitoringNetworkConfigOutputTypeDef

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]


# MonitoringNetworkConfigTypeDef

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigTypeDef]


# MonitoringNetworkConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MonitoringOutputConfigOutputTypeDef

### MonitoringOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputTypeDef]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# MonitoringOutputConfigTypeDef

### MonitoringOutputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringOutputTypeDef]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# MonitoringOutputConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MonitoringOutputTypeDef

### S3Output
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringS3OutputTypeDef'>
- **Required**: Yes


# MonitoringResourcesTypeDef

### ClusterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringClusterConfigTypeDef'>
- **Required**: Yes


# MonitoringS3OutputTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: <class 'str'>
- **Required**: Yes

### S3UploadMode
- **Type**: typing.Optional[typing.Literal['Continuous', 'EndOfJob']]


# MonitoringScheduleConfigOutputTypeDef

### ScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ScheduleConfigTypeDef]

### MonitoringJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJobDefinitionOutputTypeDef]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringScheduleConfigTypeDef

### ScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ScheduleConfigTypeDef]

### MonitoringJobDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringJobDefinitionTypeDef]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringScheduleConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MonitoringScheduleSummaryTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MonitoringScheduleStatus
- **Type**: typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']
- **Required**: Yes

### EndpointName
- **Type**: typing.Optional[str]

### MonitoringJobDefinitionName
- **Type**: typing.Optional[str]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]


# MonitoringScheduleTypeDef

### MonitoringScheduleArn
- **Type**: typing.Optional[str]

### MonitoringScheduleName
- **Type**: typing.Optional[str]

### MonitoringScheduleStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'Pending', 'Scheduled', 'Stopped']]

### MonitoringType
- **Type**: typing.Optional[typing.Literal['DataQuality', 'ModelBias', 'ModelExplainability', 'ModelQuality']]

### FailureReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### MonitoringScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringScheduleConfigOutputTypeDef]

### EndpointName
- **Type**: typing.Optional[str]

### LastMonitoringExecutionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringExecutionSummaryTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# MonitoringStatisticsResourceTypeDef

### S3Uri
- **Type**: typing.Optional[str]


# MonitoringStoppingConditionTypeDef

### MaxRuntimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# MultiModelConfigTypeDef

### ModelCacheSetting
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# NeoVpcConfigOutputTypeDef

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# NeoVpcConfigTypeDef

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# NeoVpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NestedFiltersTypeDef

### NestedPropertyName
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.FilterTypeDef]
- **Required**: Yes


# NetworkConfigOutputTypeDef

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]


# NetworkConfigTypeDef

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigTypeDef]


# NetworkConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotebookInstanceLifecycleConfigSummaryTypeDef

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceLifecycleConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# NotebookInstanceLifecycleHookTypeDef

### Content
- **Type**: typing.Optional[str]


# NotebookInstanceSummaryTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NotebookInstanceStatus
- **Type**: typing.Optional[typing.Literal['Deleting', 'Failed', 'InService', 'Pending', 'Stopped', 'Stopping', 'Updating']]

### Url
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### NotebookInstanceLifecycleConfigName
- **Type**: typing.Optional[str]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.List[str]]


# NotificationConfigurationTypeDef

### NotificationTopicArn
- **Type**: typing.Optional[str]


# ObjectiveStatusCountersTypeDef

### Succeeded
- **Type**: typing.Optional[int]

### Pending
- **Type**: typing.Optional[int]

### Failed
- **Type**: typing.Optional[int]


# OfflineStoreConfigTypeDef

### S3StorageConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.S3StorageConfigTypeDef'>
- **Required**: Yes

### DisableGlueTableCreation
- **Type**: typing.Optional[bool]

### DataCatalogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DataCatalogConfigTypeDef]

### TableFormat
- **Type**: typing.Optional[typing.Literal['Default', 'Glue', 'Iceberg']]


# OfflineStoreStatusTypeDef

### Status
- **Type**: typing.Literal['Active', 'Blocked', 'Disabled']
- **Required**: Yes

### BlockedReason
- **Type**: typing.Optional[str]


# OidcConfigForResponseTypeDef

### ClientId
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### AuthorizationEndpoint
- **Type**: typing.Optional[str]

### TokenEndpoint
- **Type**: typing.Optional[str]

### UserInfoEndpoint
- **Type**: typing.Optional[str]

### LogoutEndpoint
- **Type**: typing.Optional[str]

### JwksUri
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Dict[str, str]]


# OidcConfigTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### TokenEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### UserInfoEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### LogoutEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### JwksUri
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Optional[str]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# OidcMemberDefinitionOutputTypeDef

### Groups
- **Type**: typing.Optional[typing.List[str]]


# OidcMemberDefinitionTypeDef

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]


# OidcMemberDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OnlineStoreConfigTypeDef

### SecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OnlineStoreSecurityConfigTypeDef]

### EnableOnlineStore
- **Type**: typing.Optional[bool]

### TtlDuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TtlDurationTypeDef]

### StorageType
- **Type**: typing.Optional[typing.Literal['InMemory', 'Standard']]


# OnlineStoreConfigUpdateTypeDef

### TtlDuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TtlDurationTypeDef]


# OnlineStoreSecurityConfigTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]


# OptimizationConfigOutputTypeDef

### ModelQuantizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelQuantizationConfigOutputTypeDef]

### ModelCompilationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCompilationConfigOutputTypeDef]

### ModelShardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelShardingConfigOutputTypeDef]


# OptimizationConfigTypeDef

### ModelQuantizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelQuantizationConfigUnionTypeDef]

### ModelCompilationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCompilationConfigUnionTypeDef]

### ModelShardingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelShardingConfigUnionTypeDef]


# OptimizationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OptimizationJobModelSourceS3TypeDef

### S3Uri
- **Type**: typing.Optional[str]

### ModelAccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationModelAccessConfigTypeDef]


# OptimizationJobModelSourceTypeDef

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OptimizationJobModelSourceS3TypeDef]


# OptimizationJobOutputConfigTypeDef

### S3OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# OptimizationJobSummaryTypeDef

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes

### OptimizationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OptimizationJobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INPROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### DeploymentInstanceType
- **Type**: typing.Literal['ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### OptimizationTypes
- **Type**: typing.List[str]
- **Required**: Yes

### OptimizationStartTime
- **Type**: typing.Optional[datetime.datetime]

### OptimizationEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# OptimizationModelAccessConfigTypeDef

### AcceptEula
- **Type**: <class 'bool'>
- **Required**: Yes


# OptimizationOutputTypeDef

### RecommendedInferenceImage
- **Type**: typing.Optional[str]


# OptimizationVpcConfigOutputTypeDef

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# OptimizationVpcConfigTypeDef

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# OptimizationVpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OutputConfigTypeDef

### S3OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### TargetDevice
- **Type**: typing.Optional[typing.Literal['aisage', 'amba_cv2', 'amba_cv22', 'amba_cv25', 'coreml', 'deeplens', 'imx8mplus', 'imx8qm', 'jacinto_tda4vm', 'jetson_nano', 'jetson_tx1', 'jetson_tx2', 'jetson_xavier', 'lambda', 'ml_c4', 'ml_c5', 'ml_c6g', 'ml_eia2', 'ml_g4dn', 'ml_inf1', 'ml_inf2', 'ml_m4', 'ml_m5', 'ml_m6g', 'ml_p2', 'ml_p3', 'ml_trn1', 'qcs603', 'qcs605', 'rasp3b', 'rasp4b', 'rk3288', 'rk3399', 'sbe_c', 'sitara_am57x', 'x86_win32', 'x86_win64']]

### TargetPlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TargetPlatformTypeDef]

### CompilerOptions
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# OutputDataConfigTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]


# OutputParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# OwnershipSettingsSummaryTypeDef

### OwnerUserProfileName
- **Type**: typing.Optional[str]


# OwnershipSettingsTypeDef

### OwnerUserProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParallelismConfigurationTypeDef

### MaxParallelExecutionSteps
- **Type**: <class 'int'>
- **Required**: Yes


# ParameterRangeOutputTypeDef

### IntegerParameterRangeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.IntegerParameterRangeSpecificationTypeDef]

### ContinuousParameterRangeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContinuousParameterRangeSpecificationTypeDef]

### CategoricalParameterRangeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CategoricalParameterRangeSpecificationOutputTypeDef]


# ParameterRangeTypeDef

### IntegerParameterRangeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.IntegerParameterRangeSpecificationTypeDef]

### ContinuousParameterRangeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ContinuousParameterRangeSpecificationTypeDef]

### CategoricalParameterRangeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CategoricalParameterRangeSpecificationTypeDef]


# ParameterRangesOutputTypeDef

### IntegerParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.IntegerParameterRangeTypeDef]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ContinuousParameterRangeTypeDef]]

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CategoricalParameterRangeOutputTypeDef]]

### AutoParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.AutoParameterTypeDef]]


# ParameterRangesTypeDef

### IntegerParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.IntegerParameterRangeTypeDef]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ContinuousParameterRangeTypeDef]]

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CategoricalParameterRangeUnionTypeDef]]

### AutoParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AutoParameterTypeDef]]


# ParameterRangesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ParentHyperParameterTuningJobTypeDef

### HyperParameterTuningJobName
- **Type**: typing.Optional[str]


# ParentTypeDef

### TrialName
- **Type**: typing.Optional[str]

### ExperimentName
- **Type**: typing.Optional[str]


# PartnerAppConfigOutputTypeDef

### AdminUsers
- **Type**: typing.Optional[typing.List[str]]

### Arguments
- **Type**: typing.Optional[typing.Dict[str, str]]


# PartnerAppConfigTypeDef

### AdminUsers
- **Type**: typing.Optional[typing.Sequence[str]]

### Arguments
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PartnerAppConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PartnerAppMaintenanceConfigTypeDef

### MaintenanceWindowStart
- **Type**: typing.Optional[str]


# PartnerAppSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PendingDeploymentSummaryTypeDef

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### ProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PendingProductionVariantSummaryTypeDef]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### ShadowProductionVariants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PendingProductionVariantSummaryTypeDef]]


# PendingProductionVariantSummaryTypeDef

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### DeployedImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DeployedImageTypeDef]]

### CurrentWeight
- **Type**: typing.Optional[float]

### DesiredWeight
- **Type**: typing.Optional[float]

### CurrentInstanceCount
- **Type**: typing.Optional[int]

### DesiredInstanceCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### AcceleratorType
- **Type**: typing.Optional[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]

### VariantStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantStatusTypeDef]]

### CurrentServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]

### DesiredServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]

### ManagedInstanceScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantManagedInstanceScalingTypeDef]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantRoutingConfigTypeDef]


# PhaseTypeDef

### InitialNumberOfUsers
- **Type**: typing.Optional[int]

### SpawnRate
- **Type**: typing.Optional[int]

### DurationInSeconds
- **Type**: typing.Optional[int]


# PipelineDefinitionS3LocationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKey
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: typing.Optional[str]


# PipelineExecutionStepMetadataTypeDef

### TrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobStepMetadataTypeDef]

### ProcessingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingJobStepMetadataTypeDef]

### TransformJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobStepMetadataTypeDef]

### TuningJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TuningJobStepMetaDataTypeDef]

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelStepMetadataTypeDef]

### RegisterModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RegisterModelStepMetadataTypeDef]

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ConditionStepMetadataTypeDef]

### Callback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CallbackStepMetadataTypeDef]

### Lambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.LambdaStepMetadataTypeDef]

### EMR
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EMRStepMetadataTypeDef]

### QualityCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.QualityCheckStepMetadataTypeDef]

### ClarifyCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ClarifyCheckStepMetadataTypeDef]

### Fail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FailStepMetadataTypeDef]

### AutoMLJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobStepMetadataTypeDef]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointStepMetadataTypeDef]

### EndpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointConfigStepMetadataTypeDef]


# PipelineExecutionStepTypeDef

### StepName
- **Type**: typing.Optional[str]

### StepDisplayName
- **Type**: typing.Optional[str]

### StepDescription
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StepStatus
- **Type**: typing.Optional[typing.Literal['Executing', 'Failed', 'Starting', 'Stopped', 'Stopping', 'Succeeded']]

### CacheHitResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CacheHitResultTypeDef]

### FailureReason
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineExecutionStepMetadataTypeDef]

### AttemptCount
- **Type**: typing.Optional[int]

### SelectiveExecutionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SelectiveExecutionResultTypeDef]


# PipelineExecutionSummaryTypeDef

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### PipelineExecutionStatus
- **Type**: typing.Optional[typing.Literal['Executing', 'Failed', 'Stopped', 'Stopping', 'Succeeded']]

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### PipelineExecutionFailureReason
- **Type**: typing.Optional[str]


# PipelineExecutionTypeDef

### PipelineArn
- **Type**: typing.Optional[str]

### PipelineExecutionArn
- **Type**: typing.Optional[str]

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### PipelineExecutionStatus
- **Type**: typing.Optional[typing.Literal['Executing', 'Failed', 'Stopped', 'Stopping', 'Succeeded']]

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### PipelineExperimentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineExperimentConfigTypeDef]

### FailureReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef]

### SelectiveExecutionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SelectiveExecutionConfigOutputTypeDef]

### PipelineParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ParameterTypeDef]]


# PipelineExperimentConfigTypeDef

### ExperimentName
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]


# PipelineSummaryTypeDef

### PipelineArn
- **Type**: typing.Optional[str]

### PipelineName
- **Type**: typing.Optional[str]

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDescription
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastExecutionTime
- **Type**: typing.Optional[datetime.datetime]


# PipelineTypeDef

### PipelineArn
- **Type**: typing.Optional[str]

### PipelineName
- **Type**: typing.Optional[str]

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDescription
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### PipelineStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Deleting']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastRunTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# PredefinedMetricSpecificationTypeDef

### PredefinedMetricType
- **Type**: typing.Optional[str]


# PriorityClassTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Weight
- **Type**: <class 'int'>
- **Required**: Yes


# ProcessingClusterConfigTypeDef

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']
- **Required**: Yes

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeKmsKeyId
- **Type**: typing.Optional[str]


# ProcessingFeatureStoreOutputTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ProcessingInputTypeDef

### InputName
- **Type**: <class 'str'>
- **Required**: Yes

### AppManaged
- **Type**: typing.Optional[bool]

### S3Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingS3InputTypeDef]

### DatasetDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DatasetDefinitionTypeDef]


# ProcessingJobStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# ProcessingJobSummaryTypeDef

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProcessingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProcessingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### ProcessingEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### ExitMessage
- **Type**: typing.Optional[str]


# ProcessingJobTypeDef

### ProcessingInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingInputTypeDef]]

### ProcessingOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingOutputConfigOutputTypeDef]

### ProcessingJobName
- **Type**: typing.Optional[str]

### ProcessingResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingResourcesTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingStoppingConditionTypeDef]

### AppSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AppSpecificationOutputTypeDef]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### NetworkConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NetworkConfigOutputTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### ExperimentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef]

### ProcessingJobArn
- **Type**: typing.Optional[str]

### ProcessingJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### ExitMessage
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]

### ProcessingEndTime
- **Type**: typing.Optional[datetime.datetime]

### ProcessingStartTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### MonitoringScheduleArn
- **Type**: typing.Optional[str]

### AutoMLJobArn
- **Type**: typing.Optional[str]

### TrainingJobArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# ProcessingOutputConfigOutputTypeDef

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingOutputTypeDef]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ProcessingOutputConfigTypeDef

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingOutputTypeDef]
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ProcessingOutputConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProcessingOutputTypeDef

### OutputName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingS3OutputTypeDef]

### FeatureStoreOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingFeatureStoreOutputTypeDef]

### AppManaged
- **Type**: typing.Optional[bool]


# ProcessingResourcesTypeDef

### ClusterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingClusterConfigTypeDef'>
- **Required**: Yes


# ProcessingS3InputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProcessingS3OutputTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### S3UploadMode
- **Type**: typing.Literal['Continuous', 'EndOfJob']
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]


# ProcessingStoppingConditionTypeDef

### MaxRuntimeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# ProductionVariantCoreDumpConfigTypeDef

### DestinationS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ProductionVariantManagedInstanceScalingTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### MinInstanceCount
- **Type**: typing.Optional[int]

### MaxInstanceCount
- **Type**: typing.Optional[int]


# ProductionVariantRoutingConfigTypeDef

### RoutingStrategy
- **Type**: typing.Literal['LEAST_OUTSTANDING_REQUESTS', 'RANDOM']
- **Required**: Yes


# ProductionVariantServerlessConfigTypeDef

### MemorySizeInMB
- **Type**: <class 'int'>
- **Required**: Yes

### MaxConcurrency
- **Type**: <class 'int'>
- **Required**: Yes

### ProvisionedConcurrency
- **Type**: typing.Optional[int]


# ProductionVariantServerlessUpdateConfigTypeDef

### MaxConcurrency
- **Type**: typing.Optional[int]

### ProvisionedConcurrency
- **Type**: typing.Optional[int]


# ProductionVariantStatusTypeDef

### Status
- **Type**: typing.Literal['ActivatingTraffic', 'Baking', 'Creating', 'Deleting', 'Updating']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# ProductionVariantSummaryTypeDef

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### DeployedImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DeployedImageTypeDef]]

### CurrentWeight
- **Type**: typing.Optional[float]

### DesiredWeight
- **Type**: typing.Optional[float]

### CurrentInstanceCount
- **Type**: typing.Optional[int]

### DesiredInstanceCount
- **Type**: typing.Optional[int]

### VariantStatus
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantStatusTypeDef]]

### CurrentServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]

### DesiredServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]

### ManagedInstanceScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantManagedInstanceScalingTypeDef]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantRoutingConfigTypeDef]


# ProductionVariantTypeDef

### VariantName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: typing.Optional[str]

### InitialInstanceCount
- **Type**: typing.Optional[int]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InitialVariantWeight
- **Type**: typing.Optional[float]

### AcceleratorType
- **Type**: typing.Optional[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]

### CoreDumpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantCoreDumpConfigTypeDef]

### ServerlessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantServerlessConfigTypeDef]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### ModelDataDownloadTimeoutInSeconds
- **Type**: typing.Optional[int]

### ContainerStartupHealthCheckTimeoutInSeconds
- **Type**: typing.Optional[int]

### EnableSSMAccess
- **Type**: typing.Optional[bool]

### ManagedInstanceScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantManagedInstanceScalingTypeDef]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProductionVariantRoutingConfigTypeDef]

### InferenceAmiVersion
- **Type**: typing.Optional[typing.Literal['al2-ami-sagemaker-inference-gpu-2', 'al2-ami-sagemaker-inference-gpu-2-1', 'al2-ami-sagemaker-inference-gpu-3-1']]


# ProfilerConfigForUpdateTypeDef

### S3OutputPath
- **Type**: typing.Optional[str]

### ProfilingIntervalInMilliseconds
- **Type**: typing.Optional[int]

### ProfilingParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DisableProfiler
- **Type**: typing.Optional[bool]


# ProfilerConfigOutputTypeDef

### S3OutputPath
- **Type**: typing.Optional[str]

### ProfilingIntervalInMilliseconds
- **Type**: typing.Optional[int]

### ProfilingParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### DisableProfiler
- **Type**: typing.Optional[bool]


# ProfilerConfigTypeDef

### S3OutputPath
- **Type**: typing.Optional[str]

### ProfilingIntervalInMilliseconds
- **Type**: typing.Optional[int]

### ProfilingParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DisableProfiler
- **Type**: typing.Optional[bool]


# ProfilerConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProfilerRuleConfigurationOutputTypeDef

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProfilerRuleConfigurationTypeDef

### RuleConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleEvaluatorImage
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]

### S3OutputPath
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge']]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### RuleParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ProfilerRuleConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProfilerRuleEvaluationStatusTypeDef

### RuleConfigurationName
- **Type**: typing.Optional[str]

### RuleEvaluationJobArn
- **Type**: typing.Optional[str]

### RuleEvaluationStatus
- **Type**: typing.Optional[typing.Literal['Error', 'InProgress', 'IssuesFound', 'NoIssuesFound', 'Stopped', 'Stopping']]

### StatusDetails
- **Type**: typing.Optional[str]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# ProjectSummaryTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProjectStatus
- **Type**: typing.Literal['CreateCompleted', 'CreateFailed', 'CreateInProgress', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'Pending', 'UpdateCompleted', 'UpdateFailed', 'UpdateInProgress']
- **Required**: Yes

### ProjectDescription
- **Type**: typing.Optional[str]


# ProjectTypeDef

### ProjectArn
- **Type**: typing.Optional[str]

### ProjectName
- **Type**: typing.Optional[str]

### ProjectId
- **Type**: typing.Optional[str]

### ProjectDescription
- **Type**: typing.Optional[str]

### ServiceCatalogProvisioningDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ServiceCatalogProvisioningDetailsOutputTypeDef]

### ServiceCatalogProvisionedProductDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ServiceCatalogProvisionedProductDetailsTypeDef]

### ProjectStatus
- **Type**: typing.Optional[typing.Literal['CreateCompleted', 'CreateFailed', 'CreateInProgress', 'DeleteCompleted', 'DeleteFailed', 'DeleteInProgress', 'Pending', 'UpdateCompleted', 'UpdateFailed', 'UpdateInProgress']]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]


# PropertyNameQueryTypeDef

### PropertyNameHint
- **Type**: <class 'str'>
- **Required**: Yes


# PropertyNameSuggestionTypeDef

### PropertyName
- **Type**: typing.Optional[str]


# ProvisioningParameterTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# PublicWorkforceTaskPriceTypeDef

### AmountInUsd
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.USDTypeDef]


# PutModelPackageGroupPolicyInputTypeDef

### ModelPackageGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutModelPackageGroupPolicyOutputTypeDef

### ModelPackageGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QualityCheckStepMetadataTypeDef

### CheckType
- **Type**: typing.Optional[str]

### BaselineUsedForDriftCheckStatistics
- **Type**: typing.Optional[str]

### BaselineUsedForDriftCheckConstraints
- **Type**: typing.Optional[str]

### CalculatedBaselineStatistics
- **Type**: typing.Optional[str]

### CalculatedBaselineConstraints
- **Type**: typing.Optional[str]

### ModelPackageGroupName
- **Type**: typing.Optional[str]

### ViolationReport
- **Type**: typing.Optional[str]

### CheckJobArn
- **Type**: typing.Optional[str]

### SkipCheck
- **Type**: typing.Optional[bool]

### RegisterNewBaseline
- **Type**: typing.Optional[bool]


# QueryFiltersTypeDef

### Types
- **Type**: typing.Optional[typing.Sequence[str]]

### LineageTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Action', 'Artifact', 'Context', 'TrialComponent']]]

### CreatedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### CreatedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### ModifiedAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# QueryLineageRequestTypeDef

### StartArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Direction
- **Type**: typing.Optional[typing.Literal['Ascendants', 'Both', 'Descendants']]

### IncludeEdges
- **Type**: typing.Optional[bool]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.QueryFiltersTypeDef]

### MaxDepth
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# QueryLineageResponseTypeDef

### Vertices
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.VertexTypeDef]
- **Required**: Yes

### Edges
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EdgeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# RSessionAppSettingsOutputTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]


# RSessionAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CustomImages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CustomImageTypeDef]]


# RStudioServerProAppSettingsTypeDef

### AccessStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### UserGroup
- **Type**: typing.Optional[typing.Literal['R_STUDIO_ADMIN', 'R_STUDIO_USER']]


# RStudioServerProDomainSettingsForUpdateTypeDef

### DomainExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### RStudioConnectUrl
- **Type**: typing.Optional[str]

### RStudioPackageManagerUrl
- **Type**: typing.Optional[str]


# RStudioServerProDomainSettingsTypeDef

### DomainExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RStudioConnectUrl
- **Type**: typing.Optional[str]

### RStudioPackageManagerUrl
- **Type**: typing.Optional[str]

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]


# RealTimeInferenceConfigTypeDef

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes


# RealTimeInferenceRecommendationTypeDef

### RecommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.large', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.large', 'ml.c5d.xlarge', 'ml.c6g.12xlarge', 'ml.c6g.16xlarge', 'ml.c6g.2xlarge', 'ml.c6g.4xlarge', 'ml.c6g.8xlarge', 'ml.c6g.large', 'ml.c6g.xlarge', 'ml.c6gd.12xlarge', 'ml.c6gd.16xlarge', 'ml.c6gd.2xlarge', 'ml.c6gd.4xlarge', 'ml.c6gd.8xlarge', 'ml.c6gd.large', 'ml.c6gd.xlarge', 'ml.c6gn.12xlarge', 'ml.c6gn.16xlarge', 'ml.c6gn.2xlarge', 'ml.c6gn.4xlarge', 'ml.c6gn.8xlarge', 'ml.c6gn.large', 'ml.c6gn.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7g.12xlarge', 'ml.c7g.16xlarge', 'ml.c7g.2xlarge', 'ml.c7g.4xlarge', 'ml.c7g.8xlarge', 'ml.c7g.large', 'ml.c7g.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.dl1.24xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6g.12xlarge', 'ml.m6g.16xlarge', 'ml.m6g.2xlarge', 'ml.m6g.4xlarge', 'ml.m6g.8xlarge', 'ml.m6g.large', 'ml.m6g.xlarge', 'ml.m6gd.12xlarge', 'ml.m6gd.16xlarge', 'ml.m6gd.2xlarge', 'ml.m6gd.4xlarge', 'ml.m6gd.8xlarge', 'ml.m6gd.large', 'ml.m6gd.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.r6g.12xlarge', 'ml.r6g.16xlarge', 'ml.r6g.2xlarge', 'ml.r6g.4xlarge', 'ml.r6g.8xlarge', 'ml.r6g.large', 'ml.r6g.xlarge', 'ml.r6gd.12xlarge', 'ml.r6gd.16xlarge', 'ml.r6gd.2xlarge', 'ml.r6gd.4xlarge', 'ml.r6gd.8xlarge', 'ml.r6gd.large', 'ml.r6gd.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.r8g.12xlarge', 'ml.r8g.16xlarge', 'ml.r8g.24xlarge', 'ml.r8g.2xlarge', 'ml.r8g.48xlarge', 'ml.r8g.4xlarge', 'ml.r8g.8xlarge', 'ml.r8g.large', 'ml.r8g.medium', 'ml.r8g.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecommendationJobCompiledOutputConfigTypeDef

### S3OutputUri
- **Type**: typing.Optional[str]


# RecommendationJobContainerConfigOutputTypeDef

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### PayloadConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobPayloadConfigOutputTypeDef]

### NearestModelName
- **Type**: typing.Optional[str]

### SupportedInstanceTypes
- **Type**: typing.Optional[typing.List[str]]

### SupportedEndpointType
- **Type**: typing.Optional[typing.Literal['RealTime', 'Serverless']]

### DataInputConfig
- **Type**: typing.Optional[str]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.List[str]]


# RecommendationJobContainerConfigTypeDef

### Domain
- **Type**: typing.Optional[str]

### Task
- **Type**: typing.Optional[str]

### Framework
- **Type**: typing.Optional[str]

### FrameworkVersion
- **Type**: typing.Optional[str]

### PayloadConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobPayloadConfigTypeDef]

### NearestModelName
- **Type**: typing.Optional[str]

### SupportedInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### SupportedEndpointType
- **Type**: typing.Optional[typing.Literal['RealTime', 'Serverless']]

### DataInputConfig
- **Type**: typing.Optional[str]

### SupportedResponseMIMETypes
- **Type**: typing.Optional[typing.Sequence[str]]


# RecommendationJobInferenceBenchmarkTypeDef

### ModelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ModelConfigurationTypeDef'>
- **Required**: Yes

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationMetricsTypeDef]

### EndpointMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceMetricsTypeDef]

### EndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointOutputConfigurationTypeDef]

### FailureReason
- **Type**: typing.Optional[str]

### InvocationEndTime
- **Type**: typing.Optional[datetime.datetime]

### InvocationStartTime
- **Type**: typing.Optional[datetime.datetime]


# RecommendationJobInputConfigOutputTypeDef

### ModelPackageVersionArn
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### JobDurationInSeconds
- **Type**: typing.Optional[int]

### TrafficPattern
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrafficPatternOutputTypeDef]

### ResourceLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobResourceLimitTypeDef]

### EndpointConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputConfigurationOutputTypeDef]]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobContainerConfigOutputTypeDef]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInfoTypeDef]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobVpcConfigOutputTypeDef]


# RecommendationJobInputConfigTypeDef

### ModelPackageVersionArn
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### JobDurationInSeconds
- **Type**: typing.Optional[int]

### TrafficPattern
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrafficPatternTypeDef]

### ResourceLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobResourceLimitTypeDef]

### EndpointConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInputConfigurationTypeDef]]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### ContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobContainerConfigTypeDef]

### Endpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointInfoTypeDef]]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobVpcConfigTypeDef]


# RecommendationJobInputConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationJobOutputConfigTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]

### CompiledOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RecommendationJobCompiledOutputConfigTypeDef]


# RecommendationJobPayloadConfigOutputTypeDef

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### SupportedContentTypes
- **Type**: typing.Optional[typing.List[str]]


# RecommendationJobPayloadConfigTypeDef

### SamplePayloadUrl
- **Type**: typing.Optional[str]

### SupportedContentTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# RecommendationJobResourceLimitTypeDef

### MaxNumberOfTests
- **Type**: typing.Optional[int]

### MaxParallelOfTests
- **Type**: typing.Optional[int]


# RecommendationJobStoppingConditionsOutputTypeDef

### MaxInvocations
- **Type**: typing.Optional[int]

### ModelLatencyThresholds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ModelLatencyThresholdTypeDef]]

### FlatInvocations
- **Type**: typing.Optional[typing.Literal['Continue', 'Stop']]


# RecommendationJobStoppingConditionsTypeDef

### MaxInvocations
- **Type**: typing.Optional[int]

### ModelLatencyThresholds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ModelLatencyThresholdTypeDef]]

### FlatInvocations
- **Type**: typing.Optional[typing.Literal['Continue', 'Stop']]


# RecommendationJobStoppingConditionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationJobVpcConfigOutputTypeDef

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# RecommendationJobVpcConfigTypeDef

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RecommendationMetricsTypeDef

### CostPerHour
- **Type**: typing.Optional[float]

### CostPerInference
- **Type**: typing.Optional[float]

### MaxInvocations
- **Type**: typing.Optional[int]

### ModelLatency
- **Type**: typing.Optional[int]

### CpuUtilization
- **Type**: typing.Optional[float]

### MemoryUtilization
- **Type**: typing.Optional[float]

### ModelSetupTime
- **Type**: typing.Optional[int]


# RedshiftDatasetDefinitionTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Literal['CSV', 'PARQUET']
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### OutputCompression
- **Type**: typing.Optional[typing.Literal['BZIP2', 'GZIP', 'None', 'SNAPPY', 'ZSTD']]


# RegisterDevicesRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### Devices
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.DeviceTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# RegisterModelStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# RemoteDebugConfigForUpdateTypeDef

### EnableRemoteDebug
- **Type**: typing.Optional[bool]


# RemoteDebugConfigTypeDef

### EnableRemoteDebug
- **Type**: typing.Optional[bool]


# RenderUiTemplateRequestTypeDef

### Task
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.RenderableTaskTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### UiTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UiTemplateTypeDef]

### HumanTaskUiArn
- **Type**: typing.Optional[str]


# RenderUiTemplateResponseTypeDef

### RenderedContent
- **Type**: <class 'str'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.RenderingErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RenderableTaskTypeDef

### Input
- **Type**: <class 'str'>
- **Required**: Yes


# RenderingErrorTypeDef

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes


# RepositoryAuthConfigTypeDef

### RepositoryCredentialsProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReservedCapacityOfferingTypeDef

### InstanceType
- **Type**: typing.Literal['ml.p4d.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.trn1.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# ReservedCapacitySummaryTypeDef

### ReservedCapacityArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Literal['ml.p4d.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.trn1.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### TotalInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Expired', 'Failed', 'Pending', 'Scheduled']
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# ResolvedAttributesTypeDef

### AutoMLJobObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobObjectiveTypeDef]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]


# ResourceCatalogTypeDef

### ResourceCatalogArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceCatalogName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ResourceConfigForUpdateTypeDef

### KeepAlivePeriodInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# ResourceConfigOutputTypeDef

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### KeepAlivePeriodInSeconds
- **Type**: typing.Optional[int]

### InstanceGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.InstanceGroupTypeDef]]

### TrainingPlanArn
- **Type**: typing.Optional[str]


# ResourceConfigTypeDef

### VolumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]

### InstanceCount
- **Type**: typing.Optional[int]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### KeepAlivePeriodInSeconds
- **Type**: typing.Optional[int]

### InstanceGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.InstanceGroupTypeDef]]

### TrainingPlanArn
- **Type**: typing.Optional[str]


# ResourceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceLimitsTypeDef

### MaxParallelTrainingJobs
- **Type**: <class 'int'>
- **Required**: Yes

### MaxNumberOfTrainingJobs
- **Type**: typing.Optional[int]

### MaxRuntimeInSeconds
- **Type**: typing.Optional[int]


# ResourceSharingConfigTypeDef

### Strategy
- **Type**: typing.Literal['DontLend', 'Lend', 'LendAndBorrow']
- **Required**: Yes

### BorrowLimit
- **Type**: typing.Optional[int]


# ResourceSpecTypeDef

### SageMakerImageArn
- **Type**: typing.Optional[str]

### SageMakerImageVersionArn
- **Type**: typing.Optional[str]

### SageMakerImageVersionAlias
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.geospatial.interactive', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.micro', 'ml.t3.small', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'system']]

### LifecycleConfigArn
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

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


# RetentionPolicyTypeDef

### HomeEfsFileSystem
- **Type**: typing.Optional[typing.Literal['Delete', 'Retain']]


# RetryPipelineExecutionRequestTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef]


# RetryPipelineExecutionResponseTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetryStrategyTypeDef

### MaximumRetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


# RollingUpdatePolicyTypeDef

### MaximumBatchSize
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.CapacitySizeTypeDef'>
- **Required**: Yes

### WaitIntervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumExecutionTimeoutInSeconds
- **Type**: typing.Optional[int]

### RollbackMaximumBatchSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CapacitySizeTypeDef]


# S3DataSourceOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3DataSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3ModelDataSourceTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### S3DataType
- **Type**: typing.Literal['S3Object', 'S3Prefix']
- **Required**: Yes

### CompressionType
- **Type**: typing.Literal['Gzip', 'None']
- **Required**: Yes

### ModelAccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelAccessConfigTypeDef]

### HubAccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceHubAccessConfigTypeDef]

### ManifestS3Uri
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]

### ManifestEtag
- **Type**: typing.Optional[str]


# S3PresignTypeDef

### IamPolicyConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.IamPolicyConstraintsTypeDef]


# S3StorageConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### ResolvedOutputS3Uri
- **Type**: typing.Optional[str]


# ScalingPolicyMetricTypeDef

### InvocationsPerInstance
- **Type**: typing.Optional[int]

### ModelLatency
- **Type**: typing.Optional[int]


# ScalingPolicyObjectiveTypeDef

### MinInvocationsPerMinute
- **Type**: typing.Optional[int]

### MaxInvocationsPerMinute
- **Type**: typing.Optional[int]


# ScalingPolicyTypeDef

### TargetTracking
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TargetTrackingScalingPolicyConfigurationTypeDef]


# ScheduleConfigTypeDef

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DataAnalysisStartTime
- **Type**: typing.Optional[str]

### DataAnalysisEndTime
- **Type**: typing.Optional[str]


# SchedulerConfigOutputTypeDef

### PriorityClasses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PriorityClassTypeDef]]

### FairShare
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SchedulerConfigTypeDef

### PriorityClasses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.PriorityClassTypeDef]]

### FairShare
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# SchedulerConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchExpressionPaginatorTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.FilterTypeDef]]

### NestedFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.NestedFiltersTypeDef]]

### SubExpressions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### Operator
- **Type**: typing.Optional[typing.Literal['And', 'Or']]


# SearchExpressionTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.FilterTypeDef]]

### NestedFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.NestedFiltersTypeDef]]

### SubExpressions
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### Operator
- **Type**: typing.Optional[typing.Literal['And', 'Or']]


# SearchRecordTypeDef

### TrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobTypeDef]

### Experiment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentTypeDef]

### Trial
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialTypeDef]

### TrialComponent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentTypeDef]

### Endpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EndpointTypeDef]

### ModelPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageTypeDef]

### ModelPackageGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageGroupTypeDef]

### Pipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineTypeDef]

### PipelineExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineExecutionTypeDef]

### FeatureGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureGroupTypeDef]

### FeatureMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureMetadataTypeDef]

### Project
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProjectTypeDef]

### HyperParameterTuningJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobSearchEntityTypeDef]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelCardTypeDef]

### Model
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDashboardModelTypeDef]


# SearchRequestPaginateTypeDef

### Resource
- **Type**: typing.Literal['Endpoint', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'FeatureGroup', 'FeatureMetadata', 'HyperParameterTuningJob', 'Image', 'ImageVersion', 'Model', 'ModelCard', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'Project', 'TrainingJob']
- **Required**: Yes

### SearchExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SearchExpressionPaginatorTypeDef]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]

### VisibilityConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.VisibilityConditionsTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PaginatorConfigTypeDef]


# SearchRequestTypeDef

### Resource
- **Type**: typing.Literal['Endpoint', 'Experiment', 'ExperimentTrial', 'ExperimentTrialComponent', 'FeatureGroup', 'FeatureMetadata', 'HyperParameterTuningJob', 'Image', 'ImageVersion', 'Model', 'ModelCard', 'ModelPackage', 'ModelPackageGroup', 'Pipeline', 'PipelineExecution', 'Project', 'TrainingJob']
- **Required**: Yes

### SearchExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SearchExpressionTypeDef]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### CrossAccountFilterOption
- **Type**: typing.Optional[typing.Literal['CrossAccount', 'SameAccount']]

### VisibilityConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.VisibilityConditionsTypeDef]]


# SearchResponseTypeDef

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.SearchRecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchTrainingPlanOfferingsRequestTypeDef

### InstanceType
- **Type**: typing.Literal['ml.p4d.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.trn1.32xlarge', 'ml.trn2.48xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### TargetResources
- **Type**: typing.Sequence[typing.Literal['hyperpod-cluster', 'training-job']]
- **Required**: Yes

### StartTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### EndTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### DurationHours
- **Type**: typing.Optional[int]


# SearchTrainingPlanOfferingsResponseTypeDef

### TrainingPlanOfferings
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingPlanOfferingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SecondaryStatusTransitionTypeDef

### Status
- **Type**: typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### StatusMessage
- **Type**: typing.Optional[str]


# SelectedStepTypeDef

### StepName
- **Type**: <class 'str'>
- **Required**: Yes


# SelectiveExecutionConfigOutputTypeDef

### SelectedSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.SelectedStepTypeDef]
- **Required**: Yes

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# SelectiveExecutionConfigTypeDef

### SelectedSteps
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.SelectedStepTypeDef]
- **Required**: Yes

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# SelectiveExecutionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SelectiveExecutionResultTypeDef

### SourcePipelineExecutionArn
- **Type**: typing.Optional[str]


# SendPipelineExecutionStepFailureRequestTypeDef

### CallbackToken
- **Type**: <class 'str'>
- **Required**: Yes

### FailureReason
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# SendPipelineExecutionStepFailureResponseTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendPipelineExecutionStepSuccessRequestTypeDef

### CallbackToken
- **Type**: <class 'str'>
- **Required**: Yes

### OutputParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.OutputParameterTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# SendPipelineExecutionStepSuccessResponseTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceCatalogProvisionedProductDetailsTypeDef

### ProvisionedProductId
- **Type**: typing.Optional[str]

### ProvisionedProductStatusMessage
- **Type**: typing.Optional[str]


# ServiceCatalogProvisioningDetailsOutputTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ProvisioningParameterTypeDef]]


# ServiceCatalogProvisioningDetailsTypeDef

### ProductId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### PathId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProvisioningParameterTypeDef]]


# ServiceCatalogProvisioningDetailsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceCatalogProvisioningUpdateDetailsTypeDef

### ProvisioningArtifactId
- **Type**: typing.Optional[str]

### ProvisioningParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProvisioningParameterTypeDef]]


# SessionChainingConfigTypeDef

### EnableSessionTagChaining
- **Type**: typing.Optional[bool]


# ShadowModeConfigOutputTypeDef

### SourceModelVariantName
- **Type**: <class 'str'>
- **Required**: Yes

### ShadowModelVariants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ShadowModelVariantConfigTypeDef]
- **Required**: Yes


# ShadowModeConfigTypeDef

### SourceModelVariantName
- **Type**: <class 'str'>
- **Required**: Yes

### ShadowModelVariants
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ShadowModelVariantConfigTypeDef]
- **Required**: Yes


# ShadowModeConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ShadowModelVariantConfigTypeDef

### ShadowModelVariantName
- **Type**: <class 'str'>
- **Required**: Yes

### SamplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# SharingSettingsTypeDef

### NotebookOutputOption
- **Type**: typing.Optional[typing.Literal['Allowed', 'Disabled']]

### S3OutputPath
- **Type**: typing.Optional[str]

### S3KmsKeyId
- **Type**: typing.Optional[str]


# ShuffleConfigTypeDef

### Seed
- **Type**: <class 'int'>
- **Required**: Yes


# SourceAlgorithmSpecificationOutputTypeDef

### SourceAlgorithms
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.SourceAlgorithmTypeDef]
- **Required**: Yes


# SourceAlgorithmSpecificationTypeDef

### SourceAlgorithms
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.SourceAlgorithmTypeDef]
- **Required**: Yes


# SourceAlgorithmSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceAlgorithmTypeDef

### AlgorithmName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelDataUrl
- **Type**: typing.Optional[str]

### ModelDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelDataSourceTypeDef]

### ModelDataETag
- **Type**: typing.Optional[str]


# SourceIpConfigOutputTypeDef

### Cidrs
- **Type**: typing.List[str]
- **Required**: Yes


# SourceIpConfigTypeDef

### Cidrs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SourceIpConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SpaceAppLifecycleManagementTypeDef

### IdleSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceIdleSettingsTypeDef]


# SpaceCodeEditorAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceAppLifecycleManagementTypeDef]


# SpaceDetailsTypeDef

### DomainId
- **Type**: typing.Optional[str]

### SpaceName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SpaceSettingsSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceSettingsSummaryTypeDef]

### SpaceSharingSettingsSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceSharingSettingsSummaryTypeDef]

### OwnershipSettingsSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OwnershipSettingsSummaryTypeDef]

### SpaceDisplayName
- **Type**: typing.Optional[str]


# SpaceIdleSettingsTypeDef

### IdleTimeoutInMinutes
- **Type**: typing.Optional[int]


# SpaceJupyterLabAppSettingsOutputTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CodeRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CodeRepositoryTypeDef]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceAppLifecycleManagementTypeDef]


# SpaceJupyterLabAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]

### CodeRepositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CodeRepositoryTypeDef]]

### AppLifecycleManagement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceAppLifecycleManagementTypeDef]


# SpaceSettingsOutputTypeDef

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterServerAppSettingsOutputTypeDef]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayAppSettingsOutputTypeDef]

### CodeEditorAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceCodeEditorAppSettingsTypeDef]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceJupyterLabAppSettingsOutputTypeDef]

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceStorageSettingsTypeDef]

### CustomFileSystems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CustomFileSystemTypeDef]]


# SpaceSettingsSummaryTypeDef

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceStorageSettingsTypeDef]


# SpaceSettingsTypeDef

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterServerAppSettingsTypeDef]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayAppSettingsTypeDef]

### CodeEditorAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceCodeEditorAppSettingsTypeDef]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceJupyterLabAppSettingsTypeDef]

### AppType
- **Type**: typing.Optional[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceStorageSettingsTypeDef]

### CustomFileSystems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CustomFileSystemTypeDef]]


# SpaceSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SpaceSharingSettingsSummaryTypeDef

### SharingType
- **Type**: typing.Optional[typing.Literal['Private', 'Shared']]


# SpaceSharingSettingsTypeDef

### SharingType
- **Type**: typing.Literal['Private', 'Shared']
- **Required**: Yes


# SpaceStorageSettingsTypeDef

### EbsStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.EbsStorageSettingsTypeDef]


# StairsTypeDef

### DurationInSeconds
- **Type**: typing.Optional[int]

### NumberOfSteps
- **Type**: typing.Optional[int]

### UsersPerStep
- **Type**: typing.Optional[int]


# StartEdgeDeploymentStageRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# StartInferenceExperimentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartInferenceExperimentResponseTypeDef

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMlflowTrackingServerRequestTypeDef

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartMlflowTrackingServerResponseTypeDef

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMonitoringScheduleRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# StartNotebookInstanceInputTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipelineExecutionRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### PipelineParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ParameterTypeDef]]

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef]

### SelectiveExecutionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SelectiveExecutionConfigUnionTypeDef]


# StartPipelineExecutionResponseTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopAutoMLJobRequestTypeDef

### AutoMLJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopCompilationJobRequestTypeDef

### CompilationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopEdgeDeploymentStageRequestTypeDef

### EdgeDeploymentPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### StageName
- **Type**: <class 'str'>
- **Required**: Yes


# StopEdgePackagingJobRequestTypeDef

### EdgePackagingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopHyperParameterTuningJobRequestTypeDef

### HyperParameterTuningJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopInferenceExperimentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVariantActions
- **Type**: typing.Mapping[str, typing.Literal['Promote', 'Remove', 'Retain']]
- **Required**: Yes

### DesiredModelVariants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ModelVariantConfigTypeDef]]

### DesiredState
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Completed']]

### Reason
- **Type**: typing.Optional[str]


# StopInferenceExperimentResponseTypeDef

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopInferenceRecommendationsJobRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopLabelingJobRequestTypeDef

### LabelingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopMlflowTrackingServerRequestTypeDef

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopMlflowTrackingServerResponseTypeDef

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopMonitoringScheduleRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes


# StopNotebookInstanceInputTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes


# StopOptimizationJobRequestTypeDef

### OptimizationJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipelineExecutionRequestTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipelineExecutionResponseTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopProcessingJobRequestTypeDef

### ProcessingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopTrainingJobRequestTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StopTransformJobRequestTypeDef

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes


# StoppingConditionTypeDef

### MaxRuntimeInSeconds
- **Type**: typing.Optional[int]

### MaxWaitTimeInSeconds
- **Type**: typing.Optional[int]

### MaxPendingTimeInSeconds
- **Type**: typing.Optional[int]


# StudioLifecycleConfigDetailsTypeDef

### StudioLifecycleConfigArn
- **Type**: typing.Optional[str]

### StudioLifecycleConfigName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### StudioLifecycleConfigAppType
- **Type**: typing.Optional[typing.Literal['CodeEditor', 'JupyterLab', 'JupyterServer', 'KernelGateway']]


# StudioWebPortalSettingsOutputTypeDef

### HiddenMlTools
- **Type**: typing.Optional[typing.List[typing.Literal['AutoMl', 'Comet', 'DataWrangler', 'DeepchecksLLMEvaluation', 'EmrClusters', 'Endpoints', 'Experiments', 'FeatureStore', 'Fiddler', 'HyperPodClusters', 'InferenceOptimization', 'InferenceRecommender', 'JumpStart', 'LakeraGuard', 'ModelEvaluation', 'Models', 'PerformanceEvaluation', 'Pipelines', 'Projects', 'Training']]]

### HiddenAppTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]]

### HiddenInstanceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.geospatial.interactive', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.micro', 'ml.t3.small', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'system']]]

### HiddenSageMakerImageVersionAliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HiddenSageMakerImageOutputTypeDef]]


# StudioWebPortalSettingsTypeDef

### HiddenMlTools
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AutoMl', 'Comet', 'DataWrangler', 'DeepchecksLLMEvaluation', 'EmrClusters', 'Endpoints', 'Experiments', 'FeatureStore', 'Fiddler', 'HyperPodClusters', 'InferenceOptimization', 'InferenceRecommender', 'JumpStart', 'LakeraGuard', 'ModelEvaluation', 'Models', 'PerformanceEvaluation', 'Pipelines', 'Projects', 'Training']]]

### HiddenAppTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Canvas', 'CodeEditor', 'DetailedProfiler', 'JupyterLab', 'JupyterServer', 'KernelGateway', 'RSessionGateway', 'RStudioServerPro', 'TensorBoard']]]

### HiddenInstanceTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ml.c5.12xlarge', 'ml.c5.18xlarge', 'ml.c5.24xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.large', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.geospatial.interactive', 'ml.m5.12xlarge', 'ml.m5.16xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.8xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.micro', 'ml.t3.small', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'system']]]

### HiddenSageMakerImageVersionAliases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.HiddenSageMakerImageTypeDef]]


# SubscribedWorkteamTypeDef

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### MarketplaceTitle
- **Type**: typing.Optional[str]

### SellerName
- **Type**: typing.Optional[str]

### MarketplaceDescription
- **Type**: typing.Optional[str]

### ListingId
- **Type**: typing.Optional[str]


# SuggestionQueryTypeDef

### PropertyNameQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PropertyNameQueryTypeDef]


# TabularJobConfigOutputTypeDef

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CandidateGenerationConfigOutputTypeDef]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]

### GenerateCandidateDefinitionsOnly
- **Type**: typing.Optional[bool]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### SampleWeightAttributeName
- **Type**: typing.Optional[str]


# TabularJobConfigTypeDef

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CandidateGenerationConfigTypeDef]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTO', 'ENSEMBLING', 'HYPERPARAMETER_TUNING']]

### GenerateCandidateDefinitionsOnly
- **Type**: typing.Optional[bool]

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]

### SampleWeightAttributeName
- **Type**: typing.Optional[str]


# TabularResolvedAttributesTypeDef

### ProblemType
- **Type**: typing.Optional[typing.Literal['BinaryClassification', 'MulticlassClassification', 'Regression']]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetPlatformTypeDef

### Os
- **Type**: typing.Literal['ANDROID', 'LINUX']
- **Required**: Yes

### Arch
- **Type**: typing.Literal['ARM64', 'ARM_EABI', 'ARM_EABIHF', 'X86', 'X86_64']
- **Required**: Yes

### Accelerator
- **Type**: typing.Optional[typing.Literal['INTEL_GRAPHICS', 'MALI', 'NNA', 'NVIDIA']]


# TargetTrackingScalingPolicyConfigurationTypeDef

### MetricSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetricSpecificationTypeDef]

### TargetValue
- **Type**: typing.Optional[float]


# TensorBoardAppSettingsTypeDef

### DefaultResourceSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceSpecTypeDef]


# TensorBoardOutputConfigTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### LocalPath
- **Type**: typing.Optional[str]


# TextClassificationJobConfigTypeDef

### ContentColumn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetLabelColumn
- **Type**: <class 'str'>
- **Required**: Yes

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]


# TextGenerationJobConfigOutputTypeDef

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### BaseModelName
- **Type**: typing.Optional[str]

### TextGenerationHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### ModelAccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelAccessConfigTypeDef]


# TextGenerationJobConfigTypeDef

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### BaseModelName
- **Type**: typing.Optional[str]

### TextGenerationHyperParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ModelAccessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelAccessConfigTypeDef]


# TextGenerationResolvedAttributesTypeDef

### BaseModelName
- **Type**: typing.Optional[str]


# ThroughputConfigDescriptionTypeDef

### ThroughputMode
- **Type**: typing.Literal['OnDemand', 'Provisioned']
- **Required**: Yes

### ProvisionedReadCapacityUnits
- **Type**: typing.Optional[int]

### ProvisionedWriteCapacityUnits
- **Type**: typing.Optional[int]


# ThroughputConfigTypeDef

### ThroughputMode
- **Type**: typing.Literal['OnDemand', 'Provisioned']
- **Required**: Yes

### ProvisionedReadCapacityUnits
- **Type**: typing.Optional[int]

### ProvisionedWriteCapacityUnits
- **Type**: typing.Optional[int]


# ThroughputConfigUpdateTypeDef

### ThroughputMode
- **Type**: typing.Optional[typing.Literal['OnDemand', 'Provisioned']]

### ProvisionedReadCapacityUnits
- **Type**: typing.Optional[int]

### ProvisionedWriteCapacityUnits
- **Type**: typing.Optional[int]


# TimeSeriesConfigOutputTypeDef

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemIdentifierAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupingAttributeNames
- **Type**: typing.Optional[typing.List[str]]


# TimeSeriesConfigTypeDef

### TargetAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ItemIdentifierAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupingAttributeNames
- **Type**: typing.Optional[typing.Sequence[str]]


# TimeSeriesForecastingJobConfigOutputTypeDef

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### TimeSeriesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesConfigOutputTypeDef'>
- **Required**: Yes

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### ForecastQuantiles
- **Type**: typing.Optional[typing.List[str]]

### Transformations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesTransformationsOutputTypeDef]

### HolidayConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HolidayConfigAttributesTypeDef]]

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CandidateGenerationConfigOutputTypeDef]


# TimeSeriesForecastingJobConfigTypeDef

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### TimeSeriesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesConfigTypeDef'>
- **Required**: Yes

### FeatureSpecificationS3Uri
- **Type**: typing.Optional[str]

### CompletionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AutoMLJobCompletionCriteriaTypeDef]

### ForecastQuantiles
- **Type**: typing.Optional[typing.Sequence[str]]

### Transformations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimeSeriesTransformationsTypeDef]

### HolidayConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.HolidayConfigAttributesTypeDef]]

### CandidateGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CandidateGenerationConfigTypeDef]


# TimeSeriesForecastingSettingsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### AmazonForecastRoleArn
- **Type**: typing.Optional[str]


# TimeSeriesTransformationsOutputTypeDef

### Filling
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[typing.Literal['backfill', 'backfill_value', 'frontfill', 'frontfill_value', 'futurefill', 'futurefill_value', 'middlefill', 'middlefill_value'], str]]]

### Aggregation
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['avg', 'first', 'max', 'min', 'sum']]]


# TimeSeriesTransformationsTypeDef

### Filling
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[typing.Literal['backfill', 'backfill_value', 'frontfill', 'frontfill_value', 'futurefill', 'futurefill_value', 'middlefill', 'middlefill_value'], str]]]

### Aggregation
- **Type**: typing.Optional[typing.Mapping[str, typing.Literal['avg', 'first', 'max', 'min', 'sum']]]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrackingServerSummaryTypeDef

### TrackingServerArn
- **Type**: typing.Optional[str]

### TrackingServerName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### TrackingServerStatus
- **Type**: typing.Optional[typing.Literal['CreateFailed', 'Created', 'Creating', 'DeleteFailed', 'Deleting', 'MaintenanceComplete', 'MaintenanceFailed', 'MaintenanceInProgress', 'StartFailed', 'Started', 'Starting', 'StopFailed', 'Stopped', 'Stopping', 'UpdateFailed', 'Updated', 'Updating']]

### IsActive
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### MlflowVersion
- **Type**: typing.Optional[str]


# TrafficPatternOutputTypeDef

### TrafficType
- **Type**: typing.Optional[typing.Literal['PHASES', 'STAIRS']]

### Phases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.PhaseTypeDef]]

### Stairs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.StairsTypeDef]


# TrafficPatternTypeDef

### TrafficType
- **Type**: typing.Optional[typing.Literal['PHASES', 'STAIRS']]

### Phases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.PhaseTypeDef]]

### Stairs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.StairsTypeDef]


# TrafficRoutingConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrainingImageConfigTypeDef

### TrainingRepositoryAccessMode
- **Type**: typing.Literal['Platform', 'Vpc']
- **Required**: Yes

### TrainingRepositoryAuthConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingRepositoryAuthConfigTypeDef]


# TrainingJobDefinitionOutputTypeDef

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### InputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelOutputTypeDef]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigOutputTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# TrainingJobDefinitionTypeDef

### TrainingInputMode
- **Type**: typing.Literal['FastFile', 'File', 'Pipe']
- **Required**: Yes

### InputDataConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelTypeDef]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigTypeDef'>
- **Required**: Yes

### StoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### HyperParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TrainingJobStatusCountersTypeDef

### Completed
- **Type**: typing.Optional[int]

### InProgress
- **Type**: typing.Optional[int]

### RetryableError
- **Type**: typing.Optional[int]

### NonRetryableError
- **Type**: typing.Optional[int]

### Stopped
- **Type**: typing.Optional[int]


# TrainingJobStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# TrainingJobSummaryTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SecondaryStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']]

### WarmPoolStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WarmPoolStatusTypeDef]

### TrainingPlanArn
- **Type**: typing.Optional[str]


# TrainingJobTypeDef

### TrainingJobName
- **Type**: typing.Optional[str]

### TrainingJobArn
- **Type**: typing.Optional[str]

### TuningJobArn
- **Type**: typing.Optional[str]

### LabelingJobArn
- **Type**: typing.Optional[str]

### AutoMLJobArn
- **Type**: typing.Optional[str]

### ModelArtifacts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelArtifactsTypeDef]

### TrainingJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### SecondaryStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Downloading', 'DownloadingTrainingImage', 'Failed', 'Interrupted', 'LaunchingMLInstances', 'MaxRuntimeExceeded', 'MaxWaitTimeExceeded', 'Pending', 'PreparingTrainingStack', 'Restarting', 'Starting', 'Stopped', 'Stopping', 'Training', 'Updating', 'Uploading']]

### FailureReason
- **Type**: typing.Optional[str]

### HyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### AlgorithmSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AlgorithmSpecificationOutputTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### InputDataConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelOutputTypeDef]]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OutputDataConfigTypeDef]

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigOutputTypeDef]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.VpcConfigOutputTypeDef]

### StoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.StoppingConditionTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingStartTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SecondaryStatusTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.SecondaryStatusTransitionTypeDef]]

### FinalMetricDataList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDataTypeDef]]

### EnableNetworkIsolation
- **Type**: typing.Optional[bool]

### EnableInterContainerTrafficEncryption
- **Type**: typing.Optional[bool]

### EnableManagedSpotTraining
- **Type**: typing.Optional[bool]

### CheckpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CheckpointConfigTypeDef]

### TrainingTimeInSeconds
- **Type**: typing.Optional[int]

### BillableTimeInSeconds
- **Type**: typing.Optional[int]

### DebugHookConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DebugHookConfigOutputTypeDef]

### ExperimentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef]

### DebugRuleConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DebugRuleConfigurationOutputTypeDef]]

### TensorBoardOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TensorBoardOutputConfigTypeDef]

### DebugRuleEvaluationStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.DebugRuleEvaluationStatusTypeDef]]

### ProfilerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerConfigOutputTypeDef]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RetryStrategyTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# TrainingPlanFilterTypeDef

### Name
- **Type**: typing.Literal['Status']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TrainingPlanOfferingTypeDef

### TrainingPlanOfferingId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetResources
- **Type**: typing.List[typing.Literal['hyperpod-cluster', 'training-job']]
- **Required**: Yes

### RequestedStartTimeAfter
- **Type**: typing.Optional[datetime.datetime]

### RequestedEndTimeBefore
- **Type**: typing.Optional[datetime.datetime]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### UpfrontFee
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### ReservedCapacityOfferings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ReservedCapacityOfferingTypeDef]]


# TrainingPlanSummaryTypeDef

### TrainingPlanArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrainingPlanName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Expired', 'Failed', 'Pending', 'Scheduled']
- **Required**: Yes

### StatusMessage
- **Type**: typing.Optional[str]

### DurationHours
- **Type**: typing.Optional[int]

### DurationMinutes
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### UpfrontFee
- **Type**: typing.Optional[str]

### CurrencyCode
- **Type**: typing.Optional[str]

### TotalInstanceCount
- **Type**: typing.Optional[int]

### AvailableInstanceCount
- **Type**: typing.Optional[int]

### InUseInstanceCount
- **Type**: typing.Optional[int]

### TargetResources
- **Type**: typing.Optional[typing.List[typing.Literal['hyperpod-cluster', 'training-job']]]

### ReservedCapacitySummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ReservedCapacitySummaryTypeDef]]


# TrainingRepositoryAuthConfigTypeDef

### TrainingRepositoryCredentialsProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# TrainingSpecificationOutputTypeDef

### TrainingImage
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedTrainingInstanceTypes
- **Type**: typing.List[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]
- **Required**: Yes

### TrainingChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelSpecificationOutputTypeDef]
- **Required**: Yes

### TrainingImageDigest
- **Type**: typing.Optional[str]

### SupportedHyperParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterSpecificationOutputTypeDef]]

### SupportsDistributedTraining
- **Type**: typing.Optional[bool]

### MetricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDefinitionTypeDef]]

### SupportedTuningJobObjectiveMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobObjectiveTypeDef]]

### AdditionalS3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalS3DataSourceTypeDef]


# TrainingSpecificationTypeDef

### TrainingImage
- **Type**: <class 'str'>
- **Required**: Yes

### SupportedTrainingInstanceTypes
- **Type**: typing.Sequence[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.g6e.12xlarge', 'ml.g6e.16xlarge', 'ml.g6e.24xlarge', 'ml.g6e.2xlarge', 'ml.g6e.48xlarge', 'ml.g6e.4xlarge', 'ml.g6e.8xlarge', 'ml.g6e.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.p5e.48xlarge', 'ml.p5en.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge', 'ml.trn2.48xlarge']]
- **Required**: Yes

### TrainingChannels
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ChannelSpecificationTypeDef]
- **Required**: Yes

### TrainingImageDigest
- **Type**: typing.Optional[str]

### SupportedHyperParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterSpecificationTypeDef]]

### SupportsDistributedTraining
- **Type**: typing.Optional[bool]

### MetricDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.MetricDefinitionTypeDef]]

### SupportedTuningJobObjectiveMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.HyperParameterTuningJobObjectiveTypeDef]]

### AdditionalS3DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalS3DataSourceTypeDef]


# TrainingSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransformDataSourceTypeDef

### S3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformS3DataSourceTypeDef'>
- **Required**: Yes


# TransformInputTypeDef

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformDataSourceTypeDef'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### CompressionType
- **Type**: typing.Optional[typing.Literal['Gzip', 'None']]

### SplitType
- **Type**: typing.Optional[typing.Literal['Line', 'None', 'RecordIO', 'TFRecord']]


# TransformJobDefinitionOutputTypeDef

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformInputTypeDef'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformOutputTypeDef'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformResourcesTypeDef'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]


# TransformJobDefinitionTypeDef

### TransformInput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformInputTypeDef'>
- **Required**: Yes

### TransformOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformOutputTypeDef'>
- **Required**: Yes

### TransformResources
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.TransformResourcesTypeDef'>
- **Required**: Yes

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TransformJobStepMetadataTypeDef

### Arn
- **Type**: typing.Optional[str]


# TransformJobSummaryTypeDef

### TransformJobName
- **Type**: <class 'str'>
- **Required**: Yes

### TransformJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TransformJobStatus
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']
- **Required**: Yes

### TransformEndTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]


# TransformJobTypeDef

### TransformJobName
- **Type**: typing.Optional[str]

### TransformJobArn
- **Type**: typing.Optional[str]

### TransformJobStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### FailureReason
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### MaxConcurrentTransforms
- **Type**: typing.Optional[int]

### ModelClientConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelClientConfigTypeDef]

### MaxPayloadInMB
- **Type**: typing.Optional[int]

### BatchStrategy
- **Type**: typing.Optional[typing.Literal['MultiRecord', 'SingleRecord']]

### Environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### TransformInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformInputTypeDef]

### TransformOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformOutputTypeDef]

### DataCaptureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BatchDataCaptureConfigTypeDef]

### TransformResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformResourcesTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TransformStartTime
- **Type**: typing.Optional[datetime.datetime]

### TransformEndTime
- **Type**: typing.Optional[datetime.datetime]

### LabelingJobArn
- **Type**: typing.Optional[str]

### AutoMLJobArn
- **Type**: typing.Optional[str]

### DataProcessing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DataProcessingTypeDef]

### ExperimentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ExperimentConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# TransformOutputTypeDef

### S3OutputPath
- **Type**: <class 'str'>
- **Required**: Yes

### Accept
- **Type**: typing.Optional[str]

### AssembleWith
- **Type**: typing.Optional[typing.Literal['Line', 'None']]

### KmsKeyId
- **Type**: typing.Optional[str]


# TransformResourcesTypeDef

### InstanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge']
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### VolumeKmsKeyId
- **Type**: typing.Optional[str]


# TransformS3DataSourceTypeDef

### S3DataType
- **Type**: typing.Literal['AugmentedManifestFile', 'ManifestFile', 'S3Prefix']
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# TrialComponentArtifactTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### MediaType
- **Type**: typing.Optional[str]


# TrialComponentMetricSummaryTypeDef

### MetricName
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]

### Max
- **Type**: typing.Optional[float]

### Min
- **Type**: typing.Optional[float]

### Last
- **Type**: typing.Optional[float]

### Count
- **Type**: typing.Optional[int]

### Avg
- **Type**: typing.Optional[float]

### StdDev
- **Type**: typing.Optional[float]


# TrialComponentParameterValueTypeDef

### StringValue
- **Type**: typing.Optional[str]

### NumberValue
- **Type**: typing.Optional[float]


# TrialComponentSimpleSummaryTypeDef

### TrialComponentName
- **Type**: typing.Optional[str]

### TrialComponentArn
- **Type**: typing.Optional[str]

### TrialComponentSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSourceTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]


# TrialComponentSourceDetailTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### TrainingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrainingJobTypeDef]

### ProcessingJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProcessingJobTypeDef]

### TransformJob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TransformJobTypeDef]


# TrialComponentSourceTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]


# TrialComponentStatusTypeDef

### PrimaryStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping']]

### Message
- **Type**: typing.Optional[str]


# TrialComponentSummaryTypeDef

### TrialComponentName
- **Type**: typing.Optional[str]

### TrialComponentArn
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### TrialComponentSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSourceTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentStatusTypeDef]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]


# TrialComponentTypeDef

### TrialComponentName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### TrialComponentArn
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSourceTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentStatusTypeDef]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentParameterValueTypeDef]]

### InputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]]

### OutputArtifacts
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]]

### Metrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentMetricSummaryTypeDef]]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### SourceDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSourceDetailTypeDef]

### LineageGroupArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### Parents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.ParentTypeDef]]

### RunName
- **Type**: typing.Optional[str]


# TrialSourceTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceType
- **Type**: typing.Optional[str]


# TrialSummaryTypeDef

### TrialArn
- **Type**: typing.Optional[str]

### TrialName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### TrialSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialSourceTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# TrialTypeDef

### TrialName
- **Type**: typing.Optional[str]

### TrialArn
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### ExperimentName
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialSourceTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserContextTypeDef]

### MetadataProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.MetadataPropertiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]

### TrialComponentSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentSimpleSummaryTypeDef]]


# TtlDurationTypeDef

### Unit
- **Type**: typing.Optional[typing.Literal['Days', 'Hours', 'Minutes', 'Seconds', 'Weeks']]

### Value
- **Type**: typing.Optional[int]


# TuningJobCompletionCriteriaTypeDef

### TargetObjectiveMetricValue
- **Type**: typing.Optional[float]

### BestObjectiveNotImproving
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.BestObjectiveNotImprovingTypeDef]

### ConvergenceDetected
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ConvergenceDetectedTypeDef]


# TuningJobStepMetaDataTypeDef

### Arn
- **Type**: typing.Optional[str]


# USDTypeDef

### Dollars
- **Type**: typing.Optional[int]

### Cents
- **Type**: typing.Optional[int]

### TenthFractionsOfACent
- **Type**: typing.Optional[int]


# UiConfigTypeDef

### UiTemplateS3Uri
- **Type**: typing.Optional[str]

### HumanTaskUiArn
- **Type**: typing.Optional[str]


# UiTemplateInfoTypeDef

### Url
- **Type**: typing.Optional[str]

### ContentSha256
- **Type**: typing.Optional[str]


# UiTemplateTypeDef

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateActionRequestTypeDef

### ActionName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Unknown']]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PropertiesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateActionResponseTypeDef

### ActionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppImageConfigRequestTypeDef

### AppImageConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### KernelGatewayImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayImageConfigUnionTypeDef]

### JupyterLabAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppImageConfigUnionTypeDef]

### CodeEditorAppImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CodeEditorAppImageConfigUnionTypeDef]


# UpdateAppImageConfigResponseTypeDef

### AppImageConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateArtifactRequestTypeDef

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactName
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PropertiesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateArtifactResponseTypeDef

### ArtifactArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ClusterInstanceGroupSpecificationTypeDef]
- **Required**: Yes

### NodeRecovery
- **Type**: typing.Optional[typing.Literal['Automatic', 'None']]

### InstanceGroupsToDelete
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateClusterResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterSchedulerConfigRequestTypeDef

### ClusterSchedulerConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'int'>
- **Required**: Yes

### SchedulerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SchedulerConfigUnionTypeDef]

### Description
- **Type**: typing.Optional[str]


# UpdateClusterSchedulerConfigResponseTypeDef

### ClusterSchedulerConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterSchedulerConfigVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterSoftwareRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateClusterSoftwareResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCodeRepositoryInputTypeDef

### CodeRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### GitConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.GitConfigForUpdateTypeDef]


# UpdateCodeRepositoryOutputTypeDef

### CodeRepositoryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateComputeQuotaRequestTypeDef

### ComputeQuotaId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ComputeQuotaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaConfigUnionTypeDef]

### ComputeQuotaTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ComputeQuotaTargetTypeDef]

### ActivationState
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Description
- **Type**: typing.Optional[str]


# UpdateComputeQuotaResponseTypeDef

### ComputeQuotaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeQuotaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateContextRequestTypeDef

### ContextName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PropertiesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateContextResponseTypeDef

### ContextArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDeviceFleetRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.EdgeOutputConfigTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EnableIotRoleAlias
- **Type**: typing.Optional[bool]


# UpdateDevicesRequestTypeDef

### DeviceFleetName
- **Type**: <class 'str'>
- **Required**: Yes

### Devices
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.DeviceTypeDef]
- **Required**: Yes


# UpdateDomainRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultUserSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserSettingsUnionTypeDef]

### DomainSettingsForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DomainSettingsForUpdateTypeDef]

### AppSecurityGroupManagement
- **Type**: typing.Optional[typing.Literal['Customer', 'Service']]

### DefaultSpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DefaultSpaceSettingsUnionTypeDef]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### AppNetworkAccessType
- **Type**: typing.Optional[typing.Literal['PublicInternetOnly', 'VpcOnly']]

### TagPropagation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateDomainResponseTypeDef

### DomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEndpointInputTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### RetainAllVariantProperties
- **Type**: typing.Optional[bool]

### ExcludeRetainedVariantProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.VariantPropertyTypeDef]]

### DeploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DeploymentConfigUnionTypeDef]

### RetainDeploymentConfig
- **Type**: typing.Optional[bool]


# UpdateEndpointOutputTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEndpointWeightsAndCapacitiesInputTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredWeightsAndCapacities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.DesiredWeightAndCapacityTypeDef]
- **Required**: Yes


# UpdateEndpointWeightsAndCapacitiesOutputTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateExperimentRequestTypeDef

### ExperimentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateExperimentResponseTypeDef

### ExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFeatureGroupRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureAdditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureDefinitionTypeDef]]

### OnlineStoreConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OnlineStoreConfigUpdateTypeDef]

### ThroughputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ThroughputConfigUpdateTypeDef]


# UpdateFeatureGroupResponseTypeDef

### FeatureGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFeatureMetadataRequestTypeDef

### FeatureGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ParameterAdditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.FeatureParameterTypeDef]]

### ParameterRemovals
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateHubContentReferenceRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### MinVersion
- **Type**: typing.Optional[str]


# UpdateHubContentReferenceResponseTypeDef

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateHubContentRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentName
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentType
- **Type**: typing.Literal['Model', 'ModelReference', 'Notebook']
- **Required**: Yes

### HubContentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentDisplayName
- **Type**: typing.Optional[str]

### HubContentDescription
- **Type**: typing.Optional[str]

### HubContentMarkdown
- **Type**: typing.Optional[str]

### HubContentSearchKeywords
- **Type**: typing.Optional[typing.Sequence[str]]

### SupportStatus
- **Type**: typing.Optional[typing.Literal['Deprecated', 'Restricted', 'Supported']]


# UpdateHubContentResponseTypeDef

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### HubContentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateHubRequestTypeDef

### HubName
- **Type**: <class 'str'>
- **Required**: Yes

### HubDescription
- **Type**: typing.Optional[str]

### HubDisplayName
- **Type**: typing.Optional[str]

### HubSearchKeywords
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateHubResponseTypeDef

### HubArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateImageRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteProperties
- **Type**: typing.Optional[typing.Sequence[str]]

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateImageResponseTypeDef

### ImageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateImageVersionRequestTypeDef

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### AliasesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### AliasesToDelete
- **Type**: typing.Optional[typing.Sequence[str]]

### VendorGuidance
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'NOT_PROVIDED', 'STABLE', 'TO_BE_ARCHIVED']]

### JobType
- **Type**: typing.Optional[typing.Literal['INFERENCE', 'NOTEBOOK_KERNEL', 'TRAINING']]

### MLFramework
- **Type**: typing.Optional[str]

### ProgrammingLang
- **Type**: typing.Optional[str]

### Processor
- **Type**: typing.Optional[typing.Literal['CPU', 'GPU']]

### Horovod
- **Type**: typing.Optional[bool]

### ReleaseNotes
- **Type**: typing.Optional[str]


# UpdateImageVersionResponseTypeDef

### ImageVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInferenceComponentInputTypeDef

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### Specification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentSpecificationTypeDef]

### RuntimeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentRuntimeConfigTypeDef]

### DeploymentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentDeploymentConfigUnionTypeDef]


# UpdateInferenceComponentOutputTypeDef

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInferenceComponentRuntimeConfigInputTypeDef

### InferenceComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredRuntimeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.InferenceComponentRuntimeConfigTypeDef'>
- **Required**: Yes


# UpdateInferenceComponentRuntimeConfigOutputTypeDef

### InferenceComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInferenceExperimentRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceExperimentScheduleUnionTypeDef]

### Description
- **Type**: typing.Optional[str]

### ModelVariants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ModelVariantConfigTypeDef]]

### DataStorageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceExperimentDataStorageConfigUnionTypeDef]

### ShadowModeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ShadowModeConfigUnionTypeDef]


# UpdateInferenceExperimentResponseTypeDef

### InferenceExperimentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMlflowTrackingServerRequestTypeDef

### TrackingServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ArtifactStoreUri
- **Type**: typing.Optional[str]

### TrackingServerSize
- **Type**: typing.Optional[typing.Literal['Large', 'Medium', 'Small']]

### AutomaticModelRegistration
- **Type**: typing.Optional[bool]

### WeeklyMaintenanceWindowStart
- **Type**: typing.Optional[str]


# UpdateMlflowTrackingServerResponseTypeDef

### TrackingServerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateModelCardRequestTypeDef

### ModelCardName
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### ModelCardStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'Archived', 'Draft', 'PendingReview']]


# UpdateModelCardResponseTypeDef

### ModelCardArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateModelPackageInputTypeDef

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelApprovalStatus
- **Type**: typing.Optional[typing.Literal['Approved', 'PendingManualApproval', 'Rejected']]

### ApprovalDescription
- **Type**: typing.Optional[str]

### CustomerMetadataProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### CustomerMetadataPropertiesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### AdditionalInferenceSpecificationsToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.AdditionalInferenceSpecificationDefinitionUnionTypeDef]]

### InferenceSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InferenceSpecificationUnionTypeDef]

### SourceUri
- **Type**: typing.Optional[str]

### ModelCard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelPackageModelCardTypeDef]

### ModelLifeCycle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ModelLifeCycleTypeDef]

### ClientToken
- **Type**: typing.Optional[str]


# UpdateModelPackageOutputTypeDef

### ModelPackageArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMonitoringAlertRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### DatapointsToAlert
- **Type**: <class 'int'>
- **Required**: Yes

### EvaluationPeriod
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateMonitoringAlertResponseTypeDef

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringAlertName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMonitoringScheduleRequestTypeDef

### MonitoringScheduleName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringScheduleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.MonitoringScheduleConfigUnionTypeDef'>
- **Required**: Yes


# UpdateMonitoringScheduleResponseTypeDef

### MonitoringScheduleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNotebookInstanceInputTypeDef

### NotebookInstanceName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceType
- **Type**: typing.Optional[typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5d.18xlarge', 'ml.c5d.2xlarge', 'ml.c5d.4xlarge', 'ml.c5d.9xlarge', 'ml.c5d.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c6id.12xlarge', 'ml.c6id.16xlarge', 'ml.c6id.24xlarge', 'ml.c6id.2xlarge', 'ml.c6id.32xlarge', 'ml.c6id.4xlarge', 'ml.c6id.8xlarge', 'ml.c6id.large', 'ml.c6id.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.g6.12xlarge', 'ml.g6.16xlarge', 'ml.g6.24xlarge', 'ml.g6.2xlarge', 'ml.g6.48xlarge', 'ml.g6.4xlarge', 'ml.g6.8xlarge', 'ml.g6.xlarge', 'ml.inf1.24xlarge', 'ml.inf1.2xlarge', 'ml.inf1.6xlarge', 'ml.inf1.xlarge', 'ml.inf2.24xlarge', 'ml.inf2.48xlarge', 'ml.inf2.8xlarge', 'ml.inf2.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.xlarge', 'ml.m5d.12xlarge', 'ml.m5d.16xlarge', 'ml.m5d.24xlarge', 'ml.m5d.2xlarge', 'ml.m5d.4xlarge', 'ml.m5d.8xlarge', 'ml.m5d.large', 'ml.m5d.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m6id.12xlarge', 'ml.m6id.16xlarge', 'ml.m6id.24xlarge', 'ml.m6id.2xlarge', 'ml.m6id.32xlarge', 'ml.m6id.4xlarge', 'ml.m6id.8xlarge', 'ml.m6id.large', 'ml.m6id.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r6id.12xlarge', 'ml.r6id.16xlarge', 'ml.r6id.24xlarge', 'ml.r6id.2xlarge', 'ml.r6id.32xlarge', 'ml.r6id.4xlarge', 'ml.r6id.8xlarge', 'ml.r6id.large', 'ml.r6id.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge', 'ml.t2.2xlarge', 'ml.t2.large', 'ml.t2.medium', 'ml.t2.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']]

### RoleArn
- **Type**: typing.Optional[str]

### LifecycleConfigName
- **Type**: typing.Optional[str]

### DisassociateLifecycleConfig
- **Type**: typing.Optional[bool]

### VolumeSizeInGB
- **Type**: typing.Optional[int]

### DefaultCodeRepository
- **Type**: typing.Optional[str]

### AdditionalCodeRepositories
- **Type**: typing.Optional[typing.Sequence[str]]

### AcceleratorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ml.eia1.large', 'ml.eia1.medium', 'ml.eia1.xlarge', 'ml.eia2.large', 'ml.eia2.medium', 'ml.eia2.xlarge']]]

### DisassociateAcceleratorTypes
- **Type**: typing.Optional[bool]

### DisassociateDefaultCodeRepository
- **Type**: typing.Optional[bool]

### DisassociateAdditionalCodeRepositories
- **Type**: typing.Optional[bool]

### RootAccess
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### InstanceMetadataServiceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.InstanceMetadataServiceConfigurationTypeDef]


# UpdateNotebookInstanceLifecycleConfigInputTypeDef

### NotebookInstanceLifecycleConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### OnCreate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceLifecycleHookTypeDef]]

### OnStart
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.NotebookInstanceLifecycleHookTypeDef]]


# UpdatePartnerAppRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaintenanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PartnerAppMaintenanceConfigTypeDef]

### Tier
- **Type**: typing.Optional[str]

### ApplicationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PartnerAppConfigUnionTypeDef]

### EnableIamSessionBasedIdentity
- **Type**: typing.Optional[bool]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# UpdatePartnerAppResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePipelineExecutionRequestTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineExecutionDescription
- **Type**: typing.Optional[str]

### PipelineExecutionDisplayName
- **Type**: typing.Optional[str]

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef]


# UpdatePipelineExecutionResponseTypeDef

### PipelineExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePipelineRequestTypeDef

### PipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### PipelineDisplayName
- **Type**: typing.Optional[str]

### PipelineDefinition
- **Type**: typing.Optional[str]

### PipelineDefinitionS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.PipelineDefinitionS3LocationTypeDef]

### PipelineDescription
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ParallelismConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ParallelismConfigurationTypeDef]


# UpdatePipelineResponseTypeDef

### PipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectInputTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### ProjectDescription
- **Type**: typing.Optional[str]

### ServiceCatalogProvisioningUpdateDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ServiceCatalogProvisioningUpdateDetailsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.TagTypeDef]]


# UpdateProjectOutputTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSpaceRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceName
- **Type**: <class 'str'>
- **Required**: Yes

### SpaceSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SpaceSettingsUnionTypeDef]

### SpaceDisplayName
- **Type**: typing.Optional[str]


# UpdateSpaceResponseTypeDef

### SpaceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrainingJobRequestTypeDef

### TrainingJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfilerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerConfigForUpdateTypeDef]

### ProfilerRuleConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.ProfilerRuleConfigurationUnionTypeDef]]

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.ResourceConfigForUpdateTypeDef]

### RemoteDebugConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RemoteDebugConfigForUpdateTypeDef]


# UpdateTrainingJobResponseTypeDef

### TrainingJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrialComponentRequestTypeDef

### TrialComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentStatusTypeDef]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TimestampTypeDef]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentParameterValueTypeDef]]

### ParametersToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### InputArtifacts
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]]

### InputArtifactsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### OutputArtifacts
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.sagemaker_classes.TrialComponentArtifactTypeDef]]

### OutputArtifactsToRemove
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateTrialComponentResponseTypeDef

### TrialComponentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrialRequestTypeDef

### TrialName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]


# UpdateTrialResponseTypeDef

### TrialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserProfileRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### UserProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### UserSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.UserSettingsUnionTypeDef]


# UpdateUserProfileResponseTypeDef

### UserProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkforceRequestTypeDef

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SourceIpConfigUnionTypeDef]

### OidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OidcConfigTypeDef]

### WorkforceVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkforceVpcConfigRequestTypeDef]


# UpdateWorkforceResponseTypeDef

### Workforce
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.WorkforceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkteamRequestTypeDef

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.MemberDefinitionUnionTypeDef]]

### Description
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NotificationConfigurationTypeDef]

### WorkerAccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkerAccessConfigurationTypeDef]


# UpdateWorkteamResponseTypeDef

### Workteam
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.WorkteamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserContextTypeDef

### UserProfileArn
- **Type**: typing.Optional[str]

### UserProfileName
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### IamIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.IamIdentityTypeDef]


# UserProfileDetailsTypeDef

### DomainId
- **Type**: typing.Optional[str]

### UserProfileName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Delete_Failed', 'Deleting', 'Failed', 'InService', 'Pending', 'Update_Failed', 'Updating']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# UserSettingsOutputTypeDef

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### SharingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SharingSettingsTypeDef]

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterServerAppSettingsOutputTypeDef]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayAppSettingsOutputTypeDef]

### TensorBoardAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TensorBoardAppSettingsTypeDef]

### RStudioServerProAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RStudioServerProAppSettingsTypeDef]

### RSessionAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RSessionAppSettingsOutputTypeDef]

### CanvasAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CanvasAppSettingsOutputTypeDef]

### CodeEditorAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CodeEditorAppSettingsOutputTypeDef]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppSettingsOutputTypeDef]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DefaultSpaceStorageSettingsTypeDef]

### DefaultLandingUri
- **Type**: typing.Optional[str]

### StudioWebPortal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CustomPosixUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CustomPosixUserConfigTypeDef]

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.CustomFileSystemConfigTypeDef]]

### StudioWebPortalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.StudioWebPortalSettingsOutputTypeDef]

### AutoMountHomeEFS
- **Type**: typing.Optional[typing.Literal['DefaultAsDomain', 'Disabled', 'Enabled']]


# UserSettingsTypeDef

### ExecutionRole
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### SharingSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SharingSettingsTypeDef]

### JupyterServerAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterServerAppSettingsTypeDef]

### KernelGatewayAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.KernelGatewayAppSettingsTypeDef]

### TensorBoardAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.TensorBoardAppSettingsTypeDef]

### RStudioServerProAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RStudioServerProAppSettingsTypeDef]

### RSessionAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.RSessionAppSettingsTypeDef]

### CanvasAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CanvasAppSettingsTypeDef]

### CodeEditorAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CodeEditorAppSettingsTypeDef]

### JupyterLabAppSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.JupyterLabAppSettingsTypeDef]

### SpaceStorageSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.DefaultSpaceStorageSettingsTypeDef]

### DefaultLandingUri
- **Type**: typing.Optional[str]

### StudioWebPortal
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CustomPosixUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CustomPosixUserConfigTypeDef]

### CustomFileSystemConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_classes.CustomFileSystemConfigTypeDef]]

### StudioWebPortalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.StudioWebPortalSettingsTypeDef]

### AutoMountHomeEFS
- **Type**: typing.Optional[typing.Literal['DefaultAsDomain', 'Disabled', 'Enabled']]


# UserSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VariantPropertyTypeDef

### VariantPropertyType
- **Type**: typing.Literal['DataCaptureConfig', 'DesiredInstanceCount', 'DesiredWeight']
- **Required**: Yes


# VectorConfigTypeDef

### Dimension
- **Type**: <class 'int'>
- **Required**: Yes


# VertexTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VisibilityConditionsTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# VpcConfigOutputTypeDef

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigTypeDef

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WarmPoolStatusTypeDef

### Status
- **Type**: typing.Literal['Available', 'InUse', 'Reused', 'Terminated']
- **Required**: Yes

### ResourceRetainedBillableTimeInSeconds
- **Type**: typing.Optional[int]

### ReusedByJob
- **Type**: typing.Optional[str]


# WorkerAccessConfigurationTypeDef

### S3Presign
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.S3PresignTypeDef]


# WorkforceTypeDef

### WorkforceName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkforceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.SourceIpConfigOutputTypeDef]

### SubDomain
- **Type**: typing.Optional[str]

### CognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.CognitoConfigTypeDef]

### OidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.OidcConfigForResponseTypeDef]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### WorkforceVpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkforceVpcConfigResponseTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Deleting', 'Failed', 'Initializing', 'Updating']]

### FailureReason
- **Type**: typing.Optional[str]


# WorkforceVpcConfigRequestTypeDef

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]


# WorkforceVpcConfigResponseTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### VpcEndpointId
- **Type**: typing.Optional[str]


# WorkspaceSettingsTypeDef

### S3ArtifactPath
- **Type**: typing.Optional[str]

### S3KmsKeyId
- **Type**: typing.Optional[str]


# WorkteamTypeDef

### WorkteamName
- **Type**: <class 'str'>
- **Required**: Yes

### MemberDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_classes.MemberDefinitionOutputTypeDef]
- **Required**: Yes

### WorkteamArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### WorkforceArn
- **Type**: typing.Optional[str]

### ProductListingIds
- **Type**: typing.Optional[typing.List[str]]

### SubDomain
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.NotificationConfigurationTypeDef]

### WorkerAccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_classes.WorkerAccessConfigurationTypeDef]


