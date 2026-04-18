"""Chain of Responsibility: cadeia de validações para análise de crédito."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class CreditApplication:
    """Solicitação passada pelos handlers da corrente."""

    score: int
    requested_amount: float
    fraud_flag: bool
    kyc_verified: bool


class CreditRejected(Exception):
    """Bloqueio de crédito com motivo explícito (domínio)."""

    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(reason)


class CreditAnalysisHandler(ABC):
    """Base: cada elo processa ou encaminha para o próximo."""

    def __init__(self) -> None:
        self._next: CreditAnalysisHandler | None = None

    def set_next(self, handler: CreditAnalysisHandler) -> CreditAnalysisHandler:
        self._next = handler
        return handler

    @abstractmethod
    def process(self, application: CreditApplication) -> None:
        """Processa a solicitação ou delega ao próximo handler."""

    def _forward(self, application: CreditApplication) -> None:
        if self._next is not None:
            self._next.process(application)


class FraudCheckHandler(CreditAnalysisHandler):
    def process(self, application: CreditApplication) -> None:
        if application.fraud_flag:
            raise CreditRejected("Reprovado por suspeita de fraude.")
        self._forward(application)


class ScoreCheckHandler(CreditAnalysisHandler):
    def __init__(self, minimum_score: int = 600) -> None:
        super().__init__()
        self._minimum_score = minimum_score

    def process(self, application: CreditApplication) -> None:
        if application.score < self._minimum_score:
            raise CreditRejected("Score insuficiente.")
        self._forward(application)


class KycCheckHandler(CreditAnalysisHandler):
    def process(self, application: CreditApplication) -> None:
        if not application.kyc_verified:
            raise CreditRejected("KYC não verificado.")
        self._forward(application)


class InternalLimitHandler(CreditAnalysisHandler):
    def __init__(self, max_amount: float = 50_000.0) -> None:
        super().__init__()
        self._max_amount = max_amount

    def process(self, application: CreditApplication) -> None:
        if application.requested_amount > self._max_amount:
            raise CreditRejected("Valor acima do limite interno.")
        self._forward(application)


def build_default_chain() -> CreditAnalysisHandler:
    """Monta fraude → score → KYC → limite (ordem típica de negócio)."""
    fraud = FraudCheckHandler()
    score = ScoreCheckHandler()
    kyc = KycCheckHandler()
    limit = InternalLimitHandler()
    fraud.set_next(score).set_next(kyc).set_next(limit)
    return fraud
