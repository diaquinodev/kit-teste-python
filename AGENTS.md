# kit-teste-python — regras para agentes

Teste do kit

Vale para Claude Code, Codex e Gemini CLI. As regras gerais (trilhas, troca de agente,
honestidade) vêm do QG `agente-meriadoque`; aqui está o que um agente precisa saber
para trabalhar neste repositório sem ter o QG aberto.

## Ao começar

1. Leia o `HANDOFF.md`, se existir. Se o usuário disser só "continuar", retome dali:
   confira `git status` e siga o "Próximo comando".
2. Leia o plano da fase em andamento (link no `HANDOFF.md`).

## Durante o trabalho

- Uma branch e um PR **draft** por fase; nunca commit direto na `main`.
- Fase média ou grande: crie o `HANDOFF.md` a partir de `scripts/HANDOFF.modelo.md` e
  atualize no mesmo commit de cada passo.
- Antes de cada commit, rode a verificação abaixo e `sh scripts/handoff-check`.
- Descrição do PR com `Autor:` (o agente que escreveu); a revisão é feita por outro agente.

## Verificação

```
python -m ruff check . && python -m ruff format --check . && python -m pytest
```

## Dados e segredos

- Dados sempre fictícios no repositório; dados reais ficam em `dados/` (ignorada pelo Git).
- Segredos só no `.env` (ignorado); documente cada chave no `.env.example`.
