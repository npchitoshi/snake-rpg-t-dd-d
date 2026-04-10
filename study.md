* Links:
https://medium.com/@nomannayeem/everything-you-need-to-know-about-domain-driven-design-with-python-microservices-2c2f6556b5b1

* Utilizaçao do Frozen:
Util quando queremos criar um objeto só leitura, o qual não tem ciclo de vida

* value_objects
Diferente das entidades, value_objects não tem identidade

* decorator
Função utilizada para estender o comportamento de outra classe/função
ex:
from dataclasses import dataclass
@dataclass()
Neste caso importamos dataclass, onde por padrão importar as funçoes __init__(construtor), __repr__(print do objeto) e
__eq__(funçao para comparar o objeto)