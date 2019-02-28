from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, 'on_delete')#在topic中添加了owner，建立到模型User的外键关系

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
 
class Entry(models.Model):#继承了Django基类Model
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#这个topic为ForeigKey的实例
    text = models.TextField()#外键是数据库术语，他引用了数据库中的另一条记录
    date_added = models.DateTimeField(auto_now_add=True)
#这些代码将每个条目关联到特定的主题，每个主题创建时，都给它分配了一个键，需要
#在两项数据之间建立联系时，Django使用与每项信息相关联的键
#text是一个TextField实例，没有设置长度限制
#属性date_added使得呈现条目按照创建顺序，并在每个条目旁边放置时间戳
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """返回模型的字符串表示"""
        if len(str(self.text)) > 50:
            return  str(self.text)[:50] + "..."
        else:
            return str(self.text)
#嵌套Meta类，存储用于管理模块的额外信息，它让我们能够设置一个特殊属性，让Django
#在需要时，使用Entries来表示多个条目。如果没有这个类，将使用Entrys来表示多个条目
#__str__()函数设置呈现条目应显示哪些信息，只显示了前50个字符，并加上了省略号