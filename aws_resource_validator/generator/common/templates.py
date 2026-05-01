"""Shared Jinja2 environment factory used by both pipeline emitters.

The environment (and the compiled templates it loads) is cached per
directory; a full regeneration run otherwise re-parses the same Jinja
template files on every service.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from functools import cache
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape


@cache
def get_environment(template_dir: str) -> Environment:
    env = Environment(
        loader=FileSystemLoader(template_dir),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=select_autoescape(),
    )
    env.filters["repr"] = repr
    return env


def build_environment(template_dir: Path, filters: Mapping[str, Callable[..., object]] | None = None) -> Environment:
    """Return a shared ``Environment`` for ``template_dir``, adding ``filters`` if provided."""
    env = get_environment(str(template_dir.resolve()))
    if filters:
        env.filters.update(filters)
    return env
