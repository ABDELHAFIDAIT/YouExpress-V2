# YouExpress-V2


```bash
YouExpress-V2/
│
├── docker-compose.yml        # [ORCHESTRATION] Définit les services (db, backend, frontend)
├── .env                      # [CONFIG] Variables d'environnement globales
├── .gitignore                # Fichiers à exclure (venv, __pycache__, .env, data/)
├── README.md                 # Documentation
│
├── data/                     # [VOLUMES] Créé automatiquement par Docker
│   └── postgres_data/        # Persistance de la base de données
│
├── backend/                  # === SERVICE BACKEND (FastAPI) ===
│   ├── Dockerfile            # Instruction de construction de l'image Backend
│   ├── requirements.txt      # Dépendances Backend (fastapi, sqlalchemy, psycopg2, pyjwt...)
│   ├── alembic.ini           # Configuration des migrations
│   ├── alembic/              # Scripts de migration
│   │   ├── versions/
│   │   └── env.py
│   │
│   └── app/                  # Code Source Python
│       ├── __init__.py
│       ├── main.py           # Point d'entrée FastAPI
│       │
│       ├── api/              # [CONTROLLERS]
│       │   ├── __init__.py
│       │   ├── dependencies.py   # Vérification JWT & Rôles
│       │   └── v1/
│       │       ├── __init__.py
│       │       ├── auth_routes.py
│       │       ├── users_routes.py
│       │       ├── colis_routes.py
│       │       ├── livreurs_routes.py
│       │       └── zones_routes.py
│       │
│       ├── core/             # [CONFIG & SECURITE]
│       │   ├── __init__.py
│       │   ├── config.py     # Settings (pydantic-settings)
│       │   ├── security.py   # Hashage (Passlib) & JWT (PyJWT)
│       │   └── logging_conf.py
│       │
│       ├── db/               # [DATABASE]
│       │   ├── __init__.py
│       │   ├── session.py    # SessionLocal & Engine
│       │   └── base.py       # Import de tous les models pour Alembic
│       │
│       ├── exceptions/       # [ERROR HANDLING]
│       │   ├── __init__.py
│       │   ├── definitions.py
│       │   └── handlers.py
│       │
│       ├── models/           # [MODELS SQLALCHEMY]
│       │   ├── __init__.py
│       │   ├── user_models.py (User, Role, Livreur)
│       │   ├── colis_models.py (Colis, Historique)
│       │   └── zone_models.py
│       │
│       ├── repositories/     # [DATA ACCESS LAYER]
│       │   ├── __init__.py
│       │   ├── user_repo.py
│       │   ├── colis_repo.py
│       │   └── role_repo.py
│       │
│       ├── schemas/          # [PYDANTIC SCHEMAS]
│       │   ├── __init__.py
│       │   ├── auth_schemas.py
│       │   ├── user_schemas.py
│       │   └── colis_schemas.py
│       │
│       ├── services/         # [BUSINESS LOGIC]
│       │   ├── __init__.py
│       │   ├── auth_service.py
│       │   ├── colis_service.py
│       │   └── seed_service.py
│       │
│       └── seeds/            # [DATA INITIALE]
│           └── data_maroc.py
│
├── frontend/                 # === SERVICE FRONTEND (Streamlit) ===
│   ├── Dockerfile            # Instruction de construction de l'image Frontend
│   ├── requirements.txt      # Dépendances Frontend (streamlit, requests)
│   │
│   ├── app.py                # Point d'entrée (Main Router)
│   ├── api_client.py         # Client HTTP (Appelle http://backend:8000)
│   ├── auth_state.py         # Gestion de Session
│   │
│   ├── assets/               # CSS, Logos
│   │   └── style.css
│   │
│   ├── components/           # Widgets réutilisables
│   │   ├── sidebar.py
│   │   └── status_badge.py
│   │
│   └── views/                # Pages de l'application
│       ├── login_view.py
│       ├── admin_dashboard.py
│       ├── livreur_interface.py
│       └── client_tracking.py
│
└── tests/                    # [TESTS GLOBAUX]
    ├── __init__.py
    ├── conftest.py
    ├── test_auth.py
    └── test_flow_v2.py

```