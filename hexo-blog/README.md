# .io 博客项目

这是一个基于 Hexo 的静态博客项目，部署在 GitHub Pages 上。

## 快速开始

### 安装依赖
```bash
npm install
```

### 本地预览
```bash
npx hexo server
```
访问 http://localhost:4000 查看效果。

### 生成静态文件
```bash
npx hexo generate
```

### 部署到 GitHub Pages
```bash
npx hexo deploy
```

## 文档管理

### 目录结构
```
docs/
├── 分类1/
│   ├── 文章1.md
│   └── 文章2.md
├── 分类2/
│   └── 文章3.md
└── 示例分类/
    ├── 欢迎来到我的博客.md
    └── Hexo 使用指南.md
```

### 添加新文章

1. 在 `docs/` 目录下创建或选择分类目录
2. 创建 Markdown 文件，包含以下 front-matter：

```yaml
---
title: 文章标题
date: YYYY-MM-DD HH:MM:SS
categories:
  - 分类名
tags:
  - 标签1
  - 标签2
---

文章内容...
```

### 使用部署脚本

项目提供了便捷的部署脚本 `deploy-doc.sh`：

```bash
# 导入单个文件到指定分类
./deploy-doc.sh article.md 技术文档

# 导入整个目录
./deploy-doc.sh --dir ./my-docs 项目笔记

# 导入并自动部署
./deploy-doc.sh --deploy article.md 技术文档
```

### 使用 Python 导入工具

```bash
# 导入单个文件
python .hermes/skills/import_to_hexo.py article.md 技术文档

# 导入目录
python .hermes/skills/import_to_hexo.py --dir ./my-docs 项目笔记

# 导入并部署
python .hermes/skills/import_to_hexo.py --deploy article.md 技术文档
```

## 配置说明

### 主配置文件
- `_config.yml`: Hexo 主配置
- `_config.hexo-theme-Klise-enhanced.yml`: 主题配置

### 修改博客信息
编辑 `_config.yml`：
```yaml
title: 你的博客标题
author: 作者名
language: zh-CN
url: https://你的域名.com/
```

### 修改导航菜单
编辑 `_config.hexo-theme-Klise-enhanced.yml`：
```yaml
menu:
  Home: / || 主页
  Tags: /tags/ || 标签
  categories: /categories/ || 分类
  Archives: /archives/ || 归档
  About: /about/ || 关于
```

## 项目结构

```
hexo-blog/
├── _config.yml                 # Hexo 配置
├── _config.hexo-theme-Klise-enhanced.yml  # 主题配置
├── docs/                       # 文章源文件
├── source/                     # 静态资源
├── themes/                     # 主题
│   └── hexo-theme-Klise-enhanced/
├── .hermes/                    # Hermes 记忆和技能
│   ├── PROJECT_MEMORY.md       # 项目记忆
│   ├── TODO_EVENTS.md          # 待办事项
│   └── skills/                 # 技能文件
├── deploy-doc.sh               # 部署脚本
└── package.json                # 依赖配置
```

## 常见问题

### Q: 如何添加新分类？
A: 在 `docs/` 目录下创建新文件夹，将文章放入其中即可。

### Q: 如何修改主题？
A: 编辑 `_config.hexo-theme-Klise-enhanced.yml` 文件。

### Q: 如何自定义域名？
A: 在 `source/` 目录下创建 `CNAME` 文件，写入你的域名。

### Q: 图片无法显示？
A: 将图片放在文章同级目录，使用相对路径 `./image.png` 引用。

## 部署到 GitHub Pages

1. 在 GitHub 上创建仓库 `username.github.io`
2. 将项目推送到仓库
3. 在仓库设置中启用 GitHub Pages
4. 选择 `gh-pages` 分支作为源

## 自动化部署

项目包含 GitHub Actions 配置，可实现自动部署：

1. 推送代码到 `main` 分支
2. GitHub Actions 自动构建
3. 自动部署到 `gh-pages` 分支

## 技能文件

项目在 `.hermes/skills/` 目录下提供了以下技能：

- `hexo-doc-deploy.md`: 文档部署指南
- `import_to_hexo.py`: Python 导入工具

## 记忆文件

- `.hermes/PROJECT_MEMORY.md`: 项目基本信息和配置
- `.hermes/TODO_EVENTS.md`: 待办事项和事件日志

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License