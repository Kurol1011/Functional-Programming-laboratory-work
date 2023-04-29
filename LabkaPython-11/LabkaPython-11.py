# import os
# import pandas as pd


# files = os.listdir('data')
# print(files)

# df = pd.DataFrame()

# for file in files:
#     if file.endswith('.csv'):
#         file_path = os.path.join('data', file)
#         temp_df = pd.read_csv(file_path)
#         df = pd.concat([df, temp_df], ignore_index=True)


# output_path = os.path.join('output', 'merged_data.csv')
# df.to_csv(output_path, index=False)


import tkinter as tk


root = tk.Tk()


root.title("Olzhas Logo")


canvas = tk.Canvas(root, width=400, height=400)


canvas.create_oval(50, 50, 350, 350, outline="#aaa8e3", width=20)


canvas.create_text(200, 200, text="L", font=("Helvetica", 250),fill="#8b88cf")


canvas.create_text(230, 200, text="Z", font=("Helvetica", 170),fill="#625fad")


canvas.create_text(200, 165, text="H", font=("Helvetica", 50), fill="#44428f")


canvas.create_text(250, 220, text="A", font=("Helvetica", 30), fill="#211f5e")


canvas.create_text(250, 240, text="S", font=("Helvetica", 20), fill="#100e40")


canvas.pack()


root.mainloop()


