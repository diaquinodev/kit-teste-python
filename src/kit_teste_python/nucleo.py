"""Regras de negócio puras: sem rede, sem arquivo, fáceis de testar."""


def saudacao(nome: str) -> str:
    """Exemplo; substitua pela primeira regra de negócio do projeto."""
    nome = nome.strip()
    if not nome:
        raise ValueError("nome vazio")
    return f"Olá, {nome}!"
