import matplotlib.pyplot as plt

def plot_survivors_deceased(survival_chances, deceased_chances, k, width, tick_labels,variable):
    fig = plt.figure()
    ax = fig.add_axes([0,1,1,1])

    classes = range(0,k)
    width = .5

    ax.barh(classes,deceased_chances,width, color= "r", tick_label = tick_labels)
    ax.barh(classes,survival_chances,width,left = deceased_chances, color= "b")

    ax.set_ylabel(variable)
    ax.set_yticks(classes,tick_labels)
    ax.legend(labels = ("Deceased","Survived"),bbox_to_anchor=(0.65, 1.25))
    
    plt.show()
    
    return