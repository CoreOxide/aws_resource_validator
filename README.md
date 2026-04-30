
# AWS Resource Validator

![version](https://img.shields.io/github/v/release/CoreOxide/aws_resource_validator)
![PythonSupport](https://img.shields.io/static/v1?label=python&message=3.11-3.13&color=blue?style=flat-square&logo=python)
[![GitHub License](https://img.shields.io/github/license/CoreOxide/aws_resource_validator)](https://github.com/CoreOxide/aws_resource_validator/blob/main/LICENSE)]
![github-star-badge](https://img.shields.io/github/stars/CoreOxide/aws_resource_validator.svg?style=social)
![issues](https://img.shields.io/github/issues/CoreOxide/aws_resource_validator)

`aws_resource_validator` is a Python package that creates objects to validate, show constraints of common AWS resource names, and generate compatible patterns for tests. This helps ensure that AWS resource names comply with AWS naming rules and can be used for testing and validation purposes.

**[📜Documentation](https://coreoxide.github.io/aws_resource_validator/)** | **[Blogs website](https://alexy-grabov.medium.com/aws-resource-names-validation-and-generation-24ceb127e609)**

## Features

- **Validation**: Check if a given AWS resource name meets the AWS naming constraints.
- **Constraint Display**: Display constraints for different AWS resource names.
- **Pattern Generation**: Generate compatible patterns for AWS resource names for testing purposes.

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

## Usage Example

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

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out to us:

- Alexy Grabov: [alexy.grabov@gmail.com](mailto:alexy.grabov@gmail.com) ![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/alexygrabov)
- Yafit Tupman: [ytupman@gmail.com](mailto:ytupman@gmail.com) ![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/yafit-tupman)
