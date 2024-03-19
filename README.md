# PostOpCare

PostOpCare is a post-operative patient care tracker for hospitals and clinics. Staff can register patients and manage their appointments, consultations, medications, and recovery monitoring from a dashboard.

This repository contains **two implementations**, built at different stages of the project:

| | Stack | Entry point | Data store |
|---|---|---|---|
| **Flask version** | Python, Flask, Flask-SQLAlchemy | `app.py` | Local SQLite (`erp_healthcare.db`) |
| **Node version** | Node.js, Express, Supabase | `server.js` | Supabase (Postgres) |

Both cover the same domain — patients, appointments, consultations, medications, monitoring — but are independent. You only need to run one to use the app.

## Features

- Register patients with appointment scheduling
- Log doctor consultations and remarks
- Track medications and end dates
- Record recovery/monitoring status
- Dashboard view of all records, with delete actions

## Getting started — Flask version

```bash
pip install -r requirements.txt
python app.py
```

Runs at `http://localhost:5000`. The SQLite database is created automatically on first run.

## Getting started — Node/Supabase version

1. Create a [Supabase](https://supabase.com) project with `patients`, `appointments`, `consultations`, `medications`, and `doctors` tables.
2. Copy `.env.example` to `.env` and fill in your Supabase project URL and API key:
   ```bash
   cp .env.example .env
   ```
3. Install dependencies and start the server:
   ```bash
   npm install
   npm start
   ```

Runs at `http://localhost:4000`.

## Project structure

```
postopcare/
├── app.py               # Flask app (routes + SQLAlchemy models)
├── requirements.txt     # Python dependencies
├── templates/           # Jinja2 templates (Flask version)
├── server.js            # Express app (Supabase-backed API)
├── package.json         # Node dependencies
├── public/              # Static frontend (Node version)
└── static/images/       # Shared image assets
```

## Notes

- The Flask version stores data locally in SQLite — the simplest way to try the app with no external setup.
- The Node version expects a Supabase backend that already has matching tables; it does not create them automatically.
- Never commit a real `.env` file — `.env.example` documents the required variables only.

## License

MIT — see [LICENSE](LICENSE).
