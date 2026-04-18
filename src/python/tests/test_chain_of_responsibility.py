import pytest

from designpatterns_examples.behavioral.chain_of_responsibility.credit_analysis import (
    CreditApplication,
    CreditRejected,
    FraudCheckHandler,
    InternalLimitHandler,
    KycCheckHandler,
    ScoreCheckHandler,
    build_default_chain,
)


def _valid_app() -> CreditApplication:
    return CreditApplication(
        score=700,
        requested_amount=10_000.0,
        fraud_flag=False,
        kyc_verified=True,
    )


def test_chain_passes_when_all_rules_ok() -> None:
    chain = build_default_chain()
    chain.process(_valid_app())


def test_chain_rejects_on_fraud() -> None:
    chain = build_default_chain()
    app = CreditApplication(
        score=700,
        requested_amount=1_000.0,
        fraud_flag=True,
        kyc_verified=True,
    )
    with pytest.raises(CreditRejected, match="fraude"):
        chain.process(app)


def test_chain_rejects_on_score() -> None:
    chain = build_default_chain()
    app = CreditApplication(
        score=400,
        requested_amount=1_000.0,
        fraud_flag=False,
        kyc_verified=True,
    )
    with pytest.raises(CreditRejected, match="Score"):
        chain.process(app)


def test_chain_order_fraud_before_score() -> None:
    """Com fraude, score não deve ser avaliado (primeiro elo barra)."""
    fraud = FraudCheckHandler()
    score = ScoreCheckHandler(minimum_score=800)
    fraud.set_next(score)

    app = CreditApplication(
        score=400,
        requested_amount=1_000.0,
        fraud_flag=True,
        kyc_verified=True,
    )
    with pytest.raises(CreditRejected, match="fraude"):
        fraud.process(app)


def test_kyc_handler_in_chain() -> None:
    chain = build_default_chain()
    app = CreditApplication(
        score=700,
        requested_amount=5_000.0,
        fraud_flag=False,
        kyc_verified=False,
    )
    with pytest.raises(CreditRejected, match="KYC"):
        chain.process(app)


def test_limit_handler_in_chain() -> None:
    chain = build_default_chain()
    app = CreditApplication(
        score=700,
        requested_amount=100_000.0,
        fraud_flag=False,
        kyc_verified=True,
    )
    with pytest.raises(CreditRejected, match="limite"):
        chain.process(app)


def test_custom_chain_order() -> None:
    """Ordem explícita: apenas score → limite."""
    score = ScoreCheckHandler(minimum_score=600)
    limit = InternalLimitHandler(max_amount=20_000.0)
    score.set_next(limit)

    score.process(
        CreditApplication(
            score=650,
            requested_amount=15_000.0,
            fraud_flag=False,
            kyc_verified=False,
        )
    )


def test_set_next_returns_handler_for_fluent_chaining() -> None:
    kyc = KycCheckHandler()
    limit = InternalLimitHandler()
    assert kyc.set_next(limit) is limit
