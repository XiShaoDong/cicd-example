# main.py
def greet(name: str) -> str:
    return f"Hello, {name}!"

def fetch_user_role_from_db(user_id: int) -> str:
    # 假设这个函数会连接真实数据库，CI 环境下直接运行会报 ConnectionError
    raise ConnectionError("Database connection failed!")

def check_admin_access(user_id: int) -> bool:
    try:
        role = fetch_user_role_from_db(user_id)
        return role == "admin"
    except ConnectionError:
        return False

if __name__ == "__main__":
    print(greet("World"))
    print(check_admin_access(123))

