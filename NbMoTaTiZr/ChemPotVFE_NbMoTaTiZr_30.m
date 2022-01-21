clear, clc
% This script parses the VASP swap outputs
% --------------------------------------
datamatrix = importdata('swapdata.dat')
vacmatrix = importdata('vacdata.dat')
% --------------------------------------
N = 30
C = 5
% Cantor Alloy 20-atom SQS Epristine = -163.63523163
Epristine = -315.5119008
% --------------------------------------
% ----- Reference Energies -------------
% --------------------------------------
%ErefMn = -9.418614838
ErefNb = -10.3612882
ErefMo = -11.46799539
ErefZr = -8.807683205
%ErefCr = -9.979455835
%ErefW  = -13.52034736
ErefTi = -8.03647692
ErefTa = -12.32091286
%ErefV  = -9.38685391
%ErefFe = -8.62838345
%ErefNi = -5.82862595
%ErefCo = -7.4161202
% --------------------------------------
mu = []
VFE = []
for site = 1:N
    swapmatrix = zeros(7,7)
    % ---------------------------------
    swapmatrix(6,1) = 1
    swapmatrix(6,2) = 1
    swapmatrix(6,3) = 1
    swapmatrix(6,4) = 1
    swapmatrix(6,5) = 1
    swapmatrix(6,7) = Epristine/(N/C)
    % ---------------------------------
    for j = 1:length(datamatrix)
        if datamatrix(j,1) == site
            type = datamatrix(j,2)
            swap = datamatrix(j,3)
            E = datamatrix(j,4)
            swapmatrix(swap,type) = -1
            swapmatrix(swap,swap) = 1
            swapmatrix(swap,7) = E - Epristine
            swapmatrix(7,type) = -1
            swapmatrix(7,6) = 1 
            swapmatrix(7,7) = vacmatrix(site,2) - Epristine
        end
    end
    
    
    % ------------------------------
    mumatrix = rref(swapmatrix)
    % ------------------------------
    mu1(site)  = mumatrix(1,7)
    mu2(site)  = mumatrix(2,7)
    mu3(site)  = mumatrix(3,7)
    mu4(site)  = mumatrix(4,7)
    mu5(site)  = mumatrix(5,7)
    muVa(site) = mumatrix(6,7)
    
    VFE(site) = muVa(site)
    
    DMuMix(site,1) = mu1(site) - ErefNb
    DMuMix(site,2) = mu2(site) - ErefZr
    DMuMix(site,3) = mu3(site) - ErefTa
    DMuMix(site,4) = mu4(site) - ErefMo
    DMuMix(site,5) = mu5(site) - ErefTi
end



hold on 
%Dmu_mix_1 = mu1 - ErefNb
%Dmu_mix_2 = mu2 - ErefZr
%Dmu_mix_3 = mu3 - ErefTa
%Dmu_mix_4 = mu4 - ErefMo
%Dmu_mix_5 = mu5 - ErefTi



writematrix(DMuMix(:,1),'Delta_mu_mix_Nb.dat')
writematrix(DMuMix(:,2),'Delta_mu_mix_Zr.dat')
writematrix(DMuMix(:,3),'Delta_mu_mix_Ta.dat')
writematrix(DMuMix(:,4),'Delta_mu_mix_Mo.dat')
writematrix(DMuMix(:,5),'Delta_mu_mix_Ti.dat')
writematrix(VFE, 'NbMoTaTiZr-VFE.dat')
%

hold on
histogram(DMuMix(:,1))
histogram(DMuMix(:,2))
histogram(DMuMix(:,3))
histogram(DMuMix(:,4))
histogram(DMuMix(:,5))
legend('Nb','Zr','Ta','Mo','Ti')
xlabel('\Delta \mu^{mix} [eV/atom]')
ylabel('a.u.')
hold off



%hold on
%histogram(muVa)
%xlabel('Vacancy Formation Energy [eV]')
%ylabel('Counts')
%hold off


