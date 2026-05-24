# Hexo 文档部署技能

## 概述
将 Markdown 文档转换并部署到 Hexo 博客的指定分栏中。

## 使用场景
- 将技术文档、笔记、教程等内容部署到博客
- 按分类组织内容到不同分栏
- 自动化文档发布流程

## 操作步骤

### 1. 准备 Markdown 文档

确保文档包含完整的 YAML front-matter：

```yaml
---
title: 文档标题
date: YYYY-MM-DD HH:MM:SS
categories:
  - 主分类
  - 子分类 (可选)
tags:
  - 标签1
  - 标签2
---
```

### 2. 文档分类组织

将文档放入对应的分类目录：

```
docs/
├── 技术文档/
│   ├── Python 教程.md
│   └── JavaScript 基础.md
├── 项目笔记/
│   ├── 项目A 笔记.md
│   └── 项目B 笔记.md
└── 学习资料/
    └── 算法笔记.md
```

### 3. 部署到指定分栏

#### 方法一：手动放置
1. 将 Markdown 文件复制到 `docs/分类名/` 目录
2. 运行 `npx hexo generate` 生成静态文件
3. 运行 `npx hexo deploy` 部署

#### 方法二：使用脚本自动化
创建部署脚本 `deploy-doc.sh`：

```bash
#!/bin/bash
# 用法: ./deploy-doc.sh <md文件> <分类名>

if [ $# -ne 2 ]; then
    echo "用法: $0 <md文件> <分类名>"
    exit 1
fi

MD_FILE=$1
CATEGORY=$2
DEST_DIR="docs/$CATEGORY"

# 创建分类目录
mkdir -p "$DEST_DIR"

# 复制文件
cp "$MD_FILE" "$DEST_DIR/"

# 生成并部署
npx hexo clean
npx hexo generate
npx hexo deploy

echo "文档已部署到分类: $CATEGORY"
```

### 4. 配置导航栏分栏

编辑 `_config.hexo-theme-Klise-enhanced.yml` 添加新分栏：

```yaml
menu:
  Home: / || 主页
  Tags: /tags/ || 笔记
  categories: /categories/ || 类别
  Archives: /archives/ || 档案馆
  技术文档: /categories/技术文档/ || 技术文档
  项目笔记: /categories/项目笔记/ || 项目笔记
  About: /about/ || 关于我
```

### 5. 批量导入文档

使用脚本批量导入多个文档：

```python
#!/usr/bin/env python3
import os
import shutil
import subprocess

def import_docs(source_dir, category):
    """批量导入文档到指定分类"""
    dest_dir = f"docs/{category}"
    os.makedirs(dest_dir, exist_ok=True)
    
    for filename in os.listdir(source_dir):
        if filename.endswith('.md'):
            src = os.path.join(source_dir, filename)
            dst = os.path.join(dest_dir, filename)
            shutil.copy2(src, dst)
            print(f"导入: {filename}")
    
    # 重新生成
    subprocess.run(['npx', 'hexo', 'clean'])
    subprocess.run(['npx', 'hexo', 'generate'])
    subprocess.run(['npx', 'hexo', 'deploy'])

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("用法: python import_docs.py <源目录> <分类名>")
        sys.exit(1)
    
    import_docs(sys.argv[1], sys.argv[2])
```

## 验证部署

1. 本地预览：`npx hexo server`
2. 访问 http://localhost:4000 查看效果
3. 检查分类页面是否正确显示
4. 验证文章内容格式正确

## 常见问题

### Q: 文章没有显示在分类页面？
A: 检查 front-matter 中的 categories 字段是否正确。

### Q: 如何修改文章在导航栏的位置？
A: 编辑 `_config.hexo-theme-Klise-enhanced.yml` 中的 menu 配置。

### Q: 如何添加自定义页面？
A: 运行 `npx hexo new page "页面名"` 创建独立页面。

### Q: 图片无法显示？
A: 将图片放在文章同级目录，使用相对路径引用。

## 高级功能

### 自动化部署脚本
创建 GitHub Actions 工作流实现自动部署：

```yaml
# .github/workflows/deploy.yml
name: Deploy Hexo Blog
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '16'
      - run: npm install
      - run: npx hexo generate
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

### 文档监控脚本
监控目录变化自动部署：

```bash
#!/bin/bash
# watch-deploy.sh
inotifywait -m -r -e create,modify,delete docs/ |
while read path action file; do
    if [[ "$file" == *.md ]]; then
        echo "检测到文档变化: $file"
        npx hexo clean
        npx hexo generate
        npx hexo deploy
    fi
done
```

## 注意事项

1. 文档文件名建议使用英文或拼音，避免中文路径问题
2. 图片等静态资源建议放在 `source/` 目录下
3. 大型文档建议拆分为多个小文件
4. 定期备份 `docs/` 目录