import tkinter as tk
import numpy as np
import face_recognition
from datetime import *
import pandas as pd
from tkinter import *
from PIL import ImageTk, Image
import cv2
import os

window = tk.Tk()
window.title("Face recognition system")
window.configure(background="black")

logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black",)
l1.place(x=600, y=10)

titl = tk.Label(
    window, text="Smart College!!", bg="black", fg="green", font=("arial", 27),
)
titl.place(x=675, y=12)


welcome_label = tk.Label(
    window,
    text="Welcome to the Face Recognition Based\nAttendance Management System",
    bg="black",
    fg="yellow",
    bd=10,
    font=("arial", 35),
)
welcome_label.pack()

ri = Image.open("UI_Image/verifyy.png")
r_img = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r_img)
label1.image = r_img
label1.place(x=200, y=400)

ai = Image.open("UI_Image/aa.png")
aa_img = ImageTk.PhotoImage(ai)
label2 = Label(window, image=aa_img)
label2.image = aa_img
label2.place(x=520, y=400)

vi = Image.open("UI_Image/attendance.png")
v_img = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v_img)
label3.image = v_img
label3.place(x=830, y=400)

qi = Image.open("UI_Image/register.png")
q_img = ImageTk.PhotoImage(qi)
label4 = Label(window, image=q_img)
label4.image = q_img
label4.place(x=1170, y=400)

def entry():
    def Final_csv(file_name):
        try:
            f = pd.read_csv(file_name)
            f = f.drop_duplicates(subset=['Name'])
            f.to_csv(file_name, index=False)
        except Exception as e:
            print(f"Error in Final_csv: {e}")

    def findEncodings(images):
        encodeList = []
        for img in images:
            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodings = face_recognition.face_encodings(img)
                if encodings:
                    encodeList.append(encodings[0])
        return encodeList

    def markTIMEentry(name, Win_name):
        print("marking entry")
        Win_name += '.csv'
        nameList = []
        try:
            with open(Win_name, 'a+') as f:
                f.seek(0)
                myDataList = f.readlines()
                for line in myDataList:
                    entry = line.strip().split(',')
                    if entry and entry[0] != 'Name':
                        nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.write(f'\n{name},{dtString}')
        except Exception as e:
            print(f"Error in markTIMEentry: {e}")

    def cameraENTRY(img, Win_name):
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markTIMEentry(name, "ENTRY")
        cv2.imshow(Win_name, img)

    path = 'Training_images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print("my list", myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print("classnames", classNames)
    print("images", images)
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    try:
        while True:
            success, img = cap.read()
            if not success:
                print("Failed to read from camera.")
                break
            cameraENTRY(img, 'ENTRY')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        print("calling final csv")
        Final_csv("ENTRY.csv")
        cap.release()
        cv2.destroyAllWindows()

b1 = tk.Button(window, text="Entry", font=("Algerian", 20), bg='black', fg='yellow', bd=5, command=entry)
b1.place(relx=0.17, rely=0.75)

def exit():
    def Final_csv(file_name):
        try:
            f = pd.read_csv(file_name)
            f = f.drop_duplicates(subset=['Name'])
            f.to_csv(file_name, index=False)
        except Exception as e:
            print(f"Error in Final_csv: {e}")

    def findEncodings(images):
        encodeList = []
        for img in images:
            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodings = face_recognition.face_encodings(img)
                if encodings:
                    encodeList.append(encodings[0])
        return encodeList

    def markTIMEexit(name, Win_name):
        print("marking exit")
        Win_name += '.csv'
        nameList = []
        try:
            with open(Win_name, 'a+') as f:
                f.seek(0)
                myDataList = f.readlines()
                for line in myDataList:
                    entry = line.strip().split(',')
                    if entry and entry[0] != 'Name':
                        nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.write(f'\n{name},{dtString}')
        except Exception as e:
            print(f"Error in markTIMEexit: {e}")
        print("done")

    def cameraEXIT(img, Win_name):
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markTIMEexit(name, "EXIT")
        cv2.imshow(Win_name, img)

    path = 'Training_images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print("mylist", myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print("classnames", classNames)
    print("images list:", images)
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    try:
        while True:
            success, img = cap.read()
            if not success:
                print("Failed to read from camera.")
                break
            cameraEXIT(img, 'EXIT')
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        print("calling final csv")
        Final_csv("EXIT.csv")
        cap.release()
        cv2.destroyAllWindows()

b2 = tk.Button(window, text="Exit", font=("Algerian", 20), bg='black', fg='yellow', command=exit)
b2.place(relx=0.39, rely=0.75)

def attendance():
    def clear_CSV(file_name):
        # Overwrite the file with just the header
        try:
            with open(file_name, 'w') as file:
                file.write('Name,Time\n')
        except Exception as e:
            print(f"Error clearing CSV: {e}")

    def TOminutes(Entry, Exit):
        IN = Entry.split(':')
        OUT = Exit.split(':')
        t1 = int(IN[0]) * 60 + int(IN[1])
        t2 = int(OUT[0]) * 60 + int(OUT[1])
        return t2 - t1

    try:
        df1 = pd.read_csv("ENTRY.csv", names=["Name", "Time_ENTRY"], header=0)
        df2 = pd.read_csv("EXIT.csv", names=["Name", "Time_EXIT"], header=0)
        LIST = pd.read_csv("LIST.csv")
    except Exception as e:
        print(f"Error reading CSVs: {e}")
        return

    # Merge on Name
    result = pd.merge(df1, df2, on="Name", how="inner")
    result['DURATION'] = result.apply(lambda row: TOminutes(row['Time_ENTRY'], row['Time_EXIT']), axis=1)
    # dropping student records who have a duration less than a specified threshold
    result = result[result['DURATION'] >= 1]
    # Mark attendance
    LIST['ATTENDANCE'] = 'ABSENT'
    if not result.empty:
        present_names = set(result['Name'])
        LIST.loc[LIST['Name'].isin(present_names), 'ATTENDANCE'] = 'PRESENT'
    t = date.today().strftime("%m-%d-%Y") + '.csv'
    print(LIST)
    LIST.to_csv(t, index=False)
    clear_CSV("ENTRY.csv")
    clear_CSV("EXIT.csv")

b3 = tk.Button(window, text="Mark Attendance", font=("Algerian", 20), bg='black', fg='yellow', command=attendance)
b3.place(relx=0.54, rely=0.75)

def update1():
    path = 'Training_images'
    def setname():
        ret, frame = cap.read()
        name = e.get()
        if name:
            name = name + ".png"
            cv2.imwrite(os.path.join(path, name), frame)
    root = Toplevel(window)
    root.geometry('644x560')
    root.configure(bg='black')
    app = Frame(root, bg="white")
    app.grid()
    lmain = Label(app)
    lmain.grid()
    cap = cv2.VideoCapture(0)
    def video_stream():
        _, frame = cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(1, video_stream)
    e = Entry(root, width=20, font=('Times 15'))
    e.place(x=200, y=490, width=250, height=25)
    e.focus_set()
    b = Button(root, text='UPDATE', command=setname, width=20, font=('Helvetica 15'), bg="white", fg="black")
    b.place(x=270, y=520, width=150, height=50)
    video_stream()
    def on_closing():
        cap.release()
        cv2.destroyAllWindows()
        root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

b4 = tk.Button(window, text="Generate database", font=("Algerian", 20), bg='black', fg='yellow', command=update1)
b4.place(relx=0.73, rely=0.75)
window.geometry("2000x2000")
window.mainloop()
