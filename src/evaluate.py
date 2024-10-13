from sklearn.metrics import classification_report, confusion_matrix



def evaluate_model(y_true, y_pred):
    # Calcular la matriz de confusión
    conf_matrix = confusion_matrix(y_true, y_pred)
    print("Confusion Matrix:")
    print(conf_matrix)
    
    # Calcular el reporte de clasificación
    class_report = classification_report(y_true, y_pred)
    print("Classification Report:")
    print(class_report)