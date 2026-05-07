from dataclasses import dataclass, field
from domain.value_objects.hp import HP
from domain.bestiario import SnakesNames

@dataclass
class Snake:
    numero: int
    hp: HP
    especie: str = field(init=False)
    apelido: str = None
    status: str = "VIVO"

    def __post_init__(self):
        self.especie = SnakesNames.get(self.numero, "Espécie Desconhecida")

    def receber_golpe(self, dano: int) -> None:
        self.hp = self.hp.receber_dano(dano)

        if self.hp.atual == 0:
            self.status = "MORTO"