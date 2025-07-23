# Telegram2Discord Forwarder

## English

This script forwards messages from a Telegram channel to a Discord channel using a webhook. All settings are configured in `config.json`.

### Features
- Forwards text messages from Telegram to Discord
- Sends messages as Discord embeds (customizable: title, color, author, footer, etc.)
- Easy configuration via `config.json`

### Requirements
- Python 3.8+
- Telegram API credentials (API_ID, API_HASH)
- Discord Webhook URL

### Setup
1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Get your Telegram API credentials:**
   - Register at https://my.telegram.org
   - Create an application to get `api_id` and `api_hash`
3. **Create a Discord Webhook:**
   - Go to your Discord channel settings → Integrations → Webhooks
   - Copy the webhook URL
4. **Edit `config.json`:**
   - Fill in your API credentials, Telegram channel, Discord webhook, and embed settings
5. **Run the script:**
   ```powershell
   python index.py
   ```

---

## Русский

Этот скрипт пересылает сообщения из Telegram-канала в Discord-канал через webhook. Все настройки задаются в `config.json`.

### Возможности
- Пересылка текстовых сообщений из Telegram в Discord
- Отправка сообщений как embed в Discord (можно настроить: заголовок, цвет, автор, футер и др.)
- Простая настройка через `config.json`

### Требования
- Python 3.8+
- Данные Telegram API (API_ID, API_HASH)
- Webhook URL Discord

### Установка и запуск
1. **Установите зависимости:**
   ```powershell
   pip install -r requirements.txt
   ```
2. **Получите данные Telegram API:**
   - Зарегистрируйтесь на https://my.telegram.org
   - Создайте приложение и получите `api_id` и `api_hash`
3. **Создайте Webhook в Discord:**
   - Настройки канала Discord → Интеграции → Webhooks
   - Скопируйте ссылку webhook
4. **Отредактируйте `config.json`:**
   - Впишите свои данные API, канал Telegram, webhook Discord и настройки embed
5. **Запустите скрипт:**
   ```powershell
   python index.py
   ``` 
