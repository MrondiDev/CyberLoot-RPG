# 🎮 CyberLoot-RPG (v0.9-alpha)

[RU] 📑 Модульный текстовый RPG-движок со стилизованным янтарно-оранжевым CLI-интерфейсом и суровым бэкендом в стиле постапокалипсиса, вдохновленный вселенной Stay Out.
[EN] 📑 A modular text-based RPG engine featuring a stylized amber-orange CLI, and a hardcore post-apocalyptic backend inspired by the Stay Out universe.

---

## 🇷🇺 Описание проекта (Russian)

Проект представляет собой консольную RPG, построенную на принципах модульной архитектуры, строгой типизации данных и безопасного управления (подход DevSecOps). 

### 🔥 Ключевые фичи архитектуры:
* **Защищенная авторизация (ИБ-стандарт):** Сервис аутентификации на базе реляционной СУБД SQLite3. Защита аккаунтов реализована через криптографическое хэширование паролей по стандарту SHA-256 с использованием уникальной случайной "соли" (secrets). Система маскирует ошибки входа фразной заглушкой для защиты от брутфорса и перебора логинов.
* **Изолированная модульность:** Проект разделен на независимые функциональные модули (`auth`, `shop`, `player`, `dungeons`, `saver`), координируемые через единое состояние оперативной памяти (`state.py`).
* **Динамическая экономика и инвентарь:** Скупка хабара реализована через универсальный справочник цен (`loot_prices`), что исключает написание громоздких условий `if/elif` и позволяет масштабировать проект в 3 строчки кода. Функция скупки оснащена умным фильтром регистра (автоматически распознает ввод «ПМ» и «пм»).
* **Экипировка и расширение слотов:** Вместимость рюкзака (`max_slots`) динамически привязана к типу надетого снаряжения (Вещмешок / Туристический рюкзак). При смене рюкзака старые вещи автоматически возвращаются в инвентарь без дюпа и багов.
* **Система сохранений:** Именные JSON-файлы профилей генерируются автоматически только после успешной верификации пользователя на уровне SQL-базы.

### 🛠️ Инструкция по запуску:
1. Клонируйте репозиторий: `git clone https://github.com`
2. Запустите главный файл: `python main.py`
*Проект использует только стандартную библиотеку Python и не требует установки внешних зависимостей.*

---

## 🇬🇧 Project Description (English)

This project is a console-based RPG built on modular architecture principles, clean data structures, and secure development standards (DevSecOps approach).

### 🔥 Key Backend Features:
* **Secure Authentication (SecOps Ready):** A robust auth service powered by relational SQLite3. Account protection is implemented via SHA-256 cryptographic password hashing combined with a unique random "salt" (secrets). Login errors are deliberately obscured to mitigate user-enumeration and brute-force attacks.
* **Isolated Data Architecture:** The engine is separated into independent functional modules (`auth`, `shop`, `player`, `dungeons`, `saver`), fully coordinated via an ephemeral runtime memory state (`state.py`).
* **Dynamic Economy & Smart Dictionary:** The loot-selling mechanism leverages a centralized dictionary system (`loot_prices`), eliminating hardcoded conditionals and allowing scalability in just 3 lines of code. It includes an intelligent case-insensitive filter (e.g., auto-matching "PM" and "pm").
* **Dynamic Equipment & Inventory:** Inventory capacity (`max_slots`) updates dynamically based on the currently equipped backpack (Duffel bag / Tactical backpack). Equipped bags seamlessly return old containers to inventory slots without data duplication.
* **Dynamic Persistence:** Profile-specific JSON save files are automatically generated strictly after successful user verification at the SQL database layer.

### 🛠️ Installation & Running:
1. Clone the repository: `git clone https://github.com/MrondiDev/CyberLoot-RPG.git`
2. Run the entry point: `python main.py`
*The engine relies strictly on the Python Standard Library, requiring zero external dependencies.*


