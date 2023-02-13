from ..models import Measurement
from ..models import Variable
def get_measurements():
    measurements= Measurement.objects.all()
    return measurements

def get_measurement(mes_pk):
    measurement= Measurement.objects.get(pk= mes_pk)
    return measurement

def update_measurement(mes_pk, new_meas):
    measurement = get_measurement(mes_pk)
    measurement.variable = new_meas["variable"]
    measurement.value = new_meas["value"]
    measurement.unit  = new_meas["unit"]
    measurement.place = new_meas["place"]
    measurement.dateTime = new_meas["dateTime"]
    measurement.save()
    return measurement

def create_measurement(measure):
    variable = Variable.objects.get(pk = measure["variable"])
    measurement = Measurement(variable=variable, value = measure["value"], unit = measure["unit"], place=measure["place"], dateTime = measure["dateTime"])
    measurement.save()
    return measurement

def delete_measurement(mes_pk):
    measurement = get_measurement(mes_pk)
    measurement.delete()
    return measurement
    