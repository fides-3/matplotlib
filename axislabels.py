import matplotlib.pyplot as plt
year=[1950,1951,1952,2100]
pop=[2.53,2.57,2.62,10.85]

# adding data to the plot
year=[1800,1850,1900] + year
pop=[1.0,1.262,1.650] + pop

plt.plot(year,pop)
plt.xlabel("Year")
plt.ylabel("Population")
plt.yticks([0,2,4,6,8],
           ["0","2B","4B","6B","8B"])
plt.title("World Population Projection")

plt.show()
