import pandas as pd
import tkinter.ttk as ttk
import tkinter as tk
import chartify
import tkinter.messagebox

gdp=pd.read_csv("gdp.csv")

def windows(event):
    # ------取得所有國家名(不重複)------------
    allcountry = gdp["country"]
    country = []
    for n in allcountry.values:
        if not n in country:#若不再裡面才加入
            country.append(n)

    # ------取得所有地區名(不重複)------------
    allcontinent = gdp["continent"]
    continent = []
    for n in allcontinent.values:
        if not n in continent:#若不再裡面才加入
            continent.append(n)

        # print("------------------地區排序lifeExp在listbox內----------------------------")
        def CS1(event):
            s1 = gdp["continent"] == continent[cob1.current()]
            s2 = gdp[s1].sort_values(by="lifeExp", ascending=True)

            lbx = tk.Listbox(window, selectmode="browse")  # listbox
            lbx.pack_forget()  # 清理舊資料

            cont = 0
            for n in s2["lifeExp"]:
                lbx.insert(cont, n)
                cont += 1
            lbx.pack(fill='both', expand=1)
            # -------------圖片化-------------------
            ch = chartify.Chart()
            ch.plot.scatter(
                data_frame=s2,
                x_column='year',
                y_column='lifeExp')
            ch.set_title("年與lifeExp關係")
            ch.set_subtitle('Chartify 內建數據')
            ch.set_source_label('Chartify')
            ch.axes.set_xaxis_label('年')
            ch.axes.set_yaxis_label('lifeExp')
            ch.show('png')
            ch.save("ch.html")

            tk.messagebox.showinfo(title='chartify', message="地區資料已存入ch.html")
            window.destroy()
        # -------------------國家GDP資料---------------------------------
        def CS2(event):
            s1 = gdp["country"] == country[cob1.current()]
            s2 = gdp[s1].sort_values(by="lifeExp", ascending=True)

            lbx = tk.Listbox(window, selectmode="browse")  # listbox
            lbx.pack_forget()  # 清理舊資料

            cont = 0
            for n in s2["gdpPercap"]:
                lbx.insert(cont, n)
            cont += 1
            lbx.pack(fill='both', expand=1)
            # -------------圖片化-------------------
            ch = chartify.Chart()
            ch.plot.scatter(
                data_frame=s2,
                x_column='year',
                y_column="gdpPercap")
            ch.set_title("年與gdpPercap關係")
            ch.set_subtitle('Chartify 內建數據')
            ch.set_source_label('Chartify')
            ch.axes.set_xaxis_label('年')
            ch.axes.set_yaxis_label('gdpPercap(億)')
            ch.show('png')
            ch.save("gdp.html")
            tk.messagebox.showinfo(title='chartify', message="gdp資料已存入gdp.html")
            window.destroy()

        def CS3(event):
            AG = gdp.groupby(by="country")  # by=可不加
            G = AG["pop", "gdpPercap"]
            MEAN = G.mean()
            pd.set_option("display.max_rows", 100)
            lbl1=tk.Label(window,text=MEAN)
            lbl1.pack()


            #-------------圖片化-------------------
            ch = chartify.Chart()
            ch.plot.scatter(
                data_frame=MEAN,
                x_column='pop',
                y_column="gdpPercap")
            ch.set_title("pop與gdpPercap關係")
            ch.set_subtitle('Chartify 內建數據')
            ch.set_source_label('Chartify')
            ch.axes.set_xaxis_label('pop')
            ch.axes.set_yaxis_label('gdpPercap(億)')
            ch.show('png')
            ch.save("pop_and_gdp_AVG.html")
            tk.messagebox.showinfo(title='chartify', message="gdp資料已存入pop_and_gdp_AVG.html")
            window.destroy()
        # ------------選國家(GPD)/地區(lifeExp)------------------------
    cob = ttk.Combobox(window, width=100, values=["國家GDP", "地區lifeExp","pop&gdp groupby"])
    cob.pack()
    cob1 = ttk.Combobox(window, width=100)
    def select(event):
        print(cob.current())
        if cob.current() == 1:
            cob1=ttk.Combobox(window,width=100,values=country)
            cob1.pack()
            cob1.bind('<<ComboboxSelected>>', CS2)
        elif cob.current() == 0:
            cob1 = ttk.Combobox(window, width=100, values=continent)
            cob1.pack()
            cob1.bind('<<ComboboxSelected>>', CS1)
        elif cob.current() == 2:
            cob1 = ttk.Combobox(window, width=100, values=country)
            cob1.pack()
            cob1.bind('<<ComboboxSelected>>', CS3)
    cob.bind('<<ComboboxSelected>>', select)
    cob.pack()



#----------------------------------視窗本體-------------------------------------
window = tk.Tk()
window.title("GDP資料")
window.geometry("800x600")
LOAD_Label=tk.Label(window,text="輸入地區",bg="#87CEEB",font=('Arial', 10), width=15, height=2)
LOAD_Label.pack()
windows("")
window.mainloop()




