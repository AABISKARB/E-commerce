from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
#    from django.contrib.contenttypes.fields import 

class Comment(models.Model):
    text = models.TextField()



class Post(models.Model):
    name = models.TextField()

class Video(models.Model):
    name = models.TextField()

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # post_id = models.ForeignKey(Post)
    # video_id = models.ForeignKey(Video, null=True)
    # content_object = GenericForeignKey()



# post_content_type = ContentType.objects.get(model="Post")
# # LikedItem.objects.create(user="", content_type=post_content_type, object_id=1)
# LikedItem.objects.create(user="", post_id=1)


# video_content_type = ContentType.objects.get(model="Video")
# # LikedItem.objects.create(user="", content_type=video_content_type, object_id=10)
# LikedItem.objects.create(user="", video_id=10)


# Post.objects.get(id=1)

"""
Content Type
Row 1: app_label = contrib, model=User
Row 2: app_label = likes, model=Comment
Row 3: app_label = likes, model=LikedItem
ROw 4: app_label = likes, model=Post
Row 5: app_label = liked, model=Video
"""