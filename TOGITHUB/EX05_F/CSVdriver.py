import csv
try:
    class csvdriver:
        def __init__(self,data=["test","data"]):
            self.__data=data
            #萬用的陣列集合所有資料
        def read(self,filename,maker):
            with open(filename+'.csv', newline="", encoding='utf-8')as f:
                csv_reader = csv.reader(f, delimiter=maker)
                for x in csv_reader:
                    print_x = self.convert(x)
                    self.__data.append(print_x)
                    print_x.show()
        def show(self):
           for x in self.__data:
               print("\t",x)

        def get_data(self):
            return tuple(self.__data)
        @staticmethod
        def convert(x):
            data=[]
            for formatdata in x:
                if formatdata.isdigit():
                     data.append(int(formatdata))
                else:data.append(formatdata)
            return csvdriver(data)

        @staticmethod
        def converts(xx):
            data=[]
            for x in xx:
                C=csvdriver.convert(x)
                data.append(C)
            return data
except:
    print("error is evewhere")