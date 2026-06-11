from main import greet
from unittest.mock import patch
from main import check_admin_access

def test_check_admin_access_success():
    # 使用 patch 模拟外部依赖，让它返回 "admin"
    with patch("main.fetch_user_role_from_db") as mock_fetch:
        mock_fetch.return_value = "admin"

        # 断言当角色为 admin 时，函数应该返回 True
        assert check_admin_access(123) is True
        
def test_greet():
    assert greet("World") == "Hello, World!"


def test_fail():
    assert greet("Eric") == "Hello, Eric!"