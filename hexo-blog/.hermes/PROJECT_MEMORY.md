# .io 项目记忆

## 项目概述
这是一个 Hexo 静态博客项目，部署在 GitHub Pages 上，用于展示技术文档和个人笔记。

## 技术栈
- Hexo 8.1.1
- 主题: hexo-theme-Klise-enhanced
- 渲染器: hexo-renderer-ejs, hexo-renderer-stylus, hexo-renderer-markdown-it-plus
- 部署: GitHub Pages

## 目录结构
```
hexo-blog/
├── _config.yml                 # Hexo 主配置
├── _config.hexo-theme-Klise-enhanced.yml  # 主题配置
├── docs/                       # 文章源文件目录 (source_dir)
├── source/                     # 静态资源
├── themes/                     # 主题目录
│   └── hexo-theme-Klise-enhanced/
├── .hermes/                    # Hermes 记忆和技能
│   ├── PROJECT_MEMORY.md       # 本文件
│   ├── TODO_EVENTS.md          # 待办事件队列
│   └── skills/                 # 技能文件
│       ├── hexo-doc-deploy.md  # 文档部署技能
│       └── import_to_hexo.py   # Python 导入工具
├── .github/workflows/deploy.yml # GitHub Actions
├── deploy-doc.sh               # 部署脚本
└── scaffolds/                  # 文章模板
```

## 常用命令
```bash
# 安装依赖
npm install

# 本地预览
npx hexo server

# 生成静态文件
npx hexo generate

# 清理缓存
npx hexo clean

# 部署 (需配置 deploy 部分)
npx hexo deploy
```

## 文章组织规范
- 文章存放在 docs/ 目录下
- 按分类创建子目录，如: docs/决策树/Behavior Tree/
- 每篇文章需要 YAML front-matter 头部
- 支持 Markdown 语法，包括数学公式、代码高亮等

## 配置要点
- url: http://hoshino.fun/
- permalink: :year/:month/:day/:title/
- language: zh-CN
- 主题: hexo-theme-Klise-enhanced

## 文档导入工具
项目提供了完整的文档导入工具链：

### 部署脚本 (deploy-doc.sh)
```bash
# 导入单个文件
./deploy-doc.sh article.md 技术文档

# 导入目录
./deploy-doc.sh --dir ./docs 项目笔记

# 导入并部署
./deploy-doc.sh --deploy article.md 技术文档
```

### Python 导入工具
```bash
# 导入单个文件
python .hermes/skills/import_to_hexo.py article.md 技术文档

# 导入目录
python .hermes/skills/import_to_hexo.py --dir ./docs 项目笔记

# 导入并部署
python .hermes/skills/import_to_hexo.py --deploy article.md 技术文档
```

## 自动化部署
- GitHub Actions 配置在 `.github/workflows/deploy.yml`
- 推送到 main 分支自动触发构建和部署
- 部署到 gh-pages 分支

## 待完成事项
1. 完善主题配置，确保正常显示
2. 优化文档结构，设计分类体系
3. 添加更多示例内容
4. 配置自定义域名（如需要）

## 注意事项
- 主题配置文件为 _config.hexo-theme-Klise-enhanced.yml
- 文章分类通过目录结构实现
- 图片等静态资源放在文章同级目录或 source/ 下
- 修改配置后需要重新生成静态文件

## 更新日志
- 2026-05-24: 项目初始化，创建记忆文件体系
- 2026-05-24: 安装依赖，验证构建流程
- 2026-05-24: 创建文档导入工具和部署脚本
- 2026-05-24: 配置 GitHub Actions 自动部署