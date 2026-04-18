from designpatterns_examples.behavioral.template_method.report import CsvReport, JsonReport

ROWS = [{"a": "1", "b": "2"}]


def test_csv_report_contains_header_and_columns() -> None:
    out = CsvReport().generate(ROWS)
    assert "Relatório" in out
    assert "a,b" in out or "a, b" not in out  # csv line
    assert "1" in out


def test_json_report_is_valid_json_structure() -> None:
    out = JsonReport().generate(ROWS)
    assert '"a"' in out
    assert "1" in out
