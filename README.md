# farenus-bot

discord bot for farenus network.

## Konfiguracja

Bot wymaga aplikacji utworzonej w [Discord Developer Portal](https://discord.com/developers/applications).

Konfiguracja jest wczytywana ze zmiennych środowiskowych zapisanych w pliku `.env` (patrz `config.py`)

## Uruchomienie lokalne

```bash
git clone https://github.com/farenus/farenus-bot.git
uv sync
uv run python -m farenus_bot.main
```

## Wdrożenie na serwer

Pierwsze wdrożenie:

```bash
curl -LsSf https://astral.sh/uv/install.sh | UV_UNMANAGED_INSTALL=/usr/local/bin sh
export PATH="/usr/local/bin:$PATH"
echo 'export PATH="/usr/local/bin:$PATH"' >> /root/.bashrc
export UV_PYTHON_INSTALL_DIR=/opt/uv-python
echo 'export UV_PYTHON_INSTALL_DIR=/opt/uv-python' >> /root/.bashrc

useradd --system --no-create-home --shell /usr/sbin/nologin bot
install -d -o bot -g bot -m 750 /var/lib/bot

git clone https://github.com/farenus/farenus-bot.git /opt/bot
cd /opt/bot
git checkout vX.Y.Z

uv sync --locked --no-dev

cp .env.example .env
chown root:bot .env
chmod 640 .env

cp deploy/farenus-bot.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now farenus-bot
```

Aktualizacja do nowej wersji:

```bash
cd /opt/bot
git fetch --tags
git checkout vX.Y.Z

uv sync --locked --no-dev

systemctl restart farenus-bot
```

Jeśli zmienił się plik `deploy/farenus-bot.service`, skopiuj go ponownie i wykonaj `systemctl daemon-reload`.

## Obsługa na serwerze

```bash
systemctl status farenus-bot   # stan usługi
journalctl -u farenus-bot -f   # logi na żywo

systemctl restart farenus-bot  # restart
systemctl stop farenus-bot     # zatrzymanie
systemctl start farenus-bot    # uruchomienie
```
