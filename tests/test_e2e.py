import pytest
import subprocess
import time
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module", autouse=True)
def start_backend_server():
    """自动化钩子：在跑测试前，自动在后台把我们的 main.py 服务启起来"""
    process = subprocess.Popen(["python", "main.py"])
    time.sleep(1)  # 给服务器 1 秒钟的启动时间
    yield
    process.terminate()  # 测试跑完后，把后台服务器杀掉，释放 8080 端口

def test_fullstack_login_flow():
    with sync_playwright() as p:
        # 1. 启动无头浏览器
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 2. 浏览器打开前端网页
        page.goto("http://127.0.0.1:8080")
        
        # 3. 真实模拟：在输入框里输入 "guest"，然后点击提交
        page.fill("#username", "guest")
        page.click("#submit-btn")
        
        # 4. 断言：前端界面应该收到后端的无情拒绝
        page.wait_for_selector("#message")
        assert page.locator("#message").text_content() == "Access Denied!"
        
        # 5. 真实模拟：清空输入框，换成 "admin" 再点一次
        page.fill("#username", "")
        page.fill("#username", "admin")
        page.click("#submit-btn")
        
        # 6. 断言：全栈链路跑通，前端成功显示欢迎语
        # 这里的 locator 类似于 JS 的 document.querySelector 或者 Cypress 的 cy.get()
        assert page.locator("#message").text_content() == "Welcome, Admin!"
        
        browser.close()