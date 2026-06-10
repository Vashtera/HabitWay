# HabitWay
My last TG bot for Not Smoking tracker 
Structure:
bot/
├── main.py          — запуск бота
├── config.py        — токен, данные БД
├── database/
│   ├── db.py        — подключение к БД
│   └── queries.py   — все SQL запросы
├── handlers/
│   ├── start.py     — /start, регистрация
│   └── tracker.py   — основная логика
├── keyboards/
│   └── menu.py      — кнопки
├── states/
│   └── registration.py  — FSM состояния
└── middlewares/
    └── db.py        — передача соединения БД в handlers