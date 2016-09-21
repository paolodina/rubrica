from django.db import models
from genera import *


#Persona.objects.create('Anita', 'Rossi')
#Persona.objects.create('Rossi', 'Anita')
#Persona.objects.create(cognome='Rossi', nome='Anita')


class Persona(models.Model):
    nome = models.CharField(max_length = 10)
    cognome = models.CharField(max_length = 20)
#    telefono = models.CharField(max_length = 10)
    #indirizzo = models.CharField(max_length = 30)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Persone'


    def __str__(self):
        #return "{}".format(self.nominativo)
        return self.nome + " " + self.cognome


    def stampa(self):
        print ("Nome: " + self.nome)
        print ("Cognome: " + self.cognome)
#        print ("Telefono: " + self.telefono)
#        print ("Indirizzo: " + self.indirizzo)
