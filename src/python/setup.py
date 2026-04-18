"""Compatível com `pip install -e .` quando o pip cai no caminho legado (`setup.py develop`).

Mantenha nome, versão, pacotes e extras alinhados a `[project]` em `pyproject.toml`.
"""

from pathlib import Path

from setuptools import find_packages, setup

_root = Path(__file__).resolve().parent

# Extras `dev` espelham [project.optional-dependencies] em pyproject.toml (pip pode usar setup.py em modo editável).

setup(
    name="designpatterns-examples",
    version="0.1.0",
    description="Exemplos didáticos de padrões GoF (Gang of Four)",
    long_description=(_root / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    extras_require={
        "dev": ["pytest>=8.0", "ruff>=0.4"],
    },
)
