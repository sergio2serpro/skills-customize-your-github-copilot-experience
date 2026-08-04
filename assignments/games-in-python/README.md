
# 📘 Assignment: Jogo da Forca

## 🎯 Objective

Construir um jogo da Forca em Python para praticar manipulacao de strings, loops, condicionais e entrada de dados do usuario. Ao final, o aluno deve controlar o fluxo completo da partida com condicoes claras de vitoria e derrota.

## 📝 Tasks

### 🛠️ Criar a base do jogo e escolher a palavra

#### Descricao
Implemente a estrutura inicial do jogo, incluindo uma lista de palavras e a selecao aleatoria da palavra secreta.

#### Requisitos
O programa concluido deve:

- Definir uma lista predefinida com pelo menos 5 palavras.
- Selecionar uma palavra aleatoriamente ao iniciar a partida.
- Criar uma estrutura para armazenar letras descobertas e palpites do jogador.
- Inicializar a quantidade de tentativas incorretas restantes.

### 🛠️ Implementar palpites, progresso e regras de fim de jogo

#### Descricao
Complete o loop principal para receber letras, atualizar o progresso e encerrar o jogo corretamente quando o jogador vencer ou perder.

#### Requisitos
O programa concluido deve:

- Aceitar um palpite de letra por rodada.
- Mostrar o progresso atual da palavra no formato _ _ _. 
- Reduzir tentativas apenas quando o palpite estiver incorreto.
- Encerrar com mensagem de vitoria quando a palavra for totalmente revelada.
- Encerrar com mensagem de derrota quando as tentativas chegarem a zero, exibindo a palavra secreta.