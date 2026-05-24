#!/bin/bash
# Hexo 文档部署脚本
# 用法: ./deploy-doc.sh [选项] <源路径> <分类名>

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_info() {
    echo -e "${GREEN}[信息]${NC} $1"
}

print_warn() {
    echo -e "${YELLOW}[警告]${NC} $1"
}

print_error() {
    echo -e "${RED}[错误]${NC} $1"
}

# 显示帮助信息
show_help() {
    echo "Hexo 文档部署脚本"
    echo ""
    echo "用法:"
    echo "  $0 [选项] <源路径> <分类名>"
    echo ""
    echo "选项:"
    echo "  -d, --dir      导入整个目录"
    echo "  -D, --deploy   导入后自动部署"
    echo "  -h, --help     显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 article.md 技术文档"
    echo "  $0 --dir ./docs/项目笔记 项目笔记"
    echo "  $0 --deploy article.md 技术文档"
}

# 检查依赖
check_dependencies() {
    if ! command -v node &> /dev/null; then
        print_error "未找到 Node.js，请先安装"
        exit 1
    fi
    
    if ! command -v npx &> /dev/null; then
        print_error "未找到 npx，请先安装 Node.js"
        exit 1
    fi
    
    if [ ! -f "package.json" ]; then
        print_error "未找到 package.json，请在 Hexo 项目根目录运行此脚本"
        exit 1
    fi
}

# 导入单个文件
import_file() {
    local source_file=$1
    local category=$2
    
    if [ ! -f "$source_file" ]; then
        print_error "源文件不存在: $source_file"
        return 1
    fi
    
    # 创建分类目录
    local category_dir="docs/$category"
    mkdir -p "$category_dir"
    
    # 复制文件
    local filename=$(basename "$source_file")
    cp "$source_file" "$category_dir/"
    
    print_info "导入文件: $filename -> $category/"
    return 0
}

# 导入目录
import_directory() {
    local source_dir=$1
    local category=$2
    
    if [ ! -d "$source_dir" ]; then
        print_error "源目录不存在: $source_dir"
        return 1
    fi
    
    # 创建分类目录
    local category_dir="docs/$category"
    mkdir -p "$category_dir"
    
    # 复制所有 Markdown 文件
    local count=0
    for file in "$source_dir"/*.md; do
        if [ -f "$file" ]; then
            cp "$file" "$category_dir/"
            count=$((count + 1))
        fi
    done
    
    print_info "导入 $count 个文件到 $category/"
    return 0
}

# 重新构建博客
rebuild_blog() {
    print_info "清理缓存..."
    npx hexo clean
    
    print_info "生成静态文件..."
    npx hexo generate
    
    print_info "博客构建完成"
    return 0
}

# 部署博客
deploy_blog() {
    print_info "部署博客..."
    npx hexo deploy
    
    print_info "部署完成"
    return 0
}

# 主函数
main() {
    # 检查依赖
    check_dependencies
    
    # 解析参数
    local deploy=false
    local is_dir=false
    local source=""
    local category=""
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -d|--dir)
                is_dir=true
                shift
                ;;
            -D|--deploy)
                deploy=true
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                if [ -z "$source" ]; then
                    source=$1
                elif [ -z "$category" ]; then
                    category=$1
                else
                    print_error "未知参数: $1"
                    show_help
                    exit 1
                fi
                shift
                ;;
        esac
    done
    
    # 检查必需参数
    if [ -z "$source" ] || [ -z "$category" ]; then
        print_error "缺少必需参数"
        show_help
        exit 1
    fi
    
    # 执行导入
    if [ "$is_dir" = true ]; then
        import_directory "$source" "$category"
    else
        import_file "$source" "$category"
    fi
    
    # 重新构建
    rebuild_blog
    
    # 部署
    if [ "$deploy" = true ]; then
        deploy_blog
    fi
    
    print_info "操作完成！"
    
    if [ "$deploy" = false ]; then
        print_warn "未执行部署，如需部署请使用 --deploy 选项"
        print_info "本地预览: npx hexo server"
    fi
}

# 运行主函数
main "$@"