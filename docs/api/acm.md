# Acm Class

**Acm** class represents an AWS ACM resource and includes methods for validation and generation of ARNs.

## Attributes

- **Arn**: string, pattern: `arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`, min length: 20, max length: 2048
- **CertificateBody**: string, pattern: `-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?`, min length: 1, max length: 32768
- **CertificateChain**: string, pattern: `(-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}\u000D?\u000A)*-{5}BEGIN CERTIFICATE-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END CERTIFICATE-{5}(\u000D?\u000A)?`, min length: 1, max length: 2097152
- **DomainNameString**: string, pattern: `^(\*\.)?(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])$`, min length: 1, max length: 253
- **IdempotencyToken**: string, pattern: `\w+`, min length: 1, max length: 32
- **NextToken**: string, pattern: `[\u0009\u000A\u000D\u0020-\u00FF]*`, min length: 1, max length: 10000
- **PcaArn**: string, pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*`, min length: 20, max length: 2048
- **PrivateKey**: string, pattern: `-{5}BEGIN PRIVATE KEY-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END PRIVATE KEY-{5}(\u000D?\u000A)?`, min length: 1, max length: 524288
- **TagKey**: string, pattern: `[\p{L}\p{Z}\p{N}_.:\/=+\-@]*`, min length: 1, max length: 128
- **TagValue**: string, pattern: `[\p{L}\p{Z}\p{N}_.:\/=+\-@]*`, min length: 0, max length: 256

## Methods

### validate

Validates the given ARN.

**Parameters:**
- `arn` (str): The ARN to validate.

**Returns:**
- `bool`: True if the ARN is valid, False otherwise.

### generate

Generates a valid ARN.

**Returns:**
- `str`: A valid ARN.

## Example Usage

```python
from aws_resource_validator.class_definitions import Acm

arn = "arn:aws:acm:region:account-id:certificate/certificate-id"
if Acm.validate(arn):
    print("The ARN is valid.")
else:
    print("The ARN is invalid.")

new_arn = Acm.generate()
print("Generated ARN:", new_arn)
