from locust import HttpUser, TaskSet, task, between
from main import *  # Importa la función qa desde tu código

class UserBehavior(TaskSet):
    def on_start(self):
        self.chat_history = []

    @task
    def ask_question(self):
        query = "Pregunta: "  # Aquí puedes definir una lista de preguntas si lo deseas
        result = qa({"question": query, "chat_history": self.chat_history})
        self.chat_history.append((query, result["answer"]))

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Tiempo entre solicitudes (ajusta según tus necesidades)
