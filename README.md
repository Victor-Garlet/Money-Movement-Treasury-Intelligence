# Money Movement & Treasury Intelligence

Projeto de portfolio para desenvolver competencias de Python, SQL, APIs, dbt, versionamento com Git/GitHub e analytics aplicado ao setor financeiro.

O objetivo nao e criar mais um dashboard generico. Este projeto simula a camada analitica que uma fintech, banco digital ou banco tradicional usaria para entender:

- quao confiavel e a infraestrutura que move dinheiro;
- como pagamentos, APIs e parceiros afetam experiencia do cliente;
- como juros, cambio e liquidez afetam custo financeiro;
- como transformar dados publicos em metricas, alertas e decisoes de negocio.

## 1. Visao Do Produto

### Problema

Empresas como Wise, Revolut, Adyen, Mollie, Bank of Ireland, AIB, ING e JPMorgan dependem de sistemas complexos para mover dinheiro, manter liquidez, controlar risco e oferecer uma boa experiencia ao cliente.

Mesmo quando a taxa de sucesso parece alta, pequenos problemas em escala podem gerar impacto relevante:

- pagamentos atrasados ou falhados;
- aumento de tickets de suporte;
- perda de conversao;
- maior necessidade de buffer de liquidez;
- custo financeiro por dinheiro parado;
- risco operacional e regulatorio;
- decisoes ruins por falta de dados confiaveis.

### Solucao

Construir uma plataforma analitica modular que ingere dados publicos vivos, transforma esses dados em modelos analiticos e gera dashboards, metricas e analises executivas sobre money movement, payment reliability e treasury/funding risk.

### Publico-Alvo

- recrutadores e hiring managers de fintechs/bancos;
- times de product analytics;
- times de treasury, liquidity e finance;
- times de risk, compliance e operations;
- profissionais que querem entender dados financeiros publicos.

## 2. Perguntas De Negocio

### Payment Reliability

- Quais bancos/provedores de Open Banking apresentam maior indisponibilidade?
- A falha e tecnica ou de negocio?
- Existem padroes por mes, horario, endpoint ou tipo de API?
- O que uma taxa de falha pequena representa em volume absoluto?
- Qual seria o impacto estimado em clientes, suporte e receita?

### Instant Payments & Open Finance

- Como a adocao do Pix no Brasil compara com Open Banking/Open Finance no UK e Brasil?
- O crescimento esta vindo de volume, valor, usuarios ou chamadas de API?
- O ecossistema esta ficando mais resiliente ou mais complexo?
- Quais instituicoes lideram em uso, disponibilidade e maturidade?

### Treasury & Funding

- Como a curva de juros GBP/EUR/USD mudou nos ultimos meses?
- O que acontece com uma fintech que mantem bilhoes em saldos de clientes quando juros sobem ou caem?
- Qual o impacto estimado de um choque de +1% ou -1% nas taxas?
- Quanto custa manter liquidez imediata em caixa versus aplicar em instrumentos curtos?
- Como cambio e juros afetam uma empresa que move dinheiro entre moedas?

### Risk, KYB & Compliance

- Uma contraparte financeira esta registrada e identificavel por LEI?
- Existem sinais publicos de risco regulatorio ou sancoes?
- Como combinar Companies House, GLEIF e OpenSanctions para due diligence basica?

## 3. Fontes De Dados

### Fase Inicial

| Fonte | Uso | Frequencia Esperada |
|---|---|---|
| UK Open Banking API Performance | disponibilidade, chamadas bem-sucedidas/falhadas, performance por banco | mensal |
| ECB Data Portal | cambio, juros, estatisticas monetarias e financeiras da zona do euro | diaria/mensal |
| Bank of England Yield Curves | curva de juros GBP e analises de funding | diaria |
| Banco Central do Brasil Pix | estatisticas de pagamentos instantaneos | mensal |
| Open Finance Brasil | chamadas de APIs, consentimentos, rankings e indicadores | recorrente |

### Fase Avancada

| Fonte | Uso |
|---|---|
| Companies House API | dados de empresas UK, filings, status e diretores |
| GLEIF LEI API | identificacao global de entidades financeiras |
| OpenSanctions | sancoes, PEPs e watchlists |
| FRED | indicadores macro dos EUA e contexto global |
| BIS Statistics | estatisticas bancarias internacionais |

## 4. Stack Tecnica

### Essencial

- Python: extracao, limpeza, automacao e analise.
- SQL: modelagem e queries analiticas.
- DuckDB: banco local simples para comecar.
- dbt: transformacoes, testes e documentacao dos modelos.
- Git/GitHub: versionamento, historico e portfolio publico.
- Jupyter: exploracao inicial e aprendizado.

### Depois

- PostgreSQL: banco relacional mais proximo de ambiente real.
- Docker: reproducibilidade.
- GitHub Actions: automacao de testes e pipelines.
- Streamlit, Evidence.dev, Superset ou Power BI: dashboard.
- Great Expectations ou dbt tests: qualidade de dados.
- Airflow, Dagster ou Prefect: orquestracao.

## 5. Arquitetura-Alvo

```text
public APIs / downloads
        |
        v
src/extract/
        |
        v
data/raw/
        |
        v
src/load/
        |
        v
DuckDB or Postgres
        |
        v
dbt staging models
        |
        v
dbt intermediate models
        |
        v
dbt marts
        |
        v
dashboards / notebooks / reports
```

## 6. Estrutura Do Repositorio

```text
money-movement-treasury-intelligence/
  README.md
  data/
    raw/
    processed/
  notebooks/
    01_explore_open_banking.ipynb
    02_explore_yield_curves.ipynb
    03_pix_vs_open_finance.ipynb
  src/
    extract/
    transform/
    load/
    utils/
  dbt/
    models/
      staging/
      intermediate/
      marts/
    tests/
  sql/
  dashboards/
  docs/
    glossary.md
    metric_definitions.md
    learning_log.md
    data_sources.md
  tests/
```

## 7. Roadmap De Desenvolvimento

### Fase 0: Setup E Fundamentos

Objetivo: preparar ambiente e aprender versionamento basico.

Entregaveis:

- criar repositorio no GitHub;
- configurar ambiente Python;
- criar `README.md`;
- criar `.gitignore`;
- fazer primeiros commits;
- aprender comandos basicos: `git status`, `git add`, `git commit`, `git push`, `git log`;
- criar um arquivo `docs/learning_log.md` para registrar o que foi aprendido.

Conceitos para estudar:

- o que e Git;
- diferenca entre Git e GitHub;
- branch, commit, remote, push e pull;
- ambiente virtual Python;
- estrutura basica de projeto.

### Fase 1: Primeiro Pipeline De API

Objetivo: consumir uma fonte publica real com Python.

Fonte sugerida: UK Open Banking API Performance ou ECB Data Portal.

Entregaveis:

- script Python para baixar dados;
- salvar resposta bruta em `data/raw/`;
- criar notebook exploratorio;
- documentar endpoint, campos e limitacoes;
- criar primeira analise simples.

Conceitos para estudar:

- HTTP;
- APIs REST;
- `requests`;
- status codes;
- JSON, CSV e XML;
- tratamento de erro;
- idempotencia;
- rate limits;
- logs basicos.

### Fase 2: SQL E Modelagem Local

Objetivo: carregar dados em DuckDB e consultar com SQL.

Entregaveis:

- criar banco DuckDB local;
- carregar dados brutos;
- criar queries com filtros, joins, agregacoes e CTEs;
- criar metricas iniciais:
  - total de chamadas;
  - taxa de sucesso;
  - taxa de falha;
  - ranking de provedores;
  - variacao mensal.

Conceitos para estudar:

- SELECT, WHERE, GROUP BY, HAVING;
- CTEs;
- window functions;
- tipos de joins;
- chaves primarias e estrangeiras;
- fatos e dimensoes;
- granularidade de dados.

### Fase 3: Payment Reliability MVP

Objetivo: transformar dados de Open Banking em analise de confiabilidade.

Entregaveis:

- modelo `fct_api_performance`;
- modelo `dim_provider`;
- modelo `mart_payment_reliability`;
- ranking mensal de disponibilidade;
- analise de falhas tecnicas vs falhas de negocio;
- primeiro dashboard ou relatorio.

Metricas:

- API availability;
- successful API calls;
- failed API calls;
- failure rate;
- weighted vs unweighted availability;
- estimated impacted payments.

Conceitos para estudar:

- SLI;
- SLO;
- error budget;
- disponibilidade;
- latencia;
- incidentes;
- retry;
- timeout;
- falhas tecnicas vs falhas funcionais.

### Fase 4: Introducao Ao dbt

Objetivo: mover transformacoes SQL para dbt.

Entregaveis:

- inicializar projeto dbt;
- criar modelos staging;
- criar modelos marts;
- adicionar testes:
  - not null;
  - unique;
  - accepted values;
  - relationships;
- gerar documentacao dbt.

Conceitos para estudar:

- ELT;
- staging, intermediate e marts;
- lineage;
- data quality;
- data contracts;
- incremental models;
- seeds;
- snapshots.

### Fase 5: Treasury & Funding MVP

Objetivo: analisar juros, curvas e impacto em liquidez.

Fontes sugeridas:

- Bank of England Yield Curves;
- ECB Data Portal;
- FRED, opcional.

Entregaveis:

- extrair curva de juros GBP;
- extrair taxas/cambio EUR;
- criar tabela de curvas por data e prazo;
- criar simulador simples de choque de juros;
- calcular impacto estimado em saldos hipoteticos.

Metricas:

- yield por prazo;
- inclinacao da curva;
- mudanca diaria/semanal/mensal;
- custo de liquidez;
- interest income estimado;
- impacto de choque de +100 bps e -100 bps.

Conceitos para estudar:

- taxa de juros;
- yield curve;
- basis points;
- duration;
- net interest income;
- net interest margin;
- funding;
- liquidity buffer;
- asset liability management;
- IRRBB;
- cash management.

### Fase 6: Conexao Entre Payments E Treasury

Objetivo: mostrar que atrasos e falhas de pagamento afetam liquidez e custo financeiro.

Entregaveis:

- criar dados sinteticos de transacoes;
- simular settlement esperado vs settlement atrasado;
- estimar buffer adicional de liquidez;
- estimar custo/oportunidade desse buffer;
- criar analise executiva.

Exemplo de insight desejado:

```text
Quando a confiabilidade de um parceiro cai, pagamentos demoram mais para liquidar.
Esse atraso exige maior buffer de liquidez em determinada moeda.
Esse buffer tem custo financeiro ou custo de oportunidade, especialmente quando juros mudam.
```

Conceitos para estudar:

- settlement;
- clearing;
- reconciliation;
- liquidity coverage;
- operational risk;
- payment rails;
- FX exposure;
- treasury operations.

### Fase 7: Open Finance Brasil E Pix

Objetivo: comparar maturidade de pagamentos instantaneos e Open Finance.

Entregaveis:

- extrair dados do Pix;
- extrair indicadores do Open Finance Brasil;
- comparar crescimento, volume e uso;
- criar visualizacoes;
- escrever uma analise comparativa.

Perguntas:

- Por que o Pix escalou tao rapido?
- O que UK/Europa pode aprender com o Brasil?
- O que o Brasil pode aprender com Open Banking UK?
- Como infraestrutura regulatoria afeta produto?

Conceitos para estudar:

- pagamentos instantaneos;
- open banking;
- open finance;
- consentimento;
- iniciacao de pagamento;
- API padronizada;
- regulacao e interoperabilidade.

### Fase 8: KYB, LEI E Risco De Contraparte

Objetivo: adicionar camada de identidade institucional e compliance.

Fontes:

- Companies House;
- GLEIF;
- OpenSanctions.

Entregaveis:

- buscar empresas financeiras no Companies House;
- enriquecer entidades com LEI;
- verificar presenca em listas de sancoes;
- criar score simples de completude/risco;
- documentar limitacoes.

Conceitos para estudar:

- KYC;
- KYB;
- AML;
- sanctions screening;
- PEP;
- LEI;
- BIC;
- beneficial ownership;
- due diligence.

### Fase 9: Dashboard Publico

Objetivo: transformar modelos em produto visual.

Entregaveis:

- dashboard de Payment Reliability;
- dashboard de Treasury/Funding;
- dashboard de Pix/Open Finance;
- pagina de metodologia;
- screenshots no README;
- deploy publico, se possivel.

Ferramentas possiveis:

- Streamlit;
- Evidence.dev;
- Power BI;
- Tableau Public;
- Apache Superset.

### Fase 10: Automacao E Qualidade

Objetivo: aproximar o projeto de um ambiente profissional.

Entregaveis:

- GitHub Actions para rodar testes;
- pipeline de atualizacao;
- validacoes de dados;
- logs;
- alertas simples;
- documentacao de incidentes de dados.

Conceitos para estudar:

- CI/CD;
- data freshness;
- observabilidade;
- testes automatizados;
- scheduling;
- data quality;
- reproducibilidade.

## 8. Definicoes De Metricas

### API Success Rate

```text
successful_api_calls / total_api_calls
```

### API Failure Rate

```text
failed_api_calls / total_api_calls
```

### Estimated Impacted Payments

```text
failed_payment_related_calls * assumed_payment_conversion_factor
```

### Estimated Support Cost

```text
estimated_impacted_customers * support_contact_rate * average_support_cost
```

### Interest Income Estimate

```text
average_balance * annual_interest_rate
```

### Shock Impact

```text
average_balance * interest_rate_shock
```

Exemplo:

```text
GBP 10 billion * 1% = GBP 100 million annualized impact
```

## 9. Trilha De Aprendizado

### Python

- sintaxe basica;
- funcoes;
- ambientes virtuais;
- `requests`;
- `pandas`;
- tratamento de erros;
- logging;
- organizacao em modulos;
- testes com `pytest`.

### SQL

- SELECT e filtros;
- joins;
- agregacoes;
- CTEs;
- window functions;
- modelagem dimensional;
- otimizacao basica;
- qualidade de dados.

### dbt

- modelos;
- sources;
- refs;
- tests;
- docs;
- seeds;
- incremental models;
- marts;
- lineage.

### Financas

- pagamentos;
- Open Banking;
- Pix;
- settlement;
- liquidez;
- funding;
- cambio;
- juros;
- curva de juros;
- net interest income;
- risk and compliance.

### Engenharia De Dados

- APIs;
- ETL vs ELT;
- dados brutos vs dados tratados;
- orquestracao;
- CI/CD;
- Docker;
- observabilidade;
- contratos de dados.

### Git/GitHub

- commits pequenos;
- mensagens claras;
- branches;
- pull requests;
- issues;
- releases;
- README profissional;
- GitHub Actions.

## 10. Plano De Conteudo Para LinkedIn

Cada fase deve gerar um post curto.

Ideias:

1. Por que estou construindo um projeto de Money Movement Analytics.
2. O que aprendi consumindo minha primeira API financeira publica.
3. Como medir confiabilidade em Open Banking.
4. Por que 0.6% de falha pode ser enorme em escala.
5. Como usei SQL para criar metricas de payment reliability.
6. O que e curva de juros e por que fintechs se importam.
7. Como um choque de 1% nos juros pode afetar milhoes em receita.
8. Pix vs Open Banking: diferencas de infraestrutura e adocao.
9. Como dbt melhora qualidade e rastreabilidade dos dados.
10. O que aprendi sobre analytics para fintechs e bancos.

## 11. Criterios De Sucesso

O projeto sera considerado bem-sucedido quando tiver:

- pelo menos 3 fontes publicas automatizadas;
- modelos SQL/dbt documentados;
- testes de qualidade de dados;
- dashboard ou relatorio publico;
- README com arquitetura e metodologia;
- analises que conectam dados a decisoes de negocio;
- posts no LinkedIn mostrando evolucao;
- historico de commits consistente no GitHub.

## 12. Principio Do Projeto

Este projeto nao deve tentar parecer maior do que e. A forca dele esta em crescer de forma iterativa, com aprendizado documentado e decisoes tecnicas claras.

Cada entrega deve responder:

- qual problema estou resolvendo?
- que dado usei?
- como transformei esse dado?
- que metrica criei?
- qual decisao de negocio essa metrica poderia apoiar?
- o que aprendi tecnicamente?

## 13. Proxima Entrega

Primeiro objetivo pratico:

1. Criar ambiente Python.
2. Criar estrutura de pastas.
3. Fazer primeiro commit.
4. Escolher a primeira fonte de dados.
5. Baixar os primeiros dados via Python.
6. Criar primeira query SQL em DuckDB.
7. Escrever o primeiro post explicando o projeto.
