from json_user_processor.reader import read_json
from json_user_processor.processor import process_users, count_by_role


def main() -> None:
    try:
        users = read_json("users.json")
        processed = process_users(users)

        print("\n✅ Usuarios procesados:\n")
        for user in processed:
            print(f"- {user['name']} ({user['role']})")

        counts = count_by_role(processed)

        print("\n📊 Resumen por tipo:")
        for role, total in counts.items():
            print(f"{role}: {total}")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")

    except ValueError as e:
        print(f"❌ Error de formato: {e}")


if __name__ == "__main__":
    main()