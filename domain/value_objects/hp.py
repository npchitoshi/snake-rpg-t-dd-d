from dataclasses import dataclass

@dataclass(frozen=True)
class HP:
    atual: int
    maximo: int

    LIMITE_GLOBAL_SISTEMA = 255

    def __post_init__(self) -> None:
        if self.atual < 0:
            raise ValueError("O HP não pode ser negativo")

        if self.atual > self.maximo:
            raise ValueError("O HP atual não pode ser maior que o valor máximo")

        if self.maximo > self.LIMITE_GLOBAL_SISTEMA:
            raise ValueError("O HP não pode ultrapassar o valor de 255")
