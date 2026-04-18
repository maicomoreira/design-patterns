"""Relatórios: o fluxo `generate` é fixo; formatos variam nas subclasses."""

from __future__ import annotations

from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    """Define o template method e delega passos variáveis às subclasses."""

    def generate(self, records: list[dict[str, str]]) -> str:
        header = self._header()
        body = self._format_body(records)
        footer = self._footer()
        return f"{header}\n{body}\n{footer}"

    def _header(self) -> str:
        return "--- Relatório ---"

    @abstractmethod
    def _format_body(self, records: list[dict[str, str]]) -> str:
        """Formato específico (CSV, JSON, etc.)."""

    def _footer(self) -> str:
        return "--- fim ---"


class CsvReport(ReportGenerator):
    def _format_body(self, records: list[dict[str, str]]) -> str:
        if not records:
            return ""
        keys = list(records[0].keys())
        lines = [",".join(keys)]
        for row in records:
            lines.append(",".join(row[k] for k in keys))
        return "\n".join(lines)


class JsonReport(ReportGenerator):
    def _format_body(self, records: list[dict[str, str]]) -> str:
        import json

        return json.dumps(records, ensure_ascii=False, indent=2)
