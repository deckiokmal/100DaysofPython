print(
    """
    dMMMMb  dMMMMMP .aMMMb  dMP dMP dMP             
   dMP VMP dMP     dMP"VMP dMP.dMP amr              
  dMP dMP dMMMP   dMP     dMMMMK" dMP               
 dMP.aMP dMP     dMP.aMP dMP"AMF dMP                
dMMMMP" dMMMMMP  VMMMP" dMP dMP dMP                 
                                                    
   .aMMMb  dMP dMP dMMMMMMMMb .aMMMb  dMP           
  dMP"dMP dMP.dMP dMP"dMP"dMPdMP"dMP dMP            
 dMP dMP dMMMMK" dMP dMP dMPdMMMMMP dMP             
dMP.aMP dMP"AMF dMP dMP dMPdMP dMP dMP              
VMMMP" dMP dMP dMP dMP dMPdMP dMP dMMMMMP           
                                                    
    dMMMMb  dMP dMP dMMMMMMP dMP dMP .aMMMb  dMMMMb 
   dMP.dMP dMP.dMP    dMP   dMP dMP dMP"dMP dMP dMP 
  dMMMMP"  VMMMMP    dMP   dMMMMMP dMP dMP dMP dMP  
 dMP     dA .dMP    dMP   dMP dMP dMP.aMP dMP dMP   
dMP      VMMMP"    dMP   dMP dMP  VMMMP" dMP dMP    
                                                    
    """
)
print("==============================================")
print("Wellcome to the game.\n")
print("Your mission is to find the Treasure!\n")

step1 = input('Kemana anda akan pergi? "kiri" atau "kanan"\n')

if step1.lower() == "kiri":
    step2 = input(
        'Ok!. Saat ini anda berada di pinggiran sungai dan harus menyeberanginya. Pilih "tunggu" untuk menunggu kapal atau "berenang".\n'
    )
    if step2.lower() == "tunggu":
        step3 = input(
            'Ok!. Saat ini anda berada di depan tiga pintu. Pilih pintu: "Merah", "Kuning", "Hijau".\n'
        )
        if step3.lower() == "kuning":
            print("Congrats! You got this.")

        else:
            print("Game over!")
    else:
        print("Game over!")
else:
    print("Game over!")
