import matplotlib.pyplot as plt


def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'):  # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data


if __name__ == '__main__':
    # Load score data
    class_kr = read_data('data/class_score_kr.csv')
    class_en = read_data('data/class_score_en.csv')

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]
    # midterm_en, final_en = [0, 0]
    # total_en = [0]

    # TODO) Plot midterm/final scores as points
    plt.figure()
    plt.scatter(midterm_kr, final_kr, label='Korean', c='red')
    plt.scatter(midterm_en, final_en, label='English', c='blue', marker='+')
    plt.xlabel('Midterm scores')
    plt.ylabel('Final scores')
    plt.legend()
    plt.xlim(left=0)
    plt.ylim(bottom=0, top=100)
    plt.grid(which='both', linestyle='-',
             linewidth=0.5, color='gray', axis='both')
    plt.show()

    # TODO) Plot total scores as a histogram
    plt.figure()
    bins = list(range(0, 101, 5))  # bins with a width of 5
    plt.hist(total_kr, bins=bins, alpha=0.5, label='Korean', color='red')
    plt.hist(total_en, bins=bins, alpha=0.5, label='English', color='violet')
    plt.xlabel('Total scores')
    plt.ylabel('The number of students')
    plt.legend()
    plt.xlim(left=0, right=100)  # set the x-axis range
    plt.ylim(bottom=0)
    plt.show()
