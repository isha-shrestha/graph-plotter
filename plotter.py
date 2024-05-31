#this program reads a csv file, returns the graph and table(optionally) in pdf format


import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi
from fpdf import FPDF



def main():

    file1=File(fname(), ftype(), graph_title())
    file1.open_csv()

    file1.plot_points()
    file1.pdf_file()

#this function asks for file name from the user and returns the file name excluding the extension
def fname():

    fname=input("enter file name:").lower()

    if fname.endswith(".csv"):
        return fname[:-4]
    else:
        return fname


#this function asks for the file type from the user
def ftype():
    ftype=input("enter file type(formality ko lagi sodheko, i accept nothing but csv):").lower()

    if ftype==".csv" or ftype=="csv":
        return ".csv"
    else:
        raise TypeError("File needs to csv type")


def graph_title():
    graph_title=input("enter the title of your graph: ")    
    return graph_title


class File:

    def __init__(self,name,type,title):
        self.name=name
        self.type=type
        self.title=title

        self.fname=self.name+self.type

    def one_set(self):

         #stores the x and y label in respective variables
        self.x1_label=self.label_list[0]
        self.y1_label=self.label_list[1]

        #stores values of x and y in list
        self.x1_values=self.df[self.x1_label].tolist()
        self.y1_values=self.df[self.y1_label].tolist()

        self.data=[self.x1_values,self.y1_values]

        self.pandas_dataframe1()


    #this returns the csv values as pandas dataframe object when there is 1 set of data
    def pandas_dataframe1(self):
        dataframe=pd.DataFrame({self.x1_label:self.x1_values, self.y1_label:self.y1_values})
        self.table_title=self.title+"_table.png"
        dfi.export(dataframe,self.table_title)
        print("table wala function run vayo")


    def two_set(self):

         #stores the x and y label in respective variables
        self.x1_label=self.label_list[0]
        self.y1_label=self.label_list[1]

        #stores values of x and y in list
        self.x1_values=self.df[self.x1_label].tolist()
        self.y1_values=self.df[self.y1_label].tolist()


         #stores the x and y label in respective variables
        self.x2_label=self.label_list[2]
        self.y2_label=self.label_list[3]

        #stores values of x and y in list
        self.x2_values=self.df[self.x2_label].tolist()
        self.y2_values=self.df[self.y2_label].tolist()

        self.data=[self.x1_values,self.y1_values,self.x2_values,self.y2_values]
        self.pandas_dataframe2()


        #this returns the csv values as pandas dataframe object
    def pandas_dataframe2(self):
        dataframe=pd.DataFrame({self.x1_label:self.x1_values, self.y1_label:self.y1_values,self.x2_label:self.x2_values, self.y2_label:self.y2_values})
        self.table_title=self.title+"_table.png"
        dfi.export(dataframe,self.table_title)
        print("table wala function run vayo")


    def three_set(self):

         #stores the x and y label in respective variables
        self.x1_label=self.label_list[0]
        self.y1_label=self.label_list[1]

        #stores values of x and y in list
        self.x1_values=self.df[self.x1_label].tolist()
        self.y1_values=self.df[self.y1_label].tolist()

         #stores the x and y label in respective variables
        self.x2_label=self.label_list[2]
        self.y2_label=self.label_list[3]

        #stores values of x and y in list
        self.x2_values=self.df[self.x2_label].tolist()
        self.y2_values=self.df[self.y2_label].tolist()

         #stores the x and y label in respective variables
        self.x3_label=self.label_list[4]
        self.y3_label=self.label_list[5]

        #stores values of x and y in list
        self.x3_values=self.df[self.x3_label].tolist()
        self.y3_values=self.df[self.y3_label].tolist()


        self.data=[self.x1_values,self.y1_values,self.x2_values,self.y2_values,self.x3_values,self.y3_values]
        self.pandas_dataframe3()


        #this returns the csv values as pandas dataframe object
    def pandas_dataframe3(self):
        dataframe=pd.DataFrame({self.x1_label:self.x1_values, self.y1_label:self.y1_values,self.x2_label:self.x2_values, self.y2_label:self.y2_values,self.x3_label:self.x3_values, self.y3_label:self.y3_values})
        self.table_title=self.title+"_table.png"
        dfi.export(dataframe,self.table_title)
        print("table wala function run vayo")

    def four_set(self):

         #stores the x and y label in respective variables
        self.x1_label=self.label_list[0]
        self.y1_label=self.label_list[1]

        #stores values of x and y in list
        self.x1_values=self.df[self.x1_label].tolist()
        self.y1_values=self.df[self.y1_label].tolist()

         #stores the x and y label in respective variables
        self.x2_label=self.label_list[2]
        self.y2_label=self.label_list[3]

        #stores values of x and y in list
        self.x2_values=self.df[self.x2_label].tolist()
        self.y2_values=self.df[self.y2_label].tolist()

         #stores the x and y label in respective variables
        self.x3_label=self.label_list[4]
        self.y3_label=self.label_list[5]

        #stores values of x and y in list
        self.x3_values=self.df[self.x3_label].tolist()
        self.y3_values=self.df[self.y3_label].tolist()

        
         #stores the x and y label in respective variables
        self.x4_label=self.label_list[6]
        self.y4_label=self.label_list[7]

        #stores values of x and y in list
        self.x4_values=self.df[self.x4_label].tolist()
        self.y4_values=self.df[self.y4_label].tolist()

        self.data=[self.x1_values,self.y1_values,self.x2_values,self.y2_values,self.x3_values,self.y3_values]
        self.pandas_dataframe4()


        #this returns the csv values as pandas dataframe object
    def pandas_dataframe4(self):
        dataframe=pd.DataFrame({self.x1_label:self.x1_values, self.y1_label:self.y1_values,self.x2_label:self.x2_values, self.y2_label:self.y2_values,self.x3_label:self.x3_values, self.y3_label:self.y3_values,self.x4_label:self.x4_values, self.y4_label:self.y4_values})
        self.table_title=self.title+"_table.png"
        dfi.export(dataframe,self.table_title)
        print("table wala function run vayo")

    def five_set(self):
         #stores the x and y label in respective variables
        self.x1_label=self.label_list[0]
        self.y1_label=self.label_list[1]

        #stores values of x and y in list
        self.x1_values=self.df[self.x1_label].tolist()
        self.y1_values=self.df[self.y1_label].tolist()

         #stores the x and y label in respective variables
        self.x2_label=self.label_list[2]
        self.y2_label=self.label_list[3]

        #stores values of x and y in list
        self.x2_values=self.df[self.x2_label].tolist()
        self.y2_values=self.df[self.y2_label].tolist()

         #stores the x and y label in respective variables
        self.x3_label=self.label_list[4]
        self.y3_label=self.label_list[5]

        #stores values of x and y in list
        self.x3_values=self.df[self.x3_label].tolist()
        self.y3_values=self.df[self.y3_label].tolist()

        
         #stores the x and y label in respective variables
        self.x4_label=self.label_list[6]
        self.y4_label=self.label_list[7]

        #stores values of x and y in list
        self.x4_values=self.df[self.x4_label].tolist()
        self.y4_values=self.df[self.y4_label].tolist()


         #stores the x and y label in respective variables
        self.x5_label=self.label_list[8]
        self.y5_label=self.label_list[9]

        #stores values of x and y in list
        self.x5_values=self.df[self.x5_label].tolist()
        self.y5_values=self.df[self.y5_label].tolist()


        self.data=[self.x1_values,self.y1_values,self.x2_values,self.y2_values,self.x3_values,self.y3_values,self.x4_values,self.y4_values,self.x5_values,self.y5_values]
        self.pandas_dataframe5()


        #this returns the csv values as pandas dataframe object
    def pandas_dataframe5(self):
        dataframe=pd.DataFrame({self.x1_label:self.x1_values, self.y1_label:self.y1_values,
                                self.x2_label:self.x2_values, self.y2_label:self.y2_values,
                                self.x3_label:self.x3_values, self.y3_label:self.y3_values,
                                self.x4_label:self.x4_values, self.y4_label:self.y4_values,
                                self.x5_label:self.x5_values, self.y5_label:self.y5_values})
        self.table_title=self.title+"_table.png"
        dfi.export(dataframe,self.table_title)
        print("table wala function run vayo")

    #opens and stores values of x and y axis title and values

    def open_csv(self):

        #opening csv file
        self.df=pd.read_csv(self.fname)                  

        #label_list stores names of axes label as list
        self.label_list=self.df.columns.values.tolist()  

        if len(self.label_list)==2:
            self.x_coordinate=80
            self.one_set()

        elif len(self.label_list)==4:
            self.x_coordinate=70
            self.two_set()

        elif len(self.label_list)==6:
            self.x_coordinate=30
            self.three_set()

        elif len(self.label_list)==8:
            self.x_coordinate=20
            self.four_set()

        elif len(self.label_list)==10:
            self.x_coordinate=0
            self.five_set()


    def first_label(self):
        self.first=input("enter label for first set of data: ")
        return self.first


    def second_label(self):
        self.second=input("enter label for second set of data: ")
        return self.second
        

    def third_label(self):
        self.third=input("enter label for third set of data: ")
        return self.third

    
    def fourth_label(self):
        self.fourth=input("enter label for third set of data: ")
        return self.fourth

        
    def fifth_label(self):
        self.fifth=input("enter label for third set of data: ")
        return self.fifth


    def plot_points(self):
        plt.title(self.title)

        if len(self.label_list)==2:
            plt.plot(self.x1_values,self.y1_values,marker=".")

        elif len(self.label_list)==4:
            plt.plot(self.x1_values,self.y1_values,marker=".",label=self.first_label())
            plt.plot(self.x2_values,self.y2_values,marker=".",label=self.second_label())

        elif len(self.label_list)==6:
            plt.plot(self.x1_values,self.y1_values,marker=".",label=self.first_label())
            plt.plot(self.x2_values,self.y2_values,marker=".",label=self.second_label())
            plt.plot(self.x3_values,self.y3_values,marker=".",label=self.third_label())  

        elif len(self.label_list)==8:
            plt.plot(self.x1_values,self.y1_values,marker=".",label=self.first_label())
            plt.plot(self.x2_values,self.y2_values,marker=".",label=self.second_label())
            plt.plot(self.x3_values,self.y3_values,marker=".",label=self.third_label())   
            plt.plot(self.x4_values,self.y4_values,marker=".",label=self.fourth_label())

        elif len(self.label_list)==10:
            plt.plot(self.x1_values,self.y1_values,marker=".",label=self.first_label())
            plt.plot(self.x2_values,self.y2_values,marker=".",label=self.second_label())
            plt.plot(self.x3_values,self.y3_values,marker=".",label=self.third_label())   
            plt.plot(self.x4_values,self.y4_values,marker=".",label=self.fourth_label())
            plt.plot(self.x5_values,self.y5_values,marker=".",label=self.fifth_label())   

        plt.legend(loc="best")
             
        self.save_as=self.title+".png"

        plt.savefig(self.save_as)
        plt.show()



    def pdf_file(self):

        pdf=FPDF("P","mm","A4")

        pdf.add_page()
        pdf.set_margins(20,10,10)

        pdf.image(self.table_title,x=self.x_coordinate)
        pdf.image(self.save_as, w=170)
        print("pdf wala function run vayo")

        pdf_save_as=self.title+".pdf"
        pdf.output(pdf_save_as)



if __name__=="__main__":
    main()