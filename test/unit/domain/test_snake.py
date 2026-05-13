import pytest
from domain.entities.snake import Snake
from domain.value_objects.hp import HP

def test_criar_snake_com_sucesso():
    hp = HP(atual=10, maximo=10)
    snake = Snake(numero=1, _hp=hp)

    assert snake.hp == hp
    assert snake.status == "VIVO"
    assert snake.especie is not None

def test_snake_falha_ao_ser_criada_com_hp_zero():
    hp_zero = HP(atual=0, maximo=100)

    with pytest.raises(ValueError, match="Não é permitido criar uma Snake morta"):
        Snake(numero=1, _hp=hp_zero)

def test_snake_deve_morrer_quando_hp_chegar_a_zero():
    hp = HP(atual=10, maximo=10)
    snake = Snake(numero=1, _hp=hp)

    hp_apos_dano = snake.hp.receber_dano(10)

    snake.hp = hp_apos_dano

    assert snake._hp.atual == 0
    assert snake.status == "MORTO"
