a=int(input('Nhap he so a: '))
b=int(input('Nhap he so b: '))
c=int(input('Nhap he so c: '))

if a==0:
    if b==0:
        print('Phuong trinh vo nghiem')
    else:
        print('Phuong trinh co mot nghiem duy nhat x= ',(-c/b))
    return;
denta=b*b-4*a*c
if denta>0:
    x1=(float)((-b+math.sqrt(denta))/(2*a))
    x2=(float)((-b+math.sqrt(denta))/(2*a))
    print('Phuong trinh co hai nghiem phan biet x1=',x1,'va x2=',x2)
elif(denta==0):
    x1=(-b/(2*a))
    print('Phuong trinh co nghiem kep: x1=x2=',x1)
else:
    print('Phuong trinh vo nghiem')
