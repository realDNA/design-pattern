from adaptee import VeggieBurgur
from adaptor import VeggieBurgurAdaptor
from director import serveHamburgur

viggieBurgur = VeggieBurgur()
veggieBurgurAdaptor = VeggieBurgurAdaptor(viggieBurgur)
print("serving veggie burgur using adaptor")
serveHamburgur(veggieBurgurAdaptor)
