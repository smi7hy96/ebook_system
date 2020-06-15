from classes.gui_class import *

root = tk.Tk()
root.title('E-Book System')
main = MainView(root)
main.pack(side="top", fill="both", expand=True)
root.wm_geometry("400x400")
root.mainloop()
