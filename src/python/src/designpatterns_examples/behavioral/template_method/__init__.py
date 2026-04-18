"""Template Method: esqueleto de algoritmo na classe base, passos nas subclasses."""

from designpatterns_examples.behavioral.template_method.report import (
    CsvReport,
    JsonReport,
    ReportGenerator,
)

__all__ = ["ReportGenerator", "CsvReport", "JsonReport"]
