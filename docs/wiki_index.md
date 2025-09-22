# WIKI - Conceptual Overview of the Hierarchical Classification Tool

---

## 1. Overview

This project is an innovative concept for the hierarchical classification of complex textual requirements using Natural Language Processing (NLP) and machine learning techniques. The tool proposes a multi-level analysis structure, combining clustering at primary, secondary, and tertiary levels, supported by an intelligent assistant based on language models (LLMs) for iterative refinement and enriched results.

The project arose from the needs of **Educado**, a platform dedicated to providing educational content for waste pickers and cooperatives, which faces the challenge of a **large volume of technical and social documentation and requirements**—making manual organization and interpretation costly and error-prone.

The solution aims to facilitate the organization and interpretation of these large volumes of documents and requirements, enhancing analysis through automation and artificial intelligence, and enabling faster and more reliable decision-making in the development and management of the platform.

---

## 2. Motivation

The classification of textual requirements in complex projects faces significant challenges due to the heterogeneous, ambiguous, and voluminous nature of the data. Traditional methods, such as manual classification or simple grouping techniques, become insufficient when dealing with large volumes and multiple levels of hierarchy.

In this context, the application of advanced NLP techniques and multi-level clustering allows for more granular and intuitive organization of requirements, facilitating understanding, prioritization, and decision-making.

Moreover, the integration of language models (LLMs) as intelligent assistants to suggest refinements, adjust stopwords, and generate automatic labels increases the quality and efficiency of the process, reducing manual effort and increasing accuracy.

This motivation is directly linked to the needs of the Educado project, which requires a system capable of handling large volumes and textual complexities to support its educational and social mission.

---

## 3. Main Features

* **Multi-level Classification:** Organizes requirements into primary, secondary, and tertiary hierarchical levels, providing analysis granularity.

* **Intelligent Stopwords Assistant:** Uses language models to iteratively refine the list of irrelevant words (stopwords), improving tokenization quality.

* **Automatic Label Generation:** Creates meaningful labels for clusters through LLMs, facilitating group interpretation.

* **Cluster Auditing:** Detects and suggests merging or splitting clusters to optimize classification, with AI support.

* **Abstract Generation:** Automatically produces summaries for clusters, synthesizing main themes for easy understanding.

* **Performance Reports:** Tools for evaluating classification quality and visualizing results.

---

## 4. Conceptual Architecture

The system architecture follows Clean Architecture principles, ensuring modularity, testability, and ease of maintenance. It is divided into four main layers:

* **Domain:** Entities and interfaces that define business rules and service contracts, including ports for data loading, cleaning, tokenization, clustering, and LLM interaction.

* **Application (Use Cases):** Orchestration of main flows, such as classification, stopwords refinement, label generation, auditing, and hierarchy generation.

* **Infrastructure:** Concrete implementations of the ports, such as repositories for Excel and PDF files, data cleaning services, tokenization, KMeans clustering, integrated LLM services, and report generation.

* **Interface:** Presentation layer, currently via CLI, offering interactive menus to execute functionalities and receive user parameters.

The system integrates with external APIs, mainly OpenAI, for language model usage that supports label generation, auditing, and intelligent refinement.

This architecture allows for easy replacement and extension of components, ensuring scalability for future improvements and adaptations.

---

## 5. How to Use the Tool (Concept)

As a concept under development, the tool is currently used via a command-line interface (CLI) with interactive menus that allow:

* **Classifying documents** (Excel, PDF, or folders) at multiple hierarchical levels.
* **Managing stopwords** dynamically, with LLM assistant support for iterative refinement.
* **Generating cluster labels** automatically using language models.
* **Auditing clusters** with merge or split suggestions, promoting better organization.
* **Generating abstracts** to facilitate cluster comprehension.
* **Viewing performance reports** for classification quality analysis.

The user is guided by menus requesting file paths, clustering parameters, and refinement options, streamlining the flow without requiring deep technical knowledge.

---

## 6. Structure of Input and Output Files

**Input Files:**

* Excel documents (.xlsx) with spreadsheets containing textual requirements.
* PDF documents (.pdf) for text extraction.
* Directories containing multiple Excel or PDF files for batch processing.

**Intermediate Files:**

* `freq_words.txt`: List of frequent words extracted after cleaning and tokenization, used to assist stopword refinement.
* `all_clustered.xlsx`: File with clustering results containing IDs, tokenized texts, and cluster numbers.
* `labels.json`: JSON with labels generated for clusters by the LLM.
* `id_source_mapping.csv`: Maps IDs to the original document names.

**Output Files:**

* `merged_clusters.xlsx`: Consolidates hierarchies with labels at various levels and document names.
* `abstracts.xlsx`: Automatic summaries for clusters, facilitating thematic analysis.

Example of key columns in Excel files:

| Column           | Description                                |
| ---------------- | ------------------------------------------ |
| ID               | Unique identifier of the row/document      |
| processed\_text  | Cleaned and tokenized text                 |
| joined\_tokens   | Concatenated tokens for vectorization      |
| cluster          | Assigned cluster index                     |
| Primary\_label   | Label generated for primary cluster        |
| Secondary\_label | Label generated for secondary cluster      |
| Tertiary\_label  | Label generated for tertiary cluster       |
| DocumentName     | Original file/document name                |
| Abstract         | Summary automatically generated by the LLM |

---

## 7. Technical Considerations and Limitations

* The use of language models (LLMs) entails costs associated with API requests, which must be considered in planning.
* The quality of the results depends on the quality of the input data; poorly formatted documents can hinder classification.
* Iterative refinement processes may require significant computational time for large volumes.
* The system is at a conceptual stage and requires continuous validation to ensure robustness and scalability.
* The complexity of the hierarchy may impact human interpretation, requiring care in analyzing results.
* Future improvements may include graphical interfaces, pipeline automation, support for other languages, and **dedicated API test servers** for greater security and usage control.

---

## 8. Results

* **Database:** [Database](https://erasmusegalitarian.github.io/educado-docs/database/database_index/)

### Suggested Searches

To facilitate your navigation, we suggest the following searches in the wiki:

* **Search "financial education"**
  Explore documents related to financial education, including digital platforms, courses, and reports.

* **Search "cybersecurity"**
  Find materials on secure software development, cyberattacks, and vulnerability analysis.

* **Search "waste pickers"**
  Discover content focused on social inclusion and education for waste pickers through mobile technologies.

---

## 9. Contact and Support

This project is under development and open to collaborations and suggestions. To get in touch, contribute code, or report issues, use the following channels:

* **GitHub Repository:** [https://github.com/LucasGSAntunes/requirements\_educado\_2024](https://github.com/LucasGSAntunes/requirements_educado_2024)
* **E-mail:** [lgabrielantunes@gmail.com](mailto:lgabrielantunes@gmail.com)
* **Community and Discussions:** Contact us for more information.

Your participation is very welcome to improve this tool and make it a robust solution for hierarchical classification based on NLP and AI.

---


[← Back to Main Page](index.md)
