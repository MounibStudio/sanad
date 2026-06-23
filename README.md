# سَنَد — Sanad

> مساعد قانوني بالدارجة المغربية للمواطنين في المناطق القروية

Academic prototype — EMSI Casablanca, 2025.  
A Django web app that helps rural/illiterate Moroccan users understand legal and administrative documents through Moroccan Arabic (Darija) voice interaction.

---

## App / Ownership Map

| App | Owner | Branch | Responsibility |
|---|---|---|---|
| `core` | **Both** | `main` only | Shared models, base template, service interfaces |
| `voice` | **Dev A** | `feature/voice-access` | Audio recording, ASR integration |
| `accessibility` | **Dev A** | `feature/voice-access` | TTS playback, high-contrast / large-font UI tweaks |
| `knowledge` | **Dev B** | `feature/knowledge-geo` | FAQ model, NLU / keyword matching |
| `institutions` | **Dev B** | `feature/knowledge-geo` | Institution model, geolocation lookup |

**Rule:** Only edit `core/` on `main` (via PR reviewed by both devs). Never touch the other developer's apps.

---

## Service Interface Contract

Both branches must implement the abstract base classes in `core/services/`:

| File | ABC | Implemented by |
|---|---|---|
| `base_asr.py` | `BaseASRService.transcribe(audio: bytes) → str` | Dev A — `voice` app |
| `base_tts.py` | `BaseTTSService.synthesize(text: str, lang: str) → bytes` | Dev A — `accessibility` app |
| `base_nlu.py` | `BaseNLUService.match(text: str) → FaqEntry \| None` | Dev B — `knowledge` app |
| `base_geo.py` | `BaseGeoService.nearest(topic, lat, lon) → list[Institution]` | Dev B — `institutions` app |

---

## Git Branching Workflow

```
main  (shared foundation — protected)
 ├── feature/voice-access    ← Dev A works here
 └── feature/knowledge-geo   ← Dev B works here
```

1. **Clone** the repo and create your branch from `main`:
   ```bash
   git checkout -b feature/voice-access   # Dev A
   # or
   git checkout -b feature/knowledge-geo  # Dev B
   ```

2. **Commit** often on your own branch. Push when ready:
   ```bash
   git push -u origin feature/voice-access
   ```

3. **Open a Pull Request** into `main` when a feature is ready. The other developer reviews and merges.

4. **Keep your branch up to date** with main regularly:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

5. **Never force-push `main`.**

---

## Setup & Run

### First time

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. (Optional) Create an admin user
python manage.py createsuperuser

# 5. Start the development server
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### After pulling new changes from main

```bash
source .venv/bin/activate
pip install -r requirements.txt   # in case new packages were added
python manage.py migrate          # in case new migrations were added
python manage.py runserver
```

---

## Project Structure

```
sanad/                        ← Django project config
core/                         ← shared (main branch)
│   models.py                 Session + HistoryEntry
│   views.py + urls.py        home page
│   templates/core/
│       base.html             RTL layout, Tailwind, Arabic font
│       home.html             two pictogram buttons
│   services/
│       base_asr.py           ABC interface (no implementation)
│       base_tts.py           ABC interface (no implementation)
│       base_nlu.py           ABC interface (no implementation)
│       base_geo.py           ABC interface (no implementation)
voice/                        ← Dev A stub
accessibility/                ← Dev A stub
knowledge/                    ← Dev B stub
institutions/                 ← Dev B stub
```

---

## Stack

- **Backend:** Django 6 + SQLite (no external APIs)
- **Templates:** Django server-rendered templates (RTL, `lang="ar" dir="rtl"`)
- **Styling:** Tailwind CSS via CDN (prototype only)
- **Font:** Noto Naskh Arabic (Google Fonts)
- **Phase 1 scope:** Web prototype running locally — no ASR/TTS/NLU/geo implemented yet
