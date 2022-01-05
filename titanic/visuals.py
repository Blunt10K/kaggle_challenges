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
    ax.set_xlabel("Proportion")

    
    plt.show()
    
    return

def plot_age_distribution(ages):
    fig = plt.figure(figsize=(15,2))
    ax = fig.add_axes([0,1,1,1])

    plt.vlines(x = ages, ymin = -0.01,ymax=0.01, colors='r')
    plt.ylim((-0.05,0.05))
    plt.xlim((0,max(ages)+1))
    plt.xlabel("Age / Years")
    plt.xticks(range(0,85,5))
    
    return