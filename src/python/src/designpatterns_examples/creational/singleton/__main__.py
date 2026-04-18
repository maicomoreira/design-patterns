"""Demonstração: Singleton — configuração compartilhada."""

from designpatterns_examples.creational.singleton.settings import AppSettings


def main() -> None:
    a = AppSettings()
    b = AppSettings()
    a.set("theme", "escuro")
    print(a is b)  # True
    print(b.get("theme"))  # escuro


if __name__ == "__main__":
    main()
