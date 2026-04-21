Feature: Fluxo de realizacao de pedido
  Como usuario da loja
  Quero comprar um produto
  Para concluir um pedido com sucesso

  Scenario: Login, adicionar produto ao carrinho e seguir para checkout
    Given que acesso a home da Automation Exercise
    When eu vou para login
    And faco login com credenciais validas
    And adiciono o primeiro produto ao carrinho
    And acesso o carrinho
    Then devo visualizar o produto no carrinho
    When eu clico em Proceed To Checkout
    Then devo visualizar a tela de checkout
