
clear;

Data = csvread('1PF_data1976-01-13_1993-04-09.csv');

%Date calculations
Y = Data(:,2);
M = Data(:,3);
D = Data(:,4);


date = datenum(Y,M,D);  %Day after christ
date2 = Y + (date-datenum(Y,1,1))./(datenum(Y+1,1,1)-datenum(Y,1,1));   %Fractional Year


%Plotting Northern hemisphere
figure(1)
plot(date2,Data(:,11),'b.')
xlim([1976 1993.5])
ylim([-1 1]*3e22)
xlabel('Year')
ylabel('Total Signed Flux (Mx)')
title('North Pole (above 65^o)')

%Plotting Southern hemisphere
figure(2)
plot(date2,Data(:,20),'r.')
xlim([1976 1993.5])
ylim([-1 1]*3e22)
xlabel('Year')
ylabel('Total Signed Flux (Mx)')
title('South Pole (above 65^o)')



