# Bot-Discord-Ticket
 
![Logo do Meu Projeto](https://cdn.discordapp.com/attachments/1175249252771958844/1192685799838326874/Bot_Ticket.png?ex=65a9fa35&is=65978535&hm=2d8aca8c4e19c616370af8d074aeefb4d8d65030b0a70cdfc0dfcabaae2abd24&)

# Discord Ticket Bot

## Descrição

Este projeto implementa um bot Discord em Python usando a biblioteca discord.py. O bot fornece um sistema de tickets para atendimento aos jogadores em um servidor Discord. Ele inclui funcionalidades como fechamento de tickets, criação de tickets por meio de um menu suspenso e uma configuração inicial do bot.

## Funcionalidades Principais

### Fecharticket Cog

- Comando slash (`/fecharticket`) para fechar um atendimento atual.
- Apenas usuários com um cargo específico ou o próprio usuário que abriu o ticket podem usar o comando.

### Dropdown Cog

- Implementação de um menu suspenso com opções como "Compras", "Denúncias", "Atendimento" e "Pagamento Freelancer".
- Criação de tickets ao selecionar uma opção no menu suspenso.

### Setup Cog

- Comando slash (`/setup`) para inicializar o bot.
- Exibição de uma mensagem de apresentação do sistema de tickets e um embed com informações e um botão dropdown.

## Como Usar

1. Clone o repositório.
2. Configure as variáveis de ambiente necessárias.
3. Execute o bot com o Python.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests.
