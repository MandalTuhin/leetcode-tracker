# LeetCode Tracker API

A high-performance **RESTful API** built with **FastAPI** to systematically track and manage LeetCode problem-solving progress. This project serves as a technical bridge between algorithmic practice and backend system development.

## 🚀 Overview

The **LeetCode Tracker API** enables users to log problems, store solutions (C++), and monitor progress through various difficulty levels. It is designed with strict data validation and asynchronous capabilities to ensure scalability and reliability.

### Key Features

- **Full CRUD Functionality**: Create, Read, Update, and Delete LeetCode problem logs.
- **Partial Updates**: Implementation of the `PATCH` method for efficient data modification.
- **Automated URL Generation**: Dynamic construction of LeetCode URLs based on problem slugs.
- **Modern Tooling**: Managed with **uv** for lightning-fast, reproducible dependency management.
- **Data Integrity**: Robust schema validation using **Pydantic** models and **Enums**.
- **Self-Documenting**: Integrated OpenAPI/Swagger UI for real-time API testing.

## 🌐 Live Deployment

The API is globally accessible and documented via Swagger UI:
[Interactive API Documentation](https://leetcode-tracker-api-production.up.railway.app/docs)

_Note: This deployment is hosted on Railway for high availability and performance._

## 🛠 Tech Stack

- **Framework**: FastAPI (Python 3.10+)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Validation**: Pydantic v2
- **Database**: SQLite
- **Documentation**: Swagger UI / ReDoc (OpenAPI 3.1.0)

## 📂 API Architecture

The API follows a structured schema for consistent data handling:

| Endpoint         | Method   | Description                               |
| :--------------- | :------- | :---------------------------------------- |
| `/problems/`     | `GET`    | Retrieve a list of all tracked problems.  |
| `/problems/`     | `POST`   | Create a new problem entry.               |
| `/problems/{id}` | `GET`    | Fetch details of a specific problem.      |
| `/problems/{id}` | `PATCH`  | Partially update an existing problem.     |
| `/problems/{id}` | `DELETE` | Remove a problem from the tracker.        |
| `/cache/{id}`    | `PUT`    | Access and persist problem data in cache. |

## 📊 Data Model

The application utilizes a structured `Problem` model:

- `problem_no`: (Integer) The official LeetCode problem number.
- `title`: (String) Name of the problem.
- `difficulty`: (Enum) Easy, Medium, or Difficult.
- `solution_cpp`: (String) The source code of the implemented solution.
- `is_solved`: (Boolean) Current status of the problem.
- `leetcode_url`: (Read-Only) Automatically generated link from the problem slug.

## ⚙️ Installation & Setup

This project uses **uv** for dependency management to ensure fast and reliable environments.

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/](https://github.com/)[your-username]/leetcode-tracker-api.git
   cd leetcode-tracker-api
   ```

2. **Sync the environment:** This will automatically create a virtual environment and install all dependencies from `pyproject.toml` or `uv.lock`.

   ```bash
   uv sync
   ```

3. **Run the server:**

   ```bash
   uv run uvicorn app.main:app --reload
   ```

4. Access Documentation: Open `http://127.0.0.1:8000/docs` to view the interactive Swagger UI.

## 📈 Motivation

This API was developed to document my journey of solving **216 LeetCode problems**. By applying backend engineering principles to my algorithmic practice, I aim to demonstrate a comprehensive understanding of both software design and problem-solving logic.

## 🚀 Future Roadmap

The following features are planned for subsequent iterations to enhance security and scalability:

- [ ] **Identity & Access Management**: Implementation of OAuth2 with JWT (JSON Web Tokens) for secure, stateless user authentication.
- [ ] **Cloud Migration**: Transitioning the data layer to a managed PostgreSQL instance for increased relational durability.
- [ ] **Advanced User-State Management**: Transitioning from local SQLite sessions to a distributed caching layer (Redis) for session persistence.
- [ ] **Rate Limiting**: Implementation of API throttling strategies to prevent abuse and ensure service stability.
- [ ] **Frontend Integration**: Development of a Svelte-based dashboard for visual progress analytics.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

**Professional Note:** This project demonstrates proficiency in FastAPI, Pydantic, and modern Python tooling (uv). It showcases an ability to transition from theoretical computer science to practical, production-ready software development.
