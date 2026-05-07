from domain.entities.snake import Snake
from domain.value_objects.hp import HP


def test_criar_snake_com_sucesso():
    hp = HP(atual=10, maximo=10)
    snake = Snake(numero=1, hp=hp)

    assert snake.hp == hp
    assert snake.status == "VIVO"
    assert snake.especie is not None

# def test_snake_falha_ao_ser_criada_sem_hp():

# def test_snake_deve_morrer_quando_hp_chegar_a_zero():