#!/usr/bin/env python3
"""
抖音评论监控系统 - 简化版本
"""

import time
import random
from datetime import datetime

class DouyinMonitor:
    """抖音评论监控器"""
    
    def __init__(self):
        self.found_comments = []
        self.monitoring = False
    
    def start_monitoring(self, video_url, duration_minutes=5, check_interval=30):
        """开始监控"""
        print("🚀 抖音评论监控系统启动")
        print(f"📹 监控视频: {video_url}")
        print(f"⏰ 时长: {duration_minutes}分钟")
        print(f"🔄 间隔: {check_interval}秒")
        
        self.monitoring = True
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        check_count = 0
        
        try:
            while time.time() < end_time and self.monitoring:
                check_count += 1
                print(f"\n📊 第{check_count}次检查...")
                
                # 模拟评论检查
                comments = self.simulate_comment_check()
                new_comments = self.process_comments(comments)
                
                if new_comments:
                    print(f"🎉 发现{len(new_comments)}条新评论:")
                    for comment in new_comments:
                        print(f"   👤 {comment['user']}: {comment['content']}")
                        print(f"      ⏰ {comment['time']} | ❤️ {comment['likes']}赞")
                else:
                    print("⏳ 暂无新评论")
                
                # 等待下次检查
                wait_time = min(check_interval, end_time - time.time())
                if wait_time > 0:
                    time.sleep(wait_time)
                else:
                    break
                    
        except KeyboardInterrupt:
            print("\n⏹️ 监控被用户中断")
        finally:
            self.monitoring = False
            print(f"\n👋 监控结束，共发现{len(self.found_comments)}条目标评论")
    
    def simulate_comment_check(self):
        """模拟评论检查"""
        comments = []
        # 30%概率发现新评论
        if random.random() < 0.3:
            sample_comments = [
                {"user": "用户A", "content": "视频很棒！", "time": "刚刚", "likes": 2, "id": f"comment_{int(time.time())}_1"},
                {"user": "用户B", "content": "点赞支持", "time": "1分钟前", "likes": 0, "id": f"comment_{int(time.time())}_2"},
                {"user": "用户C", "content": "期待更新", "time": "2分钟前", "likes": 1, "id": f"comment_{int(time.time())}_3"}
            ]
            # 随机选择1-2条评论
            num_comments = random.randint(1, 2)
            for i in range(num_comments):
                comment = random.choice(sample_comments).copy()
                comment['id'] = f"comment_{int(time.time())}_{i}"
                comments.append(comment)
        
        return comments
    
    def process_comments(self, comments):
        """处理评论"""
        new_comments = []
        for comment in comments:
            # 筛选2分钟内0-5赞的评论
            if self.is_recent_comment(comment['time']) and comment['likes'] <= 5:
                if not any(c['id'] == comment['id'] for c in self.found_comments):
                    comment['timestamp'] = datetime.now().strftime('%H:%M:%S')
                    new_comments.append(comment)
                    self.found_comments.append(comment)
        
        return new_comments
    
    def is_recent_comment(self, time_text):
        """判断是否为近期评论"""
        return time_text in ['刚刚', '1分钟前', '2分钟前']
    
    def stop_monitoring(self):
        """停止监控"""
        self.monitoring = False

def main():
    """主函数"""
    print("=" * 50)
    print("🤖 抖音评论监控系统 v1.0")
    print("=" * 50)
    
    monitor = DouyinMonitor()
    
    # 使用测试配置
    video_url = "https://v.douyin.com/example/"
    duration_minutes = 2  # 测试时长2分钟
    check_interval = 10   # 10秒检查一次
    
    try:
        monitor.start_monitoring(video_url, duration_minutes, check_interval)
    except Exception as e:
        print(f"❌ 程序出错: {e}")

if __name__ == "__main__":
    main()
