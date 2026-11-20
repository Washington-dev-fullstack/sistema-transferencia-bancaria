# Sistema de transferência bancária

Um sistema de transferência bancária feito em Python, no terminal. Professor e estudante transferem dinheiro um para o outro, e o saldo é conferido a cada operação.

## Como rodar

```bash
python main.py
```

## O que o código mostra

- Uma classe `Conta`, com titular e saldo, e os métodos `informacao()` e `transferir()`.
- Dois objetos da mesma classe (o professor e o estudante) trocando valores.
- Validação: a transferência só acontece se houver saldo, e um `try/except` recusa o que não for número.
- Um laço para fazer várias transferências seguidas.

## Exemplo

```text
---Sistema de Transferência Bancária---

Antes de começar, informe quem você é de acordo com a tabela a baixo:
 p - professor
 e - estudante
Digite a letra que corresponde com voce: p

Voce tem o saldo de: 19822
Insira o valor que voce deseja transferir para o Estudante: 500
Transferência de R$500.0 concluída!


Deseja realizar outra transferencia ? (s/n)
n
Obrigado por usar nosso sistema bancario
```

## Sobre

Exercício de programação orientada a objetos em Python (2025), de **Washington Gabriel** ([GitHub](https://github.com/Washington-dev-fullstack)).
