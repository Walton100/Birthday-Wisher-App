from tkinter import *
import pandas
import random
import smtplib
import datetime
added_successfully=None
sending_letter=''
letters=['letter1','letter2','letter3']
random_letter=random.choice(letters)
with open(f'letters/{random_letter}.txt','r') as file:
    letter=file.read()

due_time=datetime.datetime.now()
current_month=due_time.month
current_day=due_time.day



window=Tk()
name=None
email=None
month=None
day=None
names=[]
emails=[]
months=[]
days=[]


window.minsize(450,500)
window.config(bg='lavender',pady=30,padx=30)
window.title('Birthday Wisher')
birthday_image=PhotoImage(file='birthday_picture.png')



canvas=Canvas(width=300,height=300,bg='lavender',highlightthickness=0)
canvas.create_image(150,150,image=birthday_image)

canvas.grid(column=1,row=0)
font='callibri'
fg='#7886c7'
name_label=Label(text='Name:',font=(font,12,'bold'),bg='lavender',fg=fg)
name_label.grid(column=0,row=1)
name_entry=Entry(width=25)
name_entry.grid(column=1,row=1)

email_label=Label(text='Email:',font=(font,12,'bold'),bg='lavender',fg=fg)
email_label.grid(column=0,row=2)
email_entry=Entry(width=25)
email_entry.grid(column=1,row=2)

month_label=Label(text='Month:',font=(font,12,'bold'),bg='lavender',fg=fg)
month_label.grid(column=0,row=3)
month_entry=Entry(width=25)
month_entry.grid(column=1,row=3)

day_label=Label(text='Day:',font=(font,12,'bold'),bg='lavender',fg=fg)
day_label.grid(column=0,row=4)
day_entry=Entry(width=25)
day_entry.grid(column=1,row=4)

added=False
def add():
    global names,emails,months,days,name,email,month,day,added_successfully,added
    added=True

    name = name_entry.get()
    names.append(name)
    email = email_entry.get()
    emails.append(email)
    month = month_entry.get()
    months.append(month)
    day = day_entry.get()
    days.append(day)

    sending_letter = letter.replace('[name]', name)


    name_entry.delete(0,END)
    email_entry.delete(0,END)
    month_entry.delete(0,END)
    day_entry.delete(0,END)


    try:
        data=pandas.read_csv('birthday_info.csv')
    except :
        added_dict = {
            'name': names,
            'email': emails,
            'month': months,
            'day': days
        }
        new_added_dict=pandas.DataFrame(added_dict)
        new_added_dict.to_csv('birthday_info.csv')
    else:

        data=data.to_dict(orient='records')
        for i in range(len(data)):
            print(data[i]['name'])
            names.append(data[i]['name'])
            emails.append(data[i]['email'])
            months.append(data[i]['month'])
            days.append(data[i]['day'])

        dict = {
            'name': names,
            'email': emails,
            'month': months,
            'day': days
        }
        new_added_dict = pandas.DataFrame(dict)
        new_added_dict.to_csv('birthday_info.csv')


if added==True:

    data=pandas.read_csv('birthday_info.csv')

    data=data.to_dict(orient='records')
    for person in data:

        if current_month==person['month'] and current_day==person['day']:

            with smtplib.SMTP('smtp.gmail.com') as connection:
                password='pxovowtjxycmbsv'
                my_email='waltonelijah51@gmail.com'
                connection.login(user=my_email,password=password)
                connection.starttls()
            with open(f'letters/{random_letter}.txt','r') as letter:
                sending_letter=letter.read()
                sending_letter=sending_letter.replace('[name]',person['name'])
                print(sending_letter)
                connection.sendmail(from_addr=my_email,to_addrs=person['email'],msg=f'Subject\n\n{sending_letter}')

        else:
            print(person['month'])
            print(person['day'])
            print(current_month)
            print(current_day)
            print('try again')











#password = 'pxovowtjxycmbsv'




add=Button(text='Add',font=(font,12,'bold'),width=23,bg='lavender',fg='#DE3170',border=0,command=add)
add.grid(column=1,row=5)





















window.mainloop()