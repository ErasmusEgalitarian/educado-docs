# WIKI - Conceptual Overview of the Hierarchical Classification Tool

---

## 1. Visão Geral

Este projeto é um conceito inovador para classificação hierárquica de requisitos textuais complexos usando técnicas de processamento de linguagem natural (NLP) e aprendizado de máquina. A ferramenta propõe uma estrutura multinível de análise, combinando clustering em níveis primário, secundário e terciário, apoiada por um assistente inteligente baseado em modelos de linguagem (LLM) para refinamento iterativo e enriquecimento dos resultados.

O projeto surgiu da necessidade do **Educado**, uma plataforma dedicada a prover conteúdo educativo para catadores e cooperativas, que enfrenta o desafio do **grande volume de documentação e requisitos técnicos e sociais**, tornando manual a organização e interpretação dos documentos algo custoso e sujeito a erros.

A solução busca facilitar a organização e interpretação desses grandes volumes de documentos e requisitos, potencializando a análise por meio da automação e inteligência artificial, promovendo decisões mais rápidas e confiáveis no desenvolvimento e gestão da plataforma.

---

## 2. Motivação

A classificação de requisitos textuais em projetos complexos enfrenta desafios significativos devido à natureza heterogênea, ambígua e volumosa dos dados. Métodos tradicionais, como classificação manual ou técnicas simples de agrupamento, tornam-se insuficientes diante de grandes volumes e múltiplos níveis de hierarquia.

Neste contexto, a aplicação de técnicas de NLP avançadas e clustering multinível permite uma organização mais granular e intuitiva dos requisitos, facilitando a compreensão, priorização e tomada de decisão.

Além disso, a integração de modelos de linguagem (LLMs) como assistentes inteligentes para sugerir refinamentos, ajustar stopwords e gerar labels automáticas eleva a qualidade e eficiência do processo, reduzindo esforço manual e aumentando a precisão.

Esta motivação está diretamente ligada às necessidades do projeto Educado, que requer um sistema capaz de lidar com grandes volumes e complexidades textuais para suportar sua missão educacional e social.

---

## 3. Principais Características

- **Classificação Multinível:** Organização dos requisitos em níveis hierárquicos primário, secundário e terciário, proporcionando granularidade na análise.

- **Assistente Inteligente para Stopwords:** Uso de modelos de linguagem para refinar iterativamente a lista de palavras irrelevantes (stopwords), melhorando a qualidade da tokenização.

- **Geração Automática de Labels:** Criação de rótulos significativos para clusters por meio de LLMs, facilitando a interpretação dos grupos.

- **Auditoria de Clusters:** Detecção e sugestão de merge ou split de clusters para otimizar a classificação, com suporte de inteligência artificial.

- **Geração de Resumos (Abstracts):** Produção automática de resumos para os clusters, sintetizando os temas principais para fácil compreensão.

- **Relatórios de Performance:** Ferramentas para avaliação da qualidade da classificação e visualização dos resultados.

---

## 4. Arquitetura Conceitual

A arquitetura do sistema segue os princípios da Clean Architecture, garantindo modularidade, testabilidade e facilidade de manutenção. Ela é dividida em quatro camadas principais:

- **Domínio:** Entidades e interfaces que definem as regras de negócio e contratos para os serviços, incluindo as portas para carregamento de dados, limpeza, tokenização, clustering e interação com LLM.

- **Aplicação (Use Cases):** Orquestração dos fluxos principais, como classificação, refinamento de stopwords, geração de labels, auditoria e geração de hierarquias.

- **Infraestrutura:** Implementações concretas das portas, como repositórios para arquivos Excel e PDF, serviços de limpeza de dados, tokenização, clustering KMeans, serviços LLM integrados e geração de relatórios.

- **Interface:** Camada de apresentação, atualmente via CLI, que oferece menus interativos para executar as funcionalidades e receber parâmetros do usuário.

O sistema integra-se com APIs externas, principalmente a OpenAI, para utilização dos modelos de linguagem que auxiliam na geração de labels, auditoria e refinamento inteligente.

Essa arquitetura permite a fácil substituição e extensão de componentes, garantindo escalabilidade para futuras melhorias e adaptações.

---

## 5. Como Usar a Ferramenta (Concept)

Por ser um conceito em desenvolvimento, o uso da ferramenta atualmente ocorre via interface de linha de comando (CLI) com menus interativos que permitem:

- **Classificar documentos** (Excel, PDF ou pastas) em múltiplos níveis hierárquicos.  
- **Gerenciar stopwords** dinamicamente, com auxílio do assistente LLM para refinamento iterativo.  
- **Gerar labels para clusters** automaticamente usando modelos de linguagem.  
- **Auditar clusters** com sugestões para merge ou split, promovendo melhor organização.  
- **Gerar resumos (abstracts)** para facilitar a compreensão dos clusters.  
- **Visualizar relatórios de performance** para análise da qualidade da classificação.

O usuário é guiado por menus que solicitam caminhos para arquivos, parâmetros de clusterização e opções de refinamento, facilitando o fluxo sem necessidade de conhecimento técnico aprofundado.

---

## 6. Estrutura dos Arquivos de Entrada e Saída

**Arquivos de Entrada:**

- Documentos Excel (.xlsx) com planilhas contendo os requisitos textuais.  
- Documentos PDF (.pdf) para extração textual.  
- Diretórios contendo múltiplos arquivos Excel ou PDF para processamento em lote.

**Arquivos Intermediários:**

- `freq_words.txt`: lista de palavras frequentes extraídas após limpeza e tokenização, usada para auxiliar refinamento de stopwords.  
- `all_clustered.xlsx`: arquivo com resultados da clusterização contendo IDs, textos tokenizados e números dos clusters.  
- `labels.json`: JSON com labels gerados para os clusters por LLM.  
- `id_source_mapping.csv`: mapeia IDs para nomes originais dos documentos.

**Arquivos de Saída:**

- `merged_clusters.xlsx`: consolida hierarquias com labels em vários níveis e nomes dos documentos.  
- `abstracts.xlsx`: resumos automáticos para clusters, facilitando análise temática.

Exemplo de colunas importantes nos arquivos Excel:

| Coluna         | Descrição                                 |
|----------------|-------------------------------------------|
| ID             | Identificador único da linha/documento    |
| processed_text | Texto limpo e tokenizado                   |
| joined_tokens  | Tokens concatenados para vetorização      |
| cluster        | Índice do cluster atribuído                |
| Primary_label  | Label gerado para cluster primário         |
| Secondary_label| Label gerado para cluster secundário       |
| Tertiary_label | Label gerado para cluster terciário        |
| DocumentName   | Nome original do arquivo/documento         |
| Abstract       | Resumo gerado automaticamente pelo LLM    |

---

## 7. Considerações Técnicas e Limitações

- A utilização de modelos de linguagem (LLMs) implica em custos associados às requisições API, que devem ser considerados no planejamento.  
- A qualidade dos resultados depende da qualidade dos dados de entrada; documentos mal formatados podem prejudicar a classificação.  
- Processos de refinamento iterativo podem demandar tempo computacional significativo para grandes volumes.  
- O sistema está em fase conceitual e requer validação contínua para assegurar robustez e escalabilidade.  
- A complexidade da hierarquia pode impactar a interpretação humana, exigindo cuidado na análise dos resultados.  
- Futuras melhorias podem incluir interfaces gráficas, automação do pipeline, suporte a outros idiomas e **servidores de teste dedicados para a API** visando maior segurança e controle do uso.

---

## 8. Resultados

- **Database:** [Database](https://erasmusegalitarian.github.io/educado-docs/database/database_index/)

### Suggested Searches

Para facilitar sua navegação, sugerimos as seguintes buscas na wiki:

- **Search "financial education"**  
  Explore documentos relacionados a educação financeira, incluindo plataformas digitais, cursos e relatórios.

- **Search "cybersecurity"**  
  Encontre materiais sobre segurança em desenvolvimento de software, ataques cibernéticos e análise de vulnerabilidades.

- **Search "waste pickers"**  
  Descubra conteúdos focados na inclusão social e educação para catadores de lixo por meio de tecnologias móveis.

---
## 9. Contato e Suporte

Este projeto está em desenvolvimento e aberto a colaborações e sugestões. Para entrar em contato, contribuir com código ou relatar problemas, utilize os seguintes canais:

- **Repositório GitHub:** [https://github.com/LucasGSAntunes/requirements_educado_2024](https://github.com/LucasGSAntunes/requirements_educado_2024)  
- **E-mail:** lgabrielantunes@gmail.com  
- **Comunidade e Discussões:** Entre em contato para mais informações.

Sua participação é muito bem-vinda para aprimorar esta ferramenta e torná-la uma solução robusta para classificação hierárquica baseada em NLP e IA.

---

## Revision History

| Date       | Version | Changes                         | Authors                                                                                          |
| ---------- | ------- | ------------------------------- | ------------------------------------------------------------------------------------------------ |
| 2025-03-28 | 0.1     | Document creation               | [Cainã Freitas](https://github.com/freitasc), [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 2025-04-18 | 0.2     | Update home page                | [Mateus Vieira](https://github.com/matix0), [Lucas Antunes](https://github.com/LucasGSAntunes)   |
| 2025-05-14 | 0.3     | Add wiki ref                    | [Mateus Vieira](https://github.com/matix0), [Lucas Antunes](https://github.com/LucasGSAntunes)   |
| 2025-06-02 | 0.4     | Add new PDF classification tool | [Lucas Antunes](https://github.com/LucasGSAntunes)                                               |


[← Back to Main Page](index.md)
