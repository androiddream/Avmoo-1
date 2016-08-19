from django.db import models

# Create your models here.


class avmoo_api(models.Model):
    #标题
    titlie = models.CharField(max_length=999)
    #封面大小图片
    #小
    indeximg = models.CharField(max_length=999)
    #大
    titileimg = models.CharField(max_length=999)
    
    #详细信息
    #番号
    fanhao = models.CharField(max_length=100)
    #发行时间
    faxingshijian = models.CharField(max_length=100)
    #影片长度
    yingpianchangdu = models.CharField(max_length=100)
    #制造商
    zhizaoshang = models.CharField(max_length=100)
    #发行商
    faxingshang = models.CharField(max_length=100)
    #系列
    xilie = models.CharField(max_length=100)
    #类别
    leibie = models.CharField(max_length=100)
    
    #老师
    artists = models.CharField(max_length=100)
    #老师照片
    artistsimg = models.CharField(max_length=999)
    
    #预览大小图
    #小
    simpleimg = models.CharField(max_length=9999)
    #大
    bigsimpleimg = models.CharField(max_length=9999)

    def __str__(self):
        return str(self.indeximg) + str(self.titileimg) + str(self.fanhao) + str(self.faxingshijian) + str(
            self.yingpianchangdu) + str(self.zhizaoshang) + str(self.faxingshang) + str(self.xilie) + str(
                self.leibie) + str(self.Artists) + str(self.simpleimg) + str(self.bigsimpleimg) + str(
                    self.Artistsimg) + str(titlie) 

class teacher(models.Model):
    teacher = models.CharField(max_length=100)

    def __str__():
        return str(self.teacher)