#this program reads a csv file, returns the graph and table(optionally) in pdf format

import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF

def main():
    file1=File(fname(), ftype(), graph_title())
    file1.open_csv()
    file1.plot_points()

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



    #opens and stores values of x and y axis title and values
    def open_csv(self):
        #opening csv file
        df=pd.read_csv(self.fname)                  

        #label_list stores names of axes label as list
        self.label_list=df.columns.values.tolist()  

        #stores the x and y label in respective variables
        self.x_label=self.label_list[0]
        self.y_label=self.label_list[1]

        #stores values of x and y in list
        self.x_values=df[self.x_label].tolist()
        self.y_values=df[self.y_label].tolist()

    #sets title, label, plots points, and saves the graph as a png image
    def plot_points(self):
        plt.title(self.title)

        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        
        plt.plot(self.x_values,self.y_values,marker=".")
        plt.legend()
        
        self.save_as=self.title+".png"
        plt.savefig(self.save_as)


        plt.show()


    def pdf_file(self):
        pdf=FPDF("P","mm","A4")

        pdf.add_page()
        pdf.set_margins(20,10,10,10)
        pdf.set_font("Arial")


        pdf.image(self.save_as, w=100)

        pdf_save_as=self.title+".pdf"
        pdf.output(pdf_save_as)


if __name__=="__main__":
    main()