
clear;

% Data = csvread('1PF_data1976-01-13_1993-04-09.csv');
Data = csvread('imb85_PF_1976-01-13_1993-04-09.csv');




%Date calculations
Y = Data(:,2);
M = Data(:,3);
D = Data(:,4);


date = datenum(Y,M,D);  %Day after christ
date2 = Y + (date-datenum(Y,1,1))./(datenum(Y+1,1,1)-datenum(Y,1,1));   %Fractional Year




ClrTh = 2.5e20;
inxNg = find(Data(:,16)>ClrTh);
inxNs = find(Data(:,16)<=ClrTh);

%Plotting Northern hemisphere
figure(3)
plot(Data(inxNs,16),Data(inxNs,11),'b.')
hold on
plot(Data(inxNg,16),Data(inxNg,11),'m.')
hold off
% xlim([1976 1993.5])
% ylim([-1 1]*3e22)
xlabel('Max abs Unsigned pixel (Mx)')
ylabel('Total Signed Flux (Mx)')
title('North Pole (above 65^o)')


inxSg = find(Data(:,26)>ClrTh);
inxSs = find(Data(:,26)<=ClrTh);
%Plotting Southern hemisphere
figure(4)
plot(Data(:,26),Data(:,21),'r.')
hold on
plot(Data(inxSg,26),Data(inxSg,21),'g.')
hold off
% xlim([1976 1993.5])
% ylim([-1 1]*3e22)
xlabel('Max abs Unsigned pixel (Mx)')
ylabel('Total Signed Flux (Mx)')
title('South Pole (above 65^o)')




%Plotting Northern hemisphere
figure(1)
plot(date2(inxNs),Data(inxNs,11),'b.')
hold on
plot(date2(inxNg),Data(inxNg,11),'m.')
hold off
xlim([1976 1993.5])
% ylim([-1 1]*3e22)
xlabel('Year')
ylabel('Total Signed Flux (Mx)')
title('North Pole (above 65^o)')

%Plotting Southern hemisphere
figure(2)
plot(date2,Data(:,21),'r.')
hold on
plot(date2(inxSg),Data(inxSg,21),'g.')
hold off
xlim([1976 1993.5])
% ylim([-1 1]*3e22)
xlabel('Year')
ylabel('Total Signed Flux (Mx)')
title('South Pole (above 65^o)')



