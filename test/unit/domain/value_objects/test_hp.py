import pytest

from domain.value_objects.hp import HP

def test_hp_nao_pode_ser_iniciado_com_valor_negativo():
    with pytest.raises(ValueError, match="O HP não pode ser negativo"):
        HP(atual=-5, maximo=100)

def test_hp_atual_nao_pode_ser_maior_hp_maximo():
    with pytest.raises(ValueError, match="O HP atual não pode ser maior que o valor máximo"):
        HP(atual=51, maximo=50)

def test_hp_nao_pode_ser_maior_que_valor_maximo():
    with pytest.raises(ValueError, match="O HP não pode ultrapassar o valor de 255"):
        HP(atual=100, maximo=256)