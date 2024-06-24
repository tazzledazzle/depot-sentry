```
RepoSentry/
│
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── github_routes.py
│   │   │   ├── gitlab_routes.py
│   │   │   ├── bitbucket_routes.py
│   │   │   └── vcs_routes.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── github_service.py
│   │   │   ├── gitlab_service.py
│   │   │   ├── bitbucket_service.py
│   │   │   └── notification_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── db.py
│   │   │   └── logger.py
│   │   └── tests/
│   │       ├── __init__.py
│   │       ├── test_app.py
│   │       └── test_services.py
│   ├── requirements.txt
│   ├── setup.py
│   ├── Dockerfile
│   └── README.md
│
├── ...
```