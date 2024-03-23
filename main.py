from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3


#initilization pyttsx3 method
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#initilization mixer method
mixer.init()

#add background music
mixer.music.load('kbc.mp3')
mixer.music.play(-1)

def select(event):
    #remove call image after click
    callimagebutton.place_forget()
    
    #remove progressbar after click
    ProgressbarA.place_forget()
    ProgressbarB.place_forget()
    ProgressbarC.place_forget()
    ProgressbarD.place_forget()

    #remove progressbarA laBEL
    ProgressbarlabelA.place_forget()
    ProgressbarlabelB.place_forget()
    ProgressbarlabelC.place_forget()
    ProgressbarlabelD.place_forget()
    
    b=event.widget
    value=b['text']
    print(value)

    for i in range(15):
        if value==currect_ans[i]:
            #if all answer are currect then
            if value==currect_ans[14]:
                #define close funtion
                def close():
                   root2.destroy()
                   root.destroy()
                #call try again funtion
                def playagain():
                   #reset life line button
                   lifeline50button.config(image=image50, state="active")
                   #for Reset audience pole button
                   audiencePolebutton.config(image=audiencePole, state="active")
                   #for Reset phone a friend button
                   phoneAFriendbutton.config(image=phoneAFriend, state="active")
                
                   root2.destroy()
                   questionArea.delete(1.0,END)
                   #when click try again all are reset at starting point
                   questionArea.insert(END,questions[0])
                   optionbutton1.config(text=first_option[0])
                   optionbutton2.config(text=second_option[0])
                   optionbutton3.config(text=third_option[0])
                   optionbutton4.config(text=forth_option[0])
                   #display amount image
                   amountLabel.config(image=amountimage)
                
                #fisrt stop music that already play
                mixer.music.stop()
                #load win music
                mixer.music.load('kbcwon.mp3')
                mixer.music.play()
                #create display for wrong answer
                root2=Toplevel()
                root2.overrideredirect()
                # for window size
                root2.geometry('500x400+140+30')
                #for title
                root2.title('you won 1 millon pounds')
                #for colour
                root2.config(bg='black')
                imgLabel=Label(root2,image=centerimage , bd=0)
                imgLabel.pack(pady=30)
                #lose level create
                winLabel=Label(root2,text='You win', font=('arial',40,'bold'),bg='black' ,fg='white')
                winLabel.pack()
                #try again button
                playagainButton=Button(root2,text='Play Again', font=('arial',20,'bold'),bg='black'
                                  ,fg='white',bd=0,activebackground='black', activeforeground='white', cursor='hand2',
                                  command=playagain)
                playagainButton.pack()
                #try again button
                closeButton=Button(root2,text='Close', font=('arial',20,'bold'),bg='black'
                               ,fg='white',bd=0,activebackground='black', activeforeground='white', cursor='hand2',
                               command=close)
                closeButton.pack()
                #add emoji 1
                happyimage=PhotoImage(file='happy.png')
                happyLabel=Label(root2,image=happyimage, bg='black')
                happyLabel.place(x=30,y=280)
                #add emoji 2
                happyLabel1=Label(root2,image=happyimage, bg='black')
                happyLabel1.place(x=390,y=280)
            
                root1.mainloop()
                break 
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionbutton1.config(text=first_option[i+1])
            optionbutton2.config(text=second_option[i+1])
            optionbutton3.config(text=third_option[i+1])
            optionbutton4.config(text=forth_option[i+1])
            #display amount image
            amountLabel.config(image=amountimages[i])
            
            
               
          
          
        if value not in currect_ans:
            #define close funtion
            def close():
                root1.destroy()
                root.destroy()
            #call try again funtion
            def tryagain():
                root1.destroy()
                questionArea.delete(1.0,END)
                #when click try again all are reset at starting point
                questionArea.insert(END,questions[0])
                optionbutton1.config(text=first_option[0])
                optionbutton2.config(text=second_option[0])
                optionbutton3.config(text=third_option[0])
                optionbutton4.config(text=forth_option[0])
                #display amount image
                amountLabel.config(image=amountimage)
                #display amount image
                amountLabel.config(image=amountimage)
                #reset life line button
                lifeline50button.config(image=image50, state="active")
                #for Reset audience pole button
                audiencePolebutton.config(image=audiencePole, state="active")
                #for Reset phone a friend button
                phoneAFriendbutton.config(image=phoneAFriend, state="active")
                
            #create display for wrong answer
            root1=Toplevel()
            root1.overrideredirect()
            # for window size
            root1.geometry('500x400+140+30')
            #for title
            root1.title('you won 0 pounds')
            #for colour
            root1.config(bg='black')
            imgLabel=Label(root1,image=centerimage , bd=0)
            imgLabel.pack(pady=30)
            #lose level create
            loseLabel=Label(root1,text='You Lose', font=('arial',40,'bold'),bg='black' ,fg='white')
            loseLabel.pack()
            #try again button
            tryagainButton=Button(root1,text='Try Again', font=('arial',20,'bold'),bg='black'
                                  ,fg='white',bd=0,activebackground='black', activeforeground='white', cursor='hand2',
                                  command=tryagain)
            tryagainButton.pack()
            #try again button
            closeButton=Button(root1,text='Close', font=('arial',20,'bold'),bg='black'
                               ,fg='white',bd=0,activebackground='black', activeforeground='white', cursor='hand2',
                               command=close)
            closeButton.pack()
            #add emoji 1
            sadimage=PhotoImage(file='sad.png')
            sadLabel=Label(root1,image=sadimage, bg='black')
            sadLabel.place(x=30,y=280)
            #add emoji 2
            sadLabel1=Label(root1,image=sadimage, bg='black')
            sadLabel1.place(x=390,y=280)
            
            root1.mainloop()
            break
        
#lide line 50-50
def lifeline50():
    
    lifeline50button.config(image=image50x, state=DISABLED)
    if questionArea.get(1.0,'end-1c')==questions[0]:
                        optionbutton2.config(text='')
                        optionbutton3.config(text='')
                        
    if questionArea.get(1.0,'end-1c')==questions[1]:
                        optionbutton2.config(text='')
                        optionbutton4.config(text='')
                        
    if questionArea.get(1.0,'end-1c')==questions[2]:
                        optionbutton1.config(text='')
                        optionbutton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[3]:
                        optionbutton1.config(text='')
                        optionbutton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[4]:
                        optionbutton1.config(text='')
                        optionbutton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[5]:
                        optionbutton1.config(text='')
                        optionbutton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[6]:
                        optionbutton2.config(text='')
                        optionbutton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[7]:
                        optionbutton1.config(text='')
                        optionbutton2.config(text='')
                        
    if questionArea.get(1.0,'end-1c')==questions[8]:
                        optionbutton2.config(text='')
                        optionbutton4.config(text='')
                        
    if questionArea.get(1.0,'end-1c')==questions[9]:
                        optionbutton2.config(text='')
                        optionbutton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[10]:
                        optionbutton2.config(text='')
                        optionbutton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[11]:
                        optionbutton1.config(text='')
                        optionbutton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[12]:
                        optionbutton3.config(text='')
                        optionbutton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[13]:
                        optionbutton1.config(text='')
                        optionbutton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[14]:
                        optionbutton1.config(text='')
                        optionbutton2.config(text='')
  

#audiencePolelifeline
def audiencePolelifeline():
    #for desable audience pole button
    audiencePolebutton.config(image=audiencePolex, state=DISABLED)
    
    ProgressbarA.place(x=580,y=190)
    ProgressbarB.place(x=620,y=190)
    ProgressbarC.place(x=660,y=190)
    ProgressbarD.place(x=700,y=190)

    ProgressbarlabelA.place(x=588,y=320)
    ProgressbarlabelB.place(x=620,y=320)
    ProgressbarlabelC.place(x=660,y=320)
    ProgressbarlabelD.place(x=700,y=320)

    if questionArea.get(1.0,'end-1c')==questions[0]:
         ProgressbarA.config(value=90)
         ProgressbarB.config(value=10)
         ProgressbarC.config(value=40)
         ProgressbarD.config(value=60)
         
    if questionArea.get(1.0,'end-1c')==questions[1]:
         ProgressbarA.config(value=80)
         ProgressbarB.config(value=50)
         ProgressbarC.config(value=40)
         ProgressbarD.config(value=30)
         
    if questionArea.get(1.0,'end-1c')==questions[2]:
         ProgressbarA.config(value=30)
         ProgressbarB.config(value=25)
         ProgressbarC.config(value=85)
         ProgressbarD.config(value=40)
         
    if questionArea.get(1.0,'end-1c')==questions[3]:
         ProgressbarA.config(value=30)
         ProgressbarB.config(value=70)
         ProgressbarC.config(value=10)
         ProgressbarD.config(value=25)
         
    if questionArea.get(1.0,'end-1c')==questions[4]:
         ProgressbarA.config(value=30)
         ProgressbarB.config(value=10)
         ProgressbarC.config(value=40)
         ProgressbarD.config(value=70)
         
    if questionArea.get(1.0,'end-1c')==questions[5]:
         ProgressbarA.config(value=30)
         ProgressbarB.config(value=79)
         ProgressbarC.config(value=40)
         ProgressbarD.config(value=55)
         
    if questionArea.get(1.0,'end-1c')==questions[6]:
         ProgressbarA.config(value=65)
         ProgressbarB.config(value=40)
         ProgressbarC.config(value=45)
         ProgressbarD.config(value=55)
         
    if questionArea.get(1.0,'end-1c')==questions[7]:
         ProgressbarA.config(value=5)
         ProgressbarB.config(value=15)
         ProgressbarC.config(value=98)
         ProgressbarD.config(value=10)
         
    if questionArea.get(1.0,'end-1c')==questions[8]:
         ProgressbarA.config(value=39)
         ProgressbarB.config(value=10)
         ProgressbarC.config(value=70)
         ProgressbarD.config(value=32)
         
    if questionArea.get(1.0,'end-1c')==questions[9]:
         ProgressbarA.config(value=55)
         ProgressbarB.config(value=45)
         ProgressbarC.config(value=30)
         ProgressbarD.config(value=20)
         
    if questionArea.get(1.0,'end-1c')==questions[10]:
         ProgressbarA.config(value=70)
         ProgressbarB.config(value=10)
         ProgressbarC.config(value=40)
         ProgressbarD.config(value=50)
         
    if questionArea.get(1.0,'end-1c')==questions[11]:
         ProgressbarA.config(value=30)
         ProgressbarB.config(value=10)
         ProgressbarC.config(value=82)
         ProgressbarD.config(value=70)
         
    if questionArea.get(1.0,'end-1c')==questions[12]:
         ProgressbarA.config(value=90)
         ProgressbarB.config(value=10)
         ProgressbarC.config(value=40)
         ProgressbarD.config(value=70)

    if questionArea.get(1.0,'end-1c')==questions[13]:
         ProgressbarA.config(value=30)
         ProgressbarB.config(value=89)
         ProgressbarC.config(value=40)
         ProgressbarD.config(value=17)

    if questionArea.get(1.0,'end-1c')==questions[14]:
         ProgressbarA.config(value=30)
         ProgressbarB.config(value=56)
         ProgressbarC.config(value=70)
         ProgressbarD.config(value=40)
         
    
def phonelifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callimagebutton.place(x=70,y=260)
    phoneAFriendbutton.config(image=phoneAFriendx, state=DISABLED)
    
def phoneclick():

    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f'the answer is {currect_ans[i]}')
            engine.runAndWait()
            mixer.music.load('kbc.mp3')
            mixer.music.play(-1)



#currect answer
currect_ans=["O(log n)","Rajasthan","array","Primary Key","''' Comment '''","Linked List","Round Robin","Sachin Tendulkar","Aarya","Aditya Chopra","color","Quick Sort","extends","puspa","Shreyas Iyer"]
#question in list data structure
questions=["1. What is the time complexity of a binary search in a sorted array?",
           " 2. Which is the largest state in India by area?",
           " 3. Which of the following is not a valid data type in Python?",
           "4. Which type of key uniquely identifies a record in a database?",
           "5. Which of the following is a correct way to comment out multiple lines in Python?",
           "6. Which data structure is best suited for implementing a queue?",
           "7. Which scheduling algorithm assigns a fixed time unit per process?",
           "8. Who is known as the \"God of Cricket\"?",
           "9. In which web series does Sushmita Sen play the lead role of Aarya Sareen?",
           "10. Who directed the Bollywood movie \"Dilwale Dulhania Le Jayenge\"?",
            "11. Which CSS property is used to change the text color of an element?",
            "12. Which sorting algorithm has the best time complexity in the average case?",
            "13. In Java, which keyword is used to implement multiple inheritance?",
            "14. The famous dialogue \"Pushpa, jhukega nahi sala..\", is associated with which movie?",
            "15. Which Indian cricketer recently became the first to hit six sixes in an over in international cricket?"
           
           ]

first_option=["O(log n)","Rajasthan","list","Foreign Key","// Comment","Array","Round Robin","Don Bradman"," Mirzapur","Aditya Chopra","color","Bubble Sort","extends","RRR","KL Rahul"]

second_option=["O(n)","Madhya Pradesh","tuple","Primary Key","/* Comment */", "Linked List","FCFS","Jacques Kallis","Delhi Crime","Karan Johar","font-color","Insertion Sort","implements","puspa","Rohit Sharma"]
third_option=["O(n log n)","Maharashtra","array","Composite Key","# Comment","Stack","Shortest Job Next","Sachin Tendulkar","Aarya","Sanjay Leela Bhansali"," text-color","Quick Sort","inheritance","Bahubali","Shreyas Iyer"]
forth_option=["O(1)","Uttar Pradesh","set","Secondary Key","''' Comment '''","Tree","Priority Scheduling","Viv Richards","Sacred Games","Farhan Akhtar","font-style","Selection Sort","a and b both","Gaddar 2","Rishabh Pant"]



#for create a window 
root=Tk()
# for window size
root.geometry('1270x652+0+0')

#for title
root.title('who wants to play kbc , that is create bt gourav mallick')

#for colour
root.config(bg='black')

#partion of windos left or right
#left
leftframe=Frame(root, bg='black', padx=90)
leftframe.grid(row=0,column=0)
#left frame divide 3 section
#1
topframe=Frame(leftframe, bg='black' , pady=15)
topframe.grid(row=0,column=0)
#2
centerframe=Frame(leftframe , bg='black', pady=15)
centerframe.grid(row=1,column=0)
#3
bottomframe=Frame(leftframe)
bottomframe.grid(row=2,column=0)
#right
rightframe=Frame(root, padx=50 , pady=25 , bg='black')
rightframe.grid(row=0,column=1)

#import image50
image50=PhotoImage(file='50-50.png')
#import image50X
image50x=PhotoImage(file='50-50-X.png')
#create a button for image50
lifeline50button=Button(topframe,image=image50 , bg='black',bd=0 , activebackground='black' ,width=180 , height=80, command=lifeline50)
lifeline50button.grid(row=0,column=0)

#import image audience pool
audiencePole=PhotoImage(file='audiencePole.png')
#import image audience pool X
audiencePolex=PhotoImage(file='audiencePoleX.png')

#create a button for audience pool
audiencePolebutton=Button(topframe,image=audiencePole , bg='black',bd=0 ,activebackground='black' ,width=180 , height=80 ,command=audiencePolelifeline)
audiencePolebutton.grid(row=0,column=1)

#import image phoneAFriend
phoneAFriend=PhotoImage(file='phoneAFriend.png')
#import image phoneAFriend
phoneAFriendx=PhotoImage(file='phoneAFriendX.png')
#create a button for phoneAFriend
phoneAFriendbutton=Button(topframe,image=phoneAFriend , bg='black' ,bd=0 ,activebackground='black',width=180 , height=80 ,command=phonelifeline)
phoneAFriendbutton.grid(row=0,column=2)

#import call image
callimage=PhotoImage(file='phone.png')
#create a button for call image
callimagebutton=Button(root,image=callimage , bg='black' ,bd=0 ,activebackground='black', cursor='hand2',command=phoneclick)


#import center image
centerimage=PhotoImage(file='center.png')
#create a lavel for centerimage
logoLabel=Label(centerframe,image=centerimage,bg='black' ,width=300 , height=200)
logoLabel.grid(row=0,column=0)

#import right side image
amountimage=PhotoImage(file='picture0.png')
amountimage1=PhotoImage(file='picture1.png')
amountimage2=PhotoImage(file='picture2.png')
amountimage3=PhotoImage(file='picture3.png')
amountimage4=PhotoImage(file='picture4.png')
amountimage5=PhotoImage(file='picture5.png')
amountimage6=PhotoImage(file='picture6.png')
amountimage7=PhotoImage(file='picture7.png')
amountimage8=PhotoImage(file='picture8.png')
amountimage9=PhotoImage(file='picture9.png')
amountimage10=PhotoImage(file='picture10.png')
amountimage11=PhotoImage(file='picture11.png')
amountimage12=PhotoImage(file='picture12.png')
amountimage13=PhotoImage(file='picture13.png')
amountimage14=PhotoImage(file='picture14.png')
amountimage15=PhotoImage(file='picture15.png')

#list of all amount images
amountimages=[amountimage1,amountimage2,amountimage3,amountimage4,amountimage5,
              amountimage6,amountimage7,amountimage8,amountimage9,amountimage10,amountimage11,
              amountimage12,amountimage13,amountimage14,amountimage15
              ]


#create a lavel for amountimage
amountLabel=Label(rightframe,image=amountimage,bg='black' )
amountLabel.grid(row=0,column=0)

#import buttom image
layoutimage=PhotoImage(file='lay.png') 
#create a lavel for amountimage
layoutLabel=Label(bottomframe,image=layoutimage,bg='black' )
layoutLabel.grid(row=0,column=0) 

#create a text area for question in layout image
questionArea=Text(bottomframe ,font=('arial',18, 'bold'), width=34, height=2 ,
                  wrap='word',bg='black' ,fg='white', bd=0)
questionArea.place(x=70,y=10)
#insert question in  questionArea
questionArea.insert(END,questions[0])
 
#insert options number A
labelA=Label(bottomframe, text='A:',bg='black' ,fg='white', bd=0 ,font=('arial',16, 'bold'))
labelA.place(x=60,y=110)
#create option button 1
optionbutton1=Button(bottomframe,text=first_option[0] ,bg='black' ,activeforeground='white',
              fg='white', bd=0 , activebackground='black' ,font=('arial',14, 'bold'),cursor='hand2',)
optionbutton1.place(x=100,y=105)

#insert options number B
labelB=Label(bottomframe, text='B:',bg='black' ,fg='white', bd=0 ,font=('arial',16, 'bold'))
labelB.place(x=330,y=110)
#create option button 2
optionbutton2=Button(bottomframe,text=second_option[0] ,bg='black' ,activeforeground='white',
              fg='white', bd=0 , activebackground='black' ,font=('arial',14, 'bold'),cursor='hand2',)
optionbutton2.place(x=370,y=105)

#insert options number C
labelC=Label(bottomframe, text='C:',bg='black' ,fg='white', bd=0 ,font=('arial',16, 'bold'))
labelC.place(x=60,y=190)
#create option button 3
optionbutton3=Button(bottomframe,text=third_option[0] ,bg='black' ,activeforeground='white',
              fg='white', bd=0 , activebackground='black' ,font=('arial',14, 'bold'),cursor='hand2',)
optionbutton3.place(x=100,y=185)

#insert options number D
labelD=Label(bottomframe, text='D:',bg='black' ,fg='white', bd=0 ,font=('arial',16, 'bold'))
labelD.place(x=330,y=190) 
#create option button 4
optionbutton4=Button(bottomframe,text=forth_option[0] ,bg='black' ,activeforeground='white',
              fg='white', bd=0 , activebackground='black' ,font=('arial',14, 'bold'),cursor='hand2',)
optionbutton4.place(x=370,y=185)

#funtionallity part start here
#create prograss bar for audiuns pol
ProgressbarA=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarB=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarC=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarD=Progressbar(root,orient=VERTICAL,length=120)

ProgressbarlabelA=Label(root, text='A',bg='black' ,fg='white', font=('arial',20, 'bold'))
ProgressbarlabelB=Label(root, text='B',bg='black' ,fg='white', font=('arial',20, 'bold'))
ProgressbarlabelC=Label(root, text='C',bg='black' ,fg='white', font=('arial',20, 'bold'))
ProgressbarlabelD=Label(root, text='D',bg='black' ,fg='white', font=('arial',20, 'bold'))
#lets create a funtion for button then define select funtion , I defibe this funtion at the top
optionbutton1.bind('<Button-1>', select)
optionbutton2.bind('<Button-1>', select)
optionbutton3.bind('<Button-1>', select)
optionbutton4.bind('<Button-1>', select)


root.mainloop() 
