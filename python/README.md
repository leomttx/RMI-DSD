## Instalar dependências

```bash
pip install Pyro4
```

## Rodar servidor

```bash
python3 servidor.py
```

## Rodar cliente

```bash
python3 cliente.py <<URI>> <<NOME>>
```

- substitua `<<URI>>` pela string obtida ao rodar o servidor. O formato da string é: `PYRO:<<referência ao objeto>>@<<endereço IP da máquina onde está o objeto>>:<<número da porta onde está o objeto>>`

- substitua `<<NOME>>` pelo seu nome