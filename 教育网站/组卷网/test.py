
from numpy import *
x=0
y=0
c=-1.806e-4
s=20.046*(pow(288.34-0.00586*y,0.5))
v=777.7*1.414
Ma=v/s
g0=9.8    #单位是m/s²
r0=6356.765   #单位是千米（北纬45°32′33″）
#以下为参与运算的五个初始值
def f(v_x,v_y,y_k,x_k,time):     #y_k表示y坐标，v_x表示水平速度，v_y表示竖直速度，x_k表示x坐标,time表示时间（这些只是变量） 
    k1=v_x
    k2=v_x+time/2*k1
    k3=v_x+time/2*k2
    k4=v_x+time*k3
    
    ky1=v_y
    ky2=v_y+time/2*ky1
    ky3=v_y+time/2*ky2
    ky4=v_y+time*ky3
    
    kv1=c*(pow(1-2.1904e-5*y_k,4.4))*(pow((pow(v_x,2)+(pow(v_y,2))),0.5))*v_x*Ma
    kvy1=c*(pow(1-2.1904e-5*y_k,4.4))*(pow((pow(v_x,2)+(pow(v_y,2))),0.5))*v_y*Ma-g0*(1-2*y_k/r0)
    kvy2=c*(pow(1-2.1904e-5*(y_k+time/2*ky1),4.4))*(pow((pow(v_x+time/2*kv1,2))+(pow(v_y+time/2*kvy1,2)),0.5))*(v_y+time/2*kvy1)*Ma-g0*(1-2*(y_k+time/2*ky1)/r0)
    kv2=c*(pow(1-2.1904e-5*(y_k+time/2*ky1),4.4))*(pow((pow(v_x+time/2*kv1,2))+(pow(v_y+time/2*kvy1,2)),0.5))*(v_x+time/2*kv1)*Ma
    kvy3=c*(pow(1-2.1904e-5*(y_k+time/2*ky2),4.4))*(pow((pow(v_x+time/2*kv2,2))+(pow(v_y+time/2*kvy2,2)),0.5))*(v_y+time/2*kvy2)*Ma-g0*(1-2*(y_k+time/2*ky2)/r0)
    kv3=c*(pow(1-2.1904e-5*(y_k+time/2*ky2),4.4))*(pow((pow(v_x+time/2*kv2,2))+(pow(v_y+time/2*kvy2,2)),0.5))*(v_x+time/2*kv2)*Ma
    kvy4=c*(pow(1-2.1904e-5*(y_k+time/2*ky3),4.4))*(pow((pow(v_x+time*kv3,2))+(pow(v_y+time*kvy3,2)),0.5))*(v_y+time*kvy3)*Ma-g0*(1-2*(y_k+time*ky3)/r0)
    kv4=c*(pow(1-2.1904e-5*(y_k+time/2*ky3),4.4))*(pow((pow(v_x+time*kv3,2))+(pow(v_y+time*kvy3,2)),0.5))*(v_x+time*kv3)*Ma

    xk_1=x_k+time/6*(k1+2*k2+2*k3+k4)
    
    yk_1=y_k+time/6*(ky1+2*ky2+2*ky3+ky4)

    vxk_1=v_x+time/6*(kv1+2*kv2+2*kv3+kv4)
    
    vyk_1=v_y+time/6*(kvy1+2*kvy2+2*kvy3+kvy4)

    return  xk_1,yk_1,vxk_1,vyk_1,time    #返回最终结果

xk=0
yk=0     #原点位置
vyk=777.7   
vxk=777.7#初始的xy方向上的速度
h=1

sx=xk
sy=yk
vx=vxk
vy=vyk
t=h

while True:           
    xk_1,yk_1,vxk_1,vyk_1,time=f(vx,vy,sy,sx,t)
    vx,vy,sy,sx,t=xk_1,yk_1,vxk_1,vyk_1,time
    print(xk_1,yk_1,vxk_1,vyk_1,time)
    if yk_1>0:
        t=t+1
    else:
        print(yk_1)  
        break    


