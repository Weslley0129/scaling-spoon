# Plano de Testes Web - Automation Exercise

Sistema alvo: [automationexercise.com](https://automationexercise.com/)

## Escopo
Validar o fluxo principal de compra (home -> login/cadastro -> produto -> carrinho -> checkout) e fluxos complementares.

## Suites e Casos (min. 3 por suite)

## 1) Home
1. CT-HOME-01: Validar carregamento da home (menu, banner, categorias).  
2. CT-HOME-02: Validar busca de produto pela barra de pesquisa.  
3. CT-HOME-03: Validar navegação para página de produtos pelo menu.

## 2) Login
1. CT-LOGIN-01: Login com credenciais válidas.  
2. CT-LOGIN-02: Login com senha inválida (mensagem de erro).  
3. CT-LOGIN-03: Logout após login bem-sucedido.

## 3) Cadastro
1. CT-CAD-01: Iniciar cadastro com e-mail novo.  
2. CT-CAD-02: Validar campos obrigatórios no formulário de cadastro.  
3. CT-CAD-03: Tentar cadastro com e-mail já existente.

## 4) Página de Produto
1. CT-PROD-01: Abrir detalhe do produto e validar nome/preço.  
2. CT-PROD-02: Adicionar produto ao carrinho pelo detalhe.  
3. CT-PROD-03: Validar quantidade no carrinho após adicionar.

## 5) Carrinho
1. CT-CART-01: Validar produto adicionado no carrinho.  
2. CT-CART-02: Alterar quantidade de item no carrinho.  
3. CT-CART-03: Remover item do carrinho.

## 6) Checkout
1. CT-CHK-01: Iniciar checkout com usuário autenticado.  
2. CT-CHK-02: Validar endereço e resumo do pedido.  
3. CT-CHK-03: Finalizar pedido e validar confirmação.

## 7) Fluxo de Pedido (E2E)
1. CT-E2E-01: Login -> escolher produto -> carrinho -> checkout.  
2. CT-E2E-02: Cadastro novo usuário -> compra completa.  
3. CT-E2E-03: Compra com alteração de quantidade e validação de total.

## Execução Manual
- Executar ao menos 1 ciclo completo para todos os casos acima.
- Registrar evidências: screenshot, data/hora, resultado (Pass/Fail), observações.

## Template de Evidência
- ID do teste:
- Data/Hora:
- Ambiente:
- Passos executados:
- Resultado obtido:
- Resultado esperado:
- Status (Pass/Fail):
- Evidência (arquivo imagem/link):
