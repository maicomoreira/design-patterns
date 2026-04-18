"""Configuração global com Singleton thread-safe (double-checked locking simplificado)."""

from __future__ import annotations

import threading
from typing import Any


class AppSettings:
    """Garante uma única instância de configurações da aplicação."""

    _instance: AppSettings | None = None
    _lock = threading.Lock()

    def __new__(cls) -> AppSettings:
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, "_initialized", False):
            return
        self._values: dict[str, Any] = {}
        self._initialized = True

    def set(self, key: str, value: Any) -> None:
        self._values[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._values.get(key, default)
