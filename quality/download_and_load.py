from urllib import request
import zipfile, io, csv
import datetime
from django.apps import apps

def download_and_load(url):
    Estacion = apps.get_model('quality', 'Estacion')
    DiaMedicion = apps.get_model('quality', 'DiaMedicion')
    HoraMedicion = apps.get_model('quality', 'HoraMedicion')

    response = request.urlopen(url)

    with zipfile.ZipFile(io.BytesIO(response.read())) as thezip:
        for zipinfo in thezip.infolist():
            if '.csv' not in zipinfo.filename:
                continue

            csv_file = io.StringIO(thezip.read(zipinfo).decode())
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                if row['MAGNITUD'] not in ['8', '08', '008']:
                    continue

                fields = ['provincia', 'municipio', 'estacion']
                dictio = {x: row.pop(x.upper()) for x in fields}
                estacion, created = Estacion.objects.get_or_create(**dictio)

                fields = ['magnitud', 'punto_muestreo', 'ano', 'mes', 'dia']
                dictio = {x: row.pop(x.upper()) for x in fields}
                dictio['estacion'] = estacion

                dia_medicion, created = DiaMedicion.objects.get_or_create(**dictio)

                for index in range(1,25):
                    ind = f'{index:02}'
                    dictio = {'cantidad' if 'H' in k else 'validacion': v for k, v in\
                              row.items() if ind in k}
                    dictio['hora'] = index
                    dictio['dia_medicion'] = dia_medicion
                    HoraMedicion.objects.get_or_create(**dictio)
