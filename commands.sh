ssh-keygen -t rsa

git clone git@github.com:oyin-bam/flask-ml-service.git

cd flask-ml-service

python3 -m venv venv

venv/bin/activate

make all

az webapp up --sku F1 -n bam-flask-app

az webapp log tail

./make_predict_azure_app.sh