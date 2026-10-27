import pytest

from kit_teste_python.nucleo import saudacao


def test_saudacao_usa_o_nome():
    assert saudacao(" Ana ") == "Olá, Ana!"


def test_saudacao_recusa_nome_vazio():
    with pytest.raises(ValueError):
        saudacao("   ")
