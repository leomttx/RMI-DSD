from datetime import datetime
import Pyro4

@Pyro4.expose
class ListaDeChamada():
    def __init__(self, professor, disciplina, data = None):
        self.alunos = []
        self.professor = professor
        self.disciplina = disciplina
        if not data:
            self.data = datetime.now()
        else:
            self.data = datetime.strptime(data, "%d/%m/%Y") # TODO: tratar ValueError (quando a string não está no formato correto)

    def adicionarAluno(self, nome_do_aluno):
        self.alunos.append(nome_do_aluno)

    def verAlunos(self):
        return self.alunos

    def verDisciplina(self):
        return self.disciplina

    def verProfessor(self):
        return self.professor

    def verData(self):
        return self.data.strftime("%d/%m/%Y")