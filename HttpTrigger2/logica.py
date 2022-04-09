import random
def random_cor():
    
    total_bolinhas=0
    azul=0
    verde=0
    vermelha=0
    sequencia_cor=[]
    max=3
    cor_ganhadora=''
    lista_numero=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    for n in range(0,30):
        total_bolinhas+=1
        sorteia_cor=random.randint(0,len(lista_numero))
        if sorteia_cor >=1 and sorteia_cor<10:

            sequencia_cor.append('verde')
            verde+=1            
        elif sorteia_cor >10 and sorteia_cor<=20:
            sequencia_cor.append('Azul')           
            azul+=1

        elif sorteia_cor >20 and sorteia_cor<=30:
            sequencia_cor.append('vermelho')
            vermelha+=1
        if verde==max:
                cor_ganhadora='verde'
                break
        if azul==max:
                cor_ganhadora='azul'
                break
        if vermelha==max:
                cor_ganhadora='vermelha'
                break
    data={
        'total_bolinhas':total_bolinhas,
        'cor_ganhadora':cor_ganhadora,
        'sequencia_cor':sequencia_cor
    }
    return data



