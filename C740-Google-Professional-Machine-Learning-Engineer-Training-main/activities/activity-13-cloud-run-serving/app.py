from flask import Flask,request,jsonify
app=Flask(__name__)
@app.get('/health')
def health(): return {'status':'ok','model_version':'v8-demo'}
@app.post('/predict')
def predict():
 d=request.get_json(silent=True) or {}
 if not isinstance(d.get('features'),list) or len(d['features'])!=3: return {'error':'features must contain 3 numbers'},400
 score=sum(map(float,d['features']))/30; return jsonify(score=max(0,min(1,score)),model_version='v8-demo')
if __name__=='__main__': app.run('0.0.0.0',8080)
