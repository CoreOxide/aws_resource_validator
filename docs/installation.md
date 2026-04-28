# Installation

The core package ships the resource validator and the `BaseValidatorModel`
runtime; per-service Pydantic models are shipped as extras so you only
download what you need.

```sh
# Core only — validators, generators, BaseValidatorModel.
pip install aws-resource-validator

# One or more individual services.
pip install 'aws-resource-validator[s3,ec2,lambda]'

# A whole domain shard (installs every service in that shard).
pip install 'aws-resource-validator[data]'

# Everything.
pip install 'aws-resource-validator[all]'
```

## Requirements

- Python 3.11+
- `pip` 22+ (for PEP 517 / PEP 621 install support).

## Which extra do I want?

- **Popular AWS services** (`s3`, `ec2`, `lambda`, `dynamodb`, `iam`, …) each
  ship as an individual extra and PyPI project.
- **Everything else** ships inside a **domain shard** — install e.g.
  `aws-resource-validator[security]` to get every IAM-related service at once.
- Extras are composable: `pip install 'aws-resource-validator[s3,security]'`.

See **[Packaging & extras](packaging.md)** for the complete list of standalone
services and shard membership.
