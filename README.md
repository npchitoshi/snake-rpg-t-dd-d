🐍 snake-rpg-t(dd)d
Um motor de combate de RPG focado em serpentes, desenvolvido em Python 3.12+.

Mais do que um jogo, este projeto é um laboratório de arquitetura de software. Aqui, o Domain-Driven Design (DDD) estrutura o domínio, enquanto o Test-Driven Development (TDD) guia a evolução de cada funcionalidade, garantindo um código resiliente e expressivo.

🧪 Metodologia: TDD na Veia
O ciclo Red → Green → Refactor não é opcional; é o motor do desenvolvimento. A evolução do sistema é 100% orientada por testes automatizados.

🔴 Red: Escrevemos o teste que falha (ex: Serpente deve ganhar bônus de agilidade em bioma de floresta).

🟢 Green: Implementamos o código mínimo necessário para o teste passar.

🔵 Refactor: Aplicamos padrões de design (como Strategy para biomas) e limpamos o código mantendo o domínio consistente.

🏗️ Arquitetura e Design
O projeto segue os princípios da Clean Architecture e DDD, garantindo que as regras de negócio sejam independentes de detalhes técnicos.

📦 Core Domain (Lógica Pura)
Entities: Objetos com identidade única (ex: Serpente).

Value Objects: Atributos imutáveis e auto-validados (ex: HP, PotenciaDoVeneno).

Domain Services: Lógica que não pertence a uma única entidade (ex: CalculadoraDeCombate).

⚙️ Application Layer (Casos de Uso)
Orquestração do fluxo de combate.

Gerenciamento de turnos e execução de ações.

🧱 Infrastructure Layer
Persistência de dados.

Logging e integrações externas.

⚔️ Mecânicas Implementadas
🐍 Sistema de Bote: Cálculo de precisão complexo baseado em comprimento e agilidade.

☠️ Gestão de Toxinas: Diferentes tipos de veneno (neurotóxico, hemotóxico) modelados como Value Objects.

🔄 Troca de Pele (Molt): Mecânica de recuperação de status baseada em turnos de inatividade.

❤️ Estados Vitais: Controle rigoroso de vida, impedindo estados inválidos através de lógica de domínio.

🛠️ Stack Tecnológica
Linguagem: Python 3.12+ (aproveitando Generic Types e Syntactic Sugar recentes).

Testes: Pytest para uma suíte de testes expressiva.

Tipagem Estática: Mypy para segurança em tempo de desenvolvimento.

Modelagem: Dataclasses & Pydantic para estruturas de dados robustas.

🚀 Como Executar
Bash
# Clone o repositório
git clone https://github.com/seu-usuario/snake-rpg-t-dd-d.git

# Instale as dependências
pip install -r requirements.txt

# Execute os testes (O coração do projeto)
pytest
🎯 Propósito
Este repositório é um ambiente prático de estudo para:

Aplicação real de Domain-Driven Design.

Disciplina com Test-Driven Development.

Construção de arquiteturas escaláveis e desacopladas.
