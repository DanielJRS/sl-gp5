# Repository Guidelines

## Project Structure & Module Organization
Main Django project code lives under `projeto/`. `manage.py` handles CLIs, while the inner `projeto/` package stores settings, URLs, and WSGI/ASGI entrypoints. Domain logic is concentrated in `sistemaVendas/`, which already exposes models, forms, views, migrations, and URL routing; keep new business modules in that app or in sibling apps when a feature grows. Shared templates reside in `templates/` (with the client layout under `templateCliente/`); mirror this structure for new features so that template discovery stays predictable.

## Build, Test, and Development Commands
Create an isolated environment before installing packages: `python -m venv .venv && source .venv/bin/activate`. Align with the current stack by installing Django 5.2.6 and the Postgres driver: `pip install django==5.2.6 psycopg2-binary`. Run schema updates through `python manage.py migrate`, boot the development server using `python manage.py runserver`, and seed credentials with `python manage.py createsuperuser`. Use `python manage.py makemigrations sistemaVendas` when introducing model changes so migrations stay versioned.

## Coding Style & Naming Conventions
Follow PEP 8 with four-space indentation, `snake_case` for variables and functions, and `PascalCase` for Django models, forms, and class-based views. Organize imports by standard library, third-party, then local modules. Keep HTML templates modular, naming files by the user action (`clientes_list.html`) and storing shared blocks in dedicated include files.

## Testing Guidelines
House unit tests alongside the app (`sistemaVendas/tests.py` or a `tests/` package). Prefer `django.test.TestCase` subclasses, naming methods with the behavior under test (`test_should_block_login_without_password`). Execute the suite with `python manage.py test sistemaVendas` before every push. Aim to cover model constraints, form validation, and view permissions, and add regression tests whenever a bug fix lands.

## Commit & Pull Request Guidelines
Existing history uses short, prefixed messages (`Feat:`, `Feature:`, `Fix:`); keep that style in the imperative mood, e.g., `Feat: ajustar fluxo de cadastro de clientes`. Commits should stay focused on one concern and include migrations when relevant. Pull requests need a concise summary, linked issue or ticket, notes on database or settings changes, and screenshots for any UI-facing update, plus manual QA steps when applicable.

## Security & Configuration Tips
`projeto/settings.py` targets a local Postgres instance by default; override credentials with environment variables or a `.env` consumed via `python-dotenv` to avoid editing the committed settings. Never commit real secrets or production connection strings. If you must develop with SQLite, adjust the `DATABASES` block in an ignored settings override so repository defaults remain untouched.
