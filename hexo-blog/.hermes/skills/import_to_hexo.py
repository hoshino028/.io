#!/usr/bin/env python3
"""
Hexo 文档导入工具
将 Markdown 文档导入到 Hexo 博客的指定分类中
"""

import os
import sys
import shutil
import subprocess
import re
from datetime import datetime
from pathlib import Path


def ensure_front_matter(content: str, title: str, category: str) -> str:
    """确保文档包含正确的 front-matter"""
    
    # 检查是否已有 front-matter
    if content.startswith('---'):
        # 已有 front-matter，检查并更新分类
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter = parts[1]
            rest_content = parts[2]
            
            # 更新或添加 categories
            if 'categories:' in front_matter:
                # 替换现有分类
                front_matter = re.sub(
                    r'categories:.*?(?=\n\w|\n---)',
                    f'categories:\n  - {category}',
                    front_matter,
                    flags=re.DOTALL
                )
            else:
                # 添加分类
                front_matter = front_matter.rstrip() + f'\ncategories:\n  - {category}\n'
            
            return f'---{front_matter}---{rest_content}'
    
    # 没有 front-matter，创建新的
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    front_matter = f"""---
title: {title}
date: {now}
categories:
  - {category}
tags: []
---

"""
    return front_matter + content


def import_document(source_file: str, category: str, docs_dir: str = 'docs') -> bool:
    """
    导入单个文档到指定分类
    
    Args:
        source_file: 源文件路径
        category: 分类名称
        docs_dir: 文档目录路径
    
    Returns:
        bool: 是否成功
    """
    try:
        # 检查源文件
        if not os.path.exists(source_file):
            print(f"错误: 源文件不存在: {source_file}")
            return False
        
        # 创建分类目录
        category_dir = os.path.join(docs_dir, category)
        os.makedirs(category_dir, exist_ok=True)
        
        # 读取源文件
        with open(source_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 获取文件名和标题
        filename = os.path.basename(source_file)
        title = os.path.splitext(filename)[0]
        
        # 确保 front-matter 正确
        content = ensure_front_matter(content, title, category)
        
        # 写入目标文件
        dest_file = os.path.join(category_dir, filename)
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"成功导入: {filename} -> {category}/")
        return True
        
    except Exception as e:
        print(f"导入失败: {e}")
        return False


def import_directory(source_dir: str, category: str, docs_dir: str = 'docs') -> int:
    """
    批量导入目录中的所有 Markdown 文件
    
    Args:
        source_dir: 源目录路径
        category: 分类名称
        docs_dir: 文档目录路径
    
    Returns:
        int: 成功导入的文件数量
    """
    if not os.path.isdir(source_dir):
        print(f"错误: 源目录不存在: {source_dir}")
        return 0
    
    success_count = 0
    for filename in os.listdir(source_dir):
        if filename.endswith('.md'):
            source_file = os.path.join(source_dir, filename)
            if import_document(source_file, category, docs_dir):
                success_count += 1
    
    return success_count


def rebuild_blog() -> bool:
    """重新构建博客"""
    try:
        print("清理缓存...")
        subprocess.run(['npx', 'hexo', 'clean'], check=True)
        
        print("生成静态文件...")
        subprocess.run(['npx', 'hexo', 'generate'], check=True)
        
        print("博客构建完成")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"构建失败: {e}")
        return False


def deploy_blog() -> bool:
    """部署博客"""
    try:
        print("部署博客...")
        subprocess.run(['npx', 'hexo', 'deploy'], check=True)
        
        print("部署完成")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"部署失败: {e}")
        return False


def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("用法:")
        print("  导入单个文件: python import_to_hexo.py <文件路径> <分类名>")
        print("  导入目录:     python import_to_hexo.py --dir <目录路径> <分类名>")
        print("  导入并部署:   python import_to_hexo.py --deploy <文件路径> <分类名>")
        sys.exit(1)
    
    # 解析参数
    deploy = False
    is_dir = False
    args = sys.argv[1:]
    
    if '--deploy' in args:
        deploy = True
        args.remove('--deploy')
    
    if '--dir' in args:
        is_dir = True
        args.remove('--dir')
    
    if len(args) != 2:
        print("错误: 需要提供源路径和分类名")
        sys.exit(1)
    
    source = args[0]
    category = args[1]
    
    # 执行导入
    if is_dir:
        count = import_directory(source, category)
        print(f"共导入 {count} 个文件")
    else:
        if import_document(source, category):
            print("导入完成")
        else:
            sys.exit(1)
    
    # 重新构建
    if not rebuild_blog():
        sys.exit(1)
    
    # 部署
    if deploy:
        if not deploy_blog():
            sys.exit(1)
    
    print("\n操作完成！")


if __name__ == '__main__':
    main()