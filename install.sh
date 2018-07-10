sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get install -y python-dev rabbitmq-server supervisor libatlas-base-dev liblapack-dev gfortran
pip install funcsigs
pip install pbr
pip install six
pip install numpy
# export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-linux_x86_64.whl
rm -r six*
pip install tensorflow-0.12.1-cp27-none-linux_x86_64.whl
pip install celery
pip install jieba
