"""Tests for :mod:`aws_resource_validator.generator.pipeline_b.shape_pattern_map`."""

from __future__ import annotations

import logging

import pytest

from aws_resource_validator.generator.pipeline_b import shape_pattern_map
from aws_resource_validator.generator.pipeline_b.shape_pattern_map import (
    FieldPatternLookup,
    _botocore_service_name,
    get_pattern_map,
)


@pytest.fixture(autouse=True)
def _reset_lru_cache() -> None:
    get_pattern_map.cache_clear()


class TestBotocoreServiceName:
    def test_strips_trailing_keyword_underscore(self) -> None:
        assert _botocore_service_name("lambda_") == "lambda"

    def test_replaces_internal_underscore_with_hyphen(self) -> None:
        assert _botocore_service_name("acm_pca") == "acm-pca"
        assert _botocore_service_name("application_autoscaling") == "application-autoscaling"

    def test_plain_name_unchanged(self) -> None:
        assert _botocore_service_name("s3") == "s3"


class TestKnownService:
    def test_acm_pca_scalar_pattern_resolved(self) -> None:
        lookup = get_pattern_map("acm_pca")
        assert not lookup.is_empty()
        scalar, list_member = lookup.for_field(
            "CreateCertificateAuthorityAuditReportRequestTypeDef",
            "CertificateAuthorityArn",
        )
        assert scalar == "Arn"
        assert list_member is None

    def test_strips_typedef_suffix_on_lookup(self) -> None:
        lookup = get_pattern_map("acm_pca")
        # Callers may pass either the stub's ``*TypeDef`` class name or the
        # bare botocore struct name; stripping makes the two symmetric.
        via_stub = lookup.for_field(
            "CreateCertificateAuthorityAuditReportRequestTypeDef", "CertificateAuthorityArn"
        )
        via_struct = lookup.for_field(
            "CreateCertificateAuthorityAuditReportRequest", "CertificateAuthorityArn"
        )
        assert via_stub == via_struct == ("Arn", None)

    def test_non_pattern_field_returns_none_tuple(self) -> None:
        lookup = get_pattern_map("acm_pca")
        assert lookup.for_field(
            "CreateCertificateAuthorityRequestTypeDef", "RevocationConfiguration"
        ) == (None, None)

    def test_list_member_pattern_resolved(self) -> None:
        # IAM's GetContextKeysForCustomPolicyRequest.PolicyInputList is a list of
        # strings whose member shape has a pattern — exercises the list branch.
        lookup = get_pattern_map("iam")
        scalar, list_member = lookup.for_field(
            "GetContextKeysForCustomPolicyRequestTypeDef", "PolicyInputList"
        )
        assert scalar is None
        assert list_member == "policyDocumentType"


class TestFailureModes:
    def test_unknown_service_returns_empty(
        self, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
    ) -> None:
        from botocore.exceptions import UnknownServiceError
        from botocore.session import Session

        def _boom(self, name):
            raise UnknownServiceError(service_name=name, known_service_names=[])

        monkeypatch.setattr(Session, "get_service_model", _boom)
        caplog.set_level(logging.WARNING, logger=shape_pattern_map.__name__)

        lookup = get_pattern_map("never_heard_of_this_service")

        assert isinstance(lookup, FieldPatternLookup)
        assert lookup.is_empty()
        assert lookup.for_field("AnythingTypeDef", "Anything") == (None, None)
        assert any("never_heard_of_this_service" in rec.message for rec in caplog.records)

    def test_unknown_typeddict_is_none(self) -> None:
        lookup = get_pattern_map("acm_pca")
        assert lookup.for_field("TotallyFakeTypeDef", "Bogus") == (None, None)
