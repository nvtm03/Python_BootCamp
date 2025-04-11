# Задание 00

## Описание

Этот проект реализует простой WSGI-сервер, который принимает HTTP-запросы и возвращает имена известных видов в формате JSON. Сервер использует словарь для сопоставления видов с их соответствующими именами.

## Функциональность

Сервер обрабатывает GET-запросы с параметром `species`. Если вид существует в словаре, сервер возвращает имя этого вида. Если вид не найден, сервер возвращает сообщение об ошибке.

### Примеры видов

- Cyberman: John Lumic
- Dalek: Davros
- Judoon: Shadow Proclamation Convention 15 Enforcer
- Human: Leonardo da Vinci
- Ood: Klineman Halpen
- Silence: Tasha Lem
- Slitheen: Coca-Cola salesman
- Sontaran: General Staal
- Time Lord: Rassilon
- Weeping Angel: The Division Representative
- Zygon: Broton

## Запуск сервера

Для запуска сервера выполните следующую команду в терминале:

```bash
python credentials.py
```

```bash
curl 'http://127.0.0.1:8888/?species=Time%20Lord'
```