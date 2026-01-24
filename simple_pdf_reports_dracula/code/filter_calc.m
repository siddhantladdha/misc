% Author: Siddhant Laddha
clear all;
clc;
% Maximally flat low pass filter prototype.
% Values from Table 8.3 Page 404
% Microwave Engineering Fourth Edition, David M. Pozar
% Gx: where x order
% Load and source is g = 1
G1 = [2];
G2 = [1.4142 1.4142];
G3 = [1 2 1];
G4 = [0.7654 1.8478 1.8478 0.7654];
G5 =  [0.6180 1.6180 2.0000 1.6180 0.6180];
% select the order to get values for
G = G3;
Ro = 50; % scaling impedances.
fo = 17.8e9;
three_dB = 2.8e9;
delta = three_dB/fo;    
omega_o = 2*pi*fo;
% Transform Lumped lowpass to lumped bandpass. See figure in report.
% Shunt capacitance becomes parallel LC 
% Ck --> Lk_ = delta/(omega_o*Ck); Ck_ = Ck/(delta*omega_o);
% Series Inductance becomes series LC.
% Lk -> Lk_ = Lk/(omega_o*delta); Ck_ = delta/(omega_o*Lk);
% Impedance Transformations.
C1 = G(1)/Ro;
L2 = G(2)*Ro;
C3 = G(3)/Ro;
%L4 = G(4)*Ro;
% Lowpass to Bandpass Transformations
% C1 - Parallel LC 
Lk_1 = delta/(omega_o*C1)
Ck_1 = C1/(delta*omega_o)
% L2 - Series LC
Lk_2 = L2/(omega_o*delta)
Ck_2 = delta/(omega_o*L2)
% C3 - Parallel LC
Lk_3 = delta/(omega_o*C3)
Ck_3 = C3/(delta*omega_o)
% L4 - Series LC
%Lk_4 = L4/(omega_o*delta)
%Ck_4 = delta/(omega_o*L4)

% Transform Lowpass to Bandpass and scale for impedance.
% This gives L and C values for use with Impedance inverters
% using QWT.
C = (G./(omega_o.*delta))./Ro
L = (delta./(omega_o.*G)).*Ro

% transform the LC tank to short circuit stub of 90 degrees Tx Line
Z_tx_line = (pi/4)*sqrt(L./C)
% transform the LC tank to open circuit stub of 90 degrees Tx line
% error in calculation hence going ahead with short circuit stubs for now.