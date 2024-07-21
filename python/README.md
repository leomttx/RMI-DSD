## Instalar dependências

```bash
pip install Pyro4
```

## Rodar servidor de nomes

```bash
python -m Pyro4.naming
```

## Rodar servidor usando o servidor de nomes

```bash
python3 servidor.py <<NOME-DO-PROFESSOR>> <<DISCIPLINA>> <<opcional:DATA>>
```

## Rodar cliente usando o servidor de nomes

```bash
python cliente.py << NOME-DO-ALUNO >>
```