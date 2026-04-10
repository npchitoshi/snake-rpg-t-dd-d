from dataclasses import dataclass, field
from domain.value_objects.hp import HP
from domain.bestiario import SnakesNames

@dataclass
class Snake:
    numero: int
    especie: str = field(init=False)
    apelido: str = None
    hp: HP
    status: str = "VIVO"

    def receber_golpe(self, dano: int) -> None:
        self.hp = self.hp.receber_dano(dano)

        if self.hp.atual == 0:
            self.status = "MORTO"