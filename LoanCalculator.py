from tkinter import Tk, Label, Button, StringVar, Entry

class LoanCalculators():
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.configure(background="light Gray")
        window.geometry("450x300")
        window.resizable(width=False,height=False)

        self.annual_intrest_rate = StringVar()
        #self.annual_intrest_rate.set("")
        self.number_of_years = StringVar()
        #self.annual_intrest_rate.set("")
        self.loan_amount = StringVar()
        #self.annual_intrest_rate.set("")
        self.monthly_payment = StringVar()
        #self.annual_intrest_rate.set("")
        self.total_payment = StringVar()
        #self.total_payment.set("")
########################################################
        annual_intrest_rate_label = Label(window,text ="Annual Intrest Rate",fg="blue")
        annual_intrest_rate_label.grid(column=0,row=0,padx=15,pady=15)

        annual_intrest_rate_entry = Entry(window,textvariable = self.annual_intrest_rate,width=14)
        annual_intrest_rate_entry.grid(column=1,row=0,padx=15,pady=15)
########################################################
        number_of_years_label = Label(window,text ="Number of years",fg="blue")
        number_of_years_label.grid(column=0,row=1,padx=15,pady=15)

        number_of_years_entry = Entry(window,textvariable = self.number_of_years,width=14)
        number_of_years_entry.grid(column=1,row=1,padx=15,pady=15)
########################################################
        loan_amount_label = Label(window,text ="Annual Intrest Rate",fg="blue")
        loan_amount_label.grid(column=0,row=2,padx=15,pady=15)

        loan_amount_entry = Entry(window,textvariable = self.loan_amount,width=14)
        loan_amount_entry.grid(column=1,row=2,padx=15,pady=15)
########################################################
        monthly_payment_label = Label(window,text ="Monthly payment",fg="blue")
        monthly_payment_label.grid(column=0,row=3,padx=15,pady=15)

        monthly_payment_entry = Entry(window,textvariable = self.monthly_payment,width=14)
        monthly_payment_entry.grid(column=1,row=3,padx=15,pady=15)
########################################################
        total_payment_label = Label(window,text ="Annual Intrest Rate",fg="blue")
        total_payment_label.grid(column=0,row=4,padx=15,pady=15)

        total_payment_entry = Entry(window,textvariable = self.total_payment,width=14)
        total_payment_entry.grid(column=1,row=4,padx=15,pady=15)
#########################################################
        Calculat_btn = Button(window,text="Calculate",bg="orange",fg="white",command="")
        Calculat_btn.grid(column=0,row=5,padx=15,pady=15)

        Clear_btn = Button(window,text="Clear",bg="orange",fg="white",command="")
        Clear_btn.grid(column=1,row=5,padx=15,pady=15)
#########################################################
    def Calculator_loan(self):
        annual_intrest_rate_value = float(self.annual_intrest_rate.get())
        number_of_years_value = float(self.number_of_years.get())
        loan_amount_value = float(self.loan_amount.get())

        #monthly_payment_value
        #total_payment_value



        window.mainloop()

LoanCalculators()
