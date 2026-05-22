# homo-skyvern-integration 🛡️

> **CloakBrowser + Skyvern 一键集成**  
> Skyvern 负责"做什么"，CloakBrowser 负责"不被发现"

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 为什么需要这个？

[Skyvern](https://github.com/Skyvern-AI/skyvern)（22k★）是一个AI浏览器自动化框架，但它依赖Playwright执行浏览器操作。Playwright被反爬检测到时，整个流程就断了。

**CloakBrowser**（15k★）是C++源码级隐身Chromium，49个反检测补丁，过所有bot检测。

好消息：Skyvern原生支持外挂浏览器（`BROWSER_TYPE=cdp-connect`）。  
这个项目帮你**一键把CloakBrowser接入Skyvern**，没有任何侵入性改动。

---

## 快速开始

```bash
# 1. 克隆
git clone https://github.com/sevenliuhu/homo-skyvern-integration.git
cd homo-skyvern-integration

# 2. 一键配置
python3 homo_skyvern.py setup

# 3. 启动CloakBrowser
cloakbrowser --remote-debugging-port=9222

# 4. 启动Skyvern
skyvern run server
```

Skyvern会自动通过cdp-connect使用CloakBrowser。

---

## 原理

```
用户发指令 → Skyvern规划 → CloakBrowser执行(隐身) → 结果返回
                              ↓
                      Cloudflare? reCAPTCHA? 全通过
```

Skyvern通过 `BROWSER_TYPE=cdp-connect` 模式连接外部浏览器。  
我们在9222端口启动CloakBrowser，Skyvern自动发现并使用它。

**Skyvern代码一行不改，零侵入。**

---

## 前提条件

| 组件 | 安装方式 |
|:-----|:---------|
| Skyvern | `pip install skyvern` |
| CloakBrowser | `pip install cloakbrowser` 或启动HOMO Scraper |

---

## 免费版 vs Pro版

| 功能 | 免费版 | Pro版 |
|:-----|:-----:|:-----:|
| CloakBrowser集成 | ✅ | ✅ |
| 一键配置脚本 | ✅ | ✅ |
| **自动CloakBrowser管理** | ❌ | ✅ |
| **智能代理池轮换** | ❌ | ✅ |
| **浏览器指纹定制** | ❌ | ✅ |
| **审计日志** | ❌ | ✅ |

---

## 验证

```bash
python3 homo_skyvern.py check
```

---

## Credits

- [Skyvern](https://github.com/Skyvern-AI/skyvern) — AI浏览器自动化框架
- [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) — 隐身Chromium引擎

---

## 产品矩阵

| 项目 | 说明 |
|:-----|:------|
| [homo-cloaked-playwright](https://github.com/sevenliuhu/homo-cloaked-playwright) | Chromium隐身浏览器 |
| [homo-skyvern-integration](https://github.com/sevenliuhu/homo-skyvern-integration) | ⬅️ 当前项目 |
| [homo-native-feel-ext](https://github.com/sevenliuhu/homo-native-feel-ext) | 跨平台桌面设计扩展 |

---

## Business Contact

**HOMO AI Agent OS** — Not just an AI assistant, your entire AI team.

| Channel | Contact |
|:--------|:--------|
| Email | **16208204@qq.com** |

| GitHub | [sevenliuhu](https://github.com/sevenliuhu) |
| Services | Web Scraping, AI Agent Workflows, Web Dev, Brand Design, Short Video, Tech Solutions |

> For custom development or commercial license, contact us above. Response within 24h.
> This repository is for reference only. Commercial use requires a license.



---

## ⭐ Star 解锁专属工具

给本仓库点 Star，即可前往解锁页面获取独家数据/工具/模板：

👉 [**https://sevenliuhu.github.io/Homo-Ai/unlock.html**](https://sevenliuhu.github.io/Homo-Ai/unlock.html)

内容包括：A股量化模板 / 反爬指纹规则集 / 134技能索引 / 记忆系统配置 / 电商SKILL模板 / 中国风设计色板 等 12 份独家资源。
