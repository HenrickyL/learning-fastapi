# Delivery Backend

## Dependencias

1. FastAPI 
2. Uvicorn - gerenciamento assincrono
3. SqlAlchemy - criar banco e modelagem
4. PassLib[bcrypt] -  criptografia de senhas
5. python-jose[criptography] - tokens JWT
6. python-dotenv - Gerenciar variaveis de ambiente
   * python-multipart - dependencia

* `pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart`

## Run

* `uvicorn main:app --reload`

---
ref: [Curso de FastAPI - Rest API com Python](https://www.youtube.com/playlist?list=PLpdAy0tYrnKy3TvpCT-x7kGqMQ5grk1Xq)