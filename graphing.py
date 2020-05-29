import matplotlib.pyplot as plt

def graphScatter(x, y):
    plt.scatter(x, y)
    plt.title('Insert Graph Title Here')
    plt.xlabel('New Cases')
    plt.ylabel('Total Cases')
    plt.show()

def graphLogScatter(x, y):
    plt.scatter(x, y)
    plt.xscale("log")
    plt.yscale("log")
    plt.title('Insert Graph Title Here')
    plt.xlabel('New Cases')
    plt.ylabel('Total Cases')
    plt.show()

def graphPlot(x, y):
    plt.plot(x, y)
    plt.title('Insert Graph Title Here')
    plt.xlabel('New Cases')
    plt.ylabel('Total Cases')
    plt.show()

def graphLogPlot(x, y):
    plt.plot(x, y)
    plt.xscale("log")
    plt.yscale("log")
    plt.title('Insert Graph Title Here')
    plt.xlabel('Total Cases')
    plt.ylabel('New Cases')
    plt.show()

def graphPLogPlot(x, y, name):
    plt.plot(x, y)
    plt.xscale("log")
    plt.title(name)
    plt.xlabel('Total Cases')
    plt.ylabel('New Cases')
    plt.grid(True)
    plt.show()

def multiGraphPLogPlot(x, y, x_1, y_1, x_2, y_2, name):
    """
    Compare daily, 3 day average and 5 day average plots of
    Total Cases vs New Cases
    """
    plt.plot(x, y)
    plt.plot(x_1, y_1)
    plt.plot(x_2, y_2)
    plt.legend('ABC')
    plt.xscale("log")
    plt.title(name)
    plt.xlabel('Total Cases')
    plt.ylabel('New Cases')
    plt.grid(True)
    plt.savefig('mGPLP.png')
    plt.show()
