### ToDo
Create weather forecast aggregator.

###Sprint 1 (10/11/2022)
1. Connect to one API resource
2. Telegam channel with command 'Now' - show current temperature/
3. Only one default city
4. Deployment on VDS
5. Script update app
6. Script restart app


###Backlog
- Add unit test
- CICD run test
- if OK - deploy on production
- Services
  - https://www.gismeteo.ru/api/
  - https://yandex.ru/dev/weather/
  - https://openweathermap.org/api
  - https://open-meteo.com/en
- add
  - yaml config  
  - default file
  - logger
- admin panel
  - flask
  - jwt auth
- db for data
  - migration
  - SQL Alchemy + Gino
    - https://habr.com/ru/company/kts/blog/579214/
- bots 
  - vk bot
    - vkware or vkbottle
  - telegram 
    - aiogram 
    - pyTelegramBotAPI
  - discord.py 
- aiohttp
  - создание ассинхронного веб сервар 
    - https://habr.com/ru/company/kts/blog/560058/
  - Dependency Injector
    - https://habr.com/ru/post/513510/ 
    - https://github.com/ets-labs/python-dependency-injector 

### Steps
1. Create project in PyCharm
2. Create repo om GitHub
3. Telnet: 
    ```
    git init
    git remote add origin https://github.com/vvuri/tempestas.git
    git pull origin main
    git branch -m master main
    ```
4. Run venv
   - Open pyCharm --> Go to Settings --> Tools --> Terminal
   - C:\Windows\system32\cmd.exe /K  "venv\Scripts\activate.bat"
   - reopen terminal
5. Telegram bot
   https://github.com/python-telegram-bot/python-telegram-bot
   ```pip install python-telegram-bot```
6. Packages:
    ```pip freeze > requirements.txt```
7. Install pyYAML:
   ```pip install pyyaml```
8. Add setup.cfg for flake8
9. Add async telegram library:
```pip install aiogram```
10. 