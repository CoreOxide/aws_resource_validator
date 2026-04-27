"""Registry mapping service names to :class:`~.Service` instances."""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from types import MappingProxyType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_resource_validator.core.service import Service


class APIRegistry(Mapping[str, "Service"]):
    """A mapping of service names (PascalCase) to :class:`Service` instances.

    Behaves like a standard :class:`~collections.abc.Mapping` and additionally
    supports attribute-style access (``registry.Acm``) for ergonomic use in
    hand-written consumer code.
    """

    __slots__ = ("_services",)

    def __init__(self) -> None:
        self._services: dict[str, Service] = {}

    @property
    def services(self) -> Mapping[str, Service]:
        """Read-only view of registered services keyed by PascalCase name."""
        return MappingProxyType(self._services)

    def add(self, service: Service) -> None:
        """Register a service by its canonical PascalCase name."""
        self._services[service.service_name] = service

    def add_service(self, service: Service) -> None:
        """Legacy alias; the committed ``class_definitions.py`` calls this name.

        Remove once Pipeline A regenerates the file.
        """
        self.add(service)

    def __getitem__(self, name: str) -> Service:
        return self._services[name]

    def __iter__(self) -> Iterator[str]:
        return iter(self._services)

    def __len__(self) -> int:
        return len(self._services)

    def __contains__(self, name: object) -> bool:
        return name in self._services

    def __getattr__(self, name: str) -> Service:
        services: dict[str, Service] = object.__getattribute__(self, "_services")
        if name in services:
            return services[name]
        raise AttributeError(f"{type(self).__name__!r} has no service {name!r}")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(services={len(self)})"
