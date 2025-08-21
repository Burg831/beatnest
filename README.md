# BeatNest

Django 5 project bootstrapped on macOS.
- App: `core`
- Python: 3.13 (Homebrew)
- Env: `.env` (not committed) via `django-environ`

## Local dev
```bash
python manage.py runserver
git add README.md
git commit -m "docs: add project README"
git push
# prove .env is ignored (should print a line showing .gitignore matched it)
git check-ignore -v .env

# add a safe example env file
cat > .env.example << 'EOF'
DEBUG=True
SECRET_KEY=
ALLOWED_HOSTS=127.0.0.1,localhost
