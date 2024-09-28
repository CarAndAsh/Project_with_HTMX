URLs:
- https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/

Этап 1:
- Инициализация Flask приложения

Этап 2:
- Установка HTMX

Этап 3:
- Ping и hover примеры
- HTMX:
  - 'hx-trigger="mouseenter"'
  - 'hx-swap="outerHTML"'
  - 'hx-trigger="click[ctrlKey]"'

Этап 4:
- Clicker via HTMX

Этап 5:
- Встраивание основы Clicker в основную страницу

Этап 6:
- Список товаров:
  - создание через стандартную HTML форму
  - создание через форму с использованием HTMX:
    - 'hx-post="{{ url_for('products_app.create') }}"'
    - 'hx-target="#products-list"'
    - 'hx-swap="outerHTML"'
    - 'hx-on::after-request="if (event.detail.successful) this.reset()"'
- Добавление товаров в список через 'hx-swap="beforeend"'
- Обработка out of band элементов с 'hx-swap="none"'