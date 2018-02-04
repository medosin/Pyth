import re;
class person:
    def __init__(self,name):
        self.name=name;
        self.money=0;
        self.mood='';
        self.healthrate=0;
    def sleep(self,hours):
        if hours == 7:
            mood='happy';
        elif hours < 7:
            mood='tired';
        elif hours > 7:
            mood='lazy';
        return mood;
    def eat(self,meal):
        if meal==3:
            self.healthrate=100;
        elif meal==2:
            self.healthrate=75;
        elif meal==1:
            self.healthrate=50;
        return self.healthrate;
    def buy(self,items):
        for i in range(int(items)):
            money-=10;
        return money;
class car:
    name='';
    def __init__(self,name):
        self.name=name;
        self.__velocity=0;
        self.__fuelrate=0
    def run(self,velocity,distance):
        self.__velocity=velocity;
        for i in range(0,distance+1):
            distance-=1;
            if(distance%10==0):
                self.__fuelrate-=((10/100)*100);
            if(distance<=0):
                self.stop(distance);
                break;
            if(self.__fuelrate<=0):
                self.stop(distance);
                break;
    def stop(self,distance):
        self.__velocity=0;
        if distance>0:
            print("remain "+distance.__str__());
        else:
            print("arrived");
    @property
    def velocity(self):
        return self.__velocity;
    @velocity.setter
    def velocity(self,velocity):
        if velocity>=0 and velocity <=200:
            self.__velocity=velocity;
        else:
            self.__velocity=0;
    @property
    def fuelrate(self):
        return __fuelrate;
    @fuelrate.setter
    def fuelrate(self,fuelrate):
        if fuelrate >=0 and fuelrate <=100:
            self.__fuelrate=fuelrate;
        else:
            self.__fuelrate=0;

class employee(person):
    def __init__(self,id,name,distancetowork):
        person.__init__(self,name);
        self.__id=id;
        self.__distnacetowork=distancetowork;
        self.__car='';
        print(car.name);
        self.c=car(car.name);
        self.__email=''; 
        self.__salary=0;
    moods=('happy','tired','lazy');
    def work(self,hours):
        if hours==8:
            mood='happy';
        elif hours>8:
            mood='tired';
        elif hours<8:
            mood='lazy';
    def sendEmail(self):
        pass;    
    @property
    def salary(self):
        return self.__salary;
    @salary.setter
    def salary(self,salary):
        if salary>=1000:
            self.__salary=salary;
        elif salary<1000:
            self.__salary=1000;
    @property
    def email(self):
        return self.__email;
    @email.setter
    def email(self,email):
       if re.match("[^@]+@[^@]+\.[^@]+",email):
           self.__email=email;
    @property
    def healthrate(self):
        return self.healthrate;
    @healthrate.setter
    def healthrate(self,hr):
       if hr>0 and hr <=100:
           self.healthrate=hr;
    def refuel(self,gasamount=100):
        self.c.fuelrate=gasamount;
    def drive(self,distance,time):
        velocity=distance/time;
        self.c.run(velocity,distance);

c=car("fiat 128");
emp=employee(1,"samy",20);
p=office("iti");
emp.refuel();
emp.drive(20,20);