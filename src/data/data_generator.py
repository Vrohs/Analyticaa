import json
import random
from datetime import datetime, timedelta

def generate_engagement_data(num_posts=500):
    post_types = ['reels', 'carousel', 'static_image']
    post_type_weights = [0.4, 0.3, 0.3]
    
    engagement_ranges = {
        'reels': (7.0, 19.0),
        'carousel': (8.0, 14.0),
        'static_image': (4.0, 12.0)
    }
    
    reach_ranges = {
        'reels': (9000, 23000),
        'carousel': (12000, 25000),
        'static_image': (9000, 20000)
    }
    
    posts = []
    base_time = datetime.now()
    
    for post_id in range(1, num_posts + 1):
        hours_back = random.randint(0, 24 * 7)
        timestamp = base_time - timedelta(hours=hours_back)
        
        post_type = random.choices(post_types, weights=post_type_weights)[0]
        
        reach = random.randint(*reach_ranges[post_type])
        
        engagement_rate = round(random.uniform(*engagement_ranges[post_type]), 2)
        
        total_engagements = int(reach * (engagement_rate / 100))
        likes = int(total_engagements * random.uniform(0.65, 0.75))
        shares = int(total_engagements * random.uniform(0.15, 0.25))
        comments = total_engagements - likes - shares
        
        post = {
            "post_id": post_id,
            "post_type": post_type,
            "likes": likes,
            "shares": shares,
            "comments": comments,
            "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "reach": reach,
            "engagement_rate": engagement_rate
        }
        
        if post_type == 'carousel':
            post.update({
                "slides": random.randint(3, 10),
                "avg_slide_time": round(random.uniform(2.8, 4.5), 1)
            })
        elif post_type == 'reels':
            post.update({
                "video_duration": random.randint(15, 60),
                "completion_rate": round(random.uniform(65.0, 85.0), 1)
            })
        else:
            post.update({
                "image_type": random.choice(['photo', 'graphic', 'infographic']),
                "has_caption": random.choice([True, False])
            })
        
        posts.append(post)
    
    posts.sort(key=lambda x: x['timestamp'], reverse=True)
    
    output_lines = ['  "posts": [']
    
    for i, post in enumerate(posts):
        post_lines = json.dumps(post, indent=6).split('\n')
        formatted_lines = [('    ' + line if line.strip() else line) for line in post_lines]
        post_string = '\n'.join(formatted_lines)
        
        if i < len(posts) - 1:
            post_string += ','
        
        output_lines.append(post_string)
    
    output_lines.append('  ]')
    
    return '{\n' + '\n'.join(output_lines) + '\n}'

if __name__ == "__main__":
    print(generate_engagement_data(100))