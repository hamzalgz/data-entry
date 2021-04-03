from tkinter import *
import sqlite3
import tkinter.messagebox as MessageBox

def insert():
    idE=idEtudiant.get()
    idF=idFilFK.get()
    n=nom.get()
    pn=prenom.get()
    a=age.get()
    if (idE=="" or idF=="" or n=="" or pn=="" or a==""):
        MessageBox.showinfo("insert Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute('''INSERT INTO Etudiant VALUES(?,?,?,?,?);''',(idE,idF,n,pn,a))
        con.execute("commit");
        idEtudiant.delete(0,"end")
        idFilFK.delete(0,"end")
        nom.delete(0,"end")
        prenom.delete(0,"end")
        age.delete(0,"end")
        show()
        MessageBox.showinfo("insert Status", "inserted successfully");
        con.close();

def delete():
    
    if (idEtudiant.get()==""):
        MessageBox.showinfo("delete Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute("DELETE from Etudiant where idEtudiant='"+idEtudiant.get()+"'")
        con.execute("commit");
        idEtudiant.delete(0,"end")
        idFilFK.delete(0,"end")
        nom.delete(0,"end")
        prenom.delete(0,"end")
        age.delete(0,"end")
        show()
        MessageBox.showinfo("delete Status", "deleted successfully");
        con.close();

def update():
    idE=idEtudiant.get()
    idF=idFilFK.get()
    n=nom.get()
    pn=prenom.get()
    a=age.get()
    if (idE=="" or idF=="" or n=="" or pn=="" or a==""):
        MessageBox.showinfo("update Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute("UPDATE Etudiant set idF='"+idFilFK.get()+"' nom='"+nom.get()+"' prenom='"+prenom.get()+"' age='"+age.get()+"'")
        con.commit();
        idFilFK.delete(0,"end")
        n.delete(0,"end")
        pn.delete(0,"end")
        a.delete(0,"end")
        show()
        MessageBox.showinfo("insert Status", "inserted successfully")
        con.close();

def get():
    if (idEtudiant.get()==""):
        MessageBox.showinfo("get Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute("select * from Etudiant where idEtudiant='"+idEtudiant.get()+"'")
        
        con.commit();
        rows=cursor.fetchall()
        for row in rows:
            idFilFK.insert(0,row[1])
            nom.insert(0,row[2])
            prenom.insert(0,row[3])
            age.insert(0,row[4])               
        
        con.close();

def show():
    con=sqlite3.connect('mon_projet')
    cursor=con.cursor()
    cursor.execute("select * from Etudiant")
        
    con.commit();
    rows=cursor.fetchall()
    for row in rows:
        insertData=str(row[0])+'         '+str(row[1])
        list.insert(list.size()+1, insertData)

    con.close()

def insertF():
    id=idFil.get()
    nF=nomfil.get()
    if (id=="" or nF==""):
        MessageBox.showinfo("insert Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute('''INSERT INTO Filiere VALUES(?,?);''',(id,nF))
        con.execute("commit");
        idFil.delete(0,"end")
        nomFil.delete(0,"end")
        showF()
        MessageBox.showinfo("insert Status", "inserted successfully");
        con.close();

def deleteF():
    
    if (idFil.get()==""):
        MessageBox.showinfo("delete Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute("DELETE from Filiere where idEtudiant='"+idFil.get()+"'")
        con.execute("commit");
        idFil.delete(0,"end")
        nomFil.delete(0,"end")
        showF()
        MessageBox.showinfo("delete Status", "deleted successfully");
        con.close();

def updateF():
    nF=nomFil.get()
    idF=idFil.get()
    if (idF==""or nF==""):
        MessageBox.showinfo("update Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute("UPDATE Filiere set idF='"+idFil.get()+"' nF='"+nomFil.get()+"'")
        con.commit();
        idFil.delete(0,"end")
        nomFIL.delete(0,"end")
        showF()
        MessageBox.showinfo("insert Status", "inserted successfully")
        con.close();

def getF():
    if (idFil.get()==""):
        MessageBox.showinfo("get Status", "all fields are required")
    else:
        con=sqlite3.connect('mon_projet')
        cursor=con.cursor()
        cursor.execute("select * from Filiere where idEtudiant='"+idFil.get()+"'")
        
        con.commit();
        rows=cursor.fetchall()
        for row in rows:
            nomFil.insert(0,row[1])               
        
        con.close();

def showF():
    con=sqlite3.connect('mon_projet')
    cursor=con.cursor()
    cursor.execute("select * from Filiere")
        
    con.commit();
    rows=cursor.fetchall()
    for row in rows:
        insertData=str(row[0])+'         '+str(row[1])
        list.insert(list.size()+1, insertData)

    con.close()

root = Tk()
root.geometry("800x400");
root.title("python-tk-sqlite3-Etudiant");

root1 = Tk()
root1.geometry("600x300");
root1.title("python-tk-sqlite3-Filiere");

idEtudiant=Label(root,text='enter IDEtudiant',font=('bold',10))
idEtudiant.place(x=20,y=30)

idFilFK=Label(root, text='enter idFilFK',font=('bold',10))
idFilFK.place(x=20,y=60)

nom=Label(root, text='enter nom',font=('bold',10))
nom.place(x=20,y=90)

prenom=Label(root, text='enter prenom',font=('bold',10))
prenom.place(x=20,y=120)

age=Label(root, text='enter age',font=('bold',10))
age.place(x=20,y=150)

idEtudiant=Entry()
idEtudiant.place(x=120,y=30)

idFilFK=Entry()
idFilFK.place(x=120,y=60)

nom=Entry()
nom.place(x=120,y=90)

prenom=Entry()
prenom.place(x=120,y=120)

age=Entry()
age.place(x=120,y=150)

idFil=Label(root1, text='enter idfili',font=('bold',10))
idFil.place(x=20,y=40)

nomFil=Label(root1, text='enter nomfili',font=('bold',10))
nomFil.place(x=20,y=70)

idFil=Entry (root1)
idFil.place(x=100,y=40)

nomFil=Entry (root1)
nomFil.place(x=100,y=70)

insert= Button(root, text='insert',font=('intalic',10),bg='green',command=insert)
insert.place(x=20,y=200)

delete= Button(root, text='delete',font=('intalic',10),bg='red',command=delete)
delete.place(x=70,y=200)

update= Button(root, text='update',font=('intalic',10),bg='blue',command=update)
update.place(x=120,y=200)

get= Button(root, text='get',font=('intalic',10),bg='white',command=get)
get.place(x=180,y=200)

insertF= Button(root1, text='insertF',font=('intalic',10),bg='green',command=insertF)
insertF.place(x=20,y=200)

deleteF= Button(root1, text='deleteF',font=('intalic',10),bg='red',command=deleteF)
deleteF.place(x=70,y=200)

updateF= Button(root1, text='updateF',font=('intalic',10),bg='blue',command=updateF)
updateF.place(x=120,y=200)

getF= Button(root1, text='getF',font=('intalic',10),bg='white',command=getF)
getF.place(x=180,y=200)

list=Listbox(root)
list.place(x=300, y=30)
show()

list=Listbox(root1)
list.place(x=300, y=30)

showF()


root.mainloop()
root1.mainloop()
