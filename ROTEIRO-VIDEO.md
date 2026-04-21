# Roteiro de Video (3 a 5 minutos)

## 1) Abertura (20-30s)
Fala sugerida:
"Neste video vou apresentar minha entrega final da disciplina de Qualidade e Teste de Software, com automacao Web usando Cypress + Cucumber e automacao de APIs usando Postman + Newman."

## 2) Visao geral do repositorio (30-40s)
Mostre no explorador:
- pasta `web-automation`
- pasta `api-automation`
- pasta `final-avaliacao/docs`

Fala sugerida:
"Organizei o repositorio separando claramente a automacao Web e a automacao de APIs, alem dos documentos de plano de testes e evidencias."

## 3) Casos de teste e plano (40-60s)
Abra:
- `final-avaliacao/docs/plano-de-testes-web.md`
- `final-avaliacao/docs/plano-de-testes-web.pdf`

Fala sugerida:
"Aqui estao as 7 suites com no minimo 3 casos por suite, cobrindo Home, Login, Cadastro, Produto, Carrinho, Checkout e fluxo ponta a ponta de pedido."

## 4) Automacao Web (60-90s)
Abra:
- `web-automation/cypress/e2e/order-flow.feature`
- `web-automation/cypress/e2e/step_definitions/order-flow.cy.js`
- `web-automation/README.md`

Mostre comando no terminal:
```bash
npm install
npm run cy:run
```

Fala sugerida:
"A automacao Web foi implementada com Cypress e Cucumber no formato BDD. O cenario automatiza o fluxo de login, adicao de produto ao carrinho e acesso ao checkout."

## 5) Automacao API (60-90s)
Abra:
- `api-automation/postman/DummyJSON-collection.json`
- `api-automation/postman/DummyJSON-environment.json`
- `api-automation/README.md`

Mostre comando:
```bash
npx newman run postman/DummyJSON-collection.json -e postman/DummyJSON-environment.json
```

Fala sugerida:
"Na parte de API, automatizei cenarios de adicionar, atualizar e remover produtos e usuarios, alem do fluxo de autenticacao com token e validacao de usuario. Os testes validam status code, tempo menor que 2 segundos e estrutura da resposta."

## 6) Evidencias e encerramento (20-30s)
Abra:
- `final-avaliacao/docs/evidencias-execucao-manual.md`

Fala sugerida:
"Aqui esta o modelo de evidencias da execucao manual. Com isso concluo a entrega com plano de testes, automacoes e instrucoes de execucao."
