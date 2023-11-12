from joblib import load
import pandas as pd

model = load('./model/svc_pipeline.joblib')

# Feature order: ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health']
# Request body: 
#    {  parents,
#       childsNursery,
#       familyForm,
#       children,
#       housing,
#       finance,
#       familySocial,
#       familyHealth
#    }

predicted_to_rank_map =  {
    0: 'Not Recommended',
    1: 'Very Recommended',
    2: 'Priority',
    3: 'Special Priority'
}

def get_features(body):
    return pd.DataFrame({ 
        'parents': [body['parents']], 
        'has_nurs': [body['childsNursery']], 
        'form': [body['familyForm']],
        'children': [body['children']], 
        'housing': [body['housing']], 
        'finance': [body['finance']], 
        'social': [body['familySocial']], 
        'health': [body['familyHealth']]
    })

def post_process(predicted):
    return predicted_to_rank_map[predicted[0]]


def rank_nursery_application(body):
    features = get_features(body)
    predicted = model.predict(features)
    print(predicted)
    return post_process(predicted)
