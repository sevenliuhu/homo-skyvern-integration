#!/bin/bash
set -e
echo "================================"
echo "  homo-skyvern-integration"
echo "  CloakBrowser → Skyvern 集成"
echo "================================"
echo ""
if python3 -c "import skyvern" 2>/dev/null; then
    echo "✅ Skyvern 已安装"
else
    echo "❌ Skyvern 未安装 (pip install skyvern)"
    exit 1
fi
CLOAK_DIR="$HOME/.cloakbrowser"
mkdir -p "$CLOAK_DIR"
cat > .env.skyvern-cloak << ENVEOF
BROWSER_TYPE=cdp-connect
BROWSER_REMOTE_DEBUGGING_URL=http://127.0.0.1:9222
ENVEOF
echo "✅ 配置已生成: .env.skyvern-cloak"
echo "下一步:"
echo "  1. 启动CloakBrowser: cloakbrowser --remote-debugging-port=9222"
echo "  2. 启动Skyvern: skyvern run server"
