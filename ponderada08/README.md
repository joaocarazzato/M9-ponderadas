# Desafio 1BRC
Repositório se baseia na resolução do [desafio](https://1brc.dev) de processamento de um bilhão de linhas.

## Solução

A solução foi baseada na resolução já pública postada no repositório [principal](https://github.com/ifnesi/1brc/blob/main/calculateAveragePolars.py) do desafio utilizando a linguagem Python e a biblioteca [Polars](https://pola.rs). A solução foi criada e proposta pelo [Taufan](https://github.com/mtaufanr).

## Por que funciona de forma performática?

O Polars é uma das bibliotecas mais performáticas de Python para dataframes, inclusive muito mais performática do que o próprio pandas, mas por que disso? 

Além de ser feita em uma linguagem de baixo nível(Rust), permitindo que o Polars possa usar todos os núcleos do processador de forma paralela, a biblioteca também utiliza o Apache Arrow, disponibilizando interoperabilidade que evita o parte de serialização/deserialização dos dados, aumentando ainda mais a performance da biblioteca. Outro assunto importante para a performance do Polars, é a otimização de querys, que além de simples possuem uma forma de mapeamento para descobrir a forma mais performática de executar esse código.

Interessante mencionar que o método que utilizamos para leitura do csv no Polars(scan_csv), contribuiu para a performance que obtivemos em código. Enquanto os métodos tradicionais(como o read_csv) tiveram uma demora considerativa pela questão de armazenamento de cache em disco, o método que utilizamos armazena tudo em memória, agilizando ainda mais esse processo.

O código utilizado pode ser encontrado em ```src/calculateAveragePolars.py ``` onde temos cada linha de código comentada. Além disso, podemos gerar o arquivo de 1 bilhão de linhas rodando o código localizado em ```src/createMeasurements.py```.