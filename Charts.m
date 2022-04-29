% Agents = 100
cycles = [0 25 50 75 100 125 150 175 200 225 250 275 300];
veto = [0 2484 3125 3435 3916 4306 4773 5217 5621 5649 6013 5916 6331];
borda = [0 2606 2922 3368 3993 4140 4746 5295 5503 5871 5865 6014 6059];
plurality = [0 2642 3284 3682 3926 4754 5287 5395 5424 6274 6745 6011 6303];
figure(1);
plot(cycles,veto,cycles,borda,cycles,plurality)
grid on;
title('Figure 1: Affects of Varying Cycles (100 Agents)');
xlabel('Cycles');
ylabel('Utility');
legend({'veto','borda','plurality'},"Location","SouthEast");

% Cycles = 200
cycles = [0 100 200 300 400 500 600 700 800 900];
veto = [0 5342 7580 10036 12203 14315 16565 18374 20926 23032];
borda = [0 5787 7836 9690 12116 13952 16519 18923 20527 22847];
plurality = [0 5923 7935 11381 13817 16783 20761 23681 27690 29551];
figure(2);
plot(cycles,veto,cycles,borda,cycles,plurality);
grid on;
title('Figure 2: Affects of Varying Agents (200 Cycles)');
xlabel('Agents');
ylabel('Utility');
legend({'veto','borda','plurality'},"Location","SouthEast");