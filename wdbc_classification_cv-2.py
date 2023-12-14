import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics, tree, model_selection
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from matplotlib.lines import Line2D

# Function to load the WDBC data
def load_wdbc_data(filename):
    class WDBCData:
        data = []  # Shape: (569, 30)
        target = []  # Shape: (569, )
        target_names = ['malignant', 'benign']
        feature_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
                         'mean smoothness', 'mean compactness', 'mean concavity',
                         'mean concave points', 'mean symmetry', 'mean fractal dimension',
                         'radius error', 'texture error', 'perimeter error', 'area error',
                         'smoothness error', 'compactness error', 'concavity error',
                         'concave points error', 'symmetry error', 'fractal dimension error',
                         'worst radius', 'worst texture', 'worst perimeter', 'worst area',
                         'worst smoothness', 'worst compactness', 'worst concavity',
                         'worst concave points', 'worst symmetry', 'worst fractal dimension']
    wdbc = WDBCData()
    with open(filename) as f:
        for line in f.readlines():
            items = line.split(',')
            wdbc.target.append(0 if items[1] == 'M' else 1)
            wdbc.data.append([float(i) for i in items[2:]])
        wdbc.data = np.array(wdbc.data)
    return wdbc

if __name__ == '__main__':
    # SVM Classifier
    # Load a dataset
    wdbc = load_wdbc_data('data/wdbc.data')

    # Create a pipeline with a scaler and SVM classifier
    pipeline = make_pipeline(StandardScaler(), svm.SVC(C=10, kernel='rbf', gamma='scale'))

    # Train the model
    pipeline.fit(wdbc.data, wdbc.target)

    # Test the model
    predict = pipeline.predict(wdbc.data)
    accuracy_svm = metrics.balanced_accuracy_score(wdbc.target, predict)
    print("SVM Classifier Accuracy:", accuracy_svm)

    # Visualize the confusion matrix for SVM
    cm_svm = metrics.confusion_matrix(wdbc.target, predict)
    plt.figure()
    plt.imshow(cm_svm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix - SVM Classifier')
    plt.colorbar()
    plt.xlabel('Predicted')
    plt.ylabel('True')
    tick_marks = np.arange(len(wdbc.target_names))
    plt.xticks(tick_marks, wdbc.target_names)
    plt.yticks(tick_marks, wdbc.target_names)
    for i in range(len(wdbc.target_names)):
        for j in range(len(wdbc.target_names)):
            plt.text(j, i, f'{cm_svm[i, j]}', ha='center', va='center', color='black')
    plt.show()
    
    

    # Decision Tree Classifier
    # Load a dataset
    wdbc = datasets.load_breast_cancer()

    # Define a decision tree model with tuned parameters
    model = tree.DecisionTreeClassifier(max_depth=5, min_samples_split=3, min_samples_leaf=1)

    # Perform cross-validation
    cv_results = model_selection.cross_validate(model, wdbc.data, wdbc.target, cv=5, return_train_score=True)

    # Evaluate the model
    acc_train = np.mean(cv_results['train_score'])
    acc_test = np.mean(cv_results['test_score'])
    print(f'* Decision Tree - Accuracy @ training data: {acc_train:.3f}')
    print(f'* Decision Tree - Accuracy @ test data: {acc_test:.3f}')
    print(f'* Your score: {max(10 + 100 * (acc_test - 0.9), 0):.0f}')
