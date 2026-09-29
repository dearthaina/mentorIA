from fastapi import FastAPI

app = FastAPI(
    title="MentorIA API",
    description="API do Projeto Integrador MentorIA",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "mensagem": "API do MentorIA funcionando!"
    }