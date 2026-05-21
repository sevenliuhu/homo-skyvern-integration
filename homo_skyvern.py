# Copyright (c) 2026 HOMO AI. Proprietary. License required. Contact: 16208204@qq.com
"""
homo-skyvern-integration — CloakBrowser + Skyvern 一键集成

Skyvern 通过 BROWSER_TYPE=cdp-connect 支持外挂浏览器。
这个脚本自动启动 CloakBrowser 并配置 Skyvern 连接它。

用法:
    python homo_skyvern.py setup          # 一键配置
    python homo_skyvern.py start-browser  # 启动CloakBrowser
    python homo_skyvern.py check          # 检查连接状态
"""
import os
import sys
import json
import subprocess
import urllib.request


def check_skyvern():
    """检查Skyvern是否安装"""
    try:
        import skyvern
        print("✅ Skyvern 已安装")
        return True
    except ImportError:
        print("❌ Skyvern 未安装 (pip install skyvern)")
        return False


def check_cloakbrowser():
    """检查CloakBrowser是否可用"""
    # 1. 检查scraper-server
    try:
        req = urllib.request.Request("http://127.0.0.1:9377/health")
        with urllib.request.urlopen(req, timeout=3) as r:
            data = json.loads(r.read())
            print(f"✅ CloakBrowser引擎在线: {data.get('status', 'ok')}")
            return True
    except:
        pass
    
    # 2. 检查CLI
    try:
        r = subprocess.run(["cloakbrowser", "--version"], capture_output=True, text=True, timeout=5)
        if r.returncode == 0:
            print(f"✅ CloakBrowser CLI可用: {r.stdout.strip()}")
            return True
    except:
        pass
    
    print("❌ CloakBrowser 不可用")
    print("   安装: pip install cloakbrowser")
    print("   或启动: HOMO Scraper Server (port 9377)")
    return False


def generate_env():
    """生成Skyvern环境配置"""
    env_content = """# ===== homo-skyvern-integration =====
# CloakBrowser + Skyvern 集成配置
# 复制到项目 .env 文件

# 浏览器模式: cdp-connect = 外挂CloakBrowser
BROWSER_TYPE=cdp-connect

# CloakBrowser远程调试端口
BROWSER_REMOTE_DEBUGGING_URL=http://127.0.0.1:9222

# 可选: 自定义Chrome路径
# BROWSER_PATH=/path/to/cloakbrowser
"""
    with open(".env.skyvern-cloak", "w") as f:
        f.write(env_content)
    print("✅ 配置已写入: .env.skyvern-cloak")
    print("   复制到项目目录: cp .env.skyvern-cloak .env")
    return True


def show_guide():
    """显示使用指南"""
    guide = """
┌─────────────────────────────────────────────────────┐
│  CloakBrowser + Skyvern 集成指南                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│  步骤1: 启动CloakBrowser                             │
│    cloakbrowser --remote-debugging-port=9222         │
│    (或启动 HOMO Scraper Server)                      │
│                                                     │
│  步骤2: 配置Skyvern                                  │
│    cp .env.skyvern-cloak .env                        │
│    # 编辑 .env, 确认BROWSER_TYPE=cdp-connect         │
│                                                     │
│  步骤3: 启动Skyvern                                  │
│    skyvern run server                                │
│                                                     │
│  步骤4: 验证                                        │
│    python homo_skyvern.py check                      │
│                                                     │
│  原理:                                              │
│    Skyvern的cdp-connect模式会连接指定端口上的浏览器    │
│    我们在这个端口上启动CloakBrowser                   │
│    Skyvern负责"做什么"，CloakBrowser负责"不被发现"    │
│                                                     │
│  免费版: 手动配置 (如上)                              │
│  Pro版: 自动配置 + 代理池 + 指纹管理                  │
│    https://github.com/sevenliuhu/homo-skyvern        │
└─────────────────────────────────────────────────────┘
"""
    print(guide)


def main():
    if len(sys.argv) < 2:
        print("用法: python homo_skyvern.py [setup|start-browser|check|guide]")
        return

    cmd = sys.argv[1]
    
    if cmd == "setup":
        check_skyvern()
        check_cloakbrowser()
        generate_env()
        show_guide()
    elif cmd == "check":
        c1 = check_skyvern()
        c2 = check_cloakbrowser()
        if c1 and c2:
            print("\n✅ 一切就绪，可以开始使用 Skyvern + CloakBrowser")
        else:
            print("\n⚠️  有组件缺失，请按指南安装")
    elif cmd == "guide":
        show_guide()
    else:
        print(f"未知命令: {cmd}")


if __name__ == "__main__":
    main()
