"""Demonstração: Chain of Responsibility — análise de crédito."""

from designpatterns_examples.behavioral.chain_of_responsibility.credit_analysis import (
    CreditApplication,
    CreditRejected,
    build_default_chain,
)


def main() -> None:
    chain = build_default_chain()

    ok = CreditApplication(
        score=720,
        requested_amount=10_000.0,
        fraud_flag=False,
        kyc_verified=True,
    )
    print("--- Aprovado na cadeia (sem exceção) ---")
    chain.process(ok)
    print("Solicitação passou por todas as etapas.")

    bad_fraud = CreditApplication(
        score=720,
        requested_amount=5_000.0,
        fraud_flag=True,
        kyc_verified=True,
    )
    print("--- Rejeição na fraude ---")
    try:
        chain.process(bad_fraud)
    except CreditRejected as e:
        print(e.reason)

    bad_score = CreditApplication(
        score=500,
        requested_amount=5_000.0,
        fraud_flag=False,
        kyc_verified=True,
    )
    print("--- Rejeição no score ---")
    try:
        chain.process(bad_score)
    except CreditRejected as e:
        print(e.reason)


if __name__ == "__main__":
    main()
