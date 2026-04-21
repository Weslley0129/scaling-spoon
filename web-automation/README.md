# Automacao Web - Cypress + Cucumber

Projeto de automacao E2E para o site [automationexercise.com](https://automationexercise.com/), com foco no fluxo de realizacao de pedido.

## Requisitos
- Node.js 18+
- npm

## Instalacao
```bash
npm install
```

## Variaveis de ambiente
Crie um arquivo `cypress.env.json`:
```json
{
  "AE_EMAIL": "seu_email_cadastrado_no_site",
  "AE_PASSWORD": "sua_senha"
}
```

## Execucao dos testes
- Modo interativo:
```bash
npm run cy:open
```
- Modo headless:
```bash
npm run cy:run
```

## Estrutura
- `cypress/e2e/order-flow.feature`: cenario em Gherkin
- `cypress/e2e/step_definitions/order-flow.cy.js`: passos do Cucumber
- `cypress/support/`: comandos customizados

## Evidencias
Ao rodar em modo headless, o Cypress gera screenshots/videos em caso de falhas (se configurado).
