#!/usr/bin/env python3
"""
抖音评论监控核心逻辑
功能：实现评论抓取、筛选和监控
"""

import time
import random
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import MONITOR_CONFIG

class DouyinCommentMonitor:
    """抖音评论监控器"""
    
    def __init__(self):
        self.driver = None
        self.setup_driver()
        self.found_comments = []
    
    def setup_driver(self):
        """配置浏览器驱动"""
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        
        # 移动端模拟
        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15"
        }
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        try:
            self.driver = webdriver.Chrome(options=options)
        except Exception as e:
            print(f"浏览器启动失败: {e}")
            # 模拟模式继续运行
            self.driver = None
    
    def is_recent_comment(self, time_text):
        """判断是否为近期评论"""
        if not time_text:
            return False
        time_text = time_text.strip()
        return '刚刚' in time_text or '1分钟前' in time_text or '2分钟前' in time_text
    
    def is_low_like_comment(self, likes):
        """判断是否为低赞评论"""
        return likes <= MONITOR_CONFIG['max_likes']
    
    def simulate_comment_check(self):
        """模拟评论检查（实际使用需替换为真实逻辑）"""
        # 生成模拟评论数据
        comments = []
        comment_templates = [
            {"user": "用户A", "content": "这个视频很棒！", "time": "刚刚", "likes": 2},
            {"user": "用户B", "content": "点赞支持！", "time": "1分钟前", "likes": 0},
            {"user": "用户C", "content": "期待更新", "time": "5分钟前", "likes": 10}
        ]
        
        # 随机选择1-2条评论
        num_comments = random.randint(1, 2)
        for i in range(num_comments):
            comment = random.choice(comment_templates).copy()
            comment['id'] = f"comment_{int(time.time())}_{i}"
            comments.append(comment)
        
        return comments
    
    def check_comments(self, video_url):
        """检查评论（模拟实现）"""
        if self.driver:
            # 真实浏览器检查逻辑
            try:
                self.driver.get(video_url)
                time.sleep(3)
                # 实际评论提取逻辑应在此实现
                return self.simulate_comment_check()
            except Exception as e:
                print(f"浏览器检查失败: {e}")
                return self.simulate_comment_check()
        else:
            # 模拟模式
            return self.simulate_comment_check()
    
    def process_comments(self, comments):
        """处理评论数据"""
        new_comments = []
        for comment in comments:
            if (self.is_recent_comment(comment['time']) and 
                self.is_low_like_comment(comment['likes'])):
                
                # 检查是否已存在
                if not any(c['id'] == comment['id'] for c in self.found_comments):
                    comment['timestamp'] = datetime.now().strftime('%H:%M:%S')
                    new_comments.append(comment)
                    self.found_comments.append(comment)
        
        return new_comments
    
    def start_monitoring(self, video_url, duration_minutes=5, check_interval=30):
        """开始监控"""
        print(f"开始监控，时长: {duration_minutes}分钟")
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        check_count = 0
        
        try:
            while time.time() < end_time:
                check_count += 1
                print(f"\n第{check_count}次检查...")
                
                # 检查评论
                comments = self.check_comments(video_url)
                new_comments = self.process_comments(comments)
                
                if new_comments:
                    print(f"发现{len(new_comments)}条新评论:")
                    for comment in new_comments:
                        print(f"  👤 {comment['user']}: {comment['content']}")
                        print(f"     ⏰ {comment['time']} | ❤️ {comment['likes']}赞")
                else:
                    print("暂无新评论")
                
                # 等待下次检查
                wait_time = min(check_interval, end_time - time.time())
                if wait_time <= 0:
                    break
                    
                print(f"下次检查: {wait_time}秒后")
                time.sleep(wait_time)
                
        except KeyboardInterrupt:
            print("监控被用户中断")
        finally:
            if self.driver:
                self.driver.quit()
            print(f"监控结束，共发现{len(self.found_comments)}条目标评论")

# 测试函数
def test_monitor():
    """测试监控器"""
    monitor = DouyinCommentMonitor()
    test_comments = monitor.simulate_comment_check()
    print("测试评论:", test_comments)
    
    # 测试处理逻辑
    processed = monitor.process_comments(test_comments)
    print("处理后的评论:", processed)

if __name__ == "__main__":
    test_monitor()
