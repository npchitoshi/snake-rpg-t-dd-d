<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/snake_1f40d.png" width="120" alt="Snake RPG Logo"/>
</p>

<h1 align="center">🐍 snake-rpg-t(dd)d</h1>

<p align="center">
  <strong>Um motor de combate RPG focado em serpentes, forjado com TDD e DDD.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+"/></a>
  <a href="#-metodologia-tdd-na-veia"><img src="https://img.shields.io/badge/TDD-Red%20→%20Green%20→%20Refactor-brightgreen?style=for-the-badge" alt="TDD"/></a>
  <a href="#-arquitetura-e-design"><img src="https://img.shields.io/badge/DDD-Domain--Driven%20Design-blueviolet?style=for-the-badge" alt="DDD"/></a>
  <a href="https://github.com/npchitoshi/snake-rpg-t-dd-d/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License MIT"/></a>
</p>

<p align="center">
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-metodologia-tdd-na-veia">Metodologia</a> •
  <a href="#️-arquitetura-e-design">Arquitetura</a> •
  <a href="#️-mecânicas-de-combate">Mecânicas</a> •
  <a href="#️-stack-tecnológica">Stack</a> •
  <a href="#-como-executar">Como Executar</a>
</p>

---

## 📖 Sobre o Projeto

> *Mais do que um jogo — um laboratório de arquitetura de software.*

O **snake-rpg-t(dd)d** é um motor de combate de RPG temático de serpentes, desenvolvido em **Python 3.12+**. O projeto serve como um ambiente prático de estudo onde o **Domain-Driven Design (DDD)** estrutura o domínio do problema, e o **Test-Driven Development (TDD)** guia a evolução de cada funcionalidade — garantindo um código **resiliente**, **expressivo** e **desacoplado**.

O nome do projeto é um trocadilho intencional:
- **t(dd)d** → **TDD** (Test-Driven Development) + **DDD** (Domain-Driven Design), os dois pilares metodológicos do projeto.

---

## 🧪 Metodologia: TDD na Veia

O ciclo **Red → Green → Refactor** não é opcional; é o **motor do desenvolvimento**. A evolução do sistema é 100% orientada por testes automatizados.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   🔴 RED           🟢 GREEN          🔵 REFACTOR       │
│   Escreva o        Implemente o      Aplique padrões    │
│   teste que        código mínimo     de design e        │
│   falha            para passar       limpe o código     │
│                                                         │
│   ────────────►   ────────────►   ──────────┐          │
│                                              │          │
│   ◄──────────────────────────────────────────┘          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

| Fase | Ação | Exemplo |
|------|------|---------|
| 🔴 **Red** | Escrevemos o teste que falha | *"Serpente deve ganhar bônus de agilidade em bioma de floresta"* |
| 🟢 **Green** | Implementamos o código mínimo para o teste passar | Lógica básica de bônus no bioma |
| 🔵 **Refactor** | Aplicamos padrões de design e limpamos o código | Strategy Pattern para biomas |

---

## 🏗️ Arquitetura e Design

O projeto segue os princípios da **Clean Architecture** e **DDD**, garantindo que as regras de negócio sejam completamente independentes de detalhes técnicos.

```
snake-rpg-t-dd-d/
│
├── 📦 domain/                    # Core Domain (Lógica Pura)
│   ├── entities/                 # Objetos com identidade única
│   │   └── serpente.py           #   → Serpente (entidade principal)
│   ├── value_objects/            # Atributos imutáveis e auto-validados
│   │   ├── hp.py                 #   → Pontos de Vida
│   │   └── potencia_do_veneno.py #   → Potência do Veneno
│   └── services/                 # Lógica cross-entity
│       └── calculadora_combate.py#   → Cálculos de combate
│
├── ⚙️ application/               # Casos de Uso
│   ├── combate_service.py        # Orquestração do fluxo de combate
│   └── turno_manager.py          # Gerenciamento de turnos
│
├── 🧱 infrastructure/            # Detalhes Técnicos
│   ├── persistence/              # Persistência de dados
│   └── logging/                  # Logging e integrações
│
└── 🧪 tests/                     # Suíte de Testes (o coração do projeto)
    ├── unit/
    └── integration/
```

### Camadas

| Camada | Responsabilidade | Exemplos |
|--------|-----------------|----------|
| **📦 Core Domain** | Lógica de negócio pura, sem dependências externas | `Serpente`, `HP`, `PotenciaDoVeneno`, `CalculadoraDeCombate` |
| **⚙️ Application** | Orquestração de casos de uso | Fluxo de combate, gerenciamento de turnos |
| **🧱 Infrastructure** | Detalhes técnicos e integrações | Persistência, logging, I/O |

---

## ⚔️ Mecânicas de Combate

<table>
  <tr>
    <td width="50%">

### 🐍 Sistema de Bote
Cálculo de **precisão complexo** baseado no comprimento e agilidade da serpente. Quanto mais longa e ágil, mais preciso o ataque.

### ☠️ Gestão de Toxinas
Diferentes tipos de veneno modelados como **Value Objects**:
- 🧠 **Neurotóxico** — afeta ações do oponente
- 🩸 **Hemotóxico** — dano contínuo por turno

</td>
<td width="50%">

### 🔄 Troca de Pele (Molt)
Mecânica de **recuperação de status** baseada em turnos de inatividade. A serpente entra em estado vulnerável para se regenerar.

### ❤️ Estados Vitais
Controle rigoroso de vida, **impedindo estados inválidos** através de lógica de domínio. O HP é um Value Object auto-validado.

</td>
  </tr>
</table>

---

## 🛠️ Stack Tecnológica

| Tecnologia | Uso | Detalhes |
|:----------:|-----|---------|
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="24"/> **Python 3.12+** | Linguagem | Generic Types, Syntactic Sugar moderno |
| 🧪 **Pytest** | Testes | Suíte de testes expressiva e poderosa |
| 🔍 **Mypy** | Tipagem estática | Segurança em tempo de desenvolvimento |
| 📐 **Dataclasses & Pydantic** | Modelagem | Estruturas de dados robustas e validadas |

---

## 🚀 Como Executar

### Pré-requisitos

- [Python 3.12+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/npchitoshi/snake-rpg-t-dd-d.git
cd snake-rpg-t-dd-d

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Executando os Testes

```bash
# Execute a suíte completa (o coração do projeto ❤️)
pytest

# Com cobertura de código
pytest --cov=domain --cov=application -v

# Verificação de tipos estáticos
mypy .
```

---

## 🎯 Propósito

Este repositório é um **ambiente prático de estudo** para:

- ✅ Aplicação real de **Domain-Driven Design** (Entities, Value Objects, Services)
- ✅ Disciplina com **Test-Driven Development** (Red → Green → Refactor)
- ✅ Construção de **arquiteturas escaláveis e desacopladas** (Clean Architecture)
- ✅ Exploração de **padrões de design** aplicados a domínios complexos (Strategy, Observer, etc.)
- ✅ Prática de **tipagem estática** e modelagem de dados em Python moderno
