
1.类的定义

class 类名(父类):

    def 方法():
        pass


class User:

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        #user
        return "Repr:User:%s" % self.username

    def __str__(self):
        #print user
        return "Print:User:%s" %self.username

    def buy_car(self,car):
        self.car = car

    @property
    def show_car(self):
        return "user %s  has car %s" % (self.username,self.car.carname)

    @classmethod
    def create_user(cls,username):
        user = cls(username=username)
        return user




class Car:

    def __init__(self,carname):
        self.carname = carname

    def drive(self):
        print("car is run")
    
    def stop(self):
        print('car is stop')






4.继承  super调用父类方法
class A:
    def __init__(self,x):
        self.x = x


class B(A):
    
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y






方法解析顺序 (MRO) 列表
class C(B):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.z = 1


 C.__mro__

 

