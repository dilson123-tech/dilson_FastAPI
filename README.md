📄 README.md
markdown
Copiar
Editar
# 📊 API de Soma com FastAPI

Este é um projeto simples desenvolvido com **FastAPI** para praticar o uso de requisições **POST com JSON**.  
Ele permite enviar dois números e retorna a soma como resposta.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic

---

## 📁 Estrutura

meu_projeto_solo/
│
├── main.py # Código principal da API
├── venv/ # Ambiente virtual
└── README.md # Documentação do projeto

yaml
Copiar
Editar

---

## ▶️ Como Rodar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/api-fastapi-json-post-soma.git
cd api-fastapi-json-post-soma

# 2. Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instale as dependências
pip install fastapi uvicorn

# 4. Rode o servidor local
uvicorn main:app --reload
🔄 Rota da API
POST /soma

Envia dois números e recebe a soma.

🔸 JSON de entrada:
json
Copiar
Editar
{
  "a": 30,
  "b": 20
}
🔸 Resposta esperada:
json
Copiar
Editar
{
  "resultado": 50
}
🧪 Testes
Você pode testar a API diretamente no navegador via Swagger:

http://127.0.0.1:8000/docs

Ou usar ferramentas como Thunder Client ou Postman.

💡 Objetivo
Este projeto faz parte do meu aprendizado prático com APIs usando Python e FastAPI.
Cada repositório representa uma etapa da minha evolução como desenvolvedor.

👨‍💻 Autor
Dilson Pereira
GitHub | LinkedIn

