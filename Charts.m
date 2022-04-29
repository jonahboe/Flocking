% Agents = 100
cycles = [0 25 50 75 100 125 150 175 200 225 250 275 300];
veto = [0 2484 3125 3435 3916 4306 4773 5217 5621 5649 6013 5916 6331];
borda = [0 2606 2922 3368 3993 4140 4746 5295 5503 5871 5865 6014 6059];
plurality = [0 2642 3284 3682 3926 4754 5287 5395 5424 6274 6745 6011 6303];
plot(cycles,veto,cycles,borda,cycles,plurality)
grid on;
legend({'veto','borda','plurality'},"Location","SouthEast")

% Cycles = 200
cycles = [0 100 200 300 400 500 600 700 800 900 1000];
veto = [0 5342 ];
borda = [0 ];
plurality = [0 ];
plot(cycles,veto,cycles,borda,cycles,plurality)
grid on;
legend({'veto','borda','plurality'},"Location","SouthEast")