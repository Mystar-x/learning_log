from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic#根据模型Topic创建一个表单，该表单只包含字段text
        fields = ['text']
        labels = {'text': ''}#让Django不要为字段text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
#widget 是一个html表单元素，如单行文本框、多行文本区域或下拉列表。
#通过让Django使用forms.Textarea, 我们定制了字段'text'的输入小部件，将文本
#区域宽度设置为80，而非默认的40列