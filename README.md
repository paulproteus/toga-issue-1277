## Steps to run this project

```
python3.7 -m venv env
env/bin/pip install -r requirements.txt
source env/bin/activate
cd repro
briefcase update android -d && briefcase build android && briefcase run android -d @beePhone
```

Clicking the button to change the label text seems to work fine.
