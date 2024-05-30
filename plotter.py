#this program reads a csv file, returns the graph and table(optionally) in pdf format


import matplotlib.pyplot as plt
import pandas as pd
import dataframe_image as dfi
from fpdf import FPDF
from fpdf_table import PDFTable

# from fpdf import Align


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

        #this returns the csv values as pandas dataframe object
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
            self.x_coordinate=55
            self.three_set()

        #stores the x and y label in respective variables

        # self.x_label=self.label_list[0]

        # self.y_label=self.label_list[1]


        #stores values of x and y in list

        # self.x_values=df[self.x_label].tolist()

        # self.y_values=df[self.y_label].tolist()

        # self.data=[self.x_values,self.y_values]
        # self.x_column=[self.x_label]+self.x_values

        # self.y_column=[self.y_label]+self.y_values


    #sets title, label, plots points, and saves the graph as a png image

    def plot_points(self):
        plt.title(self.title)

        if len(self.label_list)==2:
            plt.plot(self.x1_values,self.y1_values,marker=".")
        elif len(self.label_list)==4:
            plt.plot(self.x1_values,self.y1_values,self.x2_values,self.y2_values,marker=".")
        elif len(self.label_list)==6:
            plt.plot(self.x1_values,self.y1_values,self.x2_values,self.y2_values,self.x3_values,self.y3_values,marker=".")   

        plt.plot(self.x1_values,self.y1_values,marker=".")

        

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