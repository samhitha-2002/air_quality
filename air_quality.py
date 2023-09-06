from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.configure(bg='Pink')

w = '800'
h = '500'
root.geometry('{}x{}'.format(w, h))

frame1 = Frame(root)
frame1.configure(bg='Pink')
frame1.place(relx=0.5, rely=0.5, anchor="c")

# Creating label for each information
label1 = Label(frame1, text="Air Quality : ", bg="Pink", font=('Times New Roman', 26, 'bold'))
label2 = Label(frame1, text="O3 (μg/m3) :", bg="Pink", font=('Times New Roman', 26, 'bold'))
label3 = Label(frame1, text="NO2 (μg/m3) :", bg="Pink", font=('Times New Roman', 26, 'bold'))
label4 = Label(frame1, text="SO2 (μg/m3) :", bg="Pink", font=('Times New Roman', 26, 'bold'))
label5 = Label(frame1, text="PM2.5 (μg/m3) :", bg="Pink", font=('Times New Roman', 26, 'bold'))
label6 = Label(frame1, text="PM10 (μg/m3) :", bg="Pink", font=('Times New Roman', 26, 'bold'))
label7 = Label(frame1, text="CO (μg/m3) :", bg="Pink", font=('Times New Roman', 26, 'bold'))
label8 = Label(frame1, text="Remark :", bg="Pink", font=('Times New Roman', 26, 'bold'))
label9 = Label(frame1, text="Possible Health Impacts :", bg="Pink", font=('Times New Roman', 26, 'bold'))

# Variable Classes in tkinter
air_data = StringVar()
ar = StringVar()
o3 = StringVar()
no2 = StringVar()
so2 = StringVar()
pm = StringVar()
pml = StringVar()
co = StringVar()
res_remark = StringVar()
res_imp = StringVar()

# Creating label for class variable
label10 = Label(frame1, text="", textvariable=ar, bg="Pink",  font=('Times New Roman', 26, 'bold'))
label11 = Label(frame1, text="", textvariable=o3, bg="Pink", font=('Times New Roman', 26, 'bold'))
label12 = Label(frame1, text="", textvariable=no2, bg="Pink", font=('Times New Roman', 26, 'bold'))
label13 = Label(frame1, text="", textvariable=so2, bg="Pink", font=('Times New Roman', 26, 'bold'))
label14 = Label(frame1, text="", textvariable=pm, bg="Pink", font=('Times New Roman', 26, 'bold'))
label15 = Label(frame1, text="", textvariable=pml, bg="Pink", font=('Times New Roman', 26, 'bold'))
label16 = Label(frame1, text="", textvariable=co, bg="Pink", font=('Times New Roman', 26, 'bold'))
label17 = Label(frame1, text="", textvariable=res_remark, bg="Pink", font=('Times New Roman', 26, 'bold'))
label18 = Label(frame1, text="", textvariable=res_imp, bg="Pink", font=('Times New Roman', 26, 'bold'))

# link for extract html data
def getdata(url):
	r = requests.get(url)
	return r.text

def airinfo():
	htmldata = getdata("https://weather.com/en-IN/forecast/air-quality/l/1d4483a40e513375b6a77bde62b323ccad1362d883f8fd6caac90a871862b644")
	soup = BeautifulSoup(htmldata, 'html.parser')
	res_data = soup.find(class_="DonutChart--innerValue--3_iFF AirQuality--extendedDialText--1kqIb").text
	air_data = soup.find_all(class_="DonutChart--innerValue--3_iFF AirQuality--pollutantDialText--2Q5Oh")
	air_data=[data.text for data in air_data]
	
	ar.set(res_data)
	o3.set(air_data[0])
	no2.set(air_data[2])
	so2.set(air_data[5])
	pm.set(air_data[4])
	pml.set(air_data[3])
	co.set(air_data[1])
	res = int(res_data)
	if res <= 50:
		remark = "Good"
		impact = "Minimal impact"
	elif res <= 100 and res > 51:
		remark = "Satisfactory"
		impact = "Minor breathing discomfort to sensitive people"
	elif res <= 200 and res >= 101:
		remark = "Moderate"
		impact = "Breathing discomfort to the people with lungs, asthma and heart diseases"
	elif res <= 400 and res >= 201:
		remark = "Very Poor"
		impact = "Breathing discomfort to most people on prolonged exposure"
	elif res <= 500 and res >= 401:
		remark = "Severe"
		impact = "Affects healthy people and seriously impacts those with existing diseases"
	res_remark.set(remark)
	res_imp.set(impact)

# creating a button using the widget
button = Button(frame1, justify="center", text="Check", command=airinfo, bg="Violet", font=('Times New Roman', 26, 'bold'))

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=4,column=0)
label6.grid(row=5,column=0)
label7.grid(row=6,column=0)
label8.grid(row=7,column=0)
label9.grid(row=8,column=0)
label10.grid(row=0,column=1)
label11.grid(row=1,column=1)
label12.grid(row=2,column=1)
label13.grid(row=3,column=1)
label14.grid(row=4,column=1)
label15.grid(row=5,column=1)
label16.grid(row=6,column=1)
label17.grid(row=7,column=1)
label18.grid(row=8,column=1)
button.grid(row=0,column=2)

root.mainloop()