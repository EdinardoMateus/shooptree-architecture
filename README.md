# ShoopTree - Modernização Arquitetural

## Descrição
Projeto de modernização da plataforma de e-commerce ShoopTree, migrando do monolito para microsserviços.

## Arquitetura
- **Product Service**: Gerencia catálogo e publica eventos de compra.
- **Payment Service**: Processa pagamentos usando Strategy Pattern.
- **Notification Service**: Consome eventos e envia notificações.

## Como executar
```bash
docker-compose up --build