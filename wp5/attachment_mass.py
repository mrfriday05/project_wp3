
#Attachment mass
Fx=0.0
Fy=0.0
Fz=0.0
R=Fx+Fy+Fz 
Fp=0.0
r=0
na=0 #nr of attachm.




#Sandwich panel mass
rhon=48.2
rhof=1611
tf=0.00019805
tn=0.015
mAn=rhon*tn #mass/area for Nomex
mAf=rhof*tf*4 #mass/area for 4 layers of fabric

ns=1 #number of sanwich panels
l=1.5
mass_sandwich=(mAn*l**2+mAf*l**2)*ns


#Total mass attachmetns and sandwich
m=mass_sandwich+mass_attachments
print(m)