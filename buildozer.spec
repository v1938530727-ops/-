[app]

# 应用标题和包名
title = 抖音评论监控
package.name = douyinmonitor
package.domain = org.douyin

# 源码目录
source.dir = .

# 主程序入口文件
source.include_exts = py,png,jpg,kv,atlas
main = main.py

# 版本信息
version = 1.0

# 依赖包
requirements = python3,kivy,requests,ssl,openssl

# Android配置
osx.python_version = 3
osx.kivy_version = 2.1.0

# 权限配置
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# API级别
android.api = 30
android.minapi = 21
android.sdk = 23
android.ndk = 25.1.8937393

# 架构
android.arch = armeabi-v7a

# 图标和启动画面
presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

# 应用配置
fullscreen = 0
orientation = portrait

# 调试模式
log_level = 2

# 排除文件模式
source.exclude_exts = .pyc,.pyo,.git,.gitignore

[buildozer]
# 构建配置
warn_on_root = 1
