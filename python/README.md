# Lista de chamada

Projeto que *disponibiliza um objeto Python para ser acessado em rede* usando o protocolo `Pyro`, biblioteca [Pyro4](https://pyro4.readthedocs.io/en/stable/).

## Fluxo de funcionamento

O funcionamento do projeto é bastante simples. Os seguintes passos devem ser dados:

1. Instalar dependências;
1. Rodar servidor de nomes do Pyro;
1. Rodar o programa `servidor.py`, informando (1) o nome do professor, (2) o nome da disciplina e, *opcionalmente*, (3) uma data;
1. Rodar o programa `cliente.py` informando (1) o nome do aluno.

- O funcionamento do programa `cliente.py` depende que o programa `servidor.py` esteja em execução. Basicamente, o usuário pode registrar seu nome no objeto `ListaDeChamada` e obter uma espécie de relatório desta, que é um texto com uma leitura amigável.
- O arquivo `servidor.py` entra em loop até que o usuário suspenda a execução do daemon do Pyro pressionando Ctrl + C. A partir desse momento, o programa gera um arquivo `.txt`, com conteúdo idêntico ao relatório obtido pelo usuário no programa `cliente.py`.

**Abaixo, há instruções específicas para correta execução dos passos.**

### Ambiente de testes

Os comandos a seguir foram testados usando um ambiente baseado em Debian/GNU Linux, com instalação do Python versão 3.10.13 e bash versão 5.0.17. Os comandos descritos podem não ser compatíveis com outros sistemas operacionais.

#### Instalar dependências

```bash
pip install Pyro4
```

#### Rodar servidor de nomes do Pyro

```bash
python -m Pyro4.naming
```

#### Rodar progama servidor.py

```bash
python3 servidor.py << nome-do-professor >> << nome-da-disciplina >> << data >>
```

- Substitua `<< nome-do-professor >>` pelo nome do professor da disciplina para a qual se deseja realizar o registro da chamada.
- Substitua `<< nome-da-disciplina >>` pelo nome da disciplina para a qual se deseja realizar o registro da chamada.
- 💡 *Se os nomes forem composto, escrevê-los entre aspas*.
- Opcionalmente, substitua `<< data >>` por uma data no formato `dd/mm/yyyy`. Se este campo for deixado em branco, o programa assume a data do momento em que ele está em execução.

##### Exemplo

```bash
python3 servidor.py "Professor Fulano" "Disciplina do Professor Fulano" 12/12/2012
```

#### Rodar o programa `cliente.py`

```bash
python cliente.py << nome-do-aluno >>
```

- Substitua `<< nome-do-aluno >>` pelo nome do aluno que vai assinar o registro da chamada.
- 💡 *Se o nome for composto, escrevê-lo entre aspas*.

##### Exemplo

```bash
python cliente.py "Cicrano de Beltrano"
```