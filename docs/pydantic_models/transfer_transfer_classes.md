# Transfer Transfer Classes

# As2ConnectorConfig

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]

### MessageSubject
- **Type**: typing.Optional[str]

### Compression
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ZLIB']]

### EncryptionAlgorithm
- **Type**: typing.Optional[typing.Literal['AES128_CBC', 'AES192_CBC', 'AES256_CBC', 'DES_EDE3_CBC', 'NONE']]

### SigningAlgorithm
- **Type**: typing.Optional[typing.Literal['NONE', 'SHA1', 'SHA256', 'SHA384', 'SHA512']]

### MdnSigningAlgorithm
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NONE', 'SHA1', 'SHA256', 'SHA384', 'SHA512']]

### MdnResponse
- **Type**: typing.Optional[typing.Literal['NONE', 'SYNC']]

### BasicAuthSecretId
- **Type**: typing.Optional[str]

### PreserveContentType
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectorFileTransferResult

### FilePath
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### FailureCode
- **Type**: typing.Optional[str]

### FailureMessage
- **Type**: typing.Optional[str]


# CopyStepDetails

### Name
- **Type**: typing.Optional[str]

### DestinationFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.InputFileLocation]

### OverwriteExisting
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]

### SourceFileLocation
- **Type**: typing.Optional[str]


# CreateAccessRequest

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.HomeDirectoryMapEntry]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfile, aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfileOutput, NoneType]


# CreateAccessResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAgreementRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### LocalProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### PartnerProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### BaseDirectory
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]

### PreserveFilename
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### EnforceMessageSigning
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CustomDirectories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.CustomDirectoriesType]


# CreateAgreementResponse

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectorRequest

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### AccessRole
- **Type**: <class 'str'>
- **Required**: Yes

### As2Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.As2ConnectorConfig]

### LoggingRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]

### SftpConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.SftpConnectorConfig, aws_resource_validator.pydantic_models.transfer.transfer_classes.SftpConnectorConfigOutput, NoneType]

### SecurityPolicyName
- **Type**: typing.Optional[str]


# CreateConnectorResponse

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfileRequest

### As2Id
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileType
- **Type**: typing.Literal['LOCAL', 'PARTNER']
- **Required**: Yes

### CertificateIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# CreateProfileResponse

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServerRequest

### Certificate
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[typing.Literal['EFS', 'S3']]

### EndpointDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.EndpointDetails, aws_resource_validator.pydantic_models.transfer.transfer_classes.EndpointDetailsOutput, NoneType]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### HostKey
- **Type**: typing.Optional[str]

### IdentityProviderDetails
- **Type**: <class 'NoneType'>

### IdentityProviderType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'AWS_DIRECTORY_SERVICE', 'AWS_LAMBDA', 'SERVICE_MANAGED']]

### LoggingRole
- **Type**: typing.Optional[str]

### PostAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### PreAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]]

### ProtocolDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.ProtocolDetails, aws_resource_validator.pydantic_models.transfer.transfer_classes.ProtocolDetailsOutput, NoneType]

### SecurityPolicyName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]

### WorkflowDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetails, aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetailsOutput, NoneType]

### StructuredLogDestinations
- **Type**: typing.Optional[typing.List[str]]

### S3StorageOptions
- **Type**: <class 'NoneType'>


# CreateServerResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.HomeDirectoryMapEntry]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfile, aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfileOutput, NoneType]

### SshPublicKeyBody
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# CreateUserResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebAppRequest

### IdentityProviderDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.WebAppIdentityProviderDetails'>
- **Required**: Yes

### AccessEndpoint
- **Type**: typing.Optional[str]

### WebAppUnits
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# CreateWebAppResponse

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkflowRequest

### Steps
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowStep, aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowStepOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### OnExceptionSteps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowStep, aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowStepOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# CreateWorkflowResponse

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDirectoriesType

### FailedFilesDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### MdnFilesDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### PayloadFilesDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### StatusFilesDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### TemporaryFilesDirectory
- **Type**: <class 'str'>
- **Required**: Yes


# CustomStepDetails

### Name
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### TimeoutSeconds
- **Type**: typing.Optional[int]

### SourceFileLocation
- **Type**: typing.Optional[str]


# DecryptStepDetails

### Type
- **Type**: typing.Literal['PGP']
- **Required**: Yes

### DestinationFileLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.InputFileLocation'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### SourceFileLocation
- **Type**: typing.Optional[str]

### OverwriteExisting
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE']]


# DeleteAccessRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAgreementRequest

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCertificateRequest

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectorRequest

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostKeyRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSshPublicKeyRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStepDetails

### Name
- **Type**: typing.Optional[str]

### SourceFileLocation
- **Type**: typing.Optional[str]


# DeleteUserRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebAppCustomizationRequest

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebAppRequest

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowRequest

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Access
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedAccess'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAgreementRequest

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgreementResponse

### Agreement
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedAgreement'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCertificateRequest

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateResponse

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedCertificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectorRequest

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectorResponse

### Connector
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedConnector'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExecutionRequest

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExecutionResponse

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### Execution
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedExecution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHostKeyRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHostKeyResponse

### HostKey
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedHostKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProfileResponse

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSecurityPolicyRequest

### SecurityPolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityPolicyResponse

### SecurityPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedSecurityPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServerRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeServerRequestWait

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeServerRequestWaitExtra

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeServerResponse

### Server
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedServer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedUser'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWebAppCustomizationRequest

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWebAppCustomizationResponse

### WebAppCustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedWebAppCustomization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWebAppRequest

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWebAppResponse

### WebApp
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedWebApp'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkflowRequest

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkflowResponse

### Workflow
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedWorkflow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# DescribedAccess

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.HomeDirectoryMapEntry]]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfileOutput]

### Role
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]


# DescribedAgreement

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AgreementId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### ServerId
- **Type**: typing.Optional[str]

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]

### BaseDirectory
- **Type**: typing.Optional[str]

### AccessRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]

### PreserveFilename
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### EnforceMessageSigning
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CustomDirectories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.CustomDirectoriesType]


# DescribedCertificate

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: typing.Optional[str]

### Usage
- **Type**: typing.Optional[typing.Literal['ENCRYPTION', 'SIGNING', 'TLS']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ROTATION']]

### Certificate
- **Type**: typing.Optional[str]

### CertificateChain
- **Type**: typing.Optional[str]

### ActiveDate
- **Type**: typing.Optional[datetime.datetime]

### InactiveDate
- **Type**: typing.Optional[datetime.datetime]

### Serial
- **Type**: typing.Optional[str]

### NotBeforeDate
- **Type**: typing.Optional[datetime.datetime]

### NotAfterDate
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['CERTIFICATE', 'CERTIFICATE_WITH_PRIVATE_KEY']]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# DescribedConnector

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectorId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### As2Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.As2ConnectorConfig]

### AccessRole
- **Type**: typing.Optional[str]

### LoggingRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]

### SftpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.SftpConnectorConfigOutput]

### ServiceManagedEgressIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### SecurityPolicyName
- **Type**: typing.Optional[str]


# DescribedExecution

### ExecutionId
- **Type**: typing.Optional[str]

### InitialFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.FileLocation]

### ServiceMetadata
- **Type**: <class 'NoneType'>

### ExecutionRole
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: <class 'NoneType'>

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfileOutput]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'EXCEPTION', 'HANDLING_EXCEPTION', 'IN_PROGRESS']]

### Results
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.ExecutionResults]


# DescribedHostKey

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: typing.Optional[str]

### HostKeyFingerprint
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### DateImported
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# DescribedIdentityCenterConfig

### ApplicationArn
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]


# DescribedProfile

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: typing.Optional[str]

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]

### As2Id
- **Type**: typing.Optional[str]

### CertificateIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# DescribedSecurityPolicy

### SecurityPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### Fips
- **Type**: typing.Optional[bool]

### SshCiphers
- **Type**: typing.Optional[typing.List[str]]

### SshKexs
- **Type**: typing.Optional[typing.List[str]]

### SshMacs
- **Type**: typing.Optional[typing.List[str]]

### TlsCiphers
- **Type**: typing.Optional[typing.List[str]]

### SshHostKeyAlgorithms
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['CONNECTOR', 'SERVER']]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['FTPS', 'SFTP']]]


# DescribedServer

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: typing.Optional[str]

### ProtocolDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.ProtocolDetailsOutput]

### Domain
- **Type**: typing.Optional[typing.Literal['EFS', 'S3']]

### EndpointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.EndpointDetailsOutput]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### HostKeyFingerprint
- **Type**: typing.Optional[str]

### IdentityProviderDetails
- **Type**: <class 'NoneType'>

### IdentityProviderType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'AWS_DIRECTORY_SERVICE', 'AWS_LAMBDA', 'SERVICE_MANAGED']]

### LoggingRole
- **Type**: typing.Optional[str]

### PostAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### PreAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]]

### SecurityPolicyName
- **Type**: typing.Optional[str]

### ServerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['OFFLINE', 'ONLINE', 'STARTING', 'START_FAILED', 'STOPPING', 'STOP_FAILED']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]

### UserCount
- **Type**: typing.Optional[int]

### WorkflowDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetailsOutput]

### StructuredLogDestinations
- **Type**: typing.Optional[typing.List[str]]

### S3StorageOptions
- **Type**: <class 'NoneType'>

### As2ServiceManagedEgressIpAddresses
- **Type**: typing.Optional[typing.List[str]]


# DescribedUser

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.HomeDirectoryMapEntry]]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfileOutput]

### Role
- **Type**: typing.Optional[str]

### SshPublicKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.SshPublicKey]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]

### UserName
- **Type**: typing.Optional[str]


# DescribedWebApp

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### DescribedIdentityProviderDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedWebAppIdentityProviderDetails]

### AccessEndpoint
- **Type**: typing.Optional[str]

### WebAppEndpoint
- **Type**: typing.Optional[str]

### WebAppUnits
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# DescribedWebAppCustomization

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### LogoFile
- **Type**: typing.Optional[bytes]

### FaviconFile
- **Type**: typing.Optional[bytes]


# DescribedWebAppIdentityProviderDetails

### IdentityCenterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.DescribedIdentityCenterConfig]


# DescribedWorkflow

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowStepOutput]]

### OnExceptionSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowStepOutput]]

### WorkflowId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# EfsFileLocation

### FileSystemId
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointDetails

### AddressAllocationIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# EndpointDetailsOutput

### AddressAllocationIds
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### VpcEndpointId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# ExecutionError

### Type
- **Type**: typing.Literal['ALREADY_EXISTS', 'BAD_REQUEST', 'CUSTOM_STEP_FAILED', 'INTERNAL_SERVER_ERROR', 'NOT_FOUND', 'PERMISSION_DENIED', 'THROTTLED', 'TIMEOUT']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes


# ExecutionResults

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ExecutionStepResult]]

### OnExceptionSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ExecutionStepResult]]


# ExecutionStepResult

### StepType
- **Type**: typing.Optional[typing.Literal['COPY', 'CUSTOM', 'DECRYPT', 'DELETE', 'TAG']]

### Outputs
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.ExecutionError]


# FileLocation

### S3FileLocation
- **Type**: <class 'NoneType'>

### EfsFileLocation
- **Type**: <class 'NoneType'>


# HomeDirectoryMapEntry

### Entry
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['DIRECTORY', 'FILE']]


# IdentityCenterConfig

### InstanceArn
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]


# IdentityProviderDetails

### Url
- **Type**: typing.Optional[str]

### InvocationRole
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### Function
- **Type**: typing.Optional[str]

### SftpAuthenticationMethods
- **Type**: typing.Optional[typing.Literal['PASSWORD', 'PUBLIC_KEY', 'PUBLIC_KEY_AND_PASSWORD', 'PUBLIC_KEY_OR_PASSWORD']]


# ImportCertificateRequest

### Usage
- **Type**: typing.Literal['ENCRYPTION', 'SIGNING', 'TLS']
- **Required**: Yes

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: typing.Optional[str]

### PrivateKey
- **Type**: typing.Optional[str]

### ActiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InactiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# ImportCertificateResponse

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# ImportHostKeyRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyBody
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]]


# ImportHostKeyResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# ImportSshPublicKeyRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyBody
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# ImportSshPublicKeyResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# InputFileLocation

### S3FileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.S3InputFileLocation]

### EfsFileLocation
- **Type**: <class 'NoneType'>


# ListAccessesRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccessesRequestPaginate

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListAccessesResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Accesses
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedAccess]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAgreementsRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAgreementsRequestPaginate

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListAgreementsResponse

### Agreements
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedAgreement]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCertificatesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCertificatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListCertificatesResponse

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedCertificate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListConnectorsResponse

### Connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedConnector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExecutionsRequest

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExecutionsRequestPaginate

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListExecutionsResponse

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### Executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedExecution]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFileTransferResultsRequest

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### TransferId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFileTransferResultsRequestPaginate

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### TransferId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListFileTransferResultsResponse

### FileTransferResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ConnectorFileTransferResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHostKeysRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHostKeysResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedHostKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfilesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]


# ListProfilesRequestPaginate

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListProfilesResponse

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityPoliciesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityPoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListSecurityPoliciesResponse

### SecurityPolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListServersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListServersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListServersResponse

### Servers
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedServer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginate

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListUsersResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedUser]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWebAppsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWebAppsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListWebAppsResponse

### WebApps
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedWebApp]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.PaginatorConfig]


# ListWorkflowsResponse

### Workflows
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.ListedWorkflow]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListedAccess

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Role
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]


# ListedAgreement

### Arn
- **Type**: typing.Optional[str]

### AgreementId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### ServerId
- **Type**: typing.Optional[str]

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]


# ListedCertificate

### Arn
- **Type**: typing.Optional[str]

### CertificateId
- **Type**: typing.Optional[str]

### Usage
- **Type**: typing.Optional[typing.Literal['ENCRYPTION', 'SIGNING', 'TLS']]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE', 'PENDING_ROTATION']]

### ActiveDate
- **Type**: typing.Optional[datetime.datetime]

### InactiveDate
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['CERTIFICATE', 'CERTIFICATE_WITH_PRIVATE_KEY']]

### Description
- **Type**: typing.Optional[str]


# ListedConnector

### Arn
- **Type**: typing.Optional[str]

### ConnectorId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ListedExecution

### ExecutionId
- **Type**: typing.Optional[str]

### InitialFileLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.FileLocation]

### ServiceMetadata
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'EXCEPTION', 'HANDLING_EXCEPTION', 'IN_PROGRESS']]


# ListedHostKey

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: typing.Optional[str]

### Fingerprint
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### DateImported
- **Type**: typing.Optional[datetime.datetime]


# ListedProfile

### Arn
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### As2Id
- **Type**: typing.Optional[str]

### ProfileType
- **Type**: typing.Optional[typing.Literal['LOCAL', 'PARTNER']]


# ListedServer

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[typing.Literal['EFS', 'S3']]

### IdentityProviderType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'AWS_DIRECTORY_SERVICE', 'AWS_LAMBDA', 'SERVICE_MANAGED']]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### LoggingRole
- **Type**: typing.Optional[str]

### ServerId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['OFFLINE', 'ONLINE', 'STARTING', 'START_FAILED', 'STOPPING', 'STOP_FAILED']]

### UserCount
- **Type**: typing.Optional[int]


# ListedUser

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### Role
- **Type**: typing.Optional[str]

### SshPublicKeyCount
- **Type**: typing.Optional[int]

### UserName
- **Type**: typing.Optional[str]


# ListedWebApp

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessEndpoint
- **Type**: typing.Optional[str]

### WebAppEndpoint
- **Type**: typing.Optional[str]


# ListedWorkflow

### WorkflowId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# LoggingConfiguration

### LoggingRole
- **Type**: typing.Optional[str]

### LogGroupName
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PosixProfile

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.List[int]]


# PosixProfileOutput

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.List[int]]


# ProtocolDetails

### PassiveIp
- **Type**: typing.Optional[str]

### TlsSessionResumptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENFORCED']]

### SetStatOption
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'ENABLE_NO_OP']]

### As2Transports
- **Type**: typing.Optional[typing.List[typing.Literal['HTTP']]]


# ProtocolDetailsOutput

### PassiveIp
- **Type**: typing.Optional[str]

### TlsSessionResumptionMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENFORCED']]

### SetStatOption
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'ENABLE_NO_OP']]

### As2Transports
- **Type**: typing.Optional[typing.List[typing.Literal['HTTP']]]


# ResponseMetadata

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


# S3FileLocation

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### VersionId
- **Type**: typing.Optional[str]

### Etag
- **Type**: typing.Optional[str]


# S3InputFileLocation

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# S3StorageOptions

### DirectoryListingOptimization
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# S3Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SendWorkflowStepStateRequest

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILURE', 'SUCCESS']
- **Required**: Yes


# ServiceMetadata

### UserDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.UserDetails'>
- **Required**: Yes


# SftpConnectorConfig

### UserSecretId
- **Type**: typing.Optional[str]

### TrustedHostKeys
- **Type**: typing.Optional[typing.List[str]]


# SftpConnectorConfigOutput

### UserSecretId
- **Type**: typing.Optional[str]

### TrustedHostKeys
- **Type**: typing.Optional[typing.List[str]]


# SshPublicKey

### DateImported
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SshPublicKeyBody
- **Type**: <class 'str'>
- **Required**: Yes

### SshPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDirectoryListingRequest

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDirectoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]


# StartDirectoryListingResponse

### ListingId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFileName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# StartFileTransferRequest

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### SendFilePaths
- **Type**: typing.Optional[typing.List[str]]

### RetrieveFilePaths
- **Type**: typing.Optional[typing.List[str]]

### LocalDirectoryPath
- **Type**: typing.Optional[str]

### RemoteDirectoryPath
- **Type**: typing.Optional[str]


# StartFileTransferResponse

### TransferId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# StartServerRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# StopServerRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.Tag]
- **Required**: Yes


# TagStepDetails

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.S3Tag]]

### SourceFileLocation
- **Type**: typing.Optional[str]


# TagStepDetailsOutput

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.S3Tag]]

### SourceFileLocation
- **Type**: typing.Optional[str]


# TestConnectionRequest

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# TestConnectionResponse

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# TestIdentityProviderRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerProtocol
- **Type**: typing.Optional[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]

### SourceIp
- **Type**: typing.Optional[str]

### UserPassword
- **Type**: typing.Optional[str]


# TestIdentityProviderResponse

### Response
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccessRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.HomeDirectoryMapEntry]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfile, aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfileOutput, NoneType]

### Role
- **Type**: typing.Optional[str]


# UpdateAccessResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAgreementRequest

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LocalProfileId
- **Type**: typing.Optional[str]

### PartnerProfileId
- **Type**: typing.Optional[str]

### BaseDirectory
- **Type**: typing.Optional[str]

### AccessRole
- **Type**: typing.Optional[str]

### PreserveFilename
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### EnforceMessageSigning
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CustomDirectories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.CustomDirectoriesType]


# UpdateAgreementResponse

### AgreementId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCertificateRequest

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### InactiveDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Description
- **Type**: typing.Optional[str]


# UpdateCertificateResponse

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConnectorRequest

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: typing.Optional[str]

### As2Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.As2ConnectorConfig]

### AccessRole
- **Type**: typing.Optional[str]

### LoggingRole
- **Type**: typing.Optional[str]

### SftpConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.SftpConnectorConfig, aws_resource_validator.pydantic_models.transfer.transfer_classes.SftpConnectorConfigOutput, NoneType]

### SecurityPolicyName
- **Type**: typing.Optional[str]


# UpdateConnectorResponse

### ConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateHostKeyRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateHostKeyResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### HostKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateIds
- **Type**: typing.Optional[typing.List[str]]


# UpdateProfileResponse

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServerRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### Certificate
- **Type**: typing.Optional[str]

### ProtocolDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.ProtocolDetails, aws_resource_validator.pydantic_models.transfer.transfer_classes.ProtocolDetailsOutput, NoneType]

### EndpointDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.EndpointDetails, aws_resource_validator.pydantic_models.transfer.transfer_classes.EndpointDetailsOutput, NoneType]

### EndpointType
- **Type**: typing.Optional[typing.Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT']]

### HostKey
- **Type**: typing.Optional[str]

### IdentityProviderDetails
- **Type**: <class 'NoneType'>

### LoggingRole
- **Type**: typing.Optional[str]

### PostAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### PreAuthenticationLoginBanner
- **Type**: typing.Optional[str]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['AS2', 'FTP', 'FTPS', 'SFTP']]]

### SecurityPolicyName
- **Type**: typing.Optional[str]

### WorkflowDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetails, aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetailsOutput, NoneType]

### StructuredLogDestinations
- **Type**: typing.Optional[typing.List[str]]

### S3StorageOptions
- **Type**: <class 'NoneType'>


# UpdateServerResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserRequest

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### HomeDirectory
- **Type**: typing.Optional[str]

### HomeDirectoryType
- **Type**: typing.Optional[typing.Literal['LOGICAL', 'PATH']]

### HomeDirectoryMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.HomeDirectoryMapEntry]]

### Policy
- **Type**: typing.Optional[str]

### PosixProfile
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfile, aws_resource_validator.pydantic_models.transfer.transfer_classes.PosixProfileOutput, NoneType]

### Role
- **Type**: typing.Optional[str]


# UpdateUserResponse

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWebAppCustomizationRequest

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### LogoFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### FaviconFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# UpdateWebAppCustomizationResponse

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWebAppIdentityCenterConfig

### Role
- **Type**: typing.Optional[str]


# UpdateWebAppIdentityProviderDetails

### IdentityCenterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.UpdateWebAppIdentityCenterConfig]


# UpdateWebAppRequest

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.UpdateWebAppIdentityProviderDetails]

### AccessEndpoint
- **Type**: typing.Optional[str]

### WebAppUnits
- **Type**: <class 'NoneType'>


# UpdateWebAppResponse

### WebAppId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.transfer.transfer_classes.ResponseMetadata'>
- **Required**: Yes


# UserDetails

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WebAppIdentityProviderDetails

### IdentityCenterConfig
- **Type**: <class 'NoneType'>


# WebAppUnits

### Provisioned
- **Type**: typing.Optional[int]


# WorkflowDetail

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRole
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowDetails

### OnUpload
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetail]]

### OnPartialUpload
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetail]]


# WorkflowDetailsOutput

### OnUpload
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetail]]

### OnPartialUpload
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.transfer.transfer_classes.WorkflowDetail]]


# WorkflowStep

### Type
- **Type**: typing.Optional[typing.Literal['COPY', 'CUSTOM', 'DECRYPT', 'DELETE', 'TAG']]

### CopyStepDetails
- **Type**: <class 'NoneType'>

### CustomStepDetails
- **Type**: <class 'NoneType'>

### DeleteStepDetails
- **Type**: <class 'NoneType'>

### TagStepDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.transfer.transfer_classes.TagStepDetails, aws_resource_validator.pydantic_models.transfer.transfer_classes.TagStepDetailsOutput, NoneType]

### DecryptStepDetails
- **Type**: <class 'NoneType'>


# WorkflowStepOutput

### Type
- **Type**: typing.Optional[typing.Literal['COPY', 'CUSTOM', 'DECRYPT', 'DELETE', 'TAG']]

### CopyStepDetails
- **Type**: <class 'NoneType'>

### CustomStepDetails
- **Type**: <class 'NoneType'>

### DeleteStepDetails
- **Type**: <class 'NoneType'>

### TagStepDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.transfer.transfer_classes.TagStepDetailsOutput]

### DecryptStepDetails
- **Type**: <class 'NoneType'>


