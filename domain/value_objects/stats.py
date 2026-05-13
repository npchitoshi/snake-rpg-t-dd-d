from dataclasses import dataclass

@dataclass(frozen=True)
class Stats:
    forca: int
    defesa: int
    velocidade: int
    precisao: int

    LIMITE_ATRIBUTO = 255
    LIMITE_PRECISAO = 100

    def __post_init__(self) -> None:
        for nome, valor in [("forca", self.forca),
                            ("defesa", self.defesa),
                            ("velocidade", self.velocidade)]:
            if not (0 <= valor <= self.LIMITE_ATRIBUTO):
                raise ValueError(f"O campo {nome} deve estar entre 0 e {self.LIMITE_ATRIBUTO}")

        if not (0 <= self.precisao <= self.LIMITE_PRECISAO):
             raise ValueError(f"A precisão deve estar entre 0 e {self.LIMITE_PRECISAO}")