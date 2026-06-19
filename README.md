# DjangoProject

Djangoで作成した投稿サイトです。
共同開発では、この `djangosnippets` ディレクトリをリポジトリのルートとして扱います。

## セットアップ

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 起動URL

```text
http://127.0.0.1:8000/
```

## Git管理しないもの

以下は `.gitignore` で除外しています。

- `.venv/`
- `__pycache__/`
- `*.pyc`
- `db.sqlite3`
- `.idea/`
- `.env`
- `*.exe`

## 共同開発の注意

- 新しい機能はブランチを作って作業してください。
- `db.sqlite3` は共有しないため、各自で `python manage.py migrate` を実行してください。
- 管理画面を使う場合は、各自で `python manage.py createsuperuser` を実行してください。
