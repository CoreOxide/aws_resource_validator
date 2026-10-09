
# AWS Resource Validator

![version](https://img.shields.io/github/v/release/CoreOxide/aws_resource_validator)
![PythonSupport](https://img.shields.io/static/v1?label=python&message=3.11-3.13&color=blue?style=flat-square&logo=python)
[![GitHub License](https://img.shields.io/github/license/CoreOxide/aws_resource_validator)](https://github.com/CoreOxide/aws_resource_validator/blob/main/LICENSE)]
![github-star-badge](https://img.shields.io/github/stars/CoreOxide/aws_resource_validator.svg?style=social)
![issues](https://img.shields.io/github/issues/CoreOxide/aws_resource_validator)

`aws_resource_validator` is a Python package that creates objects to validate, show constraints of common AWS resource names, and generate compatible patterns for tests. This helps ensure that AWS resource names comply with AWS naming rules and can be used for testing and validation purposes.

**[📜Documentation](https://coreoxide.github.io/aws_resource_validator/)** | **[Blogs website](https://alexy-grabov.medium.com/aws-resource-names-validation-and-generation-24ceb127e609)**

## Features

- **Developer CLI (`arv`)**: Validate names, inspect AWS constraints, and generate synthetic test values directly in your terminal with Rich UI output.
- **Pre-Flight Boto3 Client Wrapper (`wrap_client`)**: Catch invalid parameters, illegal characters, and bad bucket names locally in < 0.01ms before network roundtrips to AWS.
- **Universal ARN Parser (`ARN`)**: Parse, validate, and build ARNs safely — no more fragile `arn.split(":")`.
- **Validation**: Check if a given AWS resource name meets the AWS naming constraints.
- **Constraint Display**: Display constraints for different AWS resource names.
- **Pattern Generation**: Generate compatible patterns for AWS resource names for testing purposes.
- **Opt-in Pydantic pattern validation**: String fields on the generated Pydantic
  models can be checked against the AWS-documented regex + length bounds on
  demand, without changing the default construction path.

## Installation

The core package ships the resource validator and the `BaseValidatorModel`
runtime; per-service Pydantic models are shipped as extras so you only
download what you need.

```sh
# Core only (validators, generators, BaseValidatorModel).
pip install aws-resource-validator

# One or more individual services.
pip install 'aws-resource-validator[s3,ec2,lambda]'

# A whole domain shard (installs every service in that shard).
pip install 'aws-resource-validator[data]'       # storage, databases, analytics
pip install 'aws-resource-validator[security]'   # IAM, KMS, WAF, ...
pip install 'aws-resource-validator[compute]'    # EC2, Lambda, ECS, EKS, ...
pip install 'aws-resource-validator[ai]'         # Bedrock, SageMaker, ...
pip install 'aws-resource-validator[networking]' # VPC, DNS, CDN, ...
pip install 'aws-resource-validator[integration]' # SNS, SQS, EventBridge, ...
pip install 'aws-resource-validator[management]' # CloudWatch, CloudFormation, ...
pip install 'aws-resource-validator[rest]'       # Media, IoT, gaming, long tail

# Everything.
pip install 'aws-resource-validator[all]'

# Regenerate models yourself (maintainers only).
pip install 'aws-resource-validator[generator]'
```

See [`docs/packaging.md`](docs/packaging.md) for the full list of standalone
service packages, shard membership, and the detailed install matrix.

## Developer CLI (`arv`)

The package includes a command-line tool, `arv`, providing instant terminal validation, constraint inspection, and test data generation powered by [Rich](https://github.com/Textualize/rich).

```sh
# Validate an AWS resource name against AWS constraints
arv validate lambda FunctionName "my-lambda-function"

# Enforce strict end-to-end regex matching (rather than botocore prefix matching)
arv validate lambda FunctionName "invalid func! name" --strict

# Inspect naming limits, regex patterns, and sample values
arv inspect lambda FunctionName

# Inspect all patterned shapes available for a service
arv inspect dynamodb

# Generate compliant synthetic test names
arv generate lambda FunctionName --count 3

# Raw output for shell scripts and pipelines
arv generate lambda FunctionName --plain

# Machine-readable JSON output for CI/CD checks
arv validate lambda FunctionName "my-func" --json

# List registered AWS services and shape counts
arv list --search s3
```

## Pre-Flight Boto3 Client Wrapper (`wrap_client`)

Botocore does not validate parameter regex patterns or length bounds locally by default. Calling AWS with an invalid parameter transmits a network request, incurs TLS latency, and burns API rate limits before AWS returns a `400 ValidationException` hundreds of milliseconds later.

`wrap_client` intercepts AWS API calls in memory before the HTTP request is built or sent, validating parameters against AWS constraints in **under 0.01ms**:

```python
import boto3
from aws_resource_validator import wrap_client, AWSValidationError

# Intercept and validate calls locally before the HTTP network request:
s3 = wrap_client(boto3.client("s3"))

# Fails in < 0.01ms locally instead of waiting for a network handshake,
# API Gateway routing, and receiving an AWS 400 ClientError 800ms later:
try:
    s3.create_bucket(Bucket="INVALID_BUCKET_NAME")
except AWSValidationError as e:
    print(e.message)
    # Parameter 'Bucket' failed pre-flight validation for S3 shape 'BucketName':
    # Value 'INVALID_BUCKET_NAME' is invalid. Value does not match required regex pattern: ^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$
```

### Wrapping Sessions

You can also wrap an entire `boto3.Session` or `botocore.session.Session` so every client created inherits pre-flight validation automatically:

```python
import boto3
from aws_resource_validator import wrap_session

session = wrap_session(boto3.Session())
s3 = session.client("s3")
lam = session.client("lambda")
```

### Validation Modes & Configuration

- **`mode="raise"` (default)**: Raises `AWSValidationError` (subclasses both `ValueError` and `botocore.exceptions.ParamValidationError`).
- **`mode="warn"`**: Emits an `AWSValidationWarning` without aborting the call.
- **`mode="log"`**: Logs a warning via standard Python `logging`.
- **`strict=True` (default)**: Enforces end-to-end regex match (`re.fullmatch`). Set `strict=False` to allow prefix matching.
- **`custom_rules`**: Supply custom `(service, shape)` regex/length constraints for organization-specific naming standards.
- **`unwrap_client(client)` / `unwrap_session(session)`**: Cleanly detach validation hooks at any time.

## Universal ARN Parser (`ARN`)

`arn.split(":")` silently breaks on S3 object keys, CloudWatch alarm names, Lambda aliases, and anything else whose resource segment contains a colon. `ARN` splits on at most five colons, decomposes the resource into type and id, and validates every segment:

```python
from aws_resource_validator import ARN

arn = ARN.parse("arn:aws:iam::123456789012:role/service-role/MyRole")
arn.partition, arn.service, arn.region, arn.account_id
# ('aws', 'iam', '', '123456789012')
arn.resource_type, arn.resource_id
# ('role', 'service-role/MyRole')
arn.is_valid  # True

bad = ARN.parse("arn:aws:iam::12345:role/x")
bad.is_valid  # False
bad.errors    # ("Account ID '12345' must be exactly 12 digits (got 5 characters), 'aws', or empty.",)

# Build ARNs programmatically (raises ARNParseError if the result is invalid)
ARN.build(service="sqs", region="us-east-1", account_id="123456789012", resource="my-queue")
ARN.build(service="lambda", region="us-east-1", account_id="123456789012",
          resource_type="function", resource_id="my-fn:prod", delimiter=":")

# Immutable; derive variants safely
arn.replace(account_id="210987654321")
```

| ARN | `resource_type` | `resource_id` | Why `split(":")` breaks |
| :--- | :--- | :--- | :--- |
| `arn:aws:s3:::my-bucket/logs/2026:10:09.gz` | `None` | `my-bucket/logs/2026:10:09.gz` | Colons in the object key |
| `arn:aws:cloudwatch:us-east-1:123456789012:alarm:CPU:High` | `alarm` | `CPU:High` | Alarm names may contain `:` |
| `arn:aws:lambda:us-east-1:123456789012:function:fn:prod` | `function` | `fn:prod` | Alias / version suffix |

**Generic vs. botocore validation.** `is_valid` checks the generic ARN grammar (partition, service, region, 12-digit account, resource, max length 2048) with zero I/O. This covers services such as IAM, SQS, SNS, and KMS whose botocore models publish no ARN regex. Botocore's own `*Arn` shape patterns are available on demand:

```python
job = ARN.parse("arn:aws:s3:us-east-1:123456789012:job/abc")
job.validate_against("s3control", "JobArn").is_valid  # True — returns a ValidationResult
job.matching_shapes()  # [('S3control', 'JobArn'), ('S3control', 'S3ResourceArn')]
```

`ARN` is also a Pydantic v2 field type — strings are parsed and validated, and serialized back to strings:

```python
from pydantic import BaseModel

class Config(BaseModel):
    role_arn: ARN

Config(role_arn="arn:aws:iam::123456789012:role/MyRole").role_arn.resource_id  # 'MyRole'
```

From the terminal:

```sh
arv arn "arn:aws:iam::123456789012:role/service-role/MyRole"   # exit 0 / 1 (invalid) / 2 (not an ARN)
arv arn "arn:aws:s3:us-east-1:123456789012:job/abc" --json
```

## Python Usage Example

Here's a simple example demonstrating how to use `aws_resource_validator`:

```python
from aws_resource_validator.class_definitions import Acm, class_registry

# Use type hint so that you can use `api_registry` with full class definitions
acm: Acm = class_registry.Acm

print(acm.Arn.pattern)
print(acm.Arn.type)
print(acm.Arn.validate("example-arn"))
print(acm.Arn.generate())
```

Using Pydantic models for boto3 models:

```python
import boto3

from aws_resource_validator.pydantic_models.dynamodb.dynamodb_classes import ListTablesOutput

dynamodb = boto3.client('dynamodb')

def list_dynamo_tables() -> List[str]:
    return ListTablesOutput(**dynamodb.list_tables()).TableNames


if __name__ == "__main__":
    tables: List[str] = list_dynamo_tables()
    print("DynamoDB Tables:", tables)
```

### Opt-in pattern validation on generated Pydantic models

Generated models carry the AWS-documented regex + length bounds for every
string field backed by a botocore shape that defines one. The check is
**off by default** so that `Cls(**data)` behaves exactly as before — no
overhead, no new exceptions, full backward compatibility. Activate it per
call by passing `context={"aws_validate_patterns": True}` to
`model_validate`:

```python
from pydantic import ValidationError

from aws_resource_validator.pydantic_models.acm_pca.acm_pca_classes import (
    CreateCertificateAuthorityAuditReportRequestTypeDef as Req,
)

payload = {
    "CertificateAuthorityArn": "not-an-arn",
    "S3BucketName": "my-bucket",
    "AuditReportResponseFormat": "JSON",
}

# Default: no pattern check. Accepts the bad ARN silently.
Req.model_validate(payload)

# Opt-in: rejects values that don't match the AWS shape regex / length bounds.
try:
    Req.model_validate(payload, context={"aws_validate_patterns": True})
except ValidationError as exc:
    for err in exc.errors():
        # err["type"] == "aws_pattern" for fields that failed the AWS regex.
        print(err["loc"], err["type"], err["msg"])
```

Validation runs through `APIObject.validate(value)` from Pipeline A, so the
regex and length bounds are always in lockstep with `class_registry`.
Fields whose target shape has no regex (or whose annotation is more
complex than `str` / `Optional[str]` / `List[str]` / `Optional[List[str]]`)
are not decorated and pass through unchanged even when validation is
active. Unknown `(service, shape)` pairs resolve to a permissive no-op —
a stale emitter will never break a caller's validation call.

## Maintainer workflows

Day-to-day repo care is scripted under `scripts/release/`. All scripts are
invoked as modules (`python -m scripts.release.<name>`) so the `scripts/`
package resolves correctly. See [CLAUDE.md](CLAUDE.md) for the architectural
invariants these scripts assume.

### Regenerating Pydantic models after `poetry update`

`poetry update` can install a newer `boto3-stubs` whose TypedDict shapes
differ from the committed `pydantic_models/` tree. Run:

```sh
python -m scripts.release.regenerate           # Pipeline B + manifest sync + gauntlet
python -m scripts.release.regenerate --only s3 # scope to one service
python -m scripts.release.regenerate --pipeline-a  # also regen class_definitions.py (needs GITHUB_TOKEN)
python -m scripts.release.regenerate --dry-run     # preview without touching the tree
python -m scripts.release.regenerate --skip-checks # skip pytest + ruff + mypy
```

It wipes `aws_resource_validator/pydantic_models/`, reruns
`arv-generate pipeline-b`, re-syncs `pyproject.toml` extras and
`docs/packaging.md`, and runs the full pytest/ruff/mypy gauntlet. It
leaves changes unstaged for review; the suggested commit is printed at
the end. Pipeline A is off by default — it hits GitHub for live
botocore shapes and doesn't need to run on every stubs bump.

### Cutting a release

```sh
python -m scripts.release.prepare_release 2.0.3
```

Rewrites `__version__` + `[project].version`, re-pins every extra to
the new version via `sync_extras --write`, regenerates
`docs/packaging.md`, and runs the gauntlet. Leaves changes unstaged.
Then:

```sh
git add aws_resource_validator/__init__.py pyproject.toml docs/packaging.md
git commit -m "Bump version to 2.0.3"
git tag v2.0.3 && git push origin main v2.0.3
gh release create v2.0.3   # triggers release-package.yml
```

Publishing the GitHub release fires the `release-package.yml`
workflow, which builds the main wheel + 423 per-service wheels + 8
shard metapackages and uploads them to PyPI via
`scripts/release/publish_wheels.py`. The first release of a version
pays the one-time new-project registration cap (~65 min/chunk);
subsequent versions of existing projects upload in one shot.

### Other release-tooling entry points

| Script | Purpose |
|---|---|
| `build_subpackages.py` | Builds per-service + shard wheels into `dist/` (invoked by CI). |
| `publish_wheels.py` | PyPI uploader with new-project rate-limit handling. Client-side `--skip-existing` via the JSON API. |
| `verify_wheels.py` | Asserts wheel contents (no stray `__init__.py` under `pydantic_models/`, etc.). |
| `smoke_test.py` | Installs each freshly-built wheel into a throwaway venv and imports it. |
| `sync_extras.py --check` / `--write` | Reconciles `[project.optional-dependencies]` with `popular_services.txt` + `shards.toml`. CI enforces `--check`. |
| `sync_packaging_docs.py --check` / `--write` | Same for `docs/packaging.md`. |

### Popular services and shards

- `scripts/release/popular_services.txt` — one service name per line
  (directory form, e.g. `lambda_`). Each gets a dedicated
  `aws-resource-validator-<svc>` wheel and a top-level extras key.
- `scripts/release/shards.toml` — groups services into domain shards
  (metapackage wheels). Exactly one shard must have `catch_all = true`
  and it absorbs every service not explicitly listed elsewhere.

After editing either file, run
`python -m scripts.release.sync_extras --write` and
`python -m scripts.release.sync_packaging_docs --write` so
`pyproject.toml` and `docs/packaging.md` stay in sync.

### Known gotchas

- **The repo does not commit `poetry.lock`.** The circular constraint
  between the main wheel and the per-service sub-packages (pinned via
  `==<version>` in extras) can't be resolved by Poetry's lockfile
  resolver across a version bump. CI uses pip, not Poetry, for the
  same reason. See `.gitignore` for the why.
- **`pydantic_models/` is a PEP 420 namespace package.** No
  `__init__.py` under it, ever — adding one breaks cross-wheel imports
  from the `aws-resource-validator-<svc>` family. `verify_wheels.py`
  enforces this.
- **`lambda` is a Python keyword.** The service directory is
  `pydantic_models/lambda_/` but the extras key and PyPI project name
  are `lambda` and `aws-resource-validator-lambda`. Normalization
  happens in `scripts/release/_naming.py::extra_key`.

## Contributing

We welcome contributions from everyone. Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## Security

For information on reporting security vulnerabilities, please see our [SECURITY.md](SECURITY.md).

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License

This project is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out to us:

- Alexy Grabov: [alexy.grabov@gmail.com](mailto:alexy.grabov@gmail.com) ![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/alexygrabov)
- Yafit Tupman: [ytupman@gmail.com](mailto:ytupman@gmail.com) ![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/yafit-tupman)
