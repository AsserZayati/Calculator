import customtkinter as ctk
import tkinter as tk
from math import *
import sympy
root=ctk.CTk()
root.geometry('540x570')
root.title("Calculatrice")
#-------------------------Partie commandes et fonctions --------------------

def Clear_txt():
    input_box.config(state='normal')
    input_box.delete(0,tk.END)
    input_box.config(state='disabled')
def Back_oneL():
    input_box.config(state='normal')
    txt=input_box.get()
    input_box.delete(len(txt)-1)
    input_box.config(state='disabled')

def display_input(_input):
    
    input_box.config(state='normal')
    input_box.insert(index=tk.INSERT,string=_input)
    input_box.config(state='readonly')
def result():
    result_box.config(state='normal')
    result_box.delete(0,tk.END)
    calcul=input_box.get()
    try :
        res=round(eval(calcul),8)
        result_box.insert(string=f"={res}",index=tk.INSERT)
    except Exception as exp :
        result_box.insert(string="Error",index=tk.INSERT)
    result_box.config(state='readonly')
def timeto():
    current_time=root.cget('bg')
    if current_time=='SystemButtonFace':
        root.configure(bg="#4F4D4D")
    else:
        root.configure(bg="SystemButtonFace")

def delete_res():
    result_box.config(state='normal')
    result_box.delete('0',tk.END)
    result_box.config(state='disabled')
def utiliser_res():
    U=result_box.get()
    U=U[1:]
    input_box.config(state='normal')
    input_box.delete(0,tk.END)
    input_box.insert(index=tk.INSERT,string=U)
    input_box.config(state='readonly')

     
     
     
#-----------Tab views


tab1 = ctk.CTkTabview(root, width=280, height=400)
tab1.place(y=110, x=16)
tab1.add("Standard")
tab1.add("Scientifique")
tab1.add("Resolutions")


#------Idee > creer des buttons au lieu de tab views ....----
#--------------------------Partie pour l'operation et autre pour le resultat

input_box=tk.Entry(root,font=("Bold",20),justify="right",border=0,state='disabled',bg="#C8C3C0")
input_box.place(y=25,x=30,width=250,height=55)
result_box=tk.Entry(root,font=("Bold",12),justify="left",border=0,bg="#C8C3C0",state='disabled')
result_box.place(y=75,x=30,width=250,height=37) 
clear_result=ctk.CTkButton(root,width=20,height=20,fg_color='red',text="X",
                           command=delete_res)
clear_result.place(y=65,x=200)
#------------------------Partie Fini !
#------------------------Partie de tous les buttons
#------------------------Calculatrice Standard----------------------------------------
clear_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color="#F58136",corner_radius=8,border_width=0,
                       text='C',font=('Bold',17),bg_color=root.cget('bg'),hover=False,command=Clear_txt)
clear_bt.place(y=45,x=25)
delete_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color="#F58136",corner_radius=8,border_width=0,
                       text='D',font=('Bold',17),bg_color=root.cget('bg'),hover=False,command=Back_oneL)
delete_bt.place(y=45,x=85)
percentage_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color="#F58136",corner_radius=8,border_width=0,
                       text='%',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='%'))
percentage_bt.place(y=45,x=145)


divide_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color='#F58136',corner_radius=8,border_width=0,
                        text='➗',bg_color=root.cget('bg'),hover=False,font=('Bold',17),
                        command=lambda:display_input(_input='/')
                        )
divide_bt.place(y=45,x=205)
multiply_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color='#F58136',corner_radius=8,border_width=0,
                        text='X',bg_color=root.cget('bg'),hover=False,font=('Bold',17),
                        command=lambda:display_input(_input='*')
                        )
multiply_bt.place(y=105,x=205)
substract_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color='#F58136',corner_radius=8,border_width=0,
                        text='-',bg_color=root.cget('bg'),hover=False,font=('Bold',17),
                        command=lambda:display_input(_input='-')
                        )
substract_bt.place(y=165,x=205)
addition_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color='#F58136',corner_radius=8,border_width=0,
                        text='+',bg_color=root.cget('bg'),hover=False,font=('Bold',17),
                        command=lambda:display_input(_input='+')
                        )
addition_bt.place(y=225,x=205)
equal_bt=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,fg_color='#F58136',corner_radius=8,border_width=0,
                        text='=',bg_color=root.cget('bg'),hover=False,font=('Bold',17),command=result
                        )
equal_bt.place(y=285,x=205)
#--------------------bouttons des chiffres 1 a 9 ---------------------
btn_7=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='7',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='7'))
btn_7.place(y=105,x=25)
btn_8=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='8',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='8'))
btn_8.place(y=105,x=85)
btn_9=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='9',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='9'))
btn_9.place(y=105,x=145)
btn_4=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='4',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='4'))
btn_4.place(y=165,x=25)
btn_5=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='5',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='5'))
btn_5.place(y=165,x=85)
btn_6=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='6',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='6'))
btn_6.place(y=165,x=145)
btn_1=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='1',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='1'))
btn_1.place(y=225,x=25)
btn_2=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='2',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='2'))
btn_2.place(y=225,x=85)
btn_3=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='3',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='3'))
btn_3.place(y=225,x=145)
btn_0=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='0',font=('Bold',17),bg_color=root.cget('bg'),hover=False,
                       command=lambda:display_input(_input='0'))
btn_0.place(y=285,x=145)
btn_point=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='.',font=('Bold',17),bg_color=root.cget('bg'),hover=False,command=lambda:display_input(_input='.'))
btn_point.place(y=285,x=85)
btn_time=ctk.CTkButton(tab1.tab("Standard"),width=38,height=38,corner_radius=8,border_width=0,
                       text='🌗',font=('Bold',17),bg_color=root.cget('bg'),hover=False,command=timeto)
btn_time.place(y=285,x=25)

#calculatrice mode scientifique ---Tab view des outils scientifiques
btn_power=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="^y",hover=False,command=lambda:display_input(_input='**'))
btn_power.place(y=45,x=25)
sqaure_btn=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="√",hover=False,command=lambda:display_input(_input='sqrt('))
sqaure_btn.place(y=45,x=85)
racinen_btn=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="^1/n",hover=False,command=lambda:display_input(_input='**(1/'))
racinen_btn.place(y=45,x=145)
btn_sin=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="Sinus",hover=False,command=lambda:display_input(_input='sin(radians('))
btn_sin.place(y=105,x=25)
btn_cos=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="Cosinus",hover=False,command=lambda:display_input(_input='cos(radians('))
btn_cos.place(y=105,x=85)
pi_i=str(round(pi,8))
btn_pi=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="∏",hover=False,command=lambda:display_input(_input=pi_i))
btn_pi.place(y=165,x=25)

e_i=str(round(e,8))
btn_exp=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="e",hover=False,command=lambda:display_input(_input=e_i))
btn_exp.place(y=165,x=85)

btn_log=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="log",hover=False,command=lambda:display_input(_input="log10("))
btn_log.place(y=165,x=145)

btn_factor=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="!",hover=False,command=lambda:display_input(_input="factorial("))
btn_factor.place(y=165,x=205)

btn_takeres=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="Resultat",hover=False,command=utiliser_res)
btn_takeres.place(y=225,x=25)



btn_tan=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="Tang",hover=False,command=lambda:display_input(_input='tan(radians('))
btn_tan.place(y=105,x=145)

open_parenths=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text="(",hover=False,command=lambda:display_input(_input='('))
open_parenths.place(y=45,x=205)
close_parenths=ctk.CTkButton(tab1.tab("Scientifique"),width=38,height=38,fg_color="#36C8F5",
                         bg_color=root.cget('bg'),text=")",hover=False,command=lambda:display_input(_input=')'))
close_parenths.place(y=105,x=205)
#--------------Mode equations ...........!!! Interessants !!
#----------Fonction de resoudre l'equation 
def resoudre_eq():
    x=Inconnu.get()
    X=sympy.symbols(x)
    egal_a=egal_entry.get()
    equation=sympy.sympify(Equation.get()+'-'+egal_a)
    
    solution_o=sympy.solve(equation,X)
    solu_affiche=str(solution_o)
    solu_affiche=solu_affiche.replace('[','')
    solu_affiche=solu_affiche.replace(']','')
    
    label_solution.configure(text=solu_affiche,font=('arial',18))
    Inconnu.config(state='disabled')
    Equation.config(state='disabled')
    egal_entry.config(state='disabled')



#Interface graphique de cette resolutions......
Inconnu=ctk.CTkEntry(tab1.tab("Resolutions"),width=63,height=39,bg_color="#949492",
                     font=('arial',14))
Inconnu.place(y=35,x=155)

Inconnu_label=ctk.CTkLabel(tab1.tab("Resolutions"),font=('arial',17),text='Inconnu ici')
Inconnu_label.place(y=44,x=70)

Equation=ctk.CTkEntry(tab1.tab("Resolutions"),font=('arial',15),placeholder_text='Votre equation ici...',
                      height=58,width=178)
Equation.place(y=85,x=18)

egal_label=ctk.CTkLabel(tab1.tab("Resolutions"),font=('arial',17),text='=',bg_color=tab1.cget('bg_color'))
egal_label.place(y=105,x=198)

egal_entry=ctk.CTkEntry(tab1.tab("Resolutions"),font=('arial',15),placeholder_text='Egal??',
                      height=58,width=42)
egal_entry.place(y=87,x=216)

Resoudre_btn=ctk.CTkButton(tab1.tab("Resolutions"),fg_color="red",bg_color=tab1.cget('bg_color'),
                           text='Resoudre',font=('arial',17),command=resoudre_eq)
Resoudre_btn.place(y=160,x=76)

label_solution=ctk.CTkLabel(tab1.tab("Resolutions"),fg_color=tab1.cget('bg_color'),font=('arial',12),
                            text="--Votre solutions s'affiche ici--")
label_solution.place(y=210,x=11)



root.mainloop()

seq='sin(radians(90))'
print(eval(seq))