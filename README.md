# HabitWay
## My last TG bot for Not Smoking tracker 
### Structure:

```
HabitWay_bot/
├── main.py                  — запуск бота и приветствие
├── config.py                — токен, данные БД
├── database/
│   ├── initializition.py    — подключение к БД
│   └── requests.py          — все SQL запросы
├── handlers/
│   ├── __init__.py          - инициализация хэндлера
│   ├── registration.py      - процесс регистрации
│   └── profile.py           - показ профиля
├── keyboards/
│   ├── exist_keyboard.py    — кнопки для зарегистрированного пользователя
│   └── unexist_keyboard.py  - кнопка для незарегистрированного пользователя
├── states/
│   └── registration.py      - состояние для регистрации
└── middlewares/
    └── middleware.py        — передача соединения БД в handlers
```   