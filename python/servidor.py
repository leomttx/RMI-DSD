import Pyro4, sys, socket
from ListaDeChamada import ListaDeChamada

def pegarArgumentosDaLinhaDeComando():
    if(len(sys.argv) < 3):
        print("Uso: python3 ", sys.argv[0], " <professor> <disciplina> [data]")
        print("Exemplo: python3 ", sys.argv[0], " Lisiane \"Como ser uma menina baixinha\"")
        exit()
    return sys.argv[1], sys.argv[2], sys.argv[3] if(len(sys.argv) > 3) else None

def pegarIp():
    nome_do_host_local = socket.gethostname()
    ip_do_host_local = socket.gethostbyname(nome_do_host_local)
    return ip_do_host_local

def iniciarProcessoEmSegundoPlano(host):
    return Pyro4.Daemon(host = host)

def localizarServidorDeNomes():
    try:
        return Pyro4.locateNS()
    except Pyro4.errors.NamingError:
        print("Servidor de nomes não encontrado")
        return exit()

def transformarObjetoOriginalEmObjetoPyro(objeto):
    return daemon.register(objeto)

def registrarObjetoPyroNoServidorDeNomes(servidor_de_nomes, uri):
    servidor_de_nomes.register("lista-de-chamada", uri)

def rodarOProcesso():
    daemon.requestLoop()

# início do programa
professor, disciplina, data = pegarArgumentosDaLinhaDeComando()

daemon = iniciarProcessoEmSegundoPlano(pegarIp()) # cria um daemon do Pyro
objeto_original = ListaDeChamada(professor, disciplina, data)
uri = transformarObjetoOriginalEmObjetoPyro(objeto_original) # registra o objeto no daemon e retorna a URI
servidor_de_nomes = localizarServidorDeNomes() # localiza o servidor de nomes
registrarObjetoPyroNoServidorDeNomes(servidor_de_nomes, uri) # registra o objeto no servidor de nomes
print("✅ Servidor configurado ()\n✅ Chamada iniciada")
print("🌐 ", uri)
print("💡 Para parar o servidor, aperte Ctrl + C\n💡 Um registro da chamada será salvo no computador")
rodarOProcesso() # inicia o servidor

nome_do_arquivo = str("lista-de-chamada-" + objeto_original.verDisciplina() + "-" + objeto_original.verData().replace("/", "-") + ".txt")
with open(nome_do_arquivo, 'w') as arquivo:
            alunos = objeto_original.verAlunos()
            arquivo.write(str("[ LISTA DE CHAMADA DA DISCIPLINA " + objeto_original.verDisciplina() + ", MINISTRADA POR " + objeto_original.verProfessor() + " — DIA " + objeto_original.verData() + "]\n"))
            for index, aluno in enumerate(alunos):
                arquivo.write("\t — Aluno #" + str(index) + ": " + aluno + "\n")
print("✅ Registro salvo (", nome_do_arquivo, ")")