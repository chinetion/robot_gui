'''
---------------------------------------------------------------------------------------------------------------------
textbox([name,default_data],...)                    // Ex - textbox(["Distance",100],["Temparator",200],["Varocity",300])
get_textbox(index_of_name)                          // Ex - get_textbox(0)
---------------------------------------------------------------------------------------------------------------------
radio("name",...)                                   // Ex - radio("Manual","Auto")
get_radio()                                         // Ex - get_radio()
---------------------------------------------------------------------------------------------------------------------
label("name",...)                                   // Ex - label("Distance","Temparator","Distance")
---------------------------------------------------------------------------------------------------------------------
progressbar("name",...)                             // Ex - progressbar("LEFT","RIGHT ")
---------------------------------------------------------------------------------------------------------------------
updates([label_data,...],[progressbar_data,...])    // Ex - gui.updates([a,b,c,d,e,f,g,h,i,j,k],[l,m])
---------------------------------------------------------------------------------------------------------------------
'''

from Tkinter import *
import ttk
import time
class GUI:
    def textbox(self,*name):
        Box2=Frame(self.SetVariable_Frame)
        Box2.pack(side=LEFT)
        for x in range(0,len(name)):
            Box=Frame(Box2)
            Box.pack(side=TOP)

            self.textbox_data.append({'1':Label(Box,text=' ['+str(len(self.textbox_data))+'] '+name[x][0],width = 11,anchor=W)})
            self.textbox_data[len(self.textbox_data)-1]['1'].pack(side=LEFT)

            self.textbox_data[len(self.textbox_data)-1]['2'] = Label(Box,text=" : ")
            self.textbox_data[len(self.textbox_data)-1]['2'].pack(side=LEFT)

            self.textbox_data[len(self.textbox_data)-1]['value'] = Entry(Box,width = 8)
            self.textbox_data[len(self.textbox_data)-1]['value'].pack(side=LEFT)
            self.textbox_data[len(self.textbox_data)-1]['value'].insert(0, name[x][1])
    def get_textbox(self,index):
        data = self.textbox_data[index]['value'].get().rstrip()
        if(not(data.isdigit())):
            data= 0
        return float(data)

    def label(self,*name):
        Box2=Frame(self.GetVariable_Frame)
        Box2.pack(side=LEFT)
        for x in range(0,len(name)):
            Box=Frame(Box2)
            Box.pack(side=TOP)
            self.label_data.append({'1':Label(Box,text=' [' + str(len(self.label_data)) + '] ' + str(name[x]),width = 11,anchor=W)})
            self.label_data[len(self.label_data)-1]['1'].pack(side=LEFT)

            self.label_data[len(self.label_data)-1]['2'] = Label(Box,text=" : ")
            self.label_data[len(self.label_data)-1]['2'].pack(side=LEFT)

            self.label_data[len(self.label_data)-1]['text'] = Label(Box,text="1234",width = 9,anchor=W)
            self.label_data[len(self.label_data)-1]['text'].pack(side=LEFT)
    def updates(self,data,progress):
        if(time.time()-self.b_time > 0.1):
            for x in range(0,len(self.label_data)):
                self.label_data[x]['text'].config(text=str(data[x]))
            for x in range(0,len(self.progressbar_data)):
                self.progressbar_data[x]['value'].set(progress[x])
            self.update()
            self.b_time = time.time()
    def button(self,*name):
        for x in range(0,len(name)):
            self.button_data_value.append(x)
            self.button_data.append(Button(self.Control_Frame2, text=name[x],anchor=N))
            print self.button_data_value[x]
            self.button_data[len(self.button_data)-1].pack(side=LEFT)
        print self.button_data[1].cget('command')
    def button_command(self,num):
        print num

    def callback(self):
        print 'x'
    def get_radio(self):
        return self.radio_data_value.get()
    def radio(self,*name):
        self.radio_data_value.set('0')
        for x in range(0,len(name)):
            self.radio_data.append(Radiobutton(self.Control_Frame, text=name[x],variable=self.radio_data_value,value=x))
            self.radio_data[len(self.radio_data)-1].pack(side=LEFT)
    def progressbar(self,*name):
        Box=Frame(self.Bar_Frame)
        Box.pack(expand=1,fill=Y)
        Box2=Frame(self.Bar_Frame)
        Box2.pack(fill=BOTH)
        for x in range(0,len(name)):
            self.progressbar_data.append({'value':DoubleVar()})
            self.progressbar_data[len(self.progressbar_data)-1]['data'] = ttk.Progressbar(Box,orient='vertical',variable=self.progressbar_data[len(self.progressbar_data)-1]['value'], maximum=100)
            self.progressbar_data[len(self.progressbar_data)-1]['data'].pack(side=LEFT,padx=20,pady=15,fill=Y)

            self.progressbar_data[len(self.progressbar_data)-1]['label'] = Label(Box2,text=name[x],width = 7 ,anchor=N)
            self.progressbar_data[len(self.progressbar_data)-1]['label'].pack(side=LEFT)
    def mainloop(self):
        self.root.mainloop()
    def update(self):
        self.root.update()
    def __init__(self):

        self.root = Tk()
        self.root.title("Betagro")
        self.progressbar_data=list()
        self.label_data=list()
        self.textbox_data=list()
        self.button_data=list()
        self.button_data_value = list()
        self.radio_data=list()
        self.radio_data_value = StringVar()

        self.Bar_Frame = LabelFrame(self.root,text="Weight Bar",labelanchor=N)
        self.Bar_Frame.pack(side=LEFT,fill=Y,ipady=10,padx=20,pady=10)

        self.Monitor_Frame = Frame(self.root)
        self.Monitor_Frame.pack(side=LEFT)

        self.SetVariable_Frame=LabelFrame(self.Monitor_Frame,text="Set Vaiable",labelanchor=NW)
        self.SetVariable_Frame.pack(side=TOP,ipadx=10,ipady=10,padx=20,pady=10,anchor=W)

        self.GetVariable_Frame=LabelFrame(self.Monitor_Frame,text="Display Variable",labelanchor=NW)
        self.GetVariable_Frame.pack(side=TOP,ipadx=10,ipady=10,padx=20,pady=10,anchor=W)

        self.Control_Frame=LabelFrame(self.Monitor_Frame,text="Mode",labelanchor=NW)
        self.Control_Frame.pack(side=LEFT,ipadx=10,ipady=10,padx=20,pady=10,anchor=W)

        #self.Control_Frame2=LabelFrame(self.Monitor_Frame,text="Button",labelanchor=NW)
        #self.Control_Frame2.pack(side=LEFT,ipadx=10,ipady=8,padx=20,pady=10,anchor=N)

        self.s = ttk.Style()
        self.s.theme_use("default")
        self.s.configure("TProgressbar", thickness=20, background='#4CAF50')

        self.b_time=0
        self.get_time=0
