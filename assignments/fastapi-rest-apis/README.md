# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objective

Construir uma API REST simples com FastAPI para praticar rotas HTTP, validação de dados com Pydantic e respostas em JSON. Ao final, o aluno terá um serviço pequeno, organizado e pronto para ser testado com um cliente HTTP.

## 📝 Tasks

### 🛠️ Definir a base da aplicação FastAPI

#### Descrição
Crie a estrutura inicial da API, configure a aplicação FastAPI e adicione rotas básicas para verificar se o serviço está funcionando.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com uma rota raiz `/`.
- Criar uma rota `/health` que retorne um status de saúde da API.
- Retornar respostas em formato JSON.
- Organizar o código de forma que seja fácil adicionar novas rotas depois.

### 🛠️ Implementar recursos em memória

#### Descrição
Implemente endpoints para listar, buscar e criar itens usando uma coleção em memória. Use uma estrutura de dados simples para armazenar os itens enquanto a aplicação estiver em execução.

#### Requisitos
O programa concluído deve:

- Criar um modelo Pydantic para representar um item com campos como `id`, `name` e `description`.
- Implementar `GET /items` para listar todos os itens.
- Implementar `GET /items/{item_id}` para retornar um item específico.
- Implementar `POST /items` para adicionar um novo item à coleção.
- Retornar `404` quando o item solicitado não existir.

### 🛠️ Adicionar validação e comportamento de API

#### Descrição
Refine a API com validação de entrada e comportamento mais robusto para que os dados enviados pelos clientes sejam tratados corretamente.

#### Requisitos
O programa concluído deve:

- Validar automaticamente os dados recebidos no corpo das requisições.
- Rejeitar payloads inválidos com erros apropriados do FastAPI.
- Definir um modelo de resposta consistente para os endpoints principais.
- Demonstrar um exemplo de requisição `POST` e sua resposta esperada.

#### Exemplo
```http
POST /items
Content-Type: application/json

{
  "name": "Notebook",
  "description": "A lightweight laptop for development"
}
```

```json
{
  "id": 3,
  "name": "Notebook",
  "description": "A lightweight laptop for development"
}
```