# Automacao API - Postman + Newman (DummyJSON)

Colecao com cenarios para:
- Produtos: adicionar, atualizar e remover
- Usuarios: adicionar, atualizar e remover
- Auth: capturar token, usar token e validar usuario autenticado

## Requisitos
- Node.js 18+
- npm
- Newman instalado globalmente ou via npx

## Arquivos
- `postman/DummyJSON-collection.json`
- `postman/DummyJSON-environment.json`

## Execucao via Newman
```bash
npx newman run postman/DummyJSON-collection.json -e postman/DummyJSON-environment.json
```

## Validacoes implementadas
- Status code correto (200, 201, etc.)
- Tempo de resposta menor que 2000ms
- Estrutura da resposta (campos obrigatorios)
- Encadeamento de dados por variavel (productId, userId, authToken)
