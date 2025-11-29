#!/usr/bin/env python3
"""
抖音评论监控系统配置
功能：存储常量和配置参数
"""

# 监控配置
MONITOR_CONFIG = {
    'max_minutes_ago': 2,      # 只监控2分钟内的评论
    'max_likes': 5,           # 最大点赞数限制
    'default_check_interval': 30,  # 默认检查间隔(秒)
    'max_comments_store': 100,    # 最大存储评论数
}

# 日志配置
LOGGING_CONFIG = {
    'level': 'INFO',          # 日志级别
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'douyin_monitor.log'  # 日志文件
}

# 浏览器配置
BROWSER_CONFIG = {
    'headless': False,        # 是否无头模式
    'timeout': 30,            # 超时时间(秒)
    'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15'
}

# 时间模式匹配
TIME_PATTERNS = [
    r'刚刚',
    r'(\d+)\s*分钟前',
    r'(\d+)\s*分钟',
    r'今天',
    r'刚刚发布'
]

# 测试数据
TEST_COMMENTS = [
    {
        'user': '测试用户1',
        'content': '这个视频内容很棒！',
        'time': '刚刚',
        'likes': 2,
        'id': 'test_1'
    },
    {
        'user': '测试用户2', 
        'content': '点赞支持作者！',
        'time': '1分钟前',
        'likes': 0,
        'id': 'test_2'
    }
]

def validate_config():
    """验证配置有效性"""
    errors = []
    
    if MONITOR_CONFIG['max_minutes_ago'] <= 0:
        errors.append('max_minutes_ago必须大于0')
    
    if MONITOR_CONFIG['max_likes'] < 0:
        errors.append('max_likes不能为负数')
    
    if MONITOR_CONFIG['default_check_interval'] < 10:
        errors.append('检查间隔不能小于10秒')
    
    return errors

# 配置验证
if __name__ == "__main__":
    errors = validate_config()
    if errors:
        print("配置错误:", errors)
    else:
        print("配置验证通过")
        print("MONITOR_CONFIG:", MONITOR_CONFIG)
        print("LOGGING_CONFIG:", LOGGING_CONFIG)
