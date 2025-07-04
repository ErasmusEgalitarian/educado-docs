# Diagrama Relacional do Banco de Dados - Plataforma de Cursos

[← Back to Main Page](../../../index.md)

## Modelo Entidade-Relacionamento (MER)

O Modelo Entidade-Relacionamento (MER) representa a estrutura lógica do banco de dados do projeto, destacando as principais entidades, seus atributos e os relacionamentos entre elas. Ele serve como base para o desenvolvimento do banco de dados relacional, facilitando o entendimento.

Cada entidade representa um conjunto de dados importantes para o sistema, como usuários, produtos ou pedidos. Os atributos descrevem as características dessas entidades, como nome, data de criação ou status. Já os relacionamentos mostram como essas entidades se conectam entre si, por exemplo, um usuário pode fazer vários pedidos, ou um produto pode pertencer a uma categoria.

---

### Entidades

- `USER`
- `ROLE`
- `COURSE`
- `MODULE`
- `LESSON`
- `EXERCISE`
- `ENROLLMENT`
- `MEDIA`
- `NOTIFICATION`

---

### Atributos

#### USER

`(user_email*, name, password, role_name, status, avatar_url, deleted_at, created_at, updated_at)`

#### ROLE

`(role_name*, description, deleted_at, created_at, updated_at)`

#### COURSE

`(id*, course_title, description, creator_email, status, cover_url, level, category, deleted_at, created_at, updated_at)`

#### MODULE

`(id*, course_id, module_title, description, display_order, deleted_at, created_at, updated_at)`

#### LESSON

`(module_title*, lesson_title*, course_title, {content}, description, display_order, deleted_at, created_at, updated_at)`

#### EXERCISE

`(id*, exercise_title, question, {choices}, answer, content, description, display_order, deleted_at, created_at, updated_at)`

#### ENROLLMENT

`(user_email*, course_title*, status, {completed_exercises}, {completed_lessons}, stars, comment, enrolled_at, deleted_at)`

#### MEDIA

`(media_url*, owner_email, type, description, deleted_at, created_at, updated_at)`

#### NOTIFICATION

`(notification_id*, sender_email, recipient_email, type, title, message, status, sent_at, read_at, deleted_at, created_at, updated_at)`

---

### Relacionamentos

- Um **COURSE** é criado por um **USER**.  
  → Um **USER** pode criar vários **COURSES**.

- Um **MODULE** pertence a um **COURSE**.  
  → Um **COURSE** pode conter vários **MODULES**.

- Uma **LESSON** pertence a um **MODULE**.  
  → Um **MODULE** pode conter várias **LESSONS**.

- Um **EXERCISE** pertence a uma **LESSON**.  
  → Uma **LESSON** pode ter vários **EXERCISES**.

- Um **ENROLLMENT** pertence a um **USER**.  
  → Um **USER** pode ter vários **ENROLLMENTS**.

- Um **ENROLLMENT** pertence a um **COURSE**.  
  → Um **COURSE** pode ter vários **ENROLLMENTS**.

---

## Legenda

- (PK) = Primary Key
- (FK) = Foreign Key
- (UK) = Unique Key
- `deleted_at` = Soft delete (data de exclusão lógica)
- `version` = Número da versão do registro (auditoria/histórico)
- `created_at` / `updated_at` = Datas de criação e modificação
- `_history` = Sufixo para tabelas de histórico de alteração

---

## Entidades Principais

### users

| Campo         | Tipo         | Restrições           | Descrição                       |
|---------------|--------------|----------------------|---------------------------------|
| id            | UUID         | PK                   | Identificador do usuário        |
| name          | VARCHAR(255) | NOT NULL             | Nome                            |
| email         | VARCHAR(255) | NOT NULL, UK         | E-mail                          |
| password_hash | VARCHAR(255) | NOT NULL             | Senha (hash)                    |
| role          | VARCHAR(32)  | NOT NULL             | Enum: 'admin', 'creator', 'student' |
| status        | VARCHAR(32)  | NOT NULL             | Enum: 'active', 'pending', 'rejected', 'inactive' |
| avatar_url    | VARCHAR(255) |                      | URL da imagem de perfil         |
| deleted_at    | TIMESTAMP    |                      | Soft delete                     |
| created_at    | TIMESTAMP    | DEFAULT now()        |                                 |
| updated_at    | TIMESTAMP    | DEFAULT now()        |                                 |
| version       | INT          | DEFAULT 1            | Controle de versão              |

#### Histórico: users_history (espelha a estrutura, incluindo quem alterou)

---

### roles

| Campo         | Tipo         | Restrições | Descrição                   |
|---------------|--------------|------------|-----------------------------|
| id            | UUID         | PK         | Identificador do papel      |
| name          | VARCHAR(32)  | UK         | Nome do papel               |
| description   | TEXT         |            | Descrição                   |
| deleted_at    | TIMESTAMP    |            | Soft delete                 |
| created_at    | TIMESTAMP    | DEFAULT now() |                           |
| updated_at    | TIMESTAMP    | DEFAULT now() |                           |
| version       | INT          | DEFAULT 1  | Controle de versão          |

#### Histórico: roles_history

---

### permissions

| Campo         | Tipo         | Restrições | Descrição                    |
|---------------|--------------|------------|------------------------------|
| id            | UUID         | PK         | Identificador da permissão   |
| name          | VARCHAR(64)  | UK         | Nome da permissão            |
| description   | TEXT         |            | Descrição                    |
| deleted_at    | TIMESTAMP    |            | Soft delete                  |
| created_at    | TIMESTAMP    | DEFAULT now() |                            |
| updated_at    | TIMESTAMP    | DEFAULT now() |                            |
| version       | INT          | DEFAULT 1  | Controle de versão           |

#### Histórico: permissions_history

---

### roles_permissions

| Campo       | Tipo   | Restrições              | Descrição                   |
|-------------|--------|-------------------------|-----------------------------|
| role_id     | UUID   | PK, FK -> roles(id)     | Papel                       |
| permission_id | UUID | PK, FK -> permissions(id) | Permissão                  |
| deleted_at  | TIMESTAMP |                      | Soft delete                 |
| created_at  | TIMESTAMP | DEFAULT now()         |                             |
| version     | INT      | DEFAULT 1              | Controle de versão          |

#### Histórico: roles_permissions_history

---

### courses

| Campo         | Tipo         | Restrições           | Descrição                         |
|---------------|--------------|----------------------|-----------------------------------|
| id            | UUID         | PK                   | Identificador do curso            |
| title         | VARCHAR(255) | NOT NULL             | Título                            |
| description   | TEXT         |                      | Descrição                         |
| creator_id    | UUID         | FK -> users(id)      | Criador do curso                  |
| status        | VARCHAR(32)  | NOT NULL             | Enum: 'active', 'inactive', 'deleted' |
| deleted_at    | TIMESTAMP    |                      | Soft delete                       |
| created_at    | TIMESTAMP    | DEFAULT now()        |                                   |
| updated_at    | TIMESTAMP    | DEFAULT now()        |                                   |
| version       | INT          | DEFAULT 1            | Controle de versão                |

#### Histórico: courses_history

---

### modules

| Campo       | Tipo         | Restrições           | Descrição                       |
|-------------|--------------|----------------------|---------------------------------|
| id          | UUID         | PK                   | Identificador do módulo         |
| course_id   | UUID         | FK -> courses(id)    | Curso                          |
| title       | VARCHAR(255) | NOT NULL             | Título                         |
| description | TEXT         |                      | Descrição                      |
| order       | INT          |                      | Ordem do módulo                |
| deleted_at  | TIMESTAMP    |                      | Soft delete                    |
| created_at  | TIMESTAMP    | DEFAULT now()        |                                |
| updated_at  | TIMESTAMP    | DEFAULT now()        |                                |
| version     | INT          | DEFAULT 1            | Controle de versão             |

#### Histórico: modules_history

---

### lessons

| Campo       | Tipo         | Restrições           | Descrição                       |
|-------------|--------------|----------------------|---------------------------------|
| id          | UUID         | PK                   | Identificador da aula           |
| module_id   | UUID         | FK -> modules(id)    | Módulo                         |
| title       | VARCHAR(255) | NOT NULL             | Título                         |
| content     | TEXT         |                      | Conteúdo                       |
| order       | INT          |                      | Ordem da aula                  |
| deleted_at  | TIMESTAMP    |                      | Soft delete                    |
| created_at  | TIMESTAMP    | DEFAULT now()        |                                |
| updated_at  | TIMESTAMP    | DEFAULT now()        |                                |
| version     | INT          | DEFAULT 1            | Controle de versão             |

#### Histórico: lessons_history

---

### exercises

| Campo       | Tipo         | Restrições           | Descrição                       |
|-------------|--------------|----------------------|---------------------------------|
| id          | UUID         | PK                   | Identificador do exercício      |
| lesson_id   | UUID         | FK -> lessons(id)    | Aula                           |
| title       | VARCHAR(255) | NOT NULL             | Título                         |
| description | TEXT         |                      | Descrição                      |
| order       | INT          |                      | Ordem                          |
| deleted_at  | TIMESTAMP    |                      | Soft delete                    |
| created_at  | TIMESTAMP    | DEFAULT now()        |                                |
| updated_at  | TIMESTAMP    | DEFAULT now()        |                                |
| version     | INT          | DEFAULT 1            | Controle de versão             |

#### Histórico: exercises_history

---

### enrollments

| Campo        | Tipo    | Restrições              | Descrição                       |
|--------------|---------|-------------------------|---------------------------------|
| id           | UUID    | PK                      | Identificador da matrícula      |
| user_id      | UUID    | FK -> users(id)         | Aluno matriculado               |
| course_id    | UUID    | FK -> courses(id)       | Curso                          |
| status       | VARCHAR(32) | NOT NULL            | Enum: 'active', 'cancelled'     |
| enrolled_at  | TIMESTAMP | DEFAULT now()         | Data da matrícula               |
| deleted_at   | TIMESTAMP |                       | Soft delete                     |
| version      | INT      | DEFAULT 1              | Controle de versão              |

#### Histórico: enrollments_history

---

### progress

| Campo        | Tipo    | Restrições                | Descrição                   |
|--------------|---------|---------------------------|-----------------------------|
| id           | UUID    | PK                        | Identificador do progresso  |
| user_id      | UUID    | FK -> users(id)           | Usuário                     |
| course_id    | UUID    | FK -> courses(id)         | Curso                       |
| module_id    | UUID    | FK -> modules(id)         | Módulo                      |
| lesson_id    | UUID    | FK -> lessons(id)         | Aula                        |
| progress_pct | NUMERIC(5,2) |                      | Percentual de conclusão     |
| updated_at   | TIMESTAMP | DEFAULT now()            | Última atualização          |
| deleted_at   | TIMESTAMP |                          | Soft delete                 |
| version      | INT      | DEFAULT 1                 | Controle de versão          |

#### Histórico: progress_history

---

### media

| Campo         | Tipo         | Restrições           | Descrição                            |
|---------------|--------------|----------------------|--------------------------------------|
| id            | UUID         | PK                   | Identificador da mídia               |
| owner_id      | UUID         | FK -> users(id)      | Dono da mídia                        |
| url           | VARCHAR(255) | NOT NULL             | Caminho/URL do arquivo               |
| type          | VARCHAR(32)  |                      | Tipo (imagem, vídeo, áudio)          |
| description   | TEXT         |                      | Descrição                            |
| deleted_at    | TIMESTAMP    |                      | Soft delete                          |
| created_at    | TIMESTAMP    | DEFAULT now()        |                                      |
| updated_at    | TIMESTAMP    | DEFAULT now()        |                                      |
| version       | INT          | DEFAULT 1            | Controle de versão                   |

#### Histórico: media_history

---

### course_media

| Campo       | Tipo   | Restrições                | Descrição                |
|-------------|--------|---------------------------|--------------------------|
| id          | UUID   | PK                        | Identificador            |
| course_id   | UUID   | FK -> courses(id)         | Curso                    |
| media_id    | UUID   | FK -> media(id)           | Mídia                    |
| deleted_at  | TIMESTAMP |                         | Soft delete              |
| created_at  | TIMESTAMP | DEFAULT now()           |                          |
| version     | INT      | DEFAULT 1                | Controle de versão       |

#### Histórico: course_media_history

---

### notifications

| Campo        | Tipo         | Restrições               | Descrição                 |
|--------------|--------------|--------------------------|---------------------------|
| id           | UUID         | PK                       | Identificador da notificação |
| sender_id    | UUID         | FK -> users(id)          | Remetente                 |
| recipient_id | UUID         | FK -> users(id)          | Destinatário              |
| title        | VARCHAR(255) | NOT NULL                 | Título                    |
| message      | TEXT         | NOT NULL                 | Mensagem                  |
| status       | VARCHAR(32)  | NOT NULL                 | Enum: 'sent', 'read'      |
| sent_at      | TIMESTAMP    |                          | Data envio                |
| read_at      | TIMESTAMP    |                          | Data leitura              |
| deleted_at   | TIMESTAMP    |                          | Soft delete               |
| created_at   | TIMESTAMP    | DEFAULT now()            |                           |
| updated_at   | TIMESTAMP    | DEFAULT now()            |                           |
| version      | INT          | DEFAULT 1                | Controle de versão        |

#### Histórico: notifications_history

---

## Observações Gerais

- **Cada tabela possui sua tabela de histórico**, espelhando campos e incluindo usuário/responsável pela alteração.
- **Soft delete**: Todos os SELECTs relevantes devem filtrar por `deleted_at IS NULL`.
- **Controle de permissão**: Use a estrutura de roles/permissions para RBAC, mesmo com uso restrito (admin/creator/student).
- **Relacionamentos**: Todos os FKs estão explícitos.
- **Versão**: O campo `version` deve ser incrementado a cada alteração, auxiliando o versionamento e a auditoria.
- **Auditoria**: As tabelas de histórico devem registrar o usuário responsável pela mudança (ex: campo `changed_by`).

---

## Diagrama Entidade-Relacionamento (ERD) - [Sugestão visual]

Para a versão visual, recomenda-se utilizar ferramentas como **dbdiagram.io** ou **draw.io** com as tabelas acima.

---

Se precisar do **DDL em SQL**, modelo visual ou ajustes finos de relacionamento, me avise antes de seguir. Se algum campo, relação ou comportamento ficou de fora, só apontar.

---

[← Back to Main Page](../../../index.md)
