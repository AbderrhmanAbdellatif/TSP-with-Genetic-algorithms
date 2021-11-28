# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:37:50 2021

@author: aellatif
"""


## from Tkinter import *
from time import sleep
from tkinter import filedialog
## import ttk
import threading
from tkinter import *
from tkinter import ttk


import threading

import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Tsp_Read_File import *
from TspDistance import *
from Init_poplist import *
from TspGen import *
matplotlib.use('TkAgg')
root = Tk()
root.title("TSP Solver")# title of frame
root.geometry("1004x768")# cozumluk sekili

text_cx = Label(root, bg='black', fg="white", width=1, font=('times', 12, 'bold'))
text_cx.grid(row=6, column=1, sticky=(W, N, S, E))
text_cy = Label(root, bg='black', fg="white", font=('times', 12, 'bold'))
text_cy.grid(row=7, column=1, sticky=(W, N, S, E))
def on_move(event):
    # get the x and y pixel coords
    x, y = event.x, event.y

    if event.inaxes:
        ax = event.inaxes  # the axes instance
        text_cx.config(text='data coords X %f' % (round(event.xdata, 1)))
        text_cy.config(text='data coords Y %f' % (round(event.ydata, 1)))

class VisualSolve:
    def __init__(self,master):
        self.city_coords=self.read_file().city_coords
        self.city_tour_init=self.read_file().city_tour_init
        self.temp = []
        self.local_temp = []
        self.best_tour = []
        self.master = master
        self.newtsp = []
        self.init_plot(master)
        self.frame = Frame(master)
        self.frame = Frame(width=150, height=500, bg="lightblue", bd=1, relief=SUNKEN)
        self.frame.grid(row=1, column=2, columnspan=2, rowspan=2, sticky=(E, W, N, S))
        self.button_open_tsp_file = ttk.Button(master, text='Open TSP file', command=self.openfile)
        self.button_open_tsp_file.grid(row=0, column=1, sticky=W)
        self.add_distance_visual_element(master)
    def read_file(self):
        newtsp = TSPParser("CitiesCoordinates.tsp")
        return newtsp
    def Setpopultion(self):
        new_pop = self.create_init_pop(self.city_coords, self.city_tour_init)  # first generte pop list 100
        print('popultion list ', new_pop)
        return new_pop
    def give_distances_list(self,new_pop):
        distances_list = []  # here we will store locally tuples of distance cost and tours
        for elem in new_pop:  # soltion steps that mean 100 soltion
            loc_dist = TSPDistance(elem, self.city_coords)  # take the list and the coor that given in file
            distances_list.append((loc_dist.distance_cost, loc_dist.tourlist))  # sum the distances of all sotion steps
        return distances_list
    def find_the_shortest_path(self,new_pop):
        self.temp = sorted(self.give_distances_list(new_pop), key=lambda x: x[0])
        shortest_path = []
        shortest_path_distance_cost = min(i[0] for i in self.temp)  # take the min in list the sum
        print('shortest_path_distance_cost ',shortest_path_distance_cost)
        for i in self.temp:# find the path that it have a lowest cost
            if i[0] == shortest_path_distance_cost:
                shortest_path = (i[1])
        print('path lowst cost ',shortest_path)
        shortest_path_tuples = []#add the coords in this list
        for city in shortest_path:
            shortest_path_tuples.append(self.city_coords.get(city)) #find coords in this list
        print("shortest path coords ", shortest_path_tuples)
        self.best_tour.append((shortest_path_distance_cost, shortest_path)) #add to list best tour
        self.update_visual_current_distance(shortest_path_distance_cost)
        self.plot_tour(shortest_path_tuples)
        button1 = Button(self.frame, text="Create children", pady=3, command=lambda: self.crossover(new_pop))
        button1.grid(row=4, column=0, columnspan=2, sticky=(E, W, N, S))
    def crossover(self,new_pop):#make crossover
        tspGeneticAlgo=TSPGeneticAlgo()
        distance_list=sorted(self.give_distances_list(new_pop), key=lambda x: x[0],reverse=True)
        print('distance cost')
        print(distance_list[0])  # take the wors index
        print(distance_list[1])  # and seconde worst index
        print('distance list')
        print(distance_list[0][1])# take the wors index
        print(distance_list[1][1])# and seconde worst index
        children=tspGeneticAlgo.crossover(distance_list[0][1],distance_list[1][1])#make crossover and get childerin
        children_list=[]
        for index in range(len(distance_list)-1):
            children_list.append(distance_list[index][1])

        # replace two childern with Parent
        print('childern list')
        children_list[0]=children[0].copy()
        children_list[1]=children[1].copy()

        print(children_list[0])# take the wors index
        print(children_list[1])# and seconde worst index
        print('calculte the cost after crossover')
        #calculte the cost after crossover
        children_list_costs=self.give_distances_list(children_list)
        for children_list in children_list_costs:
            print(children_list)

    def update_visual_current_distance(self, distance):
        """
            Each time we want to update the distance on the GUI
            we call this passing the distance as parameter
        """
        self.text_distance.config(state=NORMAL)
        self.text_distance.delete('1.0', '2.0')
        self.text_distance.insert('1.0', distance)
        self.text_distance.config(state=DISABLED)
    def create_init_pop(self, init_dict, init_tour):
        """
            We create the initial population with TSPInitialPopulation class
            we pass the dict with cities and coordinates and the initial tour
        """
        self.initial_population_size = self.w.get()
        print('population size ',self.initial_population_size)
        new_pop = TSPInitialPopulation(init_dict, init_tour, self.initial_population_size)  # plus the population initial size (here is 200)
        return new_pop.pop_group  # retrun  the soltion steps random  array equal 100
    def openfile(self, frame1=None):
        """
            This is called when the button button_open_tsp_file is pressed
            it opens the tkinter file dialog , passes the selected file to
            the parser class and process as needed.
        """
        filename = filedialog.askopenfilename()
        self.newtsp = TSPParser(filename)


        # from this line to the end of else we check if there is an error on the parser
        # if there is an error we display it, else we parse the file normally and we
        # plot the instance of the problem
        if self.newtsp.display_status:
            if frame1:
                frame1.destroy()
            frame1 = Frame(width=800, height=100, bg="red", bd=1, relief=SUNKEN)
            frame1.grid(row=2, column=1, sticky=W)
            label_distance1 = ttk.Label(frame1, text="Error:", background='red', font=('times', 12, 'bold'))
            label_distance1.grid(row=0, column=0, sticky=W)
            text_error = Text(frame1, width=90, height=1, bg='black', fg="red", font=('times', 12, 'bold'))
            text_error.grid(row=0, column=1, sticky=(W, N, S, E))
            text_error.config(state=NORMAL)
            text_error.delete('1.0', '2.0')
            text_error.insert('1.0', self.newtsp.display_status)
            text_error.config(state=DISABLED)
        else:
            if frame1:
                frame1.destroy()
            frame1 = Frame(width=800, height=100, bg="lightgreen", bd=1, relief=SUNKEN)
            frame1.grid(row=2, column=1, sticky=W)
            label_distance1 = ttk.Label(frame1, text="File opened:", background="lightgreen",
                                        font=('times', 12, 'bold'))
            label_distance1.grid(row=0, column=0, sticky=W)
            text_error = Text(frame1, width=85, height=1, bg='lightgreen', fg="blue", font=('times', 12, 'bold'))
            text_error.grid(row=0, column=1, sticky=(W, N, S, E))
            text_error.config(state=NORMAL)
            text_error.delete('1.0', '2.0')
            text_error.insert('1.0', self.newtsp.filename)
            text_error.config(state=DISABLED)

            self.plot_points(self.newtsp.city_tour_tuples)# ('41', '49'), ('35', '17'), ('55', '45'), ('55', '20'), ('15', '30'), ('25', '30'), polt this coor
            self.init_tour = self.newtsp.city_tour_init # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
            self.city_coords = self.newtsp.city_coords # 1: ('41', '49'), 2: ('35', '17'), 3: ('55', '45'), 4: ('55', '20')

            self.current_tour_distance = TSPDistance(self.newtsp.city_tour_init, self.newtsp.city_coords)
            self.update_visual_current_distance(self.current_tour_distance.distance_cost)
            self.create_initial_population_visual_element()
    def plot_tour(self, tour_tuples):
        """
            We call this passing the list of tuples with city
            coordinates to plot the tour we want on the GUI
        """
        tour_tuples.append(tour_tuples[0])
        data_in_array = np.array(tour_tuples)
        transposed = data_in_array.T
        x, y = transposed
        plt.ion()
        self.a.cla()
        self.a.plot(x, y, 'ro')
        self.a.plot(x, y, 'b-')
        self.canvas.draw()
    def init_plot(self, master):# sekili tasarm yapilmasi
        """
            Create an empty initial plot to instantiate the GUI layout
        """
        b = Figure(figsize=(8, 6), dpi=100)
        ac = b.add_subplot(111)
        ac.plot(10, 10)
        ac.set_title('Current tour plot')
        ac.set_xlabel('X axis coordinates')
        ac.set_ylabel('Y axis coordinates')
        ac.grid(True)
        canvas = FigureCanvasTkAgg(b, master)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1, sticky=W)
    def add_distance_visual_element(self, master):
        label_distance = ttk.Label(master, text="Current distance:", background='lightgreen',
                                   font=('times', 12, 'bold'))
        label_distance.grid(row=0, column=2, sticky=(W, N, S, E))
        # this get changed from update_current_visual_distance
        self.text_distance = Text(master, width=10, height=1, bg='lightgreen', fg="red", font=('times', 12, 'bold'))
        self.text_distance.grid(row=0, column=3, sticky=(W, N, S, E))
    def plot_points(self, tour_tuples):
        """
            We call this passing the list of tuples with city
            coordinates to plot the tour we want on the GUI
        """
        data_in_array = np.array(tour_tuples)#[('41', '49'), ('35', '17'), ('55', '45'), ('55', '20'), ('15', '30')
        transposed = data_in_array.T # transposed
        x, y = transposed
        plt.ion()
        # self.f, self.a = plt.subplots(1, 1)
        self.f = Figure(figsize=(8, 6), dpi=100)
        self.a = self.f.add_subplot(111, navigate=True)
        self.a.plot(x, y, 'ro')
        # self.a.plot(x, y, 'b-')
        self.a.set_title('Current best tour')
        self.a.set_xlabel('X axis coordinates')
        self.a.set_ylabel('Y axis coordinates')
        self.a.grid(True)
        self.canvas = FigureCanvasTkAgg(self.f, master=root) # self.f skilde coor , root is equl tk
        self.canvas.mpl_connect('motion_notify_event', on_move)
        self.canvas.get_tk_widget().grid(row=1, column=1, sticky=W)
        self.canvas.draw()
        #sleep(1000)
    def create_initial_population_visual_element(self):
        var = StringVar(self.frame)
        var.set("shuffle")  # initial value
        label_distance = ttk.Label(self.frame, text="Select mode:", background='lightgreen', font=('times', 12, 'bold'))
        label_distance.grid(row=0, column=0, sticky=(W, N, S))
        option1 = OptionMenu(self.frame, var, "shuffle", "elitism")
        option1.grid(row=0, column=1, sticky=(W, N, S))
        label_population = ttk.Label(self.frame, text="Choose population size", background="lightblue",
                                     font=('times', 12, 'bold'))
        label_population.grid(row=1, column=0, columnspan=2, sticky=(E, W, N, S))
        self.w = Scale(self.frame, from_=100, to=1000, resolution=10, orient=HORIZONTAL)
        self.w.grid(row=2, column=0, columnspan=2, sticky=(E, W, N, S))
        button = Button(self.frame, text="Create initial population", pady=5,
                        command=lambda: self.find_the_shortest_path(self.Setpopultion()))
        button.grid(row=3, column=0, columnspan=2, sticky=(E, W, N, S))

tsp=VisualSolve(root)
root.mainloop()
