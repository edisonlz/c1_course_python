
1) 新式类(new-style class)
新式类除了拥有经典类的全部特性之外，还有一些新的特性
比如:新增了静态方法__new__


__new__和__init__的区别
__new__是一个静态方法,而__init__是一个实例方法.


class A(object):

    def __init__(self,name):
        print("int __init__:%s" % name)
        self.name = name

    def __new__(cls, *args, **kw):
        print("before new")
        orig = super(A, cls)
        instance = orig.__new__(cls)
        print("after new")
        return instance

        



2）单例
class Singleton(object):


    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
            print("init instance")
        return cls._instance



class Me(Singleton):
    name = "ed"

me1 = Me()
me2 = Me()



