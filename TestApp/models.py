#coding:utf-8
#
from django.db import models
from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import *

def getImagePath(model_instance=None):
    if model_instance is None:
        return "aaa/"
    else:
        return "%s/" % model_instance.Name

def getDescImagePath(model_instance=None):
        return "aaa/"

class myBtn(UEditorButtonCommand):
    def onClick(self):
        return u"""
            alert("爽!");
            editor.execCommand(uiName);
        """
    def onExecuteAjaxCommand(self,state):
        if state=="success":
            return u"""
                alert("后面比较爽!"+xhr.responseText);
            """
        if state=="error":
            return u"""
                alert("讨厌，摸哪里去了！"+xhr.responseText);
            """
class myCombo(UEditorComboCommand):
    def onSelect(self):
        return u"""
            alert("选择了!");
        """
    def get_items(self):
        items=[]
        for i in xrange(10):
            items.append({
                "label":"combo_%s" % i,
                "value":i
            })
        return items

class Blog(models.Model):
    Name = models.CharField(u'姓名', max_length=100, blank=True)
    Description = UEditorField(u'描述', blank=True, toolbars="full", imagePath="cool/", settings={"a": 1},
                               command=[myBtn(uiName="mybtn1", icon="d.png", title=u"1摸我", ajax_url="/ajaxcmd/"),
                                        myBtn(uiName="mybtn2",index=22, icon="d.png", title=u"2摸我", ajax_url="/ajaxcmd/"),
                                        myCombo(uiName="myCombo3",title=u"ccc",initValue="aaa")
                                        ])
    ImagePath = models.CharField(u'图片目录', max_length=100, blank=True)
    Content = UEditorField(u'内容', height=200, width=500, default='test', imagePath=getImagePath, toolbars="mini",
                           filePath='bb/', blank=True, settings={"a": 2})

