# Manages configurable parameters such as API limits and model paths.


import yaml 

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)


YT_MAX_RESULTS = config.get("yt_api", {}).get("max_results",100)
MAX_COMMENTS=config.get('data',{}).get('max_comments',500)
SENTIMENT_MODEL=config.get('model',{}).get('model_path')
VECTORIZER_MODEL=config.get('model',{}).get('vectorizer_path')
