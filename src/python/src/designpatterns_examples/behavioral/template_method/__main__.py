"""Demonstração: Template Method — relatórios com mesmo fluxo, formatos diferentes."""

from designpatterns_examples.behavioral.template_method.report import CsvReport, JsonReport

ROWS = [{"id": "1", "nome": "Ana"}, {"id": "2", "nome": "Bruno"}]


def main() -> None:
    print(CsvReport().generate(ROWS))
    print()
    print(JsonReport().generate(ROWS))


if __name__ == "__main__":
    main()
