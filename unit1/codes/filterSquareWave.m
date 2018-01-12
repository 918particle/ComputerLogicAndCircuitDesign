clear; home
pkg load control
pkg load signal
f = 1.0;
fs = 1000.0; %sampling frequency
fc = fs/2.0; %critical frequency
fcut_low = 2.0; %cutoff frequency
fcut_high = 0.01; %cutoff frequency
dt = 1.0/fs;
T_max = 2.0;
n = 1.0e4;
t = linspace(0,T_max,n);
s = square(2.0*pi*f*t);
[b a] = butter(1,fcut_low/fc,'low');
[d c] = butter(1,fcut_high/fc,'high');
sf = filter(b,a,filter(d,c,s));

%Plotting
hold on;
grid on;
axisVector = [-0.5 3.5 -0.5 5.5];
linew = 3;
linec = 'red';
linec2 = 'blue';
linec3 = 'black';
fontname = 'Courier';
fontsize = 20.0;
plot(t,(s+1.0)*5.0/2.0,'linewidth',linew,'color',linec);
plot(t,(sf+1.0)*5.0/2.0,'linewidth',linew,'color',linec2);
plot([0 T_max],[5.0 5.0],'--','color',linec3,'linewidth',linew);
plot([0 T_max],[3.5 3.5],'--','color',linec3,'linewidth',linew);
plot([0 T_max],[1.5 1.5],'--','color',linec3,'linewidth',linew);
plot([0 T_max],[0.0 0.0],'--','color',linec3,'linewidth',linew);
axis(axisVector);
xlabel('Time (microseconds)','fontname',fontname,'fontsize',fontsize);
ylabel('Amplitude (V)','fontname',fontname,'fontsize',fontsize);
set(gca,'fontname',fontname,'fontsize',fontsize);
legend('Perfect','Filtered','HIGHMAX','HIGHMIN','LOWMAX','LOWMIN');
print -dpdf 'January8_plot1.pdf'
