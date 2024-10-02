URLs:

- https://htmx.org/essays/how-did-rest-come-to-mean-the-opposite-of-rest/

Этап 1:

- инициализация Flask приложения

Этап 2:

- установка HTMX

Этап 3:

- ping и hover примеры
- HTMX:
    - 'hx-trigger="mouseenter"'
    - 'hx-swap="outerHTML"'
    - 'hx-trigger="click[ctrlKey]"'

Этап 4:

- clicker via HTMX

Этап 5:

- встраивание основы Clicker в основную страницу

Этап 6:

- список товаров:
    - создание через стандартную HTML форму
    - создание через форму с использованием HTMX:
        - 'hx-post="{{ url_for('products_app.create') }}"'
        - 'hx-target="#products-list"'
        - 'hx-swap="outerHTML"'
        - 'hx-on::after-request="if (event.detail.successful) this.reset()"'
- добавление товаров в список через 'hx-swap="beforeend"'
- обработка out of band элементов с 'hx-swap="none"'
- возврат формы для замены и добавление нового элемента в список

Этап 7:

- добавление CSRF защиты формы из Flask-WTF
- обработка формы Flask-WTF для добавления товара

Этап 8:

- добавление заголовков 'hx-headers'
- пример с @csrf_exempt

Этап 9:

- удаление товара
- выбор цели:
    - по ближайшему тегу 'hx-target="closest li"'
    - по ближайшему классу 'hx-target="closest .product_item"'
- анимации:
- загрузка '.htmx-request'
- замена '.htmx-swapping'

Этап 10:

- обновление товара:
    - PUT запрос
    - обработка ошибок (форма)

Этап 11:
- HTMX push URL
- 'hx-target="body"'