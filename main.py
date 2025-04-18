from  PIL import Image,ImageTk
import tkinter as tk
import requests


root = tk.Tk()

root.title("Weather App")
root.geometry("600x500")

def format_response(weather):
    try: 
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemprature:%s'%(city,condition,temp)
    except:
        final_str='There was a problem retrieving that information'
    return final_str    

def get_weather(city):
    weather_key = 'YOUR_API_KEY'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    paramsm = {'APPID':weather_key,'q':city,'unit':'imperial'}
    response = requests.get(url,paramsm)
    # print(response.json())
    weather=response.json()
   
    result['text'] = format_response(weather)

    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
     size=int(frame_two.winfo_height()*0.25)
     img=ImageTk.PhotoImage(Image.open('./Icons/'+icon+'.png').resize((size,size)))
     weather_icon.delete('all')
     weather_icon.create_image(0,0,anchor='nw',image=img)
     weather_icon.image=img


img= Image.open('./Image/blue.jpg')
img= img.resize((600,500),Image.Resampling.LANCZOS)
img_photo= ImageTk.PhotoImage(img)

bg_1b1=tk.Label(root,image=img_photo)
bg_1b1.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_1b1,text='Weather Report',anchor='center',bg='orange',fg='black',font=('Georgia',22,'bold'))
heading_title.place(x=190,y=18)

frame_one = tk.Label(root,image=img_photo)
bg_1b1.place(x=0,y=0,width=600,height=500)

frame_one=tk.Frame(bg_1b1,bg="#87CEEB",bd=5)
frame_one.place(x=75,y=70,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('Georgia',22),width=17)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text='get weather',fg='black',font=('times new roman',16,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

frame_two=tk.Frame(bg_1b1,bg="#87CEEB",bd=5)
frame_two.place(x=75,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)

def clear():
    txt_box.delete(0, tk.END)
    result['text'] = ''
    weather_icon.delete('all')

def exit_app():
    root.destroy()


btn = tk.Button(text='Exit', font=("Georgia", 16, "bold"), bg='orange', fg='black',
                width=7, relief='groove', command=exit_app)
btn.place(x=310, y=370)

btn = tk.Button(text='Reset', font=("Georgia", 16, "bold"), bg='orange', fg='black',
                width=7, relief='groove', activebackground="blue", activeforeground='white',
                command=clear)
btn.place(x=180, y=370)


root.mainloop()