from django.db import models

PROVINCIA = (('01', 'Alava'), ('02', 'Albacete'), ('03', 'Alicante'),
             ('04', 'Almería'), ('05', 'Ávila'), ('06', 'Badajoz'),
             ('07', 'Baleares'), ('08', 'Barcelona'), ('09', 'Burgos'),
             ('10', 'Cáceres'), ('11', 'Cádiz'), ('12', 'Castellón'),
             ('13', 'Ciudad Real'), ('14', 'Córdoba'), ('15', 'A Coruña'),
             ('16', 'Cuenca'), ('17', 'Girona'), ('18', 'Granada'),
             ('19', 'Guadalajara'), ('20', 'Guipúzcoa'), ('21', 'Huelva'),
             ('22', 'Huesca'), ('24', 'Jaén'), ('24', 'León'),
             ('25', 'Lleida'), ('26', 'La Rioja'), ('27', 'Lugo'),
             ('28', 'Madrid'), ('29', 'Málaga'), ('30', 'Murcia'),
             ('31', 'Navarra'), ('32', 'Ourense'), ('33', 'Asturias'),
             ('34', 'Palencia'), ('35', 'Las Palmas'), ('36', 'Pontevedra'),
             ('37', 'Salamanca'), ('38', 'Santa Cruz de Tenerife'), ('39', 'Cantabria (Santander)'),
             ('40', 'Segovia'), ('41', 'Sevilla'), ('42', 'Soria'),
             ('43', 'Tarragona'), ('44', 'Teruel'), ('45', 'Toledo'),
             ('46', 'Valencia'), ('47', 'Valladolid'), ('48', 'Vizcaya'),
             ('49', 'Zamora'), ('50', 'Zaragoza'), ('51', 'Ceuta'),
             ('52', 'Melilla'),
             )

MUNICIPIO = (('079', 'Madrid'),
             )

ESTACION = ((2, 'Glta. de Carlos V'),
            (3, 'Pza. del Carmen'),
            (35, 'Pza. del Carmen'),
            (4, 'Pza. de España'),
            (5, 'Barrio del Pilar'),
            (39, 'Barrio del Pilar'),
            (6, 'Pza. Dr. Marañón'),
            (7, 'Pza. M. de Salamanca'),
            (8, 'Escuelas Aguirre'),
            (9, 'Pza. Luca de Tena'),
            (10, 'Cuatro Caminos'),
            (38, 'Cuatro Caminos'),
            (11, 'Av. Ramón y Cajal'),
            (12, 'Pza. Manuel Becerra'),
            (13, 'Vallecas'),
            (40, 'Vallecas'),
            (14, 'Pza. Fdez. Ladreda'),
            (15, 'Pza. Castilla'),
            (16, 'Arturo Soria'),
            (17, 'Villaverde Alto'),
            (18, 'C/ Farolillo'),
            (19, 'Huerta Castañeda'),
            (20, 'Moratalaz'),
            (36, 'Moratalaz'),
            (21, 'Pza. Cristo Rey'),
            (22, 'Pº. Pontones'),
            (23, 'Final C/ Alcalá'),
            (24, 'Casa de Campo'),
            (25, 'Santa Eugenia'),
            (26, 'Urb. Embajada (Barajas)'),
            (27, 'Barajas'),
            (47, 'Méndez Álvaro'),
            (48, 'Pº. Castellana'),
            (49, 'Retiro'),
            (50, 'Pza. Castilla'),
            (54, 'Ensanche Vallecas'),
            (55, 'Urb. Embajada (Barajas)'),
            (56, 'Plaza Elíptica'),
            (57, 'Sanchinarro'),
            (58, 'El Pardo'),
            (59, 'Parque Juan Carlos I'),
            (86, 'Tres Olivos'),
            (60, 'Tres Olivos'),
            )


class Estacion(models.Model):
    provincia = models.CharField(max_length=2, choices=PROVINCIA, default='28')
    municipio = models.CharField(max_length=3, choices=MUNICIPIO, default='079')
    estacion = models.IntegerField(choices=ESTACION)

    def __str__(self):
        return f'{str(self.provincia)} - {str(self.municipio)} - {str(self.estacion)}'


class DiaMedicion(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    ano = models.IntegerField()
    mes = models.IntegerField()
    dia = models.IntegerField()
    magnitud = models.IntegerField()
    punto_muestreo = models.CharField(max_length=30)

    def __str__(self):
        return '{}_{}_{}'.format(str(self.ano), str(self.mes), str(self.dia))

class HoraMedicion(models.Model):
    dia_medicion = models.ForeignKey(DiaMedicion, on_delete=models.CASCADE)
    hora = models.IntegerField()
    cantidad = models.FloatField()
    validacion = models.CharField(max_length=3)

    def __str__(self):
        return f'{str(self.dia_medicion)} - {str(self.hora)}'
