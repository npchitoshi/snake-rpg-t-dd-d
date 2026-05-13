from dataclasses import dataclass, field
from domain.value_objects.hp import HP
from domain.bestiario import SnakesNames

@dataclass
class Snake:
    numero: int
    _hp: HP
    especie: str = field(init=False)
    apelido: str = None
    status: str = "VIVO"

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, novo_hp: HP):
        if (self.status == "VIVO"):
            self._hp = novo_hp
        self._verifica_se_morreu()

    def __post_init__(self):
        if self._hp.atual == 0:
            raise ValueError("Não é permitido criar uma Snake morta")

        self.especie = SnakesNames.get(self.numero, "Espécie Desconhecida")
        self._verifica_se_morreu()

    def receber_golpe(self, dano: int) -> None:
        self.hp = self.hp.receber_dano(dano)

    def _verifica_se_morreu(self):
        if (self._hp.atual == 0):
            self.status = "MORTO"
