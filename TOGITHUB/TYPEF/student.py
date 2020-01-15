class student:
    def __init__(self,name,eng,math):
        self.name=name
        self.eng=eng
        self.math=math

    def show(self):
        s='{:<6}{:6}{:6}{:6}{:>6}'
        tot=self.eng+self.math
        avg=tot/2
        print(s.format(self.name,self.eng,self.math,tot,avg))

    @staticmethod
    def convent_to_student(list):
        name=list[0]
        eng=int(list[1])
        math=int(list[2])
        st=student(name,eng,math)
        return st