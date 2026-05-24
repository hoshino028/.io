---
title: Hexo 使用指南
date: 2026-05-24 11:00:00
categories:
  - 示例分类
tags:
  - Hexo
  - 教程
---

# Hexo 使用指南

本指南介绍如何使用 Hexo 创建和管理博客内容。

## 文章结构

每篇文章都放在 `docs/` 目录下，按分类组织：

```
docs/
├── 分类1/
│   ├── 文章1.md
│   └── 文章2.md
├── 分类2/
│   └── 文章3.md
└── 示例分类/
    └── 欢迎来到我的博客.md
```

## Front-matter 配置

文章头部使用 YAML 格式的 front-matter：

```yaml
---
title: 文章标题
date: 2026-05-24 10:00:00
categories:
  - 主分类
  - 子分类
tags:
  - 标签1
  - 标签2
---
```

## 常用命令

### 创建新文章

```bash
npx hexo new "文章标题"
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

生成的文件在 `public/` 目录下。

### 部署到 GitHub Pages

```bash
npx hexo deploy
```

## 高级功能

### 自定义页面

创建独立页面（如"关于"页面）：

```bash
npx hexo new page "about"
```

### 插件扩展

Hexo 有丰富的插件生态系统：

- `hexo-generator-search`: 搜索功能
- `hexo-generator-feed`: RSS 订阅
- `hexo-wordcount`: 字数统计

### 主题定制

修改 `_config.hexo-theme-Klise-enhanced.yml` 文件来自定义主题。

## 最佳实践

1. **保持目录结构清晰**: 按主题分类文章
2. **使用标签系统**: 便于文章发现和关联
3. **定期备份**: 使用 Git 管理源文件
4. **优化图片**: 压缩图片提高加载速度

## 常见问题

### Q: 如何修改博客标题？
A: 编辑 `_config.yml` 中的 `title` 字段。

### Q: 如何添加新分类？
A: 在文章的 front-matter 中添加 `categories` 字段。

### Q: 如何自定义域名？
A: 在 `source/` 目录下创建 `CNAME` 文件，写入你的域名。

---

*更多 Hexo 使用技巧，请参考 [官方文档](https://hexo.io/zh-cn/docs/)*