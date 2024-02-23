git clone https://github.com/Zhengwen-Lan/redcaps-downloader.git
cp -r redcaps-downloader/* .
pip install -r requirements.txt
python setup.py develop
wget https://www.dropbox.com/s/cqtdpsl4hewlli1/redcaps_v1.0_annotations.zip
mkdir data
unzip redcaps_v1.0_annotations.zip -d data