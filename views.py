
def wine_classification(request):
    
    features = ['alcohol',
 'malic_acid',
 'ash',
 'alcalinity_of_ash',
 'magnesium',
 'total_phenols',
 'flavanoids',
 'nonflavanoid_phenols',
 'proanthocyanins',
 'color_intensity',
 'hue',
 'od280/od315_of_diluted_wines',
 'proline']
    
    if request.method == 'POST':
        data = request.POST
        
        feature_values = {'alcohol':float(data.get('alcohol')),
 'malic_acid':float(data.get('malic_acid')),
 'ash':float(data.get('ash')),
 'alcalinity_of_ash':float(data.get('alcalinity_of_ash')),
 'magnesium':float(data.get('magnesium')),
 'total_phenols':float(data.get('total_phenols')),
 'flavanoids':float(data.get('flavanoids')),
 'nonflavanoid_phenols':float(data.get('nonflavanoid_phenols')),
 'proanthocyanins':float(data.get('proanthocyanins')),
 'color_intensity':float(data.get('color_intensity')),
 'hue':float(data.get('hue')),
 'od280/od315_of_diluted_wines':float(data.get('od280/od315_of_diluted_wines')),
 'proline':float(data.get('proline'))}
        
        print(feature_values)
        
        y_pred = wine_model.predict([list(feature_values.values())])[0]
        
        if y_pred == 0:
            y_pred = 'Class 0'
        elif y_pred == 1:
            y_pred = 'Class 1'
        elif y_pred == 2:
            y_pred = 'Class 2'
            
        print(y_pred)
        return render(request,'wine_prediction.html',{'features':features,'op':y_pred})
    return render(request,'wine_prediction.html',{'features':features})
