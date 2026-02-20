import random
import string

# Базовые наборы символов
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = "_"


def generate_string(
    min_len: int = 3,
    max_len: int = 15,
    use_special: bool = True,
    require_uppercase: bool = True,
    require_digit: bool = True,
) -> str:

    # Формируем пул символов
    chars = LOWERCASE + UPPERCASE + DIGITS

    if use_special:
        chars += SPECIAL

    if not chars:
        raise ValueError("Не выбран ни один набор символов")

    length = random.randint(min_len, max_len)
    result = []

    # Гарантируем наличие заглавной, если требуется
    if require_uppercase:
        # Добавляем одну заглавную букву
        result.append(random.choice(UPPERCASE))
        # Уменьшаем оставшуюся длину на 1
        remaining = length - 1
    else:
        remaining = length

    # Гарантируем наличие цифры, если требуется
    if require_digit:
        # Добавляем одну цифру
        result.append(random.choice(DIGITS))
        # Уменьшаем оставшуюся длину на 1
        remaining = length - 1
    else:
        remaining = length

    # Заполняем остаток случайными символами из пула
    result.extend(random.choice(chars) for _ in range(remaining))

    # Перемешиваем, чтобы заглавная не всегда была первой
    random.shuffle(result)

    return "".join(result)


def generate_login(
    min_len: int = 3,
    max_len: int = 15,
    use_special: bool = True,
    require_uppercase: bool = False,  # для логина заглавная необязательна
    require_digit: bool = False,  # для логина цифра необязательна
) -> str:
    """
    Генерация логина (обёртка над generate_string с разумными умолчаниями).
    """
    return generate_string(
        min_len=min_len,
        max_len=max_len,
        use_special=use_special,
        require_uppercase=require_uppercase,
        require_digit=require_digit,
    )


def generate_password(
    min_len: int = 8,
    max_len: int = 16,
    use_special: bool = False,  # в пароле запрещены спецсимволы
    require_uppercase: bool = True,  # в пароле обязательна заглавная
    require_digit: bool = True,  # в пароле обязательна цифра
) -> str:
    """
    Генерация пароля (обёртка над generate_string с разумными умолчаниями).
    """
    return generate_string(
        min_len=min_len,
        max_len=max_len,
        use_special=use_special,
        require_uppercase=require_uppercase,
        require_digit=require_digit,
    )
