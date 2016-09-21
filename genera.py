from faker import Factory

def generaNomiCasuali():

    fake = Factory.create('it_IT')


    for index in range(0, 100):
        nome = []
        nome.append(fake.first_name())
        nome.append(fake.last_name())
        nomi.append(nome)

def stampa():
    for index in range(0,20):
        print (nomi[index])



nomi = [] #lista che contiene tutti i nomi casuali
generaNomiCasuali()
