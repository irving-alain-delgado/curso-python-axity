from json_user_processor.validator import is_valid_email

def classify_user(user_type: str) -> str:
    match user_type:
        case "admin":
            return "Administrador"
        case "moderator":
            return "Moderador"
        case "user":
            return "Usuario"
        case _:
            return "Desconocido"

def process_users(users: list[dict]) -> list[dict]:
    processed_users = []

    for user in users:
        # Validar email
        if not is_valid_email(user.get("email", "")):
            print(f"⚠ Email inválido: {user.get('name')}")
            continue

        # Filtrar solo activos
        if not user.get("active", False):
            continue

        # Clasificar tipo con pattern matching
        role = classify_user(user.get("type", ""))

        user["role"] = role
        processed_users.append(user)

    return processed_users

def count_by_role(users: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}

    for user in users:
        role = user["role"]
        counts[role] = counts.get(role, 0) + 1

    return counts