from statsmodels.stats.power import tt_ind_solve_power
from tkinter import *
from math import *

def evaluate_power1():
    
    if (not power.get())+(not n.get())+(not es.get())+(not alpha.get()) == 0:
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "At least 1 blank")
    
    elif (not power.get())+(not n.get())+(not es.get())+(not alpha.get()) > 1:
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "No more than 2 blanks")
        
    elif power.get() and (float(power.get()) >= 1 or float(power.get()) <= 0):
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "Invalid power")

    elif alpha.get() and (float(alpha.get()) >= 1 or float(alpha.get()) <= 0):
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "Invalid alpha")

    elif n.get() and (int(n.get()) < 1 or int(n.get()) != float(n.get())):
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "Invalid sample size")
        
    else:
        
        Errmsg.delete(0, 'end')

        if not power.get():
            
            result = tt_ind_solve_power(effect_size = float(es.get()), nobs1=int(n.get()), alpha=float(alpha.get()), 
                                    alternative=testtype.get())
            power.delete(0, 'end')
            power.insert(0, round(result, 3))


        elif not n.get():
            
            result = tt_ind_solve_power(effect_size = float(es.get()), alpha=float(alpha.get()), 
                                    alternative=testtype.get(), power=float(power.get()))
            n.delete(0, 'end')
            n.insert(0, ceil(result))

        elif not es.get():
            result = tt_ind_solve_power(alpha=float(alpha.get()), nobs1=int(n.get()),
                                    alternative=testtype.get(), power=float(power.get()))
            es.delete(0, 'end')
            es.insert(0, round(result, 2))

        elif not alpha.get():
            result = tt_ind_solve_power(effect_size = float(es.get()), nobs1=int(n.get()),
                                    alternative=testtype.get(), power=float(power.get()))
            alpha.delete(0, 'end')
            alpha.insert(0, round(result, 2))
            
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, 'Done')


def evaluate_power2(event):
    
    if (not power.get())+(not n.get())+(not es.get())+(not alpha.get()) == 0:
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "At least 1 blank")
    
    elif (not power.get())+(not n.get())+(not es.get())+(not alpha.get()) > 1:
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "No more than 2 blanks")
        
    elif power.get() and (float(power.get()) >= 1 or float(power.get()) <= 0):
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "Invalid power")

    elif alpha.get() and (float(alpha.get()) >= 1 or float(alpha.get()) <= 0):
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "Invalid alpha")

    elif n.get() and (int(n.get()) < 1 or int(n.get()) != float(n.get())):
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, "Invalid sample size")
        
    else:
        
        Errmsg.delete(0, 'end')

        if not power.get():
            
            result = tt_ind_solve_power(effect_size = float(es.get()), nobs1=int(n.get()), alpha=float(alpha.get()), 
                                    alternative=testtype.get())
            power.delete(0, 'end')
            power.insert(0, round(result, 3))


        elif not n.get():
            
            result = tt_ind_solve_power(effect_size = float(es.get()), alpha=float(alpha.get()), 
                                    alternative=testtype.get(), power=float(power.get()))
            n.delete(0, 'end')
            n.insert(0, ceil(result))

        elif not es.get():
            result = tt_ind_solve_power(alpha=float(alpha.get()), nobs1=int(n.get()),
                                    alternative=testtype.get(), power=float(power.get()))
            es.delete(0, 'end')
            es.insert(0, round(result, 2))

        elif not alpha.get():
            result = tt_ind_solve_power(effect_size = float(es.get()), nobs1=int(n.get()),
                                    alternative=testtype.get(), power=float(power.get()))
            alpha.delete(0, 'end')
            alpha.insert(0, round(result, 2))
            
        Errmsg.delete(0, 'end')
        Errmsg.insert(0, 'Done')
    

def evaluate_power():
    try:
        evaluate_power2(event)
    except:
        evaluate_power1()
    

if __name__ == "__main__":
    
    w = Tk()
    w.geometry("500x200")
    w.title("Two sample t-test power calculator")

    row = 0

    Label(w, text="Leave blank what you want to calculate!").grid(row=row, columnspan=2)

    row += 1

    Label(w, text="Effect size (d):").grid(row=row, sticky=W)
    es = Entry(w)
    es.insert(0, 0.5)
    es.grid(row=row, column=1)

    row += 1

    Label(w, text="Sample size per group:").grid(row=row, sticky=W)
    n = Entry(w)
    n.insert(0, 20)
    n.grid(row=row, column=1)

    row += 1

    Label(w, text="Significance Level:").grid(row=row, sticky=W)
    alpha = Entry(w)
    alpha.insert(0, 0.05)
    alpha.grid(row=row, column=1)

    row += 1

    Label(w, text="Power:").grid(row=row, sticky=W)
    power = Entry(w)
    power.grid(row=row, column=1)

    row += 1

    Label(w, text="Test type:").grid(row=row, sticky=W)

    testtype = StringVar(w)
    testtype.set("two-sided") # default value

    entry_testtype = OptionMenu(w, testtype, "two-sided", "larger", "smaller")
    entry_testtype.grid(row=row, column=1, sticky=W)

    row += 1

    Label(w, text="Message: ").grid(row=row, sticky=W)
    Errmsg = Entry(w)
    Errmsg.grid(row=row, column=1, columnspan=3)
    Errmsg.insert(0, "Ready")

    row += 1

    b = Button(w, text="Compute", command=evaluate_power)
    b.grid(row=row, columnspan=2)


    w.mainloop()
