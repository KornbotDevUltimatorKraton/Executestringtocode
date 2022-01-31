listcode = ["import os","listdata = os.listdir('/home/roboticsdev')","print(listdata)","data_out = [i for i in listdata]","print(data_out)"]
for i in listcode: 
     exec(i)