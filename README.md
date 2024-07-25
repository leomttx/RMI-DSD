# rmi-dsd

Projeto que *implementa um objeto descrito em Python* e o *disponibiliza para ser acessado em rede*.


## Sobre esta documentação

Estas instruções permitem que você configure o projeto em seu computador para desenvolvimento e testes.


## Pré-requisitos

Para baixar, compilar e executar o projeto no seu computador, ele deve ter:

- [Kit de desenvolvimento Python](https://www.python.org/downloads/) (versão 3 ou superior)

## Rodando o projeto

💡 Os comandos a seguir foram testados usando um ambiente baseado em *Debian/GNU Linux*, com instalação do *Python versão 3.10.13* e *bash versão 5.0.17*. Os comandos descritos podem não ser compatíveis com outros sistemas operacionais. Sinta-se livre para sugerir comandos compatíveis com o seu sistema operacional.

Todos os comandos abaixo pressupoem que com o terminal localizado na pasta [python/](python/).

Para rodar o projeto localmente, siga os seguintes passos:

1. Instale as dependências:

```bash
pip install Pyro4
```


2. Obtenha o endereço IP da máquina onde se deseja rodar o servidor:

```bash
python3 obter-ip.py
```

💡 Copie a saída do comando. Será necessário colar essa informação no prompt do próximo passo.

3. Rode o servidor de nomes do Pyro, informando (1) o IP que foi obtido com o comando anterior:

```bash
python -m Pyro4.naming -n << ip-obtido-com-o-comando-anterior >>
```


4. Em um novo terminal, rodar o programa `servidor.py`, informando (1) o nome do professor, (2) o nome da disciplina e, *opcionalmente*, (3) uma data:

```bash
python3 servidor.py << nome-do-professor >> << nome-da-disciplina >> << data >>
```

💡 `<< data >>` é opcional. Se você desejar informá-la, certifique de colocá-la no formato `dd/mm/yyyy`.


5. Em um novo terminal, rodar o programa `cliente.py` informando (1) o nome do aluno:

```bash
python cliente.py << nome-do-aluno >>
```

## Licença

Este projeto é licenciado sob os termos da licença [GPL 3](LICENSE).
